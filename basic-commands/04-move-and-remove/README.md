# Rename and remove tracked files

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../03-diff-log-show/README.md) · [Index](../README.md) · [Next](../05-ignore-and-review/README.md)
<!-- /navigation -->

**Level:** beginner · **Estimated time:** 30 min

**Prerequisites:** [Compare and inspect history](../03-diff-log-show/README.md)

**Objective:** Distinguish working file deletion, staged deletion and removing only from the index.

## What and why

git mv OLD NEW moves a tracked path and stages the old deletion/new addition; rename detection is based on similarity, not permanent rename metadata. git rm PATH removes a tracked path from the working tree and index (stages deletion). git rm --cached PATH removes only from index, leaving working file; if tracked in HEAD it stages deletion. Git may refuse if changes risk being lost; never use -f here. Ordinary file-manager moves/deletions change the working tree; Git records their staged effects only after add/rm.

## Practice

Continue disposable lab from chapter 03: note.txt committed with third; draft.txt untracked. Confirm root and status, ensure no destination notes.txt exists. Rename only note.txt:

```text
git rev-parse --show-toplevel
git status --short
git mv -- note.txt notes.txt
git diff --cached --name-status
git status --short
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Expect staged rename (or equivalent deletion/addition). If correct and identities fictional, commit rename, then remove only the index entry:

```text
git commit -m "docs: rename note"
git rm --cached -- notes.txt
git status --short
git diff --cached --name-status
```

Expected: staged D for notes.txt and untracked notes.txt still exists on disk. Do not commit this removal; add it back to cancel the staged deletion without changing working content. Then remove the tracked file (only disposable content):

```text
git add -- notes.txt
git diff --cached --name-status
git rm -- notes.txt
git diff --cached --name-status
git status --short
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Expected: first diff empty, second D notes.txt and file absent; draft remains. If expected and identities fictional, commit:

```text
git commit -m "docs: remove note"
git status --short
```

## Common mistakes and safety

Never run rm in a work repository without understanding deletion and backup. No -f, recursive removal or wildcards. Previous committed contents remain in earlier commits, but uncommitted edits may not be recoverable. If command refuses, inspect status; stop instead of forcing. Recovery commands are taught later.

## Exercise and self-check

Compare rm and rm --cached. Answer: both remove index entry; only ordinary rm removes working file. Pass if you verify each case and explain why prior history remains. Professional use: stop tracking generated data without deleting the local copy (pair with ignore rule).

## Quick reference

- `git mv`
- `git rm`
- `git add`
- `git diff`

## Official sources

- [Git: git-mv](https://git-scm.com/docs/git-mv)
- [Git: git-rm](https://git-scm.com/docs/git-rm)
- [Git: git-add](https://git-scm.com/docs/git-add)
- [Git: git-diff](https://git-scm.com/docs/git-diff)
