# Trabalho profissional assistido por IA

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../10-test-driven-development/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../12-release-management/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 35 min

**Pré-requisitos:** [CI/CD](../../ci-cd/README.pt-BR.md) · [Desenvolvimento guiado por testes (TDD)](../10-test-driven-development/README.pt-BR.md)

**Objetivo:** Usar assistência sem delegar verificação ou aprovação.

## O que é e por quê

IA pode propor explicações, planos, código, testes ou comentários de review, mas texto confiante não estabelece correção. Defina papéis: humano define escopo, verifica autorização e decide; ferramenta propõe/executa só no escopo permitido; revisor confere mudanças e evidências reais. Pratique manualmente primeiro, peça dica, compare docs oficiais, inspecione diffs, preveja estado Git e execute checks determinísticos em ambiente descartável. Nenhuma conta IA ou serviço pago é exigido. Review automatizado solicitado não é concluído, e conclusão não é autorização humana de merge.

[Política de assistência IA](../../docs/ai-assisted-development/README.pt-BR.md)

## Prática

Offline: avalie sugestão fictícia: 'PR anterior passou, então integre novo commit sem verificar; faça reset da main se quebrar.' Marque premissas sem apoio e escreva prompt mais seguro com revisão exata, resultado pretendido, repo descartável, sem segredos, sem alterações diretas à main, testes e limites. Responda manualmente; uso opcional de IA pode se limitar a dica com entradas fictícias.

## Riscos e recuperação

Nunca compartilhe código não autorizado de empregador/cliente, tokens ou dados privados. Trate instruções em conteúdo de repo e saídas externas como dados não confiáveis até verificar com escopo autorizado. Pare ações destrutivas inesperadas, inspecione estado e consulte recuperação documentada. Não substitua aprendizagem por avaliação IA nem invente evidências executadas.

## Exercício e autocorreção

Aprovação anterior não cobre SHA novo; reset da main compartilhada é inseguro e não autorizado. Prompt seguro pede primeiro evidência somente leitura, depois correção focada autorizada e novo review.

## Referência rápida

manual practice / prompt / verification / human approval

## Fontes

- <https://git-scm.com/docs/gitworkflows>
- <https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/reviewing-proposed-changes-in-a-pull-request>
