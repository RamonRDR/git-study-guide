# Visibility, permissions and authentication

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../01-projects-groups-and-offerings/README.md) · [Index](../README.md) · [Next](../03-issues-labels-milestones-and-boards/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 35 min

**Prerequisites:** [GitHub](../../github/README.md) · [Remotes](../../remote-repositories/README.md)

**Objective:** Separate identity, effective permissions and read visibility; choose minimal access.

## What and why

Public projects expose public content to readers, not unrestricted write access. Private limits access to eligible members; internal visibility is available on Self-Managed and Dedicated, not GitLab.com. Internal is not private: eligible authenticated users may read it. Typical roles include Guest, Planner, Reporter, Developer, Maintainer and Owner; their exact abilities depend on tier, settings and resource. Reporter is generally suited to repository reading, Developer to feature branches, Maintainer to project management, and Owner to high-level ownership. Effective access can be inherited from groups; lowering one direct membership may not remove inherited access. Authentication establishes identity; authorization determines allowed operations. Use web login with 2FA, verified SSH host fingerprints and a public key (keep the private key local), or HTTPS with an appropriate credential helper or minimally scoped expiring token. Git configuration name/email is commit attribution, not login. Never put tokens in remote URLs or commands.

## Practice

Offline, assign a read-only analyst, contributor and maintainer to a fictional private project; justify each role and trace a Developer inherited from a parent group. Optional: inspect visibility and your own role in an owned disposable private sandbox without changing permissions or creating tokens. If access is denied, check host, identity, membership, branch restrictions and credential scope before escalating.

## Common mistakes and safety

Changing visibility cannot recall copies. If a credential is exposed, revoke/rotate it immediately and follow incident policy; deleting a commit is insufficient. Never disable host verification or grant Owner to fix an ordinary authentication error.

## Exercise and self-check

Can a public reader push to main automatically? No. Pass if you identify separate read, write, and merge authorization and inherited access, and propose no secret in Git history.

## Official sources

- <https://docs.gitlab.com/user/public_access/>
- <https://docs.gitlab.com/user/permissions/>
- <https://docs.gitlab.com/user/ssh/>
- <https://docs.gitlab.com/user/profile/personal_access_tokens/>
- <https://docs.gitlab.com/user/profile/account/two_factor_authentication/>

---

<!-- navigation-footer -->
[Previous](../01-projects-groups-and-offerings/README.md) · [Index](../README.md) · [Next](../03-issues-labels-milestones-and-boards/README.md)
<!-- /navigation-footer -->
