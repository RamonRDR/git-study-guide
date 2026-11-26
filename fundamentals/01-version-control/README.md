# Why version control exists

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous module](../../getting-started/README.md) · [Index](../README.md) · [Next](../02-history-of-git/README.md)
<!-- /navigation -->

**Level:** beginner · **Estimated time:** 20 min

**Prerequisites:** [Getting Started](../../getting-started/README.md)

**Objective:** Explain intentional history versus ordinary saving.

## What and why

Version control records revisions to compare changes and identify decisions. Saving overwrites current contents; manual copies like plan-final.txt and plan-final-2.txt get confusing. Git records chosen snapshots and their parent relationships. It works well for code and text documentation, not automatically for huge media or databases. It does not replace backups: disk loss can destroy local history.

## Practice

A fictional library changes weekday hours and Saturday hours. Instead of three final copies, record each change separately. Initial snapshot -> weekday revision -> Saturday revision; arrows describe history, not filenames. In your lab, inspect history without internet.

```text
git log -1 --oneline
```

## Common mistakes and safety

Do not commit secrets or private data. Git does not record every save automatically or guarantee recovery of uncommitted edits. Keep independent backups.

## Exercise and self-check

Suggest two focused commit messages. Hint: one purpose per change. Reference: `docs: update weekday hours` and `docs: update Saturday hours`. Pass if you explain why history is clearer and backup still matters.

## Quick reference

- `git log -1 --oneline`

## Official sources

- [https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control)
- [https://git-scm.com/book/en/v2/Getting-Started-What-is-Git](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git)

---

<!-- navigation-footer -->
[Previous module](../../getting-started/README.md) · [Index](../README.md) · [Next](../02-history-of-git/README.md)
<!-- /navigation-footer -->
