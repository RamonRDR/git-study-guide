# Artefactos y caché

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../06-jobs-steps-stages-and-dependencies/README.es.md) · [Índice](../README.es.md) · [Siguiente](../08-environments-variables-and-secrets/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 30 min

**Requisitos previos:** [GitHub](../../github/README.es.md) · [GitLab](../../gitlab/README.es.md) · [Jobs, steps, stages y dependencias](../06-jobs-steps-stages-and-dependencies/README.es.md)

**Objetivo:** Seleccionar artefacto o caché según propósito, duración y confianza.

## Qué es y por qué

Artefacto es salida retenida de job, como informe o paquete, asociada a ejecución y política de retención. Caché es optimización que puede reutilizar datos como dependencias descargadas entre jobs o ejecuciones; puede faltar, caducar o contener datos obsoletos. No dependa de acierto de caché para corrección. GitHub ofrece actions de carga/descarga de artefactos y caché de dependencias; GitLab usa configuración `artifacts` y `cache`. Jobs GitLab pueden descargar artefactos de stages anteriores por defecto; `needs` o `dependencies` cambia selección. En ambas plataformas, permisos, retención y límites varían. Clave de caché puede incorporar SO, versión de herramienta y digest de lockfile; artefacto de release debe asociarse a revisión exacta revisada y comprobar integridad.

## Práctica

Sin conexión: clasifique informe de test, paquete final y dependencias descargadas. Esboce clave como `linux-tool-v1-lockhash` (marcador ficticio) y manifiesto con revisión y checksum del paquete. En pipeline profesional, valide funcionamiento con caché vacía y que artefacto descargado pertenece a ejecución prevista.

## Errores comunes y seguridad

Nunca almacene credenciales en caché ni publique logs sensibles. Trate salidas de jobs no confiables como entradas no confiables; no las ejecute en jobs privilegiados. Si caché corrupta, invalide según política y reconstruya con dependencias verificadas. Si falta artefacto, reproduzca desde revisión revisada en vez de seleccionar artefacto ajeno.

## Ejercicio y autoevaluación

Informe y paquete son artefactos; dependencias descargadas son candidatas a caché. Apruebe si explica fallo de caché, retención, procedencia y confianza.

## Referencia rápida

artifact / cache / retention

## Fuentes oficiales

- <https://docs.github.com/en/actions/concepts/workflows-and-actions/workflow-artifacts>
- <https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching>
- <https://docs.gitlab.com/ci/jobs/job_artifacts/>
- <https://docs.gitlab.com/ci/caching/>
