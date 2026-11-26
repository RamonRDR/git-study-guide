# Sparse checkout: select working files

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../06-rerere/README.md) · [Index](../README.md) · [Next](../08-partial-and-shallow-clone/README.md)
<!-- /navigation -->

**Level:** advanced · **Estimated time:** 40 min

**Prerequisites:** [13 Advanced Git](../README.md) · [Security & Governance](../../security/README.md)

**Objective:** Sparse checkout limits which tracked paths populate the working tree, without removing them from commits.

## What and why

Sparse checkout limits which tracked paths populate the working tree, without removing them from commits. Cone mode selects directories; it may also retain files in ancestor directories. This can reduce checkout costs in a monorepo. It is not access control and does not necessarily reduce downloaded history or object storage.

## Practice

Create a fresh isolated fixture using the module index before each practice. Run one command at a time; stop on unexpected results. Check the printed sandbox and repository root before any changes. Use Git 2.34+ as the practice baseline; check command help and skip unavailable optional features. No commands on production repositories.

Use a clean fresh fixture with docs and src. Select docs and inspect the commit tree; src/state.txt remains in HEAD although absent from the working tree. Disable sparse checkout to restore the full checkout; do not force when local modifications are present.

For compatibility with Git 2.34, initialize cone mode explicitly before setting directories. Confirm `core.sparseCheckoutCone` is true; the newer combined `set --cone` syntax is not used here.

```bash
git sparse-checkout init --cone
git sparse-checkout set docs
test "$(git config --bool --get core.sparseCheckoutCone)" = true
git sparse-checkout list
git ls-tree -r --name-only HEAD
test ! -f src/state.txt
git sparse-checkout disable
test -f src/state.txt
git status --short
```

## Common mistakes and safety

Use only the disposable fixture and fictional data. If state differs, stop; inspect status and the relevant operation before aborting or recreating the fixture. Close the dedicated shell and remove only the recorded sandbox through the file manager after reviewing its contents.

## Exercise and self-check

Is a file outside the cone deleted from Git? No; its snapshot remains in the commit.

## Quick reference

- `git sparse-checkout init --cone`
- `git sparse-checkout set docs`
- `git config --bool --get core.sparseCheckoutCone`
- `git sparse-checkout list`
- `git ls-tree -r --name-only HEAD`
- `git sparse-checkout disable`

## Official sources

- [https://git-scm.com/docs/git-sparse-checkout](https://git-scm.com/docs/git-sparse-checkout)
- [https://git-scm.com/docs/git-sparse-checkout/2.34.0](https://git-scm.com/docs/git-sparse-checkout/2.34.0)
- [https://git-scm.com/docs/git-ls-tree](https://git-scm.com/docs/git-ls-tree)

---

<!-- navigation-footer -->
[Previous](../06-rerere/README.md) · [Index](../README.md) · [Next](../08-partial-and-shallow-clone/README.md)
<!-- /navigation-footer -->
