# Conventional Commits

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../05-workflow-trade-offs/README.es.md) · [Índice](../README.es.md) · [Siguiente](../07-semantic-versioning/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 30 min

**Requisitos previos:** [CI/CD](../../ci-cd/README.es.md) · [Elección de estrategia de flujo](../05-workflow-trade-offs/README.es.md)

**Objetivo:** Escribir mensajes útiles e identificar cambios incompatibles.

## Qué es y por qué

Conventional Commits es convención de mensajes, no requisito sintáctico de Git. Encabezado `type(scope): description`; scope opcional. `feat` indica funcionalidad, `fix` corrección y `!` antes de dos puntos o pie `BREAKING CHANGE:` indica incompatibilidad. Cuerpo tras línea en blanco explica intención; pies registran metadatos. Tipos docs, test y chore son convenciones y no cambian SemVer implícitamente salvo breaking change. Herramientas de release pueden interpretar mensajes, pero Git no incrementa versión por sí mismo. Título y cuerpo de squash deben preservar significado relevante del cambio combinado.

## Práctica

Clasifique mensajes originales: `fix(catalog): preserve empty results`, `feat(catalog): add readiness field`, `docs: explain catalog filters`, `feat(api)!: replace item identifier`. Escriba cuerpo del último cambio describiendo migración y elija título squash de PR que añade disponibilidad y tests.

## Riesgos y recuperación

No etiquete incompatibilidades como fix para evitar major. No reescriba historial publicado/compartido solo para arreglar mensaje; aclare en metadatos posteriores o siga procedimiento aprobado. Nunca incluya credenciales ni contenido privado de issues en mensajes.

## Ejercicio y autoevaluación

Fix, feature, documentación, feature incompatible respectivamente. Título squash adecuado: `feat(catalog): add readiness field`; preserve marcadores de ruptura cuando proceda.

## Referencia rápida

`type(scope): description` / `!` / `BREAKING CHANGE:`

## Fuentes

- <https://www.conventionalcommits.org/en/v1.0.0/>
- <https://git-scm.com/docs/git-commit>

---

<!-- navigation-footer -->
[Anterior](../05-workflow-trade-offs/README.es.md) · [Índice](../README.es.md) · [Siguiente](../07-semantic-versioning/README.es.md)
<!-- /navigation-footer -->
