# Partial and shallow clones

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../07-sparse-checkout/README.md) · [Index](../README.md) · [Next](../09-blame-and-grep/README.md)
<!-- /navigation -->

**Level:** advanced · **Estimated time:** 45 min

**Prerequisites:** [13 Advanced Git](../README.md) · [Security & Governance](../../security/README.md)

**Objective:** Shallow clone truncates visible ancestry with --depth; partial clone requests a filtered object set such as --filter=blob:none and may fetch omitted objects on demand from a promisor remote.

## What and why

Shallow clone truncates visible ancestry with --depth; partial clone requests a filtered object set such as --filter=blob:none and may fetch omitted objects on demand from a promisor remote. Sparse checkout selects working paths, a different dimension. Use shallow clones for bounded CI only if history-based operations are unnecessary; partial clone requires server support and connectivity for omitted objects.

## Practice

Create a fresh isolated fixture using the module index before each practice. Run one command at a time; stop on unexpected results. Check the printed sandbox and repository root before any changes. Use Git 2.34+ as the practice baseline; check command help and skip unavailable optional features. No commands on production repositories.

Use --no-local to exercise depth against the owned local path rather than local clone optimization. Verify one visible commit and shallow=true. `git fetch --unshallow` from that same complete source restores ancestry. Partial clone is a conceptual comparison here: do not contact a server or assume filtering is honored.

```bash
git clone --no-local --depth 1 . "$sandbox/shallow"
git -C "$sandbox/shallow" rev-parse --is-shallow-repository
git -C "$sandbox/shallow" rev-list --count HEAD
git -C "$sandbox/shallow" fetch --unshallow
git -C "$sandbox/shallow" rev-list --count HEAD
```

## Common mistakes and safety

Use only the disposable fixture and fictional data. If state differs, stop; inspect status and the relevant operation before aborting or recreating the fixture. Close the dedicated shell and remove only the recorded sandbox through the file manager after reviewing its contents.

## Exercise and self-check

Which technique can omit blobs while retaining commit ancestry? Partial clone, if the filter is supported.

## Quick reference

- `git clone --no-local --depth 1 . "$sandbox/shallow"`
- `git -C "$sandbox/shallow" rev-parse --is-shallow-repository`
- `git -C "$sandbox/shallow" rev-list --count HEAD`
- `git -C "$sandbox/shallow" fetch --unshallow`

## Official sources

- [https://git-scm.com/docs/git-clone](https://git-scm.com/docs/git-clone)
- [https://git-scm.com/docs/git-fetch](https://git-scm.com/docs/git-fetch)
- [https://git-scm.com/docs/partial-clone](https://git-scm.com/docs/partial-clone)

---

<!-- navigation-footer -->
[Previous](../07-sparse-checkout/README.md) · [Index](../README.md) · [Next](../09-blame-and-grep/README.md)
<!-- /navigation-footer -->
