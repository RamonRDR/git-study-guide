# Refs and HEAD: naming object IDs

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../04-object-hashes/README.md) · [Index](../README.md) · [Next](../06-index-internals/README.md)
<!-- /navigation -->

**Level:** advanced · **Estimated time:** 40 min

**Prerequisites:** [14 Git Internals](../README.md) · [Advanced Git](../../advanced-git/README.md)

**Objective:** A branch ref normally names a commit and advances on commits made on that branch.

## What and why

A branch ref normally names a commit and advances on commits made on that branch. HEAD normally is a symbolic ref to a branch; detached HEAD directly identifies a commit. Refs can be packed or stored by different backends, so reading a specific file in .git is not portable. Use ref-aware commands for tooling.

```text
HEAD -> refs/heads/main -> commit C
HEAD (detached) ----------> commit P
```

HEAD → refs/heads/main → commit; detached HEAD → commit.

## Practice

Create a fresh isolated fixture from the linked Advanced Git module index before each practice. Run commands individually and stop on unexpected results. Confirm root and printed sandbox. Git 2.34+ practice baseline, Bash (Git Bash on Windows).

Inspect symbolic HEAD, refs and resolved commit. Detach at the parent only in the disposable clean fixture; symbolic-ref -q HEAD then returns nonzero. Restore main and verify clean state. If work exists in detached HEAD, preserve it with a branch before switching.

```bash
git symbolic-ref HEAD
git show-ref
git rev-parse HEAD
git switch --detach HEAD~1
git symbolic-ref -q HEAD
git rev-parse HEAD
git switch main
git status --short
```

## Common mistakes and safety

Use the disposable fixture only. Never modify object or ref files by hand, force pruning, or run experiments against a real repository. If state differs, inspect with status, log and read-only plumbing; close the dedicated shell and remove only the recorded sandbox through the file manager after reviewing contents.

## Exercise and self-check

HEAD → refs/heads/main → commit; detached HEAD → commit. Which ref moves when committing detached? No branch ref moves automatically.

## Quick reference

- `git symbolic-ref HEAD`
- `git show-ref`
- `git rev-parse HEAD`
- `git switch --detach HEAD~1`

## Official sources

- [https://git-scm.com/docs/git-symbolic-ref](https://git-scm.com/docs/git-symbolic-ref)
- [https://git-scm.com/docs/git-show-ref](https://git-scm.com/docs/git-show-ref)
- [https://git-scm.com/docs/git-switch](https://git-scm.com/docs/git-switch)

---

<!-- navigation-footer -->
[Previous](../04-object-hashes/README.md) · [Index](../README.md) · [Next](../06-index-internals/README.md)
<!-- /navigation-footer -->
