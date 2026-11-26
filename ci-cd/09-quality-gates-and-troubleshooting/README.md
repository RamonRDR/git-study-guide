# Quality gates and troubleshooting

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../08-environments-variables-and-secrets/README.md) · [Index](../README.md) · [Next](../10-integrated-quality-pipeline-lab/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 35 min

**Prerequisites:** [GitHub](../../github/README.md) · [GitLab](../../gitlab/README.md) · [Environments, variables and secrets](../08-environments-variables-and-secrets/README.md)

**Objective:** Decide whether a revision is eligible for merge from evidence, not a green icon alone.

## What and why

A quality gate is a policy condition that must be satisfied before integration or promotion. Examples: required lint (static checks), tests, code review, security checks and authorized approval. GitHub rulesets can require named checks; GitLab merge checks can require a successful pipeline and resolved discussions where configured. Capabilities vary by plan and configuration. A workflow may be missing, queued, pending, running, failed, canceled, skipped or successful. Platform policies may treat some skipped/neutral results as satisfying checks, but they do not prove tests ran. Distinguish a configuration error, infrastructure failure and failing assertion. Verify exact head/base or merge result, logs, required job names and policy; do not infer from an earlier run. A timeout is not a pass.

## Practice

Offline: revision A passed; B changes validation configuration; B Linux passes but Windows fails. Write a pre-merge checklist: exact revision, expected jobs, logs, findings, discussion resolution, current base, authorization. Decide not to merge B, inspect Windows failure, correct it, re-review the new revision and rerun both jobs. Optional: inspect public CI logs read-only with no account where available.

## Common mistakes and safety

Do not disable gates, suppress failures or retry indefinitely to hide nondeterminism. Redact sensitive diagnostics; report reproducibility limits and escalate infrastructure issues. Correct only the root cause and preserve review evidence.

## Exercise and self-check

B is blocked; A is not evidence for B. Pass if your checklist includes both platforms, exact revision, meaningful results and human authorization.

## Quick reference

required check / revision / log

## Official sources

- <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets>
- <https://docs.gitlab.com/user/project/merge_requests/auto_merge/>
- <https://docs.gitlab.com/ci/pipelines/>
