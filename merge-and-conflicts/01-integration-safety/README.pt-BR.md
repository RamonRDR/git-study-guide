# Segurança e recuperação antes da integração

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
— · [Índice](../README.pt-BR.md) · [Próximo](../02-fast-forward/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 25 min

**Pré-requisitos:** [Gerenciamento de branches](../../branches/README.pt-BR.md) · [Configuração isolada do lab](../../getting-started/03-first-repository/README.pt-BR.md) · [Primeiro commit](../../getting-started/05-first-commit/README.pt-BR.md)

**Objetivo:** Identificar operação, pré-requisitos e saída segura antes de combinar históricos.

## O que é e por quê

Integração combina mudanças de linhas de histórico distintas. Merge pode avançar branch ou criar commit com múltiplos pais. Squash prepara conteúdo combinado sem registrar ancestralidade da origem. Rebase reaplica commits em outra base e normalmente produz novos IDs. Conflito ocorre quando Git não consegue decidir resultado combinado com segurança. Estado inicial limpo, refs conhecidas, identidade fictícia e referências locais de backup facilitam inspeção. Nenhuma dessas operações envia mudanças a servidor.

## Prática

Crie NOVO lab descartável isolado pelo módulo 00 capítulo 03 e aula do primeiro commit. Mantenha shell dedicado original, não terminal do editor. Main inicial deve ter exatamente um commit, note.txt = practice, status limpo. Feche shell do lab anterior antes de iniciar. Siga verificações do capítulo 01 antes de cada operação que altera histórico.

```text
git rev-parse --show-toplevel
git branch --show-current
git status --short
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Pare se raiz não for lab descartável, branch atual não for a indicada, status não estiver limpo antes de iniciar operação ou identidades não começarem com `Study Guide Example <learner@example.invalid>`. Antes de cada commit confira também diff preparado; pare com saída inesperada.

```text
git log --oneline --all --graph --decorate
git branch --list
git remote -v
```

Antes de rebase, crie branch separada na ponta original (ex.: backup/feature). Preserva ref nomeada de trabalho commitado, não arquivos sem commit nem backup externo. Quando merge comum parar por conflito, confira status; `git merge --abort` tenta restaurar estado pré-merge. Quando rebase parar, `git rebase --abort` volta à branch/estado original; `git rebase --continue` retoma após resolução. Use abort da operação em andamento. Comece limpo; abort não garante reconstrução de mudanças não commitadas preexistentes. `git merge --squash` não cria MERGE_HEAD, então abort de merge comum não é undo geral do squash. Se lab squash falhar, pare e descarte só aquele lab após conferir localização. Recuperação de operações concluídas vem depois.

## Erros comuns e segurança

Nunca faça rebase de histórico compartilhado/publicado nestes exercícios; nunca force push, reset hard ou rode contra este guia. Abort não desfaz operação concluída. Em estado inesperado, pare e confira em vez de empilhar comandos.

Após cada lab independente, feche editor e shell dedicado, então exclua somente pasta pai temporária exata anotada no módulo 00 pelo gerenciador se não precisar mais. Nunca exclua guia, pasta pessoal ou repo de trabalho.

## Exercício e autocorreção

Escolha próximo passo seguro em merge conflitante: status, depois merge --abort ou resolver e continuar. Para rebase, rebase --abort/--continue. Passe se explicar por que começo limpo e ref backup importam. Uso profissional: combinar política antes de tocar histórico compartilhado.

## Referência rápida

- `git status`
- `git merge --abort`
- `git rebase --abort`
- `git rebase --continue`

## Fontes oficiais

- [Git: git-merge](https://git-scm.com/docs/git-merge)
- [Git: git-rebase](https://git-scm.com/docs/git-rebase)
- [Git: git-status](https://git-scm.com/docs/git-status)
- [Git: git-branch](https://git-scm.com/docs/git-branch)
