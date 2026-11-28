# Sprint 00 baseline audit

[English](audit.md) · [Português](audit.pt-BR.md) · [Español](audit.es.md)

Read-only GitHub API audit before branch creation. Git baseline main b4bd782519ebc8e52e6751362443aa634e86e56d; only LICENSE and README.md, one protected branch and no open PRs. Public, MIT, squash only, auto-merge disabled, update branch suggestion and delete branch on merge enabled. Ruleset 28108699 active for default branch, no bypass actors, PR and conversation resolution required, 0 required approvals, linear history, deletion/force-push blocked, extra approval for unattributed changes, squash only. No required checks in ruleset; no workflow in initial tree. Do not change administration in Sprint 00.

Python baseline main 9102bbbf8f8dd846f2fb9682dd3f55bcacc10c95, public MIT, protected main and feat/problem-solving-foundations at same SHA. Inspected tree, AGENTS, constitution, specification, plan, tasks, acceptance criteria, ADRs 0001–0003, AI guidance, integration contract and related register (English representatives). Found localization, quality-checks.yml, scripts for internal links, locale coverage, structure, examples and navigation. Reuse layout, SDD, review process and revision-pinned contract; adapt Python-specific runtime, PEP 8 and code tests into language-neutral Git-state testing. No Python CI rerun, exhaustive semantic translation audit or changes to Python performed. This audit does not assert the reference's entire curriculum passes.

- [Git baseline](https://github.com/RamonRDR/git-study-guide/commit/b4bd782519ebc8e52e6751362443aa634e86e56d)
- [Ruleset](https://github.com/RamonRDR/git-study-guide/rules/28108699)
- [Python baseline](https://github.com/RamonRDR/python-study-guide/tree/9102bbbf8f8dd846f2fb9682dd3f55bcacc10c95)

## Related documents

- [Specification](specification.md)
- [Tasks](tasks.md)

## Sprint 19B final QA — baseline evidence (in progress)

Immutable baseline: [03c3043](https://github.com/RamonRDR/git-study-guide/commit/03c30438a5490d6c8f9b22dbf457a644658e042f). Sprint 19A [closure](https://github.com/RamonRDR/git-study-guide/pull/21#issuecomment-7227417357): [push CI](https://github.com/RamonRDR/git-study-guide/actions/runs/46061260750) and [manual CI](https://github.com/RamonRDR/git-study-guide/actions/runs/46062482507) both passed nine validators and 152 tests per OS; reviewed tree, single parent, noreply metadata, verified signature and branch deletion confirmed. Actual cancellation of superseded PR runs remains unexercised.

Independent inventory check: 637 regular tracked files; 18 modules, 141 unique chapter IDs, 423 unique localized chapter paths and 54 localized index paths all present; no missing locale or global navigation sequence mismatch; 159 assessment and 312 command associations. Manifest schema version 1.0.0.

Targeted semantic sampling of excerpts in six chapters across all three locales (18 files): first commit, merge conflict resolution, reset, secrets/disclosure prevention, refs and HEAD, and The Lost Commit. Compared key explanations, safety conditions and expected states; no material discrepancy identified in sampled excerpts. Fenced block contents match in all six sets. This is not a complete semantic translation audit, execution of every learner lab, macOS test, external link audit or browser runtime validation.

AC-19 remains in progress: final localized READMEs, maintainer-approved visual assets or explicit exception, truthful badges, remaining applicable QA and limitations, reviewed handoff and approved immutable release evidence. Do not tag or publish yet. No other repository changes.
