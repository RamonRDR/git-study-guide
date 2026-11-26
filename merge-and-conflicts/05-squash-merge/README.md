# Squash integration

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../04-conflict-resolution/README.md) · [Index](../README.md) · [Next](../06-rebase-and-conflicts/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 30 min

**Prerequisites:** [Resolve and abort merge conflicts](../04-conflict-resolution/README.md)

**Objective:** Combine changes into one new commit without joining source ancestry.

## What and why

`git merge --squash SOURCE` prepares the combined working tree and index like a merge but does not move HEAD, create a commit or set MERGE_HEAD. A subsequent ordinary commit has one parent, the previous target tip. Source commits remain on their branch; their changes can be represented in a new combined snapshot without their original ancestry. GitHub's squash merge is a platform integration option with similar one-commit topology, not literally this local command or a guarantee of identical metadata.

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

In the plain-text editor, create or edit detail.txt to contain exactly one line: detail, with a final newline. Save, then stage in the dedicated shell:

```text
git add -- detail.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

If diff and both identities are correct, commit:

```text
git commit -m "docs: add detail"
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

Confirm clean main and identities. Record main and feature IDs. Then prepare squash, without committing yet:

```text
git rev-parse main feat/note
git merge --squash feat/note
git rev-parse HEAD
git diff --cached
git status --short
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

HEAD unchanged; note modification and detail addition staged. If conflict or unexpected state, stop; merge --abort is not a squash undo. In this lab discard only the verified disposable folder and start again. If correct, commit:

```text
git commit -m "docs: integrate feature changes"
git rev-list --parents -1 HEAD
git log --oneline main..feat/note
git show HEAD:note.txt
git show HEAD:detail.txt
git show HEAD:overview.txt
git status --short
```

Expected one parent, two source commits still listed by main..feat/note, all three contents present and clean state. Diagram: main -> S -> C4 -> C1; feat/note -> C3 -> C2 -> C1. S contains feature changes but C3 is not a parent/ancestor of S in this lab.

## Common mistakes and safety

Do not use squash to erase a secret from existing history. Source ancestry remains on source branch. Guarded deletion may refuse after squash; inspect content and policy rather than forcing deletion. No shared branch operation here.

After each independent lab, close the editor and dedicated shell, then delete only the exact temporary parent folder you recorded in module 00 using the file manager if you no longer need it. Never delete the guide, home or work repository.

## Exercise and self-check

Is a squash commit a two-parent merge commit? No. Pass if HEAD stays unchanged until commit, new commit has one parent and source changes are present. Professional use: combine small review commits into one logical change under an agreed policy.

## Quick reference

- `git merge --squash SOURCE`
- `git diff --cached`
- `git commit -m MESSAGE`

## Official sources

- [Git: git-merge](https://git-scm.com/docs/git-merge)
- [Git: git-commit](https://git-scm.com/docs/git-commit)
- [Git: git-rev-list](https://git-scm.com/docs/git-rev-list)
- [Git: git-log](https://git-scm.com/docs/git-log)
