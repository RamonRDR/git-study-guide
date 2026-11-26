# Stash temporary work

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../05-reflog/README.md) · [Index](../README.md) · [Next](../07-cherry-pick/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 35 min

**Prerequisites:** [Isolated lab](../../getting-started/03-first-repository/README.md) · [First commit](../../getting-started/05-first-commit/README.md) · [Merge and conflicts](../../merge-and-conflicts/README.md) · [Remotes](../../remote-repositories/README.md) · [Reflog and lost commit recovery](../05-reflog/README.md)

**Objective:** Temporarily shelve staged, unstaged and untracked work and restore it deliberately.

## What and why

Stash saves selected local work as Git objects referenced by refs/stash and usually returns the affected working tree/index to HEAD. Default push saves tracked staged and unstaged changes, not untracked or ignored files. `-u` includes untracked files; `-a` also includes ignored files and may capture secrets, so avoid it without inspection. `apply` retains the stash, `pop` removes it on successful application; `--index` attempts to reinstate staged state. `drop` removes an entry. Stash is local, not a durable external backup, and applying onto changed history can conflict.

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

Edit note.txt in a plain-text editor to exactly one line `staged note` with final newline. Save, then return to the dedicated shell.

```text
git add -- note.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Edit note.txt in a plain-text editor to exactly one line `working note` with final newline. Save, then return to the dedicated shell.

Create untracked draft.txt containing only `temporary` with final newline. Verify only these fictional changes and an empty stash list; record HEAD.

```text
git status --short
git stash list
git rev-parse HEAD
git stash push -u -m "lab: temporary notes"
git status --short
git stash list
git stash show --stat --include-untracked 'stash@{0}'
git rev-parse HEAD
```

Expected clean status, one stash, unchanged HEAD. Confirm exact entry and clean state before applying.

```text
git stash apply --index 'stash@{0}'
git status --short
git diff
git diff --cached
git show :note.txt
git stash list
```

Expected staged note in index, working note on disk, draft.txt untracked, stash still listed. Read draft.txt in editor and verify temporary. Only after confirming all expected data and that the one stash is expendable, drop it; do not drop valuable work.

```text
git stash drop 'stash@{0}'
git stash list
git status --short
git rev-parse HEAD
```

Expected empty stash list, restored edits unchanged, HEAD original. Professional use: briefly switch tasks without committing unfinished changes; use an appropriate private branch and backup for longer-lived work.

After the exercise, close editors and the dedicated shell. Delete only the exact recorded temporary parent using the file manager if no longer needed; never delete the guide, home or work repository.

## Common mistakes and safety

If apply/pop conflicts, inspect status; the stash is normally retained after conflicting pop. There is no general stash --abort. Resolve carefully or seek help; do not reset hard in a real project to clear the conflict. Dropped entries may become unreachable; recovery is not guaranteed.

## Exercise and self-check

Why prefer apply before drop for uncertain recovery? Answer: inspect while retaining saved state. Pass if both staged and unstaged versions and untracked file return and HEAD stays unchanged.

## Quick reference

- `git stash push -u -m MESSAGE`
- `git stash list`
- `git stash apply --index 'stash@{0}'`
- `git stash pop`
- `git stash drop 'stash@{0}'`

## Official sources

- [Git: git-stash](https://git-scm.com/docs/git-stash)
- [Git: git-status](https://git-scm.com/docs/git-status)

---

<!-- navigation-footer -->
[Previous](../05-reflog/README.md) · [Index](../README.md) · [Next](../07-cherry-pick/README.md)
<!-- /navigation-footer -->
