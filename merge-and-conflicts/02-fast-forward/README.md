# Fast-forward merge

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../01-integration-safety/README.md) · [Index](../README.md) · [Next](../03-merge-commit/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 25 min

**Prerequisites:** [Integration safety and recovery first](../01-integration-safety/README.md)

**Objective:** Advance a branch without creating a merge commit and verify ancestry.

## What and why

If the target tip is an ancestor of the source tip, integration can fast-forward: move the target branch to the source commit and update index/working tree. No new commit is necessary. `git merge --ff-only SOURCE` refuses when fast-forward is impossible. In a diverged graph it avoids an unexpected merge commit. Use explicit flags rather than relying on defaults or configuration.

## Practice

Create a NEW isolated disposable lab using module 00 chapter 03 and its first-commit lesson. Keep the original dedicated shell, not the editor terminal. The initial main must contain exactly one commit, note.txt = practice, with clean status. Close any previous lab shell before starting. Follow the safety checks from chapter 01 before every history-changing operation.

[Isolated lab setup](../../getting-started/03-first-repository/README.md) · [First commit](../../getting-started/05-first-commit/README.md) · [Integration safety and recovery first](../01-integration-safety/README.md)

```text
git rev-parse --show-toplevel
git branch --show-current
git status --short
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Stop unless root is your disposable lab, current branch is the one specified, status is clean before starting an operation, and both identities start with `Study Guide Example <learner@example.invalid>`. Before each commit also inspect the staged diff; stop on unexpected output.

```text
git switch -c feat/note
```

In the plain-text editor, create or edit note.txt to contain exactly one line: feature, with a final newline. Save, then stage in the dedicated shell:

```text
git add -- note.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

If diff and both identities are correct, commit:

```text
git commit -m "docs: revise feature note"
```

```text
git switch main
git log --all --oneline --graph --decorate
git rev-parse main feat/note
git status --short
```

Confirm clean main at C1, source C2; C2 has C1 as parent. Then:

```text
git merge --ff-only feat/note
git rev-parse main feat/note
git rev-list --count main
git show HEAD:note.txt
git status --short
```

Expected: identical tip IDs, two commits on main, feature content and clean status. Diagram before: main -> C1; feat/note -> C2 -> C1. After: main and feat/note -> C2 -> C1. No third commit.

## Common mistakes and safety

If --ff-only refuses, inspect the graph; do not force movement. Do not use --abort after a completed fast-forward: no merge is in progress. Keep source refs until verification.

After each independent lab, close the editor and dedicated shell, then delete only the exact temporary parent folder you recorded in module 00 using the file manager if you no longer need it. Never delete the guide, home or work repository.

## Exercise and self-check

Does fast-forward add a commit? Answer: no; main moves to existing C2. Pass if main and feat/note resolve to the same ID. Professional use: enforce linear integration when the target has no unique commits.

## Quick reference

- `git merge --ff-only SOURCE`
- `git rev-parse main SOURCE`

## Official sources

- [Git: git-merge](https://git-scm.com/docs/git-merge)
- [Git: git-rev-parse](https://git-scm.com/docs/git-rev-parse)
- [Git: git-rev-list](https://git-scm.com/docs/git-rev-list)
