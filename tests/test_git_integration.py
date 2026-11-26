"""Merge/rebase topology and conflict tests in isolated disposable Git repositories."""
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


class GitIntegrationTest(unittest.TestCase):
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
        # Git invokes editors through its shell. These fixed scripts only edit
        # the Git-owned message/todo in this test; no learner code is executed.
        message_editor = root / "message_editor.py"
        message_editor.write_text("import sys\nassert len(sys.argv) == 2\n",
                                  encoding="utf-8")
        todo_editor = root / "todo_editor.py"
        todo_editor.write_text(
            "from pathlib import Path\nimport sys\n"
            "p = Path(sys.argv[1])\n"
            "lines = p.read_text(encoding='utf-8').splitlines()\n"
            "picks = [i for i, line in enumerate(lines) if line.startswith('pick ')]\n"
            "assert len(picks) == 2\n"
            "i = picks[1]\n"
            "lines[i] = 'fixup ' + lines[i][5:]\n"
            "p.write_text('\\n'.join(lines) + '\\n', encoding='utf-8')\n",
            encoding="utf-8")
        self.env["GIT_EDITOR"] = self.editor_command(message_editor)
        self.env["GIT_SEQUENCE_EDITOR"] = self.editor_command(todo_editor)
        self.git("init", "--initial-branch=main")
        self.git("config", "--local", "user.name", "Study Guide Example")
        self.git("config", "--local", "user.email", "learner@example.invalid")
        self.git("config", "--local", "commit.gpgsign", "false")
        self.git("config", "--local", "core.autocrlf", "false")
        self.git("config", "--local", "rerere.enabled", "false")
        self.write("note.txt", "practice")
        self.commit("note.txt", "docs: add note")
        self.base = self.ref("main")

    @staticmethod
    def editor_command(script):
        return '"' + Path(sys.executable).as_posix() + '" "' + script.as_posix() + '"'

    def run_git(self, *args):
        return subprocess.run(["git", *args], cwd=self.repo, env=self.env,
                              capture_output=True, text=True, timeout=30)

    def git(self, *args):
        result = self.run_git(*args)
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout

    def ref(self, name):
        return self.git("rev-parse", name).strip()

    def write(self, path, content):
        (self.repo / path).write_bytes((content + "\n").encode("ascii"))

    def commit(self, path, message):
        self.git("add", "--", path)
        for key in ("GIT_AUTHOR_IDENT", "GIT_COMMITTER_IDENT"):
            self.assertTrue(self.git("var", key).startswith(
                "Study Guide Example <learner@example.invalid> "))
        self.git("commit", "-m", message)

    def clean(self):
        self.assertEqual(self.git("status", "--porcelain=v1"), "")

    def parents(self):
        return self.git("rev-list", "--parents", "-1", "HEAD").split()[1:]

    def feature(self, two=False):
        self.git("switch", "-c", "feat/note")
        self.write("note.txt", "feature")
        self.commit("note.txt", "docs: revise feature note")
        if two:
            self.write("detail.txt", "detail")
            self.commit("detail.txt", "docs: add detail")
        return self.ref("HEAD")

    def divergent(self, conflict=False, two=False):
        feature = self.feature(two)
        self.git("switch", "main")
        path, content = ("note.txt", "main") if conflict else ("overview.txt", "overview")
        self.write(path, content)
        self.commit(path, "docs: change main")
        return self.ref("main"), feature

    def conflict_stages(self):
        self.assertEqual(self.git("status", "--porcelain=v1"), "UU note.txt\n")
        stages = self.git("ls-files", "-u").splitlines()
        self.assertEqual(len(stages), 3)
        self.assertEqual({line.split()[2] for line in stages}, {"1", "2", "3"})
        for stage, content in ((1, "practice"), (2, "main"), (3, "feature")):
            self.assertEqual(self.git("show", f":{stage}:note.txt"), content + "\n")
        self.assertIn(b"<<<<<<<", (self.repo / "note.txt").read_bytes())

    def resolve_note(self):
        self.write("note.txt", "main\nfeature")
        self.git("add", "--", "note.txt")
        self.assertEqual(self.git("ls-files", "-u"), "")
        self.assertEqual(self.git("diff", "--cached", "--check"), "")

    def test_fast_forward(self):
        feature = self.feature()
        self.git("switch", "main")
        self.git("merge", "--ff-only", "feat/note")
        self.assertEqual(self.ref("main"), feature)
        self.assertEqual(self.ref("feat/note"), feature)
        self.assertEqual(self.parents(), [self.base])
        self.assertEqual(self.git("rev-list", "--count", "main").strip(), "2")
        self.assertEqual(self.git("show", "HEAD:note.txt"), "feature\n")
        self.clean()

    def test_no_ff_preserves_two_parents_even_when_ff_possible(self):
        feature = self.feature()
        self.git("switch", "main")
        self.git("merge", "--no-ff", "--no-edit", "feat/note")
        self.assertEqual(self.parents(), [self.base, feature])
        self.assertNotEqual(self.ref("main"), feature)
        self.assertEqual(self.git("show", "HEAD:note.txt"), "feature\n")
        self.clean()

    def test_divergence_ff_refusal_and_merge_commit(self):
        main, feature = self.divergent()
        self.assertNotEqual(self.run_git("merge", "--ff-only", "feat/note").returncode, 0)
        self.assertEqual(self.ref("main"), main)
        self.assertEqual(self.ref("feat/note"), feature)
        self.clean()
        self.git("merge", "--no-ff", "--no-edit", "feat/note")
        self.assertEqual(self.parents(), [main, feature])
        self.assertEqual(self.git("show", "HEAD:note.txt"), "feature\n")
        self.assertEqual(self.git("show", "HEAD:overview.txt"), "overview\n")
        self.assertEqual(self.ref("feat/note"), feature)
        self.clean()

    def test_merge_conflict_abort_and_continue(self):
        main, feature = self.divergent(conflict=True)
        for attempt in range(2):
            self.assertNotEqual(self.run_git("merge", "--no-ff", "--no-edit",
                                             "feat/note").returncode, 0)
            self.conflict_stages()
            self.assertEqual(self.ref("MERGE_HEAD"), feature)
            if attempt == 0:
                self.git("merge", "--abort")
                self.assertEqual(self.ref("HEAD"), main)
                self.assertEqual((self.repo / "note.txt").read_bytes(), b"main\n")
                self.clean()
        self.resolve_note()
        self.git("merge", "--continue")
        self.assertEqual(self.parents(), [main, feature])
        self.assertEqual(self.git("show", "HEAD:note.txt"), "main\nfeature\n")
        self.clean()

    def test_squash_has_one_parent_and_no_source_ancestry(self):
        main, feature = self.divergent(two=True)
        self.git("merge", "--squash", "feat/note")
        self.assertEqual(self.ref("HEAD"), main)
        self.assertNotEqual(self.run_git("rev-parse", "--verify", "MERGE_HEAD").returncode, 0)
        self.assertEqual(set(self.git("diff", "--cached", "--name-status").splitlines()),
                         {"A\tdetail.txt", "M\tnote.txt"})
        self.git("commit", "-m", "docs: integrate feature changes")
        self.assertEqual(self.parents(), [main])
        self.assertEqual(self.ref("feat/note"), feature)
        self.assertEqual(self.git("rev-list", "--count", "main..feat/note").strip(), "2")
        self.assertEqual(self.run_git("merge-base", "--is-ancestor",
                                      "feat/note", "main").returncode, 1)
        for path, value in (("note.txt", "feature"), ("detail.txt", "detail"),
                            ("overview.txt", "overview")):
            self.assertEqual(self.git("show", "HEAD:" + path), value + "\n")
        self.clean()

    def test_nonconflicting_rebase(self):
        main, feature = self.divergent(two=True)
        self.git("switch", "feat/note")
        self.git("branch", "backup/feature")
        self.git("rebase", "main")
        self.assertEqual(self.ref("main"), main)
        self.assertEqual(self.ref("backup/feature"), feature)
        self.assertNotEqual(self.ref("HEAD"), feature)
        self.assertEqual(self.ref("HEAD~2"), main)
        self.assertEqual(self.git("rev-list", "--count", "main..HEAD").strip(), "2")
        self.assertEqual(self.git("show", "HEAD:note.txt"), "feature\n")
        self.assertEqual(self.git("show", "HEAD:detail.txt"), "detail\n")
        self.assertEqual(self.git("show", "HEAD:overview.txt"), "overview\n")
        self.clean()

    def test_rebase_conflict_abort_and_continue(self):
        main, feature = self.divergent(conflict=True)
        self.git("switch", "feat/note")
        self.git("branch", "backup/feature")
        for attempt in range(2):
            self.assertNotEqual(self.run_git("rebase", "main").returncode, 0)
            self.conflict_stages()
            if attempt == 0:
                self.git("rebase", "--abort")
                self.assertEqual(self.ref("HEAD"), feature)
                self.assertEqual(self.git("branch", "--show-current").strip(), "feat/note")
                self.assertEqual((self.repo / "note.txt").read_bytes(), b"feature\n")
                self.clean()
        self.resolve_note()
        self.git("rebase", "--continue")
        self.assertEqual(self.git("branch", "--show-current").strip(), "feat/note")
        self.assertEqual(self.parents(), [main])
        self.assertEqual(self.ref("main"), main)
        self.assertNotEqual(self.ref("HEAD"), feature)
        self.assertEqual(self.ref("backup/feature"), feature)
        self.assertEqual(self.git("show", "HEAD:note.txt"), "main\nfeature\n")
        self.clean()

    def test_interactive_fixup_preserves_snapshot_and_backup(self):
        feature = self.feature(two=True)
        self.git("branch", "backup/feature")
        self.git("rebase", "-i", "HEAD~2")
        self.assertEqual(self.git("rev-list", "--count", "main..HEAD").strip(), "1")
        self.assertEqual(self.git("rev-list", "--count", "main..backup/feature").strip(), "2")
        self.assertEqual(self.parents(), [self.base])
        self.assertEqual(self.ref("backup/feature"), feature)
        self.assertNotEqual(self.ref("HEAD"), feature)
        self.assertEqual(self.git("log", "-1", "--format=%s").strip(),
                         "docs: revise feature note")
        self.assertEqual(self.git("diff", "HEAD", "backup/feature"), "")
        self.assertEqual(self.git("show", "HEAD:detail.txt"), "detail\n")
        self.clean()


if __name__ == "__main__":
    unittest.main()
