# Blobs and trees: names and content

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../01-object-database/README.md) · [Index](../README.md) · [Next](../03-commits-and-tags/README.md)
<!-- /navigation -->

**Level:** advanced · **Estimated time:** 45 min

**Prerequisites:** [14 Git Internals](../README.md) · [Advanced Git](../../advanced-git/README.md)

**Objective:** A blob contains content, not a path or filename.

## What and why

A blob contains content, not a path or filename. A tree associates a name and mode with an object ID; subdirectories use trees. The same bytes can share a blob under different names. A Git tree is a snapshot structure, not a list of patch instructions. A professional reviewer can compare trees independently of checkout.

```text
tree T
  docs/  -> tree D -> guide.txt -> blob A
  src/   -> tree S -> state.txt -> blob B
```

The arrows show references or operation relationships, not filesystem paths.

## Practice

Create a fresh isolated fixture from the linked Advanced Git module index before each practice. Run commands individually and stop on unexpected results. Confirm root and printed sandbox. Git 2.34+ practice baseline, Bash (Git Bash on Windows).

Read the tree and a blob by revision:path; compare the state blob IDs across two commits. The IDs differ because bytes changed. Do not manipulate object files directly; use Git commands.

```bash
git ls-tree HEAD
git ls-tree -r HEAD
git cat-file -t HEAD:src/state.txt
git cat-file -p HEAD:src/state.txt
git rev-parse HEAD:src/state.txt
git rev-parse HEAD~1:src/state.txt
git diff HEAD~1 HEAD -- src/state.txt
```

## Common mistakes and safety

Use the disposable fixture only. Never modify object or ref files by hand, force pruning, or run experiments against a real repository. If state differs, inspect with status, log and read-only plumbing; close the dedicated shell and remove only the recorded sandbox through the file manager after reviewing contents.

## Exercise and self-check

A file rename with unchanged content can preserve which ID? The blob ID; the trees that contain the names change.

## Quick reference

- `git ls-tree HEAD`
- `git ls-tree -r HEAD`
- `git cat-file -t HEAD:src/state.txt`
- `git cat-file -p HEAD:src/state.txt`

## Official sources

- [https://git-scm.com/docs/git-ls-tree](https://git-scm.com/docs/git-ls-tree)
- [https://git-scm.com/docs/git-cat-file](https://git-scm.com/docs/git-cat-file)
- [https://git-scm.com/docs/git-diff](https://git-scm.com/docs/git-diff)

---

<!-- navigation-footer -->
[Previous](../01-object-database/README.md) · [Index](../README.md) · [Next](../03-commits-and-tags/README.md)
<!-- /navigation-footer -->
