# Ambientes, variáveis e segredos

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../07-artifacts-and-cache/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../09-quality-gates-and-troubleshooting/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 40 min

**Pré-requisitos:** [GitHub](../../github/README.pt-BR.md) · [GitLab](../../gitlab/README.pt-BR.md) · [Artifacts e cache](../07-artifacts-and-cache/README.pt-BR.md)

**Objetivo:** Separar destinos de implantação, configuração não sensível e credenciais; aplicar menor privilégio.

## O que é e por quê

Ambiente é destino de implantação ou recurso de plataforma que o representa, como staging ou produção. Variável guarda configuração; segredo guarda material sensível e não deve ser commitado. No GitHub Actions, regras de proteção e secrets de ambiente podem restringir jobs de implantação, conforme plano, visibilidade e configuração. No GitLab, ambientes e variáveis CI/CD com escopo, mascaradas, ocultas ou protegidas têm significados e elegibilidade distintos. Mascaramento reduz exposição acidental em alguns logs; não protege contra código malicioso. Variável protegida tem escopo de refs protegidas elegíveis e condições de pipeline, não segurança universal. Token automático GitHub e job token GitLab também exigem menor privilégio. Prefira credenciais de curta duração e escopo restrito, jobs confiáveis aprovados e identidades separadas; nenhuma credencial real necessária.

## Prática

Offline desenhe dois destinos: `staging` e `production`. Classifique `APP_MODE=staging` como não sensível e `DEPLOY_CREDENTIAL` apenas como nome de credencial (não atribua valor). Monte tabela de acesso: checks de PR sem credenciais de implantação; implantação aprovada recebe acesso restrito ao destino. Classifique aprovação como manual ou imposta só após verificar plano/configuração reais.

## Erros comuns e segurança

Nunca imprima segredos, coloque-os em artifacts ou exponha a código não confiável. Em suspeita de vazamento, interrompa execuções afetadas, revogue/rotacione credenciais, avise mantenedores autorizados e investigue logs/escopo. Remover valor YAML ou mascará-lo não revoga credencial. Não crie ambientes ou segredos reais para prática.

## Exercício e autocorreção

Passe se checks de PR não alcançarem credenciais de implantação, promoção à produção tiver autorização separada e mascaramento não for confundido com isolamento.

## Referência rápida

environment / variable / secret

## Fontes oficiais

- <https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments>
- <https://docs.github.com/en/actions/reference/security/secure-use>
- <https://docs.gitlab.com/ci/variables/>
- <https://docs.gitlab.com/ci/environments/>
