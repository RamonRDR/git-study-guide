# Rebase interativo e escolha de estratégia

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../06-rebase-and-conflicts/README.pt-BR.md) · [Índice](../README.pt-BR.md) · —
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 40 min

**Pré-requisitos:** [Rebase, abort e continue](../06-rebase-and-conflicts/README.pt-BR.md)

**Objetivo:** Combinar dois commits locais com fixup e comparar estratégias de integração.

## O que é e por quê

Rebase interativo abre lista todo de commits (mais antigo primeiro). `pick` mantém mudança; `reword` muda mensagem; `edit` pausa; `squash` combina com anterior e permite editar mensagem; `fixup` combina e normalmente descarta segunda mensagem; `drop` omite commit. Reordenar pode causar conflitos. Ferramentas reescrevem histórico, não edições comuns. Praticamos só fixup de dois commits locais com branch backup. Editor todo é controlado por sequence.editor ou GIT_SEQUENCE_EDITOR, distinto do editor de mensagem.

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
git branch backup/feature
git log -3 --oneline
git rev-list --count main..HEAD
```

```text
git rev-parse --show-toplevel
git branch --show-current
git status --short
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Confirme dois commits após main, feat/note limpa, backup na ponta e identidades fictícias. Use um comando, não ambos. Primeiro usa editor configurado; CLI opcional VS Code (se `code --version` funciona) é segunda opção. Se editor desconhecido, aprenda salvar/sair antes ou adie prática manual opcional. Não ajuste editor global para lab.

```text
git rebase -i HEAD~2
```

```text
git -c sequence.editor="code --wait" rebase -i HEAD~2
```

No editor todo, mantenha primeira linha pick; mude só palavra pick da segunda linha para fixup. Preserve IDs reais; placeholders abaixo ilustram formato, não cole:

```text
pick FIRST_ID docs: revise feature note
fixup SECOND_ID docs: add detail
```

Salve e feche arquivo todo. Se lista diferente, cancele sem salvar edições; lista inalterada pode fazer rebase sem mudança. Se rebase parar por conflito, aborte ou resolva pelo capítulo 06. Após sucesso:

```text
git rev-list --count main..HEAD
git rev-list --count main..backup/feature
git log -1 --format=%s
git diff HEAD backup/feature
git show HEAD:note.txt
git show HEAD:detail.txt
git status --short
```

Esperado um novo commit versus dois no backup, primeira mensagem mantida, diff de pontas vazio (mesmo snapshot), conteúdos feature e detail, status limpo. Comparação: ff-only = IDs existentes, sem commit merge novo; merge commit = dois pais e ambos históricos; squash = um novo commit destino, sem ancestralidade origem; rebase = commits locais recriados sobre nova base; rebase interativo = editar sequência local antes de integrar. Escolha por ancestralidade, histórico de review e política.

## Erros comuns e segurança

Não use drop, reordenação ou reword em histórico compartilhado. Evite editar IDs ou pular mudanças cegamente. Se resultado concluído errado, mantenha ref backup e pare; recuperação concluída no módulo 07. Interação manual com editor não coberta pelo CI; testes determinísticos usam editor todo controlado.

Após cada lab independente, feche editor e shell dedicado, então exclua somente pasta pai temporária exata anotada no módulo 00 pelo gerenciador se não precisar mais. Nunca exclua guia, pasta pessoal ou repo de trabalho.

## Exercício e autocorreção

Quando escolher squash em vez de rebase interativo? Resposta: squash integra mudanças combinadas em um commit destino; rebase interativo muda sequência local origem. Passe se snapshot final igual backup e contagem diferente. Uso profissional: preparar histórico local de review sem reescrever commits compartilhados.

## Referência rápida

- `git rebase -i HEAD~2`
- `pick`
- `fixup`
- `git diff HEAD backup/feature`

## Fontes oficiais

- [Git: git-rebase](https://git-scm.com/docs/git-rebase)
- [Git: git-config](https://git-scm.com/docs/git-config)
- [Git: git-merge](https://git-scm.com/docs/git-merge)
- [Git: git-diff](https://git-scm.com/docs/git-diff)
