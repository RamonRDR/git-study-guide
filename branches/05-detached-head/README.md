# Detached HEAD and preserving work

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../04-safe-local-deletion/README.md) · [Index](../README.md) · [Next module](../../merge-and-conflicts/README.md)
<!-- /navigation -->

**Level:** beginner · **Estimated time:** 30 min

**Prerequisites:** [Safe local branch deletion](../04-safe-local-deletion/README.md)

**Objective:** Inspect an earlier commit and give a detached commit a persistent branch name.

## What and why

Normally HEAD is a symbolic ref to a branch. Detached HEAD points directly to a commit. You can inspect a historical snapshot or test a version without moving a branch. New commits made while detached advance HEAD itself, not a named branch. Before leaving a detached commit you want to keep, create a branch at it. Otherwise the commit may eventually become unreachable and be removed; reflog recovery is not guaranteed. Text diagram: attached HEAD -> main -> C1; detached HEAD -> C1, main -> C1; after detached commit HEAD -> C4 -> C1, main remains C1.

## Practice

Continue the lab on main with clean status. Confirm root, then enter detached HEAD at main:

```text
git rev-parse --show-toplevel
git status --short
git switch --detach main
git branch --show-current
git status
git rev-parse HEAD main
```

Expected: branch --show-current is empty; status mentions detached HEAD; IDs match. Create experiment.txt containing experiment with a final newline, stage and inspect:

```text
git add -- experiment.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Only if fictional identities and expected diff:

```text
git commit -m "docs: record experiment"
git rev-parse HEAD main
git log -1 --oneline
```

HEAD now differs from main. BEFORE switching away, save the commit by creating and selecting a named branch at current HEAD:

```text
git switch -c experiment/saved
git branch --show-current
git rev-parse HEAD experiment/saved
git status --short
git switch main
git ls-files
git show experiment/saved:experiment.txt
git branch --list
```

Expected: both saved IDs match; main does not contain experiment.txt; git show reads experiment from saved branch. No integration was performed. To inspect another historical commit without creating work, choose an existing commit ID or local ref with clean status and return with git switch main. If you already left a detached commit and know its ID, inspect git show ID and create a branch at it while it still exists; detailed recovery later.

## Common mistakes and safety

Do not switch away until desired detached work has a named reference. Do not rely on automatic recovery or use force. Keep the lab only if needed; otherwise close editor and dedicated shell and delete only its exact recorded temporary parent folder with the file manager, per module 00.

## Exercise and self-check

Explain why branch creation saved the detached commit without merging. Answer: the new reference names the existing commit; main is unchanged. Pass if saved content is readable from main and status is clean. Professional use: investigate an old release without moving shared history.

## Quick reference

`git switch --detach REF`: inspect without branch; `git switch -c NAME`: name current commit and attach HEAD; `git branch --show-current`: empty while detached.

## Official sources

- [Git: git-switch](https://git-scm.com/docs/git-switch)
- [Git: git-checkout](https://git-scm.com/docs/git-checkout)
- [Git: git-branch](https://git-scm.com/docs/git-branch)
- [Git: git-symbolic-ref](https://git-scm.com/docs/git-symbolic-ref)

---

<!-- navigation-footer -->
[Previous](../04-safe-local-deletion/README.md) · [Index](../README.md) · [Next module](../../merge-and-conflicts/README.md)
<!-- /navigation-footer -->
