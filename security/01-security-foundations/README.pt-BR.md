# Fundamentos de segurança no Git

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
— · [Índice](../README.pt-BR.md) · [Próximo](../02-ssh-authentication/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 30 min

**Pré-requisitos:** [Fluxos profissionais](../../professional-workflows/README.pt-BR.md)

**Objetivo:** Distinguir camadas de segurança e fronteiras de confiança.

## O que é e por quê

Segurança protege confidencialidade (quem lê), integridade (o que é autêntico e inalterado) e disponibilidade (serviço utilizável). Autenticação identifica ator; autorização determina ações permitidas. Git registra conteúdo e histórico, não é sistema completo de controle de acesso. Hash identifica objeto, não identidade ou confiabilidade do autor. Permissões locais, políticas de hospedagem e CI são camadas distintas. Repositório público pode ser lido por todos sem permitir escrita. Cópias, clones e forks podem sobreviver à exclusão.

## Prática

Para catálogo fictício de biblioteca, classifique documentação pública, registros privados de funcionários e permissão de merge. Desenhe limites entre estação, host e runner. Para cada, identifique ativo, ameaça e controle. Usuário somente leitura pode ler docs públicas, não alterar main.

## Riscos e recuperação

Não suponha repo privado como cofre, hash como assinatura ou visibilidade pública como escrita. Se limite incerto, pare e confira permissões reais com administrador autorizado.

## Exercício e autocorreção

Docs públicas são legíveis; registros privados ficam fora do exercício; merge é decisão de autorização. Explique três propriedades de segurança.

## Referência rápida

confidentiality / integrity / availability / authentication / authorization

## Referências

- <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github>
- <https://git-scm.com/docs/git>
