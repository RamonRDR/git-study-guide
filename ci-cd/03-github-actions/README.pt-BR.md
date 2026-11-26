# Workflows do GitHub Actions

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../02-yaml-fundamentals/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../04-gitlab-ci-cd/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 45 min

**Pré-requisitos:** [GitHub](../../github/README.pt-BR.md) · [GitLab](../../gitlab/README.pt-BR.md) · [YAML e leitura de configuração](../02-yaml-fundamentals/README.pt-BR.md)

**Objetivo:** Explicar eventos, workflow, jobs, steps e permissões mínimas usando exemplo para inspeção.

## O que é e por quê

GitHub descobre arquivos de workflow em `.github/workflows/`. Evento seleciona execução; job roda em runner e steps executam em sequência. `uses` invoca action; `run` invoca comando shell. Em pull_request, checkout padrão normalmente testa ref de merge gerada; em push, revisão enviada. Inspecione checkout e evento reais. `permissions: contents: read` minimiza concessão do token padrão; desabilitar persistência de credenciais de checkout reduz exposição posterior. Fixe actions de terceiros e próprias em SHAs completos verificados, revise atualizações e não trate pinagem como garantia de segurança.

Exemplo abaixo é configuração didática completa para catálogo fictício; SHA de checkout vem do workflow revisado do guia, não versão inventada. Verifique revisão da action antes de reutilizar. Não usa implantação nem segredos do usuário.

```yaml
name: Sandbox quality
on:
  pull_request:
    branches: [main]
  push:
    branches: [main]
permissions:
  contents: read
jobs:
  quality:
    runs-on: ubuntu-latest
    timeout-minutes: 5
    steps:
      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1
        with:
          persist-credentials: false
      - name: Check catalog
        shell: bash
        run: |
          test -s catalog.txt
          grep -Fxq 'status: ready' catalog.txt
```

## Prática

Leia YAML sem instalar. No laboratório offline do capítulo 10, execute duas verificações contra seu arquivo de catálogo temporário. Preveja sucesso com linha ready exata e falha em arquivo vazio ou incorreto. Uso hospedado opcional: só em sandbox descartável próprio após revisar código, disponibilidade de runner, cotas e permissões; não use guia nem habilite uso pago. Nenhuma execução hospedada é necessária.

## Erros comuns e segurança

Nunca execute código de PR não confiável em workflow `pull_request_target` privilegiado. Não interpole texto não confiável de evento em scripts shell. Step falho exige inspecionar logs; corrija fonte e reexecute checks na nova revisão, não execução aprovada não relacionada.

## Exercício e autocorreção

Passe se nomear os dois eventos, identificar runner/job/steps, explicar permissões do token e prever resultados.

## Referência rápida

`on` / `jobs` / `steps` / `permissions`

## Fontes oficiais

- <https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax>
- <https://docs.github.com/en/actions/reference/security/secure-use>
- <https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows>
