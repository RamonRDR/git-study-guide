# Switching safely and branch naming

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../02-start-points-and-comparison/README.md) · [Index](../README.md) · [Next](../04-safe-local-deletion/README.md)
<!-- /navigation -->

**Level:** beginner · **Estimated time:** 25 min

**Prerequisites:** [Start points and branch comparison](../02-start-points-and-comparison/README.md)

**Objective:** Recognize a blocked switch and rename a branch without losing commits.

## What and why

Git may preserve compatible local changes across switch; it normally refuses a switch that would overwrite conflicting edits or obstructing untracked files. The working tree and index are not private per branch in one checkout. `git branch -m NEW` renames the current branch; `git branch -m OLD NEW` renames another local branch. It preserves the commit reference and moves associated branch configuration/reflog when present. A reflog records local reference movements; details come later. Names such as feat/note, fix/typo and docs/overview communicate intent; team conventions are not Git requirements. `git check-ref-format --branch NAME` validates branch-name syntax (not availability). Avoid spaces, reserved sequences and case-only differences for portability.

## Practice

In the same lab, start on docs/overview with clean status. Switch to feat/note, record its ID, rename it, and check the ID again:

```text
git status --short
git switch feat/note
git rev-parse HEAD
git check-ref-format --branch feat/note-revision
git branch -m feat/note-revision
git branch --show-current
git rev-parse HEAD
git branch --list
```

Expected: same ID, new name feat/note-revision, old name absent. Edit note.txt from feature to unfinished and save without staging. Inspect, then intentionally attempt a switch in this disposable lab:

```text
git status --short
git diff -- note.txt
git switch main
```

Expected refusal: main contains practice, so the switch would overwrite your changed note. Confirm still on feat/note-revision and contents unfinished. If the switch succeeds unexpectedly, stop and inspect; never force. To continue the lab, manually change ONLY the invented note.txt back to feature with its original newline (you are intentionally discarding the dummy edit, not real work). Verify clean status, then switch:

```text
git branch --show-current
git status --short
```

Only after status is empty:

```text
git switch main
git show HEAD:note.txt
git status --short
```

## Common mistakes and safety

Do not use switch --discard-changes or branch -M here. Do not erase real edits to make switching work. Preserve them in an intentional commit on the appropriate branch or use a reviewed recovery technique later. Never rename a shared branch without coordinating; remote rename/tracking is deferred to module 06.

## Exercise and self-check

Why did switch fail? Answer: it would overwrite a tracked local edit. Does rename create a commit? No. Pass if current name and ID are checked and no edit is lost unintentionally. Professional use: agree on portable descriptive branch names.

## Quick reference

`git branch -m OLD NEW`: rename; `git check-ref-format --branch NAME`: syntax; `git status --short`: inspect before switching.

## Official sources

- [Git: git-switch](https://git-scm.com/docs/git-switch)
- [Git: git-branch](https://git-scm.com/docs/git-branch)
- [Git: git-check-ref-format](https://git-scm.com/docs/git-check-ref-format)
