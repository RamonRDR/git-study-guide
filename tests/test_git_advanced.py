"""Bounded advanced Git and internals tests in owned temporary repositories."""
import os
from pathlib import Path
import subprocess
import tempfile
import unittest


class GitAdvancedTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        root = Path(self.temp.name)
        self.repo = root / "repo"
        home = root / "home"
        template = root / "template"
        for folder in (self.repo, home, template):
            folder.mkdir()
        config = root / "gitconfig"
        config.touch()
        self.env = {k: v for k, v in os.environ.items()
                    if not k.upper().startswith("GIT_")}
        self.env.update(HOME=str(home), USERPROFILE=str(home),
                        GIT_CONFIG_GLOBAL=str(config), GIT_CONFIG_NOSYSTEM="1",
                        GIT_TEMPLATE_DIR=str(template), GIT_TERMINAL_PROMPT="0",
                        GIT_CONFIG_COUNT="0", GIT_ALLOW_PROTOCOL="file")
        self.git("init", "--initial-branch=main")
        for key, value in (("user.name", "Study Guide Example"),
                           ("user.email", "learner@example.invalid"),
                           ("commit.gpgsign", "false"), ("tag.gpgsign", "false"),
                           ("core.autocrlf", "false")):
            self.git("config", "--local", key, value)
        self.base = self.commit("ok")
        self.middle = self.commit("reviewed")
        self.tip = self.commit("bad")
        self.assertEqual(self.git("remote"), "")

    def run_git(self, *args):
        return subprocess.run(["git", *args], cwd=self.repo, env=self.env,
                              capture_output=True, text=True, timeout=30)

    def git(self, *args):
        result = self.run_git(*args)
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout.strip()

    def commit(self, text):
        (self.repo / "note.txt").write_bytes((text + "\n").encode("ascii"))
        self.git("add", "--", "note.txt")
        for key in ("GIT_AUTHOR_IDENT", "GIT_COMMITTER_IDENT"):
            self.assertTrue(self.git("var", key).startswith(
                "Study Guide Example <learner@example.invalid> "))
        self.git("commit", "-m", "docs: " + text)
        return self.git("rev-parse", "HEAD")

    def test_bisect_finds_first_bad(self):
        self.git("bisect", "start", self.tip, self.base)
        self.assertEqual(self.git("rev-parse", "HEAD"), self.middle)
        self.git("bisect", "good")
        self.assertEqual(self.git("rev-parse", "refs/bisect/bad"), self.tip)
        self.git("bisect", "reset")
        self.assertEqual(self.git("symbolic-ref", "--short", "HEAD"), "main")
        self.assertEqual(self.git("rev-parse", "HEAD"), self.tip)

    def test_worktree_uses_separate_checkout(self):
        target = str(self.repo.parent / "review")
        self.git("worktree", "add", "-b", "review", target, self.middle)
        self.assertEqual(self.git("-C", target, "rev-parse", "HEAD"), self.middle)
        self.assertEqual(self.git("rev-parse", "HEAD"), self.tip)
        self.assertEqual(self.git("-C", target, "status", "--porcelain"), "")
        self.git("worktree", "remove", target)
        self.assertFalse(Path(target).exists())

    def test_sparse_checkout_preserves_tree(self):
        folder = self.repo / "docs"
        folder.mkdir()
        (folder / "guide.txt").write_bytes(b"guide\n")
        source = self.repo / "src"
        source.mkdir()
        (source / "state.txt").write_bytes(b"state\n")
        self.git("add", "--", "docs/guide.txt", "src/state.txt")
        self.git("commit", "-m", "docs: guide")
        before = self.git("rev-parse", "HEAD")
        self.git("sparse-checkout", "init", "--cone")
        self.git("sparse-checkout", "set", "docs")
        self.assertEqual(self.git("config", "--bool", "--get", "core.sparseCheckoutCone"), "true")
        self.assertTrue((folder / "guide.txt").exists())
        self.assertFalse((source / "state.txt").exists())
        self.assertIn("src/state.txt", self.git("ls-tree", "-r", "--name-only", "HEAD"))
        self.assertEqual(self.git("rev-parse", "HEAD"), before)
        self.git("sparse-checkout", "disable")
        self.assertTrue((source / "state.txt").exists())
        self.assertEqual(self.git("status", "--porcelain"), "")

    def test_shallow_clone_and_unshallow(self):
        target = str(self.repo.parent / "shallow")
        self.git("clone", "--no-local", "--depth", "1", str(self.repo), target)
        self.assertEqual(self.git("-C", target, "rev-parse", "--is-shallow-repository"), "true")
        self.assertEqual(self.git("-C", target, "rev-list", "--count", "HEAD"), "1")
        self.git("-C", target, "fetch", "--unshallow")
        self.assertEqual(self.git("-C", target, "rev-list", "--count", "HEAD"), "3")

    def test_bundle_recovers_tip(self):
        bundle = str(self.repo.parent / "history.bundle")
        target = str(self.repo.parent / "recovered")
        self.git("bundle", "create", bundle, "main")
        self.git("bundle", "verify", bundle)
        self.git("clone", "-b", "main", bundle, target)
        self.assertEqual(self.git("-C", target, "rev-parse", "HEAD"), self.tip)

    def test_object_types_and_index_tree(self):
        tree = self.git("rev-parse", "HEAD^{tree}")
        blob = self.git("rev-parse", "HEAD:note.txt")
        self.assertEqual(self.git("cat-file", "-t", self.tip), "commit")
        self.assertEqual(self.git("cat-file", "-t", tree), "tree")
        self.assertEqual(self.git("cat-file", "-t", blob), "blob")
        self.assertEqual(self.git("cat-file", "-p", blob), "bad")
        self.assertEqual(self.git("hash-object", "--no-filters", "note.txt"), blob)
        (self.repo / "note.txt").write_bytes(b"new\n")
        self.git("add", "--", "note.txt")
        self.assertNotEqual(self.git("write-tree"), tree)
        self.assertEqual(self.git("rev-parse", "HEAD"), self.tip)
        self.git("restore", "--staged", "--worktree", "--", "note.txt")
        self.assertEqual(self.git("status", "--porcelain"), "")

    def test_repack_preserves_identity(self):
        blob = self.git("rev-parse", "HEAD:note.txt")
        self.git("repack", "-a")
        self.assertEqual(self.git("rev-parse", "HEAD"), self.tip)
        self.assertEqual(self.git("rev-parse", "HEAD:note.txt"), blob)
        self.assertEqual(self.git("cat-file", "-p", blob), "bad")
        self.assertEqual(self.git("status", "--porcelain"), "")

    def test_rerere_reuses_resolution_without_staging(self):
        self.git("config", "--local", "rerere.enabled", "true")
        self.git("config", "--local", "rerere.autoupdate", "false")
        self.git("switch", "-c", "side")
        side = self.commit("side")
        self.git("switch", "main")
        before = self.commit("main")
        self.assertNotEqual(self.run_git("merge", "side").returncode, 0)
        (self.repo / "note.txt").write_bytes(b"resolved\n")
        self.git("rerere")
        self.git("add", "--", "note.txt")
        self.git("commit", "-m", "merge: resolved")
        self.git("switch", "-c", "repeat", before)
        self.assertNotEqual(self.run_git("merge", side).returncode, 0)
        self.assertEqual((self.repo / "note.txt").read_bytes(), b"resolved\n")
        self.assertTrue(self.git("ls-files", "-u", "--", "note.txt"))
        self.git("merge", "--abort")

if __name__ == "__main__":
    unittest.main()
