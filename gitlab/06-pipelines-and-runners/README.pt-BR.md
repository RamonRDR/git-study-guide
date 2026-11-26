# Introdução a pipelines e runners

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../05-protected-branches-and-merge-checks/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../07-tags-and-releases/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 30 min

**Pré-requisitos:** [GitHub](../../github/README.pt-BR.md) · [Remotos](../../remote-repositories/README.pt-BR.md)

**Objetivo:** Explicar como automação hospedada executa e interpretar estado sem rodar pipeline.

## O que é e por quê

Pipeline coordena jobs automatizados para revisão e evento; job é unidade individual de trabalho. Runner é agente de execução que recebe jobs elegíveis, prepara ambiente, executa comandos e retorna resultados. GitLab normalmente lê `.gitlab-ci.yml` do projeto; configuração e evento determinam se existe pipeline. GitHub Actions usa workflows geralmente em `.github/workflows/`; ambos automatizam trabalho, mas sintaxe, eventos, permissões e modelos de runners diferem. Runner pode ter escopo de projeto, grupo ou instância, e ser hospedado ou autogerenciado conforme modalidade. Disponibilidade, permissões e tags do runner podem afetar agendamento. Runners hospedados no GitLab.com consomem cota conforme uso e tipo; não suponha computação gratuita ilimitada. YAML completo, artifacts, cache e deployment ficam para módulo 10.

## Prática

Desenhe revisão A → pipeline → job `validate` → runner → resultado do job. Cenário: A aprova; revisão B chega e seu job está pendente. Registre por que A não estabelece estado de B. Job falho exige inspeção de logs; pendente pode significar espera de runner elegível. Opcional: inspecione pipeline público existente e revisão somente leitura quando visível; não dispare, repita ou registre runners.

## Erros comuns e segurança

Não execute código não confiável com segredos ou runners privilegiados. Check ignorado, ausente ou pendente não evidencia execução aprovada. Inspecione revisão, evento, estado e logs; não contorne checks nem compre computação para prática.

## Exercício e autocorreção

Passe se distinguir pipeline, job e runner, identificar B como não validada e explicar por que problema de cota/agendamento não é teste aprovado.

## Fontes oficiais

- <https://docs.gitlab.com/runner/>
- <https://docs.gitlab.com/ci/runners/>
- <https://docs.gitlab.com/ci/pipelines/compute_minutes/>
- <https://docs.gitlab.com/ci/pipelines/settings/>

---

<!-- navigation-footer -->
[Anterior](../05-protected-branches-and-merge-checks/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../07-tags-and-releases/README.pt-BR.md)
<!-- /navigation-footer -->
