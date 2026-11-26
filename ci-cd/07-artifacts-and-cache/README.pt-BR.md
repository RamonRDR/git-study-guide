# Artifacts e cache

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../06-jobs-steps-stages-and-dependencies/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../08-environments-variables-and-secrets/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 30 min

**Pré-requisitos:** [GitHub](../../github/README.pt-BR.md) · [GitLab](../../gitlab/README.pt-BR.md) · [Jobs, steps, stages e dependências](../06-jobs-steps-stages-and-dependencies/README.pt-BR.md)

**Objetivo:** Selecionar artifact ou cache conforme propósito, duração e confiança.

## O que é e por quê

Artifact é saída retida de job, como relatório ou pacote, associada à execução e política de retenção. Cache é otimização que pode reutilizar dados como dependências baixadas entre jobs ou execuções; pode faltar, expirar ou conter dados obsoletos. Não dependa de acerto de cache para correção. GitHub oferece actions de upload/download de artifacts e cache de dependências; GitLab usa configuração `artifacts` e `cache`. Jobs GitLab podem baixar artifacts de stages anteriores por padrão; `needs` ou `dependencies` muda seleção. Nas duas plataformas, permissões, retenção e limites variam. Chave de cache pode incorporar SO, versão de ferramenta e digest de lockfile; artifact de release deve estar associado à revisão exata revisada e ter integridade conferida.

## Prática

Offline: classifique relatório de teste, pacote final e dependências baixadas. Esboce chave como `linux-tool-v1-lockhash` (placeholder fictício) e manifest registrando revisão e checksum do pacote. Em pipeline profissional, valide funcionamento com cache vazio e se artifact baixado pertence à execução pretendida.

## Erros comuns e segurança

Nunca armazene credenciais em cache nem publique logs sensíveis. Trate saídas de jobs não confiáveis como entradas não confiáveis; não as execute em jobs privilegiados. Se cache corrompido, invalide conforme política e reconstrua com dependências verificadas. Se artifact faltar, reproduza da revisão revisada em vez de selecionar artifact não relacionado.

## Exercício e autocorreção

Relatório e pacote são artifacts; dependências baixadas são candidatas a cache. Passe se explicar cache miss, retenção, proveniência e confiança.

## Referência rápida

artifact / cache / retention

## Fontes oficiais

- <https://docs.github.com/en/actions/concepts/workflows-and-actions/workflow-artifacts>
- <https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching>
- <https://docs.gitlab.com/ci/jobs/job_artifacts/>
- <https://docs.gitlab.com/ci/caching/>

---

<!-- navigation-footer -->
[Anterior](../06-jobs-steps-stages-and-dependencies/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../08-environments-variables-and-secrets/README.pt-BR.md)
<!-- /navigation-footer -->
