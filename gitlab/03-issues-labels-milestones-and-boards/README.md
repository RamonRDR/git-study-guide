# Issues, labels, milestones and boards

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../02-visibility-permissions-and-authentication/README.md) · [Index](../README.md) · [Next](../04-merge-requests-review-and-forks/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 25 min

**Prerequisites:** [GitHub](../../github/README.md) · [Remotes](../../remote-repositories/README.md)

**Objective:** Turn a problem into traceable work with acceptance criteria and progress visibility.

## What and why

An issue records a problem or task, not a Git commit. A label categorizes work, a milestone groups work toward a target, and an issue board displays work in lists. A board may use labels or other filters; dragging a card can change its metadata according to board configuration. Projects and groups can share planning context; supported work item types and advanced boards vary by tier and version. An assignee owns execution; a reviewer checks the proposed change. Link the MR to the issue to preserve the decision trail. A closing keyword such as `Closes #12` can close a referenced issue when the relevant MR is merged into the default branch under applicable project settings. Do not use it for unrelated work.

## Practice

On paper create issue #12: the fictional catalog lacks installation instructions. State expected result (a beginner can locate setup instructions), label `documentation`, milestone `v1`, assignee and reviewer. Move a card through Open, In progress and Closed, recording what evidence would justify closure. Optional: reproduce only in a personal disposable private project; inspect the board before and after, close only your own issue if desired.

## Common mistakes and safety

Do not post real customer data, internal logs or secrets. A closed issue or moved card is not proof that code works. Reopen an incorrectly closed issue and record the reason; avoid altering others' milestones.

## Exercise and self-check

Pass if the issue has a measurable outcome, label and milestone serve different purposes, and closure depends on verified evidence rather than a board movement.

## Official sources

- <https://docs.gitlab.com/user/work_items/>
- <https://docs.gitlab.com/user/project/labels/>
- <https://docs.gitlab.com/user/project/milestones/>
- <https://docs.gitlab.com/user/project/issue_board/>
