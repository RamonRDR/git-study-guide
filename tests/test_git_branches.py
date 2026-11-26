"""Local branch state tests using isolated disposable Git repositories."""
import os
from pathlib import Path
import subprocess
import tempfile
import unittest


class GitBranchTest(unittest.TestCase):
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
        self.write("note.txt", "practice")
        self.commit("note.txt", "docs: add note")
        self.base = self.ref("main")

    def run_git(self, *args):
        return subprocess.run(["git", *args], cwd=self.repo, env=self.env,
                              capture_output=True, text=True, timeout=30)

    def git(self, *args):
        result = self.run_git(*args)
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout

    def write(self, path, content):
        (self.repo / path).write_bytes((content + "\n").encode("ascii"))

    def ref(self, name):
        return self.git("rev-parse", name).strip()

    def commit(self, path, message):
        self.git("add", "--", path)
        for key in ("GIT_AUTHOR_IDENT", "GIT_COMMITTER_IDENT"):
            self.assertTrue(self.git("var", key).startswith(
                "Study Guide Example <learner@example.invalid> "))
        self.git("commit", "-m", message)

    def feature(self):
        self.git("branch", "feat/note")
        self.assertEqual(self.ref("feat/note"), self.base)
        self.assertEqual(self.git("symbolic-ref", "HEAD").strip(), "refs/heads/main")
        self.assertEqual(self.git("status", "--porcelain=v1"), "")
        self.git("switch", "feat/note")
        self.write("note.txt", "feature")
        self.commit("note.txt", "docs: revise feature note")
        return self.ref("HEAD")

    def test_create_switch_and_branch_refs(self):
        feature = self.feature()
        self.assertNotEqual(feature, self.base)
        self.assertEqual(self.ref("main"), self.base)
        self.assertEqual(self.ref("HEAD~1"), self.base)
        self.assertEqual(self.git("branch", "--show-current").strip(), "feat/note")
        self.git("switch", "main")
        self.assertEqual((self.repo / "note.txt").read_bytes(), b"practice\n")
        self.assertEqual(self.git("show", ":note.txt"), "practice\n")
        self.git("switch", "feat/note")
        self.assertEqual((self.repo / "note.txt").read_bytes(), b"feature\n")
        self.assertEqual(self.git("show", ":note.txt"), "feature\n")
        self.assertEqual(self.ref("HEAD"), feature)
        self.assertEqual(self.git("status", "--porcelain=v1"), "")
        self.assertEqual(self.git("remote", "-v"), "")

    def test_start_points_and_comparisons(self):
        feature = self.feature()
        self.git("branch", "archive/base", "HEAD~1")
        self.assertEqual(self.ref("archive/base"), self.base)
        self.git("switch", "-c", "docs/overview", "main")
        self.assertEqual(self.ref("HEAD"), self.base)
        self.write("overview.txt", "overview")
        self.commit("overview.txt", "docs: add overview")
        overview = self.ref("HEAD")
        self.assertEqual(self.git("rev-list", "feat/note..docs/overview").splitlines(),
                         [overview])
        self.assertEqual(self.git("rev-list", "docs/overview..feat/note").splitlines(),
                         [feature])
        self.assertEqual(set(self.git("diff", "--name-status", "feat/note",
                                      "docs/overview").splitlines()),
                         {"M\tnote.txt", "A\toverview.txt"})
        self.assertEqual(self.git("diff", "--name-status", "feat/note...docs/overview"),
                         "A\toverview.txt\n")
        self.assertEqual(self.git("merge-base", "feat/note", "docs/overview").strip(),
                         self.base)
        self.assertEqual(self.ref("main"), self.base)

    def test_rename_and_blocked_switch_preserve_edits(self):
        feature = self.feature()
        self.git("check-ref-format", "--branch", "feat/note-revision")
        self.assertNotEqual(self.run_git("check-ref-format", "--branch",
                                        "bad name").returncode, 0)
        self.git("branch", "-m", "feat/note-revision")
        self.assertEqual(self.git("symbolic-ref", "HEAD").strip(),
                         "refs/heads/feat/note-revision")
        self.assertEqual(self.ref("feat/note-revision"), feature)
        self.assertNotEqual(self.run_git("show-ref", "--verify",
                                        "refs/heads/feat/note").returncode, 0)
        self.write("note.txt", "unfinished")
        self.assertNotEqual(self.run_git("switch", "main").returncode, 0)
        self.assertEqual(self.ref("HEAD"), feature)
        self.assertEqual(self.git("branch", "--show-current").strip(),
                         "feat/note-revision")
        self.assertEqual((self.repo / "note.txt").read_bytes(), b"unfinished\n")
        self.assertEqual(self.git("show", ":note.txt"), "feature\n")
        self.write("note.txt", "feature")
        self.assertEqual(self.git("status", "--porcelain=v1"), "")
        self.git("switch", "main")
        self.assertEqual(self.ref("HEAD"), self.base)

    def test_guarded_local_deletion(self):
        feature = self.feature()
        self.git("branch", "archive/base", "main")
        self.git("switch", "main")
        self.assertEqual(self.git("rev-list", "main..archive/base"), "")
        self.assertEqual(self.git("rev-list", "main..feat/note").strip(), feature)
        self.git("branch", "-d", "archive/base")
        self.assertNotEqual(self.run_git("show-ref", "--verify",
                                        "refs/heads/archive/base").returncode, 0)
        self.assertNotEqual(self.run_git("branch", "-d", "feat/note").returncode, 0)
        self.assertEqual(self.ref("feat/note"), feature)
        self.assertNotEqual(self.run_git("branch", "-d", "main").returncode, 0)
        self.assertEqual(self.ref("main"), self.base)
        self.assertEqual(self.git("status", "--porcelain=v1"), "")

    def test_detached_commit_preserved_by_branch(self):
        self.git("switch", "--detach", "main")
        self.assertEqual(self.git("branch", "--show-current"), "")
        self.assertNotEqual(self.run_git("symbolic-ref", "HEAD").returncode, 0)
        self.assertEqual(self.ref("HEAD"), self.base)
        self.write("experiment.txt", "experiment")
        self.commit("experiment.txt", "docs: record experiment")
        experiment = self.ref("HEAD")
        self.assertNotEqual(experiment, self.base)
        self.assertEqual(self.ref("main"), self.base)
        self.git("switch", "-c", "experiment/saved")
        self.assertEqual(self.ref("experiment/saved"), experiment)
        self.assertEqual(self.git("symbolic-ref", "HEAD").strip(),
                         "refs/heads/experiment/saved")
        self.git("switch", "main")
        self.assertFalse((self.repo / "experiment.txt").exists())
        self.assertEqual(self.git("show", "experiment/saved:experiment.txt"),
                         "experiment\n")
        self.assertEqual(self.ref("main"), self.base)
        self.assertEqual(self.git("status", "--porcelain=v1"), "")


if __name__ == "__main__":
    unittest.main()
