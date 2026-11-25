# ADR 0004: Integración Learning Hub

[English](0004-learning-hub-integration.md) · [Português](0004-learning-hub-integration.pt-BR.md) · [Español](0004-learning-hub-integration.es.md)

Propuesta para revisión del mantenedor; no autoriza iniciar el Sprint 01.

## Contexto

Guías futuras necesitan convenciones comunes, pero capacidades distintas. Contrato Python es preliminar.

## Decisión

Usar manifiestos preliminares compatibles fijados por revisión, mapas de idiomas, IDs estables y namespace de guía en consumidor. Separar evaluación determinista de estado Git de ejecución Python; finalizar esquemas tras pilotos y revisión coordinada. Sitio se ocupa de UI/runtime/progreso/accesibilidad.

## Alternativas

Rechazar runtime único obligatorio, esquema universal impuesto unilateralmente, sitio dentro de guía y evaluación semántica por IA.

## Consecuencias

Consumidores validan esquema/revisión, rechazan versiones major no soportadas y refs inseguras. Playground opcional: evaluar fidelidad, persistencia, aislamiento, accesibilidad, límites y costo cero antes de elegir tecnología; sin ejecución arbitraria privilegiada.

## Documentos relacionados

- [Índice ADR](README.es.md)
- [Contrato de integración](../specs/project-foundation/integration-contract.es.md)
