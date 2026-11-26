# Forks e contribuições open source

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../04-pull-requests-and-review/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../06-protection-and-rulesets/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 30 min

**Pré-requisitos:** [Remotos](../../remote-repositories/README.pt-BR.md) · [Histórico e recuperação](../../history-and-recovery/README.pt-BR.md) · [Pull requests e code review](../04-pull-requests-and-review/README.pt-BR.md)

**Objetivo:** Explicar contribuições por fork e manter upstream separado de origin.

## O que é e por quê

Fork GitHub é repositório hospedado associado a original; clone é cópia Git nativa. Fork não concede escrita no original. Clone local de fork normalmente usa origin para fork e upstream para original; convenções, não nomes reservados. Faça fetch upstream, inspecione divergência e atualize branch padrão local limpa apenas por fast-forward se possível. Contribua em branches separadas; push no fork e proponha PR de head do fork para base original. Siga licença, CONTRIBUTING, código de conduta e política de issues. Mantenedor pode recusar contribuição.

## Prática

Offline: desenhe repo original hospedado -> fork hospedado -> clone local; rotule upstream e origin da perspectiva local. Reuse modelo bare local do módulo 06 para raciocinar refs de rastreamento; simula transporte Git, não metadados fork GitHub. Opcional somente leitura: inspecione botão fork e instruções de contribuição em projeto público sem criar fork nem enviar PR de treino. Se quiser contribuição real depois, coordene antes com mantenedores. Confira URL upstream, branch, status e divergência antes de sincronizar. Não force sincronização se fast-forward recusado.

## Erros comuns e segurança

Não suponha que forks escondem conteúdo público ou obrigações da licença. Evite envios de treino não solicitados, issues duplicadas e patches confidenciais. Se destino errado, pare e corrija ou feche seu PR em vez de integrar.

## Exercício e autocorreção

Onde colaborador envia branch proposta se não tem escrita upstream? Fork autorizado próprio. Passe se setas e direção PR corretas e distinguir refs Git de forks hospedados.

## Referência rápida

- `origin`
- `upstream`
- `fork`
- `clone`

## Fontes oficiais

- <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks>
- <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork>
- <https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-open-source>

---

<!-- navigation-footer -->
[Anterior](../04-pull-requests-and-review/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../06-protection-and-rulesets/README.pt-BR.md)
<!-- /navigation-footer -->
