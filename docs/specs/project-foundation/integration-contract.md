# Learning Hub integration contract

[English](integration-contract.md) · [Português](integration-contract.pt-BR.md) · [Español](integration-contract.es.md)

Contract 1.0.0 proposed for Sprint 18 review. Scope: Git Study Guide only. The public repository is authoritative; use UTF-8 JSON/Markdown at build time, never HTML scraping or per-visitor GitHub API requests. The consumer keeps an external approved lock with full 40-character SHA-1 revision, guide_id=git-study-guide, manifest_version=1.0.0, assessment_version=1 and command_catalog_version=1. Exact versions only; reject missing, unsupported or mixed revisions. No self-embedded SHA; select the approved commit after merge and main CI. No release tag or active site pin is created here.

## Version and transport

curriculum/manifest.json is a generated inventory of 18 modules and 141 chapters (423 localized content paths). Module titles come from localized index H1 labels, chapter titles from existing localized chapter-index labels. IDs are frozen module slug or module.slug (including the existing numbered chapter slug); never renumber paths or reuse IDs when order changes. Orders are contiguous, zero-based within siblings. Global previous_id/next_id traverse chapters with null endpoints; Markdown navigation retains adjacent module indexes. Module/chapter titles and paths have exactly en (default), pt-BR and es. Kinds are lesson, reference, project and assessment. Assets and resources reference tracked files; resources are not an execution allowlist.

## Canonical sources and relationships

Four banks reference existing records.json (integer schema_version 1); command catalog has 14 categories, category and intent registries and catalog.json envelopes (integer schema_version 1). No duplicated record bodies. assessment-pilot and command-catalog validators remain authoritative for full record semantics. quiz_ids, exercise_ids and interview_ids identify the owning bank chapter and documented prerequisite relationships, not inferred chapter ownership; mock_ids identify only the mock bank chapter. command_ids identify the owning reference category and documented related chapters. Order is the canonical bank order. Exact reconstruction validates every association; mocks resolve quiz/challenge/interview IDs and same difficulty. Counts at this revision: 36 quizzes, 12 challenges, 24 interviews, three mocks, 120 operations. All are public, with solutions and rubrics visible.

## Compatibility and migration

Compared read-only with Python Study Guide commit a8a264f9f36ec276f0ad8e35f10f2d76f82fe211. Common conventions: locale maps, explicit order, immutable revision, typed associations, safe paths, fail-closed versions, guide namespace, advisory self-assessment. Git manifest adds guide_id, command_catalog, reference/assessment kinds and command_ids; bank descriptors point to aggregate records rather than Python record indexes. Git quiz type single-choice and string answer map explicitly to a consumer multiple_choice and answer.choice_id if adapting to Python-style UI; ordered lists of locale maps can be transposed to locale arrays. Git prerequisites remain many-to-many; do not invent chapter_id ownership, XP or Python coding-test fields. Preserve existing stable IDs and source bank versions. Do not import Git records as Python schema-valid records; use a guide-specific adapter. No changes made to Python or Learning Hub.

## Consumer procedure and safety

Four Draft 2020-12 structural schemas document manifest, assessment banks, command catalog and external lock. The dependency-free Python validator enforces strict JSON (duplicate keys, non-finite and fractional numeric tokens rejected), exact regenerated manifest, locale/path inventory, bank semantics, typed relationships, counts and supported versions. JSON Schema structural validation alone cannot prove existence, uniqueness by ID, semantics or reference integrity; use both schema and semantic checks in consumer integrations. Authoring: stage source changes, run python scripts/learning_hub_contract.py --write, stage manifest, then python scripts/validate.py --check learning-hub-contract and full tests. No network or new dependency.

Trusted reference consumer scripts/learning_hub_consumer.py accepts an external lock and a trusted local full-object SHA-1 Git database. It verifies the requested commit, disables replacement objects and network protocols, reads regular 100644 blobs by object ID without checkout filters, checks sizes and Git blob hashes, exports into new isolated staging, rejects traversal, symlinks, executable/submodule entries, collisions, missing/extra/modified files, and checks parsed schema equality to the trusted supported schemas outside the snapshot. It uses trusted validators, never imports snapshot code. Limits: 3000 files, 32 MiB total snapshot, 60 s per Git call. Validate candidate before adopting a pin; on failure retain previous approved pin; rollback is reselecting that full SHA. Fixture tests use actual checked-out commit and synthetic two-revision data, not live site or an independently signed release. Trust the object database, Git binary and private staging; no signature verification or hostile concurrent filesystem sandbox. Renderer must sanitize Markdown/HTML, links, assets and URLs; no execution of arbitrary content.

## Ownership and execution

Guide owns content, metadata, public solutions, reference QA and schema validation. Site owns safe UI/rendering, accessibility, progress, runtime isolation and deployment. Native Git projects and challenges are local_only with localized reasons; other chapters unverified. Browser_compatible is not supported in contract v1; no runtime was validated or introduced. Quizzes compare exact choice IDs; interviews/mocks use explicit manual rubric, never AI grading. Challenge predicates are trusted local QA fixtures, not an arbitrary learner runner; final state alone cannot prove safe intermediate behavior. Browser progress is device-specific and may be cleared. See the optional playground decision.

## Related documents

- [Manifest](../../../curriculum/manifest.json)
- [Manifest schema](../../../schemas/curriculum-manifest.schema.json)
- [Assessment schema](../../../schemas/assessment-bank.schema.json)
- [Command catalog schema](../../../schemas/command-catalog.schema.json)
- [Revision lock schema](../../../schemas/revision-lock.schema.json)
- [Reference consumer](../../../scripts/learning_hub_consumer.py)
- [Specification](specification.md)
- [ADR 0004](../../adr/0004-learning-hub-integration.md)
- [ADR 0006](../../adr/0006-browser-playground.md)
- [Python reference snapshot](https://github.com/RamonRDR/python-study-guide/blob/a8a264f9f36ec276f0ad8e35f10f2d76f82fe211/docs/specs/learning-hub-foundation/integration-contract.md)
