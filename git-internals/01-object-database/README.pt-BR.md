# Banco de objetos: armazenamento do repositório

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Módulo anterior](../../advanced-git/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../02-blobs-and-trees/README.pt-BR.md)
<!-- /navigation -->

**Nível:** avançado · **Tempo estimado:** 40 min

**Pré-requisitos:** [14 Internals do Git](../README.pt-BR.md) · [Git avançado](../../advanced-git/README.pt-BR.md)

**Objetivo:** Git armazena objetos tipados identificados pelo conteúdo: blob (conteúdo de arquivo), tree (entradas de diretório), commit (snapshot e ancestralidade), tag anotada (metadados de objeto nomeado).

## O que é e por quê

Git armazena objetos tipados identificados pelo conteúdo: blob (conteúdo de arquivo), tree (entradas de diretório), commit (snapshot e ancestralidade), tag anotada (metadados de objeto nomeado). Refs nomeiam objetos; working tree e index não são banco de objetos. Use distinção ao diagnosticar dados ausentes ou explicar por que checkout não é backup.

```text
refs/heads/main -> commit C -> tree T -> tree S -> blob B
                     |
                     +-> parent P -> tree U
```

Commit → tree raiz → tree de diretório → blob.

## Prática

Crie lab isolado novo pelo índice vinculado de Git avançado antes de cada prática. Rode comandos individualmente e pare em resultado inesperado. Confira raiz e sandbox impresso. Base Git 2.34+, Bash (Git Bash no Windows).

Inspecione tipo e tamanho de HEAD e liste objetos alcançáveis. `git count-objects -v` informa estatísticas de armazenamento, não contagem de commits. Observe que commit aponta a tree, não diretamente a cada arquivo de trabalho.

```bash
git cat-file -t HEAD
git cat-file -s HEAD
git cat-file -p HEAD
git rev-list --objects --all
git count-objects -v
```

## Erros comuns e segurança

Use só lab descartável. Nunca altere arquivos de objetos/refs à mão, force prune ou experimente em repo real. Se estado divergir, inspecione status, log e plumbing de leitura; feche shell dedicado e remova só sandbox anotado pelo gerenciador de arquivos após revisar conteúdo.

## Exercício e autocorreção

Commit → tree raiz → tree de diretório → blob. Aresta pai liga commits; refs apontam para IDs. Qual tipo guarda bytes de arquivo? Blob.

## Referência rápida

- `git cat-file -t HEAD`
- `git cat-file -s HEAD`
- `git cat-file -p HEAD`
- `git rev-list --objects --all`

## Fontes oficiais

- [https://git-scm.com/docs/git-cat-file](https://git-scm.com/docs/git-cat-file)
- [https://git-scm.com/docs/git-count-objects](https://git-scm.com/docs/git-count-objects)
- [https://git-scm.com/docs/gitrepository-layout](https://git-scm.com/docs/gitrepository-layout)

---

<!-- navigation-footer -->
[Módulo anterior](../../advanced-git/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../02-blobs-and-trees/README.pt-BR.md)
<!-- /navigation-footer -->
