# Environments, variables and secrets

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../07-artifacts-and-cache/README.md) · [Index](../README.md) · [Next](../09-quality-gates-and-troubleshooting/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 40 min

**Prerequisites:** [GitHub](../../github/README.md) · [GitLab](../../gitlab/README.md) · [Artifacts and cache](../07-artifacts-and-cache/README.md)

**Objective:** Separate deployment targets, non-sensitive configuration and credentials; apply least privilege.

## What and why

An environment is a deployment target or platform resource representing one, such as staging or production. A variable stores configuration; a secret stores sensitive material and must not be committed. In GitHub Actions, environment protection rules and environment secrets can restrict deployment jobs, subject to plan, visibility and settings. In GitLab, environments and scoped, masked, hidden or protected CI/CD variables have distinct meanings and eligibility. Masking reduces accidental disclosure in some logs; it is not protection against malicious code. A protected variable is scoped to eligible protected refs and pipeline conditions, not universally safe. GitHub's automatic token and GitLab's job token also need least privilege. Prefer short-lived scoped credentials, approved trusted jobs and separate deployment identities; no real credential is necessary for this course.

## Practice

Offline design two targets: `staging` and `production`. Classify `APP_MODE=staging` as non-sensitive and `DEPLOY_CREDENTIAL` as a credential name only (do not assign a value). Build an access table: PR checks get no deployment credentials; approved deployment gets narrowly scoped access to its target. Label approval mechanisms as manual or enforced only after checking actual plan/settings.

## Common mistakes and safety

Never echo secrets, place them in artifacts or expose them to untrusted code. On suspected exposure, stop affected runs, revoke/rotate credentials, notify authorized maintainers and investigate logs and scope. Removing a YAML value or masking it does not revoke a credential. Do not create real environments or secrets for practice.

## Exercise and self-check

Pass if PR checks cannot reach deployment credentials, production promotion is separately authorized, and masking is not mistaken for isolation.

## Quick reference

environment / variable / secret

## Official sources

- <https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments>
- <https://docs.github.com/en/actions/reference/security/secure-use>
- <https://docs.gitlab.com/ci/variables/>
- <https://docs.gitlab.com/ci/environments/>

---

<!-- navigation-footer -->
[Previous](../07-artifacts-and-cache/README.md) · [Index](../README.md) · [Next](../09-quality-gates-and-troubleshooting/README.md)
<!-- /navigation-footer -->
