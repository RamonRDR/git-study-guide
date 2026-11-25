# ADR 0003: Practice environments

[English](0003-practice-environments.md) · [Português](0003-practice-environments.pt-BR.md) · [Español](0003-practice-environments.es.md)

Proposed for maintainer review; not authorization to start Sprint 01.

## Context

Git state changes may destroy learner work and remote services need accounts; practice must remain free.

## Decision

Use installed Git in disposable temporary directories, bare origin and multiple clones. Isolate identity/config, hooks and credentials; avoid real remotes by default. Explicitly label platform-only tasks optional. Inspect state before destructive commands and clean only owned temporary paths; never target guide repository.

## Alternatives

Reject mandatory hosted labs and remote server shell (cost, credentials, isolation); defer browser simulation/runtime until evaluated by separate ADR in Sprint 18.

## Consequences

Assert state deterministically, test Linux/Windows, document supported versions and shell differences. No guarantee of recovery after destructive operations. A browser simulation must not claim Git fidelity without testing.

## Related documents

- [ADR index](README.md)
- [Integration contract](../specs/project-foundation/integration-contract.md)
