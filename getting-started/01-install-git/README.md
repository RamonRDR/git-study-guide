# Install Git

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
— · [Index](../README.md) · [Next](../02-terminal-and-help/README.md)
<!-- /navigation -->

**Level:** beginner · **Estimated time:** 25 min

**Prerequisites:** None; no programming required.

**Objective:** Install Git and verify the version.

## What and why

Git records selected versions of files locally. It is neither an editor nor a programming language. A terminal accepts commands, and its shell (PowerShell, Bash or Zsh) interprets them. Install Git once per environment, not once per project.

## Practice

Open PowerShell on Windows or Terminal on Linux/macOS. Try `git --version`. If Git is already present, use a maintained version at least 2.40. Otherwise choose ONLY your OS:

Windows: use the official installer for your architecture, or WinGet if available. Reopen the terminal.

```powershell
winget install --id Git.Git -e --source winget
```

Debian/Ubuntu (with permission):

```bash
sudo apt update
sudo apt install git
```

Fedora:

```bash
sudo dnf install git
```

macOS: request Apple's command-line tools if Git is missing, or use Homebrew if already installed and trusted; choose one.

```bash
xcode-select --install
```

```bash
brew install git
```

Re-run `git --version`. Expected: a version, not a command-not-found error. Installation steps are documentation-verified, not tested on fresh machines.

## Common mistakes and safety

Do not run all installers or use elevated privileges for ordinary Git commands. If lookup fails, reopen the terminal and check PATH (directories searched for programs). Ask IT on managed devices.

## Exercise and self-check

Identify your OS and shell. Hint: install only if missing. Pass if `git --version` works and you can explain Git versus terminal. In professional bug reports, record the Git version.

## Quick reference

- `git --version`

## Official sources

- [https://git-scm.com/install/](https://git-scm.com/install/)
- [https://git-scm.com/install/win](https://git-scm.com/install/win)
- [https://git-scm.com/install/linux.html](https://git-scm.com/install/linux.html)
- [https://git-scm.com/install/mac](https://git-scm.com/install/mac)

---

<!-- navigation-footer -->
— · [Index](../README.md) · [Next](../02-terminal-and-help/README.md)
<!-- /navigation-footer -->
