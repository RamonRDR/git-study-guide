"""Native Git tag checks; no GitHub API, network, login or learner code."""
import os
from pathlib import Path
import subprocess
import tempfile
import unittest


class GitTagTest(unittest.TestCase):
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
        self.base = self.commit("practice")
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

    def test_annotated_tag_peels_to_commit_without_moving_head(self):
        self.git("tag", "-a", "v0.1.0", "-m", "Release 0.1.0")
        self.assertEqual(self.git("cat-file", "-t", "v0.1.0"), "tag")
        self.assertEqual(self.git("rev-parse", "v0.1.0^{commit}"), self.base)
        self.assertEqual(self.git("rev-parse", "HEAD"), self.base)
        self.assertEqual(self.git("status", "--porcelain=v1"), "")

    def test_lightweight_tag_points_directly_to_commit(self):
        self.git("tag", "v0.1.0")
        self.assertEqual(self.git("cat-file", "-t", "v0.1.0"), "commit")
        self.assertEqual(self.git("rev-parse", "v0.1.0"), self.base)

    def test_tags_do_not_advance_with_branch(self):
        self.git("tag", "-a", "v0.1.0", "-m", "Release 0.1.0")
        later = self.commit("later")
        self.assertNotEqual(later, self.base)
        self.assertEqual(self.git("rev-parse", "v0.1.0^{commit}"), self.base)
        self.assertEqual(self.git("rev-parse", "main"), later)
        self.assertNotEqual(self.run_git("tag", "v0.1.0").returncode, 0)
        self.assertEqual(self.git("rev-parse", "v0.1.0^{commit}"), self.base)


if __name__ == "__main__":
    unittest.main()
