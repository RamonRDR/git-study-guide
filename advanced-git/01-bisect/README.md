# Bisect: isolate a regression

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous module](../../security/README.md) · [Index](../README.md) · [Next](../02-worktree/README.md)
<!-- /navigation -->

**Level:** advanced · **Estimated time:** 45 min

**Prerequisites:** [13 Advanced Git](../README.md) · [Security & Governance](../../security/README.md)

**Objective:** Find the first bad commit using known good and bad endpoints.

## What and why

Find the first bad commit using known good and bad endpoints. Git narrows the reachable candidates by selecting commits to test; it does not diagnose the bug itself. Use a deterministic test with a stable environment; if a commit cannot be tested, use skip, which may leave multiple candidates. In a professional incident, record the tested range and verify the result against its parent before proposing a fix.

## Practice

Create a fresh isolated fixture using the module index before each practice. Run one command at a time; stop on unexpected results. Check the printed sandbox and repository root before any changes. Use Git 2.34+ as the practice baseline; check command help and skip unavailable optional features. No commands on production repositories.

The fixture's middle commit still has `ok` in `src/state.txt`. After `git bisect start`, inspect the selected commit; mark it good only after confirming `ok`. The final result should be the newest commit. Reset returns to the original checkout. If the outcome differs, reset and inspect the fixture.

```bash
git bisect start HEAD HEAD~2
git show HEAD:src/state.txt
git bisect good
git bisect log
git bisect reset
git status --short
```

## Common mistakes and safety

Use only the disposable fixture and fictional data. If state differs, stop; inspect status and the relevant operation before aborting or recreating the fixture. Close the dedicated shell and remove only the recorded sandbox through the file manager after reviewing its contents.

## Exercise and self-check

Why not automatically mark a skipped commit good? It may contain the regression; the interval becomes unreliable.

## Quick reference

- `git bisect start HEAD HEAD~2`
- `git show HEAD:src/state.txt`
- `git bisect good`
- `git bisect log`

## Official sources

- [https://git-scm.com/docs/git-bisect](https://git-scm.com/docs/git-bisect)
- [https://git-scm.com/docs/git-rev-list](https://git-scm.com/docs/git-rev-list)

---

<!-- navigation-footer -->
[Previous module](../../security/README.md) · [Index](../README.md) · [Next](../02-worktree/README.md)
<!-- /navigation-footer -->
