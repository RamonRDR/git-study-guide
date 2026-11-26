# Release management

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../11-ai-assisted-development/README.md) · [Index](../README.md) · [Next](../13-integrated-professional-workflow-lab/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 40 min

**Prerequisites:** [CI/CD](../../ci-cd/README.md) · [AI-assisted professional work](../11-ai-assisted-development/README.md)

**Objective:** Prepare a release with version, revision, evidence and separate publication decision.

## What and why

A release identifies a tested revision and communicates what consumers can use. A Git tag is a ref, often annotated with a message; a hosted release can attach notes and assets to a tag. Deployment is the separate act of promoting an artifact into an environment. Start from approved integrated revision, decide version from public contract, record changes/migration and known limitations, verify checks and artifact provenance, create an annotated tag at the chosen commit and obtain release authorization before publishing. For local inspection use `git show v1.1.0` and `git rev-parse 'v1.1.0^{commit}'` after chapter 13. Signing and immutable release controls may be useful where configured; an annotated tag is not automatically signed or immutable.

```text
tested commit -> annotated tag -> authorized publication -> deployment decision
```

## Practice

Assume catalog 1.0.0 has a documented public format and readiness is a new backward-compatible field in this hypothetical scenario. Draft release notes for 1.1.0: feature, expected behavior, verification, migration (none required for compatible consumers), known limits (local lab only, no hosted run) and artifact/revision identifier. Draw the gate between tag, publication and deployment. Do not publish anything for this exercise.

## Risks and recovery

Do not retag a published version or publish from an unreviewed head. If a bad release escapes, communicate it, stop promotion and follow rollback/forward-fix policy; data migration may prevent easy rollback. Release and deployment permissions are separate from merge permission. No actual external artifact or deployment is required.

## Exercise and self-check

1.1.0 is justified only by the stated compatible contract. The tag targets the tested revision; release notes disclose actual checks and limits; production remains unchanged.

## Quick reference

tag / release notes / artifact / deployment

## Sources

- <https://semver.org/spec/v2.0.0.html>
- <https://git-scm.com/docs/git-tag>
- <https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository>
