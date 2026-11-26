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
| T03-01 | Módulos 00–01: primeros pasos, historia y fundamentos (AC-03; depende de T02-01) | Completado ([PR #4](https://github.com/RamonRDR/git-study-guide/pull/4)) |
| T04-01 | Módulos 02–03: arquitectura Git y comandos básicos (AC-04; depende de T03-01) | Completado ([PR #5](https://github.com/RamonRDR/git-study-guide/pull/5)) |
| T05-01 | Módulo 04: gestión de ramas (AC-05; depende de T04-01) | Completado ([PR #6](https://github.com/RamonRDR/git-study-guide/pull/6)) |
| T06-01 | Módulo 05: merge, squash, rebase y conflictos (AC-06; depende de T05-01) | Completada ([PR #7](https://github.com/RamonRDR/git-study-guide/pull/7)) |
| T07-01 | Módulo 06: remotos y colaboración (AC-07; depende de T06-01) | Completada ([PR #8](https://github.com/RamonRDR/git-study-guide/pull/8)) |
| T08-01 | Módulo 07: historial y recuperación (AC-08; depende de T07-01) | Presentada para revisión |
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

Evidencia Sprint 03: [PR #4](https://github.com/RamonRDR/git-study-guide/pull/4), [CI](https://github.com/RamonRDR/git-study-guide/actions/runs/45721626737), [main CI](https://github.com/RamonRDR/git-study-guide/actions/runs/45722633012), [Codex](https://github.com/RamonRDR/git-study-guide/pull/4#issuecomment-7177485378), [squash commit](https://github.com/RamonRDR/git-study-guide/commit/ef430abd68aa476fc9fff898bfb7c1e83b4d55da). Main y eliminación de rama verificadas; CI final aprobado, sin avisos de obsolescencia ni hallazgos pendientes. Instalaciones limpias, macOS e interacción GUI sin probar.

Evidencia Sprint 04: [PR #5](https://github.com/RamonRDR/git-study-guide/pull/5), [CI](https://github.com/RamonRDR/git-study-guide/actions/runs/45723113329), [Codex](https://github.com/RamonRDR/git-study-guide/pull/5#issuecomment-7177929221), [squash commit](https://github.com/RamonRDR/git-study-guide/commit/6695bea89c76fc6a52499ab4f17e9c89cff37fa1), [main CI](https://github.com/RamonRDR/git-study-guide/actions/runs/45724230029). Main y eliminación de rama verificadas; CI final del PR aprobó seis validadores y 24 pruebas por plataforma, sin avisos ni hallazgos pendientes. macOS e interacción GUI sin probar. CI posterior al merge aprobado.

Evidencia Sprint 05: [PR #6](https://github.com/RamonRDR/git-study-guide/pull/6), [CI](https://github.com/RamonRDR/git-study-guide/actions/runs/45724512229), [Codex](https://github.com/RamonRDR/git-study-guide/pull/6#issuecomment-7178166184), [squash commit](https://github.com/RamonRDR/git-study-guide/commit/da1a8b591e9d0349e4991cc5cef99a7a44a47ee0), [main CI](https://github.com/RamonRDR/git-study-guide/actions/runs/45727648558). Main y eliminación de rama verificadas; CI final del PR aprobó seis validadores y 29 pruebas por plataforma, sin avisos ni hallazgos pendientes. macOS e interacción GUI sin probar. CI posterior al merge aprobado.

Evidencia de Sprint 06: [PR #7](https://github.com/RamonRDR/git-study-guide/pull/7), [CI](https://github.com/RamonRDR/git-study-guide/actions/runs/45728027152), [Codex](https://github.com/RamonRDR/git-study-guide/pull/7#issuecomment-7178708117), [auditoría final](https://github.com/RamonRDR/git-study-guide/pull/7#issuecomment-7178951280), [squash commit](https://github.com/RamonRDR/git-study-guide/commit/3dcd547401632bfbfbcb6105d2ab8b5414b13d01), [main CI](https://github.com/RamonRDR/git-study-guide/actions/runs/45730087351). Main y eliminación de rama verificadas; jobs Linux y Windows posteriores al merge aprobados.

Evidencia de Sprint 07: [PR #8](https://github.com/RamonRDR/git-study-guide/pull/8), [CI](https://github.com/RamonRDR/git-study-guide/actions/runs/45730675180), [Codex](https://github.com/RamonRDR/git-study-guide/pull/8#issuecomment-7179056521), [auditoría final](https://github.com/RamonRDR/git-study-guide/pull/8#issuecomment-7179385728), [squash commit](https://github.com/RamonRDR/git-study-guide/commit/e087764de306010c76f1ee51bcdfe642a2bfab9e), [main CI](https://github.com/RamonRDR/git-study-guide/actions/runs/45733554621). Main y eliminación de rama verificadas; tree revisada idéntica; CI final y posterior al merge aprobaron 45 pruebas y seis validadores por plataforma, sin warnings identificados.
