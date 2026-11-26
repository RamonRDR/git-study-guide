# Desenvolvimento trunk-based

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../03-github-flow/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../05-workflow-trade-offs/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 40 min

**Pré-requisitos:** [CI/CD](../../ci-cd/README.pt-BR.md) · [GitHub Flow](../03-github-flow/README.pt-BR.md)

**Objetivo:** Planejar integração frequente segura.

## O que é e por quê

Trunk é linha compartilhada de integração, frequentemente main. Trunk-based integra pequenos lotes frequentemente, muitas vezes diariamente ou mais, com branches muito curtas ou integração direta onde política permite. Não exige push direto sem review. Feedback automatizado, testes confiáveis, mudanças pequenas e revisão rápida mantêm trunk saudável. Feature flag separa integração de código incompleto mas seguro da exposição a usuários; precisa de padrão, responsável e plano de remoção. Flag não é mecanismo de autorização. Branch-by-abstraction introduz interface estável para coexistência de comportamento antigo e novo durante transição. Nenhuma técnica justifica integrar trabalho quebrado.

```text
small change -> fast review + CI -> trunk -> next small change
```

## Prática

Nova busca do catálogo leva cinco dias. Divida em interface compatível, implementação oculta, testes, decisão de ativação e remoção de flag. Cada mudança é pequena, revisada e passa CI; busca antiga continua usável até ativação. Identifique etapas que alteram histórico Git e as que mudam configuração de execução. Desenhe branch curta voltando à trunk diariamente.

## Riscos e recuperação

Não use flags para esconder comportamento inseguro ou não testado. Se trunk falhar, pare integração/promoção e priorize restaurá-la com fix ou revert autorizado. Push direto à main não é permitido neste guia. Merge frequente não significa necessariamente implantação frequente.

## Exercício e autocorreção

Prefira incrementos pequenos e seguros, reviews curtos e estados de flag testáveis. Integração à trunk e ativação são decisões distintas.

## Referência rápida

trunk / short-lived branch / feature flag

## Fontes

- <https://dora.dev/capabilities/trunk-based-development/>
- <https://git-scm.com/docs/gitworkflows>
- <https://www.atlassian.com/git/tutorials/comparing-workflows>

---

<!-- navigation-footer -->
[Anterior](../03-github-flow/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../05-workflow-trade-offs/README.pt-BR.md)
<!-- /navigation-footer -->
