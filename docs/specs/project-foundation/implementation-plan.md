# Implementation plan

[English](implementation-plan.md) · [Português](implementation-plan.pt-BR.md) · [Español](implementation-plan.es.md)

Proposed for maintainer review; not authorization to start Sprint 01.

## Delivery sequence

| Sprint | Branch | Dependency | Deliverable |
| --- | --- | --- | --- |
| 00 | `docs/project-foundation` | — | Foundation, audit, SDD, ADRs, preliminary contract, indexes, provisional README |
| 01 | `docs/governance` | 00 | AGENTS, AUTHORS, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, SUPPORT, AI guidance and issue/PR templates |
| 02 | `feat/quality-automation` | 01 | Structure, navigation, validators, tests, CI; required status checks after observed runs and separate approval |
| 03 | `feat/getting-started` | 02 | Modules 00–01: onboarding, history and fundamentals |
| 04 | `feat/git-architecture` | 03 | Modules 02–03: Git architecture and basic commands |
| 05 | `feat/branch-management` | 04 | Module 04: branch management |
| 06 | `feat/merge-and-conflicts` | 05 | Module 05: merge, squash, rebase and conflicts |
| 07 | `feat/remote-repositories` | 06 | Module 06: remotes and collaboration |
| 08 | `feat/history-and-recovery` | 07 | Module 07: history and recovery |
| 09 | `feat/github` | 08 | Module 08: GitHub |
| 10 | `feat/gitlab` | 09 | Module 09: GitLab |
| 11 | `feat/ci-cd` | 10 | Module 10: CI/CD and automation |
| 12 | `feat/professional-workflows` | 11 | Module 11: professional workflows |
| 13 | `feat/security-governance` | 12 | Module 12: security and governance |
| 14 | `feat/advanced-git` | 13 | Modules 13–14: advanced Git and internals |
| 15 | `feat/command-reference` | 14 | Module 15: command reference |
| 16 | `feat/practical-projects` | 15 | Module 16: eight practical projects |
| 17 | `feat/challenges-interviews` | 16 | Module 17: challenges, quizzes and interviews; pilot structured records |
| 18 | `feat/learning-hub-contract` | 17 | Finalize content contract, manifests, schemas, consumer fixtures; evaluate optional playground separately |
| 19 | `docs/release-handoff` | 18 | Maintainer-supplied identity, final README, QA, release handoff |

## Repository design and workflow

Use root README.md and docs/localized/README.{pt-BR,es}.md; root governance translations in docs/localized/. Module and chapter folders use README.md, README.pt-BR.md, README.es.md, shared examples/ as needed. Architecture and specs are sibling translations. Proposed assets/, scripts/, tests/, .github/ and curriculum folders are created only when useful. Do not add empty directories. Keep official visual assets deferred. Before each sprint, read main and applicable instructions, scope, branch from current main, implement all locales, run available checks, review every file, inspect privacy, open PR, verify CI and request Codex review if available, address findings and revalidate latest SHA, record task evidence, obtain maintainer approval, squash merge, verify main and branch deletion, prepare handoff.

## Validation strategy

Sprint 00 bootstrap: documentary checks only, no CI. Sprint 02 adds locale presence, internal links, navigation, structure, allowlisted examples, secret scanning and Linux/Windows jobs; later sprints add deterministic state/conflict/recovery tests and schema/ID/reference validation when records exist. Use standard-library tooling where sufficient, temporary directories and isolated Git configuration; assert refs, index, tree and working files rather than fragile hashes or localized output. Never run arbitrary learner submissions in privileged CI. Required checks require separate authorization after actual check names/runs are known.

## Related documents

- [Constitution](../constitution.md)
- [Specification](specification.md)
- [Tasks](tasks.md)
- [Acceptance criteria](acceptance-criteria.md)
- [Roadmap](../../roadmap.md)
