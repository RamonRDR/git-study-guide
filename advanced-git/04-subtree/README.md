# Subtree: vendor content into a repository

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../03-submodules/README.md) · [Index](../README.md) · [Next](../05-hooks/README.md)
<!-- /navigation -->

**Level:** advanced · **Estimated time:** 40 min

**Prerequisites:** [13 Advanced Git](../README.md) · [Security & Governance](../../security/README.md)

**Objective:** Unlike a submodule, a subtree stores ordinary tracked files under a prefix.

## What and why

Unlike a submodule, a subtree stores ordinary tracked files under a prefix. The optional git subtree helper can import and synchronize another history; --squash imports a condensed snapshot rather than joining all its history. This is convenient for consumers but upstream synchronization and provenance remain responsibilities.

## Practice

Create a fresh isolated fixture using the module index before each practice. Run one command at a time; stop on unexpected results. Check the printed sandbox and repository root before any changes. Use Git 2.34+ as the practice baseline; check command help and skip unavailable optional features. No commands on production repositories.

Check `git subtree -h` for availability (help may return a nonzero exit). If unavailable, stop at conceptual comparison; do not download arbitrary scripts. Clone the known local fixture, import it under a new prefix and inspect tracked files and graph. No network. Review licenses and avoid overwriting an existing prefix.

```bash
git clone --no-hardlinks . "$sandbox/library"
git subtree add --prefix=vendor/library "$sandbox/library" main --squash
git ls-files --stage -- vendor/library
git log --oneline --graph --all -6
```

## Common mistakes and safety

Use only the disposable fixture and fictional data. If state differs, stop; inspect status and the relevant operation before aborting or recreating the fixture. Close the dedicated shell and remove only the recorded sandbox through the file manager after reviewing its contents.

## Exercise and self-check

Which approach keeps independent checkout metadata? Submodule; subtree puts ordinary files in the parent.

## Quick reference

- `git clone --no-hardlinks . "$sandbox/library"`
- `git subtree add --prefix=vendor/library "$sandbox/library" main --squash`
- `git ls-files --stage -- vendor/library`
- `git log --oneline --graph --all -6`

## Official sources

- [https://git-scm.com/docs/git-merge](https://git-scm.com/docs/git-merge)
- [https://github.com/git/git/blob/master/contrib/subtree/git-subtree.adoc](https://github.com/git/git/blob/master/contrib/subtree/git-subtree.adoc)
- [https://git-scm.com/docs/gitsubmodules](https://git-scm.com/docs/gitsubmodules)

---

<!-- navigation-footer -->
[Previous](../03-submodules/README.md) · [Index](../README.md) · [Next](../05-hooks/README.md)
<!-- /navigation-footer -->
