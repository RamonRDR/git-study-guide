# 15 Referencia de comandos

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../git-internals/README.es.md) · [Índice](../docs/learning-path.es.md) · [Siguiente](../practical-projects/README.es.md)
<!-- /navigation -->

Generado a partir del JSON canónico. Edita los registros, no esta página.

Las entradas describen comandos y operaciones, no una secuencia para ejecutar. Practica en repositorios desechables. Las operaciones alojadas son opcionales.

**Total de entradas distintas: 120**

## Categorías

<!-- chapters -->
- [Inicio y configuración](01-setup-and-configuration/README.es.md) (8)
- [Inspección del repositorio](02-repository-inspection/README.es.md) (9)
- [Working tree y staging](03-working-tree-and-staging/README.es.md) (10)
- [Commits y etiquetas](04-commits-and-tags/README.es.md) (8)
- [Historial y comparación](05-history-and-comparison/README.es.md) (10)
- [Gestión de ramas](06-branch-management/README.es.md) (10)
- [Merge, rebase y conflictos](07-merge-rebase-and-conflicts/README.es.md) (10)
- [Remotos y sincronización](08-remotes-and-synchronization/README.es.md) (7)
- [Recuperación y stash](09-recovery-and-stash/README.es.md) (7)
- [Búsqueda y diagnóstico](10-search-and-troubleshooting/README.es.md) (8)
- [Operaciones avanzadas](11-advanced-git-operations/README.es.md) (9)
- [Internals y plumbing](12-internals-and-plumbing/README.es.md) (8)
- [Seguridad y mantenimiento](13-security-and-maintenance/README.es.md) (8)
- [Plataformas y automatización](14-platforms-and-automation/README.es.md) (8)
<!-- /chapters -->

## Cantidad por tipo de entrada

- Herramienta externa: 9
- Comando nativo: 39
- Uso de opción: 61
- Operación de plataforma: 0
- Subcomando: 10
- Flujo: 1

## Buscar por intención

### Autenticar con seguridad

- [`git credential reject`](13-security-and-maintenance/README.es.md#git-credential-reject)

### Automatizar flujo

- [`git status --porcelain`](02-repository-inspection/README.es.md#git-status-porcelain)
- [`git for-each-ref`](12-internals-and-plumbing/README.es.md#git-for-each-ref)
- [`gh pr create`](14-platforms-and-automation/README.es.md#gh-pr-create)
- [`glab mr create`](14-platforms-and-automation/README.es.md#glab-mr-create)

### Registrar cambios

- [`git commit`](04-commits-and-tags/README.es.md#git-commit)
- [`git commit -a`](04-commits-and-tags/README.es.md#git-commit-all)
- [`git commit --amend`](04-commits-and-tags/README.es.md#git-commit-amend)
- [`git commit --fixup`](04-commits-and-tags/README.es.md#git-commit-fixup)
- [`git commit -S`](13-security-and-maintenance/README.es.md#git-commit-sign)

### Comparar cambios

- [`git diff`](05-history-and-comparison/README.es.md#git-diff)
- [`git diff --cached`](05-history-and-comparison/README.es.md#git-diff-cached)
- [`git diff A B`](05-history-and-comparison/README.es.md#git-diff-two-revisions)
- [`git diff --stat`](05-history-and-comparison/README.es.md#git-diff-stat)
- [`git diff A...B`](05-history-and-comparison/README.es.md#git-diff-three-dot)
- [`git range-diff`](05-history-and-comparison/README.es.md#git-range-diff)

### Configurar Git

- [`git --version`](01-setup-and-configuration/README.es.md#git-version)
- [`git init`](01-setup-and-configuration/README.es.md#git-init)
- [`git config --local`](01-setup-and-configuration/README.es.md#git-config-local)
- [`git config --global`](01-setup-and-configuration/README.es.md#git-config-global)
- [`git branch --set-upstream-to`](06-branch-management/README.es.md#git-branch-upstream)
- [`git remote add`](08-remotes-and-synchronization/README.es.md#git-remote-add)

### Configurar identidad

- [`git config --local`](01-setup-and-configuration/README.es.md#git-config-local)
- [`git config --global`](01-setup-and-configuration/README.es.md#git-config-global)
- [`git config --get`](01-setup-and-configuration/README.es.md#git-config-get)

### Crear repositorio

- [`git init`](01-setup-and-configuration/README.es.md#git-init)
- [`git init --bare`](01-setup-and-configuration/README.es.md#git-init-bare)
- [`git clone`](08-remotes-and-synchronization/README.es.md#git-clone)
- [`git clone --filter`](11-advanced-git-operations/README.es.md#git-clone-filter)

### Encontrar ayuda

- [`git help`](01-setup-and-configuration/README.es.md#git-help)

### Encontrar regresión

- [`git bisect`](10-search-and-troubleshooting/README.es.md#git-bisect)

### Ignorar archivos

- [`git check-ignore`](02-repository-inspection/README.es.md#git-check-ignore)
- [`git rm --cached`](03-working-tree-and-staging/README.es.md#git-rm-cached)

### Inspeccionar autoría

- [`git blame`](10-search-and-troubleshooting/README.es.md#git-blame)

### Inspeccionar CI

- [`gh pr checks`](14-platforms-and-automation/README.es.md#gh-pr-checks)
- [`gh run view`](14-platforms-and-automation/README.es.md#gh-run-view)
- [`glab ci status`](14-platforms-and-automation/README.es.md#glab-ci-status)

### Inspeccionar configuración

- [`git config --list --show-origin`](01-setup-and-configuration/README.es.md#git-config-show-origin)
- [`git config --get`](01-setup-and-configuration/README.es.md#git-config-get)

### Inspeccionar archivos

- [`git ls-files`](02-repository-inspection/README.es.md#git-ls-files)
- [`git clean -n`](03-working-tree-and-staging/README.es.md#git-clean-dry-run)
- [`git log -- path`](05-history-and-comparison/README.es.md#git-log-path)
- [`git sparse-checkout set`](11-advanced-git-operations/README.es.md#git-sparse-checkout-set)
- [`git ls-tree`](12-internals-and-plumbing/README.es.md#git-ls-tree)

### Inspeccionar historial

- [`git log`](05-history-and-comparison/README.es.md#git-log)
- [`git log --graph`](05-history-and-comparison/README.es.md#git-log-graph)
- [`git log -- path`](05-history-and-comparison/README.es.md#git-log-path)
- [`git show`](05-history-and-comparison/README.es.md#git-show)
- [`git diff A...B`](05-history-and-comparison/README.es.md#git-diff-three-dot)
- [`git switch --detach`](06-branch-management/README.es.md#git-switch-detach)
- [`git branch --merged`](06-branch-management/README.es.md#git-branch-merged)
- [`git reflog`](09-recovery-and-stash/README.es.md#git-reflog)
- [`git blame`](10-search-and-troubleshooting/README.es.md#git-blame)
- [`git log -S`](10-search-and-troubleshooting/README.es.md#git-log-pickaxe-string)
- [`git log -G`](10-search-and-troubleshooting/README.es.md#git-log-pickaxe-regex)
- [`git log --follow`](10-search-and-troubleshooting/README.es.md#git-log-follow)
- [`git bisect`](10-search-and-troubleshooting/README.es.md#git-bisect)
- [`git cat-file -p`](12-internals-and-plumbing/README.es.md#git-cat-file-pretty)
- [`git rev-list`](12-internals-and-plumbing/README.es.md#git-rev-list)

### Inspeccionar internals del index

- [`git ls-files --unmerged`](10-search-and-troubleshooting/README.es.md#git-ls-files-unmerged)
- [`git ls-files --stage`](12-internals-and-plumbing/README.es.md#git-ls-files-stage)

### Inspeccionar objetos Git

- [`git count-objects`](02-repository-inspection/README.es.md#git-count-objects)
- [`git show`](05-history-and-comparison/README.es.md#git-show)
- [`git cat-file -t`](12-internals-and-plumbing/README.es.md#git-cat-file-type)
- [`git cat-file -p`](12-internals-and-plumbing/README.es.md#git-cat-file-pretty)
- [`git hash-object`](12-internals-and-plumbing/README.es.md#git-hash-object)
- [`git ls-tree`](12-internals-and-plumbing/README.es.md#git-ls-tree)
- [`git rev-list`](12-internals-and-plumbing/README.es.md#git-rev-list)
- [`git ls-files --stage`](12-internals-and-plumbing/README.es.md#git-ls-files-stage)
- [`git fsck`](13-security-and-maintenance/README.es.md#git-fsck)

### Inspeccionar referencias

- [`git show-ref`](02-repository-inspection/README.es.md#git-show-ref)
- [`git tag -l`](04-commits-and-tags/README.es.md#git-tag-list)
- [`git branch --list`](06-branch-management/README.es.md#git-branch-list)
- [`git fetch`](08-remotes-and-synchronization/README.es.md#git-fetch)
- [`git reflog`](09-recovery-and-stash/README.es.md#git-reflog)
- [`git symbolic-ref HEAD`](12-internals-and-plumbing/README.es.md#git-symbolic-ref-read)
- [`git for-each-ref`](12-internals-and-plumbing/README.es.md#git-for-each-ref)

### Inspeccionar estado del repositorio

- [`git status`](02-repository-inspection/README.es.md#git-status)
- [`git rev-parse --show-toplevel`](02-repository-inspection/README.es.md#git-rev-parse-show-toplevel)
- [`git rev-parse --git-dir`](02-repository-inspection/README.es.md#git-rev-parse-git-dir)
- [`git rev-parse --is-bare-repository`](02-repository-inspection/README.es.md#git-rev-parse-is-bare)
- [`git branch --show-current`](06-branch-management/README.es.md#git-branch-show-current)
- [`git diff --check`](10-search-and-troubleshooting/README.es.md#git-diff-check)
- [`git symbolic-ref HEAD`](12-internals-and-plumbing/README.es.md#git-symbolic-ref-read)
- [`gh pr view`](14-platforms-and-automation/README.es.md#gh-pr-view)
- [`glab mr view`](14-platforms-and-automation/README.es.md#glab-mr-view)

### Comprobar versión de Git

- [`git --version`](01-setup-and-configuration/README.es.md#git-version)
- [`git help`](01-setup-and-configuration/README.es.md#git-help)

### Integrar cambios

- [`git merge`](07-merge-rebase-and-conflicts/README.es.md#git-merge)
- [`git merge --ff-only`](07-merge-rebase-and-conflicts/README.es.md#git-merge-ff-only)
- [`git merge --no-ff`](07-merge-rebase-and-conflicts/README.es.md#git-merge-no-ff)
- [`git merge --squash`](07-merge-rebase-and-conflicts/README.es.md#git-merge-squash)
- [`git merge --continue`](07-merge-rebase-and-conflicts/README.es.md#git-merge-continue)
- [`git rebase`](07-merge-rebase-and-conflicts/README.es.md#git-rebase)
- [`git pull --ff-only`](08-remotes-and-synchronization/README.es.md#git-pull-ff-only)
- [`git cherry-pick`](09-recovery-and-stash/README.es.md#git-cherry-pick)
- [`git subtree add`](11-advanced-git-operations/README.es.md#git-subtree-add)

### Limitar checkout o clonación

- [`git sparse-checkout set`](11-advanced-git-operations/README.es.md#git-sparse-checkout-set)
- [`git clone --filter`](11-advanced-git-operations/README.es.md#git-clone-filter)

### Mantener un repositorio

- [`git gc`](13-security-and-maintenance/README.es.md#git-gc)
- [`git maintenance run`](13-security-and-maintenance/README.es.md#git-maintenance-run)

### Gestionar ramas

- [`git log --graph`](05-history-and-comparison/README.es.md#git-log-graph)
- [`git branch --list`](06-branch-management/README.es.md#git-branch-list)
- [`git branch NAME`](06-branch-management/README.es.md#git-branch-create)
- [`git branch --show-current`](06-branch-management/README.es.md#git-branch-show-current)
- [`git switch`](06-branch-management/README.es.md#git-switch)
- [`git switch -c`](06-branch-management/README.es.md#git-switch-create)
- [`git branch -m`](06-branch-management/README.es.md#git-branch-rename)
- [`git branch -d`](06-branch-management/README.es.md#git-branch-delete)
- [`git branch --merged`](06-branch-management/README.es.md#git-branch-merged)
- [`git branch --set-upstream-to`](06-branch-management/README.es.md#git-branch-upstream)
- [`git push --delete`](08-remotes-and-synchronization/README.es.md#git-push-delete)
- [`git worktree add`](11-advanced-git-operations/README.es.md#git-worktree-add)

### Gestionar dependencias de repositorios

- [`git submodule add`](11-advanced-git-operations/README.es.md#git-submodule-add)
- [`git submodule update --init --recursive`](11-advanced-git-operations/README.es.md#git-submodule-update)
- [`git subtree add`](11-advanced-git-operations/README.es.md#git-subtree-add)

### Gestionar archivos

- [`git rm`](03-working-tree-and-staging/README.es.md#git-rm)
- [`git mv`](03-working-tree-and-staging/README.es.md#git-mv)

### Gestionar versiones

- [`git tag`](04-commits-and-tags/README.es.md#git-tag)
- [`git tag -a`](04-commits-and-tags/README.es.md#git-tag-annotated)
- [`gh release create`](14-platforms-and-automation/README.es.md#gh-release-create)

### Gestionar remotos

- [`git remote add`](08-remotes-and-synchronization/README.es.md#git-remote-add)
- [`git push`](08-remotes-and-synchronization/README.es.md#git-push)
- [`git push --delete`](08-remotes-and-synchronization/README.es.md#git-push-delete)

### Gestionar etiquetas

- [`git tag`](04-commits-and-tags/README.es.md#git-tag)
- [`git tag -a`](04-commits-and-tags/README.es.md#git-tag-annotated)
- [`git tag -d`](04-commits-and-tags/README.es.md#git-tag-delete)
- [`git tag -l`](04-commits-and-tags/README.es.md#git-tag-list)
- [`git tag -s`](13-security-and-maintenance/README.es.md#git-tag-sign)
- [`git verify-tag`](13-security-and-maintenance/README.es.md#git-verify-tag)
- [`gh release create`](14-platforms-and-automation/README.es.md#gh-release-create)

### Empaquetar historial o archivos

- [`git archive`](11-advanced-git-operations/README.es.md#git-archive)
- [`git bundle create`](11-advanced-git-operations/README.es.md#git-bundle-create)

### Trabajar en paralelo

- [`git branch NAME`](06-branch-management/README.es.md#git-branch-create)
- [`git switch -c`](06-branch-management/README.es.md#git-switch-create)
- [`git worktree add`](11-advanced-git-operations/README.es.md#git-worktree-add)

### Proteger historial

- [`git branch -d`](06-branch-management/README.es.md#git-branch-delete)
- [`git branch --merged`](06-branch-management/README.es.md#git-branch-merged)
- [`git merge --ff-only`](07-merge-rebase-and-conflicts/README.es.md#git-merge-ff-only)
- [`git pull --ff-only`](08-remotes-and-synchronization/README.es.md#git-pull-ff-only)
- [`git push --delete`](08-remotes-and-synchronization/README.es.md#git-push-delete)
- [`git push --force-with-lease`](08-remotes-and-synchronization/README.es.md#git-push-force-with-lease)
- [`git revert`](09-recovery-and-stash/README.es.md#git-revert)
- [`git gc`](13-security-and-maintenance/README.es.md#git-gc)

### Recuperar trabajo

- [`git switch --detach`](06-branch-management/README.es.md#git-switch-detach)
- [`git merge --abort`](07-merge-rebase-and-conflicts/README.es.md#git-merge-abort)
- [`git rebase --abort`](07-merge-rebase-and-conflicts/README.es.md#git-rebase-abort)
- [`git reflog`](09-recovery-and-stash/README.es.md#git-reflog)
- [`git cherry-pick`](09-recovery-and-stash/README.es.md#git-cherry-pick)
- [`git stash apply`](09-recovery-and-stash/README.es.md#git-stash-apply)
- [`git stash pop`](09-recovery-and-stash/README.es.md#git-stash-pop)
- [`git bundle create`](11-advanced-git-operations/README.es.md#git-bundle-create)

### Resolver conflictos

- [`git merge --abort`](07-merge-rebase-and-conflicts/README.es.md#git-merge-abort)
- [`git merge --continue`](07-merge-rebase-and-conflicts/README.es.md#git-merge-continue)
- [`git rebase --continue`](07-merge-rebase-and-conflicts/README.es.md#git-rebase-continue)
- [`git rebase --abort`](07-merge-rebase-and-conflicts/README.es.md#git-rebase-abort)
- [`git ls-files --unmerged`](10-search-and-troubleshooting/README.es.md#git-ls-files-unmerged)
- [`git rerere`](11-advanced-git-operations/README.es.md#git-rerere)

### Revisar cambios

- [`git show`](05-history-and-comparison/README.es.md#git-show)
- [`git diff`](05-history-and-comparison/README.es.md#git-diff)
- [`git diff --cached`](05-history-and-comparison/README.es.md#git-diff-cached)
- [`git diff A B`](05-history-and-comparison/README.es.md#git-diff-two-revisions)
- [`git diff --stat`](05-history-and-comparison/README.es.md#git-diff-stat)
- [`git diff A...B`](05-history-and-comparison/README.es.md#git-diff-three-dot)
- [`git range-diff`](05-history-and-comparison/README.es.md#git-range-diff)
- [`git rebase -i`](07-merge-rebase-and-conflicts/README.es.md#git-rebase-interactive)
- [`git diff --check`](10-search-and-troubleshooting/README.es.md#git-diff-check)
- [`gh pr create`](14-platforms-and-automation/README.es.md#gh-pr-create)
- [`gh pr view`](14-platforms-and-automation/README.es.md#gh-pr-view)
- [`gh pr checks`](14-platforms-and-automation/README.es.md#gh-pr-checks)
- [`glab mr create`](14-platforms-and-automation/README.es.md#glab-mr-create)
- [`glab mr view`](14-platforms-and-automation/README.es.md#glab-mr-view)

### Reescribir historial local

- [`git commit --amend`](04-commits-and-tags/README.es.md#git-commit-amend)
- [`git commit --fixup`](04-commits-and-tags/README.es.md#git-commit-fixup)
- [`git range-diff`](05-history-and-comparison/README.es.md#git-range-diff)
- [`git rebase`](07-merge-rebase-and-conflicts/README.es.md#git-rebase)
- [`git rebase -i`](07-merge-rebase-and-conflicts/README.es.md#git-rebase-interactive)
- [`git rebase --continue`](07-merge-rebase-and-conflicts/README.es.md#git-rebase-continue)
- [`git push --force-with-lease`](08-remotes-and-synchronization/README.es.md#git-push-force-with-lease)
- [`git reset`](09-recovery-and-stash/README.es.md#git-reset)

### Buscar contenido

- [`git grep`](10-search-and-troubleshooting/README.es.md#git-grep)
- [`git log -S`](10-search-and-troubleshooting/README.es.md#git-log-pickaxe-string)
- [`git log -G`](10-search-and-troubleshooting/README.es.md#git-log-pickaxe-regex)
- [`git log --follow`](10-search-and-troubleshooting/README.es.md#git-log-follow)

### Guardar trabajo temporalmente

- [`git stash push`](09-recovery-and-stash/README.es.md#git-stash-push)
- [`git stash apply`](09-recovery-and-stash/README.es.md#git-stash-apply)
- [`git stash pop`](09-recovery-and-stash/README.es.md#git-stash-pop)

### Simular colaboración

- [`git init --bare`](01-setup-and-configuration/README.es.md#git-init-bare)

### Preparar cambios

- [`git add`](03-working-tree-and-staging/README.es.md#git-add)
- [`git add -A`](03-working-tree-and-staging/README.es.md#git-add-all)
- [`git add -u`](03-working-tree-and-staging/README.es.md#git-add-update)
- [`git add -p`](03-working-tree-and-staging/README.es.md#git-add-patch)
- [`git commit -a`](04-commits-and-tags/README.es.md#git-commit-all)
- [`git diff --cached`](05-history-and-comparison/README.es.md#git-diff-cached)
- [`git merge --squash`](07-merge-rebase-and-conflicts/README.es.md#git-merge-squash)

### Cambiar contexto de trabajo

- [`git switch`](06-branch-management/README.es.md#git-switch)
- [`git switch -c`](06-branch-management/README.es.md#git-switch-create)
- [`git switch --detach`](06-branch-management/README.es.md#git-switch-detach)
- [`git stash push`](09-recovery-and-stash/README.es.md#git-stash-push)

### Sincronizar repositorios

- [`git branch --set-upstream-to`](06-branch-management/README.es.md#git-branch-upstream)
- [`git clone`](08-remotes-and-synchronization/README.es.md#git-clone)
- [`git fetch`](08-remotes-and-synchronization/README.es.md#git-fetch)
- [`git pull --ff-only`](08-remotes-and-synchronization/README.es.md#git-pull-ff-only)
- [`git push`](08-remotes-and-synchronization/README.es.md#git-push)
- [`git push --force-with-lease`](08-remotes-and-synchronization/README.es.md#git-push-force-with-lease)
- [`git submodule update --init --recursive`](11-advanced-git-operations/README.es.md#git-submodule-update)

### Diagnosticar configuración

- [`git config --list --show-origin`](01-setup-and-configuration/README.es.md#git-config-show-origin)
- [`git credential reject`](13-security-and-maintenance/README.es.md#git-credential-reject)

### Deshacer cambios

- [`git restore`](03-working-tree-and-staging/README.es.md#git-restore)
- [`git tag -d`](04-commits-and-tags/README.es.md#git-tag-delete)
- [`git reset`](09-recovery-and-stash/README.es.md#git-reset)
- [`git revert`](09-recovery-and-stash/README.es.md#git-revert)

### Retirar cambios del staging

- [`git restore --staged`](03-working-tree-and-staging/README.es.md#git-restore-staged)
- [`git reset`](09-recovery-and-stash/README.es.md#git-reset)

### Verificar integridad

- [`git fsck`](13-security-and-maintenance/README.es.md#git-fsck)

### Verificar firmas

- [`git commit -S`](13-security-and-maintenance/README.es.md#git-commit-sign)
- [`git tag -s`](13-security-and-maintenance/README.es.md#git-tag-sign)
- [`git verify-commit`](13-security-and-maintenance/README.es.md#git-verify-commit)
- [`git verify-tag`](13-security-and-maintenance/README.es.md#git-verify-tag)


---

<!-- navigation-footer -->
[Anterior](../git-internals/README.es.md) · [Índice](../docs/learning-path.es.md) · [Siguiente](../practical-projects/README.es.md)
<!-- /navigation-footer -->
