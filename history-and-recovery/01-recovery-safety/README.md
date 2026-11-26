# Inspect before undoing

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous module](../../remote-repositories/README.md) · [Index](../README.md) · [Next](../02-restore/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 20 min

**Prerequisites:** [Isolated lab](../../getting-started/03-first-repository/README.md) · [First commit](../../getting-started/05-first-commit/README.md) · [Merge and conflicts](../../merge-and-conflicts/README.md) · [Remotes](../../remote-repositories/README.md)

**Objective:** Choose the least destructive operation using the affected Git state.

## What and why

Undo is not one operation. Restore changes a selected file in the working tree or index, not the branch tip. Reset in commit mode moves the current branch; soft preserves index and files, mixed resets index, hard also replaces tracked working files. Revert creates a new inverse commit. Amend replaces the tip; cherry-pick reapplies a selected change as a new commit in the normal case. Stash stores local work temporarily. Reflog records local ref movements and can locate retained commits. Diagram: working tree -> index -> commit; a branch points to a commit, and HEAD normally points to the branch. Changing one location does not necessarily change the others. Published history should normally be corrected with a new commit, not rewritten.

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

Edit note.txt in a plain-text editor to exactly one line `draft` with final newline. Save, then return to the dedicated shell.

```text
git status --short
git diff
git diff --cached
git show HEAD:note.txt
git reflog -n 3
```

Expected: an unstaged change, empty staged diff, committed practice unchanged. Do not undo yet. Identify whether work is untracked, unstaged, staged, committed or shared. In a real incident, stop writes, preserve evidence and make an independent backup of any valuable working files before choosing a command. A backup branch preserves committed snapshots only; it is not a backup of working files or index. In this lab the draft is intentionally disposable.

After the exercise, close editors and the dedicated shell. Delete only the exact recorded temporary parent using the file manager if no longer needed; never delete the guide, home or work repository.

## Common mistakes and safety

Never assume Git can recover an untracked or unsaved file. Reflogs are local and can expire; garbage collection may remove unreachable objects. Do not run cleanup or garbage collection to troubleshoot loss. Seek help before modifying shared history.

## Exercise and self-check

A published commit is wrong; which operation normally preserves collaboration? Hint: add an inverse change. Answer: revert. Pass if you explain why a backup branch cannot save an unstaged file.

## Quick reference

- `git status --short`
- `git diff`
- `git diff --cached`
- `git log --all --graph --oneline`

## Official sources

- [Git: git-status](https://git-scm.com/docs/git-status)
- [Git: git-diff](https://git-scm.com/docs/git-diff)
- [Git: git-reflog](https://git-scm.com/docs/git-reflog)
- [Git: git-reset](https://git-scm.com/docs/git-reset)
- [Git: git-revert](https://git-scm.com/docs/git-revert)

---

<!-- navigation-footer -->
[Previous module](../../remote-repositories/README.md) · [Index](../README.md) · [Next](../02-restore/README.md)
<!-- /navigation-footer -->
