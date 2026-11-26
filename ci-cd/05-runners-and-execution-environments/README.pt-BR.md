# Runners e ambientes de execução

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../04-gitlab-ci-cd/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../06-jobs-steps-stages-and-dependencies/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 35 min

**Pré-requisitos:** [GitHub](../../github/README.pt-BR.md) · [GitLab](../../gitlab/README.pt-BR.md) · [Pipelines do GitLab CI/CD](../04-gitlab-ci-cd/README.pt-BR.md)

**Objetivo:** Escolher ambiente limitado e diagnosticar problemas de agendamento de runners.

## O que é e por quê

Runner é agente que executa jobs, não branch nem repositório. GitHub-hosted fornece ambientes gerenciados; self-hosted é controlado pelo operador. GitLab runners usam executores como shell ou Docker, e escopo/tags afetam elegibilidade. Executor shell compartilha host mais diretamente; contêiner não fornece automaticamente fronteira de segurança suficiente. Prefira runners descartáveis isolados com menor privilégio e sem acesso a redes internas sensíveis para mudanças não confiáveis. SO, shell, arquitetura, ferramentas, imagem e versão influenciam resultados. Matriz expande combinações, como Linux e Windows, em jobs separados. Jobs podem rodar em máquinas diferentes; não suponha arquivos ou processos compartilhados.

## Prática

Cenário offline: Linux passa, Windows falha por caminho específico de shell e terceiro job fica pendente por falta de runner elegível. Identifique correções distintas: caminhos portáveis ou shell explícito, e diagnóstico de agendamento/configuração. Leia [automação de qualidade](../../docs/quality-automation.pt-BR.md) do guia para exemplo real de dois SOs, sem alterá-lo.

## Erros comuns e segurança

Nunca registre runner em máquina pessoal ou da empresa para esta aula, execute Docker privilegiado ou exponha credenciais. Computação hospedada pode ter cotas e custos; nenhuma execução hospedada necessária. Verifique disponibilidade, labels/tags e limites; não contorne isolamento.

## Exercício e autocorreção

Passe se pendente não for interpretado como teste falho, falha Windows não for ignorada e nenhum runner compartilhado sensível for proposto.

## Referência rápida

runner / executor / matrix

## Fontes oficiais

- <https://docs.github.com/en/actions/concepts/runners/github-hosted-runners>
- <https://docs.gitlab.com/runner/executors/>
- <https://docs.gitlab.com/ci/runners/>
