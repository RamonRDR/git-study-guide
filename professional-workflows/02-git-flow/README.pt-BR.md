# Git Flow

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../01-feature-branch-workflow/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../03-github-flow/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 40 min

**Pré-requisitos:** [CI/CD](../../ci-cd/README.pt-BR.md) · [Fluxo com feature branches](../01-feature-branch-workflow/README.pt-BR.md)

**Objetivo:** Explicar caminhos de release/hotfix e seus custos.

## O que é e por quê

Git Flow é convenção voltada a releases programadas. No modelo clássico, `main` mantém histórico lançado, `develop` acumula trabalho futuro, features saem e voltam à develop, branches de release preparam lançamento e hotfixes tratam correções urgentes da main. Release integra na main e mudanças retornam à develop; commit de release recebe tag. Hotfixes também precisam alcançar linha de desenvolvimento e release ativa relevante conforme política. Nomes e métodos exatos são convenções de equipe, não exigências Git. Pode apoiar versões mantidas em paralelo ou janelas controladas, mas refs duradouras ampliam custo de sincronização, conflitos e review.

```text
feature -> develop -> release preparation -> main/tag
hotfix from affected release -> corrected release + compatible propagation
```

## Prática

Desenhe release 2.0.0 do catálogo em estabilização enquanto develop contém trabalho 2.1. Bug crítico aparece na 1.9 lançada. Decida onde iniciar hotfix (revisão real 1.9 de produção ou linha mantida), teste, marque release corrigida e propague correção compatível às demais linhas relevantes. No modelo clássico com main na 1.9, desenhe hotfix -> main e hotfix -> develop; considere release ativa também.

## Riscos e recuperação

Não suponha main sempre igual à produção implantada; verifique identificador da release. Nunca sobrescreva tags publicadas nem integre features futuras não relacionadas em hotfix. Se backport gerar conflitos, resolva e reteste separadamente em cada linha mantida. Evite Git Flow quando branches extras geram custo sem necessidade de release.

## Exercício e autocorreção

Hotfix começa na revisão mantida afetada, não em develop arbitrária. Registre tag de release testada e caminhos de propagação compatíveis.

## Referência rápida

main / develop / feature / release / hotfix

## Fontes

- <https://nvie.com/posts/a-successful-git-branching-model/>
- <https://www.atlassian.com/git/tutorials/comparing-workflows>
- <https://git-scm.com/docs/gitworkflows>

---

<!-- navigation-footer -->
[Anterior](../01-feature-branch-workflow/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../03-github-flow/README.pt-BR.md)
<!-- /navigation-footer -->
