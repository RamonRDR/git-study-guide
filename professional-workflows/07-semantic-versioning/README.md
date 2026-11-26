# Semantic Versioning

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../06-conventional-commits/README.md) · [Index](../README.md) · [Next](../08-code-review/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 35 min

**Prerequisites:** [CI/CD](../../ci-cd/README.md) · [Conventional Commits](../06-conventional-commits/README.md)

**Objective:** Choose a compatible version and interpret precedence.

## What and why

SemVer 2.0.0 describes versions relative to a declared public API (a contract consumers rely on, not necessarily an HTTP API). For stable versions, increment MAJOR for incompatible API changes, MINOR for backward-compatible functionality and PATCH for backward-compatible bug fixes; reset lower components when a higher component increments. Major zero is initial development with unstable API. A pre-release such as `2.0.0-rc.1` has lower precedence than the corresponding normal version; build metadata after `+` does not affect precedence. Published version contents must not be modified. A Git tag such as `v1.4.2` can name the commit for SemVer `1.4.2`; the prefix is a tag convention, not part of the SemVer version string.

## Practice

From catalog API 1.4.2, choose the next version for each independent scenario: correct a typo without changing API; add an optional backward-compatible field; remove a required response field. Compare `2.0.0-rc.1` to `2.0.0`, and `1.4.2+build.7` to `1.4.2+build.8`. Declare the API contract and identify actual consumer impact before deciding.

## Risks and recovery

A message type is evidence of intent, not proof of compatibility. Never silently replace published contents or move a release tag. If a release is wrong, follow remediation policy and publish a new corrected version; communicate affected consumers.

## Exercise and self-check

Independent results: 1.4.3, 1.5.0, 2.0.0. The release candidate precedes the normal version; build metadata versions have equal precedence.

## Quick reference

MAJOR.MINOR.PATCH / pre-release / build metadata

## Sources

- <https://semver.org/spec/v2.0.0.html>
- <https://www.conventionalcommits.org/en/v1.0.0/>
- <https://git-scm.com/docs/git-tag>
