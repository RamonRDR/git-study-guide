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

Install VS Code from its official page if desired; a plain-text editor also works. Use File > Open Folder to open ONLY the lab's repo subfolder. If configured, `code .` from the dedicated lab terminal is an alternative. Source Control can show changes, but the editor's process may not inherit your isolated Git environment. Use it only to edit text and inspect changes; do not stage, commit or run Git from the editor or its integrated terminal. Return to the original dedicated shell for all Git commands. Verify there:

```text
git rev-parse --show-toplevel
git status
```

Source Control should detect the repository; UI labels may vary. GUI steps are documentation-based, not run in CI. If the original shell was closed, repeat chapter 03 in a fresh lab.

## Common mistakes and safety

Do not click Publish, Sync, Clone or Initialize Repository for this lab. If Git is not detected, check `git --version` in the dedicated lab terminal and restart the editor if needed. Only trust folders you created or reviewed; avoid unknown extensions and tasks.

## Exercise and self-check

Find Source Control and terminal, or use a plain-text editor plus terminal. Hint: compare the repository root. Pass if you can explain why both interfaces reflect the same Git state. Professional habit: inspect visually and verify with commands.

## Quick reference

- `git rev-parse --show-toplevel`
- `git status`

## Official sources

- [https://code.visualstudio.com/download](https://code.visualstudio.com/download)
- [https://code.visualstudio.com/docs/sourcecontrol/quickstart](https://code.visualstudio.com/docs/sourcecontrol/quickstart)
- [https://git-scm.com/docs/git-gui](https://git-scm.com/docs/git-gui)
