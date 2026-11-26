# Hashes e identidade dos objetos

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../03-commits-and-tags/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../05-refs-and-head/README.pt-BR.md)
<!-- /navigation -->

**Nível:** avançado · **Tempo estimado:** 40 min

**Pré-requisitos:** [14 Internals do Git](../README.pt-BR.md) · [Git avançado](../../advanced-git/README.pt-BR.md)

**Objetivo:** IDs derivam de tipo, comprimento em bytes e conteúdo, com cabeçalho de objeto Git.

## O que é e por quê

IDs derivam de tipo, comprimento em bytes e conteúdo, com cabeçalho de objeto Git. SHA-1 e SHA-256 são formatos de repositório; não presuma 40 caracteres sempre. Checksum genérico dos bytes não é ID blob Git. Hash não é assinatura nem controle de acesso.

## Prática

Crie lab isolado novo pelo índice vinculado de Git avançado antes de cada prática. Rode comandos individualmente e pare em resultado inesperado. Confira raiz e sandbox impresso. Base Git 2.34+, Bash (Git Bash no Windows).

Calcule ID blob bruto sem gravar objetos (`--no-filters` evita conversões de atributos). Compare mesmos bytes duas vezes e depois bytes alterados. Git informa formato com rev-parse; evite hashes fixos ou IDs curtos como identificadores globalmente únicos.

```bash
git rev-parse --show-object-format
git hash-object --no-filters src/state.txt
git rev-parse HEAD:src/state.txt
printf '%s\n' bad | git hash-object --stdin
printf '%s\n' ok | git hash-object --stdin
```

## Erros comuns e segurança

Use só lab descartável. Nunca altere arquivos de objetos/refs à mão, force prune ou experimente em repo real. Se estado divergir, inspecione status, log e plumbing de leitura; feche shell dedicado e remova só sandbox anotado pelo gerenciador de arquivos após revisar conteúdo.

## Exercício e autocorreção

Por que commits com mesma tree podem diferir? IDs de pais, dados de autor/committer, horários ou mensagens podem diferir.

## Referência rápida

- `git rev-parse --show-object-format`
- `git hash-object --no-filters src/state.txt`
- `git rev-parse HEAD:src/state.txt`

## Fontes oficiais

- [https://git-scm.com/docs/git-hash-object](https://git-scm.com/docs/git-hash-object)
- [https://git-scm.com/docs/git-rev-parse](https://git-scm.com/docs/git-rev-parse)
- [https://git-scm.com/docs/hash-function-transition](https://git-scm.com/docs/hash-function-transition)

---

<!-- navigation-footer -->
[Anterior](../03-commits-and-tags/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../05-refs-and-head/README.pt-BR.md)
<!-- /navigation-footer -->
