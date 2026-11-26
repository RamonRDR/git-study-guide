# Blame and grep: investigate changes

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../08-partial-and-shallow-clone/README.md) · [Index](../README.md) · [Next](../10-archive-and-bundle/README.md)
<!-- /navigation -->

**Level:** advanced · **Estimated time:** 35 min

**Prerequisites:** [13 Advanced Git](../README.md) · [Security & Governance](../../security/README.md)

**Objective:** Blame attributes each selected line to a commit according to the chosen history and options; it is not a measure of responsibility or quality.

## What and why

Blame attributes each selected line to a commit according to the chosen history and options; it is not a measure of responsibility or quality. Grep searches tracked working files by default or a named tree when given a revision. Combine with show/log to understand context in reviews, not assign fault to an author.

## Practice

Create a fresh isolated fixture using the module index before each practice. Run one command at a time; stop on unexpected results. Check the printed sandbox and repository root before any changes. Use Git 2.34+ as the practice baseline; check command help and skip unavailable optional features. No commands on production repositories.

Compare search against HEAD and its parent. grep returns 1 for no match; this is not necessarily an error in the investigation. `git blame` should identify the change to the single state line. Avoid searching or publishing private data; keep sample output fictional.

```bash
git blame -- src/state.txt
git grep -n bad HEAD -- src
git grep -n ok HEAD~1 -- src
git log -p -- src/state.txt
```

## Common mistakes and safety

Use only the disposable fixture and fictional data. If state differs, stop; inspect status and the relevant operation before aborting or recreating the fixture. Close the dedicated shell and remove only the recorded sandbox through the file manager after reviewing its contents.

## Exercise and self-check

Why inspect a commit after blame? A line attribution alone cannot explain intent or surrounding changes.

## Quick reference

- `git blame -- src/state.txt`
- `git grep -n bad HEAD -- src`
- `git grep -n ok HEAD~1 -- src`
- `git log -p -- src/state.txt`

## Official sources

- [https://git-scm.com/docs/git-blame](https://git-scm.com/docs/git-blame)
- [https://git-scm.com/docs/git-grep](https://git-scm.com/docs/git-grep)
- [https://git-scm.com/docs/git-log](https://git-scm.com/docs/git-log)

---

<!-- navigation-footer -->
[Previous](../08-partial-and-shallow-clone/README.md) · [Index](../README.md) · [Next](../10-archive-and-bundle/README.md)
<!-- /navigation-footer -->
