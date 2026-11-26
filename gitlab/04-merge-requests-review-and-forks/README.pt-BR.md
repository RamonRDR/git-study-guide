# Merge requests, code review e forks

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../03-issues-labels-milestones-and-boards/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../05-protected-branches-and-merge-checks/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 45 min

**Pré-requisitos:** [GitHub](../../github/README.pt-BR.md) · [Remotos](../../remote-repositories/README.pt-BR.md)

**Objetivo:** Revisar mudança proposta e escolher colaboração no projeto ou por fork com segurança.

## O que é e por quê

Uma MR é proposta hospedada no GitLab para integrar branch de origem à de destino; GitHub chama recurso análogo de pull request (PR). Nenhum é objeto Git nativo. Uma MR registra descrição, diff, commits, discussões, reviewers, checks e estado de merge. Em projeto compartilhado, colaboradores enviam branches de funcionalidade onde permitido; para contribuição externa, fork é projeto hospedado separado, com permissões próprias e relação com upstream. Clone é cópia local, não fork. MR de fork pode mirar upstream, mas acesso, execução de pipeline e permissões de colaboração diferem. Revise projeto e branch de origem/destino reais, revisão exata, diff, evidência de testes e discussões abertas. Draft sinaliza trabalho não pronto para integração. Após correção, verifique a nova revisão antes de resolver discussão; aprovações não provam testes ou segurança. Método de merge altera histórico como ensinado no módulo 05.

## Prática

Simule offline issue #12 e MR !7: `docs/setup` → `main`. Diff proposto adiciona instruções mas omite pré-requisito. Escreva review pedindo esse pré-requisito e verificação testável; simule revisão corrigida e revise novamente. Para comparação Git real, use laboratório descartável de dois clones no [módulo 06](../../remote-repositories/README.pt-BR.md); inspecione `git status`, `git log --oneline main..HEAD` e `git diff main...HEAD` após verificar ref base local. Esses comandos não criam MR. Opcional: inspecione MR pública existente somente leitura; ou crie draft em sandbox privado próprio após conferir origem, destino e histórico. Nenhum merge ou contribuição externa exigidos.

## Erros comuns e segurança

Nunca execute pipeline de fork não confiável com credenciais privilegiadas; fork pode alterar configuração do pipeline. Verifique licença antes de reutilizar. Se destino ou diff estiver errado, pare, corrija proposta ou feche seu draft; não faça force-push de histórico compartilhado. Respeite política de contribuição.

## Exercício e autocorreção

Passe se distinguir clone, fork, branch e MR, nomear refs e projetos, explicar por que correção exige nova revisão e identificar pré-requisito ausente antes de recomendar merge.

## Fontes oficiais

- <https://docs.gitlab.com/user/project/merge_requests/>
- <https://docs.gitlab.com/user/project/merge_requests/reviews/>
- <https://docs.gitlab.com/user/project/merge_requests/authorization_for_merge_requests/>
- <https://docs.gitlab.com/user/project/repository/forking_workflow/>

---

<!-- navigation-footer -->
[Anterior](../03-issues-labels-milestones-and-boards/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../05-protected-branches-and-merge-checks/README.pt-BR.md)
<!-- /navigation-footer -->
