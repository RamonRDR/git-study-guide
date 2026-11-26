# Criar e alternar branches locais

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Módulo anterior](../../basic-commands/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../02-start-points-and-comparison/README.pt-BR.md)
<!-- /navigation -->

**Nível:** iniciante · **Tempo estimado:** 35 min

**Pré-requisitos:** [Configuração isolada do lab](../../getting-started/03-first-repository/README.pt-BR.md) · [Primeiro commit](../../getting-started/05-first-commit/README.pt-BR.md) · [Comandos básicos](../../basic-commands/README.pt-BR.md)

**Objetivo:** Criar referências de branch e verificar qual HEAD seleciona.

## O que é e por quê

Uma branch local é referência móvel a commit, não segunda pasta nem cópia integral. Criar branch em HEAD acrescenta referência sem mudar index ou working tree. Alternar seleciona branch destino e atualiza arquivos rastreados/index conforme necessário. Commit normalmente avança apenas branch ativa. `git branch NAME [START]` cria sem alternar; `git switch NAME` alterna; `git switch -c NAME [START]` cria e alterna. Switch surgiu no Git 2.23; lab exige 2.40+ pelo módulo 00. Tutoriais antigos usam checkout para alternância e outras operações; guia prefere switch pela clareza.

## Prática

Inicie NOVO repo descartável usando configuração isolada do módulo 00 capítulo 03 e primeiro commit do capítulo 05. Não use repo do guia. Mantenha shell dedicado até fim do módulo. Esperado exatamente um commit em main com note.txt contendo practice e status limpo. Confira raiz, status e identidades antes de continuar.

```text
git rev-parse --show-toplevel
git status --short
git log --oneline
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Se raiz não for lab, status não limpo ou identidade não fictícia, pare. Caso contrário rode:

```text
git branch feat/note
git branch --list
git symbolic-ref HEAD
git rev-parse main feat/note
git switch feat/note
git branch --show-current
git status --short
```

Inicialmente IDs iguais e HEAD refs/heads/main; após switch HEAD nomeia feat/note. Arquivo ainda contém practice. Diagrama textual: HEAD -> feat/note -> C1; main -> C1. Ambos nomes apontam C1. Edite note.txt para feature (uma linha, quebra final), salve e prepare só arquivo:

```text
git add -- note.txt
git diff --cached -- note.txt
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Só se mudança preparada e ambas identidades corretas:

```text
git commit -m "docs: revise feature note"
git log --oneline --all --graph --decorate
git switch main
git show HEAD:note.txt
git status --short
git switch feat/note
git show HEAD:note.txt
```

Esperado: main ainda C1 com practice; feat/note C2 com feature. Diagrama: main -> C1; HEAD -> feat/note -> C2 -> C1 (última seta é histórico de pais). Alternar não é integrar.

## Erros comuns e segurança

Confira status antes de alternar; edições não registradas compatíveis podem acompanhar troca, conflitantes podem bloqueá-la. Não use força/descarte. Não crie branches de HEAD indesejado. Nenhum remote neste lab.

## Exercício e autocorreção

Preveja commit de main após commit de feature. Resposta: inalterado. Passe se branch --show-current e versões de arquivo corresponderem. Uso profissional: isolar alteração pequena antes de review.

## Referência rápida

`git branch NAME [START]`: criar; `git switch NAME`: selecionar; `git switch -c NAME [START]`: criar e selecionar; `git branch --show-current`: branch ativa.

## Fontes oficiais

- [Git: git-branch](https://git-scm.com/docs/git-branch)
- [Git: git-switch](https://git-scm.com/docs/git-switch)
- [Git: git-symbolic-ref](https://git-scm.com/docs/git-symbolic-ref)

---

<!-- navigation-footer -->
[Módulo anterior](../../basic-commands/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../02-start-points-and-comparison/README.pt-BR.md)
<!-- /navigation-footer -->
