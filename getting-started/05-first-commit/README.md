# Your first commit

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../04-editor-and-gui/README.md) · [Index](../README.md) · —
<!-- /navigation -->

**Level:** beginner · **Estimated time:** 35 min

**Prerequisites:** [VS Code and graphical interfaces](../04-editor-and-gui/README.md)

**Objective:** Stage and commit a text file; inspect the resulting local history.

## What and why

A commit records a snapshot of staged contents with history information. The working tree contains editable files; the staging area (index) holds the content selected for the next commit; the local repository stores committed history. An edit after staging does not automatically change the index. A commit is not an upload.

## Practice

Use the same disposable lab, verify root and status, and create a new note.txt with one line practice plus newline. These commands overwrite files; do not run them if note.txt already exists.

```powershell
Set-Content -Path note.txt -Value "practice" -Encoding ascii
```

```bash
printf 'practice\n' > note.txt
```

Run separately; inspect each result:

```text
git status
git add note.txt
git status
git diff --cached
git commit -m "docs: add note"
git status
git log -1 --oneline
git show HEAD:note.txt
```

Before add: untracked file; after add: staged new file; cached diff: practice line; after commit: clean status, one commit with message, stored practice. HEAD identifies the current checkout, normally the current branch. Hashes, dates, localized output and line-ending warnings vary. Flow: working file -> add -> index -> commit -> local history.

## Common mistakes and safety

If identity is missing, inspect local configuration. If nothing is staged, inspect status and stage only the intended file. Avoid `git add .` in unfamiliar projects. If wrong contents were staged, stop and create a fresh lab rather than using destructive commands. Do not bypass organizational signing or hook policies. Keep the lab for module 01; after that close the editor, leave the lab with `cd $HOME` (PowerShell) or `cd "$HOME"` (Bash/Zsh), then delete only the exact temporary folder using a file manager if no longer needed.

## Exercise and self-check

Predict status after writing, add and commit. Hint: follow the three locations. Pass when log has your message, show returns practice and status is clean. Explain why an edit after add needs another add to be included. Professional habit: review staged diff before recording changes.

## Quick reference

- `git status`
- `git add note.txt`
- `git diff --cached`
- `git commit -m "docs: add note"`
- `git log -1 --oneline`
- `git show HEAD:note.txt`

## Official sources

- [https://git-scm.com/docs/gittutorial](https://git-scm.com/docs/gittutorial)
- [https://git-scm.com/docs/git-add](https://git-scm.com/docs/git-add)
- [https://git-scm.com/docs/git-commit](https://git-scm.com/docs/git-commit)
- [https://git-scm.com/docs/git-status](https://git-scm.com/docs/git-status)
