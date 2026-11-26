# Integration, delivery and deployment

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
— · [Index](../README.md) · [Next](../02-yaml-fundamentals/README.md)
<!-- /navigation -->

**Level:** beginner · **Estimated time:** 30 min

**Prerequisites:** [GitHub](../../github/README.md) · [GitLab](../../gitlab/README.md)

**Objective:** Explain the three practices and choose a safe promotion boundary.

## What and why

Continuous integration (CI) means integrating small changes frequently and obtaining fast automated feedback. Continuous delivery keeps a tested revision ready for release; production promotion can require a deliberate decision. Continuous deployment automatically promotes changes that satisfy the configured gates to production. CD can refer to either delivery or deployment; name which you mean. A build creates a deliverable, a test checks behavior, and deployment changes a running environment. Passing CI does not prove a deployment occurred or that the software is safe for every user.

Accessible flow:

```text
change -> CI checks -> release candidate -> promotion -> production
              | failure: stop and correct
```

In delivery, promotion may be manual; in deployment it is automatic after gates. A release decision may also be separate from deployment (for example, a feature toggle).

## Practice

Offline: a fictional catalog has three revisions. A fails tests; B passes but awaits approval; C is deployed after checks. Classify each and draw the gate between B and production. In a professional team, record the exact revision, test evidence, approval and rollback plan before promotion.

## Common mistakes and safety

Do not deploy from a failing or unknown revision. Rollback may require compatible data migrations; never promise a simple Git revert restores a live system. Stop promotion and follow the incident plan.

## Exercise and self-check

A is blocked; B illustrates delivery readiness; C illustrates deployment, automatic only if policy promotes it automatically. Pass if you explain all three concepts without confusing merge, release and deployment.

## Quick reference

CI / delivery / deployment

## Official sources

- <https://docs.gitlab.com/ci/introduction/>
- <https://docs.github.com/en/actions/get-started/understand-github-actions>
