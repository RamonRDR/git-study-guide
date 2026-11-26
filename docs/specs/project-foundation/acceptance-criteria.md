# Acceptance criteria

[English](acceptance-criteria.md) · [Português](acceptance-criteria.pt-BR.md) · [Español](acceptance-criteria.es.md)

Foundation approved and integrated via PR #1 on 2026-11-25. Subsequent changes require review and explicit maintainer approval.

| ID | Sprint | Observable acceptance condition |
| --- | --- | --- |
| AC-00 | 00 | Audit baseline and ruleset; 11 primary documents in three locales plus indexes, audit, roadmap and provisional README; aligned requirements/decisions; internal links and locale presence checked; latest PR evidence, no fabricated CI; maintainer approval before merge. |
| AC-01 | 01 | All governance docs and templates localized; authorship and AI roles explicit; security and support instructions usable; no affiliation claim. |
| AC-02 | 02 | Validators reject missing locales, broken links, invalid paths/navigation and unsafe or unapproved examples; CI runs on Linux/Windows with least privilege; actual run evidence; status-check configuration separately approved. |
| AC-03 | 03 | All module 00–01 topics taught; first commit reproducible; OS-specific instructions verified or limitations noted; historical claims sourced. |
| AC-04 | 04 | Modules 02–03 explain states and command effects; tests assert staging/commit/diff outcomes; accessible state diagram. |
| AC-05 | 05 | Module 04 local branch examples validate refs, switching and detached HEAD; remote practice deferred; deletion warnings. |
| AC-06 | 06 | Module 05 validates distinct merge topologies, conflict/abort/continue and squash/rebase effects; no destructive shared-history exercise. |
| AC-07 | 07 | Module 06 uses bare origin and two clones; verifies tracking, divergence and synchronization; online auth optional, safe and documented. |
| AC-08 | 08 | Module 07 distinguishes undo and history rewriting; tests recovery and limits; destructive labs disposable, with inspection/cleanup. |
| AC-09 | 09 | Module 08 covers GitHub features, PR/review/protection workflow, distinction from Git; optional account tasks and current official references. |
| AC-10 | 10 | Module 09 covers GitLab MRs, groups, runners, protection and comparison; optional hosted practice and current official references. |
| AC-11 | 11 | Module 10 distinguishes CI/delivery/deployment; safe YAML examples for both platforms; test/lint configuration as applicable; no privileged untrusted pipeline. |
| AC-12 | 12 | Module 11 compares workflow trade-offs, SDD/TDD, manual practice, reviews and releases with original scenarios. |
| AC-13 | 13 | Module 12 covers credential protection, least privilege, signing, supply chain and incident response; never expose real secrets. |
| AC-13.1 | 13.1 | Every curriculum module index and chapter has identical localized top and bottom navigation; chapter edges lead to adjacent module indexes; correct endpoints, locale and ordering enforced by deterministic regression tests. Stable content and paths preserved. |
| AC-14 | 14 | Modules 13–14 teach listed advanced operations and object/ref internals; safe bounded tests and accurate diagrams; version requirements identified. |
| AC-15 | 15 | Catalog has at least 101 meaningful distinct entry IDs; report category counts separately and validate required fields, risk and sources. |
| AC-16 | 16 | Eight projects documented in three locales with setup, objectives, expected states, cleanup, solutions and tests; account-dependent tasks optional. |
| AC-17 | 17 | Challenges and interview records map prerequisites, provide hints, solutions, explanations, objective rubrics and deterministic checks rejecting representative wrong states; pilot schema documented. |
| AC-18 | 18 | Versioned manifest and schemas reject invalid paths, missing locales, duplicate IDs, dangling refs and unsupported versions; consumer fixture uses immutable revision; optional playground ADR records compatibility, isolation, limits and cost. |
| AC-19 | 19 | Final three READMEs and approved visual assets (or explicit deferred exception), real badges, full applicable QA, documented limitations, reviewed handoff, approval and immutable revision evidence. |

## Global definition of done

All affected public documents aligned in three locales; source/links/structure verified; relevant checks actually executed or explicitly disclosed; no unresolved relevant findings, secrets or unrelated changes; task evidence current; latest PR revision reviewed and maintainer authorizes squash merge. Structural translation checks do not prove conceptual parity; human review remains necessary. An absent CI is not a passing CI. Sprint 00 cannot be marked integrated before merge.

## Related documents

- [Specification](specification.md)
- [Tasks](tasks.md)
