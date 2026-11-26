# Branch protection, rulesets e quality gates

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../05-forks-and-open-source/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../07-tags-and-releases/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 40 min

**Pré-requisitos:** [Remotos](../../remote-repositories/README.pt-BR.md) · [Histórico e recuperação](../../history-and-recovery/README.pt-BR.md) · [Forks e contribuições open source](../05-forks-and-open-source/README.pt-BR.md)

**Objetivo:** Projetar política que proteja branches compartilhadas sem contornar revisão.

## O que é e por quê

Branch protection e rulesets são políticas servidor GitHub, não comandos Git. Rulesets miram refs e podem coexistir com branch protection. Exemplo para main: exigir PR, checks obrigatórios com nomes efetivamente observados, atualização estrita quando exigida, conversas resolvidas, histórico linear, bloqueio de force push e exclusão, bypass restrito e revisões obrigatórias adequadas quando há revisores independentes. Histórico linear sozinho permite squash ou rebase, não merge commit normal; escolha métodos e regras juntos. Quantidade de aprovações deve ser realista: autores não aprovam próprio PR. Repos públicos GitHub Free suportam branch rulesets; disponibilidade privada varia por plano e tipo de regra. Nunca pague para concluir curso. Check verde é evidência de commit específico, não garantia universal.

## Prática

Exercício offline de política: avalie quatro PRs fictícios. A: destino correto, head atual, checks passam, revisões atendidas, conversas resolvidas. B: igual mas check exigido falha. C: igual mas thread aberta. D: igual mas base avançou e atualização estrita exigida. Só A é elegível à autorização humana de merge; B corrija check, C trate feedback, D atualize com segurança e revalide. Opcional somente leitura: confira regras visíveis e caixa de merge em repo acessível. Nenhuma mudança admin exigida. Antes de propor regras reais, inventarie checks e métodos existentes, revise permissões, avalie impacto em sandbox e obtenha aprovação admin explícita; aula não executa mudança de configuração.

## Erros comuns e segurança

Não adicione check obrigatório nunca executado, confunda skipped/neutral com sucesso significativo de testes, contorne enforcement ou bloqueie mantenedores. Leia logs reais e revise head atual; se regra bloquear, diagnostique e solicite resolução aprovada em vez de desativar. Workflows e permissões de runners serão aprofundados no módulo 10.

## Exercício e autocorreção

Passe se só A elegível, explicar por que squash não contorna exigência de PR e citar limitação de revisor independente em projeto solo.

## Referência rápida

- `ruleset`
- `required checks`
- `linear history`
- `bypass`

## Fontes oficiais

- <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches>
- <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets>
- <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets>

---

<!-- navigation-footer -->
[Anterior](../05-forks-and-open-source/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../07-tags-and-releases/README.pt-BR.md)
<!-- /navigation-footer -->
