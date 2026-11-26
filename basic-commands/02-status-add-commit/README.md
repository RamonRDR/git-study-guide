# Inspect, stage and commit

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../01-init-config-help/README.md) · [Index](../README.md) · [Next](../03-diff-log-show/README.md)
<!-- /navigation -->

**Level:** beginner · **Estimated time:** 30 min

**Prerequisites:** [Initialize, configure and ask for help](../01-init-config-help/README.md)

**Objective:** Record a focused change and verify that another file stays untracked.

## What and why

git status inspects staged/unstaged/untracked state; --short shows compact codes. git add PATH stages the current content of the named file. git add -p interactively selects hunks (groups of changed lines) in tracked files; git add . may stage many paths and git add -A covers additions, modifications and deletions across the working tree when no path is given. Prefer explicit paths while learning. git commit -m records index with a message; git commit -a also stages modifications/deletions of tracked files, not new untracked files, so it can include unintended edits. Avoid it until you understand selection.

## Practice

Use the new isolated repository from chapter 01. In a text editor create note.txt containing practice and draft.txt containing draft, each with a final newline. Inspect and stage only note.txt:

```text
git rev-parse --show-toplevel
git status --short
git add -- note.txt
git status --short
git diff --cached -- note.txt
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Expected: A then space for note.txt, ?? draft.txt. If root, staged diff or either identity is wrong, stop. Otherwise:

```text
git commit -m "docs: add note"
git status --short
git show HEAD:note.txt
git ls-files
```

Expected: only draft.txt is untracked; note.txt is tracked and stored as practice. -- ends option parsing so a path is not mistaken for an option. No remote operation occurred.

## Common mistakes and safety

If unwanted changes are staged, do not commit; for this beginner exercise recreate the lab. Never force-add secrets or commit private drafts. Verify both identities before every commit; use the isolated shell, not editor commit controls.

## Exercise and self-check

Predict whether draft.txt is committed. Answer: no, it was not staged. Pass if ls-files lists only note.txt. Professional use: choose files for one reviewable change.

## Quick reference

- `git status`
- `git add`
- `git commit`

## Official sources

- [Git: git-status](https://git-scm.com/docs/git-status)
- [Git: git-add](https://git-scm.com/docs/git-add)
- [Git: git-commit](https://git-scm.com/docs/git-commit)

---

<!-- navigation-footer -->
[Previous](../01-init-config-help/README.md) · [Index](../README.md) · [Next](../03-diff-log-show/README.md)
<!-- /navigation-footer -->
