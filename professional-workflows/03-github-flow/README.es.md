# GitHub Flow

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../02-git-flow/README.es.md) · [Índice](../README.es.md) · [Siguiente](../04-trunk-based-development/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 35 min

**Requisitos previos:** [CI/CD](../../ci-cd/README.es.md) · [Git Flow](../02-git-flow/README.es.md)

**Objetivo:** Describir flujo rama-PR y límite de review.

## Qué es y por qué

GitHub Flow es convención ligera: crear rama, hacer commits, abrir PR, discutir y revisar, integrar tras aprobación y eliminar rama tras comprobación. Favorece rama predeterminada lista para integración, cambios pequeños y feedback continuo. Protección y CI son políticas de alojamiento que pueden imponer partes del flujo; GitHub Flow no exige método específico de merge, despliegue automático, plan pago ni eludir aprobación. PR draft señala trabajo en progreso. Puede solaparse con trunk-based si ramas duran muy poco.

```text
branch -> commits -> PR -> review + CI -> authorized merge
```

## Práctica

Sin conexión: simule autor y revisor de corrección de etiqueta de búsqueda de catálogo. Escriba título de PR, problema, alcance, checks y límites. Revisor pide corrección ortográfica; autor aporta nueva revisión y evidencia. Dibuje recorrido de rama a main revisada. Opcional: haga en repositorio desechable propio sin servicios de pago; no se exige cuenta.

## Riesgos y recuperación

Apertura de PR no es aprobación. No integre revisión desactualizada o fallida; confirme base actual, head revisado y checks reales. No suponga que eliminar rama despliega cambio. Para regresión siga proceso acordado de revert y release.

## Ejercicio y autoevaluación

Nueva revisión debe revisarse y validarse según política; PR se cierra tras integración autorizada o abandono.

## Referencia rápida

branch / PR / review / merge

## Fuentes

- <https://docs.github.com/en/get-started/using-github/github-flow>
- <https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/reviewing-proposed-changes-in-a-pull-request>

---

<!-- navigation-footer -->
[Anterior](../02-git-flow/README.es.md) · [Índice](../README.es.md) · [Siguiente](../04-trunk-based-development/README.es.md)
<!-- /navigation-footer -->
