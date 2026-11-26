# Conventional Commits

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../05-workflow-trade-offs/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../07-semantic-versioning/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 30 min

**Pré-requisitos:** [CI/CD](../../ci-cd/README.pt-BR.md) · [Escolha de estratégia de fluxo](../05-workflow-trade-offs/README.pt-BR.md)

**Objetivo:** Escrever mensagens úteis e identificar mudanças incompatíveis.

## O que é e por quê

Conventional Commits é convenção de mensagens, não exigência sintática do Git. Cabeçalho `type(scope): description`; scope opcional. `feat` indica funcionalidade, `fix` correção e `!` antes dos dois-pontos ou rodapé `BREAKING CHANGE:` indica incompatibilidade. Corpo após linha vazia explica intenção; rodapés registram metadados. Tipos como docs, test e chore são convenções e não alteram SemVer implicitamente salvo breaking change. Ferramentas de release podem interpretar mensagens, mas Git não incrementa versão sozinho. Título e corpo do squash devem preservar significado relevante da mudança combinada.

## Prática

Classifique mensagens originais: `fix(catalog): preserve empty results`, `feat(catalog): add readiness field`, `docs: explain catalog filters`, `feat(api)!: replace item identifier`. Escreva corpo para última mudança descrevendo migração e escolha título squash para PR adicionando prontidão e testes.

## Riscos e recuperação

Não rotule incompatibilidades como fix para evitar major. Não reescreva histórico publicado/compartilhado só para arrumar mensagem; esclareça em metadados posteriores ou siga procedimento aprovado. Nunca inclua credenciais ou conteúdo privado de issues em mensagens.

## Exercício e autocorreção

Fix, feature, documentação, feature incompatível respectivamente. Título squash adequado: `feat(catalog): add readiness field`; preserve marcadores de quebra quando aplicáveis.

## Referência rápida

`type(scope): description` / `!` / `BREAKING CHANGE:`

## Fontes

- <https://www.conventionalcommits.org/en/v1.0.0/>
- <https://git-scm.com/docs/git-commit>

---

<!-- navigation-footer -->
[Anterior](../05-workflow-trade-offs/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../07-semantic-versioning/README.pt-BR.md)
<!-- /navigation-footer -->
