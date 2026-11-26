# Feature Branch Workflow

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
— · [Index](../README.md) · [Next](../02-git-flow/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 35 min

**Prerequisites:** [CI/CD](../../ci-cd/README.md)

**Objective:** Explain feature branch state and reviewed integration.

## What and why

A feature branch is a temporary line of work created from the intended integration base. Commits advance its ref without advancing main. A pull request (PR) or merge request (MR) is a hosting feature that proposes integration; Git itself knows refs and commits, not review approvals. Keep changes small, independently testable and linked to a requirement. Fetch and inspect the target before integration; update the branch according to team policy. A squash merge creates a new combined commit rather than preserving every branch commit; a normal merge can retain both histories. Choose the method intentionally.

```text
base main -> feature branch -> review -> authorized integration
```

## Practice

A fictional library catalog needs a readiness field and a separate spelling fix. Draw two branches from main, each with one purpose. For the readiness branch, predict `git switch -c feat/ready-catalog`, a commit, switching back to main and integration. Use the local laboratory in chapter 13 to observe these states; a hosted PR is optional.

## Risks and recovery

Avoid bundling unrelated changes or keeping a branch open for weeks without a reason. Inspect divergence and resolve conflicts on the owned branch; abort an unresolved merge rather than guessing. Do not force-push shared branches or bypass required review. Delete branches only after verifying integration and retention needs.

## Exercise and self-check

Two branches keep the fixes independent. Main stays unchanged until integration. State which ref moves and distinguish the proposed review from a Git commit.

## Quick reference

`git switch -c` / `git diff` / PR / MR

## Sources

- <https://git-scm.com/docs/gitworkflows>
- <https://git-scm.com/docs/git-branch>
- <https://git-scm.com/docs/git-merge>
