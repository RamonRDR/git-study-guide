# Terminal and help

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../01-install-git/README.md) · [Index](../README.md) · [Next](../03-first-repository/README.md)
<!-- /navigation -->

**Level:** beginner · **Estimated time:** 20 min

**Prerequisites:** [Install Git](../01-install-git/README.md)

**Objective:** Navigate directories and discover command help.

## What and why

The current directory is where relative paths begin. A repository is a project directory with Git metadata and history. Git usually discovers it from the current directory. Commands consist of a program, operation and optional arguments; know your location before changing anything.

## Practice

Try these read-only navigation/help operations. PowerShell and Bash/Zsh have different syntax.

```powershell
Get-Location
Get-ChildItem
Set-Location $HOME
```

```bash
pwd
ls
cd "$HOME"
```

```text
git --version
git status -h
git help status
```

Short help lists options; full help may open a manual or browser. Press q to quit a pager (scrollable text viewer).

## Common mistakes and safety

Do not copy prompt symbols such as `$` or `PS>`. Quote paths with spaces. `git status` outside a repo normally reports no repository; that is not an installation failure. Do not share screenshots containing private paths.

## Exercise and self-check

Find your current folder and look up `git add -h`. Hint: distinguish shell and Git. Pass if you find one option without modifying files. Professional habit: verify the project location before running commands.

## Quick reference

- `git --version`
- `git status -h`
- `git help status`

## Official sources

- [https://git-scm.com/docs/git-help](https://git-scm.com/docs/git-help)
- [https://git-scm.com/docs/gittutorial](https://git-scm.com/docs/gittutorial)
