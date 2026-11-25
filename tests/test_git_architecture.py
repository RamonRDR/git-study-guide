"""Deterministic state and command tests in an isolated disposable repository."""
import os
from pathlib import Path
import subprocess
import tempfile
import unittest


class GitArchitectureTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        root = Path(self.temp.name)
        self.repo = root / "repo"
        self.repo.mkdir()
        home = root / "home"
        home.mkdir()
        template = root / "template"
        template.mkdir()
        config = root / "gitconfig"
        config.write_text("", encoding="utf-8")
        self.env = {k: v for k, v in os.environ.items()
                    if not k.upper().startswith("GIT_")}
        self.env.update(HOME=str(home), USERPROFILE=str(home),
                        GIT_CONFIG_GLOBAL=str(config), GIT_CONFIG_NOSYSTEM="1",
                        GIT_TEMPLATE_DIR=str(template), GIT_TERMINAL_PROMPT="0",
                        GIT_CONFIG_COUNT="0")
        self.git("init", "--initial-branch=main")
        self.git("config", "--local", "user.name", "Study Guide Example")
        self.git("config", "--local", "user.email", "learner@example.invalid")
        self.git("config", "--local", "commit.gpgsign", "false")
        self.git("config", "--local", "core.autocrlf", "false")

    def git(self, *args, code=0):
        result = subprocess.run(["git", *args], cwd=self.repo, env=self.env,
                                capture_output=True, text=True, timeout=30)
        self.assertEqual(result.returncode, code, result.stderr)
        return result.stdout

    def write(self, path, content):
        (self.repo / path).write_bytes((content + "\n").encode("ascii"))

    def commit(self, message):
        for key in ("GIT_AUTHOR_IDENT", "GIT_COMMITTER_IDENT"):
            self.assertTrue(self.git("var", key).startswith(
                "Study Guide Example <learner@example.invalid> "))
        self.git("commit", "-m", message)

    def first_commit(self):
        self.write("note.txt", "practice")
        self.git("add", "--", "note.txt")
        self.commit("docs: add note")

    def test_three_locations_and_diff_baselines(self):
        self.first_commit()
        first = self.git("rev-parse", "HEAD").strip()
        self.write("note.txt", "second")
        self.git("add", "--", "note.txt")
        self.write("note.txt", "third")
        self.assertEqual(self.git("status", "--porcelain=v1"), "MM note.txt\n")
        self.assertEqual(self.git("show", "HEAD:note.txt"), "practice\n")
        self.assertEqual(self.git("show", ":note.txt"), "second\n")
        self.assertEqual((self.repo / "note.txt").read_bytes(), b"third\n")
        for args, old, new in [
            (("diff", "--", "note.txt"), "second", "third"),
            (("diff", "--cached", "--", "note.txt"), "practice", "second"),
            (("diff", "HEAD", "--", "note.txt"), "practice", "third"),
        ]:
            with self.subTest(args=args):
                lines = self.git(*args).splitlines()
                self.assertIn("-" + old, lines)
                self.assertIn("+" + new, lines)
        self.commit("docs: revise note")
        self.assertEqual(self.git("symbolic-ref", "HEAD").strip(), "refs/heads/main")
        self.assertEqual(self.git("rev-parse", "HEAD"),
                         self.git("rev-parse", "refs/heads/main"))
        self.assertNotEqual(self.git("rev-parse", "HEAD").strip(), first)
        self.assertEqual(self.git("rev-parse", "HEAD~1").strip(), first)
        self.assertEqual(self.git("show", "HEAD:note.txt"), "second\n")
        self.assertEqual(self.git("status", "--porcelain=v1"), " M note.txt\n")
        self.assertEqual(self.git("diff", "--cached"), "")

    def test_config_scope_and_explicit_staging(self):
        self.assertEqual(self.git("config", "--local", "--get",
                                  "core.autocrlf").strip(), "false")
        self.assertEqual(self.git("-c", "core.autocrlf=true", "config",
                                  "--get", "core.autocrlf").strip(), "true")
        self.assertEqual(self.git("config", "--local", "--get",
                                  "core.autocrlf").strip(), "false")
        self.write("note.txt", "practice")
        self.write("draft.txt", "draft")
        self.git("add", "--", "note.txt")
        self.assertEqual(set(self.git("status", "--porcelain=v1").splitlines()),
                         {"A  note.txt", "?? draft.txt"})
        self.assertEqual(self.git("diff", "--cached", "--name-only"), "note.txt\n")
        self.commit("docs: add note")
        self.assertEqual(self.git("ls-files"), "note.txt\n")
        self.assertEqual(self.git("status", "--porcelain=v1"), "?? draft.txt\n")
        self.assertEqual(self.git("remote", "-v"), "")
        self.assertEqual(self.git("diff"), "")

    def test_move_and_remove(self):
        self.first_commit()
        self.git("mv", "--", "note.txt", "notes.txt")
        self.assertFalse((self.repo / "note.txt").exists())
        self.assertEqual((self.repo / "notes.txt").read_bytes(), b"practice\n")
        self.assertEqual(self.git("ls-files"), "notes.txt\n")
        self.assertEqual(self.git("diff", "--cached", "--name-status", "-M"),
                         "R100\tnote.txt\tnotes.txt\n")
        self.commit("docs: rename note")
        self.git("rm", "--cached", "--", "notes.txt")
        self.assertTrue((self.repo / "notes.txt").is_file())
        self.assertEqual(self.git("ls-files"), "")
        self.assertEqual(self.git("diff", "--cached", "--name-status"), "D\tnotes.txt\n")
        self.git("add", "--", "notes.txt")
        self.assertEqual(self.git("diff", "--cached"), "")
        self.git("rm", "--", "notes.txt")
        self.assertFalse((self.repo / "notes.txt").exists())
        self.assertEqual(self.git("diff", "--cached", "--name-status"), "D\tnotes.txt\n")
        self.commit("docs: remove note")
        self.assertEqual(self.git("ls-files"), "")
        self.assertEqual(self.git("show", "HEAD~1:notes.txt"), "practice\n")
        self.assertEqual(self.git("status", "--porcelain=v1"), "")

    def test_ignore_rules_and_tracked_file(self):
        self.write(".gitignore", "/draft.txt\n*.tmp\n!keep.tmp\n/build/")
        self.write("draft.txt", "draft")
        self.write("report.tmp", "sample")
        self.write("keep.tmp", "keep")
        self.assertEqual(set(self.git("status", "--porcelain=v1", "--ignored").splitlines()),
                         {"?? .gitignore", "?? keep.tmp", "!! draft.txt", "!! report.tmp"})
        self.assertEqual(self.git("check-ignore", "--", "draft.txt", "report.tmp").splitlines(),
                         ["draft.txt", "report.tmp"])
        self.git("check-ignore", "--", "keep.tmp", code=1)
        self.git("add", "--", ".gitignore", "keep.tmp")
        self.commit("docs: add ignore rules")
        self.write(".gitignore", "/draft.txt\n*.tmp\n!keep.tmp\n/build/\n/keep.tmp")
        self.write("keep.tmp", "updated")
        self.assertEqual(set(self.git("status", "--porcelain=v1").splitlines()),
                         {" M .gitignore", " M keep.tmp"})
        self.assertEqual(self.git("ls-files", "--", "keep.tmp"), "keep.tmp\n")
        self.assertEqual(self.git("check-ignore", "--no-index", "--", "keep.tmp"),
                         "keep.tmp\n")
        self.git("rm", "--cached", "--", "keep.tmp")
        self.git("add", "--", ".gitignore")
        self.assertEqual(set(self.git("diff", "--cached", "--name-status").splitlines()),
                         {"M\t.gitignore", "D\tkeep.tmp"})
        self.assertEqual((self.repo / "keep.tmp").read_bytes(), b"updated\n")
        self.commit("docs: stop tracking generated file")
        self.assertEqual(self.git("ls-files"), ".gitignore\n")
        self.assertEqual(self.git("show", "HEAD~1:keep.tmp"), "keep\n")
        self.assertEqual(set(self.git("status", "--porcelain=v1", "--ignored").splitlines()),
                         {"!! draft.txt", "!! keep.tmp", "!! report.tmp"})


if __name__ == "__main__":
    unittest.main()
