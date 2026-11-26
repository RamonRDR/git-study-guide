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

Open a new dedicated PowerShell or Bash terminal solely for this lab (on macOS/Zsh, start Bash with `bash` first). Keep it open through module 01. The commands below clear inherited Git environment overrides in this shell only and create a fresh parent folder containing a repository folder, empty global config and empty template directory. System/global config and inherited author/committer overrides are excluded; the empty template avoids inherited hooks. They do not edit your real Git configuration. Use a maintained Git version 2.40 or newer for this isolation setup. Choose one shell; stop at any error.

```powershell
Get-ChildItem Env: | Where-Object { $_.Name -like 'GIT_*' } | ForEach-Object {
    Remove-Item -LiteralPath ("Env:" + $_.Name) -ErrorAction Stop
}
$lab = Join-Path ([System.IO.Path]::GetTempPath()) ("git-study-" + [guid]::NewGuid().ToString("N"))
New-Item -ItemType Directory -Path $lab -ErrorAction Stop
New-Item -ItemType Directory -Path (Join-Path $lab "repo"), (Join-Path $lab "template") -ErrorAction Stop
$env:GIT_CONFIG_GLOBAL = Join-Path $lab "gitconfig"
New-Item -ItemType File -Path $env:GIT_CONFIG_GLOBAL -ErrorAction Stop
$env:GIT_CONFIG_NOSYSTEM = "1"
$env:GIT_TEMPLATE_DIR = Join-Path $lab "template"
$env:GIT_TERMINAL_PROMPT = "0"
Set-Location (Join-Path $lab "repo") -ErrorAction Stop
Get-Location
```

```bash
for name in $(compgen -e); do
    case "$name" in GIT_*) unset "$name" ;; esac
done
lab=$(mktemp -d) &&
mkdir "$lab/repo" "$lab/template" &&
touch "$lab/gitconfig" &&
export GIT_CONFIG_GLOBAL="$lab/gitconfig" GIT_CONFIG_NOSYSTEM=1 &&
export GIT_TEMPLATE_DIR="$lab/template" GIT_TERMINAL_PROMPT=0 &&
cd "$lab/repo" && pwd
```

Record the parent folder path privately for cleanup. In its new empty repo subfolder, `git rev-parse --show-toplevel` must fail before initialization; if it succeeds, stop and choose another lab. Run individually:

```text
git init --initial-branch=main
git config --local user.name "Study Guide Example"
git config --local user.email "learner@example.invalid"
git config --local commit.gpgsign false
git config --local --get user.name
git config --local --get user.email
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
git rev-parse --show-toplevel
git status
```

Both effective identities must begin with `Study Guide Example <learner@example.invalid>`; timestamps/time zones vary. If either differs or any command fails, stop; do not commit. Expected: root is the repo subfolder, main has no commits. Keep the same dedicated shell, and do not use it for other repositories. Signing is disabled only in this disposable lab; do not change real project policy.

## Common mistakes and safety

Never initialize inside the guide, home or work repository. Do not delete `.git` to troubleshoot. A real email can become public when sharing commits. Check only local keys, not a full config dump. Local user settings alone are insufficient: inherited author/committer settings can override them. Hooks are automatic scripts. Use the dedicated isolated shell; if isolation fails, close it and restart the lab rather than changing personal settings.

## Exercise and self-check

Verify root, name and email. Pass if identity is fictional, branch main and history empty. Hint: `git var GIT_AUTHOR_IDENT` / `git var GIT_COMMITTER_IDENT`. Professional use: separate work and personal repository identities.

## Quick reference

- `git rev-parse --show-toplevel`
- `git init --initial-branch=main`
- `git config --local --get user.email`
- `git var GIT_AUTHOR_IDENT`
- `git var GIT_COMMITTER_IDENT`
- `git status`

## Official sources

- [https://git-scm.com/docs/git-init](https://git-scm.com/docs/git-init)
- [https://git-scm.com/docs/git-config](https://git-scm.com/docs/git-config)
- [https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)

- [Git: git-var](https://git-scm.com/docs/git-var)

---

<!-- navigation-footer -->
[Previous](../02-terminal-and-help/README.md) · [Index](../README.md) · [Next](../04-editor-and-gui/README.md)
<!-- /navigation-footer -->
