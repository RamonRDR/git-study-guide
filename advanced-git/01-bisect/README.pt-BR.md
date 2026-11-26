# Bisect: localizar uma regressão

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Módulo anterior](../../security/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../02-worktree/README.pt-BR.md)
<!-- /navigation -->

**Nível:** avançado · **Tempo estimado:** 45 min

**Pré-requisitos:** [13 Git avançado](../README.pt-BR.md) · [Segurança e governança](../../security/README.pt-BR.md)

**Objetivo:** Localize o primeiro commit ruim usando extremos bom e ruim conhecidos.

## O que é e por quê

Localize o primeiro commit ruim usando extremos bom e ruim conhecidos. Git reduz candidatos alcançáveis escolhendo commits para testar; não diagnostica o defeito sozinho. Use teste determinístico em ambiente estável; se um commit não puder ser testado, use skip, que pode deixar vários candidatos. Em incidente profissional, registre o intervalo testado e confirme o resultado contra seu pai antes de propor correção.

## Prática

Crie um lab isolado novo pelo índice do módulo antes de cada prática. Rode um comando por vez; pare em resultado inesperado. Confira sandbox impresso e raiz antes de alterar. Use Git 2.34+ como base da prática; confira ajuda e pule recursos opcionais indisponíveis. Não execute em repositórios de produção.

O commit intermediário do lab ainda tem `ok` em `src/state.txt`. Após `git bisect start`, inspecione o commit escolhido; marque good somente após confirmar `ok`. O resultado deve ser o commit mais novo. Reset retorna ao checkout original. Se divergir, execute reset e inspecione o lab.

```bash
git bisect start HEAD HEAD~2
git show HEAD:src/state.txt
git bisect good
git bisect log
git bisect reset
git status --short
```

## Erros comuns e segurança

Use só o lab descartável e dados fictícios. Se estado divergir, pare; inspecione status e operação antes de abortar ou recriar lab. Feche shell dedicado e remova só sandbox anotado pelo gerenciador de arquivos após revisar conteúdo.

## Exercício e autocorreção

Por que não marcar automaticamente um commit pulado como bom? Ele pode conter a regressão; o intervalo perde confiabilidade.

## Referência rápida

- `git bisect start HEAD HEAD~2`
- `git show HEAD:src/state.txt`
- `git bisect good`
- `git bisect log`

## Fontes oficiais

- [https://git-scm.com/docs/git-bisect](https://git-scm.com/docs/git-bisect)
- [https://git-scm.com/docs/git-rev-list](https://git-scm.com/docs/git-rev-list)

---

<!-- navigation-footer -->
[Módulo anterior](../../security/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../02-worktree/README.pt-BR.md)
<!-- /navigation-footer -->
