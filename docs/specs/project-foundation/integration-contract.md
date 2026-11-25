# Preliminary Learning Hub integration contract

[English](integration-contract.md) · [Português](integration-contract.pt-BR.md) · [Español](integration-contract.es.md)

Preliminary normative direction for pilots; no published schema or implemented consumer. Finalize in Sprint 18 after Sprint 17 pilots and coordinated review with Python Study Guide.

## Version and transport

Import UTF-8 Markdown/JSON at build time from one approved immutable Git SHA. Record revision and schema_version; reject unknown major versions, invalid records and mixed revisions. No HTML scraping or per-visitor GitHub API dependency. Default en, supported en/pt-BR/es; learner-visible fields require locale maps. IDs lowercase ASCII dotted/hyphenated, stable independent of order; unique per entity type. Proposed consumer identity tuple (guide_id, entity_type, id), guide_id=git-study-guide; not a unilateral Python contract change. Orders explicit nonnegative unique among siblings. Repository-relative POSIX paths only: reject traversal, absolute paths, backslashes, schemes and symlink escapes; verify existence, resolve against same revision, sanitize Markdown/HTML. Previous/next use curriculum order, null at endpoints.

## Proposed record fields

| Entity | Fields |
| --- | --- |
| Curriculum | schema_version, default_locale, supported_locales, modules |
| Module | id, order, slug, title, index, chapters |
| Chapter | id, order, slug, title, content, assets, previous_id, next_id, exercise_ids, quiz_ids, interview_ids, execution |
| Quiz | id, chapter_id, difficulty, type, prompt, choices, answer, explanation, hints, xp |
| Exercise | id, chapter_id, difficulty, estimated_minutes, title, prompt, concepts, constraints, examples, starter_path or starter text, hints, solution_path, explanation, tests, execution, allowed_dependencies |
| Interview question | id, topic, level, prompt, expected_answer, explanation, intent, common_errors, follow_ups, examples, rubric |
| Mock | id, level, duration_minutes, question_ids, exercise_ids, scoring rubric |
| Command entry | id, category, command, intent_tags, purpose, syntax, prerequisites, options, examples, expected_state, risk, recovery, references |

These are candidate fields, not a schema. Preserve compatible common names from Python; localized prose includes titles, prompts, choices, hints, explanations and rubric descriptions. Difficulty easy/medium/hard. Objective quiz types and accepted values must be explicit; XP advisory only. Command records supplement the full FR-04 fields. Git exercise tests describe setup, allowed operations, expected repository state and limits; compare refs, ancestry, index, tracked/untracked files and contents as appropriate, not incidental object hashes, times, branch defaults or localized command output. Test representative incorrect states. Open questions use reference answers and self-assessment; public solutions are inspectable.

## Execution and ownership

Retain Python-compatible execution values browser_compatible (only after pinned runtime validation), local_only (reason required), unverified (default, no automatic browser execution). Propose optional Git-specific capability metadata for simulation versus real Git and account-required activities; finalize after pilot, never infer support. Native Git labs remain local; no site/runtime here. Browser playground evaluation must address fidelity, operations supported, security, isolation, persistence, accessibility, compatibility, cancellation/time/output limits and zero additional cost. A worker alone is not a security boundary. Never run arbitrary privileged commands or AI semantic grading. Guide owns content, metadata, solutions, tests and validation; site owns safe renderer, UI, runtime isolation, progress, accessibility and deployment. Local browser progress is device-specific and may be cleared. No mandatory backend sync.

Reference (reviewed snapshot): [Python contract](https://github.com/RamonRDR/python-study-guide/blob/9102bbbf8f8dd846f2fb9682dd3f55bcacc10c95/docs/specs/learning-hub-foundation/integration-contract.md).

## Related documents

- [Specification](specification.md)
- [Architecture decisions](../../adr/README.md)
