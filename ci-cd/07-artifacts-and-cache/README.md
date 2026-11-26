# Artifacts and cache

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../06-jobs-steps-stages-and-dependencies/README.md) · [Index](../README.md) · [Next](../08-environments-variables-and-secrets/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 30 min

**Prerequisites:** [GitHub](../../github/README.md) · [GitLab](../../gitlab/README.md) · [Jobs, steps, stages and dependencies](../06-jobs-steps-stages-and-dependencies/README.md)

**Objective:** Select an artifact or cache based on purpose, lifetime and trust.

## What and why

An artifact is a retained job output, such as a test report or package, associated with a run and retention policy. A cache is an optimization that may reuse data such as downloaded dependencies between jobs or runs; it can miss, expire or contain stale data. Do not make correctness depend on a cache hit. GitHub offers artifact upload/download actions and dependency caching; GitLab uses `artifacts` and `cache` configuration. GitLab jobs may download previous-stage artifacts by default; `needs` or `dependencies` changes selection. In both platforms, permissions, retention and storage limits vary. A dependency cache key can incorporate OS, tool version and lockfile digest; a release artifact should be associated with the exact reviewed revision and checked for integrity.

## Practice

Offline: classify a test report, a final package and downloaded dependencies. Sketch a cache key such as `linux-tool-v1-lockhash` (fictional placeholder) and a manifest recording the package revision and checksum. In a professional pipeline, validate that a cold cache still works and that the downloaded artifact belongs to the intended run.

## Common mistakes and safety

Never cache credentials or publish sensitive logs. Treat outputs from untrusted jobs as untrusted inputs; do not execute them in privileged jobs. If cache is corrupted, invalidate it according to project policy and rebuild from verified dependencies. If artifact is missing, reproduce from the reviewed revision instead of selecting an unrelated artifact.

## Exercise and self-check

Report and package are artifacts; downloaded dependencies are cache candidates. Pass if you can explain cache miss, retention, provenance and trust.

## Quick reference

artifact / cache / retention

## Official sources

- <https://docs.github.com/en/actions/concepts/workflows-and-actions/workflow-artifacts>
- <https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching>
- <https://docs.gitlab.com/ci/jobs/job_artifacts/>
- <https://docs.gitlab.com/ci/caching/>

---

<!-- navigation-footer -->
[Previous](../06-jobs-steps-stages-and-dependencies/README.md) · [Index](../README.md) · [Next](../08-environments-variables-and-secrets/README.md)
<!-- /navigation-footer -->
