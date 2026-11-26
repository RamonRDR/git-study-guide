# Sparse checkout: selecionar arquivos de trabalho

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../06-rerere/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../08-partial-and-shallow-clone/README.pt-BR.md)
<!-- /navigation -->

**Nível:** avançado · **Tempo estimado:** 40 min

**Pré-requisitos:** [13 Git avançado](../README.pt-BR.md) · [Segurança e governança](../../security/README.pt-BR.md)

**Objetivo:** Sparse checkout limita caminhos rastreados presentes na working tree, sem removê-los dos commits.

## O que é e por quê

Sparse checkout limita caminhos rastreados presentes na working tree, sem removê-los dos commits. Cone mode seleciona diretórios; também pode manter arquivos em ancestrais. Reduz custo de checkout em monorepo. Não é controle de acesso nem necessariamente reduz histórico baixado ou objetos armazenados.

## Prática

Crie um lab isolado novo pelo índice do módulo antes de cada prática. Rode um comando por vez; pare em resultado inesperado. Confira sandbox impresso e raiz antes de alterar. Use Git 2.34+ como base da prática; confira ajuda e pule recursos opcionais indisponíveis. Não execute em repositórios de produção.

Use lab novo limpo com docs e src. Selecione docs e inspecione tree do commit; src/state.txt continua no HEAD embora ausente da working tree. Desative sparse checkout para restaurar checkout completo; não force quando houver mudanças locais.

```bash
git sparse-checkout set --cone docs
git sparse-checkout list
git ls-tree -r --name-only HEAD
test ! -f src/state.txt
git sparse-checkout disable
test -f src/state.txt
git status --short
```

## Erros comuns e segurança

Use só o lab descartável e dados fictícios. Se estado divergir, pare; inspecione status e operação antes de abortar ou recriar lab. Feche shell dedicado e remova só sandbox anotado pelo gerenciador de arquivos após revisar conteúdo.

## Exercício e autocorreção

Arquivo fora do cone foi apagado do Git? Não; snapshot continua no commit.

## Referência rápida

- `git sparse-checkout set --cone docs`
- `git sparse-checkout list`
- `git ls-tree -r --name-only HEAD`
- `git sparse-checkout disable`

## Fontes oficiais

- [https://git-scm.com/docs/git-sparse-checkout](https://git-scm.com/docs/git-sparse-checkout)
- [https://git-scm.com/docs/git-ls-tree](https://git-scm.com/docs/git-ls-tree)

---

<!-- navigation-footer -->
[Anterior](../06-rerere/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../08-partial-and-shallow-clone/README.pt-BR.md)
<!-- /navigation-footer -->
