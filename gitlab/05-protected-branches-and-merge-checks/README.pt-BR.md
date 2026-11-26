# Branches protegidas, aprovações e verificações de merge

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../04-merge-requests-review-and-forks/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../06-pipelines-and-runners/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 35 min

**Pré-requisitos:** [GitHub](../../github/README.pt-BR.md) · [Remotos](../../remote-repositories/README.pt-BR.md)

**Objetivo:** Desenhar política de proteção da branch padrão e distinguir gates obrigatórios de convenções.

## O que é e por quê

Branches protegidas do GitLab usam regras para restringir operações em refs selecionadas. `Allowed to merge` controla integração via MR; `Allowed to push and merge` também concede push direto. Para exigir MRs, selecione explicitamente No one para push and merge e conceda merge só a papéis adequados; regra sem configuração não equivale a negação explícita. Inspecione regras sobrepostas com wildcard e herdadas; acesso efetivo pode ser mais permissivo que regra isolada sugere. Desative force push salvo justificativa explícita. Merge checks podem exigir pipelines bem-sucedidos e discussões resolvidas quando configurados. GitLab Free oferece proteção básica e aprovações voluntárias, mas regras de aprovação obrigatória e enforcement de aprovação por Code Owner dependem de Premium/Ultimate e configurações aplicáveis. Não apresente checklist informal como regra tecnicamente imposta. Branch rules e rulesets do GitHub têm intenção análoga, não equivalência recurso a recurso. Check aprovado evidencia uma revisão, não correção universal.

## Prática

Offline desenhe política: developers enviam branches de funcionalidade, nenhum push direto na `main`, mantenedores integram só após review, pipeline obrigatório aprovado e discussões resolvidas. Marque cada controle como imposto, manual ou indisponível até verificar plano real. No cenário mantenedor encontra pipeline falho e discussão aberta: recuse merge e peça correção. Opcional: inspecione regras em sandbox privado próprio sem modificá-las; identifique plano/versão e configurações reais.

## Erros comuns e segurança

Nunca enfraqueça proteção para passar merge. Se merge bloqueado, leia check exato, resolva causa, reexecute checks na nova revisão e busque autorização. Não suponha que aprovação ou pipeline não relacionado aprovado substitui gates obrigatórios.

## Exercício e autocorreção

Maintainer em Allowed to push and merge impede push direto? Não. Passe se negar push explicitamente e distinguir aprovação obrigatória de revisão voluntária.

## Fontes oficiais

- <https://docs.gitlab.com/user/project/repository/branches/protected/>
- <https://docs.gitlab.com/user/project/repository/branches/branch_rules/>
- <https://docs.gitlab.com/user/project/merge_requests/approvals/>
- <https://docs.gitlab.com/user/project/merge_requests/approvals/rules/>
- <https://docs.gitlab.com/user/project/merge_requests/auto_merge/>

---

<!-- navigation-footer -->
[Anterior](../04-merge-requests-review-and-forks/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../06-pipelines-and-runners/README.pt-BR.md)
<!-- /navigation-footer -->
