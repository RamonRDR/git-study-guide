# Integração por squash

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../04-conflict-resolution/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../06-rebase-and-conflicts/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 30 min

**Pré-requisitos:** [Resolver e abortar conflitos de merge](../04-conflict-resolution/README.pt-BR.md)

**Objetivo:** Combinar mudanças em um novo commit sem unir ancestralidade da origem.

## O que é e por quê

`git merge --squash SOURCE` prepara working tree e index combinados como merge mas não move HEAD, cria commit nem define MERGE_HEAD. Commit comum posterior tem um pai, ponta anterior do destino. Commits origem continuam na branch; mudanças podem estar no novo snapshot sem ancestralidade original. Squash merge do GitHub é opção de integração da plataforma com topologia semelhante de um commit, não literalmente este comando local nem garantia de metadados idênticos.

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

No editor de texto, crie ou edite detail.txt com exatamente uma linha: detail, com quebra final. Salve, depois prepare no shell dedicado:

```text
git add -- detail.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Se diff e ambas identidades corretos, faça commit:

```text
git commit -m "docs: add detail"
```

```text
git switch main
```

No editor de texto, crie ou edite overview.txt com exatamente uma linha: overview, com quebra final. Salve, depois prepare no shell dedicado:

```text
git add -- overview.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Se diff e ambas identidades corretos, faça commit:

```text
git commit -m "docs: add overview"
```

```text
git rev-parse --show-toplevel
git branch --show-current
git status --short
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Confirme main limpa e identidades. Anote IDs main e feature. Prepare squash sem commit ainda:

```text
git rev-parse main feat/note
git merge --squash feat/note
git rev-parse HEAD
git diff --cached
git status --short
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

HEAD inalterado; modificação note e adição detail preparadas. Se conflito ou estado inesperado, pare; merge --abort não desfaz squash. Neste lab descarte apenas pasta descartável verificada e reinicie. Se correto, registre:

```text
git commit -m "docs: integrate feature changes"
git rev-list --parents -1 HEAD
git log --oneline main..feat/note
git show HEAD:note.txt
git show HEAD:detail.txt
git show HEAD:overview.txt
git status --short
```

Esperado um pai, dois commits origem ainda em main..feat/note, três conteúdos presentes e status limpo. Diagrama: main -> S -> C4 -> C1; feat/note -> C3 -> C2 -> C1. S contém mudanças feature mas C3 não é pai/ancestral de S neste lab.

## Erros comuns e segurança

Não use squash para apagar segredo de histórico existente. Ancestralidade origem permanece na branch origem. Exclusão protegida pode recusar após squash; confira conteúdo e política em vez de forçar. Sem operação compartilhada aqui.

Após cada lab independente, feche editor e shell dedicado, então exclua somente pasta pai temporária exata anotada no módulo 00 pelo gerenciador se não precisar mais. Nunca exclua guia, pasta pessoal ou repo de trabalho.

## Exercício e autocorreção

Commit squash é merge de dois pais? Não. Passe se HEAD ficar igual até commit, novo commit tiver um pai e mudanças origem presentes. Uso profissional: combinar commits pequenos em mudança lógica sob política acordada.

## Referência rápida

- `git merge --squash SOURCE`
- `git diff --cached`
- `git commit -m MESSAGE`

## Fontes oficiais

- [Git: git-merge](https://git-scm.com/docs/git-merge)
- [Git: git-commit](https://git-scm.com/docs/git-commit)
- [Git: git-rev-list](https://git-scm.com/docs/git-rev-list)
- [Git: git-log](https://git-scm.com/docs/git-log)
