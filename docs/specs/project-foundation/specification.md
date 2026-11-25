# Project foundation specification

[English](specification.md) · [Português](specification.pt-BR.md) · [Español](specification.es.md)

Foundation approved and integrated via PR #1 on 2026-11-25. Subsequent changes require review and explicit maintainer approval.

Goal: a public, practical, MIT-licensed Git Study Guide from beginner to advanced engineering. Baseline main: b4bd782519ebc8e52e6751362443aa634e86e56d. Python reference: 9102bbbf8f8dd846f2fb9682dd3f55bcacc10c95.

## Functional requirements

- FR-01 — Publish independent EN/PT-BR/ES content with language selectors, previous/index/next navigation, stable paths and explicit prerequisites. Follow the roadmap without requiring Python.
- FR-02 — Teach history, architecture, local operations, branches, remotes, merge strategies, recovery, platforms, CI/CD, professional workflows, security and internals. Distinguish native Git from hosting features and explain state changes.
- FR-03 — Each applicable lesson includes objective, level, prerequisites, study time, definition, rationale/problem, syntax, use/avoid, relationships, internals, basic/professional examples, common mistakes, risk/recovery, exercise, checklist, quick reference and official sources. Adapt with rationale; do not introduce undefined terms.
- FR-04 — Catalog 100+ meaningful commands/operations; stable ID, category, purpose, syntax, prerequisites, options, use/avoid, example and expected result, affected state, side effects, risk, alternatives, errors, recovery, minimum version when relevant, official references and intent tags. Do not inflate distinct subcommand counts.
- FR-05 — Use accessible diagrams with localized explanations for state, refs, history, branch/merge/rebase, divergence, cherry-pick, reflog, objects, collaboration and CI/CD. Evaluate Mermaid/SVG; validate topology and text alternatives.
- FR-06 — Provide eight practical projects using temporary repositories, bare origin and Alice/Bob clones; platform-only tasks optional. Include setup, success conditions, inspection, cleanup and safe recovery.
- FR-07 — Provide quizzes, challenges and interview records with stable IDs, three locales, prerequisites, progressive hints, reference answers, deterministic state checks and objective rubrics; open answers use self-assessment.
- FR-08 — Implement governance, trilingual AI-assisted development guidance, templates and automated quality gates; provisional README now, final identity and README in Sprint 19 with only verifiable badges.
- FR-09 — Provide versioned manifest, schemas, locale maps, stable IDs, safe relative paths, exercise capabilities, validated fixtures and approved-revision handoff; align with Python contract without unilateral universal schema decisions.

## Non-functional requirements

- NFR-01 — Zero additional cost; no paid services or obligatory AI. Verify free-tier constraints before relying on external services.
- NFR-02 — Conceptual parity in all public docs, including templates; preserve MIT, authorship and stable published paths; no private information.
- NFR-03 — Validate links, structure, navigation, examples, state, conflicts, recovery, Linux/Windows, schemas, IDs, references and secrets; macOS when justified. Use allowlisted trusted examples, temporary directories and least privilege; no untrusted privileged CI.
- NFR-04 — No mandatory site runtime, AI grading, paid servers or arbitrary privileged command execution. Browser playground optional and unverified until evaluated.
- NFR-05 — Review and record actual validation evidence; never invent metrics, approvals or results. Maintain original examples and independence from official vendors.

## Scope and sources

Sprint 00: foundation only, no lessons, site, runtime, logo, other repositories, administrative edits or changes to Python. Subsequent sprints require approved dependencies. Prefer [Git documentation](https://git-scm.com/docs), [Pro Git](https://git-scm.com/book/en/v2), [GitHub Docs](https://docs.github.com/) and [GitLab Docs](https://docs.gitlab.com/); verify changing facts before publication. Future guides and a reusable template are deferred until Python and Git mature.

## Related documents

- [Constitution](../constitution.md)
- [Implementation plan](implementation-plan.md)
- [Tasks](tasks.md)
- [Acceptance criteria](acceptance-criteria.md)
- [Integration contract](integration-contract.md)
- [Related guides](related-guides.md)
- [Architecture decisions](../../adr/README.md)
- [Roadmap](../../roadmap.md)
- [Baseline audit](audit.md)
