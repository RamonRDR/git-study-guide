"""Local bare origin and independent clone collaboration tests."""
import os
from pathlib import Path
import subprocess
import tempfile
import unittest


class GitRemotesTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.origin = self.root / "origin.git"
        self.alice = self.root / "alice"
        self.bob = self.root / "bob"
        seed = self.root / "seed"
        home = self.root / "home"
        template = self.root / "template"
        for folder in (seed, home, template):
            folder.mkdir()
        config = self.root / "gitconfig"
        config.touch()
        self.env = {k: v for k, v in os.environ.items()
                    if not k.upper().startswith("GIT_")}
        self.env.update(HOME=str(home), USERPROFILE=str(home),
                        GIT_CONFIG_GLOBAL=str(config), GIT_CONFIG_NOSYSTEM="1",
                        GIT_TEMPLATE_DIR=str(template), GIT_TERMINAL_PROMPT="0",
                        GIT_CONFIG_COUNT="0", GIT_ALLOW_PROTOCOL="file")
        self.git(self.root, "init", "--bare", "--initial-branch=main", str(self.origin))
        self.git(seed, "init", "--initial-branch=main")
        self.identity(seed)
        self.base = self.commit(seed, "note.txt", "practice")
        self.git(seed, "remote", "add", "origin", str(self.origin))
        self.git(seed, "push", "-u", "origin", "main")
        for clone in (self.alice, self.bob):
            self.git(self.root, "clone", "--no-local", str(self.origin), str(clone))
            self.identity(clone)

    def run_git(self, repo, *args):
        self.assertTrue(repo.resolve().is_relative_to(self.root))
        return subprocess.run(["git", *args], cwd=repo, env=self.env,
                              capture_output=True, text=True, timeout=30)

    def git(self, repo, *args):
        result = self.run_git(repo, *args)
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout.strip()

    def identity(self, repo):
        for key, val in (("user.name", "Study Guide Example"),
                         ("user.email", "learner@example.invalid"),
                         ("commit.gpgsign", "false"), ("core.autocrlf", "false")):
            self.git(repo, "config", "--local", key, val)

    def ref(self, repo, name="HEAD"):
        return self.git(repo, "rev-parse", name)

    def commit(self, repo, filename, content):
        (repo / filename).write_bytes((content + "\n").encode("ascii"))
        self.git(repo, "add", "--", filename)
        for key in ("GIT_AUTHOR_IDENT", "GIT_COMMITTER_IDENT"):
            self.assertTrue(self.git(repo, "var", key).startswith(
                "Study Guide Example <learner@example.invalid> "))
        self.git(repo, "commit", "-m", "docs: update " + filename)
        return self.ref(repo)

    def push(self, repo, branch="main"):
        self.assertEqual(Path(self.git(repo, "remote", "get-url", "--push",
                                       "origin")).resolve(), self.origin)
        self.git(repo, "push", "origin", branch)

    def counts(self, repo):
        return tuple(map(int, self.git(repo, "rev-list", "--left-right",
                                      "--count", "main...origin/main").split()))

    def clean(self, repo):
        self.assertEqual(self.git(repo, "status", "--porcelain=v1"), "")

    def alice_update(self):
        tip = self.commit(self.alice, "alice.txt", "alice update")
        self.push(self.alice)
        return tip

    def diverge(self):
        a = self.alice_update()
        b = self.commit(self.bob, "bob.txt", "bob update")
        return a, b

    def test_bare_and_independent_clones(self):
        self.assertEqual(self.git(self.origin, "rev-parse", "--is-bare-repository"), "true")
        self.assertEqual(self.git(self.origin, "symbolic-ref", "HEAD"), "refs/heads/main")
        self.assertFalse((self.origin / "note.txt").exists())
        for repo in (self.alice, self.bob):
            self.assertEqual(Path(self.git(repo, "rev-parse", "--show-toplevel")).resolve(), repo)
            self.assertEqual(self.ref(repo), self.base)
            self.assertEqual(self.git(repo, "symbolic-ref", "HEAD"), "refs/heads/main")
            self.assertEqual(self.git(repo, "rev-parse", "--symbolic-full-name",
                                      "@{upstream}"), "refs/remotes/origin/main")
        (self.alice / "local.txt").write_text("local", encoding="ascii")
        self.assertFalse((self.bob / "local.txt").exists())

    def test_remote_alias_configuration(self):
        self.git(self.alice, "remote", "add", "upstream", str(self.origin))
        self.git(self.alice, "remote", "set-url", "upstream", str(self.origin))
        self.git(self.alice, "remote", "rename", "upstream", "training")
        self.assertEqual(Path(self.git(self.alice, "remote", "get-url", "training")).resolve(),
                         self.origin)
        self.git(self.alice, "remote", "remove", "training")
        self.assertEqual(self.git(self.alice, "remote"), "origin")
        self.assertEqual(self.ref(self.origin, "refs/heads/main"), self.base)

    def test_fetch_updates_tracking_not_head_index_or_files(self):
        tip = self.alice_update()
        self.assertEqual(self.ref(self.origin, "refs/heads/main"), tip)
        self.assertEqual(self.ref(self.alice, "origin/main"), tip)
        self.assertEqual(self.ref(self.bob, "origin/main"), self.base)
        index = self.git(self.bob, "write-tree")
        self.git(self.bob, "fetch", "origin")
        self.assertEqual(self.ref(self.bob, "origin/main"), tip)
        self.assertEqual(self.ref(self.bob), self.base)
        self.assertEqual(self.git(self.bob, "write-tree"), index)
        self.assertFalse((self.bob / "alice.txt").exists())
        self.assertEqual(self.counts(self.bob), (0, 1))
        self.clean(self.bob)

    def test_ahead_and_fast_forward_sync(self):
        tip = self.commit(self.alice, "alice.txt", "alice update")
        self.assertEqual(self.counts(self.alice), (1, 0))
        self.push(self.alice)
        self.git(self.bob, "fetch", "origin")
        self.git(self.bob, "merge", "--ff-only", "origin/main")
        self.assertEqual(self.ref(self.bob), tip)
        self.assertEqual(self.counts(self.bob), (0, 0))
        self.assertEqual(self.git(self.bob, "show", "HEAD:alice.txt"), "alice update")
        self.clean(self.bob)

    def test_rejected_push_preserves_both_histories(self):
        a, b = self.diverge()
        result = self.run_git(self.bob, "push", "origin", "main")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.ref(self.origin, "refs/heads/main"), a)
        self.assertEqual(self.ref(self.bob), b)
        self.git(self.bob, "fetch", "origin")
        self.assertEqual(self.counts(self.bob), (1, 1))
        self.clean(self.bob)

    def test_ff_only_refusal_and_merge_sync(self):
        a, b = self.diverge()
        result = self.run_git(self.bob, "pull", "--ff-only", "origin", "main")
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.ref(self.bob), b)
        self.assertEqual(self.ref(self.bob, "origin/main"), a)
        self.assertEqual(self.counts(self.bob), (1, 1))
        self.clean(self.bob)
        self.git(self.bob, "merge", "--no-edit", "origin/main")
        self.assertEqual(self.git(self.bob, "rev-list", "--parents", "-1", "HEAD").split()[1:],
                         [b, a])
        m = self.ref(self.bob)
        self.push(self.bob)
        self.git(self.alice, "pull", "--ff-only", "origin", "main")
        for repo in (self.alice, self.bob):
            self.assertEqual(self.ref(repo), m)
            self.assertEqual(self.git(repo, "show", "HEAD:alice.txt"), "alice update")
            self.assertEqual(self.git(repo, "show", "HEAD:bob.txt"), "bob update")
            self.clean(repo)
        self.assertEqual(self.ref(self.origin, "refs/heads/main"), m)

    def test_unpublished_rebase_then_normal_push(self):
        a, b = self.diverge()
        self.git(self.bob, "branch", "backup/bob")
        self.git(self.bob, "pull", "--rebase", "origin", "main")
        self.assertEqual(self.ref(self.bob, "HEAD^"), a)
        self.assertNotEqual(self.ref(self.bob), b)
        self.assertEqual(self.ref(self.bob, "backup/bob"), b)
        self.assertEqual(self.git(self.bob, "show", "HEAD:bob.txt"), "bob update")
        self.push(self.bob)
        self.assertEqual(self.ref(self.origin, "refs/heads/main"), self.ref(self.bob))

    def test_publish_track_integrate_delete_and_prune(self):
        branch = "feat/summary"
        self.git(self.alice, "switch", "-c", branch)
        tip = self.commit(self.alice, "summary.txt", "summary ready")
        self.git(self.alice, "push", "-u", "origin", branch)
        self.assertEqual(self.git(self.alice, "rev-parse", "--symbolic-full-name",
                                  "@{upstream}"), "refs/remotes/origin/" + branch)
        self.git(self.bob, "fetch", "origin")
        self.git(self.bob, "switch", "--track", "origin/" + branch)
        self.assertEqual(self.ref(self.bob), tip)
        self.assertEqual(self.git(self.bob, "rev-parse", "--symbolic-full-name",
                                  "@{upstream}"), "refs/remotes/origin/" + branch)
        self.git(self.bob, "switch", "main")
        self.git(self.alice, "switch", "main")
        self.git(self.alice, "merge", "--ff-only", branch)
        self.push(self.alice)
        self.git(self.bob, "pull", "--ff-only", "origin", "main")
        self.git(self.alice, "fetch", "origin")
        self.git(self.alice, "merge-base", "--is-ancestor", "origin/" + branch, "origin/main")
        self.assertEqual(self.ref(self.origin, "refs/heads/" + branch), tip)
        self.git(self.alice, "push", "--delete", "origin", branch)
        self.assertEqual(self.run_git(self.origin, "show-ref", "--verify", "--quiet",
                                      "refs/heads/" + branch).returncode, 1)
        self.assertEqual(self.ref(self.bob, "origin/" + branch), tip)
        self.git(self.bob, "fetch", "--prune", "origin")
        self.assertEqual(self.run_git(self.bob, "show-ref", "--verify", "--quiet",
                                      "refs/remotes/origin/" + branch).returncode, 1)
        self.assertEqual(self.ref(self.bob, branch), tip)
        for repo in (self.alice, self.bob):
            self.git(repo, "branch", "-d", branch)
            self.assertEqual(self.ref(repo), tip)
            self.assertEqual(self.git(repo, "show", "HEAD:summary.txt"), "summary ready")
            self.clean(repo)
        self.assertEqual(self.ref(self.origin, "refs/heads/main"), tip)


if __name__ == "__main__":
    unittest.main()
