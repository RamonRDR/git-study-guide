# Primeiro repositório e configuração

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../02-terminal-and-help/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../04-editor-and-gui/README.pt-BR.md)
<!-- /navigation -->

**Nível:** iniciante · **Tempo estimado:** 30 min

**Pré-requisitos:** [Terminal e ajuda](../02-terminal-and-help/README.pt-BR.md)

**Objetivo:** Criar repo descartável e configurar identidade local fictícia.

## O que é e por quê

Repo local guarda metadados e histórico em diretório oculto `.git`. Branch é linha de desenvolvimento nomeada; main é nome inicial. Init cria metadados, não commit. Identidade é autoria registrada, não autenticação. Configuração system vale amplamente, global para usuário e local para este repo; local normalmente prevalece.

## Prática

Abra um novo terminal PowerShell ou Bash dedicado apenas ao lab (no macOS/Zsh, inicie Bash com `bash` antes). Mantenha-o aberto até o módulo 01. Os comandos limpam variáveis Git herdadas somente neste shell e criam pasta pai nova com pasta do repo, configuração global vazia e diretório de template vazio. Excluem configuração system/global e overrides herdados de autor/committer; template vazio evita hooks herdados. Não editam sua configuração Git real. Use Git mantido 2.40 ou superior para este isolamento. Escolha um shell; pare em qualquer erro.

```powershell
Get-ChildItem Env: | Where-Object { $_.Name -like 'GIT_*' } | ForEach-Object {
    Remove-Item -LiteralPath ("Env:" + $_.Name) -ErrorAction Stop
}
$lab = Join-Path ([System.IO.Path]::GetTempPath()) ("git-study-" + [guid]::NewGuid().ToString("N"))
New-Item -ItemType Directory -Path $lab -ErrorAction Stop
New-Item -ItemType Directory -Path (Join-Path $lab "repo"), (Join-Path $lab "template") -ErrorAction Stop
$env:GIT_CONFIG_GLOBAL = Join-Path $lab "gitconfig"
New-Item -ItemType File -Path $env:GIT_CONFIG_GLOBAL -ErrorAction Stop
$env:GIT_CONFIG_NOSYSTEM = "1"
$env:GIT_TEMPLATE_DIR = Join-Path $lab "template"
$env:GIT_TERMINAL_PROMPT = "0"
Set-Location (Join-Path $lab "repo") -ErrorAction Stop
Get-Location
```

```bash
for name in $(compgen -e); do
    case "$name" in GIT_*) unset "$name" ;; esac
done
lab=$(mktemp -d) &&
mkdir "$lab/repo" "$lab/template" &&
touch "$lab/gitconfig" &&
export GIT_CONFIG_GLOBAL="$lab/gitconfig" GIT_CONFIG_NOSYSTEM=1 &&
export GIT_TEMPLATE_DIR="$lab/template" GIT_TERMINAL_PROMPT=0 &&
cd "$lab/repo" && pwd
```

Anote caminho da pasta pai privadamente para limpeza. Na subpasta repo nova vazia, `git rev-parse --show-toplevel` deve falhar antes da inicialização; se funcionar, pare e escolha outro lab. Rode individualmente:

```text
git init --initial-branch=main
git config --local user.name "Study Guide Example"
git config --local user.email "learner@example.invalid"
git config --local commit.gpgsign false
git config --local --get user.name
git config --local --get user.email
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
git rev-parse --show-toplevel
git status
```

Ambas identidades efetivas devem começar com `Study Guide Example <learner@example.invalid>`; timestamps/fusos variam. Se alguma diferir ou comando falhar, pare; não faça commit. Esperado: raiz é subpasta repo, main sem commits. Mantenha mesmo shell dedicado e não use para outros repos. Assinatura desativada só neste lab descartável; não altere política real.

## Erros comuns e segurança

Nunca inicialize no guia, pasta pessoal ou repo de trabalho. Não apague `.git` para corrigir erros. E-mail real pode ficar público ao compartilhar commits. Consulte apenas chaves locais, não dump completo. Configuração local user sozinha não basta: ajustes herdados de autor/committer podem sobrescrevê-la. Hooks são scripts automáticos. Use shell dedicado isolado; se falhar, feche e reinicie lab em vez de alterar ajustes pessoais.

## Exercício e autocorreção

Confira raiz, nome e e-mail. Passe se identidade fictícia, main e histórico vazio. Dica: `git var GIT_AUTHOR_IDENT` / `git var GIT_COMMITTER_IDENT`. Uso profissional: separar identidades por repo.

## Referência rápida

- `git rev-parse --show-toplevel`
- `git init --initial-branch=main`
- `git config --local --get user.email`
- `git var GIT_AUTHOR_IDENT`
- `git var GIT_COMMITTER_IDENT`
- `git status`

## Fontes oficiais

- [https://git-scm.com/docs/git-init](https://git-scm.com/docs/git-init)
- [https://git-scm.com/docs/git-config](https://git-scm.com/docs/git-config)
- [https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)

- [Git: git-var](https://git-scm.com/docs/git-var)
