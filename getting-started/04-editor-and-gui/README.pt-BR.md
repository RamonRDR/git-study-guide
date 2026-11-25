# VS Code e interfaces gráficas

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../03-first-repository/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../05-first-commit/README.pt-BR.md)
<!-- /navigation -->

**Nível:** iniciante · **Tempo estimado:** 20 min

**Pré-requisitos:** [Primeiro repositório e configuração](../03-first-repository/README.pt-BR.md)

**Objetivo:** Abrir lab em editor e comparar GUI e terminal.

## O que é e por quê

Editor altera arquivos; Git registra conteúdo selecionado. VS Code tem suporte Git integrado mas usa instalação Git separada para operações locais. Source Control mostra mudanças e permite stage (selecionar conteúdo para commit) e commit (registrar conteúdo escolhido). Git GUI é outro cliente opcional se instalado. Nenhum exige conta de hospedagem para trabalho local.

## Prática

Instale VS Code pela página oficial se desejar; editor de texto simples serve. Use File > Open Folder para abrir APENAS seu lab. Se configurado, `code .` é alternativa. Abra Terminal > New Terminal e confira raiz e status.

```text
git rev-parse --show-toplevel
git status
```

Source Control deve detectar repo. Rótulos podem variar. Compare mudanças ali na próxima aula. GUI baseada em documentação, não executada em CI.

## Erros comuns e segurança

Não clique Publish, Sync, Clone ou Initialize Repository neste lab. Se Git não detectado, confira `git --version` no terminal integrado e reinicie editor. Confie só em pastas criadas/revisadas; evite extensões e tarefas desconhecidas.

## Exercício e autocorreção

Localize Source Control e terminal, ou use editor simples mais terminal. Dica: compare raiz do repo. Passe se explicar por que interfaces mostram mesmo estado Git. Hábito profissional: inspecionar visualmente e verificar com comandos.

## Referência rápida

- `git rev-parse --show-toplevel`
- `git status`

## Fontes oficiais

- [https://code.visualstudio.com/download](https://code.visualstudio.com/download)
- [https://code.visualstudio.com/docs/sourcecontrol/quickstart](https://code.visualstudio.com/docs/sourcecontrol/quickstart)
- [https://git-scm.com/docs/git-gui](https://git-scm.com/docs/git-gui)
