# GitHub Flow

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../02-git-flow/README.md) · [Index](../README.md) · [Next](../04-trunk-based-development/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 35 min

**Prerequisites:** [CI/CD](../../ci-cd/README.md) · [Git Flow](../02-git-flow/README.md)

**Objective:** Describe the branch-to-PR workflow and review boundary.

## What and why

GitHub Flow is a lightweight collaboration convention: create a branch, make commits, open a PR, discuss and review, integrate when approved and remove the branch after verification. It favors a default branch ready for integration, with small changes and continuous feedback. Branch protection and CI are hosting policies that can enforce parts of the flow; GitHub Flow does not mandate a particular merge method, automated deployment, paid plan or bypass of approval. A draft PR signals work in progress. It may overlap with trunk-based development when branch lifetimes are very short.

```text
branch -> commits -> PR -> review + CI -> authorized merge
```

## Practice

Offline: role-play author and reviewer of a catalog search-label correction. Write the PR title, problem, scope, checks and limitations. Reviewer requests a spelling correction; author supplies a new revision and evidence. Draw the route from feature branch to reviewed main. Optional: perform it in a disposable owned repository with no paid services; no account is required for the exercise.

## Risks and recovery

A PR opening is not approval. Do not merge an outdated or failing revision; confirm current base, reviewed head and actual checks. Do not assume a branch deletion deploys the change. For a regression follow the agreed revert and release process.

## Exercise and self-check

A new revision must be reviewed and validated according to policy; the PR can close only after authorized integration or abandonment.

## Quick reference

branch / PR / review / merge

## Sources

- <https://docs.github.com/en/get-started/using-github/github-flow>
- <https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/reviewing-proposed-changes-in-a-pull-request>
