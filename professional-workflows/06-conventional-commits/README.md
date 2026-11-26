# Conventional Commits

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../05-workflow-trade-offs/README.md) · [Index](../README.md) · [Next](../07-semantic-versioning/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 30 min

**Prerequisites:** [CI/CD](../../ci-cd/README.md) · [Choosing a workflow](../05-workflow-trade-offs/README.md)

**Objective:** Write meaningful commit messages and identify breaking changes.

## What and why

Conventional Commits is a convention for commit messages, not a Git syntax requirement. The header is `type(scope): description`; scope is optional. `feat` signals a feature, `fix` a bug correction, and `!` before the colon or a `BREAKING CHANGE:` footer signals incompatibility. A body can explain intent after a blank line; footers can record metadata. Other types such as docs, test and chore are team conventions and do not implicitly change SemVer unless a breaking change is declared. Release tooling may interpret messages, but nothing in Git automatically bumps versions. A squash commit title and body must preserve relevant meaning of the combined change.

## Practice

Classify these original messages: `fix(catalog): preserve empty results`, `feat(catalog): add readiness field`, `docs: explain catalog filters`, `feat(api)!: replace item identifier`. Write a body for the last change describing the migration, and choose a squash title for a PR adding readiness plus its tests.

## Risks and recovery

Do not label incompatible changes as fixes to avoid a major release. Do not rewrite published/shared commit history simply to tidy a message; clarify in follow-up metadata or use approved procedures. Never include credentials or private issue content in commit messages.

## Exercise and self-check

Fix, feature, documentation, breaking feature respectively. A suitable squash title is `feat(catalog): add readiness field`; preserve breaking markers when applicable.

## Quick reference

`type(scope): description` / `!` / `BREAKING CHANGE:`

## Sources

- <https://www.conventionalcommits.org/en/v1.0.0/>
- <https://git-scm.com/docs/git-commit>

---

<!-- navigation-footer -->
[Previous](../05-workflow-trade-offs/README.md) · [Index](../README.md) · [Next](../07-semantic-versioning/README.md)
<!-- /navigation-footer -->
