# Quality automation

[English](quality-automation.md) · [Português](quality-automation.pt-BR.md) · [Español](quality-automation.es.md)

Maintainers need Git (2.28 or newer for the initial-branch option) and Python 3.12; neither Python nor CI is a learner prerequisite. From the repository root, stage new files before validation because checks inspect tracked paths. Run:

```text
python scripts/validate.py
python -m unittest discover -s tests -v
```

Use --check with structure, locales, links, navigation, examples, secrets or command-catalog to isolate a check. Validators inspect portable tracked paths, three-language presence, inline Markdown relative file links and images, module/chapter order and navigation, executable example policy and common secret patterns. They do not prove semantic translation, external links, heading anchors, all Markdown syntaxes, absence of all secrets or GitHub template UI behavior. The secret check reports file and line, not detected values; it is heuristic, not comprehensive. Review diffs and rotate exposed credentials independently.

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
