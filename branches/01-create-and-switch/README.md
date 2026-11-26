# Create and switch local branches

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
— · [Index](../README.md) · [Next](../02-start-points-and-comparison/README.md)
<!-- /navigation -->

**Level:** beginner · **Estimated time:** 35 min

**Prerequisites:** [Isolated lab setup](../../getting-started/03-first-repository/README.md) · [First commit](../../getting-started/05-first-commit/README.md) · [Basic commands](../../basic-commands/README.md)

**Objective:** Create branch references and verify which reference HEAD selects.

## What and why

A local branch is a movable reference to a commit, not a second folder or a full project copy. Creating a branch at HEAD adds a reference without changing the index or working tree. Switching selects the target branch and updates tracked files/index as needed. A commit normally advances only the checked-out branch. `git branch NAME [START]` creates without switching; `git switch NAME` switches; `git switch -c NAME [START]` creates and switches. Git 2.23 introduced switch; our lab requires 2.40+ from module 00. Older tutorials use checkout for both branch switching and other operations; this guide prefers switch for clarity.

## Practice

Start a NEW disposable repository using the isolated setup in module 00 chapter 03 and first commit from chapter 05. Do not use this guide's repository. Keep the dedicated shell through this module. Expect exactly one commit on main containing note.txt with practice and clean status. Verify root, status and identities before continuing.

```text
git rev-parse --show-toplevel
git status --short
git log --oneline
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

If the root is not your lab, status is not clean, or either identity is not fictional, stop. Otherwise run:

```text
git branch feat/note
git branch --list
git symbolic-ref HEAD
git rev-parse main feat/note
git switch feat/note
git branch --show-current
git status --short
```

Initially both branch IDs match and HEAD is refs/heads/main; after switch HEAD names feat/note. The file still contains practice. Text diagram: HEAD -> feat/note -> C1; main -> C1. Both names point to C1. Edit note.txt to feature (one line, final newline), save and stage only that file:

```text
git add -- note.txt
git diff --cached -- note.txt
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Only if the staged change and both identities are correct:

```text
git commit -m "docs: revise feature note"
git log --oneline --all --graph --decorate
git switch main
git show HEAD:note.txt
git status --short
git switch feat/note
git show HEAD:note.txt
```

Expected: main still points to C1 with practice; feat/note points to C2 with feature. Text diagram: main -> C1; HEAD -> feat/note -> C2 -> C1 (last arrow is parent history). Switching is not merging.

## Common mistakes and safety

Check status before switching; compatible uncommitted edits can follow you, and conflicting edits can block the switch. Do not use force/discard options. Do not create branches from an unintended HEAD. No remote exists in this lab.

## Exercise and self-check

Predict the main commit after the feature commit. Answer: unchanged. Pass if branch --show-current and both file versions match. Professional use: isolate a small change before review.

## Quick reference

`git branch NAME [START]`: create; `git switch NAME`: select; `git switch -c NAME [START]`: create and select; `git branch --show-current`: active branch.

## Official sources

- [Git: git-branch](https://git-scm.com/docs/git-branch)
- [Git: git-switch](https://git-scm.com/docs/git-switch)
- [Git: git-symbolic-ref](https://git-scm.com/docs/git-symbolic-ref)
