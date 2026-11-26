# Rebase, abort and continue

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../05-squash-merge/README.md) · [Index](../README.md) · [Next](../07-interactive-rebase/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 45 min

**Prerequisites:** [Squash integration](../05-squash-merge/README.md)

**Objective:** Reapply a local commit onto a new base, inspect conflicts and preserve original history with a backup ref.

## What and why

Rebase selects commits from a branch and reapplies them onto a new base; when recreated, commit IDs change because parents/metadata change. It normally moves the rebased branch, not the target branch. A rebase may stop per commit. During ordinary rebase conflict, ours is the rebased-so-far side (new base plus replayed work) and theirs is the commit being replayed, not the usual mental model of your feature vs incoming main. `--abort` restores the original branch; `--continue` resumes after staging resolutions. `--skip` omits the current patch and may lose intended changes; do not use it in this lab.

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
git switch feat/note
git branch backup/feature
```

```text
git rev-parse --show-toplevel
git branch --show-current
git status --short
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Verify clean feat/note, fictional identities, backup points to its current tip. Record both tips before rebasing. Trigger the expected conflict:

```text
git rev-parse main feat/note backup/feature
git rebase main
```

Expect conflict in note.txt. Inspect stages and status; HEAD may be detached during replay:

```text
git status
git ls-files -u
git show :1:note.txt
git show :2:note.txt
git show :3:note.txt
git rebase --abort
git branch --show-current
git rev-parse feat/note backup/feature
git status --short
```

Expected base practice, stage 2 main, stage 3 feature. After abort original tip equals backup, active feat/note and clean status. Repeat rebase:

```text
git rebase main
```

Confirm conflict again. Replace dummy note.txt with two lines main then feature, final newline, remove all markers. Stage and inspect:

```text
git add -- note.txt
git ls-files -u
git diff --cached
git diff --cached --check
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

If all resolved, identities fictional and diff correct, run git rebase --continue. It may open the commit-message editor. Save the existing message and close the editor. If you have the optional VS Code CLI installed, instead use the second command (not both); --wait makes Git wait until the file is closed. If no usable editor, abort the in-progress lab rather than bypassing review. Only after success run the inspection block:

```text
git rebase --continue
```

```text
git -c core.editor="code --wait" rebase --continue
```

```text
git branch --show-current
git rev-parse main HEAD~1
git rev-parse feat/note backup/feature
git log --all --graph --oneline --decorate
git show HEAD:note.txt
git status --short
```

Expected feat/note active, main equals HEAD~1, rebased feature ID differs from backup, combined file, clean status. Diagram: main -> C3 -> C1; backup/feature -> C2 -> C1; feat/note -> C2' -> C3. The backup stays intact. For a nonconflicting rebase, the same replay completes without stopping when edits are compatible; inspect parent and content in either case.

## Common mistakes and safety

Never rewrite a published/shared branch here. Do not force push, skip or assume ours means your feature. Abort only an ongoing rebase. A backup ref is not an external backup; keep it until verified.

After each independent lab, close the editor and dedicated shell, then delete only the exact temporary parent folder you recorded in module 00 using the file manager if you no longer need it. Never delete the guide, home or work repository.

## Exercise and self-check

Why does the recreated commit have a new ID? New parent and commit metadata/content. Pass if abort restores original, continue creates new feature tip atop main and backup keeps old tip. Professional use: update unpublished work with upstream changes only under team policy.

## Quick reference

- `git rebase main`
- `git rebase --abort`
- `git rebase --continue`

## Official sources

- [Git: git-rebase](https://git-scm.com/docs/git-rebase)
- [Git: git-branch](https://git-scm.com/docs/git-branch)
- [Git: git-ls-files](https://git-scm.com/docs/git-ls-files)
- [Git: git-config](https://git-scm.com/docs/git-config)

---

<!-- navigation-footer -->
[Previous](../05-squash-merge/README.md) · [Index](../README.md) · [Next](../07-interactive-rebase/README.md)
<!-- /navigation-footer -->
