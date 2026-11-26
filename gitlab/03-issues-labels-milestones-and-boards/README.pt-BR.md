# Issues, labels, milestones e boards

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../02-visibility-permissions-and-authentication/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../04-merge-requests-review-and-forks/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 25 min

**Pré-requisitos:** [GitHub](../../github/README.pt-BR.md) · [Remotos](../../remote-repositories/README.pt-BR.md)

**Objetivo:** Transformar um problema em trabalho rastreável com critérios de aceitação e visibilidade.

## O que é e por quê

Uma issue registra problema ou tarefa, não um commit Git. Label categoriza trabalho, milestone agrupa trabalho rumo a uma meta e board exibe trabalho em listas. Um board pode usar labels ou outros filtros; arrastar cartão pode alterar metadados conforme configuração. Projetos e grupos podem compartilhar contexto de planejamento; tipos de work items e boards avançados variam por plano e versão. Assignee assume execução; reviewer verifica a mudança proposta. Vincule MR à issue para preservar rastreabilidade. Palavra de fechamento como `Closes #12` pode fechar a issue referenciada quando a MR relevante é integrada à branch padrão conforme configurações aplicáveis. Não use para trabalho não relacionado.

## Prática

No papel crie issue #12: catálogo fictício sem instruções de instalação. Defina resultado esperado (iniciante localiza instruções), label `documentation`, milestone `v1`, responsável e reviewer. Mova cartão por Open, In progress e Closed, registrando evidência que justifica fechamento. Opcional: reproduza somente em projeto privado descartável próprio; inspecione board antes e depois, feche apenas sua issue se desejar.

## Erros comuns e segurança

Não publique dados reais de clientes, logs internos ou segredos. Issue fechada ou cartão movido não prova funcionamento do código. Reabra issue fechada incorretamente e registre motivo; evite alterar milestones alheios.

## Exercício e autocorreção

Passe se a issue tiver resultado mensurável, label e milestone tiverem propósitos distintos e fechamento depender de evidência verificada, não do movimento do cartão.

## Fontes oficiais

- <https://docs.gitlab.com/user/work_items/>
- <https://docs.gitlab.com/user/project/labels/>
- <https://docs.gitlab.com/user/project/milestones/>
- <https://docs.gitlab.com/user/project/issue_board/>

---

<!-- navigation-footer -->
[Anterior](../02-visibility-permissions-and-authentication/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../04-merge-requests-review-and-forks/README.pt-BR.md)
<!-- /navigation-footer -->
