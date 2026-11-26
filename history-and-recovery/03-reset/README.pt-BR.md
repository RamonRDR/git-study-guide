# Reset e seus três modos

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../02-restore/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../04-revert/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 40 min

**Pré-requisitos:** [Laboratório isolado](../../getting-started/03-first-repository/README.pt-BR.md) · [Primeiro commit](../../getting-started/05-first-commit/README.pt-BR.md) · [Merge e conflitos](../../merge-and-conflicts/README.pt-BR.md) · [Remotos](../../remote-repositories/README.pt-BR.md) · [Restore: arquivos de trabalho e index](../02-restore/README.pt-BR.md)

**Objetivo:** Prever estado de branch, index e árvore em cada modo reset.

## O que é e por quê

Reset em modo commit move branch atual para commit alvo. Com --soft index e árvore não mudam; --mixed (padrão) redefine index mas mantém arquivos; --hard redefine ambos e pode sobrescrever ou excluir caminhos untracked que obstruem. Reset em modo caminho (ex. `git reset HEAD -- PATH`) altera index, não branch. Diagrama a partir de C2 limpo: soft -> main C1, index C2, disco C2; mixed -> main C1, index C1, disco C2; hard -> main C1, index C1, disco C1. Use apenas histórico não publicado quando reescrita for intencional; use revert em histórico compartilhado.

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

Edite note.txt em editor de texto simples para exatamente uma linha `second` com quebra final. Salve e volte à sessão dedicada.

```text
git add -- note.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Somente se o diff staged e ambas identidades estiverem corretos, continue:

```text
git commit -m "docs: add second version"
git branch backup/second
git rev-parse HEAD HEAD^ backup/second
git status --short
```

Registre os IDs C2 e C1. Confirme main limpa em C2, backup/second em C2, sem remotos. Execute soft primeiro:

```text
git reset --soft HEAD^
git rev-parse HEAD
git show :note.txt
git diff --cached
git diff
```

Esperado main C1; index/disco second; só diff staged. Agora redefina index ao HEAD atual sem mover main:

```text
git reset --mixed HEAD
git rev-parse HEAD
git show :note.txt
git diff
git diff --cached
```

Esperado main C1, index practice, disco second; só diff unstaged. Antes do hard, confirme raiz, main, sem remotos, backup/second ainda C2 e única alteração a edição descartável de note.txt. Não prossiga se houver outro trabalho. O seguinte descarta intencionalmente a edição.

```text
git reset --hard HEAD
git status --short
git show HEAD:note.txt
git show backup/second:note.txt
git merge --ff-only backup/second
git rev-parse HEAD backup/second
git status --short
```

Esperado practice limpo após hard; backup mantém second. Fast-forward restaura C2 sem inventar commit. Uso profissional: soft pode reagrupar commits privados, mas confira política e backup.

Após o exercício, feche editores e sessão dedicada. Exclua somente o pai temporário exato registrado pelo gerenciador de arquivos se não precisar mais; nunca guia, home ou repo de trabalho.

## Erros comuns e segurança

Hard não é desfazer genérico nem solução para push rejeitado. Branch de backup salva só dados commitados. ORIG_HEAD pode registrar tip anterior mas ser sobrescrito; use refs verificadas e reflog se disponível. Nunca conte com recuperação garantida.

## Exercício e autocorreção

Após mixed de C2 limpo para C1, onde está edição C2? Resposta: árvore, não index. Passe se prever os três locais e demonstrar tip do backup preservado.

## Referência rápida

- `git reset --soft COMMIT`
- `git reset --mixed COMMIT`
- `git reset --hard COMMIT`
- `git reset HEAD -- PATH`

## Fontes oficiais

- [Git: git-reset](https://git-scm.com/docs/git-reset)
- [Git: git-merge](https://git-scm.com/docs/git-merge)
- [Git: git-reflog](https://git-scm.com/docs/git-reflog)
