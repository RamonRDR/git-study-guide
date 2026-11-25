# ADR 0001: Fonte única de conteúdo

[English](0001-content-source-of-truth.md) · [Português](0001-content-source-of-truth.pt-BR.md) · [Español](0001-content-source-of-truth.es.md)

Fundação aprovada e integrada pelo PR #1 em 25/11/2026. Mudanças seguintes exigem revisão e aprovação explícita do mantenedor.

## Contexto

Guia gratuito independente e site futuro precisam de uma revisão autoritativa.

## Decisão

Markdown, exemplos compartilhados e dados estruturados vivem neste repositório. Importar commit imutável aprovado no build do site. Manter aprendizado GitHub/local independente.

## Alternativas

Rejeitar cópias manuais no site (divergência), scraping HTML (acoplamento à apresentação) e API por visitante (disponibilidade e limites).

## Consequências

Consumidor valida revisão, caminhos e renderização segura; mudanças aparecem após rebuild. Sem infraestrutura paga por design; verificar limites reais.

## Documentos relacionados

- [Índice ADR](README.pt-BR.md)
- [Contrato de integração](../specs/project-foundation/integration-contract.pt-BR.md)
