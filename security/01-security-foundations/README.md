# Git security foundations

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous module](../../professional-workflows/README.md) · [Index](../README.md) · [Next](../02-ssh-authentication/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 30 min

**Prerequisites:** [Professional workflows](../../professional-workflows/README.md)

**Objective:** Distinguish security layers and trust boundaries.

## What and why

Security protects confidentiality (who can read), integrity (what is authentic and unchanged) and availability (whether the service is usable). Authentication identifies an actor; authorization determines allowed actions. Git records content and history, not a complete access-control system. A commit hash identifies an object, not the identity or trustworthiness of its author. Local file permissions, hosting policies and CI permissions are distinct layers. A public repository can be readable by anyone without granting write access. Copies, clones and forks may outlive deletion.

## Practice

For a fictional library catalog, classify public documentation, private staff records and the permission to merge. Draw boundaries between workstation, host and runner. For each, identify one asset, threat and control. A read-only user should be able to read public docs, not alter main.

## Risks and recovery

Do not assume private repositories are a secret vault, hashes are signatures or public visibility grants write access. If a boundary is unclear, stop and verify actual permissions with an authorized administrator.

## Exercise and self-check

Public docs are readable; private staff records are excluded from the exercise; merge is an authorization decision. Explain all three security properties.

## Quick reference

confidentiality / integrity / availability / authentication / authorization

## References

- <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github>
- <https://git-scm.com/docs/git>

---

<!-- navigation-footer -->
[Previous module](../../professional-workflows/README.md) · [Index](../README.md) · [Next](../02-ssh-authentication/README.md)
<!-- /navigation-footer -->
