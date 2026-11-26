# Laboratório integrado de Git internals

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../10-porcelain-and-plumbing/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo módulo](../../command-reference/README.pt-BR.md)
<!-- /navigation -->

**Nível:** avançado · **Tempo estimado:** 55 min

**Pré-requisitos:** [14 Internals do Git](../README.pt-BR.md) · [Git avançado](../../advanced-git/README.pt-BR.md)

**Objetivo:** Inspecione snapshot da ref branch passando por commit, tree raiz e blob.

## O que é e por quê

Inspecione snapshot da ref branch passando por commit, tree raiz e blob. Depois compare stage com HEAD sem commit e confira que packing não altera identidade. É diagnóstico, não reparo manual de objetos. Investigação profissional registra IDs e comandos exatos, não conteúdo privado.

```text
HEAD -> refs/heads/main -> commit -> root tree -> subtree -> blob
index ---------------------------> prospective tree (write-tree)
```

Passe quando todos testes retornarem zero.

## Prática

Crie lab isolado novo pelo índice vinculado de Git avançado antes de cada prática. Rode comandos individualmente e pare em resultado inesperado. Confira raiz e sandbox impresso. Base Git 2.34+, Bash (Git Bash no Windows).

Use lab novo. Tipos esperados commit, tree e blob; tree staged difere da original, HEAD fica fixo e restore volta a estado limpo. Repack sem flags de remoção; confirme blob original legível. Pare em teste falho, inspecione estado e descarte só lab se necessário.

```bash
commit=$(git rev-parse HEAD)
tree=$(git rev-parse HEAD^{tree})
blob=$(git rev-parse HEAD:src/state.txt)
test "$(git cat-file -t "$commit")" = commit
test "$(git cat-file -t "$tree")" = tree
test "$(git cat-file -t "$blob")" = blob
test "$(git cat-file -p "$blob")" = bad
printf '%s\n' reviewed > src/state.txt
git add -- src/state.txt
staged=$(git write-tree)
test "$staged" != "$tree"
test "$(git rev-parse HEAD)" = "$commit"
git restore --staged --worktree -- src/state.txt
git repack -a
test "$(git rev-parse HEAD)" = "$commit"
test "$(git cat-file -p "$blob")" = bad
test -z "$(git status --porcelain)"
test -z "$(git remote)"
```

## Erros comuns e segurança

Use só lab descartável. Nunca altere arquivos de objetos/refs à mão, force prune ou experimente em repo real. Se estado divergir, inspecione status, log e plumbing de leitura; feche shell dedicado e remova só sandbox anotado pelo gerenciador de arquivos após revisar conteúdo.

## Exercício e autocorreção

Passe quando todos testes retornarem zero. Explique grafo: HEAD → branch → commit → tree → blob; index → tree futura. Por que repack é transparente ao grafo? IDs não dependem da codificação de armazenamento.

## Referência rápida

- `git add -- src/state.txt`
- `git restore --staged --worktree -- src/state.txt`
- `git repack -a`

## Fontes oficiais

- [https://git-scm.com/docs/git-cat-file](https://git-scm.com/docs/git-cat-file)
- [https://git-scm.com/docs/git-write-tree](https://git-scm.com/docs/git-write-tree)
- [https://git-scm.com/docs/git-repack](https://git-scm.com/docs/git-repack)
- [https://git-scm.com/docs/git-rev-parse](https://git-scm.com/docs/git-rev-parse)

---

<!-- navigation-footer -->
[Anterior](../10-porcelain-and-plumbing/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo módulo](../../command-reference/README.pt-BR.md)
<!-- /navigation-footer -->
