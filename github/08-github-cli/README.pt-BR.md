# GitHub CLI opcional e inspeção somente leitura

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../07-tags-and-releases/README.pt-BR.md) · [Índice](../README.pt-BR.md) · —
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 25 min

**Pré-requisitos:** [Remotos](../../remote-repositories/README.pt-BR.md) · [Histórico e recuperação](../../history-and-recovery/README.pt-BR.md) · [Tags e GitHub Releases](../07-tags-and-releases/README.pt-BR.md)

**Objetivo:** Distinguir gh de git e inspecionar metadados hospedados sem escrita.

## O que é e por quê

GitHub CLI (gh) é cliente opcional de APIs GitHub. git gerencia histórico Git local e transporte; gh lê ou altera recursos hospedados conforme autenticação e permissões. Comando terminal pode ter efeitos remotos; repo create, issue create, pr merge e release create são escritas. Use alvos --repo explícitos e comandos de leitura primeiro. Navegador ou exercícios em papel bastam; instalar CLI ou login não é exigido. Instale só por instruções oficiais se quiser; autenticação pode usar navegador e armazenamento aprovado. Tokens do ambiente podem prevalecer sobre credenciais guardadas; nunca exiba valores.

## Prática

Exercício autenticado opcional só leitura: primeiro execute gh --version, gh help e gh auth status --hostname github.com em privado. Se autenticação falhar, pare ou siga instruções oficiais; nunca cole saída com dados da conta. Substitua OWNER/study-sandbox pelo identificador real de sandbox autorizado, não placeholder literal. Confirme gh repo view identifica repo pretendido antes de listar issues ou PRs. Use navegador se sem sandbox/conta. Sem escrita, sem exibir token, sem automação exigida. Esperado: nome/visibilidade e listas de issues/PRs abertos acessíveis; listas podem estar vazias.

```text
gh --version
gh help
gh auth status --hostname github.com
```

Confirme conta correta em privado; substitua placeholder e inspecione primeiro resultado antes de executar os outros dois comandos.

```text
gh repo view OWNER/study-sandbox --json nameWithOwner,visibility,defaultBranchRef
gh issue list --repo OWNER/study-sandbox --state open
gh pr list --repo OWNER/study-sandbox --state open
```


## Erros comuns e segurança

Nunca execute gh auth token ou flags que exibam token para diagnóstico em sessão compartilhada. Não execute comandos de issue não confiável. Conta ou repo errado: pare antes de escrever. Não precisa logout nem excluir credenciais para limpeza; siga política normal da conta.

## Exercício e autocorreção

Passe se classificar git status como inspeção local, gh pr list como inspeção hospedada e gh pr merge como escrita hospedada. Explique por que listar com sucesso não implica permissão merge.

## Referência rápida

- `gh --version`
- `gh repo view`
- `gh issue list`
- `gh pr list`

## Fontes oficiais

- <https://cli.github.com/manual/>
- <https://cli.github.com/manual/gh_auth_status>
- <https://cli.github.com/manual/gh_repo_view>
- <https://cli.github.com/manual/gh_issue_list>
- <https://cli.github.com/manual/gh_pr_list>
