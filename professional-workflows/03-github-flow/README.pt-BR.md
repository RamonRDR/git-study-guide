# GitHub Flow

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../02-git-flow/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../04-trunk-based-development/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 35 min

**Pré-requisitos:** [CI/CD](../../ci-cd/README.pt-BR.md) · [Git Flow](../02-git-flow/README.pt-BR.md)

**Objetivo:** Descrever fluxo branch-PR e limite de review.

## O que é e por quê

GitHub Flow é convenção leve: criar branch, fazer commits, abrir PR, discutir e revisar, integrar após aprovação e remover branch após verificação. Favorece branch padrão pronta para integração, mudanças pequenas e feedback contínuo. Proteção e CI são políticas de hospedagem que podem impor partes do fluxo; GitHub Flow não exige método específico de merge, implantação automática, plano pago ou contorno de aprovação. PR draft sinaliza trabalho em progresso. Pode se sobrepor a trunk-based quando branches duram muito pouco.

```text
branch -> commits -> PR -> review + CI -> authorized merge
```

## Prática

Offline: simule autor e revisor de correção de rótulo de busca do catálogo. Escreva título do PR, problema, escopo, checks e limitações. Revisor pede correção de grafia; autor fornece nova revisão e evidências. Desenhe percurso da branch à main revisada. Opcional: faça em repositório descartável próprio sem serviços pagos; nenhuma conta exigida.

## Riscos e recuperação

Abertura de PR não é aprovação. Não integre revisão desatualizada ou falha; confirme base atual, head revisado e checks reais. Não suponha exclusão de branch implanta mudança. Para regressão siga processo acordado de revert e release.

## Exercício e autocorreção

Nova revisão precisa ser revisada e validada conforme política; PR encerra após integração autorizada ou abandono.

## Referência rápida

branch / PR / review / merge

## Fontes

- <https://docs.github.com/en/get-started/using-github/github-flow>
- <https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/reviewing-proposed-changes-in-a-pull-request>
