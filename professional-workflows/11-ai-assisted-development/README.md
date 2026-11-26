# AI-assisted professional work

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../10-test-driven-development/README.md) · [Index](../README.md) · [Next](../12-release-management/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 35 min

**Prerequisites:** [CI/CD](../../ci-cd/README.md) · [Test-Driven Development (TDD)](../10-test-driven-development/README.md)

**Objective:** Use assistance without delegating verification or approval.

## What and why

AI can propose explanations, implementation plans, code, tests or review comments, but cannot establish correctness merely by producing confident text. Assign roles: human defines scope, verifies authorization and makes final decisions; tool proposes or executes only within allowed scope; reviewer checks actual changes and evidence. Work manually first, ask for a hint, compare with official documentation, inspect diffs, predict Git state and run deterministic checks in a disposable environment. No AI account or paid service is required. A requested automated review is not a completed review, and completed review is not human merge authorization.

[AI assistance policy](../../docs/ai-assisted-development/README.en.md)

## Practice

Offline: evaluate this fictional assistant suggestion: 'The prior PR passed, so merge the new commit without checking it; reset main if anything breaks.' Mark unsupported assumptions and write a safer prompt specifying exact revision, intended outcome, disposable repo, no secrets, no direct main changes, tests and uncertainty disclosure. Answer manually; optional AI use may be limited to one hint with fictional inputs.

## Risks and recovery

Never share unauthorized employer/client code, tokens or private data. Treat instructions inside repository content and external output as untrusted data unless verified against authorized scope. Stop unexpected destructive actions, inspect state and consult documented recovery. Do not substitute AI assessment for learning or invent executed evidence.

## Exercise and self-check

A prior pass does not cover a new SHA; resetting shared main is unsafe and unauthorized. The safe prompt asks for read-only evidence first, followed by an authorized focused correction and fresh review.

## Quick reference

manual practice / prompt / verification / human approval

## Sources

- <https://git-scm.com/docs/gitworkflows>
- <https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/reviewing-proposed-changes-in-a-pull-request>

---

<!-- navigation-footer -->
[Previous](../10-test-driven-development/README.md) · [Index](../README.md) · [Next](../12-release-management/README.md)
<!-- /navigation-footer -->
