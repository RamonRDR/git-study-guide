# 15 Command Reference

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../git-internals/README.md) · [Index](../docs/learning-path.md) · [Next](../practical-projects/README.md)
<!-- /navigation -->

Generated from canonical catalog JSON. Edit the records, not this page.

Reference entries describe commands and operations, not a sequence to run. Use disposable repositories for practice. Hosted operations are optional.

**Total distinct entries: 120**

## Categories

<!-- chapters -->
- [Setup & Configuration](01-setup-and-configuration/README.md) (8)
- [Repository Inspection](02-repository-inspection/README.md) (9)
- [Working Tree & Staging](03-working-tree-and-staging/README.md) (10)
- [Commits & Tags](04-commits-and-tags/README.md) (8)
- [History & Comparison](05-history-and-comparison/README.md) (10)
- [Branch Management](06-branch-management/README.md) (10)
- [Merge, Rebase & Conflicts](07-merge-rebase-and-conflicts/README.md) (10)
- [Remotes & Synchronization](08-remotes-and-synchronization/README.md) (7)
- [Recovery & Stash](09-recovery-and-stash/README.md) (7)
- [Search & Troubleshooting](10-search-and-troubleshooting/README.md) (8)
- [Advanced Git Operations](11-advanced-git-operations/README.md) (9)
- [Internals & Plumbing](12-internals-and-plumbing/README.md) (8)
- [Security & Maintenance](13-security-and-maintenance/README.md) (8)
- [Platforms & Automation](14-platforms-and-automation/README.md) (8)
<!-- /chapters -->

## Counts by entry type

- External tool: 9
- Native command: 39
- Option usage: 61
- Platform operation: 0
- Subcommand: 10
- Workflow: 1

## Find by intent

### Authenticate safely

- [`git credential reject`](13-security-and-maintenance/README.md#git-credential-reject)

### Automate workflow

- [`git status --porcelain`](02-repository-inspection/README.md#git-status-porcelain)
- [`git for-each-ref`](12-internals-and-plumbing/README.md#git-for-each-ref)
- [`gh pr create`](14-platforms-and-automation/README.md#gh-pr-create)
- [`glab mr create`](14-platforms-and-automation/README.md#glab-mr-create)

### Commit changes

- [`git commit`](04-commits-and-tags/README.md#git-commit)
- [`git commit -a`](04-commits-and-tags/README.md#git-commit-all)
- [`git commit --amend`](04-commits-and-tags/README.md#git-commit-amend)
- [`git commit --fixup`](04-commits-and-tags/README.md#git-commit-fixup)
- [`git commit -S`](13-security-and-maintenance/README.md#git-commit-sign)

### Compare changes

- [`git diff`](05-history-and-comparison/README.md#git-diff)
- [`git diff --cached`](05-history-and-comparison/README.md#git-diff-cached)
- [`git diff A B`](05-history-and-comparison/README.md#git-diff-two-revisions)
- [`git diff --stat`](05-history-and-comparison/README.md#git-diff-stat)
- [`git diff A...B`](05-history-and-comparison/README.md#git-diff-three-dot)
- [`git range-diff`](05-history-and-comparison/README.md#git-range-diff)

### Configure Git

- [`git --version`](01-setup-and-configuration/README.md#git-version)
- [`git init`](01-setup-and-configuration/README.md#git-init)
- [`git config --local`](01-setup-and-configuration/README.md#git-config-local)
- [`git config --global`](01-setup-and-configuration/README.md#git-config-global)
- [`git branch --set-upstream-to`](06-branch-management/README.md#git-branch-upstream)
- [`git remote add`](08-remotes-and-synchronization/README.md#git-remote-add)

### Configure identity

- [`git config --local`](01-setup-and-configuration/README.md#git-config-local)
- [`git config --global`](01-setup-and-configuration/README.md#git-config-global)
- [`git config --get`](01-setup-and-configuration/README.md#git-config-get)

### Create a repository

- [`git init`](01-setup-and-configuration/README.md#git-init)
- [`git init --bare`](01-setup-and-configuration/README.md#git-init-bare)
- [`git clone`](08-remotes-and-synchronization/README.md#git-clone)
- [`git clone --filter`](11-advanced-git-operations/README.md#git-clone-filter)

### Find help

- [`git help`](01-setup-and-configuration/README.md#git-help)

### Find a regression

- [`git bisect`](10-search-and-troubleshooting/README.md#git-bisect)

### Ignore files

- [`git check-ignore`](02-repository-inspection/README.md#git-check-ignore)
- [`git rm --cached`](03-working-tree-and-staging/README.md#git-rm-cached)

### Inspect authorship

- [`git blame`](10-search-and-troubleshooting/README.md#git-blame)

### Inspect CI

- [`gh pr checks`](14-platforms-and-automation/README.md#gh-pr-checks)
- [`gh run view`](14-platforms-and-automation/README.md#gh-run-view)
- [`glab ci status`](14-platforms-and-automation/README.md#glab-ci-status)

### Inspect configuration

- [`git config --list --show-origin`](01-setup-and-configuration/README.md#git-config-show-origin)
- [`git config --get`](01-setup-and-configuration/README.md#git-config-get)

### Inspect files

- [`git ls-files`](02-repository-inspection/README.md#git-ls-files)
- [`git clean -n`](03-working-tree-and-staging/README.md#git-clean-dry-run)
- [`git log -- path`](05-history-and-comparison/README.md#git-log-path)
- [`git sparse-checkout set`](11-advanced-git-operations/README.md#git-sparse-checkout-set)
- [`git ls-tree`](12-internals-and-plumbing/README.md#git-ls-tree)

### Inspect history

- [`git log`](05-history-and-comparison/README.md#git-log)
- [`git log --graph`](05-history-and-comparison/README.md#git-log-graph)
- [`git log -- path`](05-history-and-comparison/README.md#git-log-path)
- [`git show`](05-history-and-comparison/README.md#git-show)
- [`git diff A...B`](05-history-and-comparison/README.md#git-diff-three-dot)
- [`git switch --detach`](06-branch-management/README.md#git-switch-detach)
- [`git branch --merged`](06-branch-management/README.md#git-branch-merged)
- [`git reflog`](09-recovery-and-stash/README.md#git-reflog)
- [`git blame`](10-search-and-troubleshooting/README.md#git-blame)
- [`git log -S`](10-search-and-troubleshooting/README.md#git-log-pickaxe-string)
- [`git log -G`](10-search-and-troubleshooting/README.md#git-log-pickaxe-regex)
- [`git log --follow`](10-search-and-troubleshooting/README.md#git-log-follow)
- [`git bisect`](10-search-and-troubleshooting/README.md#git-bisect)
- [`git cat-file -p`](12-internals-and-plumbing/README.md#git-cat-file-pretty)
- [`git rev-list`](12-internals-and-plumbing/README.md#git-rev-list)

### Inspect index internals

- [`git ls-files --unmerged`](10-search-and-troubleshooting/README.md#git-ls-files-unmerged)
- [`git ls-files --stage`](12-internals-and-plumbing/README.md#git-ls-files-stage)

### Inspect Git objects

- [`git count-objects`](02-repository-inspection/README.md#git-count-objects)
- [`git show`](05-history-and-comparison/README.md#git-show)
- [`git cat-file -t`](12-internals-and-plumbing/README.md#git-cat-file-type)
- [`git cat-file -p`](12-internals-and-plumbing/README.md#git-cat-file-pretty)
- [`git hash-object`](12-internals-and-plumbing/README.md#git-hash-object)
- [`git ls-tree`](12-internals-and-plumbing/README.md#git-ls-tree)
- [`git rev-list`](12-internals-and-plumbing/README.md#git-rev-list)
- [`git ls-files --stage`](12-internals-and-plumbing/README.md#git-ls-files-stage)
- [`git fsck`](13-security-and-maintenance/README.md#git-fsck)

### Inspect references

- [`git show-ref`](02-repository-inspection/README.md#git-show-ref)
- [`git tag -l`](04-commits-and-tags/README.md#git-tag-list)
- [`git branch --list`](06-branch-management/README.md#git-branch-list)
- [`git fetch`](08-remotes-and-synchronization/README.md#git-fetch)
- [`git reflog`](09-recovery-and-stash/README.md#git-reflog)
- [`git symbolic-ref HEAD`](12-internals-and-plumbing/README.md#git-symbolic-ref-read)
- [`git for-each-ref`](12-internals-and-plumbing/README.md#git-for-each-ref)

### Inspect repository state

- [`git status`](02-repository-inspection/README.md#git-status)
- [`git rev-parse --show-toplevel`](02-repository-inspection/README.md#git-rev-parse-show-toplevel)
- [`git rev-parse --git-dir`](02-repository-inspection/README.md#git-rev-parse-git-dir)
- [`git rev-parse --is-bare-repository`](02-repository-inspection/README.md#git-rev-parse-is-bare)
- [`git branch --show-current`](06-branch-management/README.md#git-branch-show-current)
- [`git diff --check`](10-search-and-troubleshooting/README.md#git-diff-check)
- [`git symbolic-ref HEAD`](12-internals-and-plumbing/README.md#git-symbolic-ref-read)
- [`gh pr view`](14-platforms-and-automation/README.md#gh-pr-view)
- [`glab mr view`](14-platforms-and-automation/README.md#glab-mr-view)

### Check Git version

- [`git --version`](01-setup-and-configuration/README.md#git-version)
- [`git help`](01-setup-and-configuration/README.md#git-help)

### Integrate changes

- [`git merge`](07-merge-rebase-and-conflicts/README.md#git-merge)
- [`git merge --ff-only`](07-merge-rebase-and-conflicts/README.md#git-merge-ff-only)
- [`git merge --no-ff`](07-merge-rebase-and-conflicts/README.md#git-merge-no-ff)
- [`git merge --squash`](07-merge-rebase-and-conflicts/README.md#git-merge-squash)
- [`git merge --continue`](07-merge-rebase-and-conflicts/README.md#git-merge-continue)
- [`git rebase`](07-merge-rebase-and-conflicts/README.md#git-rebase)
- [`git pull --ff-only`](08-remotes-and-synchronization/README.md#git-pull-ff-only)
- [`git cherry-pick`](09-recovery-and-stash/README.md#git-cherry-pick)
- [`git subtree add`](11-advanced-git-operations/README.md#git-subtree-add)

### Limit checkout or clone

- [`git sparse-checkout set`](11-advanced-git-operations/README.md#git-sparse-checkout-set)
- [`git clone --filter`](11-advanced-git-operations/README.md#git-clone-filter)

### Maintain a repository

- [`git gc`](13-security-and-maintenance/README.md#git-gc)
- [`git maintenance run`](13-security-and-maintenance/README.md#git-maintenance-run)

### Manage branches

- [`git log --graph`](05-history-and-comparison/README.md#git-log-graph)
- [`git branch --list`](06-branch-management/README.md#git-branch-list)
- [`git branch NAME`](06-branch-management/README.md#git-branch-create)
- [`git branch --show-current`](06-branch-management/README.md#git-branch-show-current)
- [`git switch`](06-branch-management/README.md#git-switch)
- [`git switch -c`](06-branch-management/README.md#git-switch-create)
- [`git branch -m`](06-branch-management/README.md#git-branch-rename)
- [`git branch -d`](06-branch-management/README.md#git-branch-delete)
- [`git branch --merged`](06-branch-management/README.md#git-branch-merged)
- [`git branch --set-upstream-to`](06-branch-management/README.md#git-branch-upstream)
- [`git push --delete`](08-remotes-and-synchronization/README.md#git-push-delete)
- [`git worktree add`](11-advanced-git-operations/README.md#git-worktree-add)

### Manage repository dependencies

- [`git submodule add`](11-advanced-git-operations/README.md#git-submodule-add)
- [`git submodule update --init --recursive`](11-advanced-git-operations/README.md#git-submodule-update)
- [`git subtree add`](11-advanced-git-operations/README.md#git-subtree-add)

### Manage files

- [`git rm`](03-working-tree-and-staging/README.md#git-rm)
- [`git mv`](03-working-tree-and-staging/README.md#git-mv)

### Manage releases

- [`git tag`](04-commits-and-tags/README.md#git-tag)
- [`git tag -a`](04-commits-and-tags/README.md#git-tag-annotated)
- [`gh release create`](14-platforms-and-automation/README.md#gh-release-create)

### Manage remotes

- [`git remote add`](08-remotes-and-synchronization/README.md#git-remote-add)
- [`git push`](08-remotes-and-synchronization/README.md#git-push)
- [`git push --delete`](08-remotes-and-synchronization/README.md#git-push-delete)

### Manage tags

- [`git tag`](04-commits-and-tags/README.md#git-tag)
- [`git tag -a`](04-commits-and-tags/README.md#git-tag-annotated)
- [`git tag -d`](04-commits-and-tags/README.md#git-tag-delete)
- [`git tag -l`](04-commits-and-tags/README.md#git-tag-list)
- [`git tag -s`](13-security-and-maintenance/README.md#git-tag-sign)
- [`git verify-tag`](13-security-and-maintenance/README.md#git-verify-tag)
- [`gh release create`](14-platforms-and-automation/README.md#gh-release-create)

### Package history or files

- [`git archive`](11-advanced-git-operations/README.md#git-archive)
- [`git bundle create`](11-advanced-git-operations/README.md#git-bundle-create)

### Work in parallel

- [`git branch NAME`](06-branch-management/README.md#git-branch-create)
- [`git switch -c`](06-branch-management/README.md#git-switch-create)
- [`git worktree add`](11-advanced-git-operations/README.md#git-worktree-add)

### Protect history

- [`git branch -d`](06-branch-management/README.md#git-branch-delete)
- [`git branch --merged`](06-branch-management/README.md#git-branch-merged)
- [`git merge --ff-only`](07-merge-rebase-and-conflicts/README.md#git-merge-ff-only)
- [`git pull --ff-only`](08-remotes-and-synchronization/README.md#git-pull-ff-only)
- [`git push --delete`](08-remotes-and-synchronization/README.md#git-push-delete)
- [`git push --force-with-lease`](08-remotes-and-synchronization/README.md#git-push-force-with-lease)
- [`git revert`](09-recovery-and-stash/README.md#git-revert)
- [`git gc`](13-security-and-maintenance/README.md#git-gc)

### Recover work

- [`git switch --detach`](06-branch-management/README.md#git-switch-detach)
- [`git merge --abort`](07-merge-rebase-and-conflicts/README.md#git-merge-abort)
- [`git rebase --abort`](07-merge-rebase-and-conflicts/README.md#git-rebase-abort)
- [`git reflog`](09-recovery-and-stash/README.md#git-reflog)
- [`git cherry-pick`](09-recovery-and-stash/README.md#git-cherry-pick)
- [`git stash apply`](09-recovery-and-stash/README.md#git-stash-apply)
- [`git stash pop`](09-recovery-and-stash/README.md#git-stash-pop)
- [`git bundle create`](11-advanced-git-operations/README.md#git-bundle-create)

### Resolve conflicts

- [`git merge --abort`](07-merge-rebase-and-conflicts/README.md#git-merge-abort)
- [`git merge --continue`](07-merge-rebase-and-conflicts/README.md#git-merge-continue)
- [`git rebase --continue`](07-merge-rebase-and-conflicts/README.md#git-rebase-continue)
- [`git rebase --abort`](07-merge-rebase-and-conflicts/README.md#git-rebase-abort)
- [`git ls-files --unmerged`](10-search-and-troubleshooting/README.md#git-ls-files-unmerged)
- [`git rerere`](11-advanced-git-operations/README.md#git-rerere)

### Review changes

- [`git show`](05-history-and-comparison/README.md#git-show)
- [`git diff`](05-history-and-comparison/README.md#git-diff)
- [`git diff --cached`](05-history-and-comparison/README.md#git-diff-cached)
- [`git diff A B`](05-history-and-comparison/README.md#git-diff-two-revisions)
- [`git diff --stat`](05-history-and-comparison/README.md#git-diff-stat)
- [`git diff A...B`](05-history-and-comparison/README.md#git-diff-three-dot)
- [`git range-diff`](05-history-and-comparison/README.md#git-range-diff)
- [`git rebase -i`](07-merge-rebase-and-conflicts/README.md#git-rebase-interactive)
- [`git diff --check`](10-search-and-troubleshooting/README.md#git-diff-check)
- [`gh pr create`](14-platforms-and-automation/README.md#gh-pr-create)
- [`gh pr view`](14-platforms-and-automation/README.md#gh-pr-view)
- [`gh pr checks`](14-platforms-and-automation/README.md#gh-pr-checks)
- [`glab mr create`](14-platforms-and-automation/README.md#glab-mr-create)
- [`glab mr view`](14-platforms-and-automation/README.md#glab-mr-view)

### Rewrite local history

- [`git commit --amend`](04-commits-and-tags/README.md#git-commit-amend)
- [`git commit --fixup`](04-commits-and-tags/README.md#git-commit-fixup)
- [`git range-diff`](05-history-and-comparison/README.md#git-range-diff)
- [`git rebase`](07-merge-rebase-and-conflicts/README.md#git-rebase)
- [`git rebase -i`](07-merge-rebase-and-conflicts/README.md#git-rebase-interactive)
- [`git rebase --continue`](07-merge-rebase-and-conflicts/README.md#git-rebase-continue)
- [`git push --force-with-lease`](08-remotes-and-synchronization/README.md#git-push-force-with-lease)
- [`git reset`](09-recovery-and-stash/README.md#git-reset)

### Search content

- [`git grep`](10-search-and-troubleshooting/README.md#git-grep)
- [`git log -S`](10-search-and-troubleshooting/README.md#git-log-pickaxe-string)
- [`git log -G`](10-search-and-troubleshooting/README.md#git-log-pickaxe-regex)
- [`git log --follow`](10-search-and-troubleshooting/README.md#git-log-follow)

### Shelve work temporarily

- [`git stash push`](09-recovery-and-stash/README.md#git-stash-push)
- [`git stash apply`](09-recovery-and-stash/README.md#git-stash-apply)
- [`git stash pop`](09-recovery-and-stash/README.md#git-stash-pop)

### Simulate collaboration

- [`git init --bare`](01-setup-and-configuration/README.md#git-init-bare)

### Stage changes

- [`git add`](03-working-tree-and-staging/README.md#git-add)
- [`git add -A`](03-working-tree-and-staging/README.md#git-add-all)
- [`git add -u`](03-working-tree-and-staging/README.md#git-add-update)
- [`git add -p`](03-working-tree-and-staging/README.md#git-add-patch)
- [`git commit -a`](04-commits-and-tags/README.md#git-commit-all)
- [`git diff --cached`](05-history-and-comparison/README.md#git-diff-cached)
- [`git merge --squash`](07-merge-rebase-and-conflicts/README.md#git-merge-squash)

### Switch work context

- [`git switch`](06-branch-management/README.md#git-switch)
- [`git switch -c`](06-branch-management/README.md#git-switch-create)
- [`git switch --detach`](06-branch-management/README.md#git-switch-detach)
- [`git stash push`](09-recovery-and-stash/README.md#git-stash-push)

### Synchronize repositories

- [`git branch --set-upstream-to`](06-branch-management/README.md#git-branch-upstream)
- [`git clone`](08-remotes-and-synchronization/README.md#git-clone)
- [`git fetch`](08-remotes-and-synchronization/README.md#git-fetch)
- [`git pull --ff-only`](08-remotes-and-synchronization/README.md#git-pull-ff-only)
- [`git push`](08-remotes-and-synchronization/README.md#git-push)
- [`git push --force-with-lease`](08-remotes-and-synchronization/README.md#git-push-force-with-lease)
- [`git submodule update --init --recursive`](11-advanced-git-operations/README.md#git-submodule-update)

### Troubleshoot configuration

- [`git config --list --show-origin`](01-setup-and-configuration/README.md#git-config-show-origin)
- [`git credential reject`](13-security-and-maintenance/README.md#git-credential-reject)

### Undo changes

- [`git restore`](03-working-tree-and-staging/README.md#git-restore)
- [`git tag -d`](04-commits-and-tags/README.md#git-tag-delete)
- [`git reset`](09-recovery-and-stash/README.md#git-reset)
- [`git revert`](09-recovery-and-stash/README.md#git-revert)

### Unstage changes

- [`git restore --staged`](03-working-tree-and-staging/README.md#git-restore-staged)
- [`git reset`](09-recovery-and-stash/README.md#git-reset)

### Verify integrity

- [`git fsck`](13-security-and-maintenance/README.md#git-fsck)

### Verify signatures

- [`git commit -S`](13-security-and-maintenance/README.md#git-commit-sign)
- [`git tag -s`](13-security-and-maintenance/README.md#git-tag-sign)
- [`git verify-commit`](13-security-and-maintenance/README.md#git-verify-commit)
- [`git verify-tag`](13-security-and-maintenance/README.md#git-verify-tag)


---

<!-- navigation-footer -->
[Previous](../git-internals/README.md) · [Index](../docs/learning-path.md) · [Next](../practical-projects/README.md)
<!-- /navigation-footer -->
