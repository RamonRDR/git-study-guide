"""Undo and recovery tests using only isolated disposable Git repositories."""
import os
from pathlib import Path
import subprocess
import tempfile
import unittest


class GitRecoveryTest(unittest.TestCase):
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
        for key, val in (("user.name", "Study Guide Example"),
                         ("user.email", "learner@example.invalid"),
                         ("commit.gpgsign", "false"), ("core.autocrlf", "false"),
                         ("core.logAllRefUpdates", "true"), ("gc.auto", "0"),
                         ("rerere.enabled", "false")):
            self.git("config", "--local", key, val)
        self.base = self.commit("note.txt", "practice")
        self.assertEqual(self.git("remote"), "")

    def run_git(self, *args):
        return subprocess.run(["git", *args], cwd=self.repo, env=self.env,
                              capture_output=True, text=True, timeout=30)

    def git(self, *args):
        result = self.run_git(*args)
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout.strip()

    def ref(self, ref="HEAD"):
        return self.git("rev-parse", ref)

    def write(self, file, text):
        (self.repo / file).write_bytes((text + "\n").encode("ascii"))

    def identity(self):
        for key in ("GIT_AUTHOR_IDENT", "GIT_COMMITTER_IDENT"):
            self.assertTrue(self.git("var", key).startswith(
                "Study Guide Example <learner@example.invalid> "))

    def commit(self, file, text):
        self.write(file, text)
        self.git("add", "--", file)
        self.identity()
        self.git("commit", "-m", "docs: " + text)
        return self.ref()

    def disk(self, file="note.txt"):
        return (self.repo / file).read_bytes()

    def clean(self):
        self.assertEqual(self.git("status", "--porcelain=v1"), "")

    def test_restore_worktree_and_unstage(self):
        self.write("note.txt", "staged draft")
        self.git("add", "--", "note.txt")
        self.write("note.txt", "working draft")
        self.git("restore", "--", "note.txt")
        self.assertEqual(self.disk(), b"staged draft\n")
        self.assertEqual(self.git("show", ":note.txt"), "staged draft")
        self.git("restore", "--staged", "--", "note.txt")
        self.assertEqual(self.disk(), b"staged draft\n")
        self.assertEqual(self.git("show", ":note.txt"), "practice")
        self.assertEqual(self.git("diff", "--cached"), "")
        self.assertNotEqual(self.git("diff"), "")
        self.git("restore", "--", "note.txt")
        self.assertEqual(self.disk(), b"practice\n")
        self.assertEqual(self.ref(), self.base)
        self.clean()

    def test_reset_soft(self):
        tip = self.commit("note.txt", "second")
        self.git("branch", "backup/second")
        self.git("reset", "--soft", "HEAD^")
        self.assertEqual(self.ref(), self.base)
        self.assertEqual(self.git("show", ":note.txt"), "second")
        self.assertEqual(self.disk(), b"second\n")
        self.assertEqual(self.ref("backup/second"), tip)
        self.assertEqual(self.git("diff"), "")
        self.assertNotEqual(self.git("diff", "--cached"), "")

    def test_reset_mixed(self):
        self.commit("note.txt", "second")
        self.git("reset", "--mixed", "HEAD^")
        self.assertEqual(self.ref(), self.base)
        self.assertEqual(self.git("show", ":note.txt"), "practice")
        self.assertEqual(self.disk(), b"second\n")
        self.assertEqual(self.git("diff", "--cached"), "")
        self.assertNotEqual(self.git("diff"), "")

    def test_reset_hard_and_backup_recovery(self):
        tip = self.commit("note.txt", "second")
        self.git("branch", "backup/second")
        self.git("reset", "--hard", "HEAD^")
        self.assertEqual(self.ref(), self.base)
        self.assertEqual(self.git("show", ":note.txt"), "practice")
        self.assertEqual(self.disk(), b"practice\n")
        self.clean()
        self.git("merge", "--ff-only", "backup/second")
        self.assertEqual(self.ref(), tip)
        self.assertEqual(self.disk(), b"second\n")
        self.clean()

    def test_revert_preserves_ancestry(self):
        bad = self.commit("note.txt", "wrong")
        self.identity()
        self.git("revert", "--no-edit", "HEAD")
        self.assertEqual(self.ref("HEAD^"), bad)
        self.assertEqual(self.git("rev-list", "--count", "HEAD"), "3")
        self.assertEqual(self.git("diff", self.base, "HEAD"), "")
        self.assertEqual(self.disk(), b"practice\n")
        self.clean()

    def test_revert_conflict_abort(self):
        bad = self.commit("note.txt", "wrong")
        tip = self.commit("note.txt", "later")
        self.assertNotEqual(self.run_git("revert", "--no-edit", bad).returncode, 0)
        self.assertNotEqual(self.git("ls-files", "-u"), "")
        self.git("revert", "--abort")
        self.assertEqual(self.ref(), tip)
        self.assertEqual(self.disk(), b"later\n")
        self.clean()

    def test_reflog_rescues_displaced_commit(self):
        tip = self.commit("note.txt", "rescue me")
        self.git("reset", "--hard", "HEAD^")
        self.assertEqual(self.ref(), self.base)
        self.assertNotIn(tip, self.git("rev-list", "--all").splitlines())
        self.assertEqual(self.ref("HEAD@{1}"), tip)
        self.git("branch", "rescue/note", "HEAD@{1}")
        self.assertIn(tip, self.git("rev-list", "--all").splitlines())
        self.git("merge", "--ff-only", "rescue/note")
        self.assertEqual(self.ref(), tip)
        self.assertEqual(self.disk(), b"rescue me\n")
        self.clean()

    def test_stash_default_excludes_untracked(self):
        self.write("note.txt", "draft")
        self.write("untracked.txt", "temporary")
        self.git("stash", "push", "-m", "lab: default")
        self.assertEqual(self.disk(), b"practice\n")
        self.assertTrue((self.repo / "untracked.txt").exists())
        self.assertEqual(self.ref(), self.base)
        self.git("stash", "pop")
        self.assertEqual(self.disk(), b"draft\n")
        self.assertEqual(self.git("stash", "list"), "")

    def test_stash_apply_index_and_untracked(self):
        self.write("note.txt", "staged note")
        self.git("add", "--", "note.txt")
        self.write("note.txt", "working note")
        self.write("draft.txt", "temporary")
        self.git("stash", "push", "-u", "-m", "lab: temporary")
        self.clean()
        self.assertFalse((self.repo / "draft.txt").exists())
        saved = self.ref("refs/stash")
        self.git("stash", "apply", "--index", "stash@{0}")
        self.assertEqual(self.git("show", ":note.txt"), "staged note")
        self.assertEqual(self.disk(), b"working note\n")
        self.assertEqual(self.disk("draft.txt"), b"temporary\n")
        self.assertEqual(self.ref("refs/stash"), saved)
        self.git("stash", "drop", "stash@{0}")
        self.assertEqual(self.git("stash", "list"), "")
        self.assertEqual(self.disk(), b"working note\n")
        self.assertEqual(self.ref(), self.base)

    def test_cherry_pick_distinct_parent(self):
        self.git("switch", "-c", "fix/note")
        fix = self.commit("note.txt", "fixed")
        self.git("switch", "main")
        main = self.commit("overview.txt", "overview")
        self.identity()
        self.git("cherry-pick", "-x", "fix/note")
        self.assertNotEqual(self.ref(), fix)
        self.assertEqual(self.ref("HEAD^"), main)
        self.assertEqual(self.ref("fix/note"), fix)
        self.assertEqual(self.run_git("merge-base", "--is-ancestor", fix, "HEAD").returncode, 1)
        self.assertEqual(self.disk(), b"fixed\n")
        self.assertEqual(self.disk("overview.txt"), b"overview\n")
        self.clean()

    def test_cherry_pick_conflict_abort(self):
        self.git("switch", "-c", "fix/note")
        fix = self.commit("note.txt", "fixed")
        self.git("switch", "main")
        main = self.commit("note.txt", "other")
        self.assertNotEqual(self.run_git("cherry-pick", fix).returncode, 0)
        self.assertEqual(self.ref("CHERRY_PICK_HEAD"), fix)
        self.assertNotEqual(self.git("ls-files", "-u"), "")
        self.git("cherry-pick", "--abort")
        self.assertEqual(self.ref(), main)
        self.assertEqual(self.disk(), b"other\n")
        self.clean()

    def test_amend_replaces_tip_preserves_parent(self):
        old = self.commit("note.txt", "draft version")
        self.git("branch", "backup/draft")
        self.write("note.txt", "final version")
        self.git("add", "--", "note.txt")
        self.identity()
        self.git("commit", "--amend", "-m", "docs: final version")
        self.assertNotEqual(self.ref(), old)
        self.assertEqual(self.ref("HEAD^"), self.base)
        self.assertEqual(self.ref("backup/draft"), old)
        self.assertEqual(self.git("show", "backup/draft:note.txt"), "draft version")
        self.assertEqual(self.disk(), b"final version\n")
        self.assertEqual(self.git("rev-list", "--count", "HEAD"), "2")
        self.clean()


if __name__ == "__main__":
    unittest.main()
