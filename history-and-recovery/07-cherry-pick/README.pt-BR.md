# Cherry-pick de commits selecionados

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../06-stash/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../08-amend/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 40 min

**Pré-requisitos:** [Laboratório isolado](../../getting-started/03-first-repository/README.pt-BR.md) · [Primeiro commit](../../getting-started/05-first-commit/README.pt-BR.md) · [Merge e conflitos](../../merge-and-conflicts/README.pt-BR.md) · [Remotos](../../remote-repositories/README.pt-BR.md) · [Stash: trabalho temporário](../06-stash/README.pt-BR.md)

**Objetivo:** Transferir commit selecionado entre branches divergentes sem merge de todo histórico.

## O que é e por quê

Cherry-pick aplica alteração introduzida por commit à branch atual e normalmente cria novo commit com pai/ID diferente. Não integra toda branch fonte. Use para correção independente/backport após conferir dependências; evite substituir integração normal. `-x` registra ID fonte na mensagem quando aplicável, útil para backports públicos; `--no-commit` aplica sem criar commit ainda. Commit de merge exige escolha mainline; não praticado. Diagrama: C1 -> F2 em fix; C1 -> M2 em main; após pick main M2 -> P3, fix permanece F2.

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

```text
git switch -c fix/note
```

Edite note.txt em editor de texto simples para exatamente uma linha `fixed` com quebra final. Salve e volte à sessão dedicada.

```text
git add -- note.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Somente se o diff staged e ambas identidades estiverem corretos, continue:

```text
git commit -m "docs: fix note"
git switch main
```

Crie overview.txt com linha `overview` e quebra final em main. Inspecione raiz, branch, status e identidades.

```text
git add -- overview.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Somente se o diff staged e ambas identidades estiverem corretos, continue:

```text
git commit -m "docs: add overview"
git log --all --oneline --graph
git show fix/note
git status --short
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Confirme main limpa, correção independente e identidades fictícias. Tip fonte é único commit de correção. Execute:

```text
git cherry-pick -x fix/note
git log --all --oneline --graph
git rev-parse HEAD fix/note
git show HEAD:note.txt
git show HEAD:overview.txt
git status --short
```

Esperado IDs diferentes, fixed e overview preservados, status limpo. Commit fonte permanece em fix/note; main tem novo commit com pai M2. Em backports reais inspecione pré-requisitos e teste antes de publicar.

Após o exercício, feche editores e sessão dedicada. Exclua somente o pai temporário exato registrado pelo gerenciador de arquivos se não precisar mais; nunca guia, home ou repo de trabalho.

## Erros comuns e segurança

Edições sobrepostas podem conflitar. Inspecione status e marcadores, adicione caminhos resolvidos e use cherry-pick --continue, ou cherry-pick --abort para tentar restaurar estado pré-sequência. Não aplique duas vezes cegamente; patch pode já existir. Não reescreva histórico compartilhado para remover duplicatas.

## Exercício e autocorreção

Commit fonte é ancestral do novo tip main só porque alteração foi selecionada? Resposta: não necessariamente; lab tem ancestralidade distinta. Passe se ambos arquivos sobrevivem, IDs diferem e ref fonte não muda.

## Referência rápida

- `git cherry-pick COMMIT`
- `git cherry-pick -x COMMIT`
- `git cherry-pick --continue`
- `git cherry-pick --abort`

## Fontes oficiais

- [Git: git-cherry-pick](https://git-scm.com/docs/git-cherry-pick)
- [Git: git-merge-base](https://git-scm.com/docs/git-merge-base)

---

<!-- navigation-footer -->
[Anterior](../06-stash/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../08-amend/README.pt-BR.md)
<!-- /navigation-footer -->
