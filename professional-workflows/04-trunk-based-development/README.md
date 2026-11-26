# Trunk-Based Development

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../03-github-flow/README.md) · [Index](../README.md) · [Next](../05-workflow-trade-offs/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 40 min

**Prerequisites:** [CI/CD](../../ci-cd/README.md) · [GitHub Flow](../03-github-flow/README.md)

**Objective:** Plan safe frequent integration.

## What and why

Trunk is the shared integration line, often main. Trunk-based development integrates small batches frequently, often daily or more, with very short-lived branches or direct integration where policy permits. It does not require unreviewed direct pushes. Automated feedback, reliable tests, small changes and fast review keep trunk healthy. A feature flag separates merging incomplete but safe code from exposing it to users; it must have a default, owner and removal plan. A flag is not an authorization mechanism. Branch-by-abstraction introduces a stable interface so old and new behavior can coexist during a transition. Neither technique justifies integrating broken work.

```text
small change -> fast review + CI -> trunk -> next small change
```

## Practice

A new catalog search takes five days. Split into a compatible interface, hidden implementation, tests, enablement decision and flag removal. Each change is small, reviewed and passes CI; old search remains usable until activation. Identify which steps alter Git history and which change runtime configuration. Draw a short-lived branch merging back to trunk every day.

## Risks and recovery

Do not use flags to hide insecure or untested behavior. If trunk fails, stop integration/promotion and prioritize restoring it with an authorized fix or revert. No direct main push is permitted in this guide. Frequent merge is not necessarily frequent deployment.

## Exercise and self-check

Prefer small safe increments, short review cycles and testable flag states. Trunk integration and flag activation are separate decisions.

## Quick reference

trunk / short-lived branch / feature flag

## Sources

- <https://dora.dev/capabilities/trunk-based-development/>
- <https://git-scm.com/docs/gitworkflows>
- <https://www.atlassian.com/git/tutorials/comparing-workflows>
