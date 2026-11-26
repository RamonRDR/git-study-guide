# Refs e HEAD: nomear IDs de objetos

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../04-object-hashes/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../06-index-internals/README.pt-BR.md)
<!-- /navigation -->

**Nível:** avançado · **Tempo estimado:** 40 min

**Pré-requisitos:** [14 Internals do Git](../README.pt-BR.md) · [Git avançado](../../advanced-git/README.pt-BR.md)

**Objetivo:** Ref de branch normalmente nomeia commit e avança ao commitar nela.

## O que é e por quê

Ref de branch normalmente nomeia commit e avança ao commitar nela. HEAD normalmente é ref simbólica para branch; detached HEAD identifica commit diretamente. Refs podem estar empacotadas ou em backends distintos, então ler arquivo específico em .git não é portável. Use comandos conscientes de refs.

```text
HEAD -> refs/heads/main -> commit C
HEAD (detached) ----------> commit P
```

HEAD → refs/heads/main → commit; HEAD destacado → commit.

## Prática

Crie lab isolado novo pelo índice vinculado de Git avançado antes de cada prática. Rode comandos individualmente e pare em resultado inesperado. Confira raiz e sandbox impresso. Base Git 2.34+, Bash (Git Bash no Windows).

Inspecione HEAD simbólico, refs e commit resolvido. Destaque no pai só no lab descartável limpo; symbolic-ref -q HEAD retorna não zero. Volte à main e confira limpeza. Se houver trabalho em detached HEAD, preserve com branch antes de trocar.

```bash
git symbolic-ref HEAD
git show-ref
git rev-parse HEAD
git switch --detach HEAD~1
git symbolic-ref -q HEAD
git rev-parse HEAD
git switch main
git status --short
```

## Erros comuns e segurança

Use só lab descartável. Nunca altere arquivos de objetos/refs à mão, force prune ou experimente em repo real. Se estado divergir, inspecione status, log e plumbing de leitura; feche shell dedicado e remova só sandbox anotado pelo gerenciador de arquivos após revisar conteúdo.

## Exercício e autocorreção

HEAD → refs/heads/main → commit; HEAD destacado → commit. Qual ref avança ao commitar destacado? Nenhuma branch avança automaticamente.

## Referência rápida

- `git symbolic-ref HEAD`
- `git show-ref`
- `git rev-parse HEAD`
- `git switch --detach HEAD~1`

## Fontes oficiais

- [https://git-scm.com/docs/git-symbolic-ref](https://git-scm.com/docs/git-symbolic-ref)
- [https://git-scm.com/docs/git-show-ref](https://git-scm.com/docs/git-show-ref)
- [https://git-scm.com/docs/git-switch](https://git-scm.com/docs/git-switch)

---

<!-- navigation-footer -->
[Anterior](../04-object-hashes/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../06-index-internals/README.pt-BR.md)
<!-- /navigation-footer -->
