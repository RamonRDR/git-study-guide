# Rebase, abort e continue

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../05-squash-merge/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../07-interactive-rebase/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 45 min

**Pré-requisitos:** [Integração por squash](../05-squash-merge/README.pt-BR.md)

**Objetivo:** Reaplicar commit local em nova base, inspecionar conflitos e preservar histórico original com ref backup.

## O que é e por quê

Rebase seleciona commits de branch e reaplica em nova base; ao recriar, IDs mudam por pais/metadados. Normalmente move branch rebased, não destino. Pode parar por commit. Em conflito de rebase comum, ours é lado já reaplicado (nova base mais trabalho reaplicado) e theirs é commit em reaplicação, não modelo usual sua feature versus main recebida. `--abort` restaura branch original; `--continue` retoma após preparar resoluções. `--skip` omite patch atual e pode perder mudanças pretendidas; não use no lab.

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
```

No editor de texto, crie ou edite note.txt com exatamente uma linha: main, com quebra final. Salve, depois prepare no shell dedicado:

```text
git add -- note.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Se diff e ambas identidades corretos, faça commit:

```text
git commit -m "docs: revise main note"
```

```text
git switch feat/note
git branch backup/feature
```

```text
git rev-parse --show-toplevel
git branch --show-current
git status --short
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Confira feat/note limpa, identidades fictícias e backup na ponta atual. Anote pontas antes do rebase. Provoque conflito esperado:

```text
git rev-parse main feat/note backup/feature
git rebase main
```

Espere conflito em note.txt. Confira estágios/status; HEAD pode estar detached durante reaplicação:

```text
git status
git ls-files -u
git show :1:note.txt
git show :2:note.txt
git show :3:note.txt
git rebase --abort
git branch --show-current
git rev-parse feat/note backup/feature
git status --short
```

Esperado base practice, estágio 2 main, 3 feature. Após abort ponta original igual backup, feat/note ativa e status limpo. Repita rebase:

```text
git rebase main
```

Confirme conflito novamente. Substitua note.txt fictício por duas linhas main e feature, quebra final, remova marcadores. Prepare e confira:

```text
git add -- note.txt
git ls-files -u
git diff --cached
git diff --cached --check
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Se tudo resolvido, identidades fictícias e diff correto, rode git rebase --continue. Pode abrir editor de mensagem. Salve mensagem existente e feche editor. Se CLI opcional VS Code instalada, use segundo comando em vez do primeiro (não ambos); --wait aguarda fechamento do arquivo. Sem editor utilizável, aborte lab em andamento em vez de contornar revisão. Só após sucesso rode inspeção:

```text
git rebase --continue
```

```text
git -c core.editor="code --wait" rebase --continue
```

```text
git branch --show-current
git rev-parse main HEAD~1
git rev-parse feat/note backup/feature
git log --all --graph --oneline --decorate
git show HEAD:note.txt
git status --short
```

Esperado feat/note ativa, main igual HEAD~1, feature rebased difere backup, arquivo combinado, status limpo. Diagrama: main -> C3 -> C1; backup/feature -> C2 -> C1; feat/note -> C2' -> C3. Backup intacto. Em rebase sem conflito, reaplicação conclui sem pausa quando edições compatíveis; confira pai e conteúdo em ambos casos.

## Erros comuns e segurança

Nunca reescreva branch publicada/compartilhada aqui. Não force push, skip nem suponha ours = sua feature. Abort só rebase em andamento. Ref backup não é backup externo; mantenha até verificar.

Após cada lab independente, feche editor e shell dedicado, então exclua somente pasta pai temporária exata anotada no módulo 00 pelo gerenciador se não precisar mais. Nunca exclua guia, pasta pessoal ou repo de trabalho.

## Exercício e autocorreção

Por que commit recriado tem novo ID? Novo pai e metadados/conteúdo. Passe se abort restaurar original, continue criar ponta feature sobre main e backup preservar antiga. Uso profissional: atualizar trabalho não publicado com mudanças da base sob política da equipe.

## Referência rápida

- `git rebase main`
- `git rebase --abort`
- `git rebase --continue`

## Fontes oficiais

- [Git: git-rebase](https://git-scm.com/docs/git-rebase)
- [Git: git-branch](https://git-scm.com/docs/git-branch)
- [Git: git-ls-files](https://git-scm.com/docs/git-ls-files)
- [Git: git-config](https://git-scm.com/docs/git-config)
