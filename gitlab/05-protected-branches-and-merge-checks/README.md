# Protected branches, approvals and merge checks

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../04-merge-requests-review-and-forks/README.md) · [Index](../README.md) · [Next](../06-pipelines-and-runners/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 35 min

**Prerequisites:** [GitHub](../../github/README.md) · [Remotes](../../remote-repositories/README.md)

**Objective:** Design a protected default-branch policy and distinguish enforced gates from conventions.

## What and why

GitLab protected branches use branch rules to restrict operations on selected refs. `Allowed to merge` controls MR merging; `Allowed to push and merge` also grants direct push access. To require MRs, explicitly select No one for push and merge and grant merge rights only to appropriate roles; an unset rule is not the same as explicit denial. Inspect overlapping wildcard rules and inherited rules; effective access may be more permissive than a single rule suggests. Disable force push unless explicitly justified. Merge checks can require successful pipelines and resolved discussions when configured. GitLab Free supports basic protection and voluntary approvals, but required approval rules and Code Owner approval enforcement depend on Premium/Ultimate and applicable settings. Do not represent an informal approval checklist as a technically enforced rule. Branch rules and GitHub rulesets are analogous in intent, not equivalent feature-for-feature. A passing check is evidence for a revision, not universal correctness.

## Practice

Offline design a policy: developers push feature branches, no direct push to `main`, maintainers merge only after review, successful required pipeline and resolved discussions. Mark each control enforced, manual, or unavailable until verified for the actual tier. In the scenario a maintainer finds a failing pipeline and one open discussion: decline merge and request correction. Optional: inspect rules in an owned private sandbox without modifying them; identify plan/version and actual settings.

## Common mistakes and safety

Never weaken protection to pass a merge. If a merge is blocked, read the exact check, resolve its cause, rerun checks on the new revision and seek authorization. Do not assume an approval or a successful unrelated pipeline overrides required gates.

## Exercise and self-check

Does Maintainer in Allowed to push and merge prevent direct pushes? No. Pass if direct push denial is explicit and required approval enforcement is distinguished from voluntary review.

## Official sources

- <https://docs.gitlab.com/user/project/repository/branches/protected/>
- <https://docs.gitlab.com/user/project/repository/branches/branch_rules/>
- <https://docs.gitlab.com/user/project/merge_requests/approvals/>
- <https://docs.gitlab.com/user/project/merge_requests/approvals/rules/>
- <https://docs.gitlab.com/user/project/merge_requests/auto_merge/>
