# Comparar e inspecionar histórico

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../02-status-add-commit/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../04-move-and-remove/README.pt-BR.md)
<!-- /navigation -->

**Nível:** iniciante · **Tempo estimado:** 35 min

**Pré-requisitos:** [Inspecionar, preparar e registrar](../02-status-add-commit/README.pt-BR.md)

**Objetivo:** Escolher base correta de diff e consultar histórico registrado.

## O que é e por quê

git diff compara working tree ao index para rastreados; --cached (também --staged) compara index a HEAD (ou árvore vazia antes do primeiro commit); git diff HEAD compara conteúdo rastreado de trabalho a HEAD. Não rastreados não aparecem no diff comum. Diff usa - para linhas removidas e + adicionadas; contexto mostra posição. git log lista commits com --oneline compacto e -n para limitar; git show exibe objeto como commit com patch ou caminho em commit.

## Prática

Continue capítulo 02. Edite note.txt para second e salve com quebra final, depois prepare:

```text
git add -- note.txt
```

Agora edite note.txt para third e salve sem preparar. Confira:

```text
git diff -- note.txt
git diff --cached -- note.txt
git diff HEAD -- note.txt
git log -1 --oneline
git show --stat HEAD
git show HEAD:note.txt
git show :note.txt
```

Esperado: diff simples second -> third, cached practice -> second, HEAD practice -> third. Log e show somente leitura; HEAD practice, index second. Se pager abrir, q sai. Agora prepare third, confira diff cached e identidades efetivas; se correto faça commit:

```text
git add -- note.txt
git diff --cached -- note.txt
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Pare se saída inesperada ou identidades não fictícias. Depois:

```text
git commit -m "docs: update note"
git log -2 --oneline
git diff HEAD~1 HEAD -- note.txt
git show HEAD:note.txt
```

HEAD~1 significa primeiro pai de HEAD (aqui um commit atrás); comparação mostra practice -> third. Conteúdo third; draft.txt segue não rastreado.

## Erros comuns e segurança

Diff simples vazio não prova ausência de staging ou não rastreados. Confira status e diff cached também. Se histórico menor que esperado, não invente IDs; confira log.

## Exercício e autocorreção

Qual diff mostra mudanças do próximo commit? Resposta: --cached. Qual mostra mudanças rastreadas contra último commit? git diff HEAD. Passe se identificar três bases. Uso profissional: revisar exatamente o que entrará no commit.

## Referência rápida

- `git diff`
- `git log`
- `git show`
- `gitrevisions`

## Fontes oficiais

- [Git: git-diff](https://git-scm.com/docs/git-diff)
- [Git: git-log](https://git-scm.com/docs/git-log)
- [Git: git-show](https://git-scm.com/docs/git-show)
- [Git: gitrevisions](https://git-scm.com/docs/gitrevisions)

---

<!-- navigation-footer -->
[Anterior](../02-status-add-commit/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../04-move-and-remove/README.pt-BR.md)
<!-- /navigation-footer -->
