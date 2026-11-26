# Centralized, distributed and hosting platforms

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../02-history-of-git/README.md) · [Index](../README.md) · [Next module](../../git-architecture/README.md)
<!-- /navigation -->

**Level:** beginner · **Estimated time:** 25 min

**Prerequisites:** [Linux, BitKeeper and the birth of Git](../02-history-of-git/README.md)

**Objective:** Distinguish VCS models, Git and hosting platforms.

## What and why

A centralized VCS uses a central history store; clients typically contact it to record shared revisions. A distributed VCS like Git normally gives each clone (repository copy) its own local history; shallow or partial clones may omit history or objects. Teams can still choose an authoritative shared repository. GitHub and GitLab host Git repositories and offer issues, reviews and automation. Git itself is the version control system. A remote is a configured location of another repository.

## Practice

Centralized: Alice working copy -> central history <- Bob working copy. Distributed: Alice local history <-> shared remote <-> Bob local history. Arrows show communication. Git local commits work without the shared server. GitHub uses pull requests; GitLab uses merge requests, both platform review objects, not native Git commands. Inspect your lab:

```text
git log -1 --oneline
git remote -v
```

Expected: local history and no remotes (none configured). No account is needed. Centralized models may simplify central administration; distributed ones favor local work but still require coordination.

## Common mistakes and safety

Distributed does not mean automatic backup, permissions or synchronization. A local commit is not an upload. Do not copy credentials or add real remotes yet. Clean up only your exact disposable folder as described in the first-commit lesson, or keep it for future practice.

## Exercise and self-check

Classify `git commit`, pull request, merge request and `git log`. Hint: which are local commands? Answer: commit/log are Git; PR/MR are platform review features. Pass if you explain offline history and why teams still need a shared remote.

## Quick reference

- `git log -1 --oneline`
- `git remote -v`

## Official sources

- [https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control)
- [https://git-scm.com/book/en/v2/Getting-Started-What-is-Git](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git)
- [https://docs.github.com/](https://docs.github.com/)
- [https://docs.gitlab.com/](https://docs.gitlab.com/)

---

<!-- navigation-footer -->
[Previous](../02-history-of-git/README.md) · [Index](../README.md) · [Next module](../../git-architecture/README.md)
<!-- /navigation-footer -->
