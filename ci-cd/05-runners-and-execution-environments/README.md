# Runners and execution environments

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../04-gitlab-ci-cd/README.md) · [Index](../README.md) · [Next](../06-jobs-steps-stages-and-dependencies/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 35 min

**Prerequisites:** [GitHub](../../github/README.md) · [GitLab](../../gitlab/README.md) · [GitLab CI/CD pipelines](../04-gitlab-ci-cd/README.md)

**Objective:** Choose a bounded execution environment and diagnose runner scheduling problems.

## What and why

A runner is an agent that executes jobs, not a branch or a repository. GitHub-hosted runners provide managed execution environments; self-hosted runners are controlled by the operator. GitLab runners use executors such as shell or Docker, and runner scope/tags affect job eligibility. A shell executor shares the host more directly; a container does not automatically provide a sufficient security boundary. Prefer disposable, isolated runners with least privilege and no access to sensitive internal networks for untrusted changes. OS, shell, architecture, tools, environment image and version influence results. A matrix expands combinations, such as Linux and Windows, into separate jobs. Jobs can run in different machines; do not assume files or process state are shared.

## Practice

Offline scenario: Linux passes, Windows fails because a shell-specific path is used, and a third job remains pending because no eligible runner exists. Identify separate fixes: portable paths or explicit shell, and scheduling/configuration diagnosis. Read the guide's [quality automation](../../docs/quality-automation.md) for a real two-OS example, without changing it.

## Common mistakes and safety

Never register a runner on a personal or company machine for this lesson, run privileged Docker or expose credentials. Hosted compute may have quotas and costs; no hosted execution is required. Check runner availability, labels/tags and limits; do not bypass isolation.

## Exercise and self-check

Pass if pending is not interpreted as a failed test, Windows failure is not ignored, and no sensitive shared runner is proposed.

## Quick reference

runner / executor / matrix

## Official sources

- <https://docs.github.com/en/actions/concepts/runners/github-hosted-runners>
- <https://docs.gitlab.com/runner/executors/>
- <https://docs.gitlab.com/ci/runners/>
