# Integrated advanced Git lab

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../10-archive-and-bundle/README.md) · [Index](../README.md) · [Next module](../../git-internals/README.md)
<!-- /navigation -->

**Level:** advanced · **Estimated time:** 55 min

**Prerequisites:** [13 Advanced Git](../README.md) · [Security & Governance](../../security/README.md)

**Objective:** Simulate reviewing a regression while keeping main stable, then prepare an offline history transfer.

## What and why

Simulate reviewing a regression while keeping main stable, then prepare an offline history transfer. The exercise joins worktree, inspection and bundle without changing main's history. In professional work, save evidence of the tested revision, review diff and validate recovery before delivery.

## Practice

Create a fresh isolated fixture using the module index before each practice. Run one command at a time; stop on unexpected results. Check the printed sandbox and repository root before any changes. Use Git 2.34+ as the practice baseline; check command help and skip unavailable optional features. No commands on production repositories.

Run on the fresh fixture, one command at a time. The review worktree must show ok, main bad; the bundle clone must match original main. All checks must succeed; otherwise stop and inspect. No remote network or publishing. Remove the clean linked worktree normally; leave the sandbox for review.

```bash
before=$(git rev-parse HEAD)
git worktree add -b review "$sandbox/review" HEAD~1
test "$(git -C "$sandbox/review" show HEAD:src/state.txt)" = ok
test "$(git show HEAD:src/state.txt)" = bad
git worktree remove "$sandbox/review"
git bundle create "$sandbox/history.bundle" main
git bundle verify "$sandbox/history.bundle"
git clone -b main "$sandbox/history.bundle" "$sandbox/recovered"
test "$(git -C "$sandbox/recovered" rev-parse HEAD)" = "$before"
test "$(git rev-parse HEAD)" = "$before"
test -z "$(git status --porcelain)"
test -z "$(git remote)"
```

## Common mistakes and safety

Use only the disposable fixture and fictional data. If state differs, stop; inspect status and the relevant operation before aborting or recreating the fixture. Close the dedicated shell and remove only the recorded sandbox through the file manager after reviewing its contents.

## Exercise and self-check

Pass when each test exits zero, main is clean and the recovered tip matches. Explain why this bundle is not a backup of the whole workstation.

## Quick reference

- `git worktree add -b review "<sandbox>/review" HEAD~1`
- `git worktree remove "<sandbox>/review"`
- `git bundle create "<sandbox>/history.bundle" main`
- `git bundle verify "<sandbox>/history.bundle"`

## Official sources

- [https://git-scm.com/docs/git-worktree](https://git-scm.com/docs/git-worktree)
- [https://git-scm.com/docs/git-bundle](https://git-scm.com/docs/git-bundle)
- [https://git-scm.com/docs/git-status](https://git-scm.com/docs/git-status)

---

<!-- navigation-footer -->
[Previous](../10-archive-and-bundle/README.md) · [Index](../README.md) · [Next module](../../git-internals/README.md)
<!-- /navigation-footer -->
