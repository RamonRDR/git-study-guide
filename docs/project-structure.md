# Project structure

[English](project-structure.md) · [Português](project-structure.pt-BR.md) · [Español](project-structure.es.md)

The root holds governance, the MIT license and 18 stable module indexes. docs/ holds architecture, specifications, translations and engineering guidance. scripts/ contains standard-library validation and the internal curriculum registry; tests/ contains deterministic fixtures. .github/ contains templates and CI. Assets are added only when needed. The registry is internal, not the final Learning Hub schema.

Chapters use NN-topic/README.md, README.pt-BR.md and README.es.md. Register chapter slugs in scripts/curriculum.json in numeric order; link them within the chapters block and use the navigation block for previous, index and next. Endpoints have no link in the absent direction. Module navigation follows the roadmap. Keep paths stable and do not create empty directories.

- [Learning path](learning-path.md)
- [Quality automation](quality-automation.md)
