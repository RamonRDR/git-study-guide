# Quality automation

[English](quality-automation.md) · [Português](quality-automation.pt-BR.md) · [Español](quality-automation.es.md)

Maintainers need Git (2.28 or newer for the initial-branch option) and Python 3.12; neither Python nor CI is a learner prerequisite. From the repository root, stage new files before validation because checks inspect tracked paths. Run:

```text
python scripts/validate.py
python -m unittest discover -s tests -v
```

Use --check with structure, locales, links, navigation, examples, secrets, command-catalog, assessment-pilot or learning-hub-contract to isolate a check. Validators inspect portable tracked paths, three-language presence, inline Markdown relative file links and images, module/chapter order and navigation, executable example policy and common secret patterns. They do not prove semantic translation, external links, heading anchors, all Markdown syntaxes, absence of all secrets or GitHub template UI behavior. The secret check reports file and line, not detected values; it is heuristic, not comprehensive. Review diffs and rotate exposed credentials independently.

Navigation validation enforces canonical localized header and footer blocks for every module index and chapter, exact labels and paths, chapter and module boundary transitions, placement and duplicate detection. Tests include negative fixtures for missing, divergent, reordered, wrong-language, reversed, hidden or misplaced navigation. Planned module indexes remain navigable; their lessons are not yet published.

The command-catalog check validates the 14 registered JSON categories, at least 101 distinct operations (approved target 120), locale maps, risks, official-source URL policy, related chapters, intent tags and exact equality with the canonical renderer. It does not execute catalog commands or prove semantic translation, external URL availability or correctness of every example. To change the catalog, edit its canonical JSON, stage new inputs and regenerate the registered Markdown from the repository root:

```text
python scripts/render_command_reference.py --write
```

Stage the generated pages, run `python scripts/validate.py --check command-catalog`, then run all validators and tests. The default renderer invocation checks generated output without writing.

No executable learning examples are approved yet. The empty manifest is a fail-closed gate: all files under examples/ (including inert files and case variants) are rejected, regardless of extension or mode, and nonempty manifests fail until a reviewed execution protocol exists. Do not run arbitrary learner code. Initial Git smoke test uses an isolated temporary repository and asserts staging, branch, committed content and clean status. Later sprints extend deterministic scenarios. Run local tests only from trusted reviewed revisions.

Sprint 16 adds eight fixed integration tests for project outcomes, including intermediate states, expected conflict and invalid committed snapshots. They run in isolated temporary repositories and local bare origins; the tests do not extract or execute Markdown or learner submissions. Hosted workflows remain unexecuted simulations. Run the full suite and inspect actual Ubuntu/Windows logs for the latest SHA.

CI uses standard GitHub-hosted Linux and Windows runners on pull_request and pushes to main, with read-only contents permissions, pinned first-party actions, no persisted checkout credentials, no secrets, no self-hosted runners and no paid service. Each job is limited to ten minutes. PR code remains untrusted; runners are disposable, not privileged deployment environments. Check actual runs on the latest PR revision; required status checks need separate approval after names are observed.

- [Project structure](project-structure.md)
- [GitHub Actions security](https://docs.github.com/en/actions/reference/security/secure-use)

The assessment-pilot check verifies the four versioned banks, exact difficulty counts, globally unique IDs, valid prerequisites and mock references, localized fields, choices, answers, allowed state predicates and equality with generated Markdown. Edit records.json, stage the JSON and curriculum changes, then run python scripts/render_assessments.py --write; stage generated pages and run python scripts/validate.py --check assessment-pilot and all checks/tests. The 12 fixed QA scenarios exercise valid and representative incorrect Git states. No evaluator runs learner submissions or reads arbitrary repositories; only trusted disposable fixtures are supported. Structural validation does not establish semantic translation or educational accuracy.

- [Assessment pilot schema](assessment-pilot.md)

The learning-hub-contract validator reconstructs the manifest from the curriculum registry, localized indexes, tracked paths and canonical banks. It checks exact supported versions, strict JSON, titles, global navigation and every typed relationship. After source edits, stage sources and run python scripts/learning_hub_contract.py --write; stage the result and run all checks and tests. Twelve reference consumer/contract tests include malformed manifests and locks, missing locales, invalid paths, duplicate IDs, dangling refs, schema mismatch, mixed snapshots, symlinks, immutable revision and rollback fixtures. The structural schemas are published as interchange specifications; the standard-library semantic validator is the repository gate, not a general JSON Schema engine. Site-side rendering/runtime and hostile Git databases are outside these tests.

- [Learning Hub integration contract](specs/project-foundation/integration-contract.md)
