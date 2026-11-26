# Restore working files and index

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../01-recovery-safety/README.md) · [Index](../README.md) · [Next](../03-reset/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 25 min

**Prerequisites:** [Isolated lab](../../getting-started/03-first-repository/README.md) · [First commit](../../getting-started/05-first-commit/README.md) · [Merge and conflicts](../../merge-and-conflicts/README.md) · [Remotes](../../remote-repositories/README.md) · [Inspect before undoing](../01-recovery-safety/README.md)

**Objective:** Distinguish unstaging from discarding an edit.

## What and why

With a path, `git restore -- PATH` copies from the index into the working tree by default. `git restore --staged -- PATH` defaults to HEAD as source and changes only the index. `--source=COMMIT` selects another tree; `--staged --worktree` changes both destinations. No new commit or branch movement occurs. A tracked file absent in the source may be removed. Use path-specific restore after inspecting differences; avoid bulk restores when work is valuable.

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

Edit note.txt in a plain-text editor to exactly one line `staged draft` with final newline. Save, then return to the dedicated shell.

```text
git add -- note.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Edit note.txt in a plain-text editor to exactly one line `working draft` with final newline. Save, then return to the dedicated shell.

```text
git status --short
git diff
git diff --cached
git show :note.txt
git show HEAD:note.txt
```

Expect staged draft in index, working draft on disk and practice in HEAD. The next command intentionally discards ONLY the working edit. Stop unless both drafts are disposable and the root is verified.

```text
git restore -- note.txt
git status --short
git diff
git diff --cached
git restore --staged -- note.txt
git status --short
git diff
git diff --cached
```

After first restore, disk = staged draft; after unstaging, index = practice and disk still staged draft. Confirm no useful work before the final destructive step.

```text
git restore -- note.txt
git status --short
git rev-list --count HEAD
git show HEAD:note.txt
```

Expected clean status, one commit, practice content. Professional use: unstage accidentally selected changes without losing the working edit.

After the exercise, close editors and the dedicated shell. Delete only the exact recorded temporary parent using the file manager if no longer needed; never delete the guide, home or work repository.

## Common mistakes and safety

Restore can permanently discard unstaged edits. Reflog does not record working-tree edits. If you restored useful work, stop and check independent backups or editor history; recovery is not guaranteed.

## Exercise and self-check

Which command removes a file from stage but retains the edit? Answer: restore --staged -- note.txt. Pass if staged diff is empty but ordinary diff still shows the edit.

## Quick reference

- `git restore -- PATH`
- `git restore --staged -- PATH`
- `git restore --source=COMMIT -- PATH`

## Official sources

- [Git: git-restore](https://git-scm.com/docs/git-restore)
- [Git: git-diff](https://git-scm.com/docs/git-diff)
