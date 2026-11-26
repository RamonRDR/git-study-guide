# Laboratório integrado de Git avançado

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../10-archive-and-bundle/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo módulo](../../git-internals/README.pt-BR.md)
<!-- /navigation -->

**Nível:** avançado · **Tempo estimado:** 55 min

**Pré-requisitos:** [13 Git avançado](../README.pt-BR.md) · [Segurança e governança](../../security/README.pt-BR.md)

**Objetivo:** Simule review de regressão mantendo main estável e prepare transferência offline do histórico.

## O que é e por quê

Simule review de regressão mantendo main estável e prepare transferência offline do histórico. Exercício une worktree, inspeção e bundle sem alterar histórico da main. No trabalho profissional, guarde evidência da revisão testada, revise diff e valide recuperação antes da entrega.

## Prática

Crie um lab isolado novo pelo índice do módulo antes de cada prática. Rode um comando por vez; pare em resultado inesperado. Confira sandbox impresso e raiz antes de alterar. Use Git 2.34+ como base da prática; confira ajuda e pule recursos opcionais indisponíveis. Não execute em repositórios de produção.

Rode no lab novo, um comando por vez. Worktree de review deve mostrar ok, main bad; clone bundle deve coincidir com main original. Todos checks devem passar; senão pare e inspecione. Sem rede ou publicação. Remova worktree limpa normalmente; mantenha sandbox para review.

```bash
before=$(git rev-parse HEAD)
git worktree add -b review "$sandbox/review" HEAD~1
test "$(git -C "$sandbox/review" show HEAD:src/state.txt)" = ok
test "$(git show HEAD:src/state.txt)" = bad
git worktree remove "$sandbox/review"
git bundle create "$sandbox/history.bundle" main
git bundle verify "$sandbox/history.bundle"
git clone -b main "$sandbox/history.bundle" "$sandbox/recovered"
test "$(git -C "$sandbox/recovered" rev-parse HEAD)" = "$before"
test "$(git rev-parse HEAD)" = "$before"
test -z "$(git status --porcelain)"
test -z "$(git remote)"
```

## Erros comuns e segurança

Use só o lab descartável e dados fictícios. Se estado divergir, pare; inspecione status e operação antes de abortar ou recriar lab. Feche shell dedicado e remova só sandbox anotado pelo gerenciador de arquivos após revisar conteúdo.

## Exercício e autocorreção

Passe quando cada test retornar zero, main estiver limpa e tip recuperada coincidir. Explique por que bundle não é backup de toda estação.

## Referência rápida

- `git worktree add -b review "<sandbox>/review" HEAD~1`
- `git worktree remove "<sandbox>/review"`
- `git bundle create "<sandbox>/history.bundle" main`
- `git bundle verify "<sandbox>/history.bundle"`

## Fontes oficiais

- [https://git-scm.com/docs/git-worktree](https://git-scm.com/docs/git-worktree)
- [https://git-scm.com/docs/git-bundle](https://git-scm.com/docs/git-bundle)
- [https://git-scm.com/docs/git-status](https://git-scm.com/docs/git-status)

---

<!-- navigation-footer -->
[Anterior](../10-archive-and-bundle/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo módulo](../../git-internals/README.pt-BR.md)
<!-- /navigation-footer -->
