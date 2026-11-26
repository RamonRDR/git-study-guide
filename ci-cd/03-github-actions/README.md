# GitHub Actions workflows

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../02-yaml-fundamentals/README.md) · [Index](../README.md) · [Next](../04-gitlab-ci-cd/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 45 min

**Prerequisites:** [GitHub](../../github/README.md) · [GitLab](../../gitlab/README.md) · [YAML and configuration reading](../02-yaml-fundamentals/README.md)

**Objective:** Explain events, workflow, jobs, steps and minimal permissions using an inspection-only example.

## What and why

GitHub discovers workflow files under `.github/workflows/`. An event selects a workflow run; a job runs on a runner, and its steps run in sequence. `uses` invokes an action; `run` invokes a shell command. For pull_request, the default checkout typically tests the generated merge ref; for push it tests the pushed revision. Always inspect actual checkout and event. `permissions: contents: read` minimizes the default token grant; disabling persisted checkout credentials reduces later exposure. Pin third-party and first-party actions to verified full commit SHAs, review updates and never treat pinning as a security guarantee.

The example below is a complete teaching configuration for a fictional catalog; the checkout SHA is taken from the reviewed guide workflow, not an invented version. Verify the action revision before using it elsewhere. It uses no deployment or user secrets.

```yaml
name: Sandbox quality
on:
  pull_request:
    branches: [main]
  push:
    branches: [main]
permissions:
  contents: read
jobs:
  quality:
    runs-on: ubuntu-latest
    timeout-minutes: 5
    steps:
      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1
        with:
          persist-credentials: false
      - name: Check catalog
        shell: bash
        run: |
          test -s catalog.txt
          grep -Fxq 'status: ready' catalog.txt
```

## Practice

Read the YAML without installing it. In the offline lab in chapter 10, execute the two checks against your own temporary catalog file. Predict success for the exact ready line and failure for an empty or wrong file. Optional hosted use: only in an owned disposable sandbox after reviewing code, runner availability, quotas and permissions; do not use the guide or enable paid usage. No hosted run is necessary.

## Common mistakes and safety

Never execute untrusted PR code in a privileged `pull_request_target` workflow. Do not interpolate untrusted event text into shell scripts. A failed step requires inspecting logs; correct the source and rerun checks on the new revision, not an unrelated successful run.

## Exercise and self-check

Pass if you name both events, identify runner/job/steps, explain the token permissions and predict both check outcomes.

## Quick reference

`on` / `jobs` / `steps` / `permissions`

## Official sources

- <https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax>
- <https://docs.github.com/en/actions/reference/security/secure-use>
- <https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows>

---

<!-- navigation-footer -->
[Previous](../02-yaml-fundamentals/README.md) · [Index](../README.md) · [Next](../04-gitlab-ci-cd/README.md)
<!-- /navigation-footer -->
