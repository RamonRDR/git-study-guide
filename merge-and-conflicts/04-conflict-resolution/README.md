# Resolve and abort merge conflicts

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../03-merge-commit/README.md) · [Index](../README.md) · [Next](../05-squash-merge/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 45 min

**Prerequisites:** [Divergence and merge commits](../03-merge-commit/README.md)

**Objective:** Inspect unmerged index stages, abort safely, then resolve and complete a merge.

## What and why

A text conflict can occur when both branches edit the same line incompatibly. Git pauses with unmerged index entries: stage 1 is base, 2 is current side, 3 is incoming side for a normal merge. Markers in the working file show alternatives: <<<<<<< HEAD, =======, >>>>>>> source. They are not intended final content. Resolve by understanding both changes; editing and saving alone does not resolve index state. `git add` marks a path resolved. `git merge --continue` concludes a merge and may open the commit-message editor; a normal `git commit -m` also concludes it once all paths are resolved.

## Practice

Create a NEW isolated disposable lab using module 00 chapter 03 and its first-commit lesson. Keep the original dedicated shell, not the editor terminal. The initial main must contain exactly one commit, note.txt = practice, with clean status. Close any previous lab shell before starting. Follow the safety checks from chapter 01 before every history-changing operation.

[Isolated lab setup](../../getting-started/03-first-repository/README.md) · [First commit](../../getting-started/05-first-commit/README.md) · [Integration safety and recovery first](../01-integration-safety/README.md)

```text
git rev-parse --show-toplevel
git branch --show-current
git status --short
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Stop unless root is your disposable lab, current branch is the one specified, status is clean before starting an operation, and both identities start with `Study Guide Example <learner@example.invalid>`. Before each commit also inspect the staged diff; stop on unexpected output.

```text
git switch -c feat/note
```

In the plain-text editor, create or edit note.txt to contain exactly one line: feature, with a final newline. Save, then stage in the dedicated shell:

```text
git add -- note.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

If diff and both identities are correct, commit:

```text
git commit -m "docs: revise feature note"
```

```text
git switch main
```

In the plain-text editor, create or edit note.txt to contain exactly one line: main, with a final newline. Save, then stage in the dedicated shell:

```text
git add -- note.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

If diff and both identities are correct, commit:

```text
git commit -m "docs: revise main note"
```

```text
git rev-parse --show-toplevel
git branch --show-current
git status --short
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Confirm clean main and both identities. Record main ID privately. Intentionally trigger conflict:

```text
git rev-parse main
git merge --no-ff --no-edit feat/note
```

Expect nonzero and a conflict in note.txt. Stop if different. Inspect, including opening note.txt in a plain-text editor:

```text
git status --short
git ls-files -u
git show :1:note.txt
git show :2:note.txt
git show :3:note.txt
```

Expected UU note.txt, three stages, base practice, current main, incoming feature. Abort first, while operation is in progress:

```text
git merge --abort
git status --short
git rev-parse main
git show HEAD:note.txt
```

Expect clean main, original ID and content main. Retry exactly the same merge:

```text
git merge --no-ff --no-edit feat/note
```

After confirming the same conflict, replace the entire dummy note.txt with two lines, main then feature, final newline; remove all marker lines. Inspect before committing:

```text
git add -- note.txt
git ls-files -u
git diff --cached
git diff --cached --check
git status
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

No unmerged entries or diff-check errors; read the actual file to ensure no markers remain. With expected staged content and fictional identities, finish via explicit message (or use git merge --continue and save its editor message, not both):

```text
git commit -m "docs: resolve note conflict"
git rev-list --parents -1 HEAD
git show HEAD:note.txt
git status --short
```

Expected two parents, combined two-line file and clean status. If using continue and unfamiliar editor opens, consult its instructions; do not delete message content randomly. Abort while merge is still in progress if uncertain.

## Common mistakes and safety

Do not blindly choose ours/theirs; understand what both edits mean. In a rebase the sides differ from normal merge. Never force resolution or treat marker removal as validation. A real project needs relevant tests and review, and binary/delete/rename conflicts may need other decisions.

After each independent lab, close the editor and dedicated shell, then delete only the exact temporary parent folder you recorded in module 00 using the file manager if you no longer need it. Never delete the guide, home or work repository.

## Exercise and self-check

What distinguishes edited from resolved? Answer: add replaces unmerged index stages with the selected result. Pass if abort restores initial state, retry resolves all stages and final commit has two parents. Professional use: preserve intent and test the resolution.

## Quick reference

- `git ls-files -u`
- `git show :1:note.txt`
- `git add -- note.txt`
- `git merge --abort`
- `git merge --continue`

## Official sources

- [Git: git-merge](https://git-scm.com/docs/git-merge)
- [Git: git-ls-files](https://git-scm.com/docs/git-ls-files)
- [Git: git-show](https://git-scm.com/docs/git-show)
- [Git: git-diff](https://git-scm.com/docs/git-diff)
- [Git: git-commit](https://git-scm.com/docs/git-commit)
