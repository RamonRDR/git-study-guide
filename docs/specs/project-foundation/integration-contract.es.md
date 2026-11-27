# Contrato de integración Learning Hub

[English](integration-contract.md) · [Português](integration-contract.pt-BR.md) · [Español](integration-contract.es.md)

Contrato 1.0.0 propuesto para revisión de Sprint 18. Alcance: solo Git Study Guide. Repositorio público autoritativo; usa JSON/Markdown UTF-8 en build time, nunca scraping HTML o API GitHub por visitante. Consumidor mantiene lock externo aprobado con revision SHA-1 completo de 40 caracteres, guide_id=git-study-guide, manifest_version=1.0.0, assessment_version=1 y command_catalog_version=1. Solo versiones exactas; rechaza revisiones ausentes, no admitidas o mezcladas. Sin SHA autoembebido; selecciona commit aprobado tras merge y CI main. No se crea etiqueta release ni pin activo del sitio aquí.

## Versión y transporte

curriculum/manifest.json es inventario generado de 18 módulos y 141 capítulos (423 rutas localizadas). Títulos de módulos proceden de H1 de índices localizados; títulos de capítulos de rótulos existentes de índices localizados. IDs congelados son slug del módulo o module.slug (incluido slug numerado existente); nunca renumeres rutas ni reutilices IDs cuando cambie orden. Órdenes contiguos base cero entre hermanos. previous_id/next_id globales recorren capítulos con null en extremos; navegación Markdown conserva índices de módulos adyacentes. Títulos y rutas tienen exactamente en (predeterminado), pt-BR y es. Kinds: lesson, reference, project y assessment. Assets y resources referencian archivos rastreados; resources no es allowlist de ejecución.

## Fuentes canónicas y relaciones

Cuatro bancos referencian records.json existentes (schema_version entero 1); catálogo tiene 14 categorías, registros de categorías e intenciones y envolturas catalog.json (schema_version entero 1). Sin duplicar cuerpos. Validadores assessment-pilot y command-catalog siguen autoritativos para semántica completa. quiz_ids, exercise_ids e interview_ids identifican capítulo del banco y relaciones documentadas de prerrequisitos, no propiedad inferida de capítulo; mock_ids identifica solo capítulo de simulacros. command_ids identifica categoría propietaria y capítulos relacionados documentados. Orden canónico de bancos. Reconstrucción exacta valida relaciones; simulacros resuelven IDs de cuestionario/desafío/entrevista y dificultad igual. Conteos de revisión: 36 cuestionarios, 12 desafíos, 24 entrevistas, tres simulacros, 120 operaciones. Todos públicos, soluciones y rúbricas visibles.

## Compatibilidad y migración

Comparado en modo solo lectura con commit Python Study Guide a8a264f9f36ec276f0ad8e35f10f2d76f82fe211. Convenciones comunes: mapas de idiomas, orden explícito, revisión inmutable, relaciones tipadas, rutas seguras, rechazo de versiones desconocidas, espacio de nombres, autoevaluación orientativa. Manifesto Git añade guide_id, command_catalog, kinds reference/assessment y command_ids; descriptores apuntan registros agregados en vez de índices Python. Tipo quiz Git single-choice y answer cadena mapean explícitamente a multiple_choice y answer.choice_id si se adaptan a UI estilo Python; listas ordenadas de mapas de idiomas pueden transponerse a arrays por idioma. Prerrequisitos Git son muchos-a-muchos; no inventes propiedad chapter_id, XP o campos de prueba Python. Conserva IDs y versiones existentes. No importes registros Git como válidos por esquema Python; usa adaptador específico. Sin cambios en Python o Learning Hub.

## Procedimiento y seguridad del consumidor

Cuatro esquemas estructurales Draft 2020-12 documentan manifiesto, bancos, catálogo y lock externo. Validador Python sin dependencias aplica JSON estricto (claves duplicadas, números no finitos y tokens fraccionarios rechazados), manifiesto regenerado exacto, inventario idiomas/rutas, semántica bancos, relaciones tipadas, conteos y versiones. Validación estructural JSON Schema sola no demuestra existencia, unicidad por ID, semántica o integridad referencial; usa checks estructurales y semánticos en integraciones. Autoría: prepara cambios fuente, ejecuta python scripts/learning_hub_contract.py --write, prepara manifiesto, luego python scripts/validate.py --check learning-hub-contract y suite completa. Sin red ni nueva dependencia.

Consumidor de referencia confiable scripts/learning_hub_consumer.py recibe lock externo y base de objetos Git SHA-1 local confiable y completa para instantánea. Verifica commit solicitado, desactiva objetos de reemplazo y protocolos de red, lee blobs regulares 100644 por ID sin filtros checkout, comprueba tamaños y hashes Git, exporta a staging nuevo aislado, rechaza traversal, symlinks, entradas ejecutables/submódulos, colisiones, archivos ausentes/extra/modificados y compara igualdad JSON de esquemas soportados confiables fuera de instantánea. Usa validadores confiables, nunca importa código de instantánea. Límites: 3000 archivos, 32 MiB total, 60 s por llamada Git. Valida candidato antes de adoptar pin; ante fallo conserva pin anterior aprobado; rollback es reseleccionar SHA completo. Pruebas usan commit real seleccionado y datos sintéticos de dos revisiones, no sitio real ni lanzamiento firmado independientemente. Confía base de objetos, binario Git y staging privado; sin verificación de firma ni sandbox de filesystem concurrente hostil. Renderizador debe sanear Markdown/HTML, enlaces, assets y URLs; sin ejecución de contenido arbitrario.

## Responsabilidad y ejecución

Guía posee contenido, metadatos, soluciones públicas, QA de referencia y validación de esquema. Sitio posee UI/renderizado seguro, accesibilidad, progreso, aislamiento y despliegue. Proyectos/desafíos Git nativos son local_only con razones localizadas; otros capítulos unverified. Browser_compatible no se admite en contrato v1; ningún runtime validado o introducido. Cuestionarios comparan IDs exactos; entrevistas/simulacros usan rúbrica manual explícita, nunca corrección IA. Predicados de desafío son fixtures QA locales confiables, no ejecutor arbitrario de estudiantes; estado final no demuestra seguridad de acciones intermedias. Progreso navegador específico del dispositivo y puede borrarse. Véase decisión playground opcional.

## Documentos relacionados

- [Manifest](../../../curriculum/manifest.json)
- [Manifest schema](../../../schemas/curriculum-manifest.schema.json)
- [Assessment schema](../../../schemas/assessment-bank.schema.json)
- [Command catalog schema](../../../schemas/command-catalog.schema.json)
- [Revision lock schema](../../../schemas/revision-lock.schema.json)
- [Reference consumer](../../../scripts/learning_hub_consumer.py)
- [Specification](specification.es.md)
- [ADR 0004](../../adr/0004-learning-hub-integration.es.md)
- [ADR 0006](../../adr/0006-browser-playground.es.md)
- [Python reference snapshot](https://github.com/RamonRDR/python-study-guide/blob/a8a264f9f36ec276f0ad8e35f10f2d76f82fe211/docs/specs/learning-hub-foundation/integration-contract.md)
