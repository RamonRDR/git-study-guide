# Spec-Driven Development (SDD)

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../08-code-review/README.md) · [Index](../README.md) · [Next](../10-test-driven-development/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 45 min

**Prerequisites:** [CI/CD](../../ci-cd/README.md) · [Code review and merge readiness](../08-code-review/README.md)

**Objective:** Trace requirements to tasks and acceptance evidence.

## What and why

SDD uses a specification as the basis for planning, implementation and verification. It is a family of practices, not a Git command or a single mandatory framework. A constitution establishes project principles, a specification defines observable requirements and exclusions, a plan describes implementation choices, tasks divide work, and acceptance criteria state evidence for success. An architecture decision record (ADR) documents context, decision and consequences when a significant choice needs justification. Trace requirements to tasks and tests. Use a focused branch and review changes to specs when requirements evolve. The guide's own documents illustrate one implementation; external tools and AI are optional.

[Project specification](../../docs/specs/project-foundation/specification.md) · [Acceptance criteria](../../docs/specs/project-foundation/acceptance-criteria.md)

## Practice

Draft a one-page specification for the fictional catalog: R1 exposes an exact `status: ready` line when ready; R2 retains the old draft state before integration; exclusion: no deployment or external services. AC1 checks the ready line, AC2 checks initial absence and clean integrated state. Plan a single file change and a bounded shell check; tasks T1 write the check, T2 implement, T3 inspect diff and integrate, T4 record release evidence. Map R1->AC1/T1/T2 and R2->AC2/T1/T3; link T4 to release policy. Compare the plan with chapter 13.

## Risks and recovery

Do not write vague acceptance criteria such as 'works well', generate tasks before clarifying intent, or mark an unrun test passed. Resolve contradictory specs at their source with the maintainer, update affected tasks/tests and request review. A spec does not replace experiments or feedback.

## Exercise and self-check

Each requirement has at least one observable check and each task a reason. Explicit exclusions prevent scope creep. The exact accepted revision and evidence belong in the handoff.

## Quick reference

constitution / spec / plan / task / AC / ADR

## Sources

- <https://github.github.com/spec-kit/>
