# GitLab CI/CD pipelines

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../03-github-actions/README.md) · [Index](../README.md) · [Next](../05-runners-and-execution-environments/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 45 min

**Prerequisites:** [GitHub](../../github/README.md) · [GitLab](../../gitlab/README.md) · [GitHub Actions workflows](../03-github-actions/README.md)

**Objective:** Read a GitLab pipeline and map its concepts to GitHub Actions without conflating their syntax.

## What and why

GitLab normally reads `.gitlab-ci.yml` at the repository root. `workflow: rules` determines whether a pipeline is created; job `rules` can decide whether individual jobs are included. Stages order groups of jobs by default; a job has a `script` containing commands. The runner executor defines the actual environment. An `image` is used by supported container executors, not by every executor. The example requires a compatible isolated Linux container runner, with Alpine and its BusyBox shell tools. GitLab normally checks out the revision before script execution. The example deliberately uses a readable version tag; image tags are mutable, so a production policy should verify and pin a trusted digest instead. GitLab jobs receive automatic job credentials even without user-defined secrets; restrict job-token access and runner scope as applicable.

```yaml
workflow:
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
    - if: '$CI_PIPELINE_SOURCE == "push" && $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH'
stages:
  - test
quality:
  stage: test
  image: alpine:3.22
  timeout: 5m
  script:
    - test -s catalog.txt
    - grep -Fxq 'status: ready' catalog.txt
```

## Practice

Offline, trace an MR event, a push to the default branch and a push to another branch without an MR. The configuration creates pipelines for the first two, not the third. Compare the checks with chapter 03 and perform the same offline lab in chapter 10. Optional: CI Lint can validate configuration in an authorized disposable project without executing jobs; check permissions and available free quota before any hosted operation. No runner registration or paid usage is required.

## Common mistakes and safety

Do not run fork MR pipelines in a privileged parent project with secrets or protected resources. Review `.gitlab-ci.yml` changes, includes and token access. If no pipeline appears, inspect source, workflow rules and configuration validity before changing access or retrying.

## Exercise and self-check

Pass if you distinguish workflow rules, stages, jobs, scripts and runner executor; explain automatic job credentials and why the two platforms do not share interchangeable YAML.

## Quick reference

`workflow` / `rules` / `stages` / `script`

## Official sources

- <https://docs.gitlab.com/ci/yaml/>
- <https://docs.gitlab.com/ci/yaml/lint/>
- <https://docs.gitlab.com/ci/pipelines/merge_request_pipelines/>
- <https://docs.gitlab.com/ci/jobs/ci_job_token/>
