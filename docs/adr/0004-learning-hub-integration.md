# ADR 0004: Learning Hub integration

[English](0004-learning-hub-integration.md) · [Português](0004-learning-hub-integration.pt-BR.md) · [Español](0004-learning-hub-integration.es.md)

Foundation approved and integrated via PR #1 on 2026-11-25. Subsequent changes require review and explicit maintainer approval.

## Context

Future guides need shared conventions but different execution capabilities. Python's contract is preliminary.

## Decision

Use preliminary compatible revision-pinned manifests, locale maps, stable IDs and guide namespace at consumer level. Keep Git-specific deterministic repository state assessment separate from Python execution; finalize schemas after pilots and coordinated review. Site owns UI/runtime/progress/accessibility.

## Alternatives

Reject one forced runtime, universal schema imposed unilaterally, website inside guide, and AI semantic grading.

## Consequences

Consumers validate schema/revision, reject unsupported major versions and unsafe refs. Playground is optional: evaluate fidelity, persistence, isolation, accessibility, limits and zero cost before selecting technology; no arbitrary privileged execution.

## Related documents

- [ADR index](README.md)
- [Integration contract](../specs/project-foundation/integration-contract.md)
