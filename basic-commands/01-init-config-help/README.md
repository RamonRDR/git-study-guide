# Initialize, configure and ask for help

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
— · [Index](../README.md) · [Next](../02-status-add-commit/README.md)
<!-- /navigation -->

**Level:** beginner · **Estimated time:** 25 min

**Prerequisites:** [Getting Started](../../getting-started/README.md) · [Git Architecture](../../git-architecture/README.md)

**Objective:** Distinguish repository initialization, configuration scopes and help commands.

## What and why

git init creates repository metadata, normally in .git; --initial-branch sets the initial branch name (Git 2.28+). A second init in a repository normally reinitializes it without discarding existing history, but do not use it as a repair tool. git config reads/writes settings: system, global, local and command-level overrides have different scope. Use --local for this lab and -c key=value for a single invocation. git help provides full help; command -h provides short usage (it may return nonzero).

## Practice

Start a NEW isolated disposable lab following module 00 chapter 03, including git init and fictional effective identities, but do not create a commit yet. In its repo subfolder run:

```text
git config --local --get user.name
git config --local --get user.email
git config --show-origin --get user.email
git config --local core.autocrlf false
git config --local --get core.autocrlf
git -c core.autocrlf=true config --get core.autocrlf
git config --local --get core.autocrlf
git status -h
git help init
```

Expected: fictional identity, local setting false; invocation override true, then local setting still false. --show-origin displays the source path; do not share private paths. Help does not change the repo; quit the pager with q if needed. core.autocrlf controls automatic line-ending conversion; false avoids that conversion for these plain-text exercises. No global settings changed.

## Common mistakes and safety

Use the dedicated shell only for this lab. Verify Git 2.40+ per module 00 isolation requirements. Do not run init in home or work; avoid --global/--system and dumping all config. If unexpected origin or identity, restart the isolated lab rather than modifying real settings.

## Exercise and self-check

Predict the three core.autocrlf outputs. Answer: false, true, false. Pass if you explain why -c does not persist. Professional use: check an individual setting's origin before troubleshooting.

## Quick reference

- `git init`
- `git config`
- `git help`
- `git`

## Official sources

- [Git: git-init](https://git-scm.com/docs/git-init)
- [Git: git-config](https://git-scm.com/docs/git-config)
- [Git: git-help](https://git-scm.com/docs/git-help)
- [Git: git](https://git-scm.com/docs/git)
