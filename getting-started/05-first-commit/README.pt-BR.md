# Primeiro commit

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../04-editor-and-gui/README.pt-BR.md) · [Índice](../README.pt-BR.md) · —
<!-- /navigation -->

**Nível:** iniciante · **Tempo estimado:** 35 min

**Pré-requisitos:** [VS Code e interfaces gráficas](../04-editor-and-gui/README.pt-BR.md)

**Objetivo:** Preparar e registrar arquivo de texto; conferir histórico local.

## O que é e por quê

Commit registra snapshot do conteúdo preparado com informação histórica. Working tree contém arquivos editáveis; staging area (index) guarda conteúdo selecionado para próximo commit; repo local guarda histórico. Editar depois de stage não muda index automaticamente. Commit não é upload.

## Prática

Use mesmo lab descartável, confira raiz e status, e crie note.txt novo com linha practice e quebra final. Comandos sobrescrevem arquivos; não rode se note.txt já existir.

```powershell
Set-Content -Path note.txt -Value "practice" -Encoding ascii
```

```bash
printf 'practice\n' > note.txt
```

Rode separadamente; confira cada resultado:

```text
git status
git add note.txt
git status
git diff --cached
git commit -m "docs: add note"
git status
git log -1 --oneline
git show HEAD:note.txt
```

Antes de add: arquivo não rastreado; depois: novo arquivo preparado; diff cached: linha practice; após commit: status limpo, um commit com mensagem, practice armazenado. HEAD identifica checkout atual, normalmente branch atual. Hashes, datas, saídas localizadas e avisos de quebra variam. Fluxo: arquivo de trabalho -> add -> index -> commit -> histórico local.

## Erros comuns e segurança

Se faltar autoria, confira configuração local. Se nada preparado, consulte status e selecione só arquivo desejado. Evite `git add .` em projetos desconhecidos. Se preparou conteúdo errado, pare e crie lab novo em vez de comandos destrutivos. Não contorne políticas de assinatura ou hooks. Mantenha lab para módulo 01; depois feche editor, saia com `cd $HOME` (PowerShell) ou `cd "$HOME"` (Bash/Zsh), exclua apenas pasta temporária exata pelo gerenciador se não precisar.

## Exercício e autocorreção

Preveja status após escrever, add e commit. Dica: siga três locais. Passe quando log mostrar mensagem, show retornar practice e status limpo. Explique por que edição após add exige novo add para inclusão. Hábito profissional: revisar diff preparado antes de registrar.

## Referência rápida

- `git status`
- `git add note.txt`
- `git diff --cached`
- `git commit -m "docs: add note"`
- `git log -1 --oneline`
- `git show HEAD:note.txt`

## Fontes oficiais

- [https://git-scm.com/docs/gittutorial](https://git-scm.com/docs/gittutorial)
- [https://git-scm.com/docs/git-add](https://git-scm.com/docs/git-add)
- [https://git-scm.com/docs/git-commit](https://git-scm.com/docs/git-commit)
- [https://git-scm.com/docs/git-status](https://git-scm.com/docs/git-status)
