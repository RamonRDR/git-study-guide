# Pull requests and code review

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../03-issues-and-planning/README.md) · [Index](../README.md) · [Next](../05-forks-and-open-source/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 45 min

**Prerequisites:** [Remotes](../../remote-repositories/README.md) · [History & recovery](../../history-and-recovery/README.md) · [Issues, labels, milestones and projects](../03-issues-and-planning/README.md)

**Objective:** Follow a reviewable change from branch to authorized merge.

## What and why

A pull request (PR) proposes integration from head/source to base/target; opening it does not merge Git history. A draft signals work not ready for final review. Files changed shows the proposed diff, Commits shows commits, Checks reports automated runs. Review can comment, approve or request changes; comments alone do not approve. New commits change the reviewed head and may invalidate approval under policy. A closing keyword such as Closes #1 in a PR description can close an issue when merged into the default branch under GitHub's linking rules. A merge commit preserves both parents, squash creates one combined commit, rebase-and-merge reapplies commits without a merge commit; available methods depend on settings. CI success does not guarantee correctness.

## Practice

Offline: draw issue -> feature branch -> commit -> push -> PR -> review/checks -> authorized merge -> verify base. Draft a PR description with summary, scope, tests actually run, limitations and issue link. A fictional reviewer finds missing setup instructions; revise the patch and request review of the new head. Optional: in your own private sandbox, use web branch/file editing to create feat/setup-note from main, add fictional prerequisites, commit to that branch only, open a PR to main, inspect diff and issue link (substitute actual issue number). A single-person exercise may self-inspect but cannot count as independent approval; if required approval/checks cannot be satisfied, leave PR open or close it without merging. If all applicable policies and owner authorization are satisfied, choose an allowed merge method, verify main and clean up only the merged feature branch. Never disable rules to complete the lab.

## Common mistakes and safety

Check source/target and latest head, not only green icons. Do not mark conversations resolved without addressing them. If a merged change is faulty, propose a reviewed corrective commit or revert; do not reset shared main. Treat AI feedback as suggestions, not human approval.

## Exercise and self-check

A new commit appears after approval: what next? Recheck the new diff, rerun applicable checks and obtain required review. Pass if you can distinguish base, head, checks, approval and merge.

## Quick reference

- `base`
- `head`
- `review`
- `checks`
- `Closes #1`

## Official sources

- <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests>
- <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews>
- <https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue>
- <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/about-merge-methods-on-github>
