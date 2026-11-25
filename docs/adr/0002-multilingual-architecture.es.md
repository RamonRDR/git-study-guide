# ADR 0002: Arquitectura multilingüe

[English](0002-multilingual-architecture.md) · [Português](0002-multilingual-architecture.pt-BR.md) · [Español](0002-multilingual-architecture.es.md)

Fundación aprobada e integrada mediante PR #1 el 25/11/2026. Cambios posteriores requieren revisión y aprobación explícita del mantenedor.

## Contexto

Toda prosa pública debe permanecer conceptualmente alineada y navegable en GitHub.

## Decisión

Inglés principal; README.md/README.pt-BR.md/README.es.md hermanos para capítulos; sufijos hermanos para specs/ADR, traducciones de raíz en docs/localized/. Compartir código/IDs/assets cuando sean neutros; localizar texto visible. Revisar tres idiomas en el mismo PR.

## Alternativas

Rechazados repositorios separados (divergencia), Markdown multilingüe único (mala navegación), traducción automática en runtime (significado no revisado).

## Consecuencias

Validar paridad de archivos, selectores y navegación; revisión humana verifica semántica. Preservar rutas y texto MIT.

## Documentos relacionados

- [Índice ADR](README.es.md)
- [Contrato de integración](../specs/project-foundation/integration-contract.es.md)
