# Hooks: automação local e confiança

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../04-subtree/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../06-rerere/README.pt-BR.md)
<!-- /navigation -->

**Nível:** avançado · **Tempo estimado:** 40 min

**Pré-requisitos:** [13 Git avançado](../README.pt-BR.md) · [Segurança e governança](../../security/README.pt-BR.md)

**Objetivo:** Hooks são programas chamados em eventos do Git, como pre-commit.

## O que é e por quê

Hooks são programas chamados em eventos do Git, como pre-commit. Resultado não zero no pre-commit aborta o commit. Hooks normalmente não são copiados pelo clone; core.hooksPath muda o local. Checks locais melhoram feedback, mas não substituem checks obrigatórios do servidor. Nunca execute hook de origem não confiável.

## Prática

Crie um lab isolado novo pelo índice do módulo antes de cada prática. Rode um comando por vez; pare em resultado inesperado. Confira sandbox impresso e raiz antes de alterar. Use Git 2.34+ como base da prática; confira ajuda e pule recursos opcionais indisponíveis. Não execute em repositórios de produção.

No lab novo, crie hook próprio inofensivo que sempre rejeita commit, só em pasta irmã nova. `chmod` vale em ambientes Bash com scripts executáveis. Confira HEAD inalterado e conteúdo staged intacto após rejeição; se execução não for suportada, pare. Remova apenas configuração local do lab depois; nunca contorne checks de projeto real.

```bash
mkdir "$sandbox/hooks"
printf '%s\n' '#!/bin/sh' 'exit 1' > "$sandbox/hooks/pre-commit"
chmod +x "$sandbox/hooks/pre-commit"
git config --local core.hooksPath "$sandbox/hooks"
before=$(git rev-parse HEAD)
printf '%s\n' 'review' > docs/review.txt
git add -- docs/review.txt
git commit -m "docs: hook practice"
test "$(git rev-parse HEAD)" = "$before"
git diff --cached --name-only
git config --local --unset core.hooksPath
```

## Erros comuns e segurança

Use só o lab descartável e dados fictícios. Se estado divergir, pare; inspecione status e operação antes de abortar ou recriar lab. Feche shell dedicado e remova só sandbox anotado pelo gerenciador de arquivos após revisar conteúdo.

## Exercício e autocorreção

Por que CI deve impor check de forma independente? Hooks são locais, configuráveis e não são fronteira confiável de enforcement.

## Referência rápida

- `git config --local core.hooksPath "<sandbox>/hooks"`
- `git add -- docs/review.txt`
- `git commit -m "docs: hook practice"`
- `git diff --cached --name-only`

## Fontes oficiais

- [https://git-scm.com/docs/githooks](https://git-scm.com/docs/githooks)
- [https://git-scm.com/docs/git-config](https://git-scm.com/docs/git-config)

---

<!-- navigation-footer -->
[Anterior](../04-subtree/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../06-rerere/README.pt-BR.md)
<!-- /navigation-footer -->
