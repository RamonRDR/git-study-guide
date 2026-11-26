# Subtree: integrar conteúdo de outra origem

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../03-submodules/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../05-hooks/README.pt-BR.md)
<!-- /navigation -->

**Nível:** avançado · **Tempo estimado:** 40 min

**Pré-requisitos:** [13 Git avançado](../README.pt-BR.md) · [Segurança e governança](../../security/README.pt-BR.md)

**Objetivo:** Ao contrário de submodule, subtree armazena arquivos comuns rastreados sob prefixo.

## O que é e por quê

Ao contrário de submodule, subtree armazena arquivos comuns rastreados sob prefixo. O auxiliar opcional git subtree importa e sincroniza outro histórico; --squash importa snapshot condensado em vez de unir todo histórico. Facilita consumo, mas sincronização e proveniência continuam responsabilidades.

## Prática

Crie um lab isolado novo pelo índice do módulo antes de cada prática. Rode um comando por vez; pare em resultado inesperado. Confira sandbox impresso e raiz antes de alterar. Use Git 2.34+ como base da prática; confira ajuda e pule recursos opcionais indisponíveis. Não execute em repositórios de produção.

Confira `git subtree -h` (ajuda pode retornar código não zero). Se indisponível, fique na comparação conceitual; não baixe scripts arbitrários. Clone lab local conhecido, importe sob prefixo novo e inspecione arquivos e grafo. Sem rede. Revise licenças e evite sobrescrever prefixo existente.

```bash
git clone --no-hardlinks . "$sandbox/library"
git subtree add --prefix=vendor/library "$sandbox/library" main --squash
git ls-files --stage -- vendor/library
git log --oneline --graph --all -6
```

## Erros comuns e segurança

Use só o lab descartável e dados fictícios. Se estado divergir, pare; inspecione status e operação antes de abortar ou recriar lab. Feche shell dedicado e remova só sandbox anotado pelo gerenciador de arquivos após revisar conteúdo.

## Exercício e autocorreção

Qual opção mantém metadados de checkout independentes? Submodule; subtree coloca arquivos comuns no pai.

## Referência rápida

- `git clone --no-hardlinks . "$sandbox/library"`
- `git subtree add --prefix=vendor/library "$sandbox/library" main --squash`
- `git ls-files --stage -- vendor/library`
- `git log --oneline --graph --all -6`

## Fontes oficiais

- [https://git-scm.com/docs/git-merge](https://git-scm.com/docs/git-merge)
- [https://github.com/git/git/blob/master/contrib/subtree/git-subtree.adoc](https://github.com/git/git/blob/master/contrib/subtree/git-subtree.adoc)
- [https://git-scm.com/docs/gitsubmodules](https://git-scm.com/docs/gitsubmodules)

---

<!-- navigation-footer -->
[Anterior](../03-submodules/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../05-hooks/README.pt-BR.md)
<!-- /navigation-footer -->
