# Desarrollo guiado por especificación (SDD)

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../08-code-review/README.es.md) · [Índice](../README.es.md) · [Siguiente](../10-test-driven-development/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 45 min

**Requisitos previos:** [CI/CD](../../ci-cd/README.es.md) · [Code review y preparación para merge](../08-code-review/README.es.md)

**Objetivo:** Trazar requisitos a tareas y evidencia de aceptación.

## Qué es y por qué

SDD usa especificación como base de planificación, implementación y verificación. Es familia de prácticas, no comando Git ni único framework obligatorio. Constitución establece principios, especificación define requisitos observables y exclusiones, plan describe elecciones de implementación, tareas dividen trabajo y criterios de aceptación definen evidencia de éxito. ADR (registro de decisión arquitectónica) documenta contexto, decisión y consecuencias cuando elección importante requiere justificación. Trace requisitos a tareas y tests. Use rama enfocada y revise specs al evolucionar requisitos. Documentos del guía ilustran una implementación; herramientas externas e IA son opcionales.

[Especificación del proyecto](../../docs/specs/project-foundation/specification.es.md) · [Criterios de aceptación](../../docs/specs/project-foundation/acceptance-criteria.es.md)

## Práctica

Redacte spec de una página para catálogo ficticio: R1 expone línea exacta `status: ready` cuando listo; R2 mantiene estado draft previo a integración; exclusión: sin despliegue ni servicios externos. AC1 verifica línea ready, AC2 verifica ausencia inicial y estado integrado limpio. Planifique cambio de un archivo y check shell acotado; T1 escribe check, T2 implementa, T3 inspecciona diff e integra, T4 registra evidencia de release. Mapee R1->AC1/T1/T2 y R2->AC2/T1/T3; vincule T4 a política de release. Compare plan con capítulo 13.

## Riesgos y recuperación

No escriba criterios vagos como 'funciona bien', genere tareas antes de aclarar intención ni marque test no ejecutado como aprobado. Resuelva contradicciones en origen con mantenedor, actualice tareas/tests y solicite review. Spec no sustituye experimentos ni feedback.

## Ejercicio y autoevaluación

Cada requisito tiene al menos un check observable y cada tarea un motivo. Exclusiones explícitas evitan crecimiento de alcance. Revisión aceptada exacta y evidencia pertenecen a entrega.

## Referencia rápida

constitution / spec / plan / task / AC / ADR

## Fuentes

- <https://github.github.com/spec-kit/>
