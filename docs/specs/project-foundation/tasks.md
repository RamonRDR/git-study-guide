# Task register

[English](tasks.md) · [Português](tasks.pt-BR.md) · [Español](tasks.es.md)

Foundation approved and integrated via PR #1 on 2026-11-25. Subsequent changes require review and explicit maintainer approval.

| Task | Description | Status |
| --- | --- | --- |
| T00-01 | Audit repositories, branches, ruleset and Python reference | Read-only audit completed; see audit |
| T00-02 | Draft trilingual Constitution, specification, plan, tasks, acceptance criteria and ADRs | Done ([PR #1](https://github.com/RamonRDR/git-study-guide/pull/1)) |
| T00-03 | Draft contract, related guides, indexes, roadmap and provisional README | Done ([PR #1](https://github.com/RamonRDR/git-study-guide/pull/1)) |
| T00-04 | Validate locale structure, links, content alignment and latest PR; request Codex review | Done ([PR #1](https://github.com/RamonRDR/git-study-guide/pull/1)) |
| T00-05 | Maintainer approval, squash merge, verify main | Done ([PR #1](https://github.com/RamonRDR/git-study-guide/pull/1)) |
| T01-01 | AGENTS, AUTHORS, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, SUPPORT, AI guidance and issue/PR templates (AC-01; depends on T00-05) | Done ([PR #2](https://github.com/RamonRDR/git-study-guide/pull/2)) |
| T02-01 | Structure, navigation, validators, tests, CI; required status checks after observed runs and separate approval (AC-02; depends on T01-01) | Done ([PR #3](https://github.com/RamonRDR/git-study-guide/pull/3)) |
| T03-01 | Modules 00–01: onboarding, history and fundamentals (AC-03; depends on T02-01) | Submitted for review |
| T04-01 | Modules 02–03: Git architecture and basic commands (AC-04; depends on T03-01) | Pending |
| T05-01 | Module 04: branch management (AC-05; depends on T04-01) | Pending |
| T06-01 | Module 05: merge, squash, rebase and conflicts (AC-06; depends on T05-01) | Pending |
| T07-01 | Module 06: remotes and collaboration (AC-07; depends on T06-01) | Pending |
| T08-01 | Module 07: history and recovery (AC-08; depends on T07-01) | Pending |
| T09-01 | Module 08: GitHub (AC-09; depends on T08-01) | Pending |
| T10-01 | Module 09: GitLab (AC-10; depends on T09-01) | Pending |
| T11-01 | Module 10: CI/CD and automation (AC-11; depends on T10-01) | Pending |
| T12-01 | Module 11: professional workflows (AC-12; depends on T11-01) | Pending |
| T13-01 | Module 12: security and governance (AC-13; depends on T12-01) | Pending |
| T14-01 | Modules 13–14: advanced Git and internals (AC-14; depends on T13-01) | Pending |
| T15-01 | Module 15: command reference (AC-15; depends on T14-01) | Pending |
| T16-01 | Module 16: eight practical projects (AC-16; depends on T15-01) | Pending |
| T17-01 | Module 17: challenges, quizzes and interviews; pilot structured records (AC-17; depends on T16-01) | Pending |
| T18-01 | Finalize content contract, manifests, schemas, consumer fixtures; evaluate optional playground separately (AC-18; depends on T17-01) | Pending |
| T19-01 | Maintainer-supplied identity, final README, QA, release handoff (AC-19; depends on T18-01) | Pending |

Update task evidence in each focused PR. A proposed deliverable or opened PR is not completion. Use actual check/review links and commit SHAs; after approved merge, verify main and branch deletion, and record handoff in the next authorized change if necessary.


Sprint 00 evidence: [Codex](https://github.com/RamonRDR/git-study-guide/pull/1#issuecomment-7174894634), [validation](https://github.com/RamonRDR/git-study-guide/pull/1#issuecomment-7174867993), [squash commit](https://github.com/RamonRDR/git-study-guide/commit/38fd45048a036ef377a05ec8429e624464841159). Maintainer approved; main and branch deletion verified; CI absent by plan.

## Related documents

- [Implementation plan](implementation-plan.md)
- [Acceptance criteria](acceptance-criteria.md)
- [Baseline audit](audit.md)

Sprint 01 evidence: [PR #2](https://github.com/RamonRDR/git-study-guide/pull/2), [Codex](https://github.com/RamonRDR/git-study-guide/pull/2#issuecomment-7176325295), [squash commit](https://github.com/RamonRDR/git-study-guide/commit/df139992ae109145184a4de86b2a95b7e1187e0b). Latest review had no findings; main and branch deletion verified.

Sprint 02 evidence: [PR #3](https://github.com/RamonRDR/git-study-guide/pull/3), [CI](https://github.com/RamonRDR/git-study-guide/actions/runs/45717835244), [main CI](https://github.com/RamonRDR/git-study-guide/actions/runs/45718411371), [Codex](https://github.com/RamonRDR/git-study-guide/pull/3#issuecomment-7176975402), [ruleset](https://github.com/RamonRDR/git-study-guide/rules/28108699). Main and branch deletion verified; Linux and Windows checks required with strict up-to-date policy after maintainer authorization.
