# Fluxo com feature branches

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
— · [Índice](../README.pt-BR.md) · [Próximo](../02-git-flow/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 35 min

**Pré-requisitos:** [CI/CD](../../ci-cd/README.pt-BR.md)

**Objetivo:** Explicar estado de feature branch e integração revisada.

## O que é e por quê

Feature branch é linha temporária criada a partir da base de integração pretendida. Commits avançam sua ref sem avançar a main. Pull request (PR) ou merge request (MR) é recurso de hospedagem que propõe integração; Git conhece refs e commits, não aprovações de review. Mantenha mudanças pequenas, testáveis isoladamente e ligadas a requisito. Busque e inspecione destino antes da integração; atualize branch conforme política da equipe. Squash merge cria commit combinado novo em vez de preservar todos os commits da branch; merge normal pode preservar ambos históricos. Escolha método conscientemente.

```text
base main -> feature branch -> review -> authorized integration
```

## Prática

Catálogo fictício de biblioteca precisa de campo de prontidão e correção ortográfica separada. Desenhe duas branches da main, cada uma com objetivo. Para branch de prontidão, preveja `git switch -c feat/ready-catalog`, commit, retorno à main e integração. Use laboratório local do capítulo 13 para observar estados; PR hospedado é opcional.

## Riscos e recuperação

Evite agrupar mudanças sem relação ou manter branch aberta por semanas sem motivo. Inspecione divergência e resolva conflitos na branch própria; aborte merge não resolvido em vez de adivinhar. Não force-push em branches compartilhadas nem contorne review obrigatório. Exclua branches só após verificar integração e retenção.

## Exercício e autocorreção

Duas branches mantêm correções independentes. Main permanece igual até integração. Identifique qual ref avança e distinga proposta de review de commit Git.

## Referência rápida

`git switch -c` / `git diff` / PR / MR

## Fontes

- <https://git-scm.com/docs/gitworkflows>
- <https://git-scm.com/docs/git-branch>
- <https://git-scm.com/docs/git-merge>
