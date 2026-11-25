# ADR 0001: Content source of truth

[English](0001-content-source-of-truth.md) · [Português](0001-content-source-of-truth.pt-BR.md) · [Español](0001-content-source-of-truth.es.md)

Proposed for maintainer review; not authorization to start Sprint 01.

## Context

A free independent guide and future site need one authoritative revision.

## Decision

Markdown, shared examples and structured data live in this repository. Import an approved immutable commit at site build time. Keep GitHub/local learning independent.

## Alternatives

Reject manually duplicated website content (drift), HTML scraping (presentation coupling) and per-visitor API calls (availability and limits).

## Consequences

Consumer must validate revision, paths and safe rendering; changes appear after rebuild. No paid infrastructure required by design; actual limits must be checked.

## Related documents

- [ADR index](README.md)
- [Integration contract](../specs/project-foundation/integration-contract.md)
