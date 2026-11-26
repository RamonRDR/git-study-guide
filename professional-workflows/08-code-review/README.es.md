# Code review y preparación para merge

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../07-semantic-versioning/README.es.md) · [Índice](../README.es.md) · [Siguiente](../09-spec-driven-development/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 40 min

**Requisitos previos:** [CI/CD](../../ci-cd/README.es.md) · [Versionado semántico](../07-semantic-versioning/README.es.md)

**Objetivo:** Revisar intención, comportamiento, riesgo y evidencia de revisión exacta.

## Qué es y por qué

Code review evalúa propuesta contra intención, comportamiento, mantenibilidad, seguridad y tests. Hallazgo útil indica ubicación, problema observado, impacto y dirección sugerida; distinga defectos bloqueantes de sugerencias. Revise diff enfocado, no solo icono verde. Compare head con base y compruebe logs reales y alcance de tests. GitHub/GitLab ofrecen discusiones y aprobaciones; imposición, descarte de aprobaciones obsoletas y revisores obligatorios dependen de configuración. Autor atiende hallazgos y registra evidencia; revisor verifica corrección antes de cerrar discusiones relevantes. Autorización de merge es distinta de review automatizado exitoso.

## Práctica

PR dice añadir disponibilidad, pero cambia `catalog.txt` de `status: draft` a `status: redy`. Test solo comprueba existencia. Escriba comentario bloqueante pidiendo campo exacto y tests fallido/exitoso significativos; sugerencia de nombre opcional aparte. Autor corrige valor y test. Registre nueva revisión, CI en entornos previstos, resolución y aprobación humana; use capítulo 13 para práctica local de diff.

## Riesgos y recuperación

No apruebe por cortesía, título, salida de IA o SHA anterior. Nunca silencie fallos ni resuelva discusión solo para liberar merge. Si escapa regresión, registre PR correctivo, repita checks y mejore cobertura sin culpar personas.

## Ejercicio y autoevaluación

Bloquee merge: comportamiento difiere de requisito y check no detecta. Pruebe revisión corregida exacta; autorización humana independiente aún necesaria por política del guía.

## Referencia rápida

diff / head SHA / review / approval / CI

## Fuentes

- <https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/reviewing-proposed-changes-in-a-pull-request>
- <https://docs.gitlab.com/user/project/merge_requests/reviews/>
