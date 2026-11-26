# Pipelines do GitLab CI/CD

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../03-github-actions/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../05-runners-and-execution-environments/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 45 min

**Pré-requisitos:** [GitHub](../../github/README.pt-BR.md) · [GitLab](../../gitlab/README.pt-BR.md) · [Workflows do GitHub Actions](../03-github-actions/README.pt-BR.md)

**Objetivo:** Ler pipeline GitLab e mapear conceitos ao GitHub Actions sem confundir sintaxes.

## O que é e por quê

GitLab normalmente lê `.gitlab-ci.yml` na raiz. `workflow: rules` determina criação do pipeline; `rules` de job pode decidir inclusão individual. Stages ordenam grupos de jobs por padrão; job tem `script` de comandos. Executor do runner define ambiente real. `image` é usada por executores de contêiner suportados, não todos. Exemplo exige runner Linux isolado compatível com contêiner, Alpine e ferramentas shell BusyBox. GitLab normalmente faz checkout da revisão antes do script. Exemplo usa tag de versão legível deliberadamente; tags de imagem são mutáveis, então política de produção deve verificar e fixar digest confiável. Jobs GitLab recebem credenciais automáticas de job mesmo sem segredos definidos pelo usuário; restrinja acesso do job token e escopo de runner conforme aplicável.

```yaml
workflow:
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
    - if: '$CI_PIPELINE_SOURCE == "push" && $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH'
stages:
  - test
quality:
  stage: test
  image: alpine:3.22
  timeout: 5m
  script:
    - test -s catalog.txt
    - grep -Fxq 'status: ready' catalog.txt
```

## Prática

Offline, rastreie evento MR, push na branch padrão e push em outra branch sem MR. Configuração cria pipelines nos dois primeiros, não no terceiro. Compare checks com capítulo 03 e faça mesmo laboratório offline do capítulo 10. Opcional: CI Lint pode validar configuração em projeto descartável autorizado sem executar jobs; confira permissões e cota gratuita disponível antes de operação hospedada. Não exige registro de runner nem uso pago.

## Erros comuns e segurança

Não execute pipelines de MR de fork em projeto pai privilegiado com segredos ou recursos protegidos. Revise mudanças em `.gitlab-ci.yml`, includes e acesso de token. Se pipeline não aparecer, inspecione origem, workflow rules e validade antes de mudar acesso ou repetir.

## Exercício e autocorreção

Passe se distinguir workflow rules, stages, jobs, scripts e executor do runner; explique credenciais automáticas e por que YAML não é intercambiável.

## Referência rápida

`workflow` / `rules` / `stages` / `script`

## Fontes oficiais

- <https://docs.gitlab.com/ci/yaml/>
- <https://docs.gitlab.com/ci/yaml/lint/>
- <https://docs.gitlab.com/ci/pipelines/merge_request_pipelines/>
- <https://docs.gitlab.com/ci/jobs/ci_job_token/>
