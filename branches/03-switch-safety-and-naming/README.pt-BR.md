# Alternância segura e nomes de branches

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../02-start-points-and-comparison/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../04-safe-local-deletion/README.pt-BR.md)
<!-- /navigation -->

**Nível:** iniciante · **Tempo estimado:** 25 min

**Pré-requisitos:** [Pontos de partida e comparação de branches](../02-start-points-and-comparison/README.pt-BR.md)

**Objetivo:** Reconhecer troca bloqueada e renomear branch sem perder commits.

## O que é e por quê

Git pode preservar edições locais compatíveis na troca; normalmente recusa troca que sobrescreveria edições conflitantes ou arquivos não rastreados no caminho. Working tree e index não são privados por branch em um checkout. `git branch -m NEW` renomeia atual; `git branch -m OLD NEW` renomeia outra local. Preserva referência de commit e move config/reflog associados se presentes. Reflog registra movimentos locais de refs; detalhes depois. Nomes feat/note, fix/typo e docs/overview comunicam intenção; convenções não são requisitos Git. `git check-ref-format --branch NAME` valida sintaxe (não disponibilidade). Evite espaços, sequências reservadas e diferenças apenas de caixa pela portabilidade.

## Prática

No mesmo lab, comece docs/overview com status limpo. Alterne para feat/note, anote ID, renomeie e confira ID:

```text
git status --short
git switch feat/note
git rev-parse HEAD
git check-ref-format --branch feat/note-revision
git branch -m feat/note-revision
git branch --show-current
git rev-parse HEAD
git branch --list
```

Esperado: mesmo ID, novo nome feat/note-revision, nome antigo ausente. Edite note.txt de feature para unfinished e salve sem preparar. Confira, então tente troca intencionalmente neste lab descartável:

```text
git status --short
git diff -- note.txt
git switch main
```

Recusa esperada: main contém practice, então troca sobrescreveria note alterado. Confirme ainda em feat/note-revision e conteúdo unfinished. Se troca funcionar inesperadamente, pare e inspecione; nunca force. Para continuar, altere manualmente APENAS note.txt fictício de volta para feature com quebra original (descarte intencional da edição de teste, não trabalho real). Confira status limpo, depois alterne:

```text
git branch --show-current
git status --short
```

Somente após status vazio:

```text
git switch main
git show HEAD:note.txt
git status --short
```

## Erros comuns e segurança

Não use switch --discard-changes nem branch -M aqui. Não apague edições reais para trocar. Preserve-as em commit intencional na branch adequada ou técnica de recuperação revisada depois. Não renomeie branch compartilhada sem coordenação; renome/tracking remoto fica para módulo 06.

## Exercício e autocorreção

Por que switch falhou? Resposta: sobrescreveria edição local rastreada. Renome cria commit? Não. Passe se nome e ID verificados e nenhuma edição perdida sem intenção. Uso profissional: combinar nomes portáveis e descritivos.

## Referência rápida

`git branch -m OLD NEW`: renomear; `git check-ref-format --branch NAME`: sintaxe; `git status --short`: conferir antes da troca.

## Fontes oficiais

- [Git: git-switch](https://git-scm.com/docs/git-switch)
- [Git: git-branch](https://git-scm.com/docs/git-branch)
- [Git: git-check-ref-format](https://git-scm.com/docs/git-check-ref-format)
