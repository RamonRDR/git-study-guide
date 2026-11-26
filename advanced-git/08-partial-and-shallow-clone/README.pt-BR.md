# Clones parciais e rasos

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../07-sparse-checkout/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../09-blame-and-grep/README.pt-BR.md)
<!-- /navigation -->

**Nível:** avançado · **Tempo estimado:** 45 min

**Pré-requisitos:** [13 Git avançado](../README.pt-BR.md) · [Segurança e governança](../../security/README.pt-BR.md)

**Objetivo:** Clone raso trunca ancestralidade visível com --depth; clone parcial pede conjunto filtrado, como --filter=blob:none, e pode buscar objetos omitidos sob demanda de remote promisor.

## O que é e por quê

Clone raso trunca ancestralidade visível com --depth; clone parcial pede conjunto filtrado, como --filter=blob:none, e pode buscar objetos omitidos sob demanda de remote promisor. Sparse checkout seleciona caminhos de trabalho, outra dimensão. Use raso em CI limitado quando histórico profundo for dispensável; parcial exige suporte do servidor e conectividade para objetos omitidos.

## Prática

Crie um lab isolado novo pelo índice do módulo antes de cada prática. Rode um comando por vez; pare em resultado inesperado. Confira sandbox impresso e raiz antes de alterar. Use Git 2.34+ como base da prática; confira ajuda e pule recursos opcionais indisponíveis. Não execute em repositórios de produção.

Use --no-local para exercitar depth contra caminho local próprio em vez da otimização de clone local. Confira um commit visível e shallow=true. `git fetch --unshallow` da mesma fonte completa restaura ancestralidade. Clone parcial é comparação conceitual aqui: não contate servidor nem presuma filtro aceito.

```bash
git clone --no-local --depth 1 . "$sandbox/shallow"
git -C "$sandbox/shallow" rev-parse --is-shallow-repository
git -C "$sandbox/shallow" rev-list --count HEAD
git -C "$sandbox/shallow" fetch --unshallow
git -C "$sandbox/shallow" rev-list --count HEAD
```

## Erros comuns e segurança

Use só o lab descartável e dados fictícios. Se estado divergir, pare; inspecione status e operação antes de abortar ou recriar lab. Feche shell dedicado e remova só sandbox anotado pelo gerenciador de arquivos após revisar conteúdo.

## Exercício e autocorreção

Qual técnica pode omitir blobs mantendo ancestralidade de commits? Clone parcial, se o filtro for suportado.

## Referência rápida

- `git clone --no-local --depth 1 . "$sandbox/shallow"`
- `git -C "$sandbox/shallow" rev-parse --is-shallow-repository`
- `git -C "$sandbox/shallow" rev-list --count HEAD`
- `git -C "$sandbox/shallow" fetch --unshallow`

## Fontes oficiais

- [https://git-scm.com/docs/git-clone](https://git-scm.com/docs/git-clone)
- [https://git-scm.com/docs/git-fetch](https://git-scm.com/docs/git-fetch)
- [https://git-scm.com/docs/partial-clone](https://git-scm.com/docs/partial-clone)

---

<!-- navigation-footer -->
[Anterior](../07-sparse-checkout/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../09-blame-and-grep/README.pt-BR.md)
<!-- /navigation-footer -->
