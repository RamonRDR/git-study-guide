# Stash: trabalho temporário

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../05-reflog/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../07-cherry-pick/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 35 min

**Pré-requisitos:** [Laboratório isolado](../../getting-started/03-first-repository/README.pt-BR.md) · [Primeiro commit](../../getting-started/05-first-commit/README.pt-BR.md) · [Merge e conflitos](../../merge-and-conflicts/README.pt-BR.md) · [Remotos](../../remote-repositories/README.pt-BR.md) · [Reflog e recuperação de commits perdidos](../05-reflog/README.pt-BR.md)

**Objetivo:** Guardar temporariamente trabalho staged, unstaged e untracked e restaurá-lo conscientemente.

## O que é e por quê

Stash salva trabalho local selecionado como objetos Git referenciados por refs/stash e normalmente retorna árvore/index afetados ao HEAD. Push padrão guarda alterações rastreadas staged/unstaged, não untracked ou ignoradas. `-u` inclui untracked; `-a` inclui ignorados e pode capturar segredos, evite sem inspeção. `apply` mantém stash, `pop` remove se aplicação bem-sucedida; `--index` tenta restaurar estado staged. `drop` remove entrada. Stash é local, não backup externo durável; aplicar em histórico alterado pode conflitar.

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

Edite note.txt em editor de texto simples para exatamente uma linha `staged note` com quebra final. Salve e volte à sessão dedicada.

```text
git add -- note.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Edite note.txt em editor de texto simples para exatamente uma linha `working note` com quebra final. Salve e volte à sessão dedicada.

Crie draft.txt untracked contendo apenas `temporary` com quebra final. Verifique apenas essas mudanças fictícias e lista stash vazia; registre HEAD.

```text
git status --short
git stash list
git rev-parse HEAD
git stash push -u -m "lab: temporary notes"
git status --short
git stash list
git stash show --stat --include-untracked 'stash@{0}'
git rev-parse HEAD
```

Esperado status limpo, um stash, HEAD igual. Confirme entrada exata e estado limpo antes de aplicar.

```text
git stash apply --index 'stash@{0}'
git status --short
git diff
git diff --cached
git show :note.txt
git stash list
```

Esperado staged note no index, working note em disco, draft.txt untracked, stash ainda listado. Leia draft.txt no editor e confira temporary. Só após confirmar todos dados esperados e que único stash é dispensável, descarte; não descarte trabalho valioso.

```text
git stash drop 'stash@{0}'
git stash list
git status --short
git rev-parse HEAD
```

Esperado lista vazia, edições restauradas iguais, HEAD original. Uso profissional: trocar tarefa brevemente sem commit incompleto; use branch privada adequada e backup para trabalho duradouro.

Após o exercício, feche editores e sessão dedicada. Exclua somente o pai temporário exato registrado pelo gerenciador de arquivos se não precisar mais; nunca guia, home ou repo de trabalho.

## Erros comuns e segurança

Se apply/pop conflitar, inspecione status; stash normalmente fica retido após pop conflitante. Não há stash --abort geral. Resolva com cuidado ou busque ajuda; não use hard reset em projeto real para limpar conflito. Entradas descartadas podem ficar inalcançáveis; recuperação não garantida.

## Exercício e autocorreção

Por que preferir apply antes de drop em recuperação incerta? Resposta: inspecione mantendo estado salvo. Passe se versões staged/unstaged e arquivo untracked voltam e HEAD não muda.

## Referência rápida

- `git stash push -u -m MESSAGE`
- `git stash list`
- `git stash apply --index 'stash@{0}'`
- `git stash pop`
- `git stash drop 'stash@{0}'`

## Fontes oficiais

- [Git: git-stash](https://git-scm.com/docs/git-stash)
- [Git: git-status](https://git-scm.com/docs/git-status)

---

<!-- navigation-footer -->
[Anterior](../05-reflog/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../07-cherry-pick/README.pt-BR.md)
<!-- /navigation-footer -->
