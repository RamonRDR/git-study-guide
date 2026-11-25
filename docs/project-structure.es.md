# Estructura del proyecto

[English](project-structure.md) · [Português](project-structure.pt-BR.md) · [Español](project-structure.es.md)

La raíz contiene gobernanza, licencia MIT y 18 índices estables de módulos. docs/ contiene arquitectura, especificaciones, traducciones y orientación de ingeniería. scripts/ contiene validación con biblioteca estándar y registro interno del currículo; tests/ contiene fixtures deterministas. .github/ contiene plantillas y CI. Los recursos se añaden solo cuando se necesiten. El registro es interno, no el esquema final de Learning Hub.

Capítulos usan NN-topic/README.md, README.pt-BR.md y README.es.md. Registrar slugs en scripts/curriculum.json en orden numérico; enlazarlos en el bloque chapters y usar navigation para anterior, índice y siguiente. Los extremos no tienen enlace en la dirección ausente. Navegación de módulos sigue la hoja de ruta. Mantener rutas estables y no crear directorios vacíos.

- [Ruta](learning-path.es.md)
- [Automatización de calidad](quality-automation.es.md)
