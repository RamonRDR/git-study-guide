# Merge requests, code review and forks

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../03-issues-labels-milestones-and-boards/README.md) · [Index](../README.md) · [Next](../05-protected-branches-and-merge-checks/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 45 min

**Prerequisites:** [GitHub](../../github/README.md) · [Remotes](../../remote-repositories/README.md)

**Objective:** Review a proposed change and choose same-project or fork collaboration safely.

## What and why

An MR is GitLab's hosted proposal to integrate a source branch into a target branch; GitHub calls the analogous feature a pull request (PR). Neither is a native Git object. An MR records description, diff, commits, discussions, reviewers, checks and merge state. In a shared project, contributors push feature branches where permitted; for outside contributions, a fork is a separate hosted project with its own permissions and a relationship to upstream. Clone is a local copy, not a fork. A fork MR can target upstream, but access, pipeline execution and collaboration permissions differ. Review the actual source/target project and branch, exact revision, diff, test evidence and unresolved discussions. A draft signals work not ready for integration. After a fix, verify the new revision before resolving a discussion; approvals alone do not prove tests or safety. Merge method changes history as taught in module 05.

## Practice

Offline simulate issue #12 and MR !7: `docs/setup` → `main`. Proposed diff adds instructions but omits a prerequisite. Write a review asking for that prerequisite and a testable check; simulate a corrected revision and re-review. For a real Git comparison, use the disposable two-clone lab in [module 06](../../remote-repositories/README.md); inspect `git status`, `git log --oneline main..HEAD` and `git diff main...HEAD` only after verifying the local base ref. These commands do not create an MR. Optional: inspect an existing public MR read-only; or create a draft in your own private sandbox after checking source, target and history. No merge or external contribution required.

## Common mistakes and safety

Never run an untrusted fork's pipeline with privileged credentials; a fork can change pipeline configuration. Verify license before reuse. If target or diff is wrong, stop, correct the proposal or close your own draft; do not force-push shared history. Respect project contribution policy.

## Exercise and self-check

Pass if you can distinguish clone, fork, branch and MR, name both refs and projects, explain why the correction requires fresh review and identify the missing prerequisite before recommending merge.

## Official sources

- <https://docs.gitlab.com/user/project/merge_requests/>
- <https://docs.gitlab.com/user/project/merge_requests/reviews/>
- <https://docs.gitlab.com/user/project/merge_requests/authorization_for_merge_requests/>
- <https://docs.gitlab.com/user/project/repository/forking_workflow/>
