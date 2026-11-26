# Projects, groups and GitLab offerings

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
— · [Index](../README.md) · [Next](../02-visibility-permissions-and-authentication/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 30 min

**Prerequisites:** [GitHub](../../github/README.md) · [Remotes](../../remote-repositories/README.md)

**Objective:** Distinguish Git data from GitLab services and choose an appropriate namespace and offering.

## What and why

Git stores commits, trees, branches and tags. GitLab adds a project around a repository: issues, merge requests (MRs), access control, pipelines and releases. A clone contains Git data, not the complete project database. A namespace identifies where a project lives. A group can contain projects and subgroups; membership and settings can flow down the hierarchy. For example, `studio/tools/catalog` may represent group `studio`, subgroup `tools`, and project `catalog`. A personal namespace is not a shared group. GitLab.com is a hosted multi-tenant service; Self-Managed is installed and administered by an organization, which bears infrastructure and maintenance costs; Dedicated is managed single-tenant hosting. Offering and subscription tier (Free, Premium, Ultimate) are separate decisions. Available features also depend on version, settings and permissions.

## Practice

On paper design a group for a fictional studio, with a `tools` subgroup and two projects. Draw local clone → Git repository → GitLab project → group; classify a commit, an issue, a tag and an MR. Optionally inspect a public GitLab project in a browser without logging in or posting. For a team needing central membership, prefer a group rather than distributing ownership among personal namespaces.

## Common mistakes and safety

Do not transfer or rename real projects as an exercise: paths, integrations and inherited access may change. Self-Managed is not automatically cost-free. Check the instance version and plan before promising features; no installation is needed.

## Exercise and self-check

Can a clone recover all issues and group memberships? No. Pass if Git objects and hosted metadata are distinct, the hierarchy is correct, and the chosen offering has an identified administrator.

## Official sources

- <https://docs.gitlab.com/user/namespace/>
- <https://docs.gitlab.com/user/group/>
- <https://docs.gitlab.com/subscriptions/choosing_subscription/>
