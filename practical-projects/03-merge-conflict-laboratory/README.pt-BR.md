# Laboratório de conflitos de merge

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../02-two-developers-one-project/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../04-the-lost-commit/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 45 min

**Pré-requisitos:** [merge-and-conflicts/04-conflict-resolution](../../merge-and-conflicts/04-conflict-resolution/README.pt-BR.md) · Git 2.40+ · Bash/Git Bash

**Objetivo:** Crie branches divergentes, reproduza conflito, inspecione estágios não mesclados, resolva para status: reviewed e conclua commit de merge com dois pais.

## Cenário

Duas branches revisam a mesma linha fictícia de status de formas distintas. Integração deve preservar resolução combinada intencional.

## Preparação descartável

Use apenas a seção Preparação descartável de [Meu primeiro repositório](../01-my-first-repository/README.pt-BR.md). Abra shell Bash/Git Bash dedicado novo; confira raiz impressa, identidades fictícias e ausência de remotos antes de prosseguir. Não execute desafio 01. Git 2.40+. Execute um comando por vez, pare em falha inesperada e nunca execute no guia.

## Desafio

Crie branches divergentes, reproduza conflito, inspecione estágios não mesclados, resolva para status: reviewed e conclua commit de merge com dois pais. Tente antes de ler a solução.

## Dicas progressivas

Ambos lados devem editar mesma linha original. Resultado não zero esperado de merge não é integração bem-sucedida. Prepare resolução escolhida antes do commit.

## Solução de referência

Crie base comum e pontas divergentes.

```bash
printf '%s\n' 'status: draft' > notes.txt
git add notes.txt
git commit -m 'docs: initialize notes'
git switch -c feat/review
printf '%s\n' 'status: ready' > notes.txt
git add notes.txt
git commit -m 'docs: propose ready'
git switch main
printf '%s\n' 'status: checked' > notes.txt
git add notes.txt
git commit -m 'docs: record check'
before=$(git rev-parse HEAD)
feature=$(git rev-parse feat/review)
git merge feat/review
```

O último comando deve falhar com conflito. Continue só se MERGE_HEAD existir e notes.txt tiver estágios não mesclados. Inspecione, depois substitua arquivo fictício inteiro e registre.

```bash
git rev-parse --verify MERGE_HEAD
git status --short
git ls-files -u -- notes.txt
git show :1:notes.txt
git show :2:notes.txt
git show :3:notes.txt
printf '%s\n' 'status: reviewed' > notes.txt
git add notes.txt
git diff --cached --check
git commit -m 'merge: reconcile review status'
test "$(git rev-parse HEAD^1)" = "$before"
test "$(git rev-parse HEAD^2)" = "$feature"
git status --porcelain
git show HEAD:notes.txt
```

## Critérios de sucesso

Estágios 1/2/3 existiam antes da resolução; merge final tem dois pais esperados em ordem, conteúdo reviewed e index e tree limpos. Marcador de conflito isolado não é resultado correto.

Teste fixo de manutenção (não código de aluno): `tests/test_git_practical_projects.py::test_conflict_resolution`.

## Recuperação e limpeza

Durante merge comum ativo, preserve edições desejadas antes de git merge --abort. Após conclusão inspecione pais; não redefina histórico compartilhado. Recrie laboratório descartável se necessário. Feche o shell dedicado e remova só o sandbox impresso verificado pelo gerenciador de arquivos. Preserve trabalho desejado antes.

## Fontes oficiais

- <https://git-scm.com/docs/git-merge>
- <https://git-scm.com/docs/git-status>
- <https://git-scm.com/docs/git-ls-files>

---

<!-- navigation-footer -->
[Anterior](../02-two-developers-one-project/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../04-the-lost-commit/README.pt-BR.md)
<!-- /navigation-footer -->
