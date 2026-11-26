# Cherry-pick selected commits

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../06-stash/README.md) · [Index](../README.md) · [Next](../08-amend/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 40 min

**Prerequisites:** [Isolated lab](../../getting-started/03-first-repository/README.md) · [First commit](../../getting-started/05-first-commit/README.md) · [Merge and conflicts](../../merge-and-conflicts/README.md) · [Remotes](../../remote-repositories/README.md) · [Stash temporary work](../06-stash/README.md)

**Objective:** Transfer a selected commit between divergent branches without merging all history.

## What and why

Cherry-pick applies the change introduced by a commit to the current branch and ordinarily creates a new commit with a different parent/ID. It does not merge the entire source branch. Use for an independent fix/backport after checking dependencies; avoid using it as a substitute for ordinary branch integration. `-x` records the source ID in the message when applicable, useful for public backports; `--no-commit` applies changes without creating the commit yet. A merge commit needs mainline selection; not practiced here. Diagram: C1 -> F2 on fix; C1 -> M2 on main; after pick main M2 -> P3, fix remains F2.

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

```text
git switch -c fix/note
```

Edit note.txt in a plain-text editor to exactly one line `fixed` with final newline. Save, then return to the dedicated shell.

```text
git add -- note.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Only if the staged diff and both identities are correct, continue:

```text
git commit -m "docs: fix note"
git switch main
```

Create overview.txt with one line `overview` and final newline in main. Inspect root, branch, status and identities.

```text
git add -- overview.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Only if the staged diff and both identities are correct, continue:

```text
git commit -m "docs: add overview"
git log --all --oneline --graph
git show fix/note
git status --short
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Confirm clean main, independent fix and fictional identities. The source tip is the one fix commit. Run:

```text
git cherry-pick -x fix/note
git log --all --oneline --graph
git rev-parse HEAD fix/note
git show HEAD:note.txt
git show HEAD:overview.txt
git status --short
```

Expected different IDs, fixed and overview retained, clean status. The selected source commit remains on fix/note; main has a new commit with parent M2. In real backports inspect prerequisites and run tests before publishing.

After the exercise, close editors and the dedicated shell. Delete only the exact recorded temporary parent using the file manager if no longer needed; never delete the guide, home or work repository.

## Common mistakes and safety

Overlapping edits may conflict. Inspect status and conflict markers, then stage resolved paths and use cherry-pick --continue, or cherry-pick --abort to attempt restoration to the pre-sequence state. Do not apply twice blindly; a patch may already be present. Do not rewrite shared history to remove duplicates.

## Exercise and self-check

Is the source commit an ancestor of the new main tip just because its change was picked? Answer: not necessarily; this lab has distinct ancestry. Pass if both files survive, IDs differ and source ref is unchanged.

## Quick reference

- `git cherry-pick COMMIT`
- `git cherry-pick -x COMMIT`
- `git cherry-pick --continue`
- `git cherry-pick --abort`

## Official sources

- [Git: git-cherry-pick](https://git-scm.com/docs/git-cherry-pick)
- [Git: git-merge-base](https://git-scm.com/docs/git-merge-base)
