# Inspecione antes de desfazer

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
— · [Índice](../README.pt-BR.md) · [Próximo](../02-restore/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 20 min

**Pré-requisitos:** [Laboratório isolado](../../getting-started/03-first-repository/README.pt-BR.md) · [Primeiro commit](../../getting-started/05-first-commit/README.pt-BR.md) · [Merge e conflitos](../../merge-and-conflicts/README.pt-BR.md) · [Remotos](../../remote-repositories/README.pt-BR.md)

**Objetivo:** Escolher a operação menos destrutiva conforme o estado Git afetado.

## O que é e por quê

Desfazer não é uma única operação. Restore altera arquivo selecionado na árvore de trabalho ou index, não o tip. Reset em modo commit move a branch atual; soft preserva index e arquivos, mixed restaura index, hard também substitui arquivos rastreados. Revert cria novo commit inverso. Amend substitui o tip; cherry-pick reaplica alteração selecionada como novo commit no caso normal. Stash guarda trabalho local temporário. Reflog registra movimentos locais de refs e pode localizar commits retidos. Diagrama: árvore de trabalho -> index -> commit; branch aponta para commit e HEAD normalmente aponta para branch. Alterar um local não implica alterar outros. Histórico publicado normalmente deve ser corrigido com novo commit, não reescrito.

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

Edite note.txt em editor de texto simples para exatamente uma linha `draft` com quebra final. Salve e volte à sessão dedicada.

```text
git status --short
git diff
git diff --cached
git show HEAD:note.txt
git reflog -n 3
```

Esperado: alteração unstaged, diff staged vazio, practice commitado inalterado. Não desfaça ainda. Identifique se trabalho é untracked, unstaged, staged, commitado ou compartilhado. Em incidente real, interrompa escritas, preserve evidências e faça backup independente dos arquivos de valor antes de escolher comando. Branch de backup preserva apenas snapshots commitados; não é backup de arquivos de trabalho ou index. Neste lab o draft é descartável.

Após o exercício, feche editores e sessão dedicada. Exclua somente o pai temporário exato registrado pelo gerenciador de arquivos se não precisar mais; nunca guia, home ou repo de trabalho.

## Erros comuns e segurança

Nunca suponha recuperação de arquivo untracked ou não salvo. Reflogs são locais e podem expirar; garbage collection pode remover objetos inalcançáveis. Não execute limpeza ou garbage collection para resolver perda. Busque ajuda antes de alterar histórico compartilhado.

## Exercício e autocorreção

Um commit publicado está errado; qual operação normalmente preserva colaboração? Dica: adicione mudança inversa. Resposta: revert. Passe se explicar por que branch de backup não salva arquivo unstaged.

## Referência rápida

- `git status --short`
- `git diff`
- `git diff --cached`
- `git log --all --graph --oneline`

## Fontes oficiais

- [Git: git-status](https://git-scm.com/docs/git-status)
- [Git: git-diff](https://git-scm.com/docs/git-diff)
- [Git: git-reflog](https://git-scm.com/docs/git-reflog)
- [Git: git-reset](https://git-scm.com/docs/git-reset)
- [Git: git-revert](https://git-scm.com/docs/git-revert)
