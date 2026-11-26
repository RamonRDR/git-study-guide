# Exposição de credenciais e resposta a incidentes

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../10-software-supply-chain/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../12-governance-audit-and-traceability/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 45 min

**Pré-requisitos:** [Fluxos profissionais](../../professional-workflows/README.pt-BR.md) · [Segurança da cadeia de suprimentos de software](../10-software-supply-chain/README.pt-BR.md)

**Objetivo:** Priorizar contenção e remediação coordenada.

## O que é e por quê

Trate suspeita de credencial exposta como comprometida até avaliação. Primeiro contenha: revogue/rotacione no emissor prontamente, pare automação afetada e avise responsáveis autorizados privadamente. Preserve evidência segura (revisão, período, sistema, não segredo) e avalie escopo: histórico, clones, forks, caches, logs, artifacts e registros de acesso. Restaure serviço com substitutas restritas por canais aprovados. Excluir arquivo ou reverter commit não revoga credencial nem apaga histórico alcançável. Limpeza de histórico pode exigir reescrita coordenada, IDs alterados, perda de assinaturas, limpeza de colaboradores e suporte do host; não garante remoção de cópias. Siga procedimento autorizado antes de limpeza destrutiva.

[Política de segurança](../../docs/localized/SECURITY.pt-BR.md)

## Prática

Simulação de mesa: credencial fictícia de implantação aparece em commit público. Nenhum valor é fornecido. Ordene contenção, notificação, investigação, substituição, decisão de limpeza e lições. Redija relato privado com componente, placeholder de revisão, risco e mitigação; nunca detalhes sensíveis em issue pública. Consulte política de segurança do guia.

## Riscos e recuperação

Nunca teste se credencial exposta alheia funciona. Não cole em chat/scanner nem force-push histórico como primeira resposta. Se não houver canal privado verificado, estabeleça um sem divulgar detalhes publicamente.

## Exercício e autocorreção

Revogue/rotacione e contenha primeiro; investigue e coordene limpeza depois. Recuperação não garante desaparecimento de cópias.

## Referência rápida

revoke / rotate / contain / investigate

## Referências

- <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository>
- <https://csrc.nist.gov/pubs/sp/800/61/r3/final>
