# Elección de estrategia de flujo

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../04-trunk-based-development/README.es.md) · [Índice](../README.es.md) · [Siguiente](../06-conventional-commits/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 35 min

**Requisitos previos:** [CI/CD](../../ci-cd/README.es.md) · [Desarrollo basado en trunk](../04-trunk-based-development/README.es.md)

**Objetivo:** Elegir modelo con compromisos concretos.

## Qué es y por qué

No hay modelo universal. Compare duración de ramas, frecuencia de integración, líneas de release mantenidas, aprobación, fiabilidad de CI, latencia de review y recuperación. Feature branching es técnica amplia; GitHub Flow añade convención ligera de review alojado; trunk-based enfatiza integración frecuente; Git Flow define líneas duraderas de release y desarrollo. Categorías se solapan. Equipo puede combinar trunk protegida, features cortas y ramas de mantenimiento. Más ramas no dan gobernanza automáticamente; controles explícitos y evidencia importan.

## Práctica

Compare tres equipos ficticios: guía documental con una main, PR y dos checks; producto de escritorio con dos releases antiguas mantenidas; catálogo en línea con cambios diarios seguros y CI rápido. Escriba registro de decisión con contexto, modelo elegido, alternativa rechazada, método de merge, política de release y disparadores de review. Evalúe restricciones reales, no popularidad.

## Riesgos y recuperación

No cambie modelo de producción sin plan de migración, revisión de permisos, acuerdo del equipo y mapeo de releases verificado. Evite afirmar que modelo elimina conflictos. Revise decisión cuando restricciones cambien.

## Ejercicio y autoevaluación

Opciones razonables: feature/GitHub Flow protegido para documentación; trunk con mantenimiento o Git Flow si coordinación lo justifica en escritorio; trunk-based protegido para catálogo en línea. Alternativas válidas si justificadas por restricciones.

## Referencia rápida

branch lifetime / CI / release cadence / support

## Fuentes

- <https://www.atlassian.com/git/tutorials/comparing-workflows>
- <https://dora.dev/capabilities/trunk-based-development/>
- <https://nvie.com/posts/a-successful-git-branching-model/>
