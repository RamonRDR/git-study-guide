# Quality gates e diagnóstico

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../08-environments-variables-and-secrets/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../10-integrated-quality-pipeline-lab/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 35 min

**Pré-requisitos:** [GitHub](../../github/README.pt-BR.md) · [GitLab](../../gitlab/README.pt-BR.md) · [Ambientes, variáveis e segredos](../08-environments-variables-and-secrets/README.pt-BR.md)

**Objetivo:** Decidir se revisão pode ser integrada com base em evidências, não apenas ícone verde.

## O que é e por quê

Quality gate é condição de política que deve ser satisfeita antes de integração ou promoção. Exemplos: lint obrigatório (verificações estáticas), testes, review, checks de segurança e aprovação autorizada. Rulesets GitHub podem exigir checks nomeados; merge checks GitLab podem exigir pipeline aprovado e discussões resolvidas quando configurados. Capacidades variam por plano e configuração. Workflow pode estar ausente, em fila, pendente, executando, falho, cancelado, ignorado ou aprovado. Políticas podem tratar alguns resultados skipped/neutral como satisfatórios, mas não provam execução de testes. Distinga erro de configuração, falha de infraestrutura e assertiva falha. Verifique head/base ou resultado de merge exato, logs, nomes de jobs exigidos e política; não infira de execução anterior. Timeout não é aprovação.

## Prática

Offline: revisão A passou; B muda configuração de validação; B Linux passa mas Windows falha. Escreva checklist pré-merge: revisão exata, jobs esperados, logs, apontamentos, resolução de discussões, base atual e autorização. Decida não integrar B, inspecione falha Windows, corrija, revise nova revisão e reexecute ambos jobs. Opcional: inspecione logs públicos CI somente leitura sem conta quando disponível.

## Erros comuns e segurança

Não desative gates, suprima falhas ou repita indefinidamente para ocultar não determinismo. Oculte diagnósticos sensíveis; reporte limites de reprodução e escale problemas de infraestrutura. Corrija causa raiz e preserve evidências.

## Exercício e autocorreção

B está bloqueada; A não evidencia B. Passe se checklist incluir ambas plataformas, revisão exata, resultados significativos e autorização humana.

## Referência rápida

required check / revision / log

## Fontes oficiais

- <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets>
- <https://docs.gitlab.com/user/project/merge_requests/auto_merge/>
- <https://docs.gitlab.com/ci/pipelines/>

---

<!-- navigation-footer -->
[Anterior](../08-environments-variables-and-secrets/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../10-integrated-quality-pipeline-lab/README.pt-BR.md)
<!-- /navigation-footer -->
