# Commits e tags anotadas

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../02-blobs-and-trees/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../04-object-hashes/README.pt-BR.md)
<!-- /navigation -->

**Nível:** avançado · **Tempo estimado:** 45 min

**Pré-requisitos:** [14 Internals do Git](../README.pt-BR.md) · [Git avançado](../../advanced-git/README.pt-BR.md)

**Objetivo:** Commit contém ID de tree raiz, zero ou mais pais, autor, committer, horários e mensagem.

## O que é e por quê

Commit contém ID de tree raiz, zero ou mais pais, autor, committer, horários e mensagem. Merge tem vários pais; raiz não tem. Tags anotadas são objetos com metadados e alvo; leves são refs sem objeto tag. Assinatura é metadado adicional, não prova automática de identidade.

```text
refs/tags/annotated -> tag object -> commit C -> tree T
refs/tags/lightweight ---------------> commit C
refs/heads/main ---------------------> commit C
                                      |
                                      +-> parent P
```

Objeto tag → commit → tree; ref branch → commit.

## Prática

Crie lab isolado novo pelo índice vinculado de Git avançado antes de cada prática. Rode comandos individualmente e pare em resultado inesperado. Confira raiz e sandbox impresso. Base Git 2.34+, Bash (Git Bash no Windows).

Crie tags fictícias não assinadas apenas no lab. Inspecione tipos e compare tag anotada resolvida (`^{commit}`) com HEAD. Review de release deve registrar commit resolvido em vez de confiar no nome exibido. Não force tags publicadas.

```bash
git cat-file -p HEAD
git rev-list --parents -1 HEAD
git tag lightweight
git tag -a annotated -m "Example release"
git cat-file -t lightweight
git cat-file -t annotated
git cat-file -p annotated
test "$(git rev-parse annotated^{commit})" = "$(git rev-parse HEAD)"
```

## Erros comuns e segurança

Use só lab descartável. Nunca altere arquivos de objetos/refs à mão, force prune ou experimente em repo real. Se estado divergir, inspecione status, log e plumbing de leitura; feche shell dedicado e remova só sandbox anotado pelo gerenciador de arquivos após revisar conteúdo.

## Exercício e autocorreção

Objeto tag → commit → tree; ref branch → commit. O que muda quando main avança? Ref da branch; tags não avançam automaticamente.

## Referência rápida

- `git cat-file -p HEAD`
- `git rev-list --parents -1 HEAD`
- `git tag lightweight`
- `git tag -a annotated -m "Example release"`

## Fontes oficiais

- [https://git-scm.com/docs/git-commit-tree](https://git-scm.com/docs/git-commit-tree)
- [https://git-scm.com/docs/git-tag](https://git-scm.com/docs/git-tag)
- [https://git-scm.com/docs/git-rev-parse](https://git-scm.com/docs/git-rev-parse)

---

<!-- navigation-footer -->
[Anterior](../02-blobs-and-trees/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../04-object-hashes/README.pt-BR.md)
<!-- /navigation-footer -->
