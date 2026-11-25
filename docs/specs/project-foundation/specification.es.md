# Especificación de la fundación

[English](specification.md) · [Português](specification.pt-BR.md) · [Español](specification.es.md)

Propuesta para revisión del mantenedor; no autoriza iniciar el Sprint 01.

Objetivo: Git Study Guide público, práctico, MIT, desde principiante hasta ingeniería avanzada. Baseline main: b4bd782519ebc8e52e6751362443aa634e86e56d. Referencia Python: 9102bbbf8f8dd846f2fb9682dd3f55bcacc10c95.

## Requisitos funcionales

- FR-01 — Publicar contenido independiente EN/PT-BR/ES con selectores de idioma, navegación anterior/índice/siguiente, rutas estables y requisitos explícitos. Seguir la hoja de ruta sin exigir Python.
- FR-02 — Enseñar historia, arquitectura, operaciones locales, ramas, remotos, estrategias de merge, recuperación, plataformas, CI/CD, flujos profesionales, seguridad e internals. Distinguir Git nativo de funciones de alojamiento y explicar cambios de estado.
- FR-03 — Cada lección aplicable incluye objetivo, nivel, requisitos, tiempo de estudio, definición, razón/problema, sintaxis, cuándo usar/evitar, relaciones, internals, ejemplos básico/profesional, errores, riesgo/recuperación, ejercicio, checklist, referencia rápida y fuentes oficiales. Adaptar con justificación; no introducir términos sin definir.
- FR-04 — Catalogar 100+ comandos/operaciones relevantes; ID estable, categoría, objetivo, sintaxis, requisitos, opciones, uso/evitar, ejemplo y resultado, estado afectado, efectos secundarios, riesgo, alternativas, errores, recuperación, versión mínima cuando corresponda, referencias oficiales y etiquetas de intención. No inflar la cantidad de subcomandos distintos.
- FR-05 — Usar diagramas accesibles con explicaciones localizadas para estado, refs, historial, branch/merge/rebase, divergencia, cherry-pick, reflog, objetos, colaboración y CI/CD. Evaluar Mermaid/SVG; validar topología y alternativas textuales.
- FR-06 — Ofrecer ocho proyectos prácticos con repositorios temporales, origin bare y clones Alice/Bob; actividades exclusivas de plataformas opcionales. Incluir preparación, condiciones de éxito, inspección, limpieza y recuperación segura.
- FR-07 — Proporcionar quizzes, desafíos y registros de entrevistas con IDs estables, tres idiomas, requisitos, pistas progresivas, respuestas de referencia, comprobaciones deterministas de estado y rúbricas objetivas; respuestas abiertas mediante autoevaluación.
- FR-08 — Implementar gobernanza, orientación trilingüe de desarrollo asistido por IA, plantillas y quality gates automatizados; README provisional ahora, identidad y README final en Sprint 19 con insignias verificables.
- FR-09 — Proporcionar manifiesto versionado, esquemas, mapas de idiomas, IDs estables, rutas relativas seguras, capacidades de ejercicios, fixtures validadas y entrega de revisión aprobada; alinear con contrato Python sin decisiones unilaterales de esquema universal.

## Requisitos no funcionales

- NFR-01 — Costo adicional cero; sin servicios de pago ni IA obligatoria. Verificar límites gratuitos antes de depender de servicios externos.
- NFR-02 — Paridad conceptual en toda documentación pública, incluidas plantillas; preservar MIT, autoría y rutas publicadas; sin información privada.
- NFR-03 — Validar enlaces, estructura, navegación, ejemplos, estado, conflictos, recuperación, Linux/Windows, esquemas, IDs, referencias y secretos; macOS cuando se justifique. Usar ejemplos confiables en allowlist, directorios temporales y mínimo privilegio; sin CI privilegiada no confiable.
- NFR-04 — Sin runtime obligatorio del sitio, evaluación por IA, servidores de pago ni ejecución arbitraria privilegiada. Playground en navegador opcional y no verificado hasta su evaluación.
- NFR-05 — Revisar y registrar evidencia real de validación; nunca inventar métricas, aprobaciones ni resultados. Mantener ejemplos originales e independencia de proveedores oficiales.

## Alcance y fuentes

Sprint 00: solo fundación, sin lecciones, sitio, runtime, logotipo, otros repositorios, cambios administrativos ni cambios en Python. Sprints siguientes requieren dependencias aprobadas. Priorizar [documentación Git](https://git-scm.com/docs), [Pro Git](https://git-scm.com/book/en/v2), [GitHub Docs](https://docs.github.com/) y [GitLab Docs](https://docs.gitlab.com/); verificar hechos cambiantes antes de publicar. Guías futuras y plantilla reutilizable se aplazan hasta la madurez de Python y Git.

## Documentos relacionados

- [Constitution](../constitution.es.md)
- [Plan de implementación](implementation-plan.es.md)
- [Tareas](tasks.es.md)
- [Criterios de aceptación](acceptance-criteria.es.md)
- [Contrato de integración](integration-contract.es.md)
- [Guías relacionadas](related-guides.es.md)
- [Decisiones arquitectónicas](../../adr/README.es.md)
- [Hoja de ruta](../../roadmap.es.md)
- [Auditoría inicial](audit.es.md)
