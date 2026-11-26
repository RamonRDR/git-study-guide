# Optional GitLab CLI and platform comparison

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../07-tags-and-releases/README.md) · [Index](../README.md) · —
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 30 min

**Prerequisites:** [GitHub](../../github/README.md) · [Remotes](../../remote-repositories/README.md)

**Objective:** Choose native Git or a hosting CLI and map equivalent collaboration concepts without assuming feature parity.

## What and why

`git` manipulates Git objects and refs; `glab` is the separate GitLab CLI for platform resources through network APIs; `gh` is the analogous GitHub CLI. The GitLab CLI can work with GitLab.com and configured Self-Managed hosts; confirm the host and account before queries. In an already installed CLI, `glab --version` and `glab --help` inspect local tooling; `glab auth status` checks authentication state; `glab mr list`, `glab issue list` and `glab release list` query the selected project. They do not create or merge resources. For authenticated access follow official installation/authentication docs, use a secure credential store where supported, and avoid exposing credentials or account details. CLI availability, API permissions and flags can vary by version.

## Practice

Offline map these pairs: GitHub repository ↔ GitLab project (contains repository); organization/team ↔ group/subgroup (different permission models); pull request ↔ merge request; GitHub Actions workflow ↔ GitLab CI/CD pipeline; branch protection/ruleset ↔ protected branch/branch rule; `gh` ↔ `glab`. Both use native Git for commits, branches, tags and clones. Choose Git for inspecting history, GitLab for listing MRs, and the appropriate hosting platform for team policy. Optional: use an existing authorized CLI in an owned sandbox, verify `git remote -v` locally without sharing its output and inspect `glab --help`; run read-only list commands only if the correct host/project and authentication are confirmed. No login, installation or hosted operation is required.

## Common mistakes and safety

Do not blindly translate CLI commands or promise feature parity. Free tiers allow basic collaboration, but approval enforcement, quotas and advanced governance differ by offering, plan, version and configuration. If a query fails, check help, host and access before retrying; do not broaden credentials or use a write command as a workaround.

## Exercise and self-check

Which tool lists hosted MRs: `git log` or `glab mr list`? `glab mr list`. Pass if all six mappings are explained as analogies, not exact equivalences, and no paid or authenticated activity is necessary.

## Official sources

- <https://docs.gitlab.com/cli/>
- <https://docs.gitlab.com/cli/authentication/>
- <https://docs.gitlab.com/cli/mr/list/>
- <https://docs.gitlab.com/cli/issue/list/>
- <https://docs.gitlab.com/cli/release/list/>
- <https://docs.github.com/en/github-cli/github-cli/about-github-cli>
