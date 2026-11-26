# Integration safety and recovery first

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous module](../../branches/README.md) · [Index](../README.md) · [Next](../02-fast-forward/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 25 min

**Prerequisites:** [Branch management](../../branches/README.md) · [Isolated lab setup](../../getting-started/03-first-repository/README.md) · [First commit](../../getting-started/05-first-commit/README.md)

**Objective:** Identify the operation, prerequisites and safe exit before combining histories.

## What and why

Integration combines changes from separate lines of history. Merge may advance a branch or create a commit with multiple parents. Squash stages combined content without recording source ancestry. Rebase reapplies commits onto another base and normally produces new commit IDs. A conflict occurs when Git cannot safely decide the combined result. Clean starting state, known refs, fictional identity and local backup references make experiments easier to inspect. None of these operations sends changes to a server.

## Practice

Create a NEW isolated disposable lab using module 00 chapter 03 and its first-commit lesson. Keep the original dedicated shell, not the editor terminal. The initial main must contain exactly one commit, note.txt = practice, with clean status. Close any previous lab shell before starting. Follow the safety checks from chapter 01 before every history-changing operation.

```text
git rev-parse --show-toplevel
git branch --show-current
git status --short
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Stop unless root is your disposable lab, current branch is the one specified, status is clean before starting an operation, and both identities start with `Study Guide Example <learner@example.invalid>`. Before each commit also inspect the staged diff; stop on unexpected output.

```text
git log --oneline --all --graph --decorate
git branch --list
git remote -v
```

Before a rebase, create a separate branch pointing to the original tip (e.g. backup/feature). It preserves a named reference to committed work, not uncommitted files or an external backup. When an ordinary merge stops with conflicts, inspect status; `git merge --abort` attempts to restore the pre-merge state. When a rebase stops, `git rebase --abort` returns to the original branch/state; `git rebase --continue` resumes after resolution. Use the abort for the operation actually in progress. Start clean; abort cannot guarantee reconstruction of pre-existing uncommitted changes. `git merge --squash` does not create MERGE_HEAD, so ordinary merge abort is not a general squash undo. If a squash lab fails, stop and discard only that lab after checking its location. Recovery of completed operations is taught later.

## Common mistakes and safety

Never rebase shared/published history in these exercises; never force push, reset hard or run commands against this guide. Abort is not a time machine for completed operations. On unexpected state, stop and inspect rather than stacking commands.

After each independent lab, close the editor and dedicated shell, then delete only the exact temporary parent folder you recorded in module 00 using the file manager if you no longer need it. Never delete the guide, home or work repository.

## Exercise and self-check

Choose the safe next step for a conflicting merge: inspect status, then merge --abort or resolve and continue. For rebase use rebase --abort/--continue. Pass if you explain why a clean start and a backup ref matter. Professional use: agree on integration policy before touching shared history.

## Quick reference

- `git status`
- `git merge --abort`
- `git rebase --abort`
- `git rebase --continue`

## Official sources

- [Git: git-merge](https://git-scm.com/docs/git-merge)
- [Git: git-rebase](https://git-scm.com/docs/git-rebase)
- [Git: git-status](https://git-scm.com/docs/git-status)
- [Git: git-branch](https://git-scm.com/docs/git-branch)

---

<!-- navigation-footer -->
[Previous module](../../branches/README.md) · [Index](../README.md) · [Next](../02-fast-forward/README.md)
<!-- /navigation-footer -->
