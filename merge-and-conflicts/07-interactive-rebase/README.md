# Interactive rebase and strategy choice

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../06-rebase-and-conflicts/README.md) · [Index](../README.md) · —
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 40 min

**Prerequisites:** [Rebase, abort and continue](../06-rebase-and-conflicts/README.md)

**Objective:** Combine two local commits with fixup and compare integration strategies.

## What and why

Interactive rebase opens a todo list of commits (oldest first). `pick` keeps a commit's change; `reword` changes message; `edit` pauses; `squash` combines with previous commit and allows message editing; `fixup` combines and normally discards the second message; `drop` omits a commit. Reordering can cause conflicts. These are history-rewriting tools, not ordinary edits. We practice only fixup on two local commits with a backup branch. Git's todo editor is controlled by sequence.editor or GIT_SEQUENCE_EDITOR, distinct from the commit-message editor.

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

In the plain-text editor, create or edit detail.txt to contain exactly one line: detail, with a final newline. Save, then stage in the dedicated shell:

```text
git add -- detail.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

If diff and both identities are correct, commit:

```text
git commit -m "docs: add detail"
```

```text
git branch backup/feature
git log -3 --oneline
git rev-list --count main..HEAD
```

```text
git rev-parse --show-toplevel
git branch --show-current
git status --short
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Confirm two commits after main, clean feat/note, backup at its tip and fictional identities. Use one of these commands, not both. The first uses your configured editor; optional VS Code CLI (if `code --version` works) is the second choice. If unfamiliar with the editor, learn how to save/exit first or defer this optional manual exercise. Do not set global editor configuration for the lab.

```text
git rebase -i HEAD~2
```

```text
git -c sequence.editor="code --wait" rebase -i HEAD~2
```

In the todo editor, leave the first pick line unchanged; change only the second line's word pick to fixup. Keep real IDs; the following placeholders illustrate the shape, do not paste them:

```text
pick FIRST_ID docs: revise feature note
fixup SECOND_ID docs: add detail
```

Save and close todo file. If the todo differs, cancel safely without saving your edits; an unchanged todo may perform a no-op rebase. If rebase stops with a conflict, abort or resolve using chapter 06. After successful completion:

```text
git rev-list --count main..HEAD
git rev-list --count main..backup/feature
git log -1 --format=%s
git diff HEAD backup/feature
git show HEAD:note.txt
git show HEAD:detail.txt
git status --short
```

Expected one new commit versus two on backup, first message retained, empty endpoint diff (same snapshot), feature and detail contents and clean status. Strategy comparison: ff-only = existing commit IDs, no new merge commit; merge commit = two parents and both histories; squash = one new target commit, no source ancestry; rebase = recreated local commits on new base; interactive rebase = edit local commit sequence before integration. Choose based on ancestry, review history and team policy.

## Common mistakes and safety

Do not use drop, reorder or reword on shared history. Avoid blindly editing todo IDs or skipping changes. If completed result is wrong, keep backup ref and stop; completed-operation recovery is deferred to module 07. Manual editor interaction is not exercised in CI; deterministic tests use a controlled todo editor.

After each independent lab, close the editor and dedicated shell, then delete only the exact temporary parent folder you recorded in module 00 using the file manager if you no longer need it. Never delete the guide, home or work repository.

## Exercise and self-check

When would you choose squash instead of interactive rebase? Answer: squash integrates a source's combined changes as one target commit; interactive rebase changes the local source sequence. Pass if the final snapshot matches backup while commit count differs. Professional use: prepare local review history without rewriting shared commits.

## Quick reference

- `git rebase -i HEAD~2`
- `pick`
- `fixup`
- `git diff HEAD backup/feature`

## Official sources

- [Git: git-rebase](https://git-scm.com/docs/git-rebase)
- [Git: git-config](https://git-scm.com/docs/git-config)
- [Git: git-merge](https://git-scm.com/docs/git-merge)
- [Git: git-diff](https://git-scm.com/docs/git-diff)
