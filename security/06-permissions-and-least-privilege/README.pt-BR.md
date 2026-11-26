# Permissões e menor privilégio

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../05-secrets-and-disclosure-prevention/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../07-branch-protection-and-rulesets/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 40 min

**Pré-requisitos:** [Fluxos profissionais](../../professional-workflows/README.pt-BR.md) · [Secrets e prevenção de vazamentos](../05-secrets-and-disclosure-prevention/README.pt-BR.md)

**Objetivo:** Projetar matriz de menor privilégio.

## O que é e por quê

Menor privilégio concede só recursos e ações necessários pela duração necessária. Distinga papéis do repo, permissões de branch, API e identidades CI. Papéis GitHub e GitLab são específicos, não equivalentes por nome; plano, instância e herança afetam acesso efetivo. Job build somente leitura não recebe credenciais de implantação; identidade release não pode ser usada por PR não confiável. Separe funções quando possível, revise acessos obsoletos e documente exceções. Login bem-sucedido ou clone público não autoriza mutação.

## Prática

Monte matriz para leitor, contribuidor, revisor, mantenedor, check CI e identidade de implantação fictícios. Marque ler, propor, aprovar, integrar ou implantar só se necessário. Registre responsável e data de revisão. Explique por que identidade automação com escrita ampla é excessiva para lint.

## Riscos e recuperação

Nunca resolva erro de permissão tornando todos administradores ou permitindo execução privilegiada não confiável. Inspecione política efetiva e solicite menor ajuste autorizado; revogue concessões obsoletas.

## Exercício e autocorreção

Leitor lê, contribuidor propõe, review/merge/deploy seguem políticas separadas; CI leitura salvo job justificado separadamente.

## Referência rápida

role / resource / action / duration

## Referências

- <https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/repository-roles-for-an-organization>
- <https://docs.gitlab.com/user/permissions/>
- <https://docs.github.com/en/actions/reference/security/secure-use>
