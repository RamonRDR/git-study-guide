# Inspecionar, preparar e registrar

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../01-init-config-help/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../03-diff-log-show/README.pt-BR.md)
<!-- /navigation -->

**Nível:** iniciante · **Tempo estimado:** 30 min

**Pré-requisitos:** [Inicializar, configurar e consultar ajuda](../01-init-config-help/README.pt-BR.md)

**Objetivo:** Registrar mudança focada e verificar outro arquivo não rastreado.

## O que é e por quê

git status consulta estado preparado/não preparado/não rastreado; --short mostra códigos compactos. git add PATH prepara conteúdo atual do arquivo. git add -p seleciona interativamente hunks (grupos de linhas alteradas) de rastreados; git add . pode preparar muitos caminhos e git add -A abrange adições, mudanças e exclusões em toda working tree sem caminho. Prefira caminhos explícitos. git commit -m registra index com mensagem; git commit -a prepara também mudanças/exclusões de rastreados, não novos não rastreados, podendo incluir edições indesejadas. Evite até entender seleção.

## Prática

Use repo isolado novo do capítulo 01. Em editor crie note.txt com practice e draft.txt com draft, cada qual com quebra final. Confira e prepare só note.txt:

```text
git rev-parse --show-toplevel
git status --short
git add -- note.txt
git status --short
git diff --cached -- note.txt
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Esperado: A seguido de espaço para note.txt, ?? draft.txt. Se raiz, diff preparado ou identidade incorretos, pare. Caso contrário:

```text
git commit -m "docs: add note"
git status --short
git show HEAD:note.txt
git ls-files
```

Esperado: só draft.txt não rastreado; note.txt rastreado e gravado como practice. -- encerra parsing de opções para não confundir caminho com opção. Nenhuma operação remota.

## Erros comuns e segurança

Se mudanças indesejadas preparadas, não faça commit; neste exercício recrie lab. Nunca force inclusão de segredos nem faça commit de rascunhos privados. Confira ambas identidades antes de cada commit; shell isolado, não controles do editor.

## Exercício e autocorreção

Preveja se draft.txt entra no commit. Resposta: não, não preparado. Passe se ls-files listar só note.txt. Uso profissional: selecionar arquivos para mudança revisável.

## Referência rápida

- `git status`
- `git add`
- `git commit`

## Fontes oficiais

- [Git: git-status](https://git-scm.com/docs/git-status)
- [Git: git-add](https://git-scm.com/docs/git-add)
- [Git: git-commit](https://git-scm.com/docs/git-commit)

---

<!-- navigation-footer -->
[Anterior](../01-init-config-help/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../03-diff-log-show/README.pt-BR.md)
<!-- /navigation-footer -->
