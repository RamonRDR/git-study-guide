# Restore: arquivos de trabalho e index

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../01-recovery-safety/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../03-reset/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 25 min

**Pré-requisitos:** [Laboratório isolado](../../getting-started/03-first-repository/README.pt-BR.md) · [Primeiro commit](../../getting-started/05-first-commit/README.pt-BR.md) · [Merge e conflitos](../../merge-and-conflicts/README.pt-BR.md) · [Remotos](../../remote-repositories/README.pt-BR.md) · [Inspecione antes de desfazer](../01-recovery-safety/README.pt-BR.md)

**Objetivo:** Distinguir retirar do stage de descartar edição.

## O que é e por quê

Com caminho, `git restore -- PATH` copia do index para a árvore de trabalho por padrão. `git restore --staged -- PATH` usa HEAD como fonte padrão e altera só o index. `--source=COMMIT` escolhe outra árvore; `--staged --worktree` muda ambos destinos. Não há novo commit nem movimento de branch. Arquivo rastreado ausente na fonte pode ser removido. Use restore específico após inspecionar diferenças; evite restauração ampla com trabalho valioso.

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

Edite note.txt em editor de texto simples para exatamente uma linha `staged draft` com quebra final. Salve e volte à sessão dedicada.

```text
git add -- note.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Edite note.txt em editor de texto simples para exatamente uma linha `working draft` com quebra final. Salve e volte à sessão dedicada.

```text
git status --short
git diff
git diff --cached
git show :note.txt
git show HEAD:note.txt
```

Espere staged draft no index, working draft em disco e practice em HEAD. O próximo comando descarta intencionalmente APENAS a edição de trabalho. Pare se drafts não forem descartáveis ou raiz não estiver verificada.

```text
git restore -- note.txt
git status --short
git diff
git diff --cached
git restore --staged -- note.txt
git status --short
git diff
git diff --cached
```

Após primeiro restore, disco = staged draft; após retirar stage, index = practice e disco continua staged draft. Confirme ausência de trabalho útil antes da etapa destrutiva final.

```text
git restore -- note.txt
git status --short
git rev-list --count HEAD
git show HEAD:note.txt
```

Esperado status limpo, um commit, conteúdo practice. Uso profissional: retire alterações selecionadas por engano sem perder edição.

Após o exercício, feche editores e sessão dedicada. Exclua somente o pai temporário exato registrado pelo gerenciador de arquivos se não precisar mais; nunca guia, home ou repo de trabalho.

## Erros comuns e segurança

Restore pode descartar edições unstaged permanentemente. Reflog não registra edições da árvore. Se restaurou trabalho útil, pare e confira backups independentes ou histórico do editor; recuperação não garantida.

## Exercício e autocorreção

Qual comando retira arquivo do stage mas mantém edição? Resposta: restore --staged -- note.txt. Passe se diff staged vazio e diff normal ainda mostrar edição.

## Referência rápida

- `git restore -- PATH`
- `git restore --staged -- PATH`
- `git restore --source=COMMIT -- PATH`

## Fontes oficiais

- [Git: git-restore](https://git-scm.com/docs/git-restore)
- [Git: git-diff](https://git-scm.com/docs/git-diff)

---

<!-- navigation-footer -->
[Anterior](../01-recovery-safety/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../03-reset/README.pt-BR.md)
<!-- /navigation-footer -->
