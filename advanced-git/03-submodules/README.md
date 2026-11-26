# Submodules: pinned repository dependencies

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../02-worktree/README.md) · [Index](../README.md) · [Next](../04-subtree/README.md)
<!-- /navigation -->

**Level:** advanced · **Estimated time:** 45 min

**Prerequisites:** [13 Advanced Git](../README.md) · [Security & Governance](../../security/README.md)

**Objective:** A superproject records a gitlink (mode 160000) to a specific commit of another repository; .gitmodules records path and URL metadata.

## What and why

A superproject records a gitlink (mode 160000) to a specific commit of another repository; .gitmodules records path and URL metadata. Updating the dependency requires committing the new gitlink in the parent. Submodule checkout often has detached HEAD. Use when teams need separate history and explicit pinned revisions; avoid if ordinary files suffice.

## Practice

Create a fresh isolated fixture using the module index before each practice. Run one command at a time; stop on unexpected results. Check the printed sandbox and repository root before any changes. Use Git 2.34+ as the practice baseline; check command help and skip unavailable optional features. No commands on production repositories.

Clone only the owned fixture into a local sibling, then add it as a submodule. The command-scoped file permission is only for this known local lab, never a global change. Inspect staged .gitmodules and mode 160000. Before committing any real dependency, review its URL, license and commit; do not recursively initialize unknown repositories.

```bash
git clone --no-hardlinks . "$sandbox/library"
git -c protocol.file.allow=always submodule add "$sandbox/library" vendor/library
git diff --cached -- .gitmodules
git ls-files --stage -- vendor/library
git submodule status
```

## Common mistakes and safety

Use only the disposable fixture and fictional data. If state differs, stop; inspect status and the relevant operation before aborting or recreating the fixture. Close the dedicated shell and remove only the recorded sandbox through the file manager after reviewing its contents.

## Exercise and self-check

What does the parent store? A commit ID, not a copy of all child files. A fresh clone needs an explicit initialization/update step.

## Quick reference

- `git clone --no-hardlinks . "$sandbox/library"`
- `git -c protocol.file.allow=always submodule add "$sandbox/library" vendor/library`
- `git diff --cached -- .gitmodules`
- `git ls-files --stage -- vendor/library`

## Official sources

- [https://git-scm.com/docs/git-submodule](https://git-scm.com/docs/git-submodule)
- [https://git-scm.com/docs/gitsubmodules](https://git-scm.com/docs/gitsubmodules)

---

<!-- navigation-footer -->
[Previous](../02-worktree/README.md) · [Index](../README.md) · [Next](../04-subtree/README.md)
<!-- /navigation-footer -->
