# Hoja de ruta educativa y de ingeniería

[English](roadmap.md) · [Português](roadmap.pt-BR.md) · [Español](roadmap.es.md)

Fundación aprobada e integrada mediante PR #1 el 25/11/2026. Cambios posteriores requieren revisión y aprobación explícita del mantenedor.

## Currículo (18 módulos)

| Orden | Ruta | Tema | Alcance |
| --- | --- | --- | --- |
| 00 | `getting-started/` | Primeros pasos | Instalación Windows/Linux/macOS, terminal, identidad local, ayuda, VS Code y GUI opcional, primer repositorio y commit; introducción al vocabulario básico. |
| 01 | `fundamentals/` | Historia y fundamentos | Linux, Linus Torvalds, BitKeeper, VCS centralizado/distribuido, Git frente a GitHub/GitLab; por qué importa el historial local. |
| 02 | `git-architecture/` | Arquitectura Git | Working tree, index, repositorio, concepto de remote, snapshots, HEAD, refs y estados de archivos. |
| 03 | `basic-commands/` | Comandos básicos | init, status, add, commit, diff, log, show, rm, mv, config, help, reglas de ignore; inspeccionar antes de cambiar. |
| 04 | `branches/` | Gestión de ramas | Crear desde refs, cambiar, renombrar, comparar, eliminación local, detached HEAD, nombres; aplazar práctica de eliminación remota/tracking a 06. |
| 05 | `merge-and-conflicts/` | Merge y conflictos | Fast-forward, merge commits, squash, rebase, rebase interactivo, resolución de conflictos, abort/continue; reescritura solo local; inspeccionar estado. |
| 06 | `remote-repositories/` | Repositorios remotos | clone, remote, fetch, pull, push, origin/upstream, tracking, divergencia, eliminación remota, refspecs cuando sean útiles; introducir autenticación segura antes de practicar en línea. |
| 07 | `history-and-recovery/` | Historial y recuperación | restore, reset, revert, reflog, stash, cherry-pick, amend, límites de recuperación y reescritura; operaciones destructivas solo en entornos desechables. |
| 08 | `github/` | GitHub | Repositorios, forks, PR, issues, reviews, discussions, releases, projects, rulesets, protección de ramas, código abierto, CLI opcional. |
| 09 | `gitlab/` | GitLab | Projects/groups, MR, issues, review, runners, releases, ramas protegidas, colaboración y comparación con GitHub. |
| 10 | `ci-cd/` | CI/CD y automatización | Integración/entrega/despliegue, GitHub Actions, GitLab CI/CD, YAML, jobs, steps, pipelines, artifacts, cache, environments, secrets, runners y quality gates; permisos seguros primero. |
| 11 | `professional-workflows/` | Flujos profesionales | Git Flow, GitHub Flow, trunk-based, feature branches, Conventional Commits, SemVer, code review, SDD/TDD, asistencia de IA, releases. |
| 12 | `security/` | Seguridad y gobernanza | SSH, HTTPS, tokens, credential managers, secrets, permisos, protección de ramas, rulesets, CODEOWNERS, firma, cadena de suministro, exposición accidental, mínimo privilegio. |
| 13 | `advanced-git/` | Git avanzado | bisect, worktree, submodules, subtree, hooks, rerere, sparse-checkout, partial/shallow clone, blame, grep, archive, bundle y compensaciones. |
| 14 | `git-internals/` | Internals de Git | Blobs, trees, commits, tags, hashes, refs, object database, packfiles, garbage collection, reflogs, porcelain/plumbing. |
| 15 | `command-reference/` | Referencia de comandos | Catálogo consultable por categoría e intención: 120 operaciones distintas en 14 categorías, generadas desde JSON canónico trilingüe; distingue comandos nativos, subcomandos, usos de opciones, flujos y herramientas externas. |
| 16 | `practical-projects/` | Proyectos prácticos | Ocho proyectos integrados: My First Repository; Two Developers, One Project; Merge Conflict Laboratory; The Lost Commit; Open Source Contribution; Automated Quality Pipeline; Release Management; Professional Engineering Workflow. |
| 17 | `exercises/` | Desafíos y entrevistas | Ejercicios, quizzes, troubleshooting, desafíos, entrevistas, simulaciones profesionales y rúbricas de autoevaluación; mapear requisitos primero. |

Política de requisitos: módulo 00 presenta solo vocabulario mínimo para el primer commit; 01–03 profundizan. Módulo 04 enseña ramas locales; práctica de tracking/eliminación remota espera a 06. Explicar recuperación/abort seguros antes de merge o rebase riesgoso en 05, profundizar en 07. Enseñar manejo seguro de credenciales antes de 06 y mínimo privilegio antes de 10; módulo 12 consolida seguridad. Introducir conceptos de objetos/refs antes de tareas avanzadas. Referenciar enseñanza anterior antes de evaluar; los módulos 00–14 tienen lecciones; módulo 15 contiene referencia de comandos; módulos 16–17 están previstos.

## Ingeniería (20 sprints)

| Sprint | Fase | Entrega |
| --- | --- | --- |
| 00 | I | Fundación, auditoría, SDD, ADR, contrato preliminar, índices, README provisional |
| 01 | I | AGENTS, AUTHORS, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, SUPPORT, orientación de IA y plantillas de issue/PR |
| 02 | I | Estructura, navegación, validadores, pruebas, CI; status checks obligatorios tras ejecuciones observadas y aprobación separada |
| 03 | II | Módulos 00–01: primeros pasos, historia y fundamentos |
| 04 | II | Módulos 02–03: arquitectura Git y comandos básicos |
| 05 | II | Módulo 04: gestión de ramas |
| 06 | III | Módulo 05: merge, squash, rebase y conflictos |
| 07 | III | Módulo 06: remotos y colaboración |
| 08 | III | Módulo 07: historial y recuperación |
| 09 | IV | Módulo 08: GitHub |
| 10 | IV | Módulo 09: GitLab |
| 11 | IV | Módulo 10: CI/CD y automatización |
| 12 | IV | Módulo 11: flujos profesionales |
| 13 | IV | Módulo 12: seguridad y gobernanza |
| 13.1 | IV | Complementaria: navegación educativa continua y UX, pruebas de regresión y estándares |
| 14 | V | Módulos 13–14: Git avanzado e internals |
| 15 | V | Módulo 15: referencia de comandos |
| 16 | V | Módulo 16: ocho proyectos prácticos |
| 17 | V | Módulo 17: desafíos, quizzes y entrevistas; piloto de registros estructurados |
| 18 | VI | Finalizar contrato, manifiestos, esquemas, fixtures del consumidor; evaluar playground opcional por separado |
| 19 | VI | Identidad aportada por el mantenedor, README final, QA, entrega |

Fases: I Fundación; II Esenciales; III Colaboración y recuperación; IV Plataformas e ingeniería; V Avanzado y práctica; VI Learning Hub y release. Sprints 00–14 y Sprint complementaria 13.1 integradas mediante PR #1–16; implementación de Sprint 15 preparada para validación y revisión; Sprints 16–19 previstas. Las 20 sprints principales permanecen sin cambios. Dividir sprints grandes en PR enfocados sin cambiar alcance. No confundir numeración de sprints con módulos.

## Documentos relacionados

- [Especificación](specs/project-foundation/specification.es.md)
- [Plan de implementación](specs/project-foundation/implementation-plan.es.md)
- [Criterios de aceptación](specs/project-foundation/acceptance-criteria.es.md)

- [Ruta](learning-path.es.md)
