# ADR 0002: Multilingual architecture

[English](0002-multilingual-architecture.md) · [Português](0002-multilingual-architecture.pt-BR.md) · [Español](0002-multilingual-architecture.es.md)

Foundation approved and integrated via PR #1 on 2026-11-25. Subsequent changes require review and explicit maintainer approval.

## Context

All public prose must remain conceptually aligned and easily browsable on GitHub.

## Decision

English primary; sibling README.md/README.pt-BR.md/README.es.md for chapters; sibling suffixes for specs/ADRs, root translations in docs/localized/. Share code/IDs/assets when text-neutral; localize learner-visible text. Review three locales in same PR.

## Alternatives

Separate repositories (drift); one multilingual Markdown file (poor navigation); machine translation at runtime (unreviewed meaning) rejected.

## Consequences

Validate file parity, locale selectors and navigation; human review verifies semantics. Preserve paths and MIT text.

## Related documents

- [ADR index](README.md)
- [Integration contract](../specs/project-foundation/integration-contract.md)
