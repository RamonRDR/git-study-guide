# Projetos, grupos e modalidades do GitLab

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
— · [Índice](../README.pt-BR.md) · [Próximo](../02-visibility-permissions-and-authentication/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 30 min

**Pré-requisitos:** [GitHub](../../github/README.pt-BR.md) · [Remotos](../../remote-repositories/README.pt-BR.md)

**Objetivo:** Distinguir dados Git de serviços GitLab e escolher namespace e modalidade adequados.

## O que é e por quê

Git armazena commits, árvores, branches e tags. O GitLab adiciona um projeto ao redor do repositório: issues, merge requests (MRs), controle de acesso, pipelines e releases. Um clone contém dados Git, não todo o banco de dados do projeto. Um namespace identifica onde o projeto reside. Um grupo pode conter projetos e subgrupos; membros e configurações podem ser herdados pela hierarquia. Por exemplo, `studio/tools/catalog` pode representar o grupo `studio`, subgrupo `tools` e projeto `catalog`. Um namespace pessoal não é um grupo compartilhado. GitLab.com é um serviço hospedado multi-tenant; Self-Managed é instalado e administrado pela organização, que assume custos de infraestrutura e manutenção; Dedicated é hospedagem gerenciada single-tenant. Modalidade e plano (Free, Premium, Ultimate) são decisões distintas. Recursos também dependem da versão, configurações e permissões.

## Prática

No papel, desenhe um grupo para um estúdio fictício, com subgrupo `tools` e dois projetos. Desenhe clone local → repositório Git → projeto GitLab → grupo; classifique commit, issue, tag e MR. Opcionalmente inspecione um projeto público no navegador sem login ou publicação. Para uma equipe que precisa centralizar membros, prefira grupo a distribuir a propriedade em namespaces pessoais.

## Erros comuns e segurança

Não transfira nem renomeie projetos reais como exercício: caminhos, integrações e acesso herdado podem mudar. Self-Managed não é automaticamente gratuito. Consulte versão e plano antes de prometer recursos; nenhuma instalação é necessária.

## Exercício e autocorreção

Um clone recupera todas as issues e membros do grupo? Não. Passe se distinguir objetos Git de metadados hospedados, acertar a hierarquia e identificar quem administra a modalidade escolhida.

## Fontes oficiais

- <https://docs.gitlab.com/user/namespace/>
- <https://docs.gitlab.com/user/group/>
- <https://docs.gitlab.com/subscriptions/choosing_subscription/>
