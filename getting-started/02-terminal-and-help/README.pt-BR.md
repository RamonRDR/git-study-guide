# Terminal e ajuda

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../01-install-git/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../03-first-repository/README.pt-BR.md)
<!-- /navigation -->

**Nível:** iniciante · **Tempo estimado:** 20 min

**Pré-requisitos:** [Instalar o Git](../01-install-git/README.pt-BR.md)

**Objetivo:** Navegar por diretórios e consultar ajuda.

## O que é e por quê

Diretório atual é onde caminhos relativos começam. Repositório é pasta com metadados e histórico Git. Git normalmente o encontra a partir do diretório atual. Comandos têm programa, operação e argumentos opcionais; saiba onde está antes de alterar.

## Prática

Tente estas operações de navegação/ajuda. PowerShell e Bash/Zsh têm sintaxes diferentes.

```powershell
Get-Location
Get-ChildItem
Set-Location $HOME
```

```bash
pwd
ls
cd "$HOME"
```

```text
git --version
git status -h
git help status
```

Ajuda curta lista opções; completa pode abrir manual ou navegador. Pressione q para sair de pager (visualizador rolável).

## Erros comuns e segurança

Não copie símbolos do prompt como `$` ou `PS>`. Use aspas em caminhos com espaços. `git status` fora de repo normalmente informa ausência de repo; não é falha de instalação. Não compartilhe prints com caminhos privados.

## Exercício e autocorreção

Descubra pasta atual e consulte `git add -h`. Dica: diferencie shell e Git. Passe se achar uma opção sem mudar arquivos. Hábito profissional: confira localização do projeto antes de rodar comandos.

## Referência rápida

- `git --version`
- `git status -h`
- `git help status`

## Fontes oficiais

- [https://git-scm.com/docs/git-help](https://git-scm.com/docs/git-help)
- [https://git-scm.com/docs/gittutorial](https://git-scm.com/docs/gittutorial)
