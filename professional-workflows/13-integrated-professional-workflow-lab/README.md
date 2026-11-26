# Integrated professional workflow lab

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../12-release-management/README.md) · [Index](../README.md) · —
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 60 min

**Prerequisites:** [CI/CD](../../ci-cd/README.md) · [Release management](../12-release-management/README.md)

**Objective:** Verify a safe local workflow from specification to tag.

## What and why

This offline lab connects SDD, a red/green demonstration, feature branch, diff review, Conventional Commits, integration and a local annotated tag. For this simplified exercise, the catalog contract explicitly allows the existing status field to change from draft to ready; assume a new backward-compatible readiness capability and a hypothetical previous release 1.0.0, so the example label is 1.1.0. No previous tag is required. The check asserts one exact line, not full application behavior. The first commit represents the baseline, the second the scoped change. Fast-forward is chosen for the local exercise because main has not diverged; actual guide PRs use authorized squash merge. No hosted PR, review, deployment or publication is simulated as a real platform event.

## Practice

Prerequisites: Git 2.28+ and Bash with mktemp/grep (Linux, macOS or Git Bash on Windows); use an ordinary clean shell, never the guide repository. Write R1/AC1 from chapter 09 before running. Execute the block in a disposable shell; stop on unexpected output. It creates a new temporary directory, isolates normal Git global/system config, uses fictional identity and leaves the sandbox for inspection. Expected: red message, staged one-line diff, two commits with main and tag at second commit, final PASS. Record the path, checks and limitations as a mock PR. Remove the sandbox later using a file manager after verifying its printed path. Role-play a separate reviewer and release approver; no real approval is inferred.

```bash
(
  set -eu
  sandbox=$(mktemp -d)
  printf 'Sandbox: %s\n' "$sandbox"
  unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE GIT_COMMON_DIR GIT_CONFIG_PARAMETERS
  export GIT_CONFIG_NOSYSTEM=1 GIT_CONFIG_GLOBAL="$sandbox/global-config" GIT_CONFIG_COUNT=0
  git init -b main "$sandbox/catalog"
  cd "$sandbox/catalog"
  git config user.name 'Catalog Learner'
  git config user.email 'learner@example.invalid'
  git config commit.gpgsign false
  git config tag.gpgsign false
  printf '%s\n' 'status: draft' > catalog.txt
  git add catalog.txt
  git commit -m 'chore: initialize catalog'
  git switch -c feat/ready-catalog
  if grep -Fxq 'status: ready' catalog.txt; then
    exit 1
  fi
  printf '%s\n' 'RED: ready line absent'
  printf '%s\n' 'status: ready' > catalog.txt
  grep -Fxq 'status: ready' catalog.txt
  git diff --check
  git add catalog.txt
  git diff --cached
  git commit -m 'feat: expose catalog readiness'
  git switch main
  test "$(cat catalog.txt)" = 'status: draft'
  git merge --ff-only feat/ready-catalog
  git tag -a v1.1.0 -m 'Release 1.1.0'
  test "$(git rev-parse 'v1.1.0^{commit}')" = "$(git rev-parse HEAD)"
  test -z "$(git status --porcelain)"
  grep -Fxq 'status: ready' catalog.txt
  git log --oneline --decorate -2
  printf '%s\n' 'PASS: integrated tagged clean revision'
)
```

## Risks and recovery

No remote, push, real release or credentials are used. Do not substitute a real path, configure a remote or copy commands into a production repository. This is not a hardened sandbox against a malicious shell environment. If a command fails, inspect the temporary repo with status and log; do not reset or force a merge. Before integration, the read-only diff is a practice review, not independent sign-off. Optional refactor exercise: extract the check into a function in a separate disposable shell and verify equivalent exit statuses; the supplied block demonstrates red/green, not a full refactoring cycle.

## Exercise and self-check

Pass if initial draft does not satisfy the check, ready does, main is unchanged until integration, the tag resolves to HEAD, status is clean and no remote exists. Explain why a passing local exercise does not prove a hosted CI, formal review or deployment. Compare the hypothetical release version to the contract in chapter 07.

## Quick reference

`git status` / `git diff --cached` / `git merge --ff-only` / `git tag -a`

## Sources

- <https://git-scm.com/docs/gitworkflows>
- <https://git-scm.com/docs/git-merge>
- <https://git-scm.com/docs/git-tag>
- <https://www.conventionalcommits.org/en/v1.0.0/>
- <https://semver.org/spec/v2.0.0.html>
