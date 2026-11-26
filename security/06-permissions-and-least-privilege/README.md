# Permissions and least privilege

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../05-secrets-and-disclosure-prevention/README.md) · [Index](../README.md) · [Next](../07-branch-protection-and-rulesets/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 40 min

**Prerequisites:** [Professional workflows](../../professional-workflows/README.md) · [Secrets and disclosure prevention](../05-secrets-and-disclosure-prevention/README.md)

**Objective:** Design a least-privilege access matrix.

## What and why

Least privilege grants only the resources and actions needed for the task, for the necessary duration. Distinguish repository roles, branch permissions, API token permissions and CI runtime identities. GitHub roles and GitLab project/group roles are platform-specific, not equivalent by name; plan, instance and inherited membership affect effective access. A read-only build job should not receive deployment credentials; a release identity should not be usable by untrusted PR code. Separate duties where possible, periodically review stale access and document exceptions. A successful login or public clone does not authorize mutation.

## Practice

Build an access matrix for fictional reader, contributor, reviewer, maintainer, CI check and production deployment identity. For each mark read, propose change, approve, integrate or deploy only if needed. Record owner and review date. Explain why an automation identity with repository-wide write access is excessive for lint.

## Risks and recovery

Never solve a permission error by making everyone an administrator or allowing privileged execution of untrusted code. Inspect effective policy and request the narrowest authorized adjustment; revoke obsolete grants.

## Exercise and self-check

Reader reads, contributor proposes, review/merge/deploy rights follow separate policy; CI read-only unless a separately justified job needs more.

## Quick reference

role / resource / action / duration

## References

- <https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/repository-roles-for-an-organization>
- <https://docs.gitlab.com/user/permissions/>
- <https://docs.github.com/en/actions/reference/security/secure-use>
