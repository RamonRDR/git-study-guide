# 07 Merge, Rebase & Conflicts

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../06-branch-management/README.md) · [Index](../README.md) · [Next](../08-remotes-and-synchronization/README.md)
<!-- /navigation -->

Generated from canonical catalog JSON. Edit the records, not this page.

Reference entries describe commands and operations, not a sequence to run. Use disposable repositories for practice. Hosted operations are optional.

**Total distinct entries: 10**

- [`git merge`](#git-merge)
- [`git merge --ff-only`](#git-merge-ff-only)
- [`git merge --no-ff`](#git-merge-no-ff)
- [`git merge --squash`](#git-merge-squash)
- [`git merge --abort`](#git-merge-abort)
- [`git merge --continue`](#git-merge-continue)
- [`git rebase`](#git-rebase)
- [`git rebase -i`](#git-rebase-interactive)
- [`git rebase --continue`](#git-rebase-continue)
- [`git rebase --abort`](#git-rebase-abort)

## git-merge

**`git merge`**

**Type:** Native command

**Level:** Intermediate

**Find by intent:** Integrate changes

**Risk:** State change. Integration can conflict or change the current tip; verify target and review the resulting diff and tests before sharing.

**Purpose:** Integrate changes from another revision into the current branch.

**Prerequisites:** Use an owned disposable repository, clean status, verified refs and fictional identity. Save the original tip before integration.

**Options:** --ff-only refuses non-fast-forward integration; --no-ff requests a merge commit when integration is needed.

**When to use:** When bringing reviewed branch work into the selected local target.

**When to avoid:** Avoid integrating with valuable uncommitted edits, unknown target refs or unfinished operations.

**Syntax**

`git merge feature`

**Basic example**

`git merge feature`

From clean main, integrate an existing local practice branch.

**Professional example**

`git merge feat/docs`

After verifying local target and reviewed documentation branch, integrate and test.

**State effects**

- Working tree: Conditional
- Index: Conditional
- Objects / refs / history: Conditional
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** May report already up to date, advance by fast-forward, create a merge commit or pause for conflicts, depending on ancestry and configuration.

**Effects and side effects:** May update working files, index, current ref, objects and merge metadata; no remote update is inherent.

**Common errors:** Running from the source rather than target branch or assuming merge always creates a commit.

**Alternatives:** Use --ff-only when only a linear advancement is allowed; use rebase only under a suitable history policy.

**Recovery:** Inspect status and the saved tip. If the operation is still paused, use its matching abort command when appropriate. After completion, choose recovery according to whether history was shared; do not reset blindly.

**Version and dependencies:** Standard Git syntax; use the guide's Git 2.40 or newer lab baseline. A trusted editor and local hooks may affect execution.

**Related lessons**

- [merge-and-conflicts/01-integration-safety](../../merge-and-conflicts/01-integration-safety/README.md)
- [merge-and-conflicts/03-merge-commit](../../merge-and-conflicts/03-merge-commit/README.md)
- [merge-and-conflicts/04-conflict-resolution](../../merge-and-conflicts/04-conflict-resolution/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-merge>

## git-merge-ff-only

**`git merge --ff-only`**

**Type:** Option usage

**Level:** Beginner

**Find by intent:** Integrate changes, Protect history

**Risk:** State change. Integration can conflict or change the current tip; verify target and review the resulting diff and tests before sharing.

**Purpose:** Integrate only if the current tip can advance without a merge commit, or is already up to date.

**Prerequisites:** Use an owned disposable repository, clean status, verified refs and fictional identity. Save the original tip before integration.

**Options:** --ff-only refuses integration requiring a merge commit.

**When to use:** When enforcing a linear integration path without rewriting commits.

**When to avoid:** Do not use it expecting Git to reconcile divergent histories automatically.

**Syntax**

`git merge --ff-only feature`

**Basic example**

`git merge --ff-only feature`

Integrate a local branch descending from main while on main.

**Professional example**

`git merge --ff-only feat/docs`

Enforce a linear local integration after checking ancestry.

**State effects**

- Working tree: Conditional
- Index: Conditional
- Objects / refs / history: Conditional
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** Advances the current ref to the source tip when possible, leaves it unchanged if already contained, or refuses divergence.

**Effects and side effects:** May update working files, index and current ref; no new merge commit is created.

**Common errors:** Treating a refusal as a reason to force or reset the branch.

**Alternatives:** Inspect divergence and choose a reviewed merge or private rebase according to policy.

**Recovery:** If refused, inspect ancestry and status; if advanced incorrectly, use the saved original tip to assess recovery without overwriting shared history.

**Version and dependencies:** Standard Git syntax; use the guide's Git 2.40 or newer lab baseline. A trusted editor and local hooks may affect execution.

**Related lessons**

- [merge-and-conflicts/02-fast-forward](../../merge-and-conflicts/02-fast-forward/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-merge>

## git-merge-no-ff

**`git merge --no-ff`**

**Type:** Option usage

**Level:** Intermediate

**Find by intent:** Integrate changes

**Risk:** State change. Integration can conflict or change the current tip; verify target and review the resulting diff and tests before sharing.

**Purpose:** Preserve an explicit merge boundary even when a fast-forward would otherwise be possible.

**Prerequisites:** Use an owned disposable repository, clean status, verified refs and fictional identity. Save the original tip before integration.

**Options:** --no-ff requests a merge commit when changes need integrating; -m supplies its message.

**When to use:** When team policy requires an explicit integration commit.

**When to avoid:** Avoid on branches requiring strictly linear history.

**Syntax**

`git merge --no-ff feature`

**Basic example**

`git merge --no-ff feature`

Integrate a non-contained practice branch with an explicit merge boundary.

**Professional example**

`git merge --no-ff -m "Merge documentation" feat/docs`

Record a reviewed integration where merge commits are permitted.

**State effects**

- Working tree: Conditional
- Index: Conditional
- Objects / refs / history: Conditional
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** On successful integration of a single non-contained branch, creates a commit with two parents; already-contained history may be unchanged.

**Effects and side effects:** May update working tree, index, objects and ref; conflicts can pause before commit creation.

**Common errors:** Expecting a merge commit even when there is nothing to integrate.

**Alternatives:** Use --ff-only for linear advancement, or a reviewed squash workflow when policy requires one new commit without merge ancestry.

**Recovery:** Inspect status and the saved tip. If the operation is still paused, use its matching abort command when appropriate. After completion, choose recovery according to whether history was shared; do not reset blindly.

**Version and dependencies:** Standard Git syntax; use the guide's Git 2.40 or newer lab baseline. A trusted editor and local hooks may affect execution.

**Related lessons**

- [merge-and-conflicts/03-merge-commit](../../merge-and-conflicts/03-merge-commit/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-merge>

## git-merge-squash

**`git merge --squash`**

**Type:** Option usage

**Level:** Intermediate

**Find by intent:** Integrate changes, Stage changes

**Risk:** State change. Review the entire staged result before committing; source commits may remain outside target ancestry.

**Purpose:** Prepare the combined changes of another branch without moving HEAD or recording merge ancestry.

**Prerequisites:** Use an owned disposable repository, clean status, verified refs and fictional identity. Save the original tip before integration.

**Options:** --squash prepares the integration result; a separate git commit records the staged snapshot.

**When to use:** When a reviewed local integration should become one ordinary commit.

**When to avoid:** Avoid when preserving source commit ancestry is required or the index contains unrelated edits.

**Syntax**

`git merge --squash feature`

**Basic example**

`git merge --squash feature`

Prepare combined changes from an existing practice branch, then inspect before committing.

**Professional example**

`git merge --squash feat/docs`

Prepare reviewed documentation for a single later commit; verify diff and tests.

**State effects**

- Working tree: Conditional
- Index: Conditional
- Objects / refs / history: Conditional
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** On clean success, working tree and index reflect the combined result while HEAD stays unchanged; conflicts may require resolution.

**Effects and side effects:** Does not set MERGE\_HEAD; the later ordinary commit has one parent. Local objects or squash metadata may be created.

**Common errors:** Assuming --squash commits automatically or that git merge --abort always works for a squash operation.

**Alternatives:** Use an ordinary merge when preserving ancestry is important.

**Recovery:** Inspect status and staged changes; since there is no MERGE\_HEAD, do not rely on merge --abort. In a verified initially clean disposable lab, reset --merge HEAD may discard the attempted tracked integration after preserving needed edits; assess separately if work existed.

**Version and dependencies:** Standard Git syntax; use the guide's Git 2.40 or newer lab baseline. A trusted editor and local hooks may affect execution.

**Related lessons**

- [merge-and-conflicts/05-squash-merge](../../merge-and-conflicts/05-squash-merge/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-merge>

## git-merge-abort

**`git merge --abort`**

**Type:** Option usage

**Level:** Intermediate

**Find by intent:** Resolve conflicts, Recover work

**Risk:** Destructive. Cancellation discards conflict-resolution work; preserve any desired edits separately first. Recovery of prior uncommitted work is not guaranteed.

**Purpose:** Attempt to cancel an in-progress ordinary merge and reconstruct its pre-merge state.

**Prerequisites:** Use an owned disposable repository with the specified operation already paused; inspect git status and preserve any resolution edits you need.

**Options:** --abort operates on an active merge; it is not a general undo command.

**When to use:** When abandoning an unresolved ordinary merge in a disposable clean-start lab.

**When to avoid:** Avoid if resolution work must be preserved or the merge already completed; squash merges lack MERGE\_HEAD.

**Syntax**

`git merge --abort`

**Basic example**

`git merge --abort`

Cancel a deliberately conflicted ordinary practice merge.

**Professional example**

`git merge --abort`

After saving desired resolution edits, abandon an unsuitable local integration.

**State effects**

- Working tree: Conditional
- Index: Conditional
- Objects / refs / history: Conditional
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** Attempts to restore pre-merge state and clears the active merge on success; prior dirty work may not be reconstructed.

**Effects and side effects:** May change working tree, index and merge metadata; auto-stash can be reapplied and may conflict.

**Common errors:** Using abort after a completed merge or assuming it guarantees recovery of uncommitted work.

**Alternatives:** Resolve and stage conflicts then use git merge --continue if integration should finish.

**Recovery:** Verify status and original tip after abort. If it fails, stop and inspect remaining state before further changes.

**Version and dependencies:** Standard Git syntax; use the guide's Git 2.40 or newer lab baseline. A trusted editor and local hooks may affect execution.

**Related lessons**

- [merge-and-conflicts/04-conflict-resolution](../../merge-and-conflicts/04-conflict-resolution/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-merge>

## git-merge-continue

**`git merge --continue`**

**Type:** Option usage

**Level:** Intermediate

**Find by intent:** Resolve conflicts, Integrate changes

**Risk:** State change. Integration can conflict or change the current tip; verify target and review the resulting diff and tests before sharing.

**Purpose:** Finish an active ordinary merge after conflicts are resolved and staged.

**Prerequisites:** In a disposable repository with the indicated operation paused, resolve conflicts, stage intended resolutions, review the staged diff and confirm fictional identity.

**Options:** --continue checks for an active merge and invokes commit; the editor or hooks may require interaction.

**When to use:** When all intended conflict resolutions are staged and reviewed.

**When to avoid:** Do not continue while unmerged paths remain or resolution content is unreviewed.

**Syntax**

`git merge --continue`

**Basic example**

`git merge --continue`

Finish the practice merge after staging a resolved file.

**Professional example**

`git merge --continue`

After reviewing resolution diff and running tests, complete a local merge.

**State effects**

- Working tree: Conditional
- Index: Conditional
- Objects / refs / history: Conditional
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** On success creates the merge commit and clears merge state; otherwise may remain paused.

**Effects and side effects:** May update ref, objects, index metadata and merge state; hooks can change local state.

**Common errors:** Assuming removing conflict markers alone stages the resolution.

**Alternatives:** Use git commit to conclude an ordinary merge after inspecting its state, or abort if abandoning it.

**Recovery:** Inspect status and the saved tip. If the operation is still paused, use its matching abort command when appropriate. After completion, choose recovery according to whether history was shared; do not reset blindly.

**Version and dependencies:** Standard Git syntax; use the guide's Git 2.40 or newer lab baseline. A trusted editor and local hooks may affect execution.

**Related lessons**

- [merge-and-conflicts/04-conflict-resolution](../../merge-and-conflicts/04-conflict-resolution/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-merge>

## git-rebase

**`git rebase`**

**Type:** Native command

**Level:** Advanced

**Find by intent:** Integrate changes, Rewrite local history

**Risk:** History rewrite. Replay can change commit IDs and disrupt collaborators. Use private history, retain the original tip and verify the result before sharing.

**Purpose:** Replay selected commits on a different base to reorganize local history.

**Prerequisites:** Use an owned disposable repository, clean status, verified refs and fictional identity. Save the original tip before integration.

**Options:** Specify the upstream revision; --onto allows a separate new base and requires careful range selection.

**When to use:** When updating a private feature branch on a newer integration base.

**When to avoid:** Avoid rewriting shared commits without agreement, or rebasing with unfinished operations.

**Syntax**

`git rebase main`

**Basic example**

`git rebase main`

From a clean private feature branch, replay onto existing main.

**Professional example**

`git rebase main`

After saving the private topic tip, update its base and compare the revised series.

**State effects**

- Working tree: Conditional
- Index: Conditional
- Objects / refs / history: Conditional
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** May replay commits with new IDs, skip equivalent changes, fast-forward, do nothing or pause for conflicts.

**Effects and side effects:** May change working files, index, objects, current ref and sequencer state; HEAD may be detached during replay.

**Common errors:** Assuming rebase preserves IDs or runs from the integration target instead of the branch being replayed.

**Alternatives:** Use merge to integrate without replacing existing source commits.

**Recovery:** Inspect status and the saved tip. If the operation is still paused, use its matching abort command when appropriate. After completion, choose recovery according to whether history was shared; do not reset blindly.

**Version and dependencies:** Standard Git syntax; use the guide's Git 2.40 or newer lab baseline. A trusted editor and local hooks may affect execution.

**Related lessons**

- [merge-and-conflicts/06-rebase-and-conflicts](../../merge-and-conflicts/06-rebase-and-conflicts/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-rebase>

## git-rebase-interactive

**`git rebase -i`**

**Type:** Option usage

**Level:** Advanced

**Find by intent:** Rewrite local history, Review changes

**Risk:** History rewrite. Replay can change commit IDs and disrupt collaborators. Use private history, retain the original tip and verify the result before sharing.

**Purpose:** Edit the sequence of selected private commits before replaying them.

**Prerequisites:** Use an owned disposable repository, clean status, verified refs and fictional identity. Save the original tip before integration.

**Options:** -i opens a todo list with actions such as pick, reword, edit, squash, fixup and drop; review the order and effects before saving.

**When to use:** When refining an unpublished patch series before review.

**When to avoid:** Avoid changing shared history, dropping needed commits or blindly reordering dependent changes.

**Syntax**

`git rebase -i HEAD~2`

**Basic example**

`git rebase -i HEAD~2`

With at least two private commits after a base, inspect the todo list before changing it.

**Professional example**

`git rebase -i main`

On a private linear feature series, review planned edits or fixup actions and validate afterward.

**State effects**

- Working tree: Conditional
- Index: Conditional
- Objects / refs / history: Conditional
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** Applies the chosen actions; may replace, combine, omit or pause on commits. An unchanged todo may leave history unchanged.

**Effects and side effects:** May modify history, working files, index and rebase metadata; default behavior does not preserve merge topology.

**Common errors:** Confusing todo order with newest-first log order, or dropping a prerequisite commit.

**Alternatives:** Use an ordinary follow-up commit if history must remain intact; use range-diff to review revised series.

**Recovery:** Inspect status and the saved tip. If the operation is still paused, use its matching abort command when appropriate. After completion, choose recovery according to whether history was shared; do not reset blindly.

**Version and dependencies:** Standard Git syntax; use the guide's Git 2.40 or newer lab baseline. A trusted editor and local hooks may affect execution.

**Related lessons**

- [merge-and-conflicts/07-interactive-rebase](../../merge-and-conflicts/07-interactive-rebase/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-rebase>

## git-rebase-continue

**`git rebase --continue`**

**Type:** Option usage

**Level:** Advanced

**Find by intent:** Resolve conflicts, Rewrite local history

**Risk:** History rewrite. Replay can change commit IDs and disrupt collaborators. Use private history, retain the original tip and verify the result before sharing.

**Purpose:** Resume an interrupted rebase after handling its current stop.

**Prerequisites:** In a disposable repository with the indicated operation paused, resolve conflicts, stage intended resolutions, review the staged diff and confirm fictional identity.

**Options:** --continue resumes the active sequence; more conflicts or edit stops may follow.

**When to use:** When intended resolutions or planned edits are ready and reviewed.

**When to avoid:** Avoid continuing with unresolved paths or using --skip merely to silence a conflict.

**Syntax**

`git rebase --continue`

**Basic example**

`git rebase --continue`

After staging the resolved practice file, resume the replay.

**Professional example**

`git rebase --continue`

Review staged resolution and test the private series before resuming; repeat if paused again.

**State effects**

- Working tree: Conditional
- Index: Conditional
- Objects / refs / history: Conditional
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** Resumes replay; may finish and update the branch or pause again.

**Effects and side effects:** May create replacement commits, update index and working tree, move HEAD and change sequencer metadata.

**Common errors:** Assuming one continuation always completes the entire series.

**Alternatives:** Use git rebase --abort to abandon the active rebase after preserving needed resolution work.

**Recovery:** Inspect status and the saved tip. If the operation is still paused, use its matching abort command when appropriate. After completion, choose recovery according to whether history was shared; do not reset blindly.

**Version and dependencies:** Standard Git syntax; use the guide's Git 2.40 or newer lab baseline. A trusted editor and local hooks may affect execution.

**Related lessons**

- [merge-and-conflicts/06-rebase-and-conflicts](../../merge-and-conflicts/06-rebase-and-conflicts/README.md)
- [merge-and-conflicts/07-interactive-rebase](../../merge-and-conflicts/07-interactive-rebase/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-rebase>

## git-rebase-abort

**`git rebase --abort`**

**Type:** Option usage

**Level:** Advanced

**Find by intent:** Resolve conflicts, Recover work

**Risk:** Destructive. Cancellation discards conflict-resolution work; preserve any desired edits separately first. Recovery of prior uncommitted work is not guaranteed.

**Purpose:** Cancel an active rebase and restore HEAD to the original branch or starting position.

**Prerequisites:** Use an owned disposable repository with the specified operation already paused; inspect git status and preserve any resolution edits you need.

**Options:** --abort cancels replay; --quit stops tracking the operation without the same reset of HEAD, index and working tree.

**When to use:** When abandoning an unfinished private rebase because its conflicts or plan are unsuitable.

**When to avoid:** Avoid aborting if needed resolution changes are not saved separately; it is not an undo for completed rebase.

**Syntax**

`git rebase --abort`

**Basic example**

`git rebase --abort`

Cancel a conflicted practice rebase started from clean state.

**Professional example**

`git rebase --abort`

After preserving necessary resolution edits, abandon a private replay and verify the original tip.

**State effects**

- Working tree: Conditional
- Index: Conditional
- Objects / refs / history: Conditional
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** Restores the original checkout position and clears the active rebase on success; auto-stash may complicate restoration.

**Effects and side effects:** May discard intermediate replay and resolution state, update working files, index and HEAD; created objects may remain until cleanup.

**Common errors:** Expecting edits made during conflict resolution to survive cancellation.

**Alternatives:** Resolve and continue when the original integration plan is still appropriate.

**Recovery:** Verify the saved original tip, status and any stash after cancellation; if restoration fails, preserve remaining data and inspect before further action.

**Version and dependencies:** Standard Git syntax; use the guide's Git 2.40 or newer lab baseline. A trusted editor and local hooks may affect execution.

**Related lessons**

- [merge-and-conflicts/06-rebase-and-conflicts](../../merge-and-conflicts/06-rebase-and-conflicts/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-rebase>


---

<!-- navigation-footer -->
[Previous](../06-branch-management/README.md) · [Index](../README.md) · [Next](../08-remotes-and-synchronization/README.md)
<!-- /navigation-footer -->
