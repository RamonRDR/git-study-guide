# Governança, auditoria e rastreabilidade

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../11-credential-exposure-and-incident-response/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../13-integrated-security-lab/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 40 min

**Pré-requisitos:** [Fluxos profissionais](../../professional-workflows/README.pt-BR.md) · [Exposição de credenciais e resposta a incidentes](../11-credential-exposure-and-incident-response/README.pt-BR.md)

**Objetivo:** Registrar aprovação e evidência auditável.

## O que é e por quê

Governança define quem decide, executa e revisa; evidências registram o ocorrido. Histórico de commits é útil mas não captura toda ação administrativa/hospedagem. Logs de auditoria, PR/MR, CI, metadados de artifacts e aprovação complementam, sujeitos a acesso e retenção. Registre head/base, revisão merge testada, resultados/limites, apontamentos, autorização, commit/tree integrados, limpeza de branch e checks pós-merge. Separe desenho de política, imposição efetiva e resultados observados. Não invente evidências nem preserve informações privadas em notas públicas.

[Registro de tarefas](../../docs/specs/project-foundation/tasks.pt-BR.md)

## Prática

Crie registro fictício: requisito, PR, placeholder SHA revisado, status Linux/Windows, apontamentos pendentes, decisão humana, comparação de tree e risco residual. Se Windows pendente, marque gate pendente, não aprovado. Compare políticas de contribuição e tarefas do guia.

## Riscos e recuperação

Não confunda pedido de review com aprovação, ou disponibilidade de log com completude. Restrinja evidência sensível a retenção/canais autorizados. Nunca altere regras ou integre por aprovação presumida; registre lacunas e escale.

## Exercício e autocorreção

Windows pendente bloqueia gate; autorização e resultados observados referem-se à revisão exata. Registre limitações honestamente.

## Referência rápida

revision / evidence / decision / residual risk

## Referências

- <https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/reviewing-the-audit-log-for-your-organization>
- <https://docs.gitlab.com/user/compliance/audit_events/>
