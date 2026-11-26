# Loose objects and packfiles

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../06-index-internals/README.md) · [Index](../README.md) · [Next](../08-gc-and-maintenance/README.md)
<!-- /navigation -->

**Level:** advanced · **Estimated time:** 40 min

**Prerequisites:** [14 Git Internals](../README.md) · [Advanced Git](../../advanced-git/README.md)

**Objective:** Objects may be stored individually or in packs with indexes and delta compression.

## What and why

Objects may be stored individually or in packs with indexes and delta compression. Packing changes storage representation, not the object identity or logical commit graph. Git uses deltas for compression even though its logical snapshots are trees. Use count-objects to inspect repository size and avoid guessing history from disk layout.

```text
logical object ID B
       |
       +-> loose object (before repack)
       +-> pack + index (after repack)
          same logical bytes
```

The arrows show references or operation relationships, not filesystem paths.

## Practice

Create a fresh isolated fixture from the linked Advanced Git module index before each practice. Run commands individually and stop on unexpected results. Confirm root and printed sandbox. Git 2.34+ practice baseline, Bash (Git Bash on Windows).

In the fresh small fixture, run `git repack -a` (no deletion option). Compare HEAD and the same blob contents before and after. Counts and sizes vary; do not infer an exact pack count. Use pack inspection tools only on owned repos and never delete packfiles manually.

```bash
before=$(git rev-parse HEAD)
git count-objects -v
git repack -a
git count-objects -v
test "$(git rev-parse HEAD)" = "$before"
git cat-file -p HEAD:src/state.txt
```

## Common mistakes and safety

Use the disposable fixture only. Never modify object or ref files by hand, force pruning, or run experiments against a real repository. If state differs, inspect with status, log and read-only plumbing; close the dedicated shell and remove only the recorded sandbox through the file manager after reviewing contents.

## Exercise and self-check

Can a blob stored as a delta still be read normally? Yes; Git reconstructs the original object bytes.

## Quick reference

- `git count-objects -v`
- `git repack -a`
- `git count-objects -v`
- `git cat-file -p HEAD:src/state.txt`

## Official sources

- [https://git-scm.com/docs/git-repack](https://git-scm.com/docs/git-repack)
- [https://git-scm.com/docs/git-count-objects](https://git-scm.com/docs/git-count-objects)
- [https://git-scm.com/docs/gitformat-pack](https://git-scm.com/docs/gitformat-pack)

---

<!-- navigation-footer -->
[Previous](../06-index-internals/README.md) · [Index](../README.md) · [Next](../08-gc-and-maintenance/README.md)
<!-- /navigation-footer -->
