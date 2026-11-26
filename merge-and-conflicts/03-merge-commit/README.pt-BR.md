# Divergência e commits de merge

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../02-fast-forward/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../04-conflict-resolution/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 35 min

**Pré-requisitos:** [Merge fast-forward](../02-fast-forward/README.pt-BR.md)

**Objetivo:** Distinguir merge de dois pais de fast-forward e verificar ambos pais.

## O que é e por quê

Quando ambas branches têm commits exclusivos, nenhuma ponta é ancestral da outra. Merge normal de duas pontas combina mudanças usando base comum. Commit de merge bem-sucedido registra snapshot combinado com dois pais (primeiro: destino anterior; segundo: origem). `--no-ff` solicita commit de merge mesmo se fast-forward possível, exceto se já atualizado. `--no-edit` aceita mensagem gerada. Merge preserva ancestralidade das duas linhas.

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

No editor de texto, crie ou edite overview.txt com exatamente uma linha: overview, com quebra final. Salve, depois prepare no shell dedicado:

```text
git add -- overview.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Se diff e ambas identidades corretos, faça commit:

```text
git commit -m "docs: add overview"
```

```text
git rev-parse --show-toplevel
git branch --show-current
git status --short
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Confirme main limpa, identidades fictícias e gráfico divergente pretendido. Primeiro tente operação protegida (deve falhar sem mudar histórico):

```text
git log --all --graph --oneline --decorate
git rev-parse main feat/note
git merge --ff-only feat/note
```

Após recusa, confira pontas e status inalterados. Então integre:

```text
git status --short
git rev-parse main feat/note
git merge --no-ff --no-edit feat/note
git log --all --graph --oneline --decorate
git rev-list --parents -1 HEAD
git show HEAD:note.txt
git show HEAD:overview.txt
git status --short
```

Esperado: novo M com dois pais, note feature e overview overview; status limpo. Antes: C2 -> C1 <- C3 (C2 origem, C3 destino; setas apontam pais). Depois: main -> M, M -> C3 e C2, ambos -> C1; feat/note ainda -> C2. rev-list mostra três IDs: M, C3, C2.

## Erros comuns e segurança

Se conflito inesperado, use status e abort de merge comum do capítulo 01; não prepare conteúdo aleatório. Inspecione branches antes; merge bem-sucedido sozinho não prova correção.

Após cada lab independente, feche editor e shell dedicado, então exclua somente pasta pai temporária exata anotada no módulo 00 pelo gerenciador se não precisar mais. Nunca exclua guia, pasta pessoal ou repo de trabalho.

## Exercício e autocorreção

Por que --ff-only recusou? Pontas têm commits exclusivos. Passe se merge tiver dois pais e ambos conteúdos. Uso profissional: preservar histórico de integração quando política permite commits de merge.

## Referência rápida

- `git merge --no-ff --no-edit SOURCE`
- `git rev-list --parents -1 HEAD`

## Fontes oficiais

- [Git: git-merge](https://git-scm.com/docs/git-merge)
- [Git: git-rev-list](https://git-scm.com/docs/git-rev-list)
- [Git: git-log](https://git-scm.com/docs/git-log)

---

<!-- navigation-footer -->
[Anterior](../02-fast-forward/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../04-conflict-resolution/README.pt-BR.md)
<!-- /navigation-footer -->
