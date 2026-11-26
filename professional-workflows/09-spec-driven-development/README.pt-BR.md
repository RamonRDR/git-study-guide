# Desenvolvimento guiado por especificação (SDD)

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../08-code-review/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../10-test-driven-development/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 45 min

**Pré-requisitos:** [CI/CD](../../ci-cd/README.pt-BR.md) · [Code review e prontidão para merge](../08-code-review/README.pt-BR.md)

**Objetivo:** Rastrear requisitos a tarefas e evidências de aceitação.

## O que é e por quê

SDD usa especificação como base de planejamento, implementação e verificação. É família de práticas, não comando Git ou framework obrigatório único. Constituição estabelece princípios, especificação define requisitos observáveis e exclusões, plano descreve escolhas de implementação, tarefas dividem trabalho e critérios de aceitação definem evidências de sucesso. ADR (registro de decisão arquitetural) documenta contexto, decisão e consequências quando escolha importante exige justificativa. Rastreie requisitos a tarefas e testes. Use branch focada e revise specs quando requisitos evoluírem. Documentos do guia ilustram uma implementação; ferramentas externas e IA são opcionais.

[Especificação do projeto](../../docs/specs/project-foundation/specification.pt-BR.md) · [Critérios de aceitação](../../docs/specs/project-foundation/acceptance-criteria.pt-BR.md)

## Prática

Redija spec de uma página para catálogo fictício: R1 expõe linha exata `status: ready` quando pronto; R2 mantém estado draft anterior à integração; exclusão: sem implantação ou serviços externos. AC1 verifica linha ready, AC2 verifica ausência inicial e estado integrado limpo. Planeje mudança de um arquivo e check shell limitado; T1 escreve check, T2 implementa, T3 inspeciona diff e integra, T4 registra evidência de release. Mapeie R1->AC1/T1/T2 e R2->AC2/T1/T3; ligue T4 à política de release. Compare plano com capítulo 13.

## Riscos e recuperação

Não escreva critérios vagos como 'funciona bem', gere tarefas antes de esclarecer intenção ou marque teste não executado como aprovado. Resolva contradições na origem com mantenedor, atualize tarefas/testes e solicite review. Spec não substitui experimentos ou feedback.

## Exercício e autocorreção

Cada requisito tem ao menos check observável e cada tarefa um motivo. Exclusões explícitas evitam aumento de escopo. Revisão aceita exata e evidências pertencem à entrega.

## Referência rápida

constitution / spec / plan / task / AC / ADR

## Fontes

- <https://github.github.com/spec-kit/>

---

<!-- navigation-footer -->
[Anterior](../08-code-review/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../10-test-driven-development/README.pt-BR.md)
<!-- /navigation-footer -->
