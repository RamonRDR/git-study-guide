# Worktrees: diretórios de trabalho paralelos

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../01-bisect/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../03-submodules/README.pt-BR.md)
<!-- /navigation -->

**Nível:** avançado · **Tempo estimado:** 40 min

**Pré-requisitos:** [13 Git avançado](../README.pt-BR.md) · [Segurança e governança](../../security/README.pt-BR.md)

**Objetivo:** Uma worktree vinculada tem checkout, HEAD e index próprios, mas compartilha a maioria das refs e objetos com a principal.

## O que é e por quê

Uma worktree vinculada tem checkout, HEAD e index próprios, mas compartilha a maioria das refs e objetos com a principal. Permite hotfix enquanto outra tarefa está aberta, sem stash ou clone completo. Git normalmente impede checkout simultâneo da mesma branch. Worktrees não isolam segurança nem configuração.

## Prática

Crie um lab isolado novo pelo índice do módulo antes de cada prática. Rode um comando por vez; pare em resultado inesperado. Confira sandbox impresso e raiz antes de alterar. Use Git 2.34+ como base da prática; confira ajuda e pule recursos opcionais indisponíveis. Não execute em repositórios de produção.

Crie branch review distinta em pasta irmã; compare HEAD e liste as duas worktrees. Confira limpeza da vinculada antes de remover. Não force remoção de worktree suja nem apague diretórios manualmente; consulte `git worktree list` e procedimento oficial de repair se movida.

```bash
git worktree add -b review "$sandbox/review" HEAD~1
git worktree list
git -C "$sandbox/review" status --short
git -C "$sandbox/review" rev-parse HEAD
git rev-parse HEAD
git worktree remove "$sandbox/review"
git worktree list
```

## Erros comuns e segurança

Use só o lab descartável e dados fictícios. Se estado divergir, pare; inspecione status e operação antes de abortar ou recriar lab. Feche shell dedicado e remova só sandbox anotado pelo gerenciador de arquivos após revisar conteúdo.

## Exercício e autocorreção

Worktree vinculada tem banco de objetos separado? Normalmente não; checkout e index são separados.

## Referência rápida

- `git worktree add -b review "$sandbox/review" HEAD~1`
- `git worktree list`
- `git -C "$sandbox/review" status --short`
- `git -C "$sandbox/review" rev-parse HEAD`

## Fontes oficiais

- [https://git-scm.com/docs/git-worktree](https://git-scm.com/docs/git-worktree)
- [https://git-scm.com/docs/gitrepository-layout](https://git-scm.com/docs/gitrepository-layout)

---

<!-- navigation-footer -->
[Anterior](../01-bisect/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../03-submodules/README.pt-BR.md)
<!-- /navigation-footer -->
