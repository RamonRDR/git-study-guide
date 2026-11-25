# Plan de implementación

[English](implementation-plan.md) · [Português](implementation-plan.pt-BR.md) · [Español](implementation-plan.es.md)

Fundación aprobada e integrada mediante PR #1 el 25/11/2026. Cambios posteriores requieren revisión y aprobación explícita del mantenedor.

## Secuencia de entregas

| Sprint | Branch | Dependencia | Entrega |
| --- | --- | --- | --- |
| 00 | `docs/project-foundation` | — | Fundación, auditoría, SDD, ADR, contrato preliminar, índices, README provisional |
| 01 | `docs/governance` | 00 | AGENTS, AUTHORS, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, SUPPORT, orientación de IA y plantillas de issue/PR |
| 02 | `feat/quality-automation` | 01 | Estructura, navegación, validadores, pruebas, CI; status checks obligatorios tras ejecuciones observadas y aprobación separada |
| 03 | `feat/getting-started` | 02 | Módulos 00–01: primeros pasos, historia y fundamentos |
| 04 | `feat/git-architecture` | 03 | Módulos 02–03: arquitectura Git y comandos básicos |
| 05 | `feat/branch-management` | 04 | Módulo 04: gestión de ramas |
| 06 | `feat/merge-and-conflicts` | 05 | Módulo 05: merge, squash, rebase y conflictos |
| 07 | `feat/remote-repositories` | 06 | Módulo 06: remotos y colaboración |
| 08 | `feat/history-and-recovery` | 07 | Módulo 07: historial y recuperación |
| 09 | `feat/github` | 08 | Módulo 08: GitHub |
| 10 | `feat/gitlab` | 09 | Módulo 09: GitLab |
| 11 | `feat/ci-cd` | 10 | Módulo 10: CI/CD y automatización |
| 12 | `feat/professional-workflows` | 11 | Módulo 11: flujos profesionales |
| 13 | `feat/security-governance` | 12 | Módulo 12: seguridad y gobernanza |
| 14 | `feat/advanced-git` | 13 | Módulos 13–14: Git avanzado e internals |
| 15 | `feat/command-reference` | 14 | Módulo 15: referencia de comandos |
| 16 | `feat/practical-projects` | 15 | Módulo 16: ocho proyectos prácticos |
| 17 | `feat/challenges-interviews` | 16 | Módulo 17: desafíos, quizzes y entrevistas; piloto de registros estructurados |
| 18 | `feat/learning-hub-contract` | 17 | Finalizar contrato, manifiestos, esquemas, fixtures del consumidor; evaluar playground opcional por separado |
| 19 | `docs/release-handoff` | 18 | Identidad aportada por el mantenedor, README final, QA, entrega |

## Estructura y flujo

Usar README.md en raíz y docs/localized/README.{pt-BR,es}.md; traducciones de gobernanza de raíz en docs/localized/. Carpetas de módulos y capítulos usan README.md, README.pt-BR.md, README.es.md, examples/ compartido cuando haga falta. Arquitectura y specs con traducciones hermanas. assets/, scripts/, tests/, .github/ y carpetas curriculares solo cuando sean útiles. No crear directorios vacíos. Activos visuales oficiales aplazados. Antes de cada sprint, leer main e instrucciones aplicables, delimitar alcance, crear rama desde main actual, implementar idiomas, ejecutar checks disponibles, revisar cada archivo, inspeccionar privacidad, abrir PR, verificar CI y solicitar Codex Review si disponible, tratar hallazgos y revalidar último SHA, registrar evidencia, obtener aprobación del mantenedor, squash merge, verificar main y eliminación de rama, preparar entrega.

## Estrategia de validación

Bootstrap Sprint 00: solo checks documentales, sin CI. Sprint 02 añade presencia de idiomas, enlaces, navegación, estructura, ejemplos en allowlist, detección de secretos y jobs Linux/Windows; sprints siguientes añaden pruebas deterministas de estado/conflicto/recuperación y validación de esquema/ID/referencia cuando existan registros. Usar biblioteca estándar cuando baste, directorios temporales y configuración Git aislada; verificar refs, index, árbol y archivos en vez de hashes frágiles o salida localizada. Nunca ejecutar aportes arbitrarios de estudiantes en CI privilegiada. Checks obligatorios requieren autorización separada tras conocer nombres/ejecuciones reales.

## Documentos relacionados

- [Constitution](../constitution.es.md)
- [Especificación](specification.es.md)
- [Tareas](tasks.es.md)
- [Criterios de aceptación](acceptance-criteria.es.md)
- [Hoja de ruta](../../roadmap.es.md)
