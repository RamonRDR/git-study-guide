# ADR 0005: Command catalog architecture

[English](0005-command-catalog-architecture.md) · [Português](0005-command-catalog-architecture.pt-BR.md) · [Español](0005-command-catalog-architecture.es.md)

Status: approved for Sprint 15 implementation by the maintainer; integration pending review.

## Decision

Maintain one canonical UTF-8 JSON document per registered command-reference category, with a local schema version, stable lowercase IDs, shared technical values and explicit en/pt-BR/es maps for learner-facing prose. Generate all three category pages and the module index deterministically using Python's standard library. Commit the generated Markdown for direct GitHub reading; do not edit it independently. Use the existing curriculum registry and canonical navigation functions. Build category and intent indexes from the same records.

Validate counts (at least 101 meaningful operations, target 120), uniqueness, fields, risks, sources, chapter references, locale maps and generated output equality. Distinguish native commands, subcommands, option usages, workflows, external tools and platform operations. No automatic execution of catalog commands.

## Alternatives and consequences

Hand-maintained JSON plus Markdown duplicates content; a website-only catalog prevents independent GitHub reading. Neither is adopted. Structural checks cannot establish technical accuracy or semantic translation. Review actual examples, version requirements and official sources separately. This is an internal pilot, not a finalized Learning Hub schema or consumer; Sprint 18 remains responsible for the final integration contract. No new paid service or dependency.

- [ADR index](README.md)
- [Integration contract](../specs/project-foundation/integration-contract.md)
