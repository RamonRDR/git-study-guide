# Code review and merge readiness

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../07-semantic-versioning/README.md) · [Index](../README.md) · [Next](../09-spec-driven-development/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 40 min

**Prerequisites:** [CI/CD](../../ci-cd/README.md) · [Semantic Versioning](../07-semantic-versioning/README.md)

**Objective:** Review intent, behavior, risk and exact revision evidence.

## What and why

Code review evaluates a proposed change against intent, behavior, maintainability, security and tests. A useful finding states location, observed problem, impact and a suggested direction; distinguish blocking defects from optional suggestions. Review a focused diff, not just a green icon. Compare head to the intended base and verify actual logs and test scope. GitHub and GitLab provide review discussions and approvals; enforcement, dismissal of stale approvals and required reviewers depend on repository configuration. An author addresses findings and records evidence; a reviewer verifies the correction before closing relevant discussions. Merge authorization remains separate from a successful automated review.

## Practice

A PR claims to add readiness, but changes `catalog.txt` from `status: draft` to `status: redy`. The test checks only file existence. Write a blocking comment asking for the exact expected field and meaningful failing/passing tests; write an optional naming suggestion separately. Author corrects the value and test. Record new revision, CI on expected environments, resolution and human approval; use chapter 13 for local diff practice.

## Risks and recovery

Do not approve based on politeness, title, AI output or an earlier SHA. Never silence failures or resolve a thread merely to unblock merge. On missed regression, record a corrective PR, rerun checks and improve test coverage instead of blaming people.

## Exercise and self-check

Block merge because behavior differs from requirement and the check cannot detect it. Retest exact corrected revision; independent human authorization is still necessary under guide policy.

## Quick reference

diff / head SHA / review / approval / CI

## Sources

- <https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/reviewing-proposed-changes-in-a-pull-request>
- <https://docs.gitlab.com/user/project/merge_requests/reviews/>

---

<!-- navigation-footer -->
[Previous](../07-semantic-versioning/README.md) · [Index](../README.md) · [Next](../09-spec-driven-development/README.md)
<!-- /navigation-footer -->
