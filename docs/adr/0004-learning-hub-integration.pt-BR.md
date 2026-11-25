# ADR 0004: Integração Learning Hub

[English](0004-learning-hub-integration.md) · [Português](0004-learning-hub-integration.pt-BR.md) · [Español](0004-learning-hub-integration.es.md)

Fundação aprovada e integrada pelo PR #1 em 25/11/2026. Mudanças seguintes exigem revisão e aprovação explícita do mantenedor.

## Contexto

Guias futuros precisam de convenções comuns, mas capacidades distintas. Contrato Python é preliminar.

## Decisão

Usar manifestos preliminares compatíveis fixados por revisão, locale maps, IDs estáveis e namespace de guia no consumidor. Separar avaliação determinística de estado Git da execução Python; finalizar schemas após pilotos e revisão coordenada. Site responde por UI/runtime/progresso/acessibilidade.

## Alternativas

Rejeitar runtime único obrigatório, schema universal imposto unilateralmente, site dentro do guia e avaliação semântica por IA.

## Consequências

Consumidores validam schema/revisão, rejeitam versões major não suportadas e refs inseguras. Playground opcional: avaliar fidelidade, persistência, isolamento, acessibilidade, limites e custo zero antes de escolher tecnologia; sem execução arbitrária privilegiada.

## Documentos relacionados

- [Índice ADR](README.pt-BR.md)
- [Contrato de integração](../specs/project-foundation/integration-contract.pt-BR.md)
