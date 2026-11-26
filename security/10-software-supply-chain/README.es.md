# Seguridad de cadena de suministro de software

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../09-commit-and-tag-signing/README.es.md) · [Índice](../README.es.md) · [Siguiente](../11-credential-exposure-and-incident-response/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 45 min

**Requisitos previos:** [Flujos profesionales](../../professional-workflows/README.es.md) · [Firma de commits y tags](../09-commit-and-tag-signing/README.es.md)

**Objetivo:** Identificar controles de cadena de suministro y riesgos residuales.

## Qué es y por qué

Cadena incluye fuente, dependencias, herramientas build, actions CI, imágenes, runners, registros y artefactos distribuidos. Lockfiles registran versiones resueltas; no prueban seguridad. SBOM inventaría componentes; procedencia describe dónde/cómo se construyó artefacto; atestación es declaración verificable sobre objeto. Verifique fuentes confiables, revise dependencias, fije actions GitHub a SHA completos verificados e imágenes a digests verificados cuando viable, actualice periódicamente mediante cambios revisados. Fijación no elimina vulnerabilidades ni garantiza transitivas seguras. Use mínimo privilegio y CI no confiable aislado; no despliegue artefactos de jobs no confiables sin frontera verificada.

[Automatización de calidad](../../docs/quality-automation.es.md)

## Práctica

Dibuje fuente -> build revisado -> artefacto -> promoción verificada. En PR ficticio cambiando action de SHA revisado a tag móvil, identifique referencia mutable y solicite revisión verificada independientemente. Añada inventario, checksum/procedencia esperados y responsable de actualización a checklist. Lea política de quality workflow del guía sin modificar.

## Riesgos y recuperación

No ejecute dependencias no revisadas, CI privilegiado de terceros ni artefactos arbitrarios. Si dependencia comprometida, detenga jobs/releases afectados, siga incidente, verifique reemplazo y reconstruya con entradas confiables. Nunca afirme que scanner prueba ausencia de vulnerabilidades.

## Ejercicio y autoevaluación

Revisiones fijadas verificadas, actualizaciones revisadas, build aislado, inventario y procedencia reducen riesgos distintos. Ningún control garantiza confianza.

## Referencia rápida

lockfile / SBOM / provenance / attestation

## Referencias

- <https://docs.github.com/en/actions/reference/security/secure-use>
- <https://slsa.dev/spec/v1.0/>
- <https://www.cisa.gov/sbom>

---

<!-- navigation-footer -->
[Anterior](../09-commit-and-tag-signing/README.es.md) · [Índice](../README.es.md) · [Siguiente](../11-credential-exposure-and-incident-response/README.es.md)
<!-- /navigation-footer -->
