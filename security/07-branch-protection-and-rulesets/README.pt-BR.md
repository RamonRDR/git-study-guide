# Proteção de branches e rulesets

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../06-permissions-and-least-privilege/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../08-codeowners-and-responsibilities/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 40 min

**Pré-requisitos:** [Fluxos profissionais](../../professional-workflows/README.pt-BR.md) · [Permissões e menor privilégio](../06-permissions-and-least-privilege/README.pt-BR.md)

**Objetivo:** Distinguir regras impostas de branch e política de equipe.

## O que é e por quê

Branches Git são refs; hospedagem adiciona regras de servidor. Proteção e rulesets GitHub podem restringir push, exclusão, force-push, métodos de merge, checks e reviews; regras aplicáveis podem combinar. Branches protegidas e merge checks GitLab governam push/merge e condições de pipeline. Recursos variam por plano, visibilidade e configuração. Distinga checks impostos de política escrita: autorização humana pode existir sem requisito numérico de approvals. Confira destino, modo, atores/bypass, nomes de checks e comportamento de review obsoleto. Histórico linear não garante toda mudança revisada.

## Prática

Offline: desenhe regras para catálogo público: PR obrigatório, checks Ubuntu/Windows, sem bypass, push direto, force-push ou exclusão main, só squash, discussões resolvidas e autorização humana separada. Com SHA anterior verde e novo não testado, decida merge. Inspecione configurações públicas somente leitura se disponíveis; nunca altere settings do guia.

## Riscos e recuperação

Nunca remova proteção ou adicione bypass só para liberar CI. Diagnostique checks falhos/pendentes; corrija mudança focada e revalide. Mudanças administrativas exigem autorização separada.

## Exercício e autocorreção

SHA novo não tem evidência válida. Preserve proteções e obtenha validação nova e autorização explícita.

## Referência rápida

protected branch / ruleset / required checks / bypass

## Referências

- <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets>
- <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches>
- <https://docs.gitlab.com/user/project/repository/branches/protected/>

---

<!-- navigation-footer -->
[Anterior](../06-permissions-and-least-privilege/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../08-codeowners-and-responsibilities/README.pt-BR.md)
<!-- /navigation-footer -->
