# Reflog e recuperação de commits perdidos

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../04-revert/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../06-stash/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 30 min

**Pré-requisitos:** [Laboratório isolado](../../getting-started/03-first-repository/README.pt-BR.md) · [Primeiro commit](../../getting-started/05-first-commit/README.pt-BR.md) · [Merge e conflitos](../../merge-and-conflicts/README.pt-BR.md) · [Remotos](../../remote-repositories/README.pt-BR.md) · [Revert sem reescrever histórico](../04-revert/README.pt-BR.md)

**Objetivo:** Encontrar commit deslocado no reflog local e recuperá-lo com nova branch.

## O que é e por quê

Reflog registra atualizações de refs locais, incluindo movimentos HEAD. Diferente de git log, que percorre ancestralidade, reflog pode mostrar tips não mais alcançáveis da branch atual. `HEAD@{1}` refere-se a valor anterior de HEAD, não necessariamente pai; use aspas no shell. Entradas locais podem expirar e objetos inalcançáveis podem ser coletados depois. Diagrama: main C1; antes main C2 -> C1; reflog registra C2 mesmo sem main apontar para ele. Criar branch de resgate no commit verificado torna-o alcançável novamente.

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

Edite note.txt em editor de texto simples para exatamente uma linha `rescue me` com quebra final. Salve e volte à sessão dedicada.

```text
git add -- note.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Somente se o diff staged e ambas identidades estiverem corretos, continue:

```text
git commit -m "docs: add rescue note"
git rev-parse HEAD HEAD^
git status --short
git reflog -n 3
```

Registre C2 em privado. Confirme raiz, main limpa, sem remoto, exatamente dois commits e dados descartáveis. O próximo comando intencionalmente move main de C2 e redefine index/arquivos; não use em trabalho real.

```text
git reset --hard HEAD^
git log --oneline
git reflog -n 4
git show 'HEAD@{1}':note.txt
git rev-parse 'HEAD@{1}'
```

Esperado log só C1, reflog inclui C2, show retorna rescue me. Seletor só vale se ainda resolver ao C2 registrado; senão inspecione reflog e escolha ID completo correto sem adivinhar. Após verificar crie branch de resgate:

```text
git branch rescue/note 'HEAD@{1}'
git show rescue/note:note.txt
git log --all --oneline --graph
git merge --ff-only rescue/note
git rev-parse HEAD rescue/note
git status --short
```

Esperado ambas refs em C2, ID original recuperado, status limpo. Uso profissional: preserve ref candidata antes de novas mudanças; inspecione conteúdo e integre só após revisão.

Após o exercício, feche editores e sessão dedicada. Exclua somente o pai temporário exato registrado pelo gerenciador de arquivos se não precisar mais; nunca guia, home ou repo de trabalho.

## Erros comuns e segurança

Reflog não é backup remoto e não garante recuperação. Não execute reflog expire, gc ou limpeza destrutiva em incidente; preserve cópias independentes. Conteúdo nunca commitado/registrado pode estar indisponível.

## Exercício e autocorreção

Por que log não vê C2 após reset mas reflog pode achar? Resposta: ancestralidade versus movimento de ref. Passe se ID resgatado igual ao C2 original, não só conteúdo.

## Referência rápida

- `git reflog`
- `git show COMMIT`
- `git branch rescue/note COMMIT`

## Fontes oficiais

- [Git: git-reflog](https://git-scm.com/docs/git-reflog)
- [Git: git-reset](https://git-scm.com/docs/git-reset)
- [Git: git-branch](https://git-scm.com/docs/git-branch)
- [Git: git-gc](https://git-scm.com/docs/git-gc)

---

<!-- navigation-footer -->
[Anterior](../04-revert/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../06-stash/README.pt-BR.md)
<!-- /navigation-footer -->
