# Forks and open-source contributions

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../04-pull-requests-and-review/README.md) · [Index](../README.md) · [Next](../06-protection-and-rulesets/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 30 min

**Prerequisites:** [Remotes](../../remote-repositories/README.md) · [History & recovery](../../history-and-recovery/README.md) · [Pull requests and code review](../04-pull-requests-and-review/README.md)

**Objective:** Explain fork-based contributions and keep upstream separate from origin.

## What and why

A GitHub fork is a hosted repository associated with an original repository; clone is a native Git copy. A fork does not grant write access to the original. A typical local clone of a fork uses origin for the fork and upstream for the original; these are conventions, not reserved names. Fetch upstream, inspect divergence and update a clean local default branch with fast-forward only if possible. Make contributions on separate branches; push to the fork and propose PR from fork head to original base. Follow license, CONTRIBUTING, code of conduct and issue policy. A maintainer may decline a contribution.

## Practice

Offline: draw original hosted repo -> fork hosted repo -> local clone; label upstream and origin from local perspective. Reuse the local bare-remote model from module 06 to reason about tracking refs; it simulates Git transport, not GitHub fork metadata. Optional read-only: inspect the fork button and contribution instructions in a public project without forking or submitting a practice PR. If a real contribution is wanted later, coordinate with maintainers first. Check upstream URL, branch, status and divergence before any sync. Do not force synchronization if fast-forward is refused.

## Common mistakes and safety

Do not assume forks hide public content or license obligations. Avoid unsolicited practice submissions, duplicated issues and confidential patches. If you targeted the wrong base, stop and correct or close your own PR rather than merging it.

## Exercise and self-check

Where does a contributor push a proposed branch when they lack upstream write access? Their authorized fork. Pass if arrows and PR direction are correct and Git tracking refs are distinguished from hosted forks.

## Quick reference

- `origin`
- `upstream`
- `fork`
- `clone`

## Official sources

- <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks>
- <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork>
- <https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-open-source>
