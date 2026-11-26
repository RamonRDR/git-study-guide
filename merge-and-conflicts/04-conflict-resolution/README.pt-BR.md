# Resolver e abortar conflitos de merge

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../03-merge-commit/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../05-squash-merge/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 45 min

**Pré-requisitos:** [Divergência e commits de merge](../03-merge-commit/README.pt-BR.md)

**Objetivo:** Inspecionar estágios não integrados do index, abortar com segurança, resolver e concluir merge.

## O que é e por quê

Conflito textual pode ocorrer quando branches editam mesma linha de modo incompatível. Git pausa com entradas não integradas no index: estágio 1 base, 2 lado atual, 3 recebido em merge comum. Marcadores no arquivo mostram alternativas: <<<<<<< HEAD, =======, >>>>>>> origem. Não são conteúdo final. Resolva entendendo ambas mudanças; editar/salvar não resolve index. `git add` marca caminho resolvido. `git merge --continue` conclui merge e pode abrir editor da mensagem; `git commit -m` também conclui se todos caminhos resolvidos.

## Prática

Crie NOVO lab descartável isolado pelo módulo 00 capítulo 03 e aula do primeiro commit. Mantenha shell dedicado original, não terminal do editor. Main inicial deve ter exatamente um commit, note.txt = practice, status limpo. Feche shell do lab anterior antes de iniciar. Siga verificações do capítulo 01 antes de cada operação que altera histórico.

[Configuração isolada do lab](../../getting-started/03-first-repository/README.pt-BR.md) · [Primeiro commit](../../getting-started/05-first-commit/README.pt-BR.md) · [Segurança e recuperação antes da integração](../01-integration-safety/README.pt-BR.md)

```text
git rev-parse --show-toplevel
git branch --show-current
git status --short
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Pare se raiz não for lab descartável, branch atual não for a indicada, status não estiver limpo antes de iniciar operação ou identidades não começarem com `Study Guide Example <learner@example.invalid>`. Antes de cada commit confira também diff preparado; pare com saída inesperada.

```text
git switch -c feat/note
```

No editor de texto, crie ou edite note.txt com exatamente uma linha: feature, com quebra final. Salve, depois prepare no shell dedicado:

```text
git add -- note.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Se diff e ambas identidades corretos, faça commit:

```text
git commit -m "docs: revise feature note"
```

```text
git switch main
```

No editor de texto, crie ou edite note.txt com exatamente uma linha: main, com quebra final. Salve, depois prepare no shell dedicado:

```text
git add -- note.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Se diff e ambas identidades corretos, faça commit:

```text
git commit -m "docs: revise main note"
```

```text
git rev-parse --show-toplevel
git branch --show-current
git status --short
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Confirme main limpa e identidades. Anote ID de main privadamente. Provoque conflito intencional:

```text
git rev-parse main
git merge --no-ff --no-edit feat/note
```

Espere não zero e conflito em note.txt. Pare se diferente. Inspecione, inclusive abrindo note.txt em editor simples:

```text
git status --short
git ls-files -u
git show :1:note.txt
git show :2:note.txt
git show :3:note.txt
```

Esperado UU note.txt, três estágios, base practice, atual main, recebido feature. Aborte primeiro, com operação em andamento:

```text
git merge --abort
git status --short
git rev-parse main
git show HEAD:note.txt
```

Espere main limpa, ID original e conteúdo main. Repita mesmo merge:

```text
git merge --no-ff --no-edit feat/note
```

Após confirmar mesmo conflito, substitua note.txt fictício inteiro por duas linhas, main e depois feature, quebra final; remova marcadores. Confira antes de registrar:

```text
git add -- note.txt
git ls-files -u
git diff --cached
git diff --cached --check
git status
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Sem entradas não integradas nem erros diff-check; leia arquivo real para garantir ausência de marcadores. Com conteúdo esperado e identidades fictícias, conclua com mensagem explícita (ou git merge --continue salvando mensagem do editor, não ambos):

```text
git commit -m "docs: resolve note conflict"
git rev-list --parents -1 HEAD
git show HEAD:note.txt
git status --short
```

Esperado dois pais, arquivo combinado de duas linhas e status limpo. Se usar continue e editor desconhecido abrir, consulte instruções; não apague mensagem aleatoriamente. Aborte enquanto merge estiver em andamento se dúvida.

## Erros comuns e segurança

Não escolha ours/theirs cegamente; entenda edições. Em rebase os lados diferem de merge comum. Nunca force resolução nem trate remoção de marcadores como validação. Projeto real precisa testes e review; conflitos binários/exclusão/renome podem exigir outras decisões.

Após cada lab independente, feche editor e shell dedicado, então exclua somente pasta pai temporária exata anotada no módulo 00 pelo gerenciador se não precisar mais. Nunca exclua guia, pasta pessoal ou repo de trabalho.

## Exercício e autocorreção

O que diferencia editado de resolvido? Resposta: add substitui estágios não integrados pelo resultado escolhido. Passe se abort restaurar estado, repetição resolver estágios e commit final tiver dois pais. Uso profissional: preservar intenção e testar resolução.

## Referência rápida

- `git ls-files -u`
- `git show :1:note.txt`
- `git add -- note.txt`
- `git merge --abort`
- `git merge --continue`

## Fontes oficiais

- [Git: git-merge](https://git-scm.com/docs/git-merge)
- [Git: git-ls-files](https://git-scm.com/docs/git-ls-files)
- [Git: git-show](https://git-scm.com/docs/git-show)
- [Git: git-diff](https://git-scm.com/docs/git-diff)
- [Git: git-commit](https://git-scm.com/docs/git-commit)
