# Snapshots, HEAD e referências

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../01-three-locations/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../03-file-states/README.pt-BR.md)
<!-- /navigation -->

**Nível:** iniciante · **Tempo estimado:** 25 min

**Pré-requisitos:** [Working tree, index e repositório](../01-three-locations/README.pt-BR.md)

**Objetivo:** Explicar o que commit e referência de branch representam.

## O que é e por quê

Commit aponta para árvore que representa snapshot do projeto e normalmente para commit(s) pai(s), com metadados de identidade e mensagem. Git armazena objetos endereçados por conteúdo; conteúdo igual pode compartilhar objeto. Git calcula diferenças entre snapshots; commit não é só arquivo de patch. Ref é nome que aponta para objeto (branch, para commit). HEAD normalmente referencia simbolicamente branch atual; em detached HEAD aponta direto para commit, tratado depois. Antes do primeiro commit HEAD pode nomear branch ainda sem commit.

## Prática

Continue lab isolado do capítulo 01. Antes do commit confira raiz, conteúdo preparado e ambas identidades. Registre apenas versão second preparada:

```text
git rev-parse --show-toplevel
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
git diff --cached
```

Pare se raiz incorreta, identidades não fictícias ou diff inesperado. Caso contrário:

```text
git commit -m "docs: revise note"
git symbolic-ref HEAD
git rev-parse HEAD
git rev-parse refs/heads/main
git log -2 --oneline
git show HEAD:note.txt
git status --short
```

Esperado: refs/heads/main; ambos rev-parse retornam mesmo ID de objeto, variável entre labs. Segundo commit aponta ao primeiro como pai. HEAD:note.txt contém second; arquivo continua third e status mostra espaço seguido de M. Diagrama: HEAD -> main -> C2 -> C1, última seta segue histórico de pais.

## Erros comuns e segurança

Não decore IDs nem suponha nome main universal. Nunca mova refs editando .git. IDs dependem de snapshot, pais e metadados; alterar histórico muda IDs. Nenhuma operação destrutiva necessária.

## Exercício e autocorreção

Explique HEAD versus main versus ID. Dica: um aponta branch, outro nomeia commit, outro identifica objeto. Resposta: HEAD normalmente nomeia branch atual; branch avança no commit; ID identifica conteúdo imutável do commit. Passe se verificar os dois rev-parse.

## Referência rápida

- `git rev-parse`
- `git symbolic-ref`
- `git log`
- `git show`
- `gitglossary`

## Fontes oficiais

- [Git: git-rev-parse](https://git-scm.com/docs/git-rev-parse)
- [Git: git-symbolic-ref](https://git-scm.com/docs/git-symbolic-ref)
- [Git: git-log](https://git-scm.com/docs/git-log)
- [Git: git-show](https://git-scm.com/docs/git-show)
- [Git: gitglossary](https://git-scm.com/docs/gitglossary)
