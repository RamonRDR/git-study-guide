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

Crie pasta temporária nova, não guia nem projeto existente. Escolha seu shell.

```powershell
$lab = Join-Path ([System.IO.Path]::GetTempPath()) ("git-study-" + [guid]::NewGuid().ToString("N"))
New-Item -ItemType Directory -Path $lab -ErrorAction Stop
Set-Location $lab -ErrorAction Stop
Get-Location
```

```bash
lab=$(mktemp -d) && cd "$lab" && pwd
```

Pare se criação/navegação falhar. Na pasta vazia nova, `git rev-parse --show-toplevel` deve falhar (fora de repo). Se funcionar, escolha outra. Depois rode individualmente:

```text
git init --initial-branch=main
git config --local user.name "Study Guide Example"
git config --local user.email "learner@example.invalid"
git config --local commit.gpgsign false
git config --local --get user.name
git config --local --get user.email
git rev-parse --show-toplevel
git status
```

Esperado: identidade fictícia, pasta nova, branch main e nenhum commit. Assinatura desativada apenas no lab descartável; não altere políticas reais. Mantenha lab para próximas aulas.

## Erros comuns e segurança

Nunca inicialize no guia, pasta pessoal ou repo de trabalho. Não apague `.git` para corrigir erros. E-mail real pode ficar público ao compartilhar commits. Consulte apenas chaves locais, não dump completo. Hooks (scripts automáticos) ou ajustes existentes podem afetar prática; CI isola configuração. Na dúvida pare e crie lab novo.

## Exercício e autocorreção

Confira raiz, nome e e-mail. Passe se identidade fictícia, main e histórico vazio. Dica: `git config --local --get user.email`. Uso profissional: separar identidades por repo.

## Referência rápida

- `git rev-parse --show-toplevel`
- `git init --initial-branch=main`
- `git config --local --get user.email`
- `git status`

## Fontes oficiais

- [https://git-scm.com/docs/git-init](https://git-scm.com/docs/git-init)
- [https://git-scm.com/docs/git-config](https://git-scm.com/docs/git-config)
- [https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)
