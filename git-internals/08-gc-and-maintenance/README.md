# Garbage collection and maintenance

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../07-loose-objects-and-packfiles/README.md) · [Index](../README.md) · [Next](../09-reflogs-and-reachability/README.md)
<!-- /navigation -->

**Level:** advanced · **Estimated time:** 40 min

**Prerequisites:** [14 Git Internals](../README.md) · [Advanced Git](../../advanced-git/README.md)

**Objective:** Garbage collection organizes storage and can remove unreachable objects subject to retention policies; maintenance schedules or runs repository housekeeping tasks.

## What and why

Garbage collection organizes storage and can remove unreachable objects subject to retention policies; maintenance schedules or runs repository housekeeping tasks. Reachability and expiry depend on refs, reflogs, config and Git version. Immediate pruning can destroy recovery options and interfere with concurrent writers. Normal maintenance is not a secret-erasure guarantee.

## Practice

Create a fresh isolated fixture from the linked Advanced Git module index before each practice. Run commands individually and stop on unexpected results. Confirm root and printed sandbox. Git 2.34+ practice baseline, Bash (Git Bash on Windows).

Use diagnostics only in this chapter. Inspect counts, reachable object IDs and relevant config. No forced pruning, expiry changes, automatic scheduled jobs or manual object deletion. A professional maintenance plan includes backups, a quiet window and verification after maintenance. Config lookup can return nonzero when unset.

```bash
git count-objects -v
git rev-list --objects --all
git config --local --get gc.pruneExpire
git config --local --get gc.reflogExpire
git fsck --no-reflogs
```

## Common mistakes and safety

Use the disposable fixture only. Never modify object or ref files by hand, force pruning, or run experiments against a real repository. If state differs, inspect with status, log and read-only plumbing; close the dedicated shell and remove only the recorded sandbox through the file manager after reviewing contents.

## Exercise and self-check

Why not use immediate pruning for a lost commit? It may remove objects needed for recovery. Preserve evidence and consult recovery procedures first.

## Quick reference

- `git count-objects -v`
- `git rev-list --objects --all`
- `git config --local --get gc.pruneExpire`
- `git config --local --get gc.reflogExpire`

## Official sources

- [https://git-scm.com/docs/git-gc](https://git-scm.com/docs/git-gc)
- [https://git-scm.com/docs/git-maintenance](https://git-scm.com/docs/git-maintenance)
- [https://git-scm.com/docs/git-fsck](https://git-scm.com/docs/git-fsck)

---

<!-- navigation-footer -->
[Previous](../07-loose-objects-and-packfiles/README.md) · [Index](../README.md) · [Next](../09-reflogs-and-reachability/README.md)
<!-- /navigation-footer -->
