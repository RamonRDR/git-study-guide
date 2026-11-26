# Submodules: dependências fixadas por commit

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../02-worktree/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../04-subtree/README.pt-BR.md)
<!-- /navigation -->

**Nível:** avançado · **Tempo estimado:** 45 min

**Pré-requisitos:** [13 Git avançado](../README.pt-BR.md) · [Segurança e governança](../../security/README.pt-BR.md)

**Objetivo:** O superprojeto registra gitlink (modo 160000) para commit específico de outro repositório; .gitmodules registra caminho e URL.

## O que é e por quê

O superprojeto registra gitlink (modo 160000) para commit específico de outro repositório; .gitmodules registra caminho e URL. Atualizar dependência exige commit do novo gitlink no pai. Checkout do submodule costuma ficar em detached HEAD. Use para históricos separados e revisões fixadas; evite se arquivos comuns bastarem.

## Prática

Crie um lab isolado novo pelo índice do módulo antes de cada prática. Rode um comando por vez; pare em resultado inesperado. Confira sandbox impresso e raiz antes de alterar. Use Git 2.34+ como base da prática; confira ajuda e pule recursos opcionais indisponíveis. Não execute em repositórios de produção.

Clone apenas o lab próprio em pasta irmã local e adicione como submodule. Permissão file restrita ao comando serve só para este lab local conhecido, nunca ajuste global. Inspecione .gitmodules staged e modo 160000. Antes de registrar dependência real, revise URL, licença e commit; não inicialize recursivamente repositórios desconhecidos.

```bash
git clone --no-hardlinks . "$sandbox/library"
git -c protocol.file.allow=always submodule add "$sandbox/library" vendor/library
git diff --cached -- .gitmodules
git ls-files --stage -- vendor/library
git submodule status
```

## Erros comuns e segurança

Use só o lab descartável e dados fictícios. Se estado divergir, pare; inspecione status e operação antes de abortar ou recriar lab. Feche shell dedicado e remova só sandbox anotado pelo gerenciador de arquivos após revisar conteúdo.

## Exercício e autocorreção

O que o pai armazena? ID de commit, não cópia de todos os arquivos filhos. Clone novo requer inicialização/atualização explícita.

## Referência rápida

- `git clone --no-hardlinks . "$sandbox/library"`
- `git -c protocol.file.allow=always submodule add "$sandbox/library" vendor/library`
- `git diff --cached -- .gitmodules`
- `git ls-files --stage -- vendor/library`

## Fontes oficiais

- [https://git-scm.com/docs/git-submodule](https://git-scm.com/docs/git-submodule)
- [https://git-scm.com/docs/gitsubmodules](https://git-scm.com/docs/gitsubmodules)

---

<!-- navigation-footer -->
[Anterior](../02-worktree/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../04-subtree/README.pt-BR.md)
<!-- /navigation-footer -->
