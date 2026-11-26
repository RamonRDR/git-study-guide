# File states and remote boundaries

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../02-snapshots-head-and-refs/README.md) · [Index](../README.md) · [Next module](../../basic-commands/README.md)
<!-- /navigation -->

**Level:** beginner · **Estimated time:** 25 min

**Prerequisites:** [Snapshots, HEAD and references](../02-snapshots-head-and-refs/README.md)

**Objective:** Interpret tracked, untracked, modified, staged and ignored files.

## What and why

Tracked means a path is represented in the index; untracked paths are not tracked. Modified means contents differ from a comparison baseline; staged means index differs from HEAD. These are not mutually exclusive: MM means two differences. An ignored untracked file matches an ignore rule and is normally omitted from status and add; ignoring does not untrack an already tracked file. A clean status means no reported differences or untracked nonignored files, not that backups exist or that a remote is synchronized.

## Practice

Continue the same lab with third still edited. Create a new draft.txt in the editor containing draft. Inspect (read-only):

```text
git status --short
git ls-files
git remote -v
```

Expected: space-M note.txt and ?? draft.txt; ls-files lists note.txt; remote listing is empty because none was configured. Short status has two positions XY: X compares index to HEAD, Y compares working tree to index (ordinary non-conflict entries). ?? means untracked, !! means ignored when requested. A means added, M modified, D deleted, R rename detected. Conflict codes come later.

## Common mistakes and safety

Do not infer remote state from local status. No fetch, push or credentials are necessary. Do not blindly add every file; inspect first. If you see unexpected paths, stop and confirm the disposable repo root. Keep lab for module 03 or recreate it from module 00.

## Exercise and self-check

Classify note.txt and draft.txt. Answer: note tracked and modified but not staged; draft untracked. Pass if you explain why no remote listing does not prevent commits. Professional use: inspect changes before a review.

## Quick reference

- `git status`
- `git ls-files`
- `git remote`
- `gitignore`

## Official sources

- [Git: git-status](https://git-scm.com/docs/git-status)
- [Git: git-ls-files](https://git-scm.com/docs/git-ls-files)
- [Git: git-remote](https://git-scm.com/docs/git-remote)
- [Git: gitignore](https://git-scm.com/docs/gitignore)

---

<!-- navigation-footer -->
[Previous](../02-snapshots-head-and-refs/README.md) · [Index](../README.md) · [Next module](../../basic-commands/README.md)
<!-- /navigation-footer -->
