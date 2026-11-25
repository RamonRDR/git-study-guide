# ADR 0001: Fuente única de contenido

[English](0001-content-source-of-truth.md) · [Português](0001-content-source-of-truth.pt-BR.md) · [Español](0001-content-source-of-truth.es.md)

Propuesta para revisión del mantenedor; no autoriza iniciar el Sprint 01.

## Contexto

Guía gratuita independiente y sitio futuro necesitan una revisión autoritativa.

## Decisión

Markdown, ejemplos compartidos y datos estructurados viven en este repositorio. Importar commit inmutable aprobado en el build del sitio. Mantener aprendizaje GitHub/local independiente.

## Alternativas

Rechazar copias manuales en el sitio (divergencia), scraping HTML (acoplamiento a presentación) y API por visitante (disponibilidad y límites).

## Consecuencias

Consumidor valida revisión, rutas y renderizado seguro; cambios aparecen tras rebuild. Sin infraestructura de pago por diseño; verificar límites reales.

## Documentos relacionados

- [Índice ADR](README.es.md)
- [Contrato de integración](../specs/project-foundation/integration-contract.es.md)
