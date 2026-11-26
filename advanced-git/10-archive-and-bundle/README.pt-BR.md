# Archive e bundle: distribuir snapshots ou histórico

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../09-blame-and-grep/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../11-integrated-advanced-lab/README.pt-BR.md)
<!-- /navigation -->

**Nível:** avançado · **Tempo estimado:** 40 min

**Pré-requisitos:** [13 Git avançado](../README.pt-BR.md) · [Segurança e governança](../../security/README.pt-BR.md)

**Objetivo:** Archive exporta tree selecionada (sujeita a atributos) sem histórico; bundle empacota refs e objetos Git e serve como fonte de transferência offline.

## O que é e por quê

Archive exporta tree selecionada (sujeita a atributos) sem histórico; bundle empacota refs e objetos Git e serve como fonte de transferência offline. Bundles podem ser incrementais e exigir pré-requisitos. Nenhum é backup completo de arquivos não rastreados, configurações locais ou segredos; revise permissões de distribuição.

## Prática

Crie um lab isolado novo pelo índice do módulo antes de cada prática. Rode um comando por vez; pare em resultado inesperado. Confira sandbox impresso e raiz antes de alterar. Use Git 2.34+ como base da prática; confira ajuda e pule recursos opcionais indisponíveis. Não execute em repositórios de produção.

Grave ambas saídas fora do repo no sandbox novo. Verifique bundle, clone em outra pasta própria, compare HEAD e inspecione lista do archive com unzip se disponível. Não publique artefatos automaticamente; bundle pode conter dados sensíveis históricos.

```bash
git archive --format=zip -o "$sandbox/snapshot.zip" HEAD
git bundle create "$sandbox/history.bundle" main
git bundle verify "$sandbox/history.bundle"
git clone -b main "$sandbox/history.bundle" "$sandbox/recovered"
test "$(git rev-parse HEAD)" = "$(git -C "$sandbox/recovered" rev-parse HEAD)"
```

## Erros comuns e segurança

Use só o lab descartável e dados fictícios. Se estado divergir, pare; inspecione status e operação antes de abortar ou recriar lab. Feche shell dedicado e remova só sandbox anotado pelo gerenciador de arquivos após revisar conteúdo.

## Exercício e autocorreção

Qual saída permite clone Git da branch escolhida? Bundle completo, não archive zip.

## Referência rápida

- `git archive --format=zip -o "$sandbox/snapshot.zip" HEAD`
- `git bundle create "$sandbox/history.bundle" main`
- `git bundle verify "$sandbox/history.bundle"`
- `git clone -b main "$sandbox/history.bundle" "$sandbox/recovered"`

## Fontes oficiais

- [https://git-scm.com/docs/git-archive](https://git-scm.com/docs/git-archive)
- [https://git-scm.com/docs/git-bundle](https://git-scm.com/docs/git-bundle)

---

<!-- navigation-footer -->
[Anterior](../09-blame-and-grep/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../11-integrated-advanced-lab/README.pt-BR.md)
<!-- /navigation-footer -->
