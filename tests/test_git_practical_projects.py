"""Fixed integration checks for the manual practical projects."""
import os
from pathlib import Path
import subprocess
import tempfile
import unittest


class PracticalProjectsTest(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.repo = self.root / "repo"
        self.repo.mkdir()
        home = self.root / "home"
        home.mkdir()
        template = self.root / "template"
        template.mkdir()
        config = self.root / "gitconfig"
        config.write_text("", encoding="utf-8")
        self.env = {k: v for k, v in os.environ.items() if not k.upper().startswith("GIT_")}
        self.env.update(HOME=str(home), USERPROFILE=str(home),
                        XDG_CONFIG_HOME=str(home), GIT_CONFIG_GLOBAL=str(config),
                        GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_COUNT="0",
                        GIT_TEMPLATE_DIR=str(template), GIT_TERMINAL_PROMPT="0")
        self.git("init", "-b", "main")
        for key, value in (("user.name", "Study Guide Example"),
                           ("user.email", "learner@example.invalid"),
                           ("core.autocrlf", "false"),
                           ("commit.gpgsign", "false"),
                           ("core.hooksPath", str(self.root / "no-hooks"))):
            self.git("config", "--local", key, value)

    def git(self, *args):
        result = subprocess.run(["git", *args], cwd=self.repo, env=self.env,
                                capture_output=True, text=True, timeout=30)
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout

    def write(self, content):
        (self.repo / "notes.txt").write_bytes((content + "\n").encode("ascii"))

    def commit(self, message):
        identity = "Study Guide Example <learner@example.invalid> "
        for key in ("GIT_AUTHOR_IDENT", "GIT_COMMITTER_IDENT"):
            self.assertTrue(self.git("var", key).startswith(identity))
        self.git("commit", "-m", message)

    def test_first_repository_staged_snapshot(self):
        self.write("status: draft")
        self.assertEqual(self.git("status", "--porcelain=v1"), "?? notes.txt\n")
        self.git("add", "notes.txt")
        self.commit("docs: initialize notes")
        initial = self.git("rev-parse", "HEAD").strip()
        self.write("status: ready")
        self.git("add", "notes.txt")
        self.write("status: experiment")
        self.assertEqual(self.git("status", "--porcelain=v1"), "MM notes.txt\n")
        self.assertEqual(self.git("show", "HEAD:notes.txt"), "status: draft\n")
        self.assertEqual(self.git("show", ":notes.txt"), "status: ready\n")
        self.commit("docs: mark notes ready")
        self.assertEqual(self.git("show", "HEAD:notes.txt"), "status: ready\n")
        self.assertEqual(self.git("status", "--porcelain=v1"), " M notes.txt\n")
        self.git("restore", "--worktree", "--", "notes.txt")
        self.assertEqual((self.repo / "notes.txt").read_bytes(), b"status: ready\n")
        self.assertEqual(self.git("rev-parse", "HEAD^1").strip(), initial)
        self.assertEqual(self.git("rev-list", "--count", "HEAD").strip(), "2")
        self.assertEqual(self.git("symbolic-ref", "--short", "HEAD").strip(), "main")
        self.assertEqual(self.git("status", "--porcelain=v1"), "")
        self.assertEqual(self.git("remote"), "")


if __name__ == "__main__":
    unittest.main()
