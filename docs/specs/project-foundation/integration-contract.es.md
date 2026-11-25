# Contrato preliminar de integración Learning Hub

[English](integration-contract.md) · [Português](integration-contract.pt-BR.md) · [Español](integration-contract.es.md)

Dirección normativa preliminar para pilotos; sin esquema publicado ni consumidor implementado. Finalizar en Sprint 18 tras pilotos del Sprint 17 y revisión coordinada con Python Study Guide.

## Versión y transporte

Importar Markdown/JSON UTF-8 en build time desde un SHA Git inmutable aprobado. Registrar revision y schema_version; rechazar versiones major desconocidas, registros inválidos y revisiones mezcladas. Sin scraping HTML ni API GitHub por visitante. Default en, soportados en/pt-BR/es; campos visibles requieren mapas de idiomas. IDs ASCII minúsculos con puntos/guiones, estables independientemente del orden; únicos por tipo de entidad. Tupla propuesta en consumidor (guide_id, entity_type, id), guide_id=git-study-guide; no cambia unilateralmente contrato Python. Órdenes explícitas no negativas únicas entre hermanos. Solo rutas POSIX relativas al repositorio: rechazar traversal, rutas absolutas, barras invertidas, esquemas y escapes por symlink; verificar existencia, resolver en misma revisión, sanitizar Markdown/HTML. Anterior/siguiente sigue orden curricular, null en extremos.

## Campos propuestos

| Entity | Fields |
| --- | --- |
| Curriculum | schema_version, default_locale, supported_locales, modules |
| Module | id, order, slug, title, index, chapters |
| Chapter | id, order, slug, title, content, assets, previous_id, next_id, exercise_ids, quiz_ids, interview_ids, execution |
| Quiz | id, chapter_id, difficulty, type, prompt, choices, answer, explanation, hints, xp |
| Exercise | id, chapter_id, difficulty, estimated_minutes, title, prompt, concepts, constraints, examples, starter_path or starter text, hints, solution_path, explanation, tests, execution, allowed_dependencies |
| Interview question | id, topic, level, prompt, expected_answer, explanation, intent, common_errors, follow_ups, examples, rubric |
| Mock | id, level, duration_minutes, question_ids, exercise_ids, scoring rubric |
| Command entry | id, category, command, intent_tags, purpose, syntax, prerequisites, options, examples, expected_state, risk, recovery, references |

Campos candidatos, no un esquema. Preservar nombres comunes compatibles de Python; prosa localizada incluye títulos, prompts, opciones, pistas, explicaciones y rúbricas. Dificultad easy/medium/hard. Tipos de quiz objetivo y valores aceptados explícitos; XP solo orientativo. Registros de comandos complementan campos FR-04. Pruebas Git describen preparación, operaciones permitidas, estado esperado y límites; comparar refs, ascendencia, index, archivos rastreados/no rastreados y contenidos según corresponda, no hashes incidentales, horas, defaults de rama o salida localizada. Probar estados incorrectos representativos. Preguntas abiertas usan respuestas de referencia y autoevaluación; soluciones públicas son inspeccionables.

## Ejecución y responsabilidades

Mantener valores de ejecución compatibles con Python: browser_compatible (solo tras validar runtime fijado), local_only (motivo obligatorio), unverified (default, sin ejecución automática en navegador). Proponer metadatos opcionales Git para simulación frente a Git real y actividades con cuenta; finalizar tras piloto, nunca inferir soporte. Labs Git nativos siguen locales; sin sitio/runtime aquí. Evaluación de playground debe abordar fidelidad, operaciones soportadas, seguridad, aislamiento, persistencia, accesibilidad, compatibilidad, cancelación/límites de tiempo/salida y costo adicional cero. Worker solo no es frontera de seguridad. Nunca ejecutar comandos arbitrarios privilegiados ni evaluación semántica por IA. Guía se ocupa de contenido, metadatos, soluciones, pruebas y validación; sitio de renderizado seguro, UI, aislamiento de runtime, progreso, accesibilidad y despliegue. Progreso local del navegador es específico del dispositivo y puede borrarse. Sin sincronización obligatoria vía backend.

Referencia (snapshot consultado): [Python contract](https://github.com/RamonRDR/python-study-guide/blob/9102bbbf8f8dd846f2fb9682dd3f55bcacc10c95/docs/specs/learning-hub-foundation/integration-contract.md).

## Documentos relacionados

- [Especificación](specification.es.md)
- [Decisiones arquitectónicas](../../adr/README.es.md)
