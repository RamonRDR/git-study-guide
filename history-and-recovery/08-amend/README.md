# Amend an unpublished commit

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../07-cherry-pick/README.md) · [Index](../README.md) · —
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 25 min

**Prerequisites:** [Isolated lab](../../getting-started/03-first-repository/README.md) · [First commit](../../getting-started/05-first-commit/README.md) · [Merge and conflicts](../../merge-and-conflicts/README.md) · [Remotes](../../remote-repositories/README.md) · [Cherry-pick selected commits](../07-cherry-pick/README.md)

**Objective:** Correct a private tip while keeping its original parent and a recovery reference.

## What and why

`git commit --amend` replaces the current tip with a commit based on the index and normally retains its parents; it can change the message and/or content. Changed content or message yields a new ID. `--no-edit` retains the message. It is not editing a commit object in place. Use for unpublished commits only; on shared branches, add a corrective commit or revert instead. Diagram: C1 -> C2 (old); main moves to C2' with same parent C1; backup stays at C2.

## Practice

Start a NEW independent disposable lab using the linked setup and first-commit lessons. Keep the dedicated Bash or PowerShell shell in the recorded repo directory, with system/global Git config isolated, inherited Git variables cleared and empty templates. Use Git 2.40 or later. The initial main must contain exactly one commit with note.txt = practice, no remotes and clean status. Run every command individually. Before any mutation, repeat the inspection below: root must be the recorded disposable repo, branch must be the one specified, remotes empty, status exactly as described; both identities must begin with `Study Guide Example <learner@example.invalid>`. Before every commit also inspect staged changes and both identities. Stop on unexpected output or failure. Never execute these labs in the guide or a real project.

```text
git rev-parse --show-toplevel
git branch --show-current
git remote -v
git status --short
git diff
git diff --cached
git log --oneline --all --graph --decorate
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Edit note.txt in a plain-text editor to exactly one line `draft version` with final newline. Save, then return to the dedicated shell.

```text
git add -- note.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Only if the staged diff and both identities are correct, continue:

```text
git commit -m "docs: add draft"
git branch backup/draft
git rev-parse HEAD HEAD^
git status --short
```

Edit note.txt in a plain-text editor to exactly one line `final version` with final newline. Save, then return to the dedicated shell.

```text
git add -- note.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Only if the staged diff and both identities are correct, continue:

```text
git commit --amend -m "docs: add final version"
git rev-parse HEAD backup/draft
git rev-parse HEAD^ backup/draft^
git show HEAD:note.txt
git show backup/draft:note.txt
git rev-list --count HEAD
git status --short
```

Expected different tip IDs, same parent IDs, two commits reachable from main, final version in HEAD and draft version in backup. Professional use: fix a forgotten file or typo before publishing. For a message-only correction confirm index unchanged before amending.

After the exercise, close editors and the dedicated shell. Delete only the exact recorded temporary parent using the file manager if no longer needed; never delete the guide, home or work repository.

## Common mistakes and safety

Amend includes staged changes, even those unrelated to the intended fix. Inspect before executing. Never force push a shared branch to publish the amended commit. If the wrong private tip was replaced, inspect backup/reflog and preserve a rescue branch before further changes.

## Exercise and self-check

Why can two commits with the same parent have different IDs? Answer: content/message or metadata differs. Pass if original tip is retained on backup and current tip has the intended content and same parent.

## Quick reference

- `git commit --amend -m MESSAGE`
- `git commit --amend --no-edit`
- `git branch backup/draft`

## Official sources

- [Git: git-commit](https://git-scm.com/docs/git-commit)
- [Git: git-reflog](https://git-scm.com/docs/git-reflog)
- [Git: git-revert](https://git-scm.com/docs/git-revert)
