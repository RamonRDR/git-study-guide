# Permissions and authentication

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../01-platform-and-repositories/README.md) · [Index](../README.md) · [Next](../03-issues-and-planning/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 25 min

**Prerequisites:** [Remotes](../../remote-repositories/README.md) · [History & recovery](../../history-and-recovery/README.md) · [GitHub, repositories and visibility](../01-platform-and-repositories/README.md)

**Objective:** Separate identity, authentication and authorization and apply least privilege.

## What and why

Commit author fields identify a claimed author; they are not login credentials. Authentication verifies access to an account; authorization decides permitted actions. Organization repository roles include read, triage, write, maintain and admin; personal repositories use a different permission model. A collaborator with write access can normally propose and push permitted branches but still faces rulesets. Owners/admins configure permissions; reviewers evaluate changes; maintainers decide integration. Use two-factor authentication, approved HTTPS credential managers or SSH keys, and narrowly scoped expiring tokens only if needed. Never store credentials in URLs, Markdown, shell history or screenshots. A verified signature is separate from authorization.

## Practice

Offline: fictional team has a reader, issue coordinator, developer and administrator. Assign the minimum organization role for reading, triaging issues, pushing feature branches and changing access respectively. Optional: review your own account security settings privately; no token generation, sharing or role changes required. Check official authentication guide before cloning any private sandbox; verify target account and repository. If access denied, inspect account, remote and policy rather than escalating permissions.

## Common mistakes and safety

Do not grant admin merely to fix a rejected push. If a credential leaks, revoke or rotate it immediately and notify the responsible owner; removing it from the latest commit is not enough. Never paste account diagnostics or tokens into issues.

## Exercise and self-check

Answer: read, triage, write, admin, subject to organization policy. Pass if author name is not treated as proof of login and permissions are not broadened unnecessarily.

## Quick reference

- `authentication`
- `authorization`
- `least privilege`

## Official sources

- <https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/repository-roles-for-an-organization>
- <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github>

---

<!-- navigation-footer -->
[Previous](../01-platform-and-repositories/README.md) · [Index](../README.md) · [Next](../03-issues-and-planning/README.md)
<!-- /navigation-footer -->
