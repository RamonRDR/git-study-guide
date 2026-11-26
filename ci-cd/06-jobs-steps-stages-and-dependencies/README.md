# Jobs, steps, stages and dependencies

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../05-runners-and-execution-environments/README.md) · [Index](../README.md) · [Next](../07-artifacts-and-cache/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 35 min

**Prerequisites:** [GitHub](../../github/README.md) · [GitLab](../../gitlab/README.md) · [Runners and execution environments](../05-runners-and-execution-environments/README.md)

**Objective:** Model execution order, failure propagation and parallelism.

## What and why

In GitHub Actions, steps within a job are ordered; independent jobs can run concurrently and `needs` declares job dependencies. In GitLab, stages impose default ordering and `needs` can describe a more direct dependency graph, allowing jobs to start before an entire earlier stage finishes. A directed acyclic graph (DAG) is a graph of dependencies without cycles. Consider `lint` and `test` independent; `package` needs both. Neither platform guarantees job order merely from textual order. A failed required dependency normally prevents downstream success-dependent work; explicit failure/condition options can change that behavior. Avoid `continue-on-error` or `allow_failure` for required checks. A matrix is expansion, not a dependency declaration.

```text
lint ----> package
           ^
           |
test ------+
```

## Practice

Offline, draw the graph below. Compute the allowed next jobs when lint passes but test fails; then when both pass. Sketch a GitHub job with `needs: [lint, test]` and a GitLab job with the same dependency key in the job mapping. These are fragments for reasoning, not complete configurations.

## Common mistakes and safety

Do not remove a required dependency to make a pipeline green. Check whether upstream files must be explicitly transferred. Diagnose skipped jobs and conditions before changing gates; no execution is needed.

## Exercise and self-check

Package is blocked when test fails and eligible when both pass, subject to runner availability and conditions. Pass if you identify both edges, no cycle, and parallel jobs.

## Quick reference

`needs` / DAG / stage

## Official sources

- <https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax>
- <https://docs.gitlab.com/ci/yaml/needs/>

---

<!-- navigation-footer -->
[Previous](../05-runners-and-execution-environments/README.md) · [Index](../README.md) · [Next](../07-artifacts-and-cache/README.md)
<!-- /navigation-footer -->
