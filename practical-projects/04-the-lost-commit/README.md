# The Lost Commit

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../03-merge-conflict-laboratory/README.md) · [Index](../README.md) · [Next](../05-open-source-contribution/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 45 min

**Prerequisites:** [history-and-recovery/05-reflog](../../history-and-recovery/05-reflog/README.md) · Git 2.40+ · Bash/Git Bash

**Objective:** Create two commits, record the second ID outside the repository, verify a clean checkout, reset one commit back in this disposable lab, locate the displaced commit with reflog and create a recovery branch. Keep main at the first commit.

## Scenario

A private practice branch loses its tip after an intentional reset. Recover the committed content without moving main again.

## Disposable setup

Use only the Disposable setup section of [My First Repository](../01-my-first-repository/README.md). Start a fresh dedicated Bash/Git Bash shell; verify printed sandbox root, fictional identities and no remotes before proceeding. Do not run project 01's challenge. Git 2.40+. Run one command at a time, stop on any unexpected failure and never run these commands in the guide.

## Challenge

Create two commits, record the second ID outside the repository, verify a clean checkout, reset one commit back in this disposable lab, locate the displaced commit with reflog and create a recovery branch. Keep main at the first commit. Try before reading the solution.

## Progressive hints

A reflog is local and expires. Match the candidate to the saved ID and inspect its content before naming it. A branch ref protects reachable history better than a remembered reflog position.

## Reference solution

Prepare the fictional commits and verify the clean state before the destructive demonstration. If the status test fails, stop.

```bash
printf '%s\n' 'status: draft' > notes.txt
git add notes.txt
git commit -m 'docs: initialize notes'
base=$(git rev-parse HEAD)
printf '%s\n' 'status: recovered' > notes.txt
git add notes.txt
git commit -m 'docs: preserve recovery example'
git rev-parse HEAD > "$sandbox/saved-tip.txt"
test -z "$(git status --porcelain)"
git reset --hard "$base"
git reflog show HEAD
```

Identify the previous tip in the displayed reflog. Immediately after these exact steps, HEAD@{1} is the displaced revision; verify it against the saved ID rather than assuming this position works generally.

```bash
candidate=$(git rev-parse 'HEAD@{1}')
test "$candidate" = "$(cat "$sandbox/saved-tip.txt")"
git show "$candidate":notes.txt
git branch recovery/notes "$candidate"
test "$(git rev-parse main)" = "$base"
git show recovery/notes:notes.txt
git status --porcelain
```

## Success checks

Main remains at base and recovery/notes names the exact saved tip with recovered content; working tree is clean. Explain why uncommitted edits would not be guaranteed recoverable.

Fixed maintainer test (not learner code): `tests/test_git_practical_projects.py::test_lost_commit_recovery`.

## Recovery and cleanup

Do not perform reset --hard outside this fresh lab. If the candidate differs, stop and inspect the reflog and saved ID; avoid garbage collection while recovering. Recovery is not guaranteed if objects disappear. Close the dedicated shell and remove only the verified printed sandbox using a file manager. Preserve desired work first.

## Official sources

- <https://git-scm.com/docs/git-reset>
- <https://git-scm.com/docs/git-reflog>
- <https://git-scm.com/docs/git-branch>
- <https://git-scm.com/docs/git-show>

---

<!-- navigation-footer -->
[Previous](../03-merge-conflict-laboratory/README.md) · [Index](../README.md) · [Next](../05-open-source-contribution/README.md)
<!-- /navigation-footer -->
