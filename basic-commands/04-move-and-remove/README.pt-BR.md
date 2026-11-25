# Renomear e remover arquivos rastreados

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../03-diff-log-show/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../05-ignore-and-review/README.pt-BR.md)
<!-- /navigation -->

**Nível:** iniciante · **Tempo estimado:** 30 min

**Pré-requisitos:** [Comparar e inspecionar histórico](../03-diff-log-show/README.pt-BR.md)

**Objetivo:** Distinguir exclusão de arquivo de trabalho, exclusão preparada e remoção apenas do index.

## O que é e por quê

git mv OLD NEW move caminho rastreado e prepara exclusão antiga/adição nova; detecção de renome depende de similaridade, não metadado permanente. git rm PATH remove rastreado de working tree e index (prepara exclusão). git rm --cached PATH remove só index mantendo arquivo; se rastreado em HEAD prepara exclusão. Git pode recusar por risco de perda; nunca use -f aqui. Movimentar/excluir no gerenciador muda working tree; Git registra efeitos preparados após add/rm.

## Prática

Continue lab descartável capítulo 03: note.txt commitado com third; draft.txt não rastreado. Confira raiz/status, garanta que destino notes.txt não existe. Renomeie só note.txt:

```text
git rev-parse --show-toplevel
git status --short
git mv -- note.txt notes.txt
git diff --cached --name-status
git status --short
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Esperado renome preparado (ou exclusão/adição equivalente). Se correto e identidades fictícias, registre renome e remova só entrada do index:

```text
git commit -m "docs: rename note"
git rm --cached -- notes.txt
git status --short
git diff --cached --name-status
```

Esperado: D preparado de notes.txt e notes.txt não rastreado continua no disco. Não registre remoção; adicione de volta para cancelar exclusão preparada sem alterar conteúdo. Depois remova rastreado (só conteúdo descartável):

```text
git add -- notes.txt
git diff --cached --name-status
git rm -- notes.txt
git diff --cached --name-status
git status --short
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Esperado: primeiro diff vazio, segundo D notes.txt e arquivo ausente; draft permanece. Se esperado e identidades fictícias, registre:

```text
git commit -m "docs: remove note"
git status --short
```

## Erros comuns e segurança

Nunca rode rm em repo real sem entender exclusão/backup. Sem -f, remoção recursiva ou curingas. Conteúdo commitado anterior permanece no histórico, mas edições não registradas podem não ser recuperáveis. Se comando recusar, confira status; pare em vez de forçar. Recuperação depois.

## Exercício e autocorreção

Compare rm e rm --cached. Resposta: ambos removem entrada index; só rm comum remove arquivo. Passe se verificar cada caso e explicar histórico anterior. Uso profissional: parar de rastrear dado gerado sem apagar cópia local (junto a regra ignore).

## Referência rápida

- `git mv`
- `git rm`
- `git add`
- `git diff`

## Fontes oficiais

- [Git: git-mv](https://git-scm.com/docs/git-mv)
- [Git: git-rm](https://git-scm.com/docs/git-rm)
- [Git: git-add](https://git-scm.com/docs/git-add)
- [Git: git-diff](https://git-scm.com/docs/git-diff)
