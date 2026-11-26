# Reflogs e alcançabilidade

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../08-gc-and-maintenance/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../10-porcelain-and-plumbing/README.pt-BR.md)
<!-- /navigation -->

**Nível:** avançado · **Tempo estimado:** 45 min

**Pré-requisitos:** [14 Internals do Git](../README.pt-BR.md) · [Git avançado](../../advanced-git/README.pt-BR.md)

**Objetivo:** Objeto é alcançável de raiz ao percorrer arestas relevantes (pais, trees, blobs e alvos tag).

## O que é e por quê

Objeto é alcançável de raiz ao percorrer arestas relevantes (pais, trees, blobs e alvos tag). Reflogs registram localmente atualizações de refs, frequentemente mantendo tips anteriores recuperáveis após mover branch; expiram e geralmente não são transferidos por clone. Alcançabilidade por refs atuais difere de incluir reflogs e index.

```text
refs/heads/main -> C -> B -> A
reflog old tip --> D -> B -> A
                 (D may not be reachable from current refs)
```

As setas mostram relações de referências ou operações, não caminhos de arquivos.

## Prática

Crie lab isolado novo pelo índice vinculado de Git avançado antes de cada prática. Rode comandos individualmente e pare em resultado inesperado. Confira raiz e sandbox impresso. Base Git 2.34+, Bash (Git Bash no Windows).

Inspecione refs atuais, reflog e grafo alcançável no lab. Leia HEAD@{1} só após confirmar entrada no reflog. Em recuperação real, crie branch nova no commit perdido verificado em vez de reescrever main. Nunca expire reflogs nem prune objetos para recuperar.

```bash
git show-ref
git reflog show HEAD
git rev-list --all
git rev-list --all --reflog
git show --stat 'HEAD@{1}'
```

## Erros comuns e segurança

Use só lab descartável. Nunca altere arquivos de objetos/refs à mão, force prune ou experimente em repo real. Se estado divergir, inspecione status, log e plumbing de leitura; feche shell dedicado e remova só sandbox anotado pelo gerenciador de arquivos após revisar conteúdo.

## Exercício e autocorreção

Reflog garante recuperação meses depois? Não; expiração, config, exclusão ou limpeza de objetos podem remover evidência.

## Referência rápida

- `git show-ref`
- `git reflog show HEAD`
- `git rev-list --all`
- `git rev-list --all --reflog`

## Fontes oficiais

- [https://git-scm.com/docs/git-reflog](https://git-scm.com/docs/git-reflog)
- [https://git-scm.com/docs/git-rev-list](https://git-scm.com/docs/git-rev-list)
- [https://git-scm.com/docs/git-fsck](https://git-scm.com/docs/git-fsck)

---

<!-- navigation-footer -->
[Anterior](../08-gc-and-maintenance/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../10-porcelain-and-plumbing/README.pt-BR.md)
<!-- /navigation-footer -->
