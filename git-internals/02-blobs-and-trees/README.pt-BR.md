# Blobs e trees: nomes e conteúdo

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../01-object-database/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../03-commits-and-tags/README.pt-BR.md)
<!-- /navigation -->

**Nível:** avançado · **Tempo estimado:** 45 min

**Pré-requisitos:** [14 Internals do Git](../README.pt-BR.md) · [Git avançado](../../advanced-git/README.pt-BR.md)

**Objetivo:** Blob contém conteúdo, não caminho ou nome.

## O que é e por quê

Blob contém conteúdo, não caminho ou nome. Tree associa nome e modo a ID de objeto; subdiretórios usam trees. Mesmos bytes podem compartilhar blob com nomes distintos. Tree Git é estrutura de snapshot, não lista de patches. Review profissional pode comparar trees independentemente de checkout.

```text
tree T
  docs/  -> tree D -> guide.txt -> blob A
  src/   -> tree S -> state.txt -> blob B
```

As setas mostram relações de referências ou operações, não caminhos de arquivos.

## Prática

Crie lab isolado novo pelo índice vinculado de Git avançado antes de cada prática. Rode comandos individualmente e pare em resultado inesperado. Confira raiz e sandbox impresso. Base Git 2.34+, Bash (Git Bash no Windows).

Leia tree e blob por revisão:caminho; compare IDs do blob de estado entre dois commits. IDs diferem porque bytes mudaram. Não manipule arquivos de objetos diretamente; use comandos Git.

```bash
git ls-tree HEAD
git ls-tree -r HEAD
git cat-file -t HEAD:src/state.txt
git cat-file -p HEAD:src/state.txt
git rev-parse HEAD:src/state.txt
git rev-parse HEAD~1:src/state.txt
git diff HEAD~1 HEAD -- src/state.txt
```

## Erros comuns e segurança

Use só lab descartável. Nunca altere arquivos de objetos/refs à mão, force prune ou experimente em repo real. Se estado divergir, inspecione status, log e plumbing de leitura; feche shell dedicado e remova só sandbox anotado pelo gerenciador de arquivos após revisar conteúdo.

## Exercício e autocorreção

Renomear arquivo sem mudar conteúdo pode preservar qual ID? O blob; trees com os nomes mudam.

## Referência rápida

- `git ls-tree HEAD`
- `git ls-tree -r HEAD`
- `git cat-file -t HEAD:src/state.txt`
- `git cat-file -p HEAD:src/state.txt`

## Fontes oficiais

- [https://git-scm.com/docs/git-ls-tree](https://git-scm.com/docs/git-ls-tree)
- [https://git-scm.com/docs/git-cat-file](https://git-scm.com/docs/git-cat-file)
- [https://git-scm.com/docs/git-diff](https://git-scm.com/docs/git-diff)

---

<!-- navigation-footer -->
[Anterior](../01-object-database/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../03-commits-and-tags/README.pt-BR.md)
<!-- /navigation-footer -->
