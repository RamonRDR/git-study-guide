# Amend de um commit não publicado

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../07-cherry-pick/README.pt-BR.md) · [Índice](../README.pt-BR.md) · —
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 25 min

**Pré-requisitos:** [Laboratório isolado](../../getting-started/03-first-repository/README.pt-BR.md) · [Primeiro commit](../../getting-started/05-first-commit/README.pt-BR.md) · [Merge e conflitos](../../merge-and-conflicts/README.pt-BR.md) · [Remotos](../../remote-repositories/README.pt-BR.md) · [Cherry-pick de commits selecionados](../07-cherry-pick/README.pt-BR.md)

**Objetivo:** Corrigir tip privado mantendo pai original e ref de recuperação.

## O que é e por quê

`git commit --amend` substitui tip por commit baseado no index e normalmente mantém pais; pode mudar mensagem e/ou conteúdo. Conteúdo ou mensagem alterados geram novo ID. `--no-edit` mantém mensagem. Não edita objeto commit no lugar. Use apenas commits não publicados; em branches compartilhadas adicione commit corretivo ou revert. Diagrama: C1 -> C2 (antigo); main move para C2' com mesmo pai C1; backup fica em C2.

## Prática

Inicie um NOVO lab descartável independente pelas aulas vinculadas de configuração e primeiro commit. Mantenha a sessão Bash ou PowerShell dedicada na pasta repo registrada, com configuração Git system/global isolada, variáveis Git herdadas limpas e templates vazios. Use Git 2.40 ou posterior. Main inicial deve conter exatamente um commit com note.txt = practice, sem remotos e status limpo. Execute comandos individualmente. Antes de qualquer mudança, repita a inspeção abaixo: raiz deve ser o repo descartável registrado, branch deve ser a indicada, remotos vazios, status exatamente como descrito; ambas identidades devem começar com `Study Guide Example <learner@example.invalid>`. Antes de cada commit inspecione alterações staged e ambas identidades. Pare em saída ou falha inesperada. Nunca execute estes labs no guia ou projeto real.

```text
git rev-parse --show-toplevel
git branch --show-current
git remote -v
git status --short
git diff
git diff --cached
git log --oneline --all --graph --decorate
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Edite note.txt em editor de texto simples para exatamente uma linha `draft version` com quebra final. Salve e volte à sessão dedicada.

```text
git add -- note.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Somente se o diff staged e ambas identidades estiverem corretos, continue:

```text
git commit -m "docs: add draft"
git branch backup/draft
git rev-parse HEAD HEAD^
git status --short
```

Edite note.txt em editor de texto simples para exatamente uma linha `final version` com quebra final. Salve e volte à sessão dedicada.

```text
git add -- note.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Somente se o diff staged e ambas identidades estiverem corretos, continue:

```text
git commit --amend -m "docs: add final version"
git rev-parse HEAD backup/draft
git rev-parse HEAD^ backup/draft^
git show HEAD:note.txt
git show backup/draft:note.txt
git rev-list --count HEAD
git status --short
```

Esperado tips diferentes, pais iguais, dois commits alcançáveis de main, final version em HEAD e draft version no backup. Uso profissional: corrigir arquivo esquecido ou erro antes de publicar. Para corrigir só mensagem confirme index inalterado antes do amend.

Após o exercício, feche editores e sessão dedicada. Exclua somente o pai temporário exato registrado pelo gerenciador de arquivos se não precisar mais; nunca guia, home ou repo de trabalho.

## Erros comuns e segurança

Amend inclui mudanças staged mesmo alheias à correção. Inspecione antes. Nunca faça force push de branch compartilhada para publicar amend. Se tip privado errado foi substituído, inspecione backup/reflog e preserve branch de resgate antes de novas mudanças.

## Exercício e autocorreção

Por que dois commits com mesmo pai podem ter IDs diferentes? Resposta: conteúdo/mensagem ou metadados diferem. Passe se tip original permanece no backup e tip atual tem conteúdo pretendido e mesmo pai.

## Referência rápida

- `git commit --amend -m MESSAGE`
- `git commit --amend --no-edit`
- `git branch backup/draft`

## Fontes oficiais

- [Git: git-commit](https://git-scm.com/docs/git-commit)
- [Git: git-reflog](https://git-scm.com/docs/git-reflog)
- [Git: git-revert](https://git-scm.com/docs/git-revert)
