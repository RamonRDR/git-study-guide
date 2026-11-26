# Reset and its three modes

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../02-restore/README.md) · [Index](../README.md) · [Next](../04-revert/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 40 min

**Prerequisites:** [Isolated lab](../../getting-started/03-first-repository/README.md) · [First commit](../../getting-started/05-first-commit/README.md) · [Merge and conflicts](../../merge-and-conflicts/README.md) · [Remotes](../../remote-repositories/README.md) · [Restore working files and index](../02-restore/README.md)

**Objective:** Predict branch, index and working-tree state for each reset mode.

## What and why

Commit-mode reset moves the current branch to a target commit. With --soft the index and working tree are unchanged; --mixed (default) resets index but leaves working files; --hard resets both and may overwrite or delete obstructing untracked paths. Path-mode reset (e.g. `git reset HEAD -- PATH`) changes the index, not the branch. Diagram from clean C2: soft -> main C1, index C2, disk C2; mixed -> main C1, index C1, disk C2; hard -> main C1, index C1, disk C1. Use only on unpublished history when rewriting is intended; use revert for shared history.

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

Edit note.txt in a plain-text editor to exactly one line `second` with final newline. Save, then return to the dedicated shell.

```text
git add -- note.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Only if the staged diff and both identities are correct, continue:

```text
git commit -m "docs: add second version"
git branch backup/second
git rev-parse HEAD HEAD^ backup/second
git status --short
```

Record the two IDs as C2 and C1. Confirm clean main at C2, backup/second at C2, no remotes. Run soft reset first:

```text
git reset --soft HEAD^
git rev-parse HEAD
git show :note.txt
git diff --cached
git diff
```

Expected main C1; index/disk second; staged diff only. Now reset index to current HEAD, without moving main:

```text
git reset --mixed HEAD
git rev-parse HEAD
git show :note.txt
git diff
git diff --cached
```

Expected main C1, index practice, disk second; only unstaged diff. Before hard reset, confirm root, main, no remotes, backup/second still C2, and the only change is the disposable note.txt edit. Do not proceed if any other work exists. The following intentionally discards the edit.

```text
git reset --hard HEAD
git status --short
git show HEAD:note.txt
git show backup/second:note.txt
git merge --ff-only backup/second
git rev-parse HEAD backup/second
git status --short
```

Expected clean practice after hard; backup retains second. Fast-forward restores C2 without inventing a commit. Professional use: soft reset can regroup private commits, but check policy and backup first.

After the exercise, close editors and the dedicated shell. Delete only the exact recorded temporary parent using the file manager if no longer needed; never delete the guide, home or work repository.

## Common mistakes and safety

Hard reset is not a general undo or a way to fix a rejected push. A branch backup saves committed data only. ORIG_HEAD may record the earlier tip but can be overwritten; use verified backup refs and reflog if available. Never rely on guaranteed recovery.

## Exercise and self-check

After mixed reset of a clean C2 to C1, where is the C2 edit? Answer: working tree, not index. Pass if you can predict all three state locations and demonstrate the backup tip remains.

## Quick reference

- `git reset --soft COMMIT`
- `git reset --mixed COMMIT`
- `git reset --hard COMMIT`
- `git reset HEAD -- PATH`

## Official sources

- [Git: git-reset](https://git-scm.com/docs/git-reset)
- [Git: git-merge](https://git-scm.com/docs/git-merge)
- [Git: git-reflog](https://git-scm.com/docs/git-reflog)
