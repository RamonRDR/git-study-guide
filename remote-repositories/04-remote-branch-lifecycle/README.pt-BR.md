# Ciclo de vida de branches remotas e prune

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../03-pull-push-and-divergence/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../05-secure-authentication/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 30 min

**Pré-requisitos:** [Pull, push e históricos divergentes](../03-pull-push-and-divergence/README.pt-BR.md)

**Objetivo:** Publicar, acompanhar, integrar e excluir uma branch remota descartável preservando trabalho.

## O que é e por quê

`git push -u origin BRANCH` publica e configura upstream se push for bem-sucedido ou já atualizado. `git switch --track origin/BRANCH` cria branch local acompanhando a ref remota de tracking. `git push --delete origin BRANCH` remove uma ref remota, não necessariamente os objetos; colegas podem manter refs obsoletas até fetch --prune. Prune usa o refspec de fetch e não remove branches locais comuns com o mapeamento padrão do clone. Refspecs não padrão podem remover outras refs, inclusive tags; inspecione a configuração.

## Prática

Continue o capítulo 03 com clones limpos e sincronizados no pai registrado. Repita verificações do capítulo 02 para cada ator antes das mudanças. Após trocar Alice para feat/summary, crie alice/summary.txt com `summary ready` e quebra final; inspecione diff staged e ambas as identidades antes do commit. Execute em ordem, pausando no switch para criar o arquivo.
```text
git -C alice switch -c feat/summary
git -C alice add -- summary.txt
git -C alice diff --cached
git -C alice commit -m "docs: add summary"
git -C alice push -u origin feat/summary
git -C alice branch -vv
git -C bob fetch origin
git -C bob switch --track origin/feat/summary
git -C bob branch -vv
git -C bob switch main
git -C alice switch main
git -C alice merge --ff-only feat/summary
git -C alice push origin main
git -C bob pull --ff-only origin main
```
Esperado: branch local de Bob acompanha origin/feat/summary; main contém o commit summary nos dois clones. Para exclusão, primeiro confirme concordância de todos os colegas (Alice e Bob neste lab), ausência de trabalho adicional na feature e que feature remota é ancestral da main remota. Execute separadamente os três primeiros comandos de inspeção abaixo; ancestralidade deve retornar 0 e ambas as refs retornadas por ls-remote devem coincidir com as refs obtidas. Só então exclua feat/summary, nunca main. Nenhum ator concorrente pode alterar refs durante o exercício; em equipes reais reconfira e use proteção da plataforma e fluxo acordado.
```text
git -C alice fetch origin
git -C alice merge-base --is-ancestor origin/feat/summary origin/main
git -C alice ls-remote --heads origin refs/heads/main refs/heads/feat/summary
git -C alice rev-parse origin/main origin/feat/summary
git -C alice push --delete origin feat/summary
git -C bob ls-remote --heads origin refs/heads/feat/summary
git -C bob branch -r
git -C bob fetch --prune origin
git -C bob branch -r
git -C bob branch -vv
git -C bob branch -d feat/summary
git -C alice branch -d feat/summary
git -C alice rev-parse main
git -C bob rev-parse main
git -C origin.git rev-parse refs/heads/main
git -C bob show HEAD:summary.txt
git -C bob status --short
git -C alice status --short
```
Esperado: branch remota ausente após exclusão; cache origin/feat/summary de Bob pode existir antes do prune e some depois. A branch local permanece até -d; tips main locais iguais ao origin main e summary ready preservado. Exclusão local pode recusar se não integrada; pare em vez de forçar. Uso profissional: limpar branches integradas após revisão, não antes. Confirme que nenhum trabalho restante é necessário. Feche editores e sessão dedicada; exclua apenas o pai temporário registrado pelo gerenciador de arquivos, nunca guia, home ou repo de trabalho.

## Erros comuns e segurança

Exclusão remota pode prejudicar colegas ou remover a última ref nomeada de trabalho. Ancestralidade vale para este lab fast-forward/merge; squash pode exigir evidências de conteúdo e revisão separadas. Prune não é exclusão no servidor. Recuperação depende de commit disponível e autorização para republicar; não é garantida.

## Exercício e autocorreção

Após excluir feature remota, por que Bob ainda a vê? Dica: ref em cache. Resposta: fetch --prune remove ref de tracking obsoleta, não a branch local de Bob. Passe se feature remota e cache sumirem após prune, main preservar summary e status estiver limpo.

## Referência rápida

- `git push -u origin feat/summary`
- `git switch --track origin/feat/summary`
- `git push --delete origin feat/summary`
- `git fetch --prune origin`

## Fontes oficiais

- [Git: git-push](https://git-scm.com/docs/git-push)
- [Git: git-fetch](https://git-scm.com/docs/git-fetch)
- [Git: git-switch](https://git-scm.com/docs/git-switch)
- [Git: git-branch](https://git-scm.com/docs/git-branch)
- [Git: git-ls-remote](https://git-scm.com/docs/git-ls-remote)
- [Git: git-merge-base](https://git-scm.com/docs/git-merge-base)
