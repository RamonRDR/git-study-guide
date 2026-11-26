# Revert sem reescrever histórico

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../03-reset/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../05-reflog/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 30 min

**Pré-requisitos:** [Laboratório isolado](../../getting-started/03-first-repository/README.pt-BR.md) · [Primeiro commit](../../getting-started/05-first-commit/README.pt-BR.md) · [Merge e conflitos](../../merge-and-conflicts/README.pt-BR.md) · [Remotos](../../remote-repositories/README.pt-BR.md) · [Reset e seus três modos](../03-reset/README.pt-BR.md)

**Objetivo:** Desfazer alteração commitada adicionando histórico em vez de reescrevê-lo.

## O que é e por quê

Revert calcula o inverso de commit em relação ao pai e aplica ao estado atual, normalmente criando novo commit. Útil para corrigir histórico compartilhado pelo processo de revisão da equipe. Pode conflitar se edições posteriores se sobrepõem. `--no-edit` usa mensagem gerada; `--no-commit` prepara resultado sem commit imediato. Commit de merge exige pai mainline escolhido conscientemente (`-m`); reverter merge afeta merges futuros, então a aula não executa essa variante.

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

Edite note.txt em editor de texto simples para exatamente uma linha `wrong` com quebra final. Salve e volte à sessão dedicada.

```text
git add -- note.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Somente se o diff staged e ambas identidades estiverem corretos, continue:

```text
git commit -m "docs: add wrong note"
git log --oneline
git show HEAD
git status --short
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Confirme main limpa, identidades fictícias e HEAD como única mudança errada a reverter. Execute:

```text
git revert --no-edit HEAD
git log --oneline
git rev-list --count HEAD
git show HEAD:note.txt
git diff HEAD~2 HEAD
git status --short
```

Esperado C1 -> C2 -> R3, três commits; C2 continua ancestral, snapshot R3 igual a C1, status limpo. Commit inverso não remove o original. Em projeto real revise/teste patch inverso antes de publicar.

Após o exercício, feche editores e sessão dedicada. Exclua somente o pai temporário exato registrado pelo gerenciador de arquivos se não precisar mais; nunca guia, home ou repo de trabalho.

## Erros comuns e segurança

Se houver conflito, inspecione status e mudanças staged; resolva e use revert --continue, ou revert --abort durante operação. Revert não remove segredos expostos do histórico; revogue credenciais separadamente. Evite reverter commits sem avaliar dependências.

## Exercício e autocorreção

Reverter C2 exclui seu ID? Resposta: não. Passe se histórico tem três commits e conteúdo HEAD igual ao original.

## Referência rápida

- `git revert --no-edit COMMIT`
- `git revert --no-commit COMMIT`
- `git revert --abort`
- `git revert --continue`

## Fontes oficiais

- [Git: git-revert](https://git-scm.com/docs/git-revert)
- [Git: git-log](https://git-scm.com/docs/git-log)
