# Controles de calidad y diagnóstico

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../08-environments-variables-and-secrets/README.es.md) · [Índice](../README.es.md) · [Siguiente](../10-integrated-quality-pipeline-lab/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 35 min

**Requisitos previos:** [GitHub](../../github/README.es.md) · [GitLab](../../gitlab/README.es.md) · [Entornos, variables y secretos](../08-environments-variables-and-secrets/README.es.md)

**Objetivo:** Decidir si revisión puede integrarse con evidencia, no solo icono verde.

## Qué es y por qué

Control de calidad es condición de política que debe satisfacerse antes de integración o promoción. Ejemplos: lint obligatorio (comprobaciones estáticas), tests, review, checks de seguridad y aprobación autorizada. Rulesets GitHub pueden exigir checks nombrados; merge checks GitLab pueden exigir pipeline exitoso y discusiones resueltas cuando se configuran. Capacidades varían por plan y configuración. Workflow puede estar ausente, en cola, pendiente, ejecutando, fallido, cancelado, omitido o exitoso. Políticas pueden tratar algunos resultados skipped/neutral como satisfactorios, pero no prueban ejecución de tests. Distinga error de configuración, fallo de infraestructura y aserción fallida. Verifique head/base o resultado de merge exacto, logs, nombres de jobs exigidos y política; no infiera de ejecución previa. Timeout no es aprobación.

## Práctica

Sin conexión: revisión A pasó; B cambia configuración de validación; B Linux pasa pero Windows falla. Escriba checklist pre-merge: revisión exacta, jobs esperados, logs, hallazgos, resolución de discusiones, base actual y autorización. Decida no integrar B, inspeccione fallo Windows, corrija, revise nueva revisión y repita ambos jobs. Opcional: inspeccione logs públicos CI solo lectura sin cuenta cuando disponibles.

## Errores comunes y seguridad

No desactive controles, suprima fallos ni repita indefinidamente para ocultar no determinismo. Oculte diagnósticos sensibles; informe límites de reproducción y escale problemas de infraestructura. Corrija causa raíz y preserve evidencias.

## Ejercicio y autoevaluación

B está bloqueada; A no evidencia B. Apruebe si checklist incluye ambas plataformas, revisión exacta, resultados significativos y autorización humana.

## Referencia rápida

required check / revision / log

## Fuentes oficiales

- <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets>
- <https://docs.gitlab.com/user/project/merge_requests/auto_merge/>
- <https://docs.gitlab.com/ci/pipelines/>
