# Detached HEAD e preservação do trabalho

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../04-safe-local-deletion/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo módulo](../../merge-and-conflicts/README.pt-BR.md)
<!-- /navigation -->

**Nível:** iniciante · **Tempo estimado:** 30 min

**Pré-requisitos:** [Exclusão segura de branches locais](../04-safe-local-deletion/README.pt-BR.md)

**Objetivo:** Inspecionar commit anterior e dar nome de branch persistente a commit detached.

## O que é e por quê

Normalmente HEAD é ref simbólica de branch. Detached HEAD aponta direto para commit. Permite inspecionar snapshot histórico ou testar versão sem mover branch. Novos commits em detached avançam HEAD, não branch nomeada. Antes de sair de commit detached que deseja manter, crie branch nele. Senão commit pode ficar inalcançável e ser removido; recuperação por reflog não é garantida. Diagrama textual: ligado HEAD -> main -> C1; detached HEAD -> C1, main -> C1; após commit detached HEAD -> C4 -> C1, main segue C1.

## Prática

Continue lab em main com status limpo. Confira raiz, depois entre detached HEAD em main:

```text
git rev-parse --show-toplevel
git status --short
git switch --detach main
git branch --show-current
git status
git rev-parse HEAD main
```

Esperado: branch --show-current vazio; status menciona detached HEAD; IDs iguais. Crie experiment.txt com experiment e quebra final, prepare e confira:

```text
git add -- experiment.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Só se identidades fictícias e diff esperado:

```text
git commit -m "docs: record experiment"
git rev-parse HEAD main
git log -1 --oneline
```

HEAD agora difere de main. ANTES de sair, preserve commit criando e selecionando branch nomeada em HEAD atual:

```text
git switch -c experiment/saved
git branch --show-current
git rev-parse HEAD experiment/saved
git status --short
git switch main
git ls-files
git show experiment/saved:experiment.txt
git branch --list
```

Esperado: IDs salvos iguais; main não contém experiment.txt; git show lê experiment da branch salva. Nenhuma integração. Para inspecionar commit histórico sem criar trabalho, escolha ID ou ref local existente com status limpo e volte com git switch main. Se já saiu de commit detached e sabe ID, confira git show ID e crie branch nele enquanto existir; recuperação detalhada depois.

## Erros comuns e segurança

Não saia antes de trabalho detached desejado ter ref nomeada. Não confie em recuperação automática nem use força. Mantenha lab só se precisar; senão feche editor e shell dedicado e exclua apenas pasta pai temporária exata anotada pelo gerenciador, conforme módulo 00.

## Exercício e autocorreção

Explique por que criação de branch preservou commit detached sem merge. Resposta: nova ref nomeia commit existente; main inalterada. Passe se conteúdo salvo legível a partir de main e status limpo. Uso profissional: investigar release antiga sem mover histórico compartilhado.

## Referência rápida

`git switch --detach REF`: inspecionar sem branch; `git switch -c NAME`: nomear commit atual e ligar HEAD; `git branch --show-current`: vazio em detached.

## Fontes oficiais

- [Git: git-switch](https://git-scm.com/docs/git-switch)
- [Git: git-checkout](https://git-scm.com/docs/git-checkout)
- [Git: git-branch](https://git-scm.com/docs/git-branch)
- [Git: git-symbolic-ref](https://git-scm.com/docs/git-symbolic-ref)

---

<!-- navigation-footer -->
[Anterior](../04-safe-local-deletion/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo módulo](../../merge-and-conflicts/README.pt-BR.md)
<!-- /navigation-footer -->
