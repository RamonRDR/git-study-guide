# Reflog and lost commit recovery

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../04-revert/README.md) · [Index](../README.md) · [Next](../06-stash/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 30 min

**Prerequisites:** [Isolated lab](../../getting-started/03-first-repository/README.md) · [First commit](../../getting-started/05-first-commit/README.md) · [Merge and conflicts](../../merge-and-conflicts/README.md) · [Remotes](../../remote-repositories/README.md) · [Revert without rewriting history](../04-revert/README.md)

**Objective:** Find a displaced commit in the local reflog and recover it with a new branch.

## What and why

Reflog records updates of local refs, including HEAD movements. Unlike git log, which walks commit ancestry, reflog can show tips no longer reachable from the current branch. `HEAD@{1}` refers to a previous HEAD value, not necessarily the parent; quote it in shells. Entries are local, can expire, and unreachable objects can later be collected. Diagram: main C1; previously main C2 -> C1; reflog records C2 even though main no longer points there. Creating a rescue branch at a verified commit makes it reachable again.

## Practice

Start a NEW independent disposable lab using the linked setup and first-commit lessons. Keep the dedicated Bash or PowerShell shell in the recorded repo directory, with system/global Git config isolated, inherited Git variables cleared and empty templates. Use Git 2.40 or later. The initial main must contain exactly one commit with note.txt = practice, no remotes and clean status. Run every command individually. Before any mutation, repeat the inspection below: root must be the recorded disposable repo, branch must be the one specified, remotes empty, status exactly as described; both identities must begin with `Study Guide Example <learner@example.invalid>`. Before every commit also inspect staged changes and both identities. Stop on unexpected output or failure. Never execute these labs in the guide or a real project.

```text
git rev-parse --show-toplevel
git branch --show-current
git remote -v
git status --short
git diff
git diff --cached
git log --oneline --all --graph --decorate
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Edit note.txt in a plain-text editor to exactly one line `rescue me` with final newline. Save, then return to the dedicated shell.

```text
git add -- note.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Only if the staged diff and both identities are correct, continue:

```text
git commit -m "docs: add rescue note"
git rev-parse HEAD HEAD^
git status --short
git reflog -n 3
```

Record C2 privately. Confirm root, clean main, no remote, exactly two commits, and all data disposable. The next command intentionally moves main away from C2 and resets index/files; do not use it in real work.

```text
git reset --hard HEAD^
git log --oneline
git reflog -n 4
git show 'HEAD@{1}':note.txt
git rev-parse 'HEAD@{1}'
```

Expected log only C1, reflog includes C2, show returns rescue me. The selector is valid only if it still resolves to the recorded C2; if not, inspect reflog and choose the correct full ID rather than guessing. After verification create a rescue branch:

```text
git branch rescue/note 'HEAD@{1}'
git show rescue/note:note.txt
git log --all --oneline --graph
git merge --ff-only rescue/note
git rev-parse HEAD rescue/note
git status --short
```

Expected both refs at C2, original ID recovered, clean status. Professional use: preserve a candidate recovery ref before attempting further changes; inspect content and integrate only after review.

After the exercise, close editors and the dedicated shell. Delete only the exact recorded temporary parent using the file manager if no longer needed; never delete the guide, home or work repository.

## Common mistakes and safety

Reflog is not a remote backup and cannot promise recovery. Do not run reflog expire, gc or destructive cleanup in a recovery incident; preserve independent copies. Never committed/recorded content may be unavailable.

## Exercise and self-check

Why does git log miss C2 after reset but reflog can find it? Answer: ancestry versus ref movement. Pass if the rescued ID equals the original C2, not just its content.

## Quick reference

- `git reflog`
- `git show COMMIT`
- `git branch rescue/note COMMIT`

## Official sources

- [Git: git-reflog](https://git-scm.com/docs/git-reflog)
- [Git: git-reset](https://git-scm.com/docs/git-reset)
- [Git: git-branch](https://git-scm.com/docs/git-branch)
- [Git: git-gc](https://git-scm.com/docs/git-gc)

---

<!-- navigation-footer -->
[Previous](../04-revert/README.md) · [Index](../README.md) · [Next](../06-stash/README.md)
<!-- /navigation-footer -->
