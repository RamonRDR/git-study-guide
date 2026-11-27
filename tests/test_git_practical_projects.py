"""Fixed integration checks for the manual practical projects."""
import os
from pathlib import Path
import subprocess
import tempfile
import tarfile
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

    def at(self, repo, *args, expected=0):
        result = subprocess.run(["git", *args], cwd=repo, env=self.env,
                                capture_output=True, text=True, timeout=30)
        self.assertEqual(result.returncode, expected, result.stderr)
        return result.stdout

    def configure_clone(self, repo):
        for key, value in (("user.name", "Study Guide Example"),
                           ("user.email", "learner@example.invalid"),
                           ("core.autocrlf", "false"),
                           ("commit.gpgsign", "false"),
                           ("core.hooksPath", str(self.root / "no-hooks"))):
            self.at(repo, "config", "--local", key, value)

    def seed(self, content="status: draft"):
        self.write(content)
        self.git("add", "notes.txt")
        self.commit("docs: initialize notes")
        return self.git("rev-parse", "HEAD").strip()

    def local_origin(self):
        origin = self.root / "origin.git"
        self.git("init", "--bare", "-b", "main", str(origin))
        self.git("remote", "add", "origin", str(origin))
        self.git("push", "-u", "origin", "main")
        return origin

    def clone(self, source, name):
        target = self.root / name
        self.git("clone", str(source), str(target))
        self.configure_clone(target)
        return target

    def test_two_developers_sync(self):
        self.seed("shared: draft")
        origin = self.local_origin()
        alice = self.clone(origin, "alice")
        bob = self.clone(origin, "bob")
        before = self.at(bob, "rev-parse", "HEAD")
        (alice / "notes.txt").write_bytes(b"shared: ready\n")
        self.at(alice, "add", "notes.txt")
        self.at(alice, "commit", "-m", "docs: prepare shared notes")
        self.at(alice, "push", "origin", "main")
        self.at(bob, "fetch", "origin")
        self.assertEqual(self.at(bob, "rev-parse", "HEAD"), before)
        self.assertNotEqual(self.at(bob, "rev-parse", "origin/main"), before)
        self.assertEqual((bob / "notes.txt").read_bytes(), b"shared: draft\n")
        self.at(bob, "merge", "--ff-only", "origin/main")
        (bob / "review.txt").write_bytes(b"review: done\n")
        self.at(bob, "add", "review.txt")
        self.at(bob, "commit", "-m", "docs: record review")
        self.at(bob, "push", "origin", "main")
        self.at(alice, "pull", "--ff-only", "origin", "main")
        tip = self.at(bob, "rev-parse", "HEAD")
        self.assertEqual(self.at(alice, "rev-parse", "HEAD"), tip)
        self.assertEqual(self.at(origin, "rev-parse", "main"), tip)
        for clone in (alice, bob):
            self.assertEqual((clone / "notes.txt").read_bytes(), b"shared: ready\n")
            self.assertEqual((clone / "review.txt").read_bytes(), b"review: done\n")
            self.assertEqual(self.at(clone, "status", "--porcelain"), "")

    def test_conflict_resolution(self):
        self.seed()
        self.git("switch", "-c", "feat/review")
        self.write("status: ready")
        self.git("add", "notes.txt")
        self.commit("docs: propose ready")
        feature = self.git("rev-parse", "HEAD").strip()
        self.git("switch", "main")
        self.write("status: checked")
        self.git("add", "notes.txt")
        self.commit("docs: record check")
        before = self.git("rev-parse", "HEAD").strip()
        self.at(self.repo, "merge", "feat/review", expected=1)
        self.assertEqual(self.git("rev-parse", "MERGE_HEAD").strip(), feature)
        for stage, content in ((1, "draft"), (2, "checked"), (3, "ready")):
            self.assertEqual(self.git("show", f":{stage}:notes.txt"), f"status: {content}\n")
        self.assertEqual(len(self.git("ls-files", "-u", "--", "notes.txt").splitlines()), 3)
        self.write("status: reviewed")
        self.git("add", "notes.txt")
        self.git("diff", "--cached", "--check")
        self.commit("merge: reconcile review status")
        self.assertEqual(self.git("rev-list", "--parents", "-1", "HEAD").split()[1:], [before, feature])
        self.assertEqual(self.git("show", "HEAD:notes.txt"), "status: reviewed\n")
        self.assertEqual(self.git("status", "--porcelain"), "")

    def test_lost_commit_recovery(self):
        base = self.seed()
        self.write("status: recovered")
        self.git("add", "notes.txt")
        self.commit("docs: preserve recovery example")
        saved = self.git("rev-parse", "HEAD").strip()
        (self.root / "saved-tip.txt").write_text(saved, encoding="ascii")
        self.assertEqual(self.git("status", "--porcelain"), "")
        self.git("reset", "--hard", base)
        self.assertEqual(self.git("rev-parse", "main").strip(), base)
        candidate = self.git("rev-parse", "HEAD@{1}").strip()
        self.assertEqual(candidate, (self.root / "saved-tip.txt").read_text(encoding="ascii"))
        self.git("branch", "recovery/notes", candidate)
        self.assertEqual(self.git("rev-parse", "recovery/notes").strip(), saved)
        self.assertEqual(self.git("show", "recovery/notes:notes.txt"), "status: recovered\n")
        self.assertEqual(self.git("rev-parse", "main").strip(), base)
        self.assertEqual(self.git("status", "--porcelain"), "")

    def test_contribution_offline(self):
        base = self.seed()
        origin = self.local_origin()
        fork = self.root / "fork.git"
        self.git("clone", "--bare", str(origin), str(fork))
        contributor = self.clone(fork, "contributor")
        self.at(contributor, "remote", "add", "upstream", str(origin))
        self.at(contributor, "fetch", "upstream")
        self.at(contributor, "switch", "-c", "feat/clarify-notes")
        (contributor / "notes.txt").write_bytes(b"status: ready\n")
        self.at(contributor, "add", "notes.txt")
        self.at(contributor, "commit", "-m", "docs: clarify notes")
        self.at(contributor, "diff", "--check", "upstream/main...HEAD")
        self.at(contributor, "push", "-u", "origin", "feat/clarify-notes")
        reviewed = self.at(contributor, "rev-parse", "HEAD").strip()
        for bare in (origin, fork):
            self.assertEqual(self.at(bare, "rev-parse", "main").strip(), base)
        self.git("remote", "add", "contribution", str(fork))
        self.git("fetch", "contribution")
        self.git("diff", "--check", "main...contribution/feat/clarify-notes")
        self.git("merge", "--ff-only", "contribution/feat/clarify-notes")
        self.git("push", "origin", "main")
        self.assertEqual(self.at(origin, "rev-parse", "main").strip(), reviewed)
        self.assertEqual(self.at(fork, "rev-parse", "main").strip(), base)
        self.assertEqual(self.git("show", "HEAD:notes.txt"), "status: ready\n")
        self.assertEqual(self.git("status", "--porcelain"), "")

    def gate(self, revision, path):
        result = subprocess.run(["git", "show", f"{revision}:{path}"],
                                cwd=self.repo, env=self.env, capture_output=True,
                                timeout=30)
        return result.returncode == 0 and result.stdout == b"status: ready\n"

    def catalog_commit(self, data, message):
        (self.repo / "catalog.txt").write_bytes(data)
        self.git("add", "catalog.txt")
        self.commit(message)

    def test_quality_pipeline(self):
        self.catalog_commit(b"status: draft\n", "docs: initialize catalog")
        self.git("switch", "-c", "feat/ready-catalog")
        self.assertFalse(self.gate("HEAD", "catalog.txt"))
        (self.repo / "catalog.txt").write_bytes(b"status: ready\n")
        self.assertFalse(self.gate("HEAD", "catalog.txt"))
        self.catalog_commit(b"status: ready\n", "feat: mark catalog ready")
        self.assertTrue(self.gate("HEAD", "catalog.txt"))
        good = self.git("rev-parse", "HEAD").strip()
        self.git("switch", "-c", "test/invalid-catalog")
        self.catalog_commit(b"", "test: empty catalog")
        self.assertFalse(self.gate("HEAD", "catalog.txt"))
        self.catalog_commit(b"status: ready\nextra: invalid\n", "test: extra catalog line")
        self.assertFalse(self.gate("HEAD", "catalog.txt"))
        self.assertFalse(self.gate("HEAD", "absent.txt"))
        self.git("switch", "main")
        self.git("diff", "--check", "main...feat/ready-catalog")
        self.assertTrue(self.gate("feat/ready-catalog", "catalog.txt"))
        self.git("merge", "--ff-only", "feat/ready-catalog")
        self.assertEqual(self.git("rev-parse", "HEAD").strip(), good)
        self.assertTrue(self.gate("HEAD", "catalog.txt"))
        self.assertEqual(self.git("status", "--porcelain"), "")

    def test_release_management(self):
        self.catalog_commit(b"status: draft\n", "docs: initialize catalog")
        self.git("tag", "-a", "v1.0.0", "-m", "Initial draft contract")
        self.catalog_commit(b"status: draft\nstatus: ready\n", "feat: add ready status")
        self.git("tag", "-a", "v1.1.0", "-m", "Add backward-compatible ready status")
        released = self.git("rev-parse", "v1.1.0^{commit}").strip()
        for tag in ("v1.0.0", "v1.1.0"):
            self.assertEqual(self.git("cat-file", "-t", tag).strip(), "tag")
        archive = self.root / "catalog-v1.1.0.tar"
        self.git("archive", "--format=tar", "--output=" + str(archive), "v1.1.0")
        (self.repo / "future.txt").write_bytes(b"future work\n")
        self.git("add", "future.txt")
        self.commit("docs: begin future work")
        self.assertEqual(self.git("rev-parse", "v1.1.0^{commit}").strip(), released)
        self.assertNotEqual(self.git("rev-parse", "HEAD").strip(), released)
        self.assertEqual(self.git("show", "v1.0.0:catalog.txt"), "status: draft\n")
        self.assertEqual(self.git("show", "v1.1.0:catalog.txt"), "status: draft\nstatus: ready\n")
        with tarfile.open(archive) as artifact:
            self.assertEqual(artifact.getnames(), ["catalog.txt"])
            with artifact.extractfile("catalog.txt") as content:
                self.assertEqual(content.read(), b"status: draft\nstatus: ready\n")
        self.assertEqual(self.git("status", "--porcelain"), "")

    def test_professional_workflow(self):
        base = self.seed()
        self.git("switch", "-c", "feat/ready-notes")
        self.assertFalse(self.gate("HEAD", "notes.txt"))
        self.write("status: ready")
        self.git("add", "notes.txt")
        self.commit("feat: mark notes ready")
        (self.repo / "review.txt").write_bytes(b"R1: notes are ready\n")
        self.git("add", "review.txt")
        self.commit("docs: record readiness requirement")
        self.assertTrue(self.gate("HEAD", "notes.txt"))
        self.git("diff", "--check", "main...HEAD")
        reviewed = self.git("rev-parse", "HEAD").strip()
        tree = self.git("rev-parse", "HEAD^{tree}").strip()
        self.assertEqual(self.git("rev-list", "--count", "main..HEAD").strip(), "2")
        self.git("switch", "main")
        self.assertEqual(self.git("rev-parse", "HEAD").strip(), base)
        self.assertEqual(self.git("rev-parse", "feat/ready-notes").strip(), reviewed)
        self.git("merge", "--squash", "feat/ready-notes")
        self.assertEqual(self.git("rev-parse", "HEAD").strip(), base)
        self.assertFalse((self.repo / ".git" / "MERGE_HEAD").exists())
        self.git("diff", "--cached", "--check")
        self.commit("feat: deliver reviewed notes")
        self.assertEqual(self.git("rev-list", "--parents", "-1", "HEAD").split()[1:], [base])
        self.assertEqual(self.git("rev-parse", "HEAD^{tree}").strip(), tree)
        self.assertEqual(self.git("rev-list", "--count", "HEAD").strip(), "2")
        self.assertTrue(self.gate("HEAD", "notes.txt"))
        self.git("tag", "-a", "v1.0.0", "-m", "First reviewed notes release")
        self.assertEqual(self.git("rev-parse", "v1.0.0^{commit}"),
                         self.git("rev-parse", "HEAD"))
        self.assertEqual(self.git("status", "--porcelain"), "")
        self.assertEqual(self.git("remote"), "")


if __name__ == "__main__":
    unittest.main()
