# Instalar o Git

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
— · [Índice](../README.pt-BR.md) · [Próximo](../02-terminal-and-help/README.pt-BR.md)
<!-- /navigation -->

**Nível:** iniciante · **Tempo estimado:** 25 min

**Pré-requisitos:** Nenhum; programação não exigida.

**Objetivo:** Instalar Git e verificar a versão.

## O que é e por quê

Git registra versões selecionadas de arquivos localmente. Não é editor nem linguagem de programação. O terminal recebe comandos e o shell (PowerShell, Bash ou Zsh) os interpreta. Instale Git uma vez por ambiente, não por projeto.

## Prática

Abra PowerShell no Windows ou Terminal no Linux/macOS. Teste `git --version`. Se já instalado, use versão mantida de pelo menos 2.40. Senão escolha APENAS seu SO:

Windows: use instalador oficial da arquitetura ou WinGet se disponível. Reabra terminal.

```powershell
winget install --id Git.Git -e --source winget
```

Debian/Ubuntu (com permissão):

```bash
sudo apt update
sudo apt install git
```

Fedora:

```bash
sudo dnf install git
```

macOS: solicite ferramentas de linha de comando Apple se Git ausente, ou Homebrew se já instalado e confiável; escolha um.

```bash
xcode-select --install
```

```bash
brew install git
```

Repita `git --version`. Esperado: versão, não comando inexistente. Instalações conferidas em documentação, não testadas em máquinas limpas.

## Erros comuns e segurança

Não rode todos instaladores nem use privilégios elevados para comandos Git normais. Se comando falhar, reabra terminal e confira PATH (diretórios pesquisados por programas). Consulte TI em dispositivos gerenciados.

## Exercício e autocorreção

Identifique SO e shell. Dica: instale só se ausente. Passe se `git --version` funcionar e explicar Git versus terminal. Em relatos profissionais, registre versão Git.

## Referência rápida

- `git --version`

## Fontes oficiais

- [https://git-scm.com/install/](https://git-scm.com/install/)
- [https://git-scm.com/install/win](https://git-scm.com/install/win)
- [https://git-scm.com/install/linux.html](https://git-scm.com/install/linux.html)
- [https://git-scm.com/install/mac](https://git-scm.com/install/mac)
