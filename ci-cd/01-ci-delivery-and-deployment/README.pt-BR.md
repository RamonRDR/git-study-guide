# Integração, entrega e implantação contínuas

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
— · [Índice](../README.pt-BR.md) · [Próximo](../02-yaml-fundamentals/README.pt-BR.md)
<!-- /navigation -->

**Nível:** iniciante · **Tempo estimado:** 30 min

**Pré-requisitos:** [GitHub](../../github/README.pt-BR.md) · [GitLab](../../gitlab/README.pt-BR.md)

**Objetivo:** Explicar as três práticas e escolher um limite seguro de promoção.

## O que é e por quê

Integração contínua (CI) significa integrar pequenas mudanças frequentemente e obter feedback automatizado rápido. Entrega contínua mantém revisão testada pronta para release; promoção à produção pode exigir decisão deliberada. Implantação contínua promove automaticamente à produção mudanças que satisfazem os gates configurados. CD pode significar entrega ou implantação; especifique qual. Build cria entregável, teste verifica comportamento e implantação altera ambiente em execução. CI aprovada não prova implantação nem segurança para todo usuário.

Fluxo acessível:

```text
change -> CI checks -> release candidate -> promotion -> production
              | failure: stop and correct
```

Na entrega, promoção pode ser manual; na implantação, é automática após gates. Decisão de liberar funcionalidade também pode ser separada da implantação (por exemplo, feature toggle).

## Prática

Offline: catálogo fictício tem três revisões. A falha testes; B passa mas aguarda aprovação; C é implantada após checks. Classifique cada e desenhe gate entre B e produção. Em equipe profissional, registre revisão exata, evidências, aprovação e plano de rollback antes de promover.

## Erros comuns e segurança

Não implante revisão falha ou desconhecida. Rollback pode exigir migrações de dados compatíveis; nunca prometa que Git revert restaura sistema ativo. Pare promoção e siga plano de incidente.

## Exercício e autocorreção

A está bloqueada; B ilustra prontidão de entrega; C ilustra implantação, automática só se política a promover automaticamente. Passe se explicar três conceitos sem confundir merge, release e implantação.

## Referência rápida

CI / delivery / deployment

## Fontes oficiais

- <https://docs.gitlab.com/ci/introduction/>
- <https://docs.github.com/en/actions/get-started/understand-github-actions>
