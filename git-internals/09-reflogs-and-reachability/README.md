# Reflogs and reachability

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../08-gc-and-maintenance/README.md) · [Index](../README.md) · [Next](../10-porcelain-and-plumbing/README.md)
<!-- /navigation -->

**Level:** advanced · **Estimated time:** 45 min

**Prerequisites:** [14 Git Internals](../README.md) · [Advanced Git](../../advanced-git/README.md)

**Objective:** An object is reachable from a root when traversing the relevant object edges (commit parents, trees, blobs and tag targets).

## What and why

An object is reachable from a root when traversing the relevant object edges (commit parents, trees, blobs and tag targets). Reflogs locally record updates to refs, often keeping previous tips recoverable even after a branch moves; they expire and are not generally transferred by clone. Reachability relative to current refs differs from reachability including reflogs and index.

```text
refs/heads/main -> C -> B -> A
reflog old tip --> D -> B -> A
                 (D may not be reachable from current refs)
```

The arrows show references or operation relationships, not filesystem paths.

## Practice

Create a fresh isolated fixture from the linked Advanced Git module index before each practice. Run commands individually and stop on unexpected results. Confirm root and printed sandbox. Git 2.34+ practice baseline, Bash (Git Bash on Windows).

Inspect current refs, reflog and reachable graph in the fixture. Read HEAD@{1} only after confirming the reflog has that entry. Use a new branch at a verified lost commit in real recovery rather than rewriting main. Never expire reflogs or prune objects as a recovery step.

```bash
git show-ref
git reflog show HEAD
git rev-list --all
git rev-list --all --reflog
git show --stat 'HEAD@{1}'
```

## Common mistakes and safety

Use the disposable fixture only. Never modify object or ref files by hand, force pruning, or run experiments against a real repository. If state differs, inspect with status, log and read-only plumbing; close the dedicated shell and remove only the recorded sandbox through the file manager after reviewing contents.

## Exercise and self-check

Can reflog guarantee recovery months later? No; expiry, configuration, deletion or object cleanup may remove evidence.

## Quick reference

- `git show-ref`
- `git reflog show HEAD`
- `git rev-list --all`
- `git rev-list --all --reflog`

## Official sources

- [https://git-scm.com/docs/git-reflog](https://git-scm.com/docs/git-reflog)
- [https://git-scm.com/docs/git-rev-list](https://git-scm.com/docs/git-rev-list)
- [https://git-scm.com/docs/git-fsck](https://git-scm.com/docs/git-fsck)

---

<!-- navigation-footer -->
[Previous](../08-gc-and-maintenance/README.md) · [Index](../README.md) · [Next](../10-porcelain-and-plumbing/README.md)
<!-- /navigation-footer -->
