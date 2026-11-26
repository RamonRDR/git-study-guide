# Introduction to pipelines and runners

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../05-protected-branches-and-merge-checks/README.md) · [Index](../README.md) · [Next](../07-tags-and-releases/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 30 min

**Prerequisites:** [GitHub](../../github/README.md) · [Remotes](../../remote-repositories/README.md)

**Objective:** Explain how hosted automation executes and how to interpret its status without running a pipeline.

## What and why

A pipeline coordinates automated jobs for a revision and event; a job is an individual unit of work. A runner is an execution agent that picks up eligible jobs, prepares an environment, runs commands and returns results. GitLab normally reads `.gitlab-ci.yml` from the project; configuration and event determine whether a pipeline exists. GitHub Actions uses workflows commonly under `.github/workflows/`; both systems automate work, but syntax, events, permissions and runner models differ. A runner may be scoped to a project, group or instance, and hosted or self-managed depending on offering. Runner availability, permissions and tags can affect scheduling. Hosted runners on GitLab.com consume quota according to usage and runner type; do not assume unlimited free compute. Full YAML, artifacts, cache and deployment are deferred to module 10.

## Practice

Draw revision A → pipeline → job `validate` → runner → job result. Scenario: A succeeds; revision B arrives and its job is pending. Record why A cannot establish B's status. A failed job requires log inspection; pending may mean waiting for an eligible runner. Optional: inspect an existing public pipeline and its revision read-only when visible; do not trigger, retry or register runners.

## Common mistakes and safety

Do not execute untrusted code with secrets or privileged runners. A skipped, missing or pending check is not evidence of successful execution. Inspect revision, event, status and logs; do not bypass checks or buy compute for practice.

## Exercise and self-check

Pass if you distinguish pipeline, job and runner, identify B as not yet validated and explain why a quota or scheduling problem is not a passing test.

## Official sources

- <https://docs.gitlab.com/runner/>
- <https://docs.gitlab.com/ci/runners/>
- <https://docs.gitlab.com/ci/pipelines/compute_minutes/>
- <https://docs.gitlab.com/ci/pipelines/settings/>
