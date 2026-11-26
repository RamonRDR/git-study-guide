# Escolha de estratégia de fluxo

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../04-trunk-based-development/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../06-conventional-commits/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 35 min

**Pré-requisitos:** [CI/CD](../../ci-cd/README.pt-BR.md) · [Desenvolvimento trunk-based](../04-trunk-based-development/README.pt-BR.md)

**Objetivo:** Escolher modelo com trade-offs concretos.

## O que é e por quê

Não há modelo universal. Compare duração de branches, frequência de integração, linhas de release mantidas, aprovação, confiabilidade de CI, latência de review e recuperação. Feature branching é técnica ampla; GitHub Flow adiciona convenção leve de review hospedado; trunk-based enfatiza integração frequente; Git Flow define linhas duradouras de release e desenvolvimento. Categorias se sobrepõem. Equipe pode combinar trunk protegida, features curtas e branches de manutenção. Mais branches não dão governança automaticamente; controles explícitos e evidências importam.

## Prática

Compare três equipes fictícias: guia documental com uma main, PR e dois checks; produto desktop mantendo duas releases antigas; catálogo online com mudanças diárias seguras e CI rápido. Escreva registro de decisão com contexto, modelo escolhido, alternativa rejeitada, método de merge, política de release e gatilhos de review. Avalie restrições reais, não popularidade.

## Riscos e recuperação

Não mude modelo de produção sem plano de migração, revisão de permissões, acordo da equipe e mapeamento de releases verificado. Evite afirmar que modelo elimina conflitos. Revise decisão quando restrições mudarem.

## Exercício e autocorreção

Escolhas razoáveis: feature/GitHub Flow protegido para documentação; trunk com manutenção ou Git Flow se coordenação justificar no desktop; trunk-based protegido para catálogo online. Alternativas são válidas se justificadas pelas restrições.

## Referência rápida

branch lifetime / CI / release cadence / support

## Fontes

- <https://www.atlassian.com/git/tutorials/comparing-workflows>
- <https://dora.dev/capabilities/trunk-based-development/>
- <https://nvie.com/posts/a-successful-git-branching-model/>

---

<!-- navigation-footer -->
[Anterior](../04-trunk-based-development/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../06-conventional-commits/README.pt-BR.md)
<!-- /navigation-footer -->
