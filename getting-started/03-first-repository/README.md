# First repository and configuration

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../02-terminal-and-help/README.md) · [Index](../README.md) · [Next](../04-editor-and-gui/README.md)
<!-- /navigation -->

**Level:** beginner · **Estimated time:** 30 min

**Prerequisites:** [Terminal and help](../02-terminal-and-help/README.md)

**Objective:** Create a disposable repository and configure fictional local identity.

## What and why

A local repository stores metadata and history in a hidden `.git` directory. A branch is a named line of development; main is our initial name. Init creates metadata, not a commit. Identity is recorded author information, not authentication. System settings apply broadly, global to your user and local to this repository; local generally overrides global.

## Practice

Create a fresh temporary folder, not the guide or an existing project. Choose your shell.

```powershell
$lab = Join-Path ([System.IO.Path]::GetTempPath()) ("git-study-" + [guid]::NewGuid().ToString("N"))
New-Item -ItemType Directory -Path $lab -ErrorAction Stop
Set-Location $lab -ErrorAction Stop
Get-Location
```

```bash
lab=$(mktemp -d) && cd "$lab" && pwd
```

Stop if creation or navigation fails. In the new empty folder, `git rev-parse --show-toplevel` must fail (outside any repo). If it succeeds, choose another folder. Then run individually:

```text
git init --initial-branch=main
git config --local user.name "Study Guide Example"
git config --local user.email "learner@example.invalid"
git config --local commit.gpgsign false
git config --local --get user.name
git config --local --get user.email
git rev-parse --show-toplevel
git status
```

Expected: fictional identity, new folder, branch main and no commits. Signing is disabled only in this disposable lab; do not change real project signing policies. Keep the lab for the following lessons.

## Common mistakes and safety

Never initialize inside the guide, home or work repository. Do not delete `.git` to troubleshoot. A real email can become public when sharing commits. Check only local keys, not a full config dump. Existing hooks (automatic scripts) or settings may affect manual practice; CI isolates configuration. If unsure, stop and create a fresh lab.

## Exercise and self-check

Verify root, name and email. Pass if identity is fictional, branch main and history empty. Hint: `git config --local --get user.email`. Professional use: separate work and personal repository identities.

## Quick reference

- `git rev-parse --show-toplevel`
- `git init --initial-branch=main`
- `git config --local --get user.email`
- `git status`

## Official sources

- [https://git-scm.com/docs/git-init](https://git-scm.com/docs/git-init)
- [https://git-scm.com/docs/git-config](https://git-scm.com/docs/git-config)
- [https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)
