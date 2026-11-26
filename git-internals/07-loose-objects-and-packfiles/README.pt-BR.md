# Objetos soltos e packfiles

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../06-index-internals/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../08-gc-and-maintenance/README.pt-BR.md)
<!-- /navigation -->

**Nível:** avançado · **Tempo estimado:** 40 min

**Pré-requisitos:** [14 Internals do Git](../README.pt-BR.md) · [Git avançado](../../advanced-git/README.pt-BR.md)

**Objetivo:** Objetos podem estar individuais ou em packs com índices e compressão delta.

## O que é e por quê

Objetos podem estar individuais ou em packs com índices e compressão delta. Empacotar muda representação, não identidade ou grafo lógico. Git usa deltas para compressão apesar de snapshots lógicos serem trees. Use count-objects para inspecionar tamanho, sem deduzir histórico do layout em disco.

```text
logical object ID B
       |
       +-> loose object (before repack)
       +-> pack + index (after repack)
          same logical bytes
```

As setas mostram relações de referências ou operações, não caminhos de arquivos.

## Prática

Crie lab isolado novo pelo índice vinculado de Git avançado antes de cada prática. Rode comandos individualmente e pare em resultado inesperado. Confira raiz e sandbox impresso. Base Git 2.34+, Bash (Git Bash no Windows).

No lab pequeno novo, rode `git repack -a` (sem opção de remoção). Compare HEAD e mesmo conteúdo blob antes/depois. Contagens e tamanhos variam; não presuma número de packs. Use ferramentas só em repos próprios e nunca apague packfiles manualmente.

```bash
before=$(git rev-parse HEAD)
git count-objects -v
git repack -a
git count-objects -v
test "$(git rev-parse HEAD)" = "$before"
git cat-file -p HEAD:src/state.txt
```

## Erros comuns e segurança

Use só lab descartável. Nunca altere arquivos de objetos/refs à mão, force prune ou experimente em repo real. Se estado divergir, inspecione status, log e plumbing de leitura; feche shell dedicado e remova só sandbox anotado pelo gerenciador de arquivos após revisar conteúdo.

## Exercício e autocorreção

Blob armazenado como delta pode ser lido normalmente? Sim; Git reconstrói bytes originais.

## Referência rápida

- `git count-objects -v`
- `git repack -a`
- `git count-objects -v`
- `git cat-file -p HEAD:src/state.txt`

## Fontes oficiais

- [https://git-scm.com/docs/git-repack](https://git-scm.com/docs/git-repack)
- [https://git-scm.com/docs/git-count-objects](https://git-scm.com/docs/git-count-objects)
- [https://git-scm.com/docs/gitformat-pack](https://git-scm.com/docs/gitformat-pack)

---

<!-- navigation-footer -->
[Anterior](../06-index-internals/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../08-gc-and-maintenance/README.pt-BR.md)
<!-- /navigation-footer -->
