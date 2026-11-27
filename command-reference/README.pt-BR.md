# 15 Referência de comandos

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../git-internals/README.pt-BR.md) · [Índice](../docs/learning-path.pt-BR.md) · [Próximo](../practical-projects/README.pt-BR.md)
<!-- /navigation -->

Gerado a partir do JSON canônico. Edite os registros, não esta página.

As entradas descrevem comandos e operações, não uma sequência a executar. Pratique em repositórios descartáveis. Operações hospedadas são opcionais.

**Total de entradas distintas: 120**

## Categorias

<!-- chapters -->
- [Inicialização e configuração](01-setup-and-configuration/README.pt-BR.md) (8)
- [Inspeção do repositório](02-repository-inspection/README.pt-BR.md) (9)
- [Working tree e staging](03-working-tree-and-staging/README.pt-BR.md) (10)
- [Commits e tags](04-commits-and-tags/README.pt-BR.md) (8)
- [Histórico e comparação](05-history-and-comparison/README.pt-BR.md) (10)
- [Gerenciamento de branches](06-branch-management/README.pt-BR.md) (10)
- [Merge, rebase e conflitos](07-merge-rebase-and-conflicts/README.pt-BR.md) (10)
- [Remotos e sincronização](08-remotes-and-synchronization/README.pt-BR.md) (7)
- [Recuperação e stash](09-recovery-and-stash/README.pt-BR.md) (7)
- [Pesquisa e diagnóstico](10-search-and-troubleshooting/README.pt-BR.md) (8)
- [Operações avançadas](11-advanced-git-operations/README.pt-BR.md) (9)
- [Internals e plumbing](12-internals-and-plumbing/README.pt-BR.md) (8)
- [Segurança e manutenção](13-security-and-maintenance/README.pt-BR.md) (8)
- [Plataformas e automação](14-platforms-and-automation/README.pt-BR.md) (8)
<!-- /chapters -->

## Quantidade por tipo de entrada

- Ferramenta externa: 9
- Comando nativo: 39
- Uso de opção: 61
- Operação de plataforma: 0
- Subcomando: 10
- Fluxo: 1

## Pesquisar por intenção

### Autenticar com segurança

- [`git credential reject`](13-security-and-maintenance/README.pt-BR.md#git-credential-reject)

### Automatizar fluxo

- [`git status --porcelain`](02-repository-inspection/README.pt-BR.md#git-status-porcelain)
- [`git for-each-ref`](12-internals-and-plumbing/README.pt-BR.md#git-for-each-ref)
- [`gh pr create`](14-platforms-and-automation/README.pt-BR.md#gh-pr-create)
- [`glab mr create`](14-platforms-and-automation/README.pt-BR.md#glab-mr-create)

### Registrar alterações

- [`git commit`](04-commits-and-tags/README.pt-BR.md#git-commit)
- [`git commit -a`](04-commits-and-tags/README.pt-BR.md#git-commit-all)
- [`git commit --amend`](04-commits-and-tags/README.pt-BR.md#git-commit-amend)
- [`git commit --fixup`](04-commits-and-tags/README.pt-BR.md#git-commit-fixup)
- [`git commit -S`](13-security-and-maintenance/README.pt-BR.md#git-commit-sign)

### Comparar alterações

- [`git diff`](05-history-and-comparison/README.pt-BR.md#git-diff)
- [`git diff --cached`](05-history-and-comparison/README.pt-BR.md#git-diff-cached)
- [`git diff A B`](05-history-and-comparison/README.pt-BR.md#git-diff-two-revisions)
- [`git diff --stat`](05-history-and-comparison/README.pt-BR.md#git-diff-stat)
- [`git diff A...B`](05-history-and-comparison/README.pt-BR.md#git-diff-three-dot)
- [`git range-diff`](05-history-and-comparison/README.pt-BR.md#git-range-diff)

### Configurar Git

- [`git --version`](01-setup-and-configuration/README.pt-BR.md#git-version)
- [`git init`](01-setup-and-configuration/README.pt-BR.md#git-init)
- [`git config --local`](01-setup-and-configuration/README.pt-BR.md#git-config-local)
- [`git config --global`](01-setup-and-configuration/README.pt-BR.md#git-config-global)
- [`git branch --set-upstream-to`](06-branch-management/README.pt-BR.md#git-branch-upstream)
- [`git remote add`](08-remotes-and-synchronization/README.pt-BR.md#git-remote-add)

### Configurar identidade

- [`git config --local`](01-setup-and-configuration/README.pt-BR.md#git-config-local)
- [`git config --global`](01-setup-and-configuration/README.pt-BR.md#git-config-global)
- [`git config --get`](01-setup-and-configuration/README.pt-BR.md#git-config-get)

### Criar repositório

- [`git init`](01-setup-and-configuration/README.pt-BR.md#git-init)
- [`git init --bare`](01-setup-and-configuration/README.pt-BR.md#git-init-bare)
- [`git clone`](08-remotes-and-synchronization/README.pt-BR.md#git-clone)
- [`git clone --filter`](11-advanced-git-operations/README.pt-BR.md#git-clone-filter)

### Encontrar ajuda

- [`git help`](01-setup-and-configuration/README.pt-BR.md#git-help)

### Encontrar regressão

- [`git bisect`](10-search-and-troubleshooting/README.pt-BR.md#git-bisect)

### Ignorar arquivos

- [`git check-ignore`](02-repository-inspection/README.pt-BR.md#git-check-ignore)
- [`git rm --cached`](03-working-tree-and-staging/README.pt-BR.md#git-rm-cached)

### Inspecionar autoria

- [`git blame`](10-search-and-troubleshooting/README.pt-BR.md#git-blame)

### Inspecionar CI

- [`gh pr checks`](14-platforms-and-automation/README.pt-BR.md#gh-pr-checks)
- [`gh run view`](14-platforms-and-automation/README.pt-BR.md#gh-run-view)
- [`glab ci status`](14-platforms-and-automation/README.pt-BR.md#glab-ci-status)

### Inspecionar configuração

- [`git config --list --show-origin`](01-setup-and-configuration/README.pt-BR.md#git-config-show-origin)
- [`git config --get`](01-setup-and-configuration/README.pt-BR.md#git-config-get)

### Inspecionar arquivos

- [`git ls-files`](02-repository-inspection/README.pt-BR.md#git-ls-files)
- [`git clean -n`](03-working-tree-and-staging/README.pt-BR.md#git-clean-dry-run)
- [`git log -- path`](05-history-and-comparison/README.pt-BR.md#git-log-path)
- [`git sparse-checkout set`](11-advanced-git-operations/README.pt-BR.md#git-sparse-checkout-set)
- [`git ls-tree`](12-internals-and-plumbing/README.pt-BR.md#git-ls-tree)

### Inspecionar histórico

- [`git log`](05-history-and-comparison/README.pt-BR.md#git-log)
- [`git log --graph`](05-history-and-comparison/README.pt-BR.md#git-log-graph)
- [`git log -- path`](05-history-and-comparison/README.pt-BR.md#git-log-path)
- [`git show`](05-history-and-comparison/README.pt-BR.md#git-show)
- [`git diff A...B`](05-history-and-comparison/README.pt-BR.md#git-diff-three-dot)
- [`git switch --detach`](06-branch-management/README.pt-BR.md#git-switch-detach)
- [`git branch --merged`](06-branch-management/README.pt-BR.md#git-branch-merged)
- [`git reflog`](09-recovery-and-stash/README.pt-BR.md#git-reflog)
- [`git blame`](10-search-and-troubleshooting/README.pt-BR.md#git-blame)
- [`git log -S`](10-search-and-troubleshooting/README.pt-BR.md#git-log-pickaxe-string)
- [`git log -G`](10-search-and-troubleshooting/README.pt-BR.md#git-log-pickaxe-regex)
- [`git log --follow`](10-search-and-troubleshooting/README.pt-BR.md#git-log-follow)
- [`git bisect`](10-search-and-troubleshooting/README.pt-BR.md#git-bisect)
- [`git cat-file -p`](12-internals-and-plumbing/README.pt-BR.md#git-cat-file-pretty)
- [`git rev-list`](12-internals-and-plumbing/README.pt-BR.md#git-rev-list)

### Inspecionar internals do index

- [`git ls-files --unmerged`](10-search-and-troubleshooting/README.pt-BR.md#git-ls-files-unmerged)
- [`git ls-files --stage`](12-internals-and-plumbing/README.pt-BR.md#git-ls-files-stage)

### Inspecionar objetos Git

- [`git count-objects`](02-repository-inspection/README.pt-BR.md#git-count-objects)
- [`git show`](05-history-and-comparison/README.pt-BR.md#git-show)
- [`git cat-file -t`](12-internals-and-plumbing/README.pt-BR.md#git-cat-file-type)
- [`git cat-file -p`](12-internals-and-plumbing/README.pt-BR.md#git-cat-file-pretty)
- [`git hash-object`](12-internals-and-plumbing/README.pt-BR.md#git-hash-object)
- [`git ls-tree`](12-internals-and-plumbing/README.pt-BR.md#git-ls-tree)
- [`git rev-list`](12-internals-and-plumbing/README.pt-BR.md#git-rev-list)
- [`git ls-files --stage`](12-internals-and-plumbing/README.pt-BR.md#git-ls-files-stage)
- [`git fsck`](13-security-and-maintenance/README.pt-BR.md#git-fsck)

### Inspecionar referências

- [`git show-ref`](02-repository-inspection/README.pt-BR.md#git-show-ref)
- [`git tag -l`](04-commits-and-tags/README.pt-BR.md#git-tag-list)
- [`git branch --list`](06-branch-management/README.pt-BR.md#git-branch-list)
- [`git fetch`](08-remotes-and-synchronization/README.pt-BR.md#git-fetch)
- [`git reflog`](09-recovery-and-stash/README.pt-BR.md#git-reflog)
- [`git symbolic-ref HEAD`](12-internals-and-plumbing/README.pt-BR.md#git-symbolic-ref-read)
- [`git for-each-ref`](12-internals-and-plumbing/README.pt-BR.md#git-for-each-ref)

### Inspecionar estado do repositório

- [`git status`](02-repository-inspection/README.pt-BR.md#git-status)
- [`git rev-parse --show-toplevel`](02-repository-inspection/README.pt-BR.md#git-rev-parse-show-toplevel)
- [`git rev-parse --git-dir`](02-repository-inspection/README.pt-BR.md#git-rev-parse-git-dir)
- [`git rev-parse --is-bare-repository`](02-repository-inspection/README.pt-BR.md#git-rev-parse-is-bare)
- [`git branch --show-current`](06-branch-management/README.pt-BR.md#git-branch-show-current)
- [`git diff --check`](10-search-and-troubleshooting/README.pt-BR.md#git-diff-check)
- [`git symbolic-ref HEAD`](12-internals-and-plumbing/README.pt-BR.md#git-symbolic-ref-read)
- [`gh pr view`](14-platforms-and-automation/README.pt-BR.md#gh-pr-view)
- [`glab mr view`](14-platforms-and-automation/README.pt-BR.md#glab-mr-view)

### Verificar versão do Git

- [`git --version`](01-setup-and-configuration/README.pt-BR.md#git-version)
- [`git help`](01-setup-and-configuration/README.pt-BR.md#git-help)

### Integrar alterações

- [`git merge`](07-merge-rebase-and-conflicts/README.pt-BR.md#git-merge)
- [`git merge --ff-only`](07-merge-rebase-and-conflicts/README.pt-BR.md#git-merge-ff-only)
- [`git merge --no-ff`](07-merge-rebase-and-conflicts/README.pt-BR.md#git-merge-no-ff)
- [`git merge --squash`](07-merge-rebase-and-conflicts/README.pt-BR.md#git-merge-squash)
- [`git merge --continue`](07-merge-rebase-and-conflicts/README.pt-BR.md#git-merge-continue)
- [`git rebase`](07-merge-rebase-and-conflicts/README.pt-BR.md#git-rebase)
- [`git pull --ff-only`](08-remotes-and-synchronization/README.pt-BR.md#git-pull-ff-only)
- [`git cherry-pick`](09-recovery-and-stash/README.pt-BR.md#git-cherry-pick)
- [`git subtree add`](11-advanced-git-operations/README.pt-BR.md#git-subtree-add)

### Limitar checkout ou clone

- [`git sparse-checkout set`](11-advanced-git-operations/README.pt-BR.md#git-sparse-checkout-set)
- [`git clone --filter`](11-advanced-git-operations/README.pt-BR.md#git-clone-filter)

### Manter um repositório

- [`git gc`](13-security-and-maintenance/README.pt-BR.md#git-gc)
- [`git maintenance run`](13-security-and-maintenance/README.pt-BR.md#git-maintenance-run)

### Gerenciar branches

- [`git log --graph`](05-history-and-comparison/README.pt-BR.md#git-log-graph)
- [`git branch --list`](06-branch-management/README.pt-BR.md#git-branch-list)
- [`git branch NAME`](06-branch-management/README.pt-BR.md#git-branch-create)
- [`git branch --show-current`](06-branch-management/README.pt-BR.md#git-branch-show-current)
- [`git switch`](06-branch-management/README.pt-BR.md#git-switch)
- [`git switch -c`](06-branch-management/README.pt-BR.md#git-switch-create)
- [`git branch -m`](06-branch-management/README.pt-BR.md#git-branch-rename)
- [`git branch -d`](06-branch-management/README.pt-BR.md#git-branch-delete)
- [`git branch --merged`](06-branch-management/README.pt-BR.md#git-branch-merged)
- [`git branch --set-upstream-to`](06-branch-management/README.pt-BR.md#git-branch-upstream)
- [`git push --delete`](08-remotes-and-synchronization/README.pt-BR.md#git-push-delete)
- [`git worktree add`](11-advanced-git-operations/README.pt-BR.md#git-worktree-add)

### Gerenciar dependências de repositórios

- [`git submodule add`](11-advanced-git-operations/README.pt-BR.md#git-submodule-add)
- [`git submodule update --init --recursive`](11-advanced-git-operations/README.pt-BR.md#git-submodule-update)
- [`git subtree add`](11-advanced-git-operations/README.pt-BR.md#git-subtree-add)

### Gerenciar arquivos

- [`git rm`](03-working-tree-and-staging/README.pt-BR.md#git-rm)
- [`git mv`](03-working-tree-and-staging/README.pt-BR.md#git-mv)

### Gerenciar releases

- [`git tag`](04-commits-and-tags/README.pt-BR.md#git-tag)
- [`git tag -a`](04-commits-and-tags/README.pt-BR.md#git-tag-annotated)
- [`gh release create`](14-platforms-and-automation/README.pt-BR.md#gh-release-create)

### Gerenciar remotos

- [`git remote add`](08-remotes-and-synchronization/README.pt-BR.md#git-remote-add)
- [`git push`](08-remotes-and-synchronization/README.pt-BR.md#git-push)
- [`git push --delete`](08-remotes-and-synchronization/README.pt-BR.md#git-push-delete)

### Gerenciar tags

- [`git tag`](04-commits-and-tags/README.pt-BR.md#git-tag)
- [`git tag -a`](04-commits-and-tags/README.pt-BR.md#git-tag-annotated)
- [`git tag -d`](04-commits-and-tags/README.pt-BR.md#git-tag-delete)
- [`git tag -l`](04-commits-and-tags/README.pt-BR.md#git-tag-list)
- [`git tag -s`](13-security-and-maintenance/README.pt-BR.md#git-tag-sign)
- [`git verify-tag`](13-security-and-maintenance/README.pt-BR.md#git-verify-tag)
- [`gh release create`](14-platforms-and-automation/README.pt-BR.md#gh-release-create)

### Empacotar histórico ou arquivos

- [`git archive`](11-advanced-git-operations/README.pt-BR.md#git-archive)
- [`git bundle create`](11-advanced-git-operations/README.pt-BR.md#git-bundle-create)

### Trabalhar em paralelo

- [`git branch NAME`](06-branch-management/README.pt-BR.md#git-branch-create)
- [`git switch -c`](06-branch-management/README.pt-BR.md#git-switch-create)
- [`git worktree add`](11-advanced-git-operations/README.pt-BR.md#git-worktree-add)

### Proteger histórico

- [`git branch -d`](06-branch-management/README.pt-BR.md#git-branch-delete)
- [`git branch --merged`](06-branch-management/README.pt-BR.md#git-branch-merged)
- [`git merge --ff-only`](07-merge-rebase-and-conflicts/README.pt-BR.md#git-merge-ff-only)
- [`git pull --ff-only`](08-remotes-and-synchronization/README.pt-BR.md#git-pull-ff-only)
- [`git push --delete`](08-remotes-and-synchronization/README.pt-BR.md#git-push-delete)
- [`git push --force-with-lease`](08-remotes-and-synchronization/README.pt-BR.md#git-push-force-with-lease)
- [`git revert`](09-recovery-and-stash/README.pt-BR.md#git-revert)
- [`git gc`](13-security-and-maintenance/README.pt-BR.md#git-gc)

### Recuperar trabalho

- [`git switch --detach`](06-branch-management/README.pt-BR.md#git-switch-detach)
- [`git merge --abort`](07-merge-rebase-and-conflicts/README.pt-BR.md#git-merge-abort)
- [`git rebase --abort`](07-merge-rebase-and-conflicts/README.pt-BR.md#git-rebase-abort)
- [`git reflog`](09-recovery-and-stash/README.pt-BR.md#git-reflog)
- [`git cherry-pick`](09-recovery-and-stash/README.pt-BR.md#git-cherry-pick)
- [`git stash apply`](09-recovery-and-stash/README.pt-BR.md#git-stash-apply)
- [`git stash pop`](09-recovery-and-stash/README.pt-BR.md#git-stash-pop)
- [`git bundle create`](11-advanced-git-operations/README.pt-BR.md#git-bundle-create)

### Resolver conflitos

- [`git merge --abort`](07-merge-rebase-and-conflicts/README.pt-BR.md#git-merge-abort)
- [`git merge --continue`](07-merge-rebase-and-conflicts/README.pt-BR.md#git-merge-continue)
- [`git rebase --continue`](07-merge-rebase-and-conflicts/README.pt-BR.md#git-rebase-continue)
- [`git rebase --abort`](07-merge-rebase-and-conflicts/README.pt-BR.md#git-rebase-abort)
- [`git ls-files --unmerged`](10-search-and-troubleshooting/README.pt-BR.md#git-ls-files-unmerged)
- [`git rerere`](11-advanced-git-operations/README.pt-BR.md#git-rerere)

### Revisar alterações

- [`git show`](05-history-and-comparison/README.pt-BR.md#git-show)
- [`git diff`](05-history-and-comparison/README.pt-BR.md#git-diff)
- [`git diff --cached`](05-history-and-comparison/README.pt-BR.md#git-diff-cached)
- [`git diff A B`](05-history-and-comparison/README.pt-BR.md#git-diff-two-revisions)
- [`git diff --stat`](05-history-and-comparison/README.pt-BR.md#git-diff-stat)
- [`git diff A...B`](05-history-and-comparison/README.pt-BR.md#git-diff-three-dot)
- [`git range-diff`](05-history-and-comparison/README.pt-BR.md#git-range-diff)
- [`git rebase -i`](07-merge-rebase-and-conflicts/README.pt-BR.md#git-rebase-interactive)
- [`git diff --check`](10-search-and-troubleshooting/README.pt-BR.md#git-diff-check)
- [`gh pr create`](14-platforms-and-automation/README.pt-BR.md#gh-pr-create)
- [`gh pr view`](14-platforms-and-automation/README.pt-BR.md#gh-pr-view)
- [`gh pr checks`](14-platforms-and-automation/README.pt-BR.md#gh-pr-checks)
- [`glab mr create`](14-platforms-and-automation/README.pt-BR.md#glab-mr-create)
- [`glab mr view`](14-platforms-and-automation/README.pt-BR.md#glab-mr-view)

### Reescrever histórico local

- [`git commit --amend`](04-commits-and-tags/README.pt-BR.md#git-commit-amend)
- [`git commit --fixup`](04-commits-and-tags/README.pt-BR.md#git-commit-fixup)
- [`git range-diff`](05-history-and-comparison/README.pt-BR.md#git-range-diff)
- [`git rebase`](07-merge-rebase-and-conflicts/README.pt-BR.md#git-rebase)
- [`git rebase -i`](07-merge-rebase-and-conflicts/README.pt-BR.md#git-rebase-interactive)
- [`git rebase --continue`](07-merge-rebase-and-conflicts/README.pt-BR.md#git-rebase-continue)
- [`git push --force-with-lease`](08-remotes-and-synchronization/README.pt-BR.md#git-push-force-with-lease)
- [`git reset`](09-recovery-and-stash/README.pt-BR.md#git-reset)

### Pesquisar conteúdo

- [`git grep`](10-search-and-troubleshooting/README.pt-BR.md#git-grep)
- [`git log -S`](10-search-and-troubleshooting/README.pt-BR.md#git-log-pickaxe-string)
- [`git log -G`](10-search-and-troubleshooting/README.pt-BR.md#git-log-pickaxe-regex)
- [`git log --follow`](10-search-and-troubleshooting/README.pt-BR.md#git-log-follow)

### Guardar trabalho temporariamente

- [`git stash push`](09-recovery-and-stash/README.pt-BR.md#git-stash-push)
- [`git stash apply`](09-recovery-and-stash/README.pt-BR.md#git-stash-apply)
- [`git stash pop`](09-recovery-and-stash/README.pt-BR.md#git-stash-pop)

### Simular colaboração

- [`git init --bare`](01-setup-and-configuration/README.pt-BR.md#git-init-bare)

### Preparar alterações

- [`git add`](03-working-tree-and-staging/README.pt-BR.md#git-add)
- [`git add -A`](03-working-tree-and-staging/README.pt-BR.md#git-add-all)
- [`git add -u`](03-working-tree-and-staging/README.pt-BR.md#git-add-update)
- [`git add -p`](03-working-tree-and-staging/README.pt-BR.md#git-add-patch)
- [`git commit -a`](04-commits-and-tags/README.pt-BR.md#git-commit-all)
- [`git diff --cached`](05-history-and-comparison/README.pt-BR.md#git-diff-cached)
- [`git merge --squash`](07-merge-rebase-and-conflicts/README.pt-BR.md#git-merge-squash)

### Trocar contexto de trabalho

- [`git switch`](06-branch-management/README.pt-BR.md#git-switch)
- [`git switch -c`](06-branch-management/README.pt-BR.md#git-switch-create)
- [`git switch --detach`](06-branch-management/README.pt-BR.md#git-switch-detach)
- [`git stash push`](09-recovery-and-stash/README.pt-BR.md#git-stash-push)

### Sincronizar repositórios

- [`git branch --set-upstream-to`](06-branch-management/README.pt-BR.md#git-branch-upstream)
- [`git clone`](08-remotes-and-synchronization/README.pt-BR.md#git-clone)
- [`git fetch`](08-remotes-and-synchronization/README.pt-BR.md#git-fetch)
- [`git pull --ff-only`](08-remotes-and-synchronization/README.pt-BR.md#git-pull-ff-only)
- [`git push`](08-remotes-and-synchronization/README.pt-BR.md#git-push)
- [`git push --force-with-lease`](08-remotes-and-synchronization/README.pt-BR.md#git-push-force-with-lease)
- [`git submodule update --init --recursive`](11-advanced-git-operations/README.pt-BR.md#git-submodule-update)

### Diagnosticar configuração

- [`git config --list --show-origin`](01-setup-and-configuration/README.pt-BR.md#git-config-show-origin)
- [`git credential reject`](13-security-and-maintenance/README.pt-BR.md#git-credential-reject)

### Desfazer alterações

- [`git restore`](03-working-tree-and-staging/README.pt-BR.md#git-restore)
- [`git tag -d`](04-commits-and-tags/README.pt-BR.md#git-tag-delete)
- [`git reset`](09-recovery-and-stash/README.pt-BR.md#git-reset)
- [`git revert`](09-recovery-and-stash/README.pt-BR.md#git-revert)

### Retirar alterações do staging

- [`git restore --staged`](03-working-tree-and-staging/README.pt-BR.md#git-restore-staged)
- [`git reset`](09-recovery-and-stash/README.pt-BR.md#git-reset)

### Verificar integridade

- [`git fsck`](13-security-and-maintenance/README.pt-BR.md#git-fsck)

### Verificar assinaturas

- [`git commit -S`](13-security-and-maintenance/README.pt-BR.md#git-commit-sign)
- [`git tag -s`](13-security-and-maintenance/README.pt-BR.md#git-tag-sign)
- [`git verify-commit`](13-security-and-maintenance/README.pt-BR.md#git-verify-commit)
- [`git verify-tag`](13-security-and-maintenance/README.pt-BR.md#git-verify-tag)


---

<!-- navigation-footer -->
[Anterior](../git-internals/README.pt-BR.md) · [Índice](../docs/learning-path.pt-BR.md) · [Próximo](../practical-projects/README.pt-BR.md)
<!-- /navigation-footer -->
