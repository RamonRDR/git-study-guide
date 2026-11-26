# Inicializar, configurar e consultar ajuda

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Módulo anterior](../../git-architecture/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../02-status-add-commit/README.pt-BR.md)
<!-- /navigation -->

**Nível:** iniciante · **Tempo estimado:** 25 min

**Pré-requisitos:** [Primeiros passos](../../getting-started/README.pt-BR.md) · [Arquitetura Git](../../git-architecture/README.pt-BR.md)

**Objetivo:** Distinguir inicialização, escopos de configuração e comandos de ajuda.

## O que é e por quê

git init cria metadados normalmente em .git; --initial-branch define branch inicial (Git 2.28+). Segundo init normalmente reinicializa sem descartar histórico, mas não use como reparo. git config lê/grava ajustes: system, global, local e overrides por comando têm escopos diferentes. Use --local no lab e -c chave=valor por invocação. git help fornece ajuda completa; comando -h uso curto (pode retornar não zero).

## Prática

Inicie NOVO lab descartável isolado pelo módulo 00 capítulo 03, incluindo git init e identidades efetivas fictícias, mas ainda sem commit. Na subpasta repo rode:

```text
git config --local --get user.name
git config --local --get user.email
git config --show-origin --get user.email
git config --local core.autocrlf false
git config --local --get core.autocrlf
git -c core.autocrlf=true config --get core.autocrlf
git config --local --get core.autocrlf
git status -h
git help init
```

Esperado: identidade fictícia, ajuste local false; override da invocação true, depois local ainda false. --show-origin mostra caminho de origem; não compartilhe caminhos privados. Ajuda não muda repo; saia do pager com q. core.autocrlf controla conversão automática de quebras de linha; false evita essa conversão nestes exercícios de texto. Nenhum ajuste global alterado.

## Erros comuns e segurança

Use shell dedicado só neste lab. Confira Git 2.40+ conforme isolamento do módulo 00. Não rode init na pasta pessoal/trabalho; evite --global/--system e listar toda configuração. Se origem/identidade inesperada reinicie lab isolado sem alterar ajustes reais.

## Exercício e autocorreção

Preveja três saídas core.autocrlf. Resposta: false, true, false. Passe se explicar por que -c não persiste. Uso profissional: conferir origem de ajuste antes de diagnosticar.

## Referência rápida

- `git init`
- `git config`
- `git help`
- `git`

## Fontes oficiais

- [Git: git-init](https://git-scm.com/docs/git-init)
- [Git: git-config](https://git-scm.com/docs/git-config)
- [Git: git-help](https://git-scm.com/docs/git-help)
- [Git: git](https://git-scm.com/docs/git)

---

<!-- navigation-footer -->
[Módulo anterior](../../git-architecture/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../02-status-add-commit/README.pt-BR.md)
<!-- /navigation-footer -->
