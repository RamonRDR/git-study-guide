# 03 Working Tree & Staging

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../02-repository-inspection/README.md) · [Index](../README.md) · [Next](../04-commits-and-tags/README.md)
<!-- /navigation -->

Generated from canonical catalog JSON. Edit the records, not this page.

Reference entries describe commands and operations, not a sequence to run. Use disposable repositories for practice. Hosted operations are optional.

**Total distinct entries: 10**

- [`git add`](#git-add)
- [`git add -A`](#git-add-all)
- [`git add -u`](#git-add-update)
- [`git add -p`](#git-add-patch)
- [`git restore`](#git-restore)
- [`git restore --staged`](#git-restore-staged)
- [`git rm`](#git-rm)
- [`git rm --cached`](#git-rm-cached)
- [`git mv`](#git-mv)
- [`git clean -n`](#git-clean-dry-run)

## git-add

**`git add`**

**Type:** Native command

**Level:** Beginner

**Find by intent:** Stage changes

**Risk:** State change. Review the exact paths and staged changes; do not operate on the guide repository.

**Purpose:** Stage selected paths for the next commit.

**Prerequisites:** Use an owned disposable repository; inspect git status first and protect valuable work.

**Options:** -- ends option parsing; specify one or more paths.

**When to use:** After inspecting changes you want to commit.

**When to avoid:** Do not stage credentials or unrelated changes.

**Syntax**

`git add -- path`

**Basic example**

`git add -- notes.txt`

Review a fictional notes file before staging it.

**Professional example**

`git add -- src/main.py`

Stage only the reviewed source file for a focused commit.

**State effects**

- Working tree: Unchanged
- Index: Changes
- Objects / refs / history: Conditional
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Index entries reflect selected working-tree content or deletions.

**Effects and side effects:** Updates the index and may store blob objects; no commit or remote update.

**Common errors:** Assuming later edits are staged automatically.

**Alternatives:** Use git add -p to select hunks.

**Recovery:** Inspect git diff --cached afterward. Unstage unwanted changes with git restore --staged on Git 2.23+ when HEAD exists; keep working files.

**Version and dependencies:** No optional tool required; the example uses standard Git syntax.

**Related lessons**

- [basic-commands/02-status-add-commit](../../basic-commands/02-status-add-commit/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-add>

## git-add-all

**`git add -A`**

**Type:** Option usage

**Level:** Beginner

**Find by intent:** Stage changes

**Risk:** State change. Review the exact paths and staged changes; do not operate on the guide repository.

**Purpose:** Stage additions, modifications and removals within the selected scope.

**Prerequisites:** Use an owned disposable repository; inspect git status first and protect valuable work.

**Options:** -A updates all matching index entries; a pathspec narrows the scope.

**When to use:** When all changes in a deliberate scope belong together.

**When to avoid:** Avoid broad staging when unrelated or sensitive files may exist.

**Syntax**

`git add -A [-- pathspec]`

**Basic example**

`git add -A`

In a cleanly scoped lab, inspect all changes before staging them together.

**Professional example**

`git add -A -- src`

Limit broad staging to a reviewed src directory.

**State effects**

- Working tree: Unchanged
- Index: Changes
- Objects / refs / history: Conditional
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** New, modified and deleted paths in scope are staged, subject to ignore rules.

**Effects and side effects:** Updates index and may write objects; leaves working files in place.

**Common errors:** Forgetting that deletions and new files can be included.

**Alternatives:** Use explicit git add paths or git add -p for finer scope.

**Recovery:** Inspect git diff --cached afterward. Unstage unwanted changes with git restore --staged on Git 2.23+ when HEAD exists; keep working files.

**Version and dependencies:** No optional tool required; the example uses standard Git syntax.

**Related lessons**

- [basic-commands/02-status-add-commit](../../basic-commands/02-status-add-commit/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-add>

## git-add-update

**`git add -u`**

**Type:** Option usage

**Level:** Intermediate

**Find by intent:** Stage changes

**Risk:** State change. Review the exact paths and staged changes; do not operate on the guide repository.

**Purpose:** Stage modifications and deletions of already indexed paths without adding new untracked paths.

**Prerequisites:** Use an owned disposable repository; inspect git status first and protect valuable work.

**Options:** -u updates tracked index entries; pathspec optionally limits scope.

**When to use:** When updating existing tracked files only.

**When to avoid:** Do not use when required new files must be included automatically.

**Syntax**

`git add -u [-- pathspec]`

**Basic example**

`git add -u`

Modify a tracked file and create an untracked file; stage tracked changes only.

**Professional example**

`git add -u -- src`

Prepare tracked changes under src without adding generated untracked files.

**State effects**

- Working tree: Unchanged
- Index: Changes
- Objects / refs / history: Conditional
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Tracked modifications and removals are staged; new untracked paths remain untracked.

**Effects and side effects:** Changes index and may write blobs, not commits.

**Common errors:** Omitting a new dependency file or accidentally staging tracked deletions.

**Alternatives:** Use git add -A if deliberately including new paths too.

**Recovery:** Inspect git diff --cached afterward. Unstage unwanted changes with git restore --staged on Git 2.23+ when HEAD exists; keep working files.

**Version and dependencies:** No optional tool required; the example uses standard Git syntax.

**Related lessons**

- [basic-commands/02-status-add-commit](../../basic-commands/02-status-add-commit/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-add>

## git-add-patch

**`git add -p`**

**Type:** Option usage

**Level:** Intermediate

**Find by intent:** Stage changes

**Risk:** State change. Review the exact paths and staged changes; do not operate on the guide repository.

**Purpose:** Interactively select diff hunks to stage.

**Prerequisites:** Use an owned disposable repository; inspect git status first and protect valuable work.

**Options:** -p opens interactive hunk selection; available actions are shown in the prompt.

**When to use:** When a file contains changes belonging to separate commits.

**When to avoid:** Avoid blind confirmation; related hunks may depend on one another.

**Syntax**

`git add -p [-- pathspec]`

**Basic example**

`git add -p -- notes.txt`

Edit two independent lines and choose one hunk where Git separates them.

**Professional example**

`git add -p -- src/main.py`

Separate a bug fix from unrelated refactoring in a reviewed source file.

**State effects**

- Working tree: Unchanged
- Index: Changes
- Objects / refs / history: Conditional
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Only accepted changes enter the index; remaining edits stay unstaged.

**Effects and side effects:** Updates selected index content; working file stays unchanged.

**Common errors:** Staging half of a dependent change or assuming a selected hunk equals a tested commit.

**Alternatives:** Use explicit paths for whole-file staging or split work into separate files.

**Recovery:** Inspect git diff --cached afterward. Unstage unwanted changes with git restore --staged on Git 2.23+ when HEAD exists; keep working files.

**Version and dependencies:** No optional tool required; the example uses standard Git syntax.

**Related lessons**

- [basic-commands/02-status-add-commit](../../basic-commands/02-status-add-commit/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-add>

## git-restore

**`git restore`**

**Type:** Native command

**Level:** Beginner

**Find by intent:** Undo changes

**Risk:** Destructive. May remove or overwrite working files. Use only disposable practice data and back up anything valuable first.

**Purpose:** Restore a working-tree path from the index by default, discarding unstaged differences.

**Prerequisites:** Use an owned disposable repository; inspect git status first and protect valuable work.

**Options:** --source selects an explicit tree; -- limits option parsing.

**When to use:** Only when inspected unstaged edits are intentionally unwanted.

**When to avoid:** Do not discard uncommitted work you may need; save it independently first.

**Syntax**

`git restore [--source=tree] -- path`

**Basic example**

`git restore -- notes.txt`

In a disposable lab, discard an intentionally unwanted edit to a tracked notes file.

**Professional example**

`git restore -- src/main.py`

After reviewing and backing up changes, restore only the unwanted source-file edit in a disposable clone.

**State effects**

- Working tree: Changes
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Selected working path matches source; default leaves staged content intact.

**Effects and side effects:** May overwrite or remove working files; does not move HEAD or alter the index in this usage.

**Common errors:** Confusing the default source with HEAD when staged content differs.

**Alternatives:** Save a patch or backup before discard; use git restore --staged to unstage instead.

**Recovery:** Unstaged edits may never have entered Git; use an independent backup or editor history if available. Recovery is not guaranteed.

**Version and dependencies:** git restore requires Git 2.23 or newer.

**Related lessons**

- [history-and-recovery/02-restore](../../history-and-recovery/02-restore/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-restore>

## git-restore-staged

**`git restore --staged`**

**Type:** Option usage

**Level:** Beginner

**Find by intent:** Unstage changes

**Risk:** State change. Review the exact paths and staged changes; do not operate on the guide repository.

**Purpose:** Restore the selected index entry from HEAD by default while preserving working files.

**Prerequisites:** Use an owned disposable repository; inspect git status first and protect valuable work.

**Options:** --staged targets the index; default source is HEAD; use -- to mark paths.

**When to use:** When an existing commit is present and a path was staged prematurely.

**When to avoid:** Do not combine with --worktree unless you intend to overwrite working files too.

**Syntax**

`git restore --staged -- path`

**Basic example**

`git restore --staged -- notes.txt`

Unstage a tracked file after making a first commit.

**Professional example**

`git restore --staged -- src/main.py`

Remove an unrelated source-file change from the pending commit without discarding the edit.

**State effects**

- Working tree: Unchanged
- Index: Changes
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Selected index entries match HEAD; working edits remain available.

**Effects and side effects:** Changes index only in this usage; does not move refs.

**Common errors:** Using default HEAD source before the first commit; assuming prior partial staging can always be reconstructed.

**Alternatives:** Use git reset HEAD -- path for an existing HEAD on older Git.

**Recovery:** Review the working diff and stage desired changes again; earlier staged-only content may need a backup.

**Version and dependencies:** git restore requires Git 2.23 or newer.

**Related lessons**

- [history-and-recovery/02-restore](../../history-and-recovery/02-restore/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-restore>

## git-rm

**`git rm`**

**Type:** Native command

**Level:** Beginner

**Find by intent:** Manage files

**Risk:** Destructive. May remove or overwrite working files. Use only disposable practice data and back up anything valuable first.

**Purpose:** Remove a tracked path from the working tree and stage its deletion.

**Prerequisites:** Use an owned disposable repository; inspect git status first and protect valuable work.

**Options:** -r permits recursive removal; --cached removes only index entries; do not force bypass safety checks.

**When to use:** When a reviewed tracked file should be removed in the next commit.

**When to avoid:** Do not remove valuable local changes; avoid -f in routine practice.

**Syntax**

`git rm -- path`

**Basic example**

`git rm -- old.txt`

Remove a committed obsolete text file in a disposable repository.

**Professional example**

`git rm -- src/obsolete.py`

Stage deletion of a reviewed obsolete module in a disposable clone.

**State effects**

- Working tree: Changes
- Index: Changes
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** The tracked file is absent and its deletion is staged if the operation succeeds.

**Effects and side effects:** Changes working tree and index; prior commits stay unchanged.

**Common errors:** Assuming git rm erases earlier committed copies from history.

**Alternatives:** Use git rm --cached to keep the working file while removing tracking.

**Recovery:** If deletion is uncommitted and HEAD contains the desired file, restore index and working copy explicitly from HEAD after inspection; other lost edits may be unrecoverable.

**Version and dependencies:** No optional tool required; the example uses standard Git syntax.

**Related lessons**

- [basic-commands/04-move-and-remove](../../basic-commands/04-move-and-remove/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-rm>

## git-rm-cached

**`git rm --cached`**

**Type:** Option usage

**Level:** Intermediate

**Find by intent:** Ignore files

**Risk:** State change. Review the exact paths and staged changes; do not operate on the guide repository.

**Purpose:** Remove an indexed path from tracking while keeping the working copy.

**Prerequisites:** Use an owned disposable repository; inspect git status first and protect valuable work.

**Options:** --cached targets only index entries; -r is needed for recursive directory removal.

**When to use:** When a previously tracked non-sensitive generated file should no longer be tracked.

**When to avoid:** Do not use as a secret-removal procedure; earlier commits still contain the file.

**Syntax**

`git rm --cached -- path`

**Basic example**

`git rm --cached -- notes.tmp`

Stop tracking a harmless committed temporary file, then inspect status.

**Professional example**

`git rm --cached -- local-settings.txt`

Keep a harmless local settings fixture on disk while preparing its removal from tracking.

**State effects**

- Working tree: Unchanged
- Index: Changes
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Working file stays; tracked removal is staged when HEAD contains the path.

**Effects and side effects:** Changes index; no immediate remote or committed-history change.

**Common errors:** Adding an ignore rule alone and expecting an already tracked file to stop being tracked.

**Alternatives:** Use a suitable ignore rule for future untracked copies; use ordinary git rm if deleting the working file is intended.

**Recovery:** Before committing, inspect the staged removal and re-add the intended file if appropriate; original staged-only content may require backup.

**Version and dependencies:** No optional tool required; the example uses standard Git syntax.

**Related lessons**

- [basic-commands/05-ignore-and-review](../../basic-commands/05-ignore-and-review/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-rm>

## git-mv

**`git mv`**

**Type:** Native command

**Level:** Beginner

**Find by intent:** Manage files

**Risk:** State change. Review the exact paths and staged changes; do not operate on the guide repository.

**Purpose:** Move or rename a path and update the index accordingly.

**Prerequisites:** Use an owned disposable repository; inspect git status first and protect valuable work.

**Options:** -- ends option parsing; -n previews; avoid -f overwriting a destination.

**When to use:** When renaming a tracked file as part of a focused change.

**When to avoid:** Do not overwrite an existing destination or ignore dependent references.

**Syntax**

`git mv -- source destination`

**Basic example**

`git mv -- old.txt new.txt`

Rename a committed notes file to a new unused name.

**Professional example**

`git mv -- src/old.py src/new.py`

Rename an illustrative module and separately review dependent imports and tests.

**State effects**

- Working tree: Changes
- Index: Changes
- Objects / refs / history: Conditional
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Old path is removed and new path exists; index is updated; rename display depends on detection.

**Effects and side effects:** Updates working paths and index; Git commits snapshots, not explicit rename records.

**Common errors:** Assuming imports or documentation links are automatically updated.

**Alternatives:** Move with OS tools and stage old/new paths explicitly.

**Recovery:** Inspect status; reverse an uncommitted rename with an explicit inverse move if safe and destination is free.

**Version and dependencies:** No optional tool required; the example uses standard Git syntax.

**Related lessons**

- [basic-commands/04-move-and-remove](../../basic-commands/04-move-and-remove/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-mv>

## git-clean-dry-run

**`git clean -n`**

**Type:** Option usage

**Level:** Intermediate

**Find by intent:** Inspect files

**Risk:** Read-only. Preview only; never execute a destructive variant automatically.

**Purpose:** Preview untracked paths that a matching clean operation would remove.

**Prerequisites:** Use an owned disposable repository; inspect git status first and protect valuable work.

**Options:** -n is dry run; -d includes untracked directories; ignored paths are normally excluded.

**When to use:** Before considering cleanup of disposable untracked artifacts.

**When to avoid:** Do not replace -n with a destructive flag without separate backup and scope review.

**Syntax**

`git clean -n [-d]`

**Basic example**

`git clean -n`

Preview cleanup with a harmless untracked file in a disposable lab.

**Professional example**

`git clean -nd`

Preview untracked directories in a disposable clone before deciding whether cleanup is appropriate.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Lists candidate removals without deleting them.

**Effects and side effects:** No file removal in dry-run mode; no index or ref mutation.

**Common errors:** Assuming preview remains valid after files or ignore rules change.

**Alternatives:** Use git ls-files --others --exclude-standard to inspect untracked files.

**Recovery:** No recovery needed for preview itself; actual deletion of untracked files may be unrecoverable without backup.

**Version and dependencies:** No optional tool required; the example uses standard Git syntax.

**Related lessons**

- [history-and-recovery/01-recovery-safety](../../history-and-recovery/01-recovery-safety/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-clean>


---

<!-- navigation-footer -->
[Previous](../02-repository-inspection/README.md) · [Index](../README.md) · [Next](../04-commits-and-tags/README.md)
<!-- /navigation-footer -->
