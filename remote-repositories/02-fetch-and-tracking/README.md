# Fetch, references and upstream tracking

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../01-remote-concepts/README.md) · [Index](../README.md) · [Next](../03-pull-push-and-divergence/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 30 min

**Prerequisites:** [Remotes, bare repositories and clones](../01-remote-concepts/README.md)

**Objective:** Observe a remote update before and after fetch without changing Bob's working tree.

## What and why

HEAD normally points to refs/heads/main. The remote has its own refs/heads/main; Bob's refs/remotes/origin/main is a local record of the last known remote tip. Fetch downloads objects and updates configured refs (and FETCH_HEAD), not the checked-out branch, index or working files in this normal clone. Push requests a remote update and can update the pushing clone's tracking ref. The configured upstream lets status and branch -vv compare local history to its tracking ref, not live server state. Ahead/behind count commits unique to each side.

## Practice

Continue chapter 01 in the recorded parent. Before each change, check the target clone root, branch, clean status, push/fetch URLs and fictional author and committer identities; the sample below is for Alice, substitute bob when acting as Bob. Both identities must start with `Study Guide Example <learner@example.invalid>`. Before every commit repeat both identity checks and inspect the staged diff. Run commands individually and stop if any unexpected state.
```text
git -C alice rev-parse --show-toplevel
git -C alice branch --show-current
git -C alice status --short
git -C alice var GIT_AUTHOR_IDENT
git -C alice var GIT_COMMITTER_IDENT
git -C alice remote get-url --push origin
```
Create alice/alice.txt in a plain-text editor with line `alice update` and final newline. Stage and inspect; commit only if expected, then push only to the verified local origin.
```text
git -C alice add -- alice.txt
git -C alice diff --cached
git -C alice commit -m "docs: add Alice note"
git -C alice push origin main
git -C origin.git rev-parse refs/heads/main
git -C bob rev-parse HEAD refs/remotes/origin/main
git -C bob fetch origin
git -C bob rev-parse HEAD refs/remotes/origin/main
git -C bob rev-list --left-right --count main...origin/main
git -C bob log --oneline main..origin/main
git -C bob diff main origin/main
git -C bob branch -vv
git -C bob config --get remote.origin.fetch
```
Before Bob fetches, origin main has C2, Bob main and origin/main still C1. After fetch, origin/main = C2 while HEAD/main = C1; count is 0 1, alice.txt is absent in Bob's working tree. The default fetch refspec `+refs/heads/*:refs/remotes/origin/*` maps remote branch refs to local tracking refs; + allows tracking ref updates even when the remote history changed non-fast-forward. It is not permission to force push. `main..origin/main` lists commits reachable from origin/main but not main. Compare snapshots with diff before integrating. Verify Bob clean and on main, then:
```text
git -C bob merge --ff-only origin/main
git -C bob rev-parse HEAD origin/main
git -C bob show HEAD:alice.txt
git -C bob status --short
```
Expected: equal tips, alice update in Bob, clean status. Professional use: fetch and inspect before integrating teammates' work.

## Common mistakes and safety

Do not treat origin/main as live server data or edit it directly. Do not assume fetch resolves conflicts. If fast-forward refuses, inspect divergence instead of forcing.

## Exercise and self-check

After Alice pushes, but before Bob fetches, can Bob be behind while status says up to date? Hint: local tracking. Answer: yes; its cached reference is stale. Pass if fetch changes only Bob's tracking tip and subsequent merge advances main.

## Quick reference

- `git fetch origin`
- `git branch -vv`
- `git rev-list --left-right --count main...origin/main`
- `git merge --ff-only origin/main`

## Official sources

- [Git: git-fetch](https://git-scm.com/docs/git-fetch)
- [Git: git-branch](https://git-scm.com/docs/git-branch)
- [Git: git-rev-list](https://git-scm.com/docs/git-rev-list)
- [Git: git-merge](https://git-scm.com/docs/git-merge)
