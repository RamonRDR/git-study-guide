# Pontos de partida e comparação de branches

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../01-create-and-switch/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../03-switch-safety-and-naming/README.pt-BR.md)
<!-- /navigation -->

**Nível:** iniciante · **Tempo estimado:** 30 min

**Pré-requisitos:** [Criar e alternar branches locais](../01-create-and-switch/README.pt-BR.md)

**Objetivo:** Escolher commit inicial e comparar históricos e snapshots.

## O que é e por quê

Branches podem partir de branch local nomeada ou ID de commit, em vez de HEAD atual. HEAD~1 é primeiro pai de HEAD. Há divergência quando ambos lados têm commits ausentes no outro. `git log A..B` lista commits alcançáveis por B mas não A; inverter nomes muda conjunto. `git diff A B` compara árvores finais, não quantidade de commits. `git diff A..B` também compara pontas; `git diff A...B` compara merge base (melhor ancestral comum) a B. Merge e rebase no próximo módulo; comandos aqui apenas consultam.

## Prática

Continue em feat/note limpa (C2). Crie branch do pai C1 e selecione nova branch docs a partir de main. Confira raiz e status limpo primeiro:

```text
git branch archive/base HEAD~1
git rev-parse archive/base main
git switch -c docs/overview main
git branch --show-current
git status --short
```

Esperado: archive/base e main mesmo ID, docs/overview atual em C1. Crie overview.txt com overview e quebra final. Prepare e confira:

```text
git add -- overview.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Só com diff esperado e identidades fictícias:

```text
git commit -m "docs: add overview"
git log --all --graph --oneline --decorate
git log --oneline feat/note..docs/overview
git log --oneline docs/overview..feat/note
git diff --name-status feat/note docs/overview
git diff --name-status feat/note...docs/overview
git merge-base feat/note docs/overview
git rev-parse main
```

Esperado: um commit distinto em cada intervalo log. Diff de pontas mostra note.txt modificado e overview.txt adicionado; diff três pontos só overview.txt adicionado. IDs finais merge-base/main iguais. Diagrama: feat/note -> C2 -> C1; docs/overview -> C3 -> C1; main e archive/base -> C1. Nenhum histórico alterado ao comparar.

## Erros comuns e segurança

Não suponha que intervalos log e diff significam o mesmo. Nome de branch pode mover; confira rev-parse antes de escolher base. Se IDs divergirem do esperado, veja gráfico em vez de mover refs à força.

## Exercício e autocorreção

Qual comparação isola commits de docs/overview ausentes em feat/note? Resposta: git log feat/note..docs/overview. Qual diff mostra mudanças desde ancestral comum? git diff feat/note...docs/overview. Passe se saídas corresponderem ao gráfico. Uso profissional: conferir escopo de review.

## Referência rápida

`git branch NAME START`: criar na base; `git log A..B`: commits exclusivos de B em relação a A; `git diff A B`: árvores; `git diff A...B`: base a B.

## Fontes oficiais

- [Git: git-branch](https://git-scm.com/docs/git-branch)
- [Git: git-log](https://git-scm.com/docs/git-log)
- [Git: git-diff](https://git-scm.com/docs/git-diff)
- [Git: git-merge-base](https://git-scm.com/docs/git-merge-base)
- [Git: gitrevisions](https://git-scm.com/docs/gitrevisions)
