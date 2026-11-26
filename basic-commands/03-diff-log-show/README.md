# Compare and inspect history

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../02-status-add-commit/README.md) · [Index](../README.md) · [Next](../04-move-and-remove/README.md)
<!-- /navigation -->

**Level:** beginner · **Estimated time:** 35 min

**Prerequisites:** [Inspect, stage and commit](../02-status-add-commit/README.md)

**Objective:** Choose the right diff baseline and inspect recorded history.

## What and why

git diff compares working tree to index for tracked paths; --cached (also --staged) compares index to HEAD (or empty tree before the first commit); git diff HEAD compares tracked working contents to HEAD. Untracked files are not shown by ordinary diff. A diff uses - for removed lines and + for added lines; context lines explain placement. git log lists commits with --oneline for compact display and -n to limit; git show displays an object such as a commit with its patch or a path at a commit.

## Practice

Continue from chapter 02. Edit note.txt to second and save with a final newline, then stage it:

```text
git add -- note.txt
```

Now edit note.txt to third and save without staging. Inspect:

```text
git diff -- note.txt
git diff --cached -- note.txt
git diff HEAD -- note.txt
git log -1 --oneline
git show --stat HEAD
git show HEAD:note.txt
git show :note.txt
```

Expected: plain diff second -> third, cached practice -> second, HEAD practice -> third. Log and show are read-only; HEAD content practice, index second. If a pager opens, q exits. Now stage third, inspect cached diff and effective identities; if correct commit:

```text
git add -- note.txt
git diff --cached -- note.txt
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Stop on unexpected output or nonfictional identities. Then:

```text
git commit -m "docs: update note"
git log -2 --oneline
git diff HEAD~1 HEAD -- note.txt
git show HEAD:note.txt
```

HEAD~1 means first parent of HEAD (here one commit back); comparing the two commits shows practice -> third. Stored content third; draft.txt remains untracked.

## Common mistakes and safety

Do not treat an empty plain diff as proof that nothing is staged or untracked. Check status and cached diff too. If history is shorter than expected, do not invent IDs; inspect log.

## Exercise and self-check

Which diff shows the next commit's changes? Answer: --cached. Which shows all tracked working changes against last commit? git diff HEAD. Pass if you identify the three baselines. Professional use: review exactly what will be committed.

## Quick reference

- `git diff`
- `git log`
- `git show`
- `gitrevisions`

## Official sources

- [Git: git-diff](https://git-scm.com/docs/git-diff)
- [Git: git-log](https://git-scm.com/docs/git-log)
- [Git: git-show](https://git-scm.com/docs/git-show)
- [Git: gitrevisions](https://git-scm.com/docs/gitrevisions)

---

<!-- navigation-footer -->
[Previous](../02-status-add-commit/README.md) · [Index](../README.md) · [Next](../04-move-and-remove/README.md)
<!-- /navigation-footer -->
