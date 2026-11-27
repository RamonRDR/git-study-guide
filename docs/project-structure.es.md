# Estructura del proyecto

[English](project-structure.md) · [Português](project-structure.pt-BR.md) · [Español](project-structure.es.md)

La raíz contiene gobernanza, licencia MIT y 18 índices estables de módulos. docs/ contiene arquitectura, especificaciones, traducciones y orientación de ingeniería. scripts/ contiene validación con biblioteca estándar y registro interno del currículo; tests/ contiene fixtures deterministas. .github/ contiene plantillas y CI. Los recursos se añaden solo cuando se necesiten. El registro es interno, no el esquema final de Learning Hub.

Capítulos usan NN-topic/README.md, README.pt-BR.md y README.es.md. Registrar slugs en scripts/curriculum.json en orden numérico y enlazarlos en el bloque chapters. Cada índice de módulo y capítulo tiene navegación localizada idéntica en los bloques navigation y navigation-footer, el primero tras título y selector de idioma y el segundo al final. Usar anterior/índice/siguiente en ese orden. Primer y último capítulos enlazan índices de módulos adyacentes (incluso reservados), con etiquetas Módulo anterior/Siguiente módulo. Solo direcciones ausentes en extremos de la hoja de ruta usan raya sin enlace. Índices de módulos enlazan índices adyacentes y ruta de aprendizaje. Las funciones navigation_entries y navigation_line del validador definen destinos y etiquetas canónicas. Mantener rutas estables y no crear directorios vacíos.

El módulo 15 usa un catalog.json canónico por categoría, más registros de categorías e intenciones en scripts/. Las páginas Markdown trilingües se generan desde esos registros con scripts/render_command_reference.py y el registro de navegación existente. Edita JSON en lugar de páginas generadas; consulta [ADR 0005](adr/0005-command-catalog-architecture.es.md). Es piloto interno, no contrato final de integración.

- [Ruta](learning-path.es.md)
- [Automatización de calidad](quality-automation.es.md)
