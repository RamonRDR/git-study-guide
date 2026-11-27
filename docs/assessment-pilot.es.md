# Esquema del piloto de evaluaciones

[English](assessment-pilot.md) · [Português](assessment-pilot.pt-BR.md) · [Español](assessment-pilot.es.md)

Piloto interno Sprint 17, schema_version 1. No es contrato publicado Learning Hub. Cuatro archivos canónicos en exercises/ almacenan envoltura con schema_version, kind y records. Inglés es primario; cada texto de estudiante es mapa no vacío exactamente en, pt-BR y es. IDs son tokens minúsculos con guiones prefijados por tipo. Dificultad easy, medium o hard. Prerrequisitos nombran rutas anteriores de módulo/capítulo registrados. Sin contenido ejecutable ni credenciales. Orden de registros es orden de presentación.

## Campos comunes

id, difficulty, prerequisites, title, prompt, hints, explanation. Pistas son mapas localizados ordenados; prerrequisitos resuelven capítulos existentes fuera de módulo 17.

- Cuestionario: type single-choice, tres choices con IDs únicos estables y texto localizado, answer es ID exacto. Sin comparación aproximada.
- Desafío: estimated_minutes, setup, solution (pasos localizados ordenados), execution=local_only, execution_reason, checks. Preparación apunta fixture aislada nueva; soluciones son instrucciones, no cadenas ejecutables. Checks son predicados de estado tipados permitidos; sin rutas, opciones ni comandos arbitrarios.
- Entrevista: expected_answer, rubric, follow_ups. Un punto por criterio cumplido, cero en otro caso; solo autoevaluación.
- Simulacro: duration_minutes, quiz_ids, challenge_ids, interview_ids, rubric. Referencias resuelven tipo correcto y misma dificultad. Cuatro cuestionarios (4 puntos), un desafío (2), dos entrevistas (4), total 10.

Checks de estado usan estado limpio, rama actual, bytes exactos confirmados/index/trabajo, rutas rastreadas/no rastreadas, igualdad/desigualdad de refs, ascendencia, igualdad de tree, conteo de padres/commits, tipo de objeto etiqueta y entradas no fusionadas. Cada predicado tiene conjunto exacto de campos permitidos; nombres/valores de fixture restringidos. assessment_state acepta solo callbacks controlados de fixtures QA confiables; no es sandbox ni ejecutor público. Check final no demuestra camino seguido por estudiante ni seguridad de operación intermedia; usa evidencia manual cuando se requiera. No evalúes repos no confiables ni ejecutes código de estudiante. Ejecución navegador y contrato final quedan para Sprint 18.

El check assessment-pilot verifica cuatro bancos versionados, conteos exactos por dificultad, IDs globalmente únicos, prerrequisitos y referencias de simulacros válidos, campos localizados, opciones, respuestas, predicados de estado permitidos e igualdad con Markdown generado. Edita records.json, prepara JSON y currículo, ejecuta python scripts/render_assessments.py --write; prepara páginas generadas y ejecuta python scripts/validate.py --check assessment-pilot y todos checks/pruebas. Los 12 escenarios fijos QA ejercitan estados Git válidos e incorrectos representativos. Ningún evaluador ejecuta entregas de estudiantes ni lee repos arbitrarios; solo fixtures desechables confiables. Validación estructural no demuestra traducción semántica ni precisión educativa.

- [Module 17](../exercises/README.es.md)
- [Integration contract](specs/project-foundation/integration-contract.es.md)
- [Quality automation](quality-automation.es.md)
