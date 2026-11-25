"""Initial deterministic Git state test, using a disposable owned repository."""
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

class GitSmokeTest(unittest.TestCase):
    def test_first_commit_state(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            repo = root / "repo"
            repo.mkdir()
            home = root / "home"
            home.mkdir()
            config = root / "gitconfig"
            config.write_text("", encoding="utf-8")
            env = {k: v for k, v in os.environ.items() if not k.upper().startswith("GIT_")}
            env.update({"HOME": str(home), "USERPROFILE": str(home),
                        "GIT_CONFIG_GLOBAL": str(config), "GIT_CONFIG_NOSYSTEM": "1",
                        "GIT_TERMINAL_PROMPT": "0", "GIT_CONFIG_COUNT": "0"})
            def git(*args):
                return subprocess.run(["git", "-c", "core.hooksPath=" + str(root / "no-hooks"),
                                       "-c", "commit.gpgsign=false", *args], cwd=repo, env=env,
                                      check=True, capture_output=True, text=True, timeout=30).stdout
            git("init", "--initial-branch=main")
            git("config", "--local", "user.name", "Study Guide Example")
            git("config", "--local", "user.email", "learner@example.invalid")
            git("config", "--local", "commit.gpgsign", "false")
            self.assertEqual(git("config", "--local", "--get", "user.name").strip(), "Study Guide Example")
            self.assertEqual(git("config", "--local", "--get", "user.email").strip(), "learner@example.invalid")
            git("config", "core.autocrlf", "false")
            (repo / "note.txt").write_bytes(b"practice\n")
            self.assertEqual(git("status", "--porcelain=v1").strip(), "?? note.txt")
            git("add", "note.txt")
            self.assertEqual(git("diff", "--cached", "--name-only").strip(), "note.txt")
            self.assertIn("+practice", git("diff", "--cached"))
            git("commit", "-m", "docs: add note")
            self.assertEqual(git("status", "--porcelain=v1").strip(), "")
            self.assertEqual(git("symbolic-ref", "--short", "HEAD").strip(), "main")
            self.assertEqual(git("show", "HEAD:note.txt"), "practice\n")
            self.assertEqual(git("rev-list", "--count", "HEAD").strip(), "1")
            self.assertEqual(git("log", "-1", "--format=%s").strip(), "docs: add note")
            self.assertEqual(git("remote", "-v").strip(), "")
            # Verify that edits after staging do not silently enter the commit.
            (repo / "note.txt").write_bytes(b"second\n")
            git("add", "note.txt")
            (repo / "note.txt").write_bytes(b"third\n")
            self.assertEqual(git("show", ":note.txt"), "second\n")
            git("commit", "-m", "docs: revise note")
            self.assertEqual(git("show", "HEAD:note.txt"), "second\n")
            self.assertEqual(git("status", "--porcelain=v1").strip(), "M note.txt")

if __name__ == "__main__":
    unittest.main()
