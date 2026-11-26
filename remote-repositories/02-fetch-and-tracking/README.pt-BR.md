# Fetch, referências e upstream tracking

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../01-remote-concepts/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../03-pull-push-and-divergence/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 30 min

**Pré-requisitos:** [Remotos, repositórios bare e clones](../01-remote-concepts/README.pt-BR.md)

**Objetivo:** Observar atualização remota antes e depois de fetch sem mudar a árvore de Bob.

## O que é e por quê

HEAD normalmente aponta para refs/heads/main. O remoto tem sua própria refs/heads/main; refs/remotes/origin/main de Bob é um registro local do último tip remoto conhecido. Fetch baixa objetos e atualiza refs configuradas (e FETCH_HEAD), não a branch em checkout, index ou arquivos de trabalho neste clone normal. Push solicita atualização remota e pode atualizar a ref de tracking do clone que envia. O upstream configurado permite que status e branch -vv comparem histórico local com a ref de tracking, não com o estado ao vivo do servidor. Ahead/behind contam commits exclusivos de cada lado.

## Prática

Continue o capítulo 01 no pai registrado. Antes de cada mudança, confira raiz do clone alvo, branch, status limpo, URLs de push/fetch e identidades fictícias de autor e committer; o exemplo é para Alice, substitua alice por bob ao agir como Bob. Ambas as identidades devem começar com `Study Guide Example <learner@example.invalid>`. Antes de todo commit repita ambas as verificações e inspecione o diff staged. Execute individualmente e pare diante de estado inesperado.
```text
git -C alice rev-parse --show-toplevel
git -C alice branch --show-current
git -C alice status --short
git -C alice var GIT_AUTHOR_IDENT
git -C alice var GIT_COMMITTER_IDENT
git -C alice remote get-url --push origin
```
Crie alice/alice.txt em editor de texto simples com linha `alice update` e quebra final. Adicione ao index e inspecione; faça commit somente se esperado, depois envie apenas ao origin local verificado.
```text
git -C alice add -- alice.txt
git -C alice diff --cached
git -C alice commit -m "docs: add Alice note"
git -C alice push origin main
git -C origin.git rev-parse refs/heads/main
git -C bob rev-parse HEAD refs/remotes/origin/main
git -C bob fetch origin
git -C bob rev-parse HEAD refs/remotes/origin/main
git -C bob rev-list --left-right --count main...origin/main
git -C bob log --oneline main..origin/main
git -C bob diff main origin/main
git -C bob branch -vv
git -C bob config --get remote.origin.fetch
```
Antes do fetch de Bob, origin main está em C2, main e origin/main de Bob ainda em C1. Após fetch, origin/main = C2 e HEAD/main = C1; contagem 0 1, alice.txt ausente da árvore de Bob. O refspec padrão `+refs/heads/*:refs/remotes/origin/*` mapeia refs de branches remotas para refs locais de tracking; + permite atualizá-las mesmo com mudança remota não fast-forward. Não é permissão para force push. `main..origin/main` lista commits alcançáveis a partir de origin/main mas não main. Compare snapshots com diff antes de integrar. Verifique Bob limpo e em main, então:
```text
git -C bob merge --ff-only origin/main
git -C bob rev-parse HEAD origin/main
git -C bob show HEAD:alice.txt
git -C bob status --short
```
Esperado: tips iguais, alice update em Bob, status limpo. Uso profissional: fetch e inspeção antes de integrar trabalho de colegas.

## Erros comuns e segurança

Não trate origin/main como dado ao vivo nem o edite diretamente. Fetch não resolve conflitos. Se fast-forward recusar, inspecione divergência sem forçar.

## Exercício e autocorreção

Depois do push de Alice, antes do fetch de Bob, Bob pode estar atrasado mesmo com status atualizado? Dica: tracking local. Resposta: sim; sua ref está obsoleta. Passe se fetch mudar apenas o tip de tracking e merge posterior avançar main.

## Referência rápida

- `git fetch origin`
- `git branch -vv`
- `git rev-list --left-right --count main...origin/main`
- `git merge --ff-only origin/main`

## Fontes oficiais

- [Git: git-fetch](https://git-scm.com/docs/git-fetch)
- [Git: git-branch](https://git-scm.com/docs/git-branch)
- [Git: git-rev-list](https://git-scm.com/docs/git-rev-list)
- [Git: git-merge](https://git-scm.com/docs/git-merge)
