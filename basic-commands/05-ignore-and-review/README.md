# Ignore rules and final review

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../04-move-and-remove/README.md) · [Index](../README.md) · [Next module](../../branches/README.md)
<!-- /navigation -->

**Level:** beginner · **Estimated time:** 30 min

**Prerequisites:** [Rename and remove tracked files](../04-move-and-remove/README.md)

**Objective:** Use .gitignore and understand why ignored tracked files remain tracked.

## What and why

A .gitignore file holds patterns for intentionally untracked paths, such as generated output. A leading slash anchors a pattern relative to that ignore file; trailing slash matches directories; * matches within path components; ! can negate earlier rules (but cannot reinclude a file if its parent is excluded). Git also supports repository-local .git/info/exclude and global core.excludesFile; this lab uses only a shared .gitignore. Ignore is not encryption, access control or history removal. Already tracked paths are unaffected by ignore rules until removed from index.

## Practice

Continue the lab: draft.txt is untracked. Create a plain-text .gitignore at repo root with these lines, and a dummy report.tmp containing sample (never real secrets):

```text
/draft.txt
*.tmp
!keep.tmp
/build/
```

Create keep.tmp with keep. Inspect:

```text
git status --short --ignored
git check-ignore -v -- draft.txt report.tmp
git add -- .gitignore keep.tmp
git diff --cached --name-status
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Expected: draft.txt/report.tmp ignored (!!), keep.tmp untracked before add, then staged with .gitignore. If diff and fictional identities match, commit. 

```text
git commit -m "docs: add ignore rules"
```

Only now append /keep.tmp to .gitignore and edit keep.tmp to updated; save both. Then:

```text
git status --short
git ls-files -- keep.tmp
git check-ignore --no-index -v -- keep.tmp
```

Run the last three commands AFTER the editor changes. Expected: both tracked files modified, keep.tmp still tracked, --no-index shows matching ignore rule even for tracked path. Do not stage keep.tmp. Optionally stop tracking it as a deliberate local exercise, inspect staged deletion and stage only the ignore change:

```text
git rm --cached -- keep.tmp
git add -- .gitignore
git diff --cached --name-status
git status --short --ignored
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Expected: staged deletion of keep.tmp, modification of .gitignore, keep.tmp remains on disk and ignored. Commit only if expected and fictional identities verified:

```text
git commit -m "docs: stop tracking generated file"
git status --short --ignored
git ls-files
```

## Common mistakes and safety

If a secret was committed, ignore or rm --cached is not sufficient; revoke/rotate the credential and follow the incident process (module 12). Never force add sensitive content. Review status, cached diff, identity and commit history. To finish, close editor and dedicated shell, then use the file manager to delete ONLY the exact temporary parent folder recorded in module 00, if no longer needed.

## Exercise and self-check

Why does keep.tmp still appear modified after adding an ignore rule? Answer: it was already tracked. Pass if you can distinguish ignoring, untracking and deleting, and explain why an ignored secret in old history is still a problem. Professional use: review ignore rules with generated files before initial commit.

## Quick reference

- `gitignore`
- `git check-ignore`
- `git rm`
- `git status`

## Official sources

- [Git: gitignore](https://git-scm.com/docs/gitignore)
- [Git: git-check-ignore](https://git-scm.com/docs/git-check-ignore)
- [Git: git-rm](https://git-scm.com/docs/git-rm)
- [Git: git-status](https://git-scm.com/docs/git-status)

---

<!-- navigation-footer -->
[Previous](../04-move-and-remove/README.md) · [Index](../README.md) · [Next module](../../branches/README.md)
<!-- /navigation-footer -->
