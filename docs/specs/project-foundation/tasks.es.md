# Registro de tareas

[English](tasks.md) · [Português](tasks.pt-BR.md) · [Español](tasks.es.md)

Fundación aprobada e integrada mediante PR #1 el 25/11/2026. Cambios posteriores requieren revisión y aprobación explícita del mantenedor.

| Task | Descripción | Estado |
| --- | --- | --- |
| T00-01 | Auditar repositorios, ramas, ruleset y referencia Python | Auditoría de lectura completada; ver auditoría |
| T00-02 | Elaborar Constitution, specification, plan, tareas, criterios y ADR trilingües | Completado ([PR #1](https://github.com/RamonRDR/git-study-guide/pull/1)) |
| T00-03 | Elaborar contrato, guías relacionadas, índices, hoja de ruta y README provisional | Completado ([PR #1](https://github.com/RamonRDR/git-study-guide/pull/1)) |
| T00-04 | Validar estructura de idiomas, enlaces, alineación y último PR; solicitar Codex Review | Completado ([PR #1](https://github.com/RamonRDR/git-study-guide/pull/1)) |
| T00-05 | Aprobación del mantenedor, squash merge, verificar main | Completado ([PR #1](https://github.com/RamonRDR/git-study-guide/pull/1)) |
| T01-01 | AGENTS, AUTHORS, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, SUPPORT, orientación de IA y plantillas de issue/PR (AC-01; depende de T00-05) | Completado ([PR #2](https://github.com/RamonRDR/git-study-guide/pull/2)) |
| T02-01 | Estructura, navegación, validadores, pruebas, CI; status checks obligatorios tras ejecuciones observadas y aprobación separada (AC-02; depende de T01-01) | Completado ([PR #3](https://github.com/RamonRDR/git-study-guide/pull/3)) |
| T03-01 | Módulos 00–01: primeros pasos, historia y fundamentos (AC-03; depende de T02-01) | Presentado para revisión |
| T04-01 | Módulos 02–03: arquitectura Git y comandos básicos (AC-04; depende de T03-01) | Pendiente |
| T05-01 | Módulo 04: gestión de ramas (AC-05; depende de T04-01) | Pendiente |
| T06-01 | Módulo 05: merge, squash, rebase y conflictos (AC-06; depende de T05-01) | Pendiente |
| T07-01 | Módulo 06: remotos y colaboración (AC-07; depende de T06-01) | Pendiente |
| T08-01 | Módulo 07: historial y recuperación (AC-08; depende de T07-01) | Pendiente |
| T09-01 | Módulo 08: GitHub (AC-09; depende de T08-01) | Pendiente |
| T10-01 | Módulo 09: GitLab (AC-10; depende de T09-01) | Pendiente |
| T11-01 | Módulo 10: CI/CD y automatización (AC-11; depende de T10-01) | Pendiente |
| T12-01 | Módulo 11: flujos profesionales (AC-12; depende de T11-01) | Pendiente |
| T13-01 | Módulo 12: seguridad y gobernanza (AC-13; depende de T12-01) | Pendiente |
| T14-01 | Módulos 13–14: Git avanzado e internals (AC-14; depende de T13-01) | Pendiente |
| T15-01 | Módulo 15: referencia de comandos (AC-15; depende de T14-01) | Pendiente |
| T16-01 | Módulo 16: ocho proyectos prácticos (AC-16; depende de T15-01) | Pendiente |
| T17-01 | Módulo 17: desafíos, quizzes y entrevistas; piloto de registros estructurados (AC-17; depende de T16-01) | Pendiente |
| T18-01 | Finalizar contrato, manifiestos, esquemas, fixtures del consumidor; evaluar playground opcional por separado (AC-18; depende de T17-01) | Pendiente |
| T19-01 | Identidad aportada por el mantenedor, README final, QA, entrega (AC-19; depende de T18-01) | Pendiente |

Actualizar evidencia en cada PR enfocado. Entrega propuesta o PR abierto no es finalización. Usar enlaces reales de checks/reviews y SHA; tras merge aprobado, verificar main y eliminación de rama, registrar entrega en el siguiente cambio autorizado si hace falta.


Evidencia Sprint 00: [Codex](https://github.com/RamonRDR/git-study-guide/pull/1#issuecomment-7174894634), [validation](https://github.com/RamonRDR/git-study-guide/pull/1#issuecomment-7174867993), [squash commit](https://github.com/RamonRDR/git-study-guide/commit/38fd45048a036ef377a05ec8429e624464841159). Mantenedor aprobó; main y eliminación de rama verificadas; CI ausente según plan.

## Documentos relacionados

- [Plan de implementación](implementation-plan.es.md)
- [Criterios de aceptación](acceptance-criteria.es.md)
- [Auditoría inicial](audit.es.md)

Evidencia Sprint 01: [PR #2](https://github.com/RamonRDR/git-study-guide/pull/2), [Codex](https://github.com/RamonRDR/git-study-guide/pull/2#issuecomment-7176325295), [squash commit](https://github.com/RamonRDR/git-study-guide/commit/df139992ae109145184a4de86b2a95b7e1187e0b). Última revisión sin hallazgos; main y eliminación de rama verificadas.

Evidencia Sprint 02: [PR #3](https://github.com/RamonRDR/git-study-guide/pull/3), [CI](https://github.com/RamonRDR/git-study-guide/actions/runs/45717835244), [main CI](https://github.com/RamonRDR/git-study-guide/actions/runs/45718411371), [Codex](https://github.com/RamonRDR/git-study-guide/pull/3#issuecomment-7176975402), [ruleset](https://github.com/RamonRDR/git-study-guide/rules/28108699). Main y eliminación de rama verificadas; checks Linux y Windows obligatorios con política estricta de actualización tras autorización del mantenedor.
