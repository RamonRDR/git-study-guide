# Blame e grep: investigar mudanças

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../08-partial-and-shallow-clone/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../10-archive-and-bundle/README.pt-BR.md)
<!-- /navigation -->

**Nível:** avançado · **Tempo estimado:** 35 min

**Pré-requisitos:** [13 Git avançado](../README.pt-BR.md) · [Segurança e governança](../../security/README.pt-BR.md)

**Objetivo:** Blame atribui linhas selecionadas a commits conforme histórico e opções; não mede responsabilidade nem qualidade.

## O que é e por quê

Blame atribui linhas selecionadas a commits conforme histórico e opções; não mede responsabilidade nem qualidade. Grep busca arquivos rastreados de trabalho por padrão ou tree nomeada com revisão. Combine com show/log para entender contexto de review, não culpar autor.

## Prática

Crie um lab isolado novo pelo índice do módulo antes de cada prática. Rode um comando por vez; pare em resultado inesperado. Confira sandbox impresso e raiz antes de alterar. Use Git 2.34+ como base da prática; confira ajuda e pule recursos opcionais indisponíveis. Não execute em repositórios de produção.

Compare busca no HEAD e no pai. grep retorna 1 sem correspondência; não é necessariamente erro da investigação. `git blame` deve identificar mudança da linha de estado. Evite buscar ou publicar dados privados; mantenha saída fictícia.

```bash
git blame -- src/state.txt
git grep -n bad HEAD -- src
git grep -n ok HEAD~1 -- src
git log -p -- src/state.txt
```

## Erros comuns e segurança

Use só o lab descartável e dados fictícios. Se estado divergir, pare; inspecione status e operação antes de abortar ou recriar lab. Feche shell dedicado e remova só sandbox anotado pelo gerenciador de arquivos após revisar conteúdo.

## Exercício e autocorreção

Por que inspecionar commit após blame? Atribuição de linha sozinha não explica intenção nem contexto.

## Referência rápida

- `git blame -- src/state.txt`
- `git grep -n bad HEAD -- src`
- `git grep -n ok HEAD~1 -- src`
- `git log -p -- src/state.txt`

## Fontes oficiais

- [https://git-scm.com/docs/git-blame](https://git-scm.com/docs/git-blame)
- [https://git-scm.com/docs/git-grep](https://git-scm.com/docs/git-grep)
- [https://git-scm.com/docs/git-log](https://git-scm.com/docs/git-log)

---

<!-- navigation-footer -->
[Anterior](../08-partial-and-shallow-clone/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../10-archive-and-bundle/README.pt-BR.md)
<!-- /navigation-footer -->
