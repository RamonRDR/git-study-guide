# Working tree, index and repository

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous module](../../fundamentals/README.md) · [Index](../README.md) · [Next](../02-snapshots-head-and-refs/README.md)
<!-- /navigation -->

**Level:** beginner · **Estimated time:** 30 min

**Prerequisites:** [Getting Started](../../getting-started/README.md) · [Fundamentals](../../fundamentals/README.md)

**Objective:** Distinguish the three locations and predict which content a commit records.

## What and why

The working tree is the checked-out files you edit. The index (staging area) stores the contents selected for the next snapshot, including unchanged tracked entries. The local repository contains Git metadata, objects and references, usually under .git. `git add` updates the index from working files; `git commit` records the index as a snapshot and normally advances the current branch. Neither command sends anything to a remote (another repository location). The index is not a list of filenames alone: it represents selected file versions.

## Practice

Accessible state diagram (arrows show the direction of selected content, not a file move):

```text
Working tree -- git add --> Index -- git commit --> Local repository
       |                       |                       |
   editable file           selected version         recorded history
```

Use the isolated terminal from module 00. In a fresh lab with the first note.txt commit completed, edit note.txt to the single line second, save with a final newline, then run:

```text
git add note.txt
```

Now edit note.txt to third and save with a final newline without staging. Inspect:

```text
git status --short
git diff --cached
git diff
git show HEAD:note.txt
git show :note.txt
```

Expected: MM note.txt; HEAD has practice, index second, working file third. The first M is index versus HEAD; the second M is working tree versus index. The cached diff shows practice -> second; plain diff shows second -> third. The colon path requests the staged version.

## Common mistakes and safety

Inspect root and effective identities before any commit. Never edit .git files by hand. Do not assume saving stages files. If your result differs, inspect the two diffs; do not reset or force anything.

## Exercise and self-check

Which version would a commit record now? Hint: follow the second arrow. Answer: second; third remains edited. Pass if you can explain both M columns. Professional use: isolate a reviewed change from unrelated edits.

## Quick reference

- `git add`
- `git commit`
- `git status`
- `git diff`
- `git show`

## Official sources

- [Git: git-add](https://git-scm.com/docs/git-add)
- [Git: git-commit](https://git-scm.com/docs/git-commit)
- [Git: git-status](https://git-scm.com/docs/git-status)
- [Git: git-diff](https://git-scm.com/docs/git-diff)
- [Git: git-show](https://git-scm.com/docs/git-show)

---

<!-- navigation-footer -->
[Previous module](../../fundamentals/README.md) · [Index](../README.md) · [Next](../02-snapshots-head-and-refs/README.md)
<!-- /navigation-footer -->
