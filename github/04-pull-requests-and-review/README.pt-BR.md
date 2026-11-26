# Pull requests e code review

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../03-issues-and-planning/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../05-forks-and-open-source/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 45 min

**Pré-requisitos:** [Remotos](../../remote-repositories/README.pt-BR.md) · [Histórico e recuperação](../../history-and-recovery/README.pt-BR.md) · [Issues, labels, milestones e projects](../03-issues-and-planning/README.pt-BR.md)

**Objetivo:** Acompanhar mudança revisável da branch ao merge autorizado.

## O que é e por quê

Pull request (PR) propõe integração de head/origem em base/destino; abrir não integra histórico Git. Draft sinaliza trabalho não pronto para revisão final. Files changed mostra diff, Commits mostra commits, Checks mostra execuções automáticas. Revisão pode comentar, aprovar ou pedir mudanças; só comentário não aprova. Novos commits mudam head revisado e podem invalidar aprovação conforme política. Palavra-chave como Closes #1 na descrição pode fechar issue ao merge na branch padrão conforme regras GitHub. Merge commit preserva ambos pais, squash cria um commit combinado, rebase-and-merge reaplica commits sem merge commit; métodos dependem de configurações. CI verde não garante correção.

## Prática

Offline: desenhe issue -> feature branch -> commit -> push -> PR -> revisão/checks -> merge autorizado -> verificar base. Rascunhe descrição com resumo, escopo, testes realmente executados, limitações e link issue. Revisor fictício encontra instruções faltantes; revise patch e solicite revisão do novo head. Opcional: no sandbox privado próprio use edição web de branch/arquivo para criar feat/setup-note a partir de main, adicione pré-requisitos fictícios, commit só nessa branch, abra PR para main, inspecione diff e vínculo (substitua número real da issue). Exercício individual permite autoinspeção mas não conta como aprovação independente; se aprovação/checks exigidos não puderem ser atendidos, deixe PR aberto ou feche sem merge. Se políticas aplicáveis e autorização do owner estiverem satisfeitas, escolha método permitido, confira main e limpe só branch feature integrada. Nunca desative regras para concluir lab.

## Erros comuns e segurança

Confira origem/destino e head atual, não só ícones verdes. Não marque conversas resolvidas sem tratá-las. Se mudança integrada falhar, proponha commit corretivo revisado ou revert; não dê reset em main compartilhada. Trate feedback de IA como sugestões, não aprovação humana.

## Exercício e autocorreção

Surge novo commit após aprovação: o que fazer? Revise novo diff, reexecute checks aplicáveis e obtenha revisão exigida. Passe se distinguir base, head, checks, aprovação e merge.

## Referência rápida

- `base`
- `head`
- `review`
- `checks`
- `Closes #1`

## Fontes oficiais

- <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests>
- <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews>
- <https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue>
- <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/about-merge-methods-on-github>
