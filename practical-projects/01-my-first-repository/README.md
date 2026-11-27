# My First Repository

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous module](../../command-reference/README.md) · [Index](../README.md) · [Next module](../../exercises/README.md)
<!-- /navigation -->

**Level:** beginner · **Estimated time:** 30 min

**Prerequisites:** [First repository](../../getting-started/03-first-repository/README.md) · [Three locations](../../git-architecture/01-three-locations/README.md) · [Status, add and commit](../../basic-commands/02-status-add-commit/README.md). Git 2.40+ and Bash (Linux/macOS or Git Bash on Windows).

**Objective:** Create a private local notes repository and demonstrate that a commit records the index, not every working-file edit.

## Scenario

You maintain a fictional notes file with a draft and a ready state. A third experimental edit must not enter the history. No remote, account or programming knowledge is needed.

## Disposable setup

Open a dedicated ordinary Bash shell, not the guide's working directory. Run these commands one at a time. Stop if any fails, especially temporary directory creation or cd. Confirm the printed root is the new sandbox repository, both identities are fictional, and remote output is empty. The isolated configuration is for this shell only, not a hardened security sandbox.

```bash
sandbox=$(mktemp -d)
printf 'Sandbox: %s\n' "$sandbox"
for key in $(compgen -e); do
  case "$key" in GIT_*) unset "$key";; esac
done
mkdir "$sandbox/home" "$sandbox/template"
export HOME="$sandbox/home" USERPROFILE="$sandbox/home"
export XDG_CONFIG_HOME="$sandbox/home"
export GIT_CONFIG_NOSYSTEM=1 GIT_CONFIG_GLOBAL="$sandbox/gitconfig"
export GIT_CONFIG_COUNT=0 GIT_TERMINAL_PROMPT=0
export GIT_TEMPLATE_DIR="$sandbox/template"
git init -b main "$sandbox/repo"
cd "$sandbox/repo"
git config --local user.name 'Study Guide Example'
git config --local user.email 'learner@example.invalid'
git config --local commit.gpgsign false
git config --local core.autocrlf false
git config --local core.hooksPath "$sandbox/no-hooks"
git rev-parse --show-toplevel
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
git remote
```

## Challenge

Create notes.txt containing status: draft and make the first commit. Change it to status: ready and stage it; then change the working file to status: experiment without staging again. Inspect all three locations. Commit only the ready snapshot. Confirm the experiment is still unstaged, then intentionally discard only that fictional edit. End on main with two commits and a clean working tree. Try without looking at the solution.

## Progressive hints

1. Use git status and git add to distinguish an untracked file from a staged change.
2. Compare git show HEAD:notes.txt, git show :notes.txt and the working file. git diff and git diff --cached compare different locations.
3. A plain commit records the index. After confirming the remaining edit is disposable, restore that one working path from the index.

## Reference solution

First, create and record the draft. The initial porcelain output is ?? notes.txt.

```bash
printf '%s\n' 'status: draft' > notes.txt
git status --porcelain=v1
git add notes.txt
git diff --cached
git commit -m 'docs: initialize notes'
```

Next, stage ready and edit the working file again. Expect MM notes.txt before committing: both index and working file differ from their respective comparison points. HEAD contains draft, the index contains ready, and the working file contains experiment. After commit, HEAD contains ready and porcelain shows a leading space followed by M.

```bash
printf '%s\n' 'status: ready' > notes.txt
git add notes.txt
printf '%s\n' 'status: experiment' > notes.txt
git status --porcelain=v1
git show HEAD:notes.txt
git show :notes.txt
git diff
git diff --cached
git commit -m 'docs: mark notes ready'
git show HEAD:notes.txt
git status --porcelain=v1
```

Only after verifying that the experimental line is deliberately disposable, restore the working file from the index. This discards that unstaged edit; do not use this on valuable work.

```bash
git restore --worktree -- notes.txt
git status --porcelain=v1
git log --oneline
git rev-list --count HEAD
git branch --show-current
git remote
```

## Success checks

- Exactly two commits reachable from main; second commit contains status: ready, its parent contains status: draft.
- Working file and index match HEAD; porcelain output is empty.
- Current branch is main; no remotes.
- Explain why a staged ready snapshot was committed while experiment remained unstaged. A clean tree alone would not prove the intended snapshot.

Maintainer test: tests/test_git_practical_projects.py, test_first_repository_staged_snapshot. It asserts intermediate and final states, including the intentionally incorrect dirty final candidate. It runs fixed commands only, not learner submissions.

## Recovery and cleanup

If the state differs, stop and inspect status, diff and staged diff. Preserve any valuable content before restoring; Git does not guarantee recovery of discarded unstaged edits. Close the dedicated shell and remove only the printed sandbox directory via the file manager after verifying its contents. Never remove a real repository.

## Official sources

- <https://git-scm.com/docs/git-init>
- <https://git-scm.com/docs/git-status>
- <https://git-scm.com/docs/git-add>
- <https://git-scm.com/docs/git-commit>
- <https://git-scm.com/docs/git-restore>

---

<!-- navigation-footer -->
[Previous module](../../command-reference/README.md) · [Index](../README.md) · [Next module](../../exercises/README.md)
<!-- /navigation-footer -->
