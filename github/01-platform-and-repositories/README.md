# GitHub, repositories and visibility

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
— · [Index](../README.md) · [Next](../02-permissions-and-authentication/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 25 min

**Prerequisites:** [Remotes](../../remote-repositories/README.md) · [History & recovery](../../history-and-recovery/README.md)

**Objective:** Distinguish local Git data from hosted services and choose safe visibility.

## What and why

Git works without GitHub. GitHub hosts Git repositories and adds web browsing, identities, access controls, issues and pull requests. A clone is a local Git repository; publishing sends selected Git objects and refs to a server. Public means anyone can read public content, not that anyone can push. Private limits access but is not a place for secrets. Internal visibility is an organization/enterprise feature, not required here. A public repository is not automatically open source: the license determines reuse rights. README explains the project; LICENSE grants rights; CONTRIBUTING describes contributions; SECURITY gives a private reporting path where available.

## Practice

Offline: sketch local clone -> remote Git repository -> GitHub web features. Classify commit, branch, issue, pull request and label by layer. Optional: visit a public repository in a browser without posting. Inspect default branch, files, history, license and visibility. To practice creation, use a new personal disposable repository named study-sandbox, private by default, with fictional README only. Never use employer or guide repositories. Before any publication inspect all committed history, identity and files; no visibility change is necessary. A hosted sandbox created with an initial README has its own first commit; clone it instead of combining unrelated histories.

## Common mistakes and safety

Changing public to private cannot recall existing clones or all copies; making private public exposes history. Stop if any content is confidential; do not experiment with visibility on real repositories. Use an independent backup before authorized deletion; cleanup can simply mean leaving an empty private sandbox unused.

## Exercise and self-check

Can a visitor push to a public repo by default? No. Pass if you distinguish read visibility, write permission and licensing, and identify three native Git concepts and two hosted features.

## Quick reference

- `Git`
- `GitHub`
- `README`
- `LICENSE`

## Official sources

- <https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories>
- <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility>
