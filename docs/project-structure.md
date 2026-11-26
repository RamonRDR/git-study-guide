# Project structure

[English](project-structure.md) · [Português](project-structure.pt-BR.md) · [Español](project-structure.es.md)

The root holds governance, the MIT license and 18 stable module indexes. docs/ holds architecture, specifications, translations and engineering guidance. scripts/ contains standard-library validation and the internal curriculum registry; tests/ contains deterministic fixtures. .github/ contains templates and CI. Assets are added only when needed. The registry is internal, not the final Learning Hub schema.

Chapters use NN-topic/README.md, README.pt-BR.md and README.es.md. Register chapter slugs in scripts/curriculum.json in numeric order and link them in the chapters block. Each module index and chapter has identical localized navigation inside the navigation and navigation-footer blocks, the former after title and locale selector and the latter at the end. Use previous/index/next in that order. The first and last chapters link to the adjacent module indexes (including reserved ones) using Previous module/Next module labels. Only absent directions at the roadmap endpoints use an unlinked dash. Module indexes link to the adjacent indexes and learning path. The validator's navigation_entries and navigation_line functions define canonical destinations and labels. Keep paths stable and do not create empty directories.

- [Learning path](learning-path.md)
- [Quality automation](quality-automation.md)
