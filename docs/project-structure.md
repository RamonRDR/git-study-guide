# Project structure

[English](project-structure.md) · [Português](project-structure.pt-BR.md) · [Español](project-structure.es.md)

The root holds governance, the MIT license and 18 stable module indexes. docs/ holds architecture, specifications, translations and engineering guidance. scripts/ contains standard-library validation and the internal curriculum registry; tests/ contains deterministic fixtures. .github/ contains templates and CI. Assets are added only when needed. The registry is internal, not the final Learning Hub schema.

Chapters use NN-topic/README.md, README.pt-BR.md and README.es.md. Register chapter slugs in scripts/curriculum.json in numeric order and link them in the chapters block. Each module index and chapter has identical localized navigation inside the navigation and navigation-footer blocks, the former after title and locale selector and the latter at the end. Use previous/index/next in that order. The first and last chapters link to the adjacent module indexes (including reserved ones) using Previous module/Next module labels. Only absent directions at the roadmap endpoints use an unlinked dash. Module indexes link to the adjacent indexes and learning path. The validator's navigation_entries and navigation_line functions define canonical destinations and labels. Keep paths stable and do not create empty directories.

Module 15 uses one canonical catalog.json per category, plus category and intent registries in scripts/. Its trilingual Markdown pages are generated from those records using scripts/render_command_reference.py and the existing navigation registry. Edit JSON rather than generated pages; see [ADR 0005](adr/0005-command-catalog-architecture.md). This is an internal pilot, not the final integration contract.

Module 16 provides eight manually executed trilingual projects under practical-projects/. Each uses a fresh disposable environment, explicit acceptance states and a public reference solution. Shared setup comes from project 01; no executable learner artifacts or new dependencies. The fixed tests in tests/test_git_practical_projects.py independently reproduce the intended states. Bash/Git Bash is for learners; Python's standard library is for repository QA.

- [Learning path](learning-path.md)
- [Quality automation](quality-automation.md)

- [Assessment pilot schema](assessment-pilot.md)
