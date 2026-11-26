# Rerere: reutilizar resoluções de conflitos

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../05-hooks/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../07-sparse-checkout/README.pt-BR.md)
<!-- /navigation -->

**Nível:** avançado · **Tempo estimado:** 45 min

**Pré-requisitos:** [13 Git avançado](../README.pt-BR.md) · [Segurança e governança](../../security/README.pt-BR.md)

**Objetivo:** Rerere registra preimage conflitada e postimage resolvida para Git reaplicar resolução compatível depois.

## O que é e por quê

Rerere registra preimage conflitada e postimage resolvida para Git reaplicar resolução compatível depois. Não prova que decisão anterior ainda atende intenção atual. Com rerere.autoupdate=false, inspecione arquivo e faça stage explícito. Equipes podem reduzir trabalho repetido em integrações longas.

## Prática

Crie um lab isolado novo pelo índice do módulo antes de cada prática. Rode um comando por vez; pare em resultado inesperado. Confira sandbox impresso e raiz antes de alterar. Use Git 2.34+ como base da prática; confira ajuda e pule recursos opcionais indisponíveis. Não execute em repositórios de produção.

Use duas branches a partir do HEAD atual do lab. Crie mudanças conflitantes na mesma linha. Primeiro merge deve conflitar; resolva com texto escolhido, rode rerere e commit. Inspecione status e histórico. Isso registra resolução; não presuma futura autorresolução correta. Se parar no conflito, use merge --abort no lab.

O segundo merge deve reportar conflito não resolvido, mas rerere deve restaurar `reviewed` no arquivo de trabalho. Como stage automático está desabilitado, `git ls-files -u` ainda mostra entradas não resolvidas. Inspecione o conteúdo; aborte esse merge repetido após o check. Se algum merge tiver sucesso inesperado ou o conteúdo divergir, pare e recrie o lab.

```bash
git config --local rerere.enabled true
git config --local rerere.autoupdate false
git switch -c side
printf '%s\n' 'side' > src/state.txt
git add -- src/state.txt
git commit -m "docs: side state"
git switch main
printf '%s\n' 'main' > src/state.txt
git add -- src/state.txt
git commit -m "docs: main state"
before=$(git rev-parse HEAD)
git merge side
git rerere status
printf '%s\n' 'reviewed' > src/state.txt
git rerere
git add -- src/state.txt
git commit -m "merge: reviewed resolution"
git switch -c repeat "$before"
git merge side
git ls-files -u -- src/state.txt
git diff -- src/state.txt
test "$(cat src/state.txt)" = reviewed
git merge --abort
git status --short
```

## Erros comuns e segurança

Use só o lab descartável e dados fictícios. Se estado divergir, pare; inspecione status e operação antes de abortar ou recriar lab. Feche shell dedicado e remova só sandbox anotado pelo gerenciador de arquivos após revisar conteúdo.

## Exercício e autocorreção

Rerere substitui review? Não; confira conteúdo e testes antes do stage.

## Referência rápida

- `git config --local rerere.enabled true`
- `git config --local rerere.autoupdate false`
- `git switch -c side`
- `git add -- src/state.txt`

## Fontes oficiais

- [https://git-scm.com/docs/git-rerere](https://git-scm.com/docs/git-rerere)
- [https://git-scm.com/docs/git-merge](https://git-scm.com/docs/git-merge)

---

<!-- navigation-footer -->
[Anterior](../05-hooks/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../07-sparse-checkout/README.pt-BR.md)
<!-- /navigation-footer -->
