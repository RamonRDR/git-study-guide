# ADR 0002: Arquitetura multilíngue

[English](0002-multilingual-architecture.md) · [Português](0002-multilingual-architecture.pt-BR.md) · [Español](0002-multilingual-architecture.es.md)

Fundação aprovada e integrada pelo PR #1 em 25/11/2026. Mudanças seguintes exigem revisão e aprovação explícita do mantenedor.

## Contexto

Toda prosa pública deve permanecer conceitualmente alinhada e navegável no GitHub.

## Decisão

Inglês principal; README.md/README.pt-BR.md/README.es.md irmãos para capítulos; sufixos irmãos para specs/ADRs, traduções da raiz em docs/localized/. Compartilhar código/IDs/assets quando neutros; localizar texto visível. Revisar três idiomas no mesmo PR.

## Alternativas

Rejeitados repositórios separados (divergência), Markdown multilíngue único (navegação ruim), tradução automática em runtime (significado não revisado).

## Consequências

Validar paridade de arquivos, seletores e navegação; revisão humana verifica semântica. Preservar caminhos e texto MIT.

## Documentos relacionados

- [Índice ADR](README.pt-BR.md)
- [Contrato de integração](../specs/project-foundation/integration-contract.pt-BR.md)
