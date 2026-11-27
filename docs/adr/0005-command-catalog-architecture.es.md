# ADR 0005: Arquitectura del catálogo de comandos

[English](0005-command-catalog-architecture.md) · [Português](0005-command-catalog-architecture.pt-BR.md) · [Español](0005-command-catalog-architecture.es.md)

Estado: integrado mediante [PR #17](https://github.com/RamonRDR/git-study-guide/pull/17); validación posterior al merge completada.

## Decisión

Mantener un documento JSON UTF-8 canónico por categoría registrada de command-reference, con versión de esquema local, IDs estables en minúsculas, valores técnicos compartidos y mapas explícitos en/pt-BR/es para textos educativos. Generar las tres páginas de categoría y el índice del módulo de forma determinista con la biblioteca estándar de Python. Versionar el Markdown generado para lectura directa en GitHub; no editarlo por separado. Utilizar el registro curricular y las funciones canónicas de navegación existentes. Construir índices por categoría e intención a partir de los mismos registros.

Validar cantidad (al menos 101 operaciones relevantes, objetivo 120), unicidad, campos, riesgos, fuentes, referencias a capítulos, mapas de idiomas e igualdad del contenido generado. Distinguir comandos nativos, subcomandos, usos de opciones, flujos, herramientas externas y operaciones de plataforma. No ejecutar automáticamente los comandos del catálogo.

## Alternativas y consecuencias

Mantener JSON y Markdown manualmente duplica contenido; un catálogo exclusivo del sitio impide la lectura independiente en GitHub. No se adopta ninguna opción. Las comprobaciones estructurales no demuestran precisión técnica ni traducción semántica. Revisar por separado ejemplos reales, requisitos de versión y fuentes oficiales. Es un piloto interno, no un esquema definitivo ni un consumidor de Learning Hub; Sprint 18 sigue siendo responsable del contrato final. Sin servicios de pago ni dependencias adicionales.

- [Índice de ADRs](README.es.md)
- [Contrato de integración](../specs/project-foundation/integration-contract.es.md)
