# Choosing a workflow

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../04-trunk-based-development/README.md) · [Index](../README.md) · [Next](../06-conventional-commits/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 35 min

**Prerequisites:** [CI/CD](../../ci-cd/README.md) · [Trunk-Based Development](../04-trunk-based-development/README.md)

**Objective:** Choose a model using concrete trade-offs.

## What and why

There is no universal branching model. Compare branch lifetime, integration frequency, supported release lines, release approval, CI reliability, review latency and recovery requirements. Feature branching is a broad technique; GitHub Flow adds a lightweight hosted review convention; trunk-based emphasizes frequent integration; Git Flow defines longer-lived release and development lines. These categories overlap. A team may combine protected trunk, short feature branches and maintenance branches for supported releases. More branches do not automatically provide stronger governance; explicit controls and evidence matter.

## Practice

Compare three fictional teams: a documentation guide with one main, PR and two required checks; a desktop product supporting two older releases; an online catalog with many daily safe changes and fast CI. Write a decision record with context, chosen model, rejected alternative, merge method, release policy and review triggers. Evaluate actual constraints, not popularity.

## Risks and recovery

Do not change a production branch model without a migration plan, permissions review, team agreement and verified release mappings. Avoid claiming that a model eliminates merge conflicts. Revisit the decision when constraints change.

## Exercise and self-check

Reasonable choices: protected feature/GitHub Flow for documentation; trunk with maintenance branches or Git Flow if release coordination warrants it for desktop; protected trunk-based for online catalog. Alternatives are valid when justified with constraints.

## Quick reference

branch lifetime / CI / release cadence / support

## Sources

- <https://www.atlassian.com/git/tutorials/comparing-workflows>
- <https://dora.dev/capabilities/trunk-based-development/>
- <https://nvie.com/posts/a-successful-git-branching-model/>
