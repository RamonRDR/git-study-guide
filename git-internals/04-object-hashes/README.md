# Hashes and object identity

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../03-commits-and-tags/README.md) · [Index](../README.md) · [Next](../05-refs-and-head/README.md)
<!-- /navigation -->

**Level:** advanced · **Estimated time:** 40 min

**Prerequisites:** [14 Git Internals](../README.md) · [Advanced Git](../../advanced-git/README.md)

**Objective:** Object IDs derive from the object type, byte length and content, with Git's object header.

## What and why

Object IDs derive from the object type, byte length and content, with Git's object header. SHA-1 and SHA-256 are repository formats; do not assume 40 characters for every repository. Hashing file bytes with a generic checksum is not the same as a Git blob ID. A hash is not a signature or access control.

## Practice

Create a fresh isolated fixture from the linked Advanced Git module index before each practice. Run commands individually and stop on unexpected results. Confirm root and printed sandbox. Git 2.34+ practice baseline, Bash (Git Bash on Windows).

Compute a raw blob ID without writing objects (`--no-filters` avoids attribute conversions). Compare the same bytes twice and then the changed bytes. Git reports the repository's object format with rev-parse; avoid hardcoding specific hashes or using short IDs as globally unique identifiers.

```bash
git rev-parse --show-object-format
git hash-object --no-filters src/state.txt
git rev-parse HEAD:src/state.txt
printf '%s\n' bad | git hash-object --stdin
printf '%s\n' ok | git hash-object --stdin
```

## Common mistakes and safety

Use the disposable fixture only. Never modify object or ref files by hand, force pruning, or run experiments against a real repository. If state differs, inspect with status, log and read-only plumbing; close the dedicated shell and remove only the recorded sandbox through the file manager after reviewing contents.

## Exercise and self-check

Why can two commits with the same tree differ? Parent IDs, author/committer data, timestamps or messages can differ.

## Quick reference

- `git rev-parse --show-object-format`
- `git hash-object --no-filters src/state.txt`
- `git rev-parse HEAD:src/state.txt`

## Official sources

- [https://git-scm.com/docs/git-hash-object](https://git-scm.com/docs/git-hash-object)
- [https://git-scm.com/docs/git-rev-parse](https://git-scm.com/docs/git-rev-parse)
- [https://git-scm.com/docs/hash-function-transition](https://git-scm.com/docs/hash-function-transition)

---

<!-- navigation-footer -->
[Previous](../03-commits-and-tags/README.md) · [Index](../README.md) · [Next](../05-refs-and-head/README.md)
<!-- /navigation-footer -->
