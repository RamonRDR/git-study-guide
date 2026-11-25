# Estados dos arquivos e limites do remote

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../02-snapshots-head-and-refs/README.pt-BR.md) · [Índice](../README.pt-BR.md) · —
<!-- /navigation -->

**Nível:** iniciante · **Tempo estimado:** 25 min

**Pré-requisitos:** [Snapshots, HEAD e referências](../02-snapshots-head-and-refs/README.pt-BR.md)

**Objetivo:** Interpretar arquivos rastreados, não rastreados, modificados, preparados e ignorados.

## O que é e por quê

Rastreado significa caminho representado no index; não rastreado não está. Modificado significa conteúdo diferente de uma base de comparação; preparado significa index difere de HEAD. Não são exclusivos: MM indica duas diferenças. Arquivo não rastreado ignorado corresponde a regra e normalmente não aparece no status/add; ignorar não deixa de rastrear arquivo já rastreado. Status limpo significa ausência de diferenças reportadas ou não rastreados não ignorados, não backup nem sincronização remota.

## Prática

Continue lab com third ainda editado. Crie draft.txt novo no editor com draft. Inspecione (somente leitura):

```text
git status --short
git ls-files
git remote -v
```

Esperado: espaço-M note.txt e ?? draft.txt; ls-files lista note.txt; remotes vazio porque nenhum foi configurado. Status curto tem duas posições XY: X compara index a HEAD, Y working tree a index (entradas comuns sem conflito). ?? não rastreado, !! ignorado quando solicitado. A adicionado, M modificado, D excluído, R renome detectado. Conflitos depois.

## Erros comuns e segurança

Não deduza estado remoto por status local. Não precisa fetch, push nem credenciais. Não adicione tudo cegamente; confira antes. Se caminhos inesperados, pare e confira raiz descartável. Mantenha lab para módulo 03 ou recrie pelo 00.

## Exercício e autocorreção

Classifique note.txt e draft.txt. Resposta: note rastreado e modificado não preparado; draft não rastreado. Passe se explicar por que remote vazio não impede commits. Uso profissional: conferir alterações antes de revisão.

## Referência rápida

- `git status`
- `git ls-files`
- `git remote`
- `gitignore`

## Fontes oficiais

- [Git: git-status](https://git-scm.com/docs/git-status)
- [Git: git-ls-files](https://git-scm.com/docs/git-ls-files)
- [Git: git-remote](https://git-scm.com/docs/git-remote)
- [Git: gitignore](https://git-scm.com/docs/gitignore)
