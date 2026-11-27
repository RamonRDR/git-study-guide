# Merge Conflict Laboratory

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../02-two-developers-one-project/README.md) · [Index](../README.md) · [Next](../04-the-lost-commit/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 45 min

**Prerequisites:** [merge-and-conflicts/04-conflict-resolution](../../merge-and-conflicts/04-conflict-resolution/README.md) · Git 2.40+ · Bash/Git Bash

**Objective:** Create divergent branches, reproduce a conflict, inspect unmerged stages, resolve to status: reviewed, and finish a two-parent merge commit.

## Scenario

Two branches revise the same fictional status line differently. Integration must retain an intentional combined resolution.

## Disposable setup

Use only the Disposable setup section of [My First Repository](../01-my-first-repository/README.md). Start a fresh dedicated Bash/Git Bash shell; verify printed sandbox root, fictional identities and no remotes before proceeding. Do not run project 01's challenge. Git 2.40+. Run one command at a time, stop on any unexpected failure and never run these commands in the guide.

## Challenge

Create divergent branches, reproduce a conflict, inspect unmerged stages, resolve to status: reviewed, and finish a two-parent merge commit. Try before reading the solution.

## Progressive hints

Both sides must edit the same original line. An expected nonzero merge result is not a successful integration. Stage the chosen resolution before committing.

## Reference solution

Create the common base and divergent tips.

```bash
printf '%s\n' 'status: draft' > notes.txt
git add notes.txt
git commit -m 'docs: initialize notes'
git switch -c feat/review
printf '%s\n' 'status: ready' > notes.txt
git add notes.txt
git commit -m 'docs: propose ready'
git switch main
printf '%s\n' 'status: checked' > notes.txt
git add notes.txt
git commit -m 'docs: record check'
before=$(git rev-parse HEAD)
feature=$(git rev-parse feat/review)
git merge feat/review
```

The last command is expected to fail with a conflict. Continue only if MERGE_HEAD exists and notes.txt has unmerged stages. Inspect, then replace the whole fictional file and commit.

```bash
git rev-parse --verify MERGE_HEAD
git status --short
git ls-files -u -- notes.txt
git show :1:notes.txt
git show :2:notes.txt
git show :3:notes.txt
printf '%s\n' 'status: reviewed' > notes.txt
git add notes.txt
git diff --cached --check
git commit -m 'merge: reconcile review status'
test "$(git rev-parse HEAD^1)" = "$before"
test "$(git rev-parse HEAD^2)" = "$feature"
git status --porcelain
git show HEAD:notes.txt
```

## Success checks

Unmerged stages 1/2/3 existed before resolution; final merge has the two expected parents in order, reviewed content and a clean index and tree. A conflict marker alone is not the correct result.

Fixed maintainer test (not learner code): `tests/test_git_practical_projects.py::test_conflict_resolution`.

## Recovery and cleanup

During the active ordinary merge, preserve desired resolution edits before git merge --abort. After completion inspect parents; do not reset shared history. Recreate the disposable lab if needed. Close the dedicated shell and remove only the verified printed sandbox using a file manager. Preserve desired work first.

## Official sources

- <https://git-scm.com/docs/git-merge>
- <https://git-scm.com/docs/git-status>
- <https://git-scm.com/docs/git-ls-files>

---

<!-- navigation-footer -->
[Previous](../02-two-developers-one-project/README.md) · [Index](../README.md) · [Next](../04-the-lost-commit/README.md)
<!-- /navigation-footer -->
