# Code review e prontidão para merge

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../07-semantic-versioning/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../09-spec-driven-development/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 40 min

**Pré-requisitos:** [CI/CD](../../ci-cd/README.pt-BR.md) · [Versionamento semântico](../07-semantic-versioning/README.pt-BR.md)

**Objetivo:** Revisar intenção, comportamento, risco e evidência da revisão exata.

## O que é e por quê

Code review avalia proposta contra intenção, comportamento, manutenção, segurança e testes. Apontamento útil informa local, problema observado, impacto e direção sugerida; distinga defeitos bloqueantes de sugestões. Revise diff focado, não só ícone verde. Compare head à base e verifique logs reais e escopo dos testes. GitHub/GitLab oferecem discussões e aprovações; imposição, descarte de aprovações obsoletas e revisores obrigatórios dependem da configuração. Autor trata apontamentos e registra evidências; revisor verifica correção antes de encerrar discussões relevantes. Autorização de merge é distinta de review automatizado bem-sucedido.

## Prática

PR diz adicionar prontidão, mas muda `catalog.txt` de `status: draft` para `status: redy`. Teste só verifica existência. Escreva comentário bloqueante pedindo campo exato e testes falho/aprovado significativos; sugestão de nome opcional separada. Autor corrige valor e teste. Registre nova revisão, CI nos ambientes esperados, resolução e aprovação humana; use capítulo 13 para prática local de diff.

## Riscos e recuperação

Não aprove por cortesia, título, saída de IA ou SHA anterior. Nunca silencie falhas ou resolva conversa só para liberar merge. Se regressão escapar, registre PR corretivo, reexecute checks e melhore cobertura sem culpar pessoas.

## Exercício e autocorreção

Bloqueie merge: comportamento diverge do requisito e check não detecta. Reteste revisão corrigida exata; autorização humana independente ainda necessária pela política do guia.

## Referência rápida

diff / head SHA / review / approval / CI

## Fontes

- <https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/reviewing-proposed-changes-in-a-pull-request>
- <https://docs.gitlab.com/user/project/merge_requests/reviews/>

---

<!-- navigation-footer -->
[Anterior](../07-semantic-versioning/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../09-spec-driven-development/README.pt-BR.md)
<!-- /navigation-footer -->
