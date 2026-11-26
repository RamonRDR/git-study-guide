# Porcelain and plumbing: stable inspection

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../09-reflogs-and-reachability/README.md) · [Index](../README.md) · [Next](../11-integrated-internals-lab/README.md)
<!-- /navigation -->

**Level:** advanced · **Estimated time:** 40 min

**Prerequisites:** [14 Git Internals](../README.md) · [Advanced Git](../../advanced-git/README.md)

**Objective:** Porcelain commands support user workflows; plumbing commands expose primitives for scripts and diagnostics.

## What and why

Porcelain commands support user workflows; plumbing commands expose primitives for scripts and diagnostics. `git status --porcelain=v1` provides a stable machine-oriented status format despite the name porcelain. Prefer documented output formats and NUL-delimited path lists for scripts; avoid parsing human-localized messages. Plumbing can change refs or objects, so favor read-only inspection until you understand invariants.

## Practice

Create a fresh isolated fixture from the linked Advanced Git module index before each practice. Run commands individually and stop on unexpected results. Confirm root and printed sandbox. Git 2.34+ practice baseline, Bash (Git Bash on Windows).

Compare human status with porcelain and object inspection. The clean fixture gives empty porcelain output; rev-parse resolves HEAD independently of human log formatting. For arbitrary filenames use NUL output (`-z`) and a parser supporting it, not line splitting. Avoid direct update-ref in shared repositories.

```bash
git status
git status --porcelain=v1
git rev-parse --verify HEAD
git cat-file -t HEAD
git ls-files --stage
git ls-tree -r HEAD
```

## Common mistakes and safety

Use the disposable fixture only. Never modify object or ref files by hand, force pruning, or run experiments against a real repository. If state differs, inspect with status, log and read-only plumbing; close the dedicated shell and remove only the recorded sandbox through the file manager after reviewing contents.

## Exercise and self-check

Why not parse `git status` text for CI? It may vary by locale or configuration; use the documented porcelain format and exit status.

## Quick reference

- `git status`
- `git status --porcelain=v1`
- `git rev-parse --verify HEAD`
- `git cat-file -t HEAD`

## Official sources

- [https://git-scm.com/docs/git](https://git-scm.com/docs/git)
- [https://git-scm.com/docs/git-status](https://git-scm.com/docs/git-status)
- [https://git-scm.com/docs/git-rev-parse](https://git-scm.com/docs/git-rev-parse)

---

<!-- navigation-footer -->
[Previous](../09-reflogs-and-reachability/README.md) · [Index](../README.md) · [Next](../11-integrated-internals-lab/README.md)
<!-- /navigation-footer -->
