# Worktrees: parallel working directories

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../01-bisect/README.md) · [Index](../README.md) · [Next](../03-submodules/README.md)
<!-- /navigation -->

**Level:** advanced · **Estimated time:** 40 min

**Prerequisites:** [13 Advanced Git](../README.md) · [Security & Governance](../../security/README.md)

**Objective:** A linked worktree has its own checkout, HEAD and index but shares most refs and objects with the main worktree.

## What and why

A linked worktree has its own checkout, HEAD and index but shares most refs and objects with the main worktree. This supports a hotfix while another task is open, without stashing or cloning the entire repository. Git normally prevents checking out the same branch twice. Worktrees are not security or configuration isolation boundaries.

## Practice

Create a fresh isolated fixture using the module index before each practice. Run one command at a time; stop on unexpected results. Check the printed sandbox and repository root before any changes. Use Git 2.34+ as the practice baseline; check command help and skip unavailable optional features. No commands on production repositories.

Create a distinct review branch in a sibling directory; compare HEAD and list both worktrees. Check the linked directory is clean before removal. Do not force removal of dirty worktrees or delete their directories manually; inspect `git worktree list` and use the documented repair procedure if moved.

```bash
git worktree add -b review "$sandbox/review" HEAD~1
git worktree list
git -C "$sandbox/review" status --short
git -C "$sandbox/review" rev-parse HEAD
git rev-parse HEAD
git worktree remove "$sandbox/review"
git worktree list
```

## Common mistakes and safety

Use only the disposable fixture and fictional data. If state differs, stop; inspect status and the relevant operation before aborting or recreating the fixture. Close the dedicated shell and remove only the recorded sandbox through the file manager after reviewing its contents.

## Exercise and self-check

Does a linked worktree have a separate object database? Normally no; checkout and index are separate.

## Quick reference

- `git worktree add -b review "$sandbox/review" HEAD~1`
- `git worktree list`
- `git -C "$sandbox/review" status --short`
- `git -C "$sandbox/review" rev-parse HEAD`

## Official sources

- [https://git-scm.com/docs/git-worktree](https://git-scm.com/docs/git-worktree)
- [https://git-scm.com/docs/gitrepository-layout](https://git-scm.com/docs/gitrepository-layout)

---

<!-- navigation-footer -->
[Previous](../01-bisect/README.md) · [Index](../README.md) · [Next](../03-submodules/README.md)
<!-- /navigation-footer -->
