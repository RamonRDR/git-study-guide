# Pull, push e históricos divergentes

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../02-fetch-and-tracking/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../04-remote-branch-lifecycle/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 35 min

**Pré-requisitos:** [Fetch, referências e upstream tracking](../02-fetch-and-tracking/README.pt-BR.md)

**Objetivo:** Reproduzir e resolver com segurança a rejeição non-fast-forward.

## O que é e por quê

Pull faz fetch e integra na branch atual. `git pull --ff-only origin main` recusa histórico divergente, embora fetch ainda possa atualizar refs de tracking. `git pull --no-rebase origin main` escolhe merge (pode criar commit de dois pais); `git pull --rebase origin main` reaplica commits locais sobre a base obtida, normalmente mudando IDs. Padrões variam por versão/configuração, escolha explicitamente. Push normalmente recusa atualização de branch que descartaria ancestralidade remota. A rejeição protege trabalho compartilhado, não deve ser contornada.

## Prática

Continue com clones sincronizados em main. Repita todas as verificações de segurança e identidade do capítulo 02 para cada ator antes das operações; inspecione cada diff staged antes do commit. Crie alice/plan.txt com `shared plan` e bob/bob.txt com `bob update`, ambos com quebra final. Publique Alice, depois faça commit de Bob e tente seu push.
```text
git -C alice add -- plan.txt
git -C alice diff --cached
git -C alice commit -m "docs: add plan"
git -C alice push origin main
git -C bob add -- bob.txt
git -C bob diff --cached
git -C bob commit -m "docs: add Bob note"
git -C bob push origin main
```
Esperado: o ÚLTIMO push falha (non-fast-forward, às vezes descrito como fetch first). Pare em qualquer falha anterior. Verifique origin main ainda igual ao tip de Alice e commit de Bob preservado. Então:
```text
git -C bob fetch origin
git -C bob rev-list --left-right --count main...origin/main
git -C bob log --all --graph --oneline --decorate
git -C bob diff main origin/main
git -C bob pull --ff-only origin main
```
Esperado: contagem 1 1; último pull recusa. Diagrama: C2 -> A3 (origin/main); C2 -> B3 (main de Bob). Ambos têm commits exclusivos. Verifique HEAD de Bob ainda B3 e status limpo. Faça merge explícito da ref já inspecionada; não se espera conflito porque os arquivos diferem.
```text
git -C bob merge --no-edit origin/main
git -C bob show HEAD:plan.txt
git -C bob show HEAD:bob.txt
git -C bob status --short
git -C bob push origin main
git -C alice pull --ff-only origin main
git -C alice rev-parse HEAD origin/main
git -C bob rev-parse HEAD origin/main
git -C origin.git rev-parse refs/heads/main
```
Esperado: commit de merge M tem pais B3 e A3; ambos os arquivos sobrevivem, tips main iguais a M, status limpo. Em equipe, escolha merge ou rebase conforme política. Apenas para commit local não publicado, rebase após fetch e ref de backup é alternativa; veja módulo 05. Não execute ambas as estratégias neste laboratório.

## Erros comuns e segurança

Não faça force push ou reset para silenciar rejeição. Se houver conflito inesperado no merge, inspecione status e use merge --abort ou resolva como no módulo 05. Se escolher rebase em outro contexto, use rebase --abort/--continue. Push concluído não pode ser desfeito por abort; coordene recuperação com colegas.

## Exercício e autocorreção

Pull ff-only recusado implica que nada mudou? Dica: fase fetch. Resposta: main local não muda, refs de tracking podem atualizar. Passe se os dois commits exclusivos forem ancestrais da main final e ambos os arquivos existirem.

## Referência rápida

- `git pull --ff-only`
- `git pull --no-rebase`
- `git pull --rebase`
- `git push origin main`

## Fontes oficiais

- [Git: git-pull](https://git-scm.com/docs/git-pull)
- [Git: git-push](https://git-scm.com/docs/git-push)
- [Git: git-merge](https://git-scm.com/docs/git-merge)
- [Git: git-rebase](https://git-scm.com/docs/git-rebase)
