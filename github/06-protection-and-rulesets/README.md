# Branch protection, rulesets and quality gates

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../05-forks-and-open-source/README.md) · [Index](../README.md) · [Next](../07-tags-and-releases/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 40 min

**Prerequisites:** [Remotes](../../remote-repositories/README.md) · [History & recovery](../../history-and-recovery/README.md) · [Forks and open-source contributions](../05-forks-and-open-source/README.md)

**Objective:** Design a policy that protects shared branches without bypassing review.

## What and why

Branch protection and rulesets are server-side GitHub policy, not Git commands. Rulesets target refs and can layer with branch protection. Example policy for main: require PR, required checks with exact observed names, strict up-to-date where required, resolved conversations, linear history, blocked force pushes and deletion, restricted bypass, and suitable required reviews when independent reviewers exist. Linear history alone permits squash or rebase, not a normal merge commit; choose repository merge methods and rules together. An approval count must be realistic: authors cannot approve their own PR. Public repositories on GitHub Free support branch rulesets; private availability varies by plan and rule type. Never pay to complete this course. A green check is evidence for a specific commit, not a universal safety guarantee.

## Practice

Offline policy exercise: evaluate four fictional PRs. A: correct target, current head, checks pass, reviews satisfied, conversations resolved. B: same but a required check fails. C: same but unresolved review thread. D: same but base advanced and strict update required. Only A is eligible for human merge authorization; B fix check, C address feedback, D update safely and revalidate. Optional read-only: inspect visible repository rules and merge box in an accessible repo. No admin changes required. Before proposing rules in real work, inventory existing checks and merge methods, review permissions, evaluate impact in a sandbox and obtain explicit admin approval; this lesson does not execute settings changes.

## Common mistakes and safety

Do not add a required check that has never run, confuse skipped/neutral checks with meaningful test success, bypass enforcement or lock out maintainers. Read actual logs and review current head; if a rule blocks work, diagnose and request approved policy resolution rather than disabling it. Workflows and runner permissions are expanded in module 10.

## Exercise and self-check

Pass if only A is eligible, you can explain why squash does not bypass a PR requirement, and name an independent reviewer limitation for a solo project.

## Quick reference

- `ruleset`
- `required checks`
- `linear history`
- `bypass`

## Official sources

- <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches>
- <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets>
- <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets>

---

<!-- navigation-footer -->
[Previous](../05-forks-and-open-source/README.md) · [Index](../README.md) · [Next](../07-tags-and-releases/README.md)
<!-- /navigation-footer -->
