# Desarrollo basado en trunk

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../03-github-flow/README.es.md) · [Índice](../README.es.md) · [Siguiente](../05-workflow-trade-offs/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 40 min

**Requisitos previos:** [CI/CD](../../ci-cd/README.es.md) · [GitHub Flow](../03-github-flow/README.es.md)

**Objetivo:** Planificar integración frecuente segura.

## Qué es y por qué

Trunk es línea compartida de integración, a menudo main. Trunk-based integra lotes pequeños con frecuencia, muchas veces diariamente o más, con ramas muy cortas o integración directa donde política lo permite. No exige push directo sin review. Feedback automatizado, tests fiables, cambios pequeños y revisión rápida mantienen trunk sano. Feature flag separa integración de código incompleto pero seguro de exposición a usuarios; requiere valor predeterminado, responsable y plan de retirada. Flag no es mecanismo de autorización. Branch-by-abstraction introduce interfaz estable para coexistencia de comportamiento antiguo y nuevo durante transición. Ninguna técnica justifica integrar trabajo roto.

```text
small change -> fast review + CI -> trunk -> next small change
```

## Práctica

Nueva búsqueda de catálogo tarda cinco días. Divida en interfaz compatible, implementación oculta, tests, decisión de activación y retirada de flag. Cada cambio es pequeño, revisado y pasa CI; búsqueda anterior sigue usable hasta activación. Identifique etapas que cambian historial Git y las que cambian configuración de ejecución. Dibuje rama corta volviendo a trunk diariamente.

## Riesgos y recuperación

No use flags para esconder comportamiento inseguro o no probado. Si trunk falla, detenga integración/promoción y priorice restaurarlo con fix o revert autorizado. Push directo a main no se permite en este guía. Merge frecuente no significa necesariamente despliegue frecuente.

## Ejercicio y autoevaluación

Prefiera incrementos pequeños seguros, reviews cortos y estados de flag comprobables. Integración a trunk y activación son decisiones distintas.

## Referencia rápida

trunk / short-lived branch / feature flag

## Fuentes

- <https://dora.dev/capabilities/trunk-based-development/>
- <https://git-scm.com/docs/gitworkflows>
- <https://www.atlassian.com/git/tutorials/comparing-workflows>
