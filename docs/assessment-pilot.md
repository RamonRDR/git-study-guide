# Assessment pilot schema

[English](assessment-pilot.md) · [Português](assessment-pilot.pt-BR.md) · [Español](assessment-pilot.es.md)

Internal Sprint 17 pilot, schema_version 1. Not a published Learning Hub contract. Four canonical files under exercises/ store an envelope with schema_version, kind and records. English is primary; every learner-facing string is a nonempty map with exactly en, pt-BR and es. IDs are stable lower-case hyphen tokens prefixed by record kind. Difficulty is easy, medium or hard. Prerequisites name earlier registered module/chapter paths. No executable content or credentials. Record order is presentation order.

## Common fields

id, difficulty, prerequisites, title, prompt, hints, explanation. Hints are ordered localized maps; prerequisites resolve to existing curriculum chapters outside module 17.

- Quiz: type single-choice, three choices with unique stable IDs and localized text, answer is exact choice ID. No fuzzy matching.
- Challenge: estimated_minutes, setup, solution (ordered localized steps), execution=local_only, execution_reason, checks. Setup points to a fresh isolated fixture, and solutions are instructions, not executable strings. Checks are allowlisted typed state predicates; no arbitrary paths, options or commands.
- Interview: expected_answer, rubric, follow_ups. One point per met rubric criterion, zero otherwise; self-assessment only.
- Mock: duration_minutes, quiz_ids, challenge_ids, interview_ids, rubric. References must resolve to correct type and same difficulty. Four quizzes (4 points), one challenge (2), two interviews (4), total 10.

State checks use clean status, current branch, exact committed/index/working bytes, tracked/untracked paths, ref equality or inequality, ancestry, tree equality, parent/commit counts, tag object type and unmerged entries. Each predicate has an exact allowed field set; fixture filenames and values are constrained. The assessment_state module accepts only controlled callbacks from trusted QA fixtures; it is not a sandbox or public runner. A final-state check cannot prove how a learner reached it, nor whether an intermediate operation was safe; use manual evidence when required. Do not evaluate untrusted repositories or execute learner code. Browser execution and the final consumer contract are deferred to Sprint 18.

The assessment-pilot check verifies the four versioned banks, exact difficulty counts, globally unique IDs, valid prerequisites and mock references, localized fields, choices, answers, allowed state predicates and equality with generated Markdown. Edit records.json, stage the JSON and curriculum changes, then run python scripts/render_assessments.py --write; stage generated pages and run python scripts/validate.py --check assessment-pilot and all checks/tests. The 12 fixed QA scenarios exercise valid and representative incorrect Git states. No evaluator runs learner submissions or reads arbitrary repositories; only trusted disposable fixtures are supported. Structural validation does not establish semantic translation or educational accuracy.

- [Module 17](../exercises/README.md)
- [Integration contract](specs/project-foundation/integration-contract.md)
- [Quality automation](quality-automation.md)
