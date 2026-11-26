# Divergence and merge commits

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../02-fast-forward/README.md) · [Index](../README.md) · [Next](../04-conflict-resolution/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 35 min

**Prerequisites:** [Fast-forward merge](../02-fast-forward/README.md)

**Objective:** Distinguish a two-parent merge from a fast-forward and verify both parents.

## What and why

When both branches have unique commits, neither tip is an ancestor of the other. A normal two-head merge combines changes using their common base. A successful merge commit records the combined snapshot with two parents (first: previous target; second: source). `--no-ff` requests a merge commit even where a fast-forward could otherwise occur, except when already up to date. `--no-edit` accepts the generated message. A merge commit preserves the ancestry of both lines.

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
```

In the plain-text editor, create or edit overview.txt to contain exactly one line: overview, with a final newline. Save, then stage in the dedicated shell:

```text
git add -- overview.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

If diff and both identities are correct, commit:

```text
git commit -m "docs: add overview"
```

```text
git rev-parse --show-toplevel
git branch --show-current
git status --short
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Confirm clean main, fictional identities and the intended divergent graph. First try the guarded operation (expected to fail without changing history):

```text
git log --all --graph --oneline --decorate
git rev-parse main feat/note
git merge --ff-only feat/note
```

After refusal, verify both tips and status are unchanged. Then merge:

```text
git status --short
git rev-parse main feat/note
git merge --no-ff --no-edit feat/note
git log --all --graph --oneline --decorate
git rev-list --parents -1 HEAD
git show HEAD:note.txt
git show HEAD:overview.txt
git status --short
```

Expected: new M with two parents, note feature and overview overview; clean status. Before: C2 -> C1 <- C3 (C2 source, C3 target; arrows point to parents). After: main -> M, M -> C3 and C2, both -> C1; feat/note still -> C2. rev-list outputs three IDs: M then C3 then C2.

## Common mistakes and safety

If an unexpected conflict occurs, use status and the ordinary merge abort from chapter 01; do not stage random content. Inspect both branches before integration; never infer correctness from a successful merge alone.

After each independent lab, close the editor and dedicated shell, then delete only the exact temporary parent folder you recorded in module 00 using the file manager if you no longer need it. Never delete the guide, home or work repository.

## Exercise and self-check

Why did --ff-only refuse? Both tips have unique commits. Pass if the merge has exactly two parents and both file contents. Professional use: preserve integration history when team policy permits merge commits.

## Quick reference

- `git merge --no-ff --no-edit SOURCE`
- `git rev-list --parents -1 HEAD`

## Official sources

- [Git: git-merge](https://git-scm.com/docs/git-merge)
- [Git: git-rev-list](https://git-scm.com/docs/git-rev-list)
- [Git: git-log](https://git-scm.com/docs/git-log)
