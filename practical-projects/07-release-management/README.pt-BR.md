# Gestão de releases

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../06-automated-quality-pipeline/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../08-professional-engineering-workflow/README.pt-BR.md)
<!-- /navigation -->

**Nível:** avançado · **Tempo estimado:** 60 min

**Pré-requisitos:** [professional-workflows/12-release-management](../../professional-workflows/12-release-management/README.pt-BR.md) · Git 2.40+ · Bash/Git Bash · tar

**Objetivo:** Registre e marque versão 1.0.0, adicione ready sem remover draft, revise e marque 1.1.0, depois prepare arquivo de código do snapshot marcado. Faça mudança posterior e demonstre tag de release ainda aponta ao commit anterior.

## Cenário

Catálogo fictício de texto declara contrato público de status. Release inicial suporta draft; exemplo adicional ready retrocompatível motiva release minor. Tags anotadas locais identificam revisões exatas; nenhuma release de plataforma é publicada.

## Preparação descartável

Use apenas a seção Preparação descartável de [Meu primeiro repositório](../01-my-first-repository/README.pt-BR.md). Abra shell Bash/Git Bash dedicado novo; confira raiz impressa, identidades fictícias e ausência de remotos antes de prosseguir. Não execute desafio 01. Git 2.40+. Execute um comando por vez, pare em falha inesperada e nunca execute no guia.

## Desafio

Registre e marque versão 1.0.0, adicione ready sem remover draft, revise e marque 1.1.0, depois prepare arquivo de código do snapshot marcado. Faça mudança posterior e demonstre tag de release ainda aponta ao commit anterior. Tente antes de ler a solução.

## Dicas progressivas

SemVer minor significa funcionalidade pública retrocompatível sob contrato declarado, não quantidade de edições. Tags anotadas são objetos resolvíveis a commits; use git archive para conteúdo do snapshot e inspecione arquivo.

## Solução de referência

Registre duas versões com notas explícitas nas mensagens das tags. Confira preservação da funcionalidade draft existente.

```bash
printf '%s\n' 'status: draft' > catalog.txt
git add catalog.txt
git commit -m 'docs: initialize catalog'
git tag -a v1.0.0 -m 'Initial draft contract'
printf '%s\n' 'status: draft' 'status: ready' > catalog.txt
git add catalog.txt
git diff --cached --check
git diff --cached
git commit -m 'feat: add ready status'
git tag -a v1.1.0 -m 'Add backward-compatible ready status'
released=$(git rev-parse 'v1.1.0^{commit}')
git cat-file -t v1.1.0
git archive --format=tar --output="$sandbox/catalog-v1.1.0.tar" v1.1.0
tar -tf "$sandbox/catalog-v1.1.0.tar"
tar -xOf "$sandbox/catalog-v1.1.0.tar" catalog.txt
```

Avance main local com mudança futura separada; demonstre tag imutável por convenção, não protegida automaticamente por Git local.

```bash
printf '%s\n' 'future work' > future.txt
git add future.txt
git commit -m 'docs: begin future work'
test "$(git rev-parse 'v1.1.0^{commit}')" = "$released"
test "$(git rev-parse HEAD)" != "$released"
git show v1.0.0:catalog.txt
git show v1.1.0:catalog.txt
git status --porcelain
```

## Critérios de sucesso

Ambas tags anotadas; v1.1.0 mantém draft e adiciona ready, e tar contém só catalog.txt com conteúdo exato, sem .git ou future.txt. Tag não move quando main avança. Explique por que não é release publicada em plataforma.

Teste fixo de manutenção (não código de aluno): `tests/test_git_practical_projects.py::test_release_management`.

## Recuperação e limpeza

Confira versões e destinos antes de marcar. Não sobrescreva tag publicada; use política de correção de release. Draft hospedado opcional só em repositório próprio autorizado com tag existente verificada e sem pré-requisito pago. Feche o shell dedicado e remova só o sandbox impresso verificado pelo gerenciador de arquivos. Preserve trabalho desejado antes.

## Fontes oficiais

- <https://git-scm.com/docs/git-tag>
- <https://git-scm.com/docs/git-archive>
- <https://git-scm.com/docs/git-show>
- <https://semver.org/spec/v2.0.0.html>

---

<!-- navigation-footer -->
[Anterior](../06-automated-quality-pipeline/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../08-professional-engineering-workflow/README.pt-BR.md)
<!-- /navigation-footer -->
