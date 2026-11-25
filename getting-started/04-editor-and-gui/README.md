# VS Code and graphical interfaces

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../03-first-repository/README.md) · [Index](../README.md) · [Next](../05-first-commit/README.md)
<!-- /navigation -->

**Level:** beginner · **Estimated time:** 20 min

**Prerequisites:** [First repository and configuration](../03-first-repository/README.md)

**Objective:** Open the lab in an editor and compare GUI and terminal.

## What and why

An editor changes files; Git records selected content. VS Code includes Git support but uses the separate Git installation for local operations. Source Control displays changes and lets you stage (select content for a commit) and commit (record selected content). Git GUI is another optional client if installed. Neither requires a hosting account for local work.

## Practice

Install VS Code from the official page if desired; any plain-text editor works. Use File > Open Folder to open ONLY your lab. If configured, `code .` is an alternative. Open Terminal > New Terminal and check root and status.

```text
git rev-parse --show-toplevel
git status
```

Source Control should detect the repository. UI labels may vary. Compare changes there in the next chapter. GUI steps are documentation-based, not run in CI.

## Common mistakes and safety

Do not click Publish, Sync, Clone or Initialize Repository for this lab. If Git is not detected, check `git --version` in the integrated terminal and restart the editor. Only trust folders you created or reviewed; avoid unknown extensions and tasks.

## Exercise and self-check

Find Source Control and terminal, or use a plain-text editor plus terminal. Hint: compare the repository root. Pass if you can explain why both interfaces reflect the same Git state. Professional habit: inspect visually and verify with commands.

## Quick reference

- `git rev-parse --show-toplevel`
- `git status`

## Official sources

- [https://code.visualstudio.com/download](https://code.visualstudio.com/download)
- [https://code.visualstudio.com/docs/sourcecontrol/quickstart](https://code.visualstudio.com/docs/sourcecontrol/quickstart)
- [https://git-scm.com/docs/git-gui](https://git-scm.com/docs/git-gui)
