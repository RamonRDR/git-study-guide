# Object database: the repository's content store

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous module](../../advanced-git/README.md) · [Index](../README.md) · [Next](../02-blobs-and-trees/README.md)
<!-- /navigation -->

**Level:** advanced · **Estimated time:** 40 min

**Prerequisites:** [14 Git Internals](../README.md) · [Advanced Git](../../advanced-git/README.md)

**Objective:** Git stores typed objects identified by content: blob (file content), tree (directory entries), commit (snapshot and ancestry), annotated tag (named object metadata).

## What and why

Git stores typed objects identified by content: blob (file content), tree (directory entries), commit (snapshot and ancestry), annotated tag (named object metadata). Refs name objects; the working tree and index are not the object database. Use this distinction when diagnosing missing data or explaining why a checkout is not a backup.

```text
refs/heads/main -> commit C -> tree T -> tree S -> blob B
                     |
                     +-> parent P -> tree U
```

A commit → root tree → directory tree → blob.

## Practice

Create a fresh isolated fixture from the linked Advanced Git module index before each practice. Run commands individually and stop on unexpected results. Confirm root and printed sandbox. Git 2.34+ practice baseline, Bash (Git Bash on Windows).

Inspect the object type and size of HEAD and list reachable objects. `git count-objects -v` reports storage statistics, not a count of commits. Observe that the commit points to a tree, not directly to every working file.

```bash
git cat-file -t HEAD
git cat-file -s HEAD
git cat-file -p HEAD
git rev-list --objects --all
git count-objects -v
```

## Common mistakes and safety

Use the disposable fixture only. Never modify object or ref files by hand, force pruning, or run experiments against a real repository. If state differs, inspect with status, log and read-only plumbing; close the dedicated shell and remove only the recorded sandbox through the file manager after reviewing contents.

## Exercise and self-check

A commit → root tree → directory tree → blob. A parent edge joins commits; refs point to object IDs. Which type stores file bytes? Blob.

## Quick reference

- `git cat-file -t HEAD`
- `git cat-file -s HEAD`
- `git cat-file -p HEAD`
- `git rev-list --objects --all`

## Official sources

- [https://git-scm.com/docs/git-cat-file](https://git-scm.com/docs/git-cat-file)
- [https://git-scm.com/docs/git-count-objects](https://git-scm.com/docs/git-count-objects)
- [https://git-scm.com/docs/gitrepository-layout](https://git-scm.com/docs/gitrepository-layout)

---

<!-- navigation-footer -->
[Previous module](../../advanced-git/README.md) · [Index](../README.md) · [Next](../02-blobs-and-trees/README.md)
<!-- /navigation-footer -->
