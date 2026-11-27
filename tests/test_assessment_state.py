"""Positive and incorrect states for each of the twelve fixed challenge fixtures."""
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

from scripts.assessment_pilot import read_json
from scripts.assessment_state import evaluate

ROOT = Path(__file__).resolve().parents[1]


class AssessmentStateTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = {r["id"]: r for r in read_json(
            ROOT, "exercises/02-challenges/records.json")["records"]}

    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        self.repo = root / "repo"
        self.repo.mkdir()
        home = root / "home"
        home.mkdir()
        template = root / "template"
        template.mkdir()
        config = root / "gitconfig"
        config.write_text("", encoding="utf-8")
        self.env = {k: v for k, v in os.environ.items() if not k.upper().startswith("GIT_")}
        self.env.update(HOME=str(home), USERPROFILE=str(home), XDG_CONFIG_HOME=str(home),
                        GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=str(config),
                        GIT_CONFIG_COUNT="0", GIT_TEMPLATE_DIR=str(template),
                        GIT_TERMINAL_PROMPT="0")
        self.git("init", "-b", "main")
        for key, value in (("user.name", "Study Guide Example"), ("user.email", "learner@example.invalid"),
                           ("core.autocrlf", "false"), ("commit.gpgsign", "false"),
                           ("tag.gpgsign", "false"), ("core.hooksPath", str(root / "no-hooks")),
                           ("rerere.enabled", "false")):
            self.git("config", "--local", key, value)

    def run_git(self, *args):
        return subprocess.run(["git", *args], cwd=self.repo, env=self.env,
                              capture_output=True, timeout=30)

    def git(self, *args, expected=0):
        result = self.run_git(*args)
        self.assertEqual(result.returncode, expected, result.stderr)
        return result.stdout

    def read_file(self, name):
        path = self.repo / name
        return path.read_bytes() if path.is_file() and not path.is_symlink() else None

    def write(self, text, name="notes.txt"):
        (self.repo / name).write_bytes((text + "\n").encode("ascii"))

    def commit_file(self, text, name="notes.txt", message="docs: update notes"):
        self.write(text, name)
        self.git("add", "--", name)
        self.git("commit", "-m", message)

    def seed(self):
        self.commit_file("status: draft", message="docs: initialize notes")

    def feature(self):
        self.git("switch", "-c", "feat/notes")
        self.commit_file("status: ready")

    def assert_state(self, challenge, expected):
        checks = self.records["challenge-" + challenge]["checks"]
        actual = [evaluate(check, self.run_git, self.read_file) for check in checks]
        if expected:
            self.assertTrue(all(actual), list(zip(checks, actual)))
        else:
            self.assertFalse(all(actual), list(zip(checks, actual)))

    def test_first_commit(self):
        self.assert_state("first-commit", False)
        self.commit_file("status: ready", message="docs: add notes")
        self.assert_state("first-commit", True)
        self.write("status: experiment")
        self.assert_state("first-commit", False)

    def test_staged_snapshot(self):
        self.seed()
        self.assert_state("staged-snapshot", False)
        self.write("status: ready")
        self.git("add", "notes.txt")
        self.write("status: experiment")
        self.assert_state("staged-snapshot", True)
        self.git("add", "notes.txt")
        self.assert_state("staged-snapshot", False)

    def test_unstage(self):
        self.seed()
        self.write("status: ready")
        self.git("add", "notes.txt")
        self.assert_state("unstage", False)
        self.git("restore", "--staged", "--", "notes.txt")
        self.assert_state("unstage", True)
        self.git("restore", "--worktree", "--", "notes.txt")
        self.assert_state("unstage", False)

    def test_feature_branch(self):
        self.seed()
        self.assert_state("feature-branch", False)
        self.feature()
        self.assert_state("feature-branch", True)
        self.git("switch", "main")
        self.assert_state("feature-branch", False)

    def test_fast_forward(self):
        self.seed()
        self.feature()
        self.git("switch", "main")
        self.assert_state("fast-forward", False)
        self.git("merge", "--ff-only", "feat/notes")
        self.assert_state("fast-forward", True)
        self.commit_file("status: experiment")
        self.assert_state("fast-forward", False)

    def test_merge_resolution(self):
        self.seed()
        self.feature()
        self.git("switch", "main")
        self.commit_file("status: experiment")
        self.git("merge", "feat/notes", expected=1)
        self.assertEqual(len(self.git("ls-files", "-u").splitlines()), 3)
        self.assert_state("merge-resolution", False)
        self.write("status: reviewed")
        self.git("add", "notes.txt")
        self.git("commit", "-m", "merge: resolve notes")
        self.assert_state("merge-resolution", True)
        self.write("status: experiment")
        self.assert_state("merge-resolution", False)

    def test_revert(self):
        self.seed()
        self.commit_file("status: ready")
        self.assert_state("revert", False)
        self.git("revert", "--no-edit", "HEAD")
        self.assert_state("revert", True)
        self.commit_file("status: ready")
        self.assert_state("revert", False)

    def test_stash(self):
        self.seed()
        self.write("status: ready")
        self.write("review: done", "review.txt")
        self.git("stash", "push", "-u", "-m", "practice notes")
        self.assertEqual(self.git("status", "--porcelain"), b"")
        self.assert_state("stash", False)
        self.git("stash", "apply")
        self.assert_state("stash", True)
        self.assertTrue(self.git("stash", "list"))
        self.git("add", "review.txt")
        self.assert_state("stash", False)

    def test_recover_tip(self):
        self.seed()
        self.commit_file("status: recovered")
        saved = self.git("rev-parse", "HEAD")
        self.assertEqual(self.git("status", "--porcelain"), b"")
        self.git("reset", "--hard", "HEAD~1")
        self.assert_state("recover-tip", False)
        self.assertEqual(self.git("rev-parse", "HEAD@{1}"), saved)
        self.git("branch", "recovery/notes", "HEAD@{1}")
        self.assert_state("recover-tip", True)
        self.git("branch", "-f", "recovery/notes", "main")
        self.assert_state("recover-tip", False)

    def test_squash(self):
        self.seed()
        self.feature()
        self.commit_file("review: done", "review.txt")
        self.git("switch", "main")
        self.git("merge", "--squash", "feat/notes")
        self.assert_state("squash", False)
        self.git("commit", "-m", "feat: deliver reviewed notes")
        self.assert_state("squash", True)
        self.commit_file("status: experiment")
        self.assert_state("squash", False)

    def test_release_tag(self):
        self.seed()
        self.commit_file("status: ready")
        self.git("tag", "-a", "v1.0.0", "-m", "Ready notes release")
        self.assert_state("release-tag", False)
        self.commit_file("future work", "future.txt")
        self.assert_state("release-tag", True)
        self.git("tag", "-f", "v1.0.0", "HEAD")
        self.assert_state("release-tag", False)

    def test_cherry_pick(self):
        self.seed()
        self.git("switch", "-c", "feat/notes")
        self.commit_file("review: done", "review.txt")
        self.git("switch", "main")
        self.commit_file("status: ready")
        self.assert_state("cherry-pick", False)
        self.git("cherry-pick", "feat/notes")
        self.assert_state("cherry-pick", True)
        self.write("status: experiment")
        self.assert_state("cherry-pick", False)


if __name__ == "__main__":
    unittest.main()
