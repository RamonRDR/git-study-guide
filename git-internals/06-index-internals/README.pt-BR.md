# Internals do index: entradas preparadas

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../05-refs-and-head/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../07-loose-objects-and-packfiles/README.pt-BR.md)
<!-- /navigation -->

**Nível:** avançado · **Tempo estimado:** 45 min

**Pré-requisitos:** [14 Internals do Git](../README.pt-BR.md) · [Git avançado](../../advanced-git/README.pt-BR.md)

**Objetivo:** Index registra caminhos, modos, IDs e metadados da tree futura.

## O que é e por quê

Index registra caminhos, modos, IDs e metadados da tree futura. Entradas comuns têm stage 0; merge não resolvido pode ter stages 1 (base), 2 (ours) e 3 (theirs), conforme conflito. `write-tree` materializa tree do index resolvido sem commit. Evite editar index binário diretamente.

```text
working tree --add--> index --write-tree--> tree object
                       |                      |
                       +--- git commit ------> commit -> branch ref advances
```

Arquivo → add → index (stage 0) → write-tree → objeto tree; commit também avança branch atual.

## Prática

Crie lab isolado novo pelo índice vinculado de Git avançado antes de cada prática. Rode comandos individualmente e pare em resultado inesperado. Confira raiz e sandbox impresso. Base Git 2.34+, Bash (Git Bash no Windows).

Prepare uma edição fictícia no lab novo. Compare IDs blob staged e HEAD. `git write-tree` grava ou reutiliza trees; não move HEAD. Use `git ls-files -u` para inspecionar entradas em lab de conflito, não para criar conflitos aqui. Restaure arquivo staged e trabalho só neste lab descartável.

```bash
before=$(git rev-parse HEAD)
git ls-files --stage
printf '%s\n' reviewed > src/state.txt
git add -- src/state.txt
git ls-files --stage -- src/state.txt
git diff --cached -- src/state.txt
git write-tree
test "$(git rev-parse HEAD)" = "$before"
git restore --staged --worktree -- src/state.txt
git status --short
```

## Erros comuns e segurança

Use só lab descartável. Nunca altere arquivos de objetos/refs à mão, force prune ou experimente em repo real. Se estado divergir, inspecione status, log e plumbing de leitura; feche shell dedicado e remova só sandbox anotado pelo gerenciador de arquivos após revisar conteúdo.

## Exercício e autocorreção

Arquivo → add → index (stage 0) → write-tree → objeto tree; commit também avança branch atual. Por que write-tree pode falhar em conflito? Index tem entradas não resolvidas.

## Referência rápida

- `git ls-files --stage`
- `git add -- src/state.txt`
- `git ls-files --stage -- src/state.txt`
- `git diff --cached -- src/state.txt`

## Fontes oficiais

- [https://git-scm.com/docs/git-ls-files](https://git-scm.com/docs/git-ls-files)
- [https://git-scm.com/docs/git-write-tree](https://git-scm.com/docs/git-write-tree)
- [https://git-scm.com/docs/gitformat-index](https://git-scm.com/docs/gitformat-index)

---

<!-- navigation-footer -->
[Anterior](../05-refs-and-head/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../07-loose-objects-and-packfiles/README.pt-BR.md)
<!-- /navigation-footer -->
