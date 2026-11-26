# Revert without rewriting history

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../03-reset/README.md) · [Index](../README.md) · [Next](../05-reflog/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 30 min

**Prerequisites:** [Isolated lab](../../getting-started/03-first-repository/README.md) · [First commit](../../getting-started/05-first-commit/README.md) · [Merge and conflicts](../../merge-and-conflicts/README.md) · [Remotes](../../remote-repositories/README.md) · [Reset and its three modes](../03-reset/README.md)

**Objective:** Undo a committed change by adding history rather than rewriting it.

## What and why

Revert calculates the inverse of a selected commit relative to its parent and applies it to the current state, normally creating a new commit. It is useful for correcting shared history through the team review process. It can conflict if later edits overlap. `--no-edit` uses the generated message; `--no-commit` stages the result without immediately committing. A merge commit needs a deliberately selected mainline parent (`-m`); reversing a merge has effects on future merges, so this lesson does not execute that variant.

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

Edit note.txt in a plain-text editor to exactly one line `wrong` with final newline. Save, then return to the dedicated shell.

```text
git add -- note.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Only if the staged diff and both identities are correct, continue:

```text
git commit -m "docs: add wrong note"
git log --oneline
git show HEAD
git status --short
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Confirm clean main, fictional identities and that HEAD is the single wrong change to reverse. Run:

```text
git revert --no-edit HEAD
git log --oneline
git rev-list --count HEAD
git show HEAD:note.txt
git diff HEAD~2 HEAD
git status --short
```

Expected C1 -> C2 -> R3, three commits; C2 remains an ancestor, R3 snapshot equals C1, clean status. The inverse commit is not removal of the original commit. In a real project review/test the inverse patch before publishing.

After the exercise, close editors and the dedicated shell. Delete only the exact recorded temporary parent using the file manager if no longer needed; never delete the guide, home or work repository.

## Common mistakes and safety

If conflict occurs, inspect status and staged changes; resolve and use revert --continue, or revert --abort while the operation is in progress. Revert does not remove exposed secrets from history; revoke credentials separately. Avoid reverting unrelated commits without checking dependencies.

## Exercise and self-check

Does reverting C2 delete its ID? Answer: no. Pass if history has three commits and HEAD content equals the original.

## Quick reference

- `git revert --no-edit COMMIT`
- `git revert --no-commit COMMIT`
- `git revert --abort`
- `git revert --continue`

## Official sources

- [Git: git-revert](https://git-scm.com/docs/git-revert)
- [Git: git-log](https://git-scm.com/docs/git-log)
