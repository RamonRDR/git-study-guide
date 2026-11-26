# Merge fast-forward

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../01-integration-safety/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../03-merge-commit/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 25 min

**Pré-requisitos:** [Segurança e recuperação antes da integração](../01-integration-safety/README.pt-BR.md)

**Objetivo:** Avançar branch sem criar commit de merge e verificar ancestralidade.

## O que é e por quê

Se ponta destino é ancestral da origem, integração pode fazer fast-forward: mover branch destino ao commit origem e atualizar index/working tree. Não precisa novo commit. `git merge --ff-only SOURCE` recusa se fast-forward impossível. Em gráfico divergente evita commit de merge inesperado. Use flags explícitas em vez de depender de padrão/configuração.

## Prática

Crie NOVO lab descartável isolado pelo módulo 00 capítulo 03 e aula do primeiro commit. Mantenha shell dedicado original, não terminal do editor. Main inicial deve ter exatamente um commit, note.txt = practice, status limpo. Feche shell do lab anterior antes de iniciar. Siga verificações do capítulo 01 antes de cada operação que altera histórico.

[Configuração isolada do lab](../../getting-started/03-first-repository/README.pt-BR.md) · [Primeiro commit](../../getting-started/05-first-commit/README.pt-BR.md) · [Segurança e recuperação antes da integração](../01-integration-safety/README.pt-BR.md)

```text
git rev-parse --show-toplevel
git branch --show-current
git status --short
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Pare se raiz não for lab descartável, branch atual não for a indicada, status não estiver limpo antes de iniciar operação ou identidades não começarem com `Study Guide Example <learner@example.invalid>`. Antes de cada commit confira também diff preparado; pare com saída inesperada.

```text
git switch -c feat/note
```

No editor de texto, crie ou edite note.txt com exatamente uma linha: feature, com quebra final. Salve, depois prepare no shell dedicado:

```text
git add -- note.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Se diff e ambas identidades corretos, faça commit:

```text
git commit -m "docs: revise feature note"
```

```text
git switch main
git log --all --oneline --graph --decorate
git rev-parse main feat/note
git status --short
```

Confirme main limpa em C1, origem C2; C2 tem C1 como pai. Depois:

```text
git merge --ff-only feat/note
git rev-parse main feat/note
git rev-list --count main
git show HEAD:note.txt
git status --short
```

Esperado: IDs iguais, dois commits em main, conteúdo feature e status limpo. Antes: main -> C1; feat/note -> C2 -> C1. Depois: main e feat/note -> C2 -> C1. Sem terceiro commit.

## Erros comuns e segurança

Se --ff-only recusar, confira gráfico; não force movimento. Não use --abort após fast-forward concluído: não há merge em andamento. Mantenha refs origem até verificar.

Após cada lab independente, feche editor e shell dedicado, então exclua somente pasta pai temporária exata anotada no módulo 00 pelo gerenciador se não precisar mais. Nunca exclua guia, pasta pessoal ou repo de trabalho.

## Exercício e autocorreção

Fast-forward adiciona commit? Resposta: não; main move ao C2 existente. Passe se main e feat/note tiverem mesmo ID. Uso profissional: exigir integração linear quando destino não tem commits exclusivos.

## Referência rápida

- `git merge --ff-only SOURCE`
- `git rev-parse main SOURCE`

## Fontes oficiais

- [Git: git-merge](https://git-scm.com/docs/git-merge)
- [Git: git-rev-parse](https://git-scm.com/docs/git-rev-parse)
- [Git: git-rev-list](https://git-scm.com/docs/git-rev-list)

---

<!-- navigation-footer -->
[Anterior](../01-integration-safety/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../03-merge-commit/README.pt-BR.md)
<!-- /navigation-footer -->
