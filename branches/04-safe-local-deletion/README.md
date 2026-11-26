# Safe local branch deletion

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../03-switch-safety-and-naming/README.md) · [Index](../README.md) · [Next](../05-detached-head/README.md)
<!-- /navigation -->

**Level:** beginner · **Estimated time:** 25 min

**Prerequisites:** [Switching safely and branch naming](../03-switch-safety-and-naming/README.md)

**Objective:** Identify reachable commits and delete only an already-contained local branch.

## What and why

Deleting a branch removes its name, not immediately every object it referenced. If commits are not reachable from surviving references, eventual cleanup may make them unrecoverable. `git branch --merged main` lists branches whose tips are ancestors of main or main itself; `--no-merged main` lists others. `git branch -d NAME` checks whether the branch is fully merged into its configured upstream, or HEAD if none; it does not always check main. In this lab there is no upstream. `-D` overrides merged-status protection and can lose the only named access to work; do not execute it. A branch checked out in a worktree cannot be deleted this way. Review reachability relative to the intended surviving branch before removal.

## Practice

Continue the isolated lab on main with clean status. archive/base still points to C1; feat/note-revision and docs/overview have separate commits. Inspect:

```text
git rev-parse --show-toplevel
git branch --show-current
git status --short
git branch --merged main
git branch --no-merged main
git log --oneline main..archive/base
git log --oneline main..feat/note-revision
```

Expected: archive/base and main are contained; feature and docs are not. The first range is empty; second has a commit. Delete ONLY archive/base after confirming it is contained and not current:

```text
git branch -d archive/base
git branch --list
git log -1 --oneline main
```

The old name disappears, C1 remains on main. Next intentionally demonstrate protection against deleting unmerged work; do NOT substitute -D:

```text
git branch -d feat/note-revision
```

Expected nonzero refusal. Verify branch still exists, its distinct commit remains and main is unchanged:

```text
git branch --list
git log --oneline main..feat/note-revision
git status --short
```

## Common mistakes and safety

Do not force-delete any branch here. A squash merge may preserve content without preserving ancestry, so a failed -d is not proof work is absent from another snapshot; inspect history and content, seek review, and keep the branch if unsure. Merge strategies arrive in module 05. Remote tracking and remote deletion arrive in module 06; no push commands in this module.

## Exercise and self-check

Which branch may be safely removed in this specific lab? Answer: archive/base, whose tip is already reachable from main. Pass if feature remains after the refusal. Professional use: review merged status, intended target and team policy before cleanup.

## Quick reference

`git branch --merged main`: contained tips; `git branch --no-merged main`: other tips; `git branch -d NAME`: guarded local deletion.

## Official sources

- [Git: git-branch](https://git-scm.com/docs/git-branch)
- [Git: git-log](https://git-scm.com/docs/git-log)
- [Git: gitrevisions](https://git-scm.com/docs/gitrevisions)

---

<!-- navigation-footer -->
[Previous](../03-switch-safety-and-naming/README.md) · [Index](../README.md) · [Next](../05-detached-head/README.md)
<!-- /navigation-footer -->
