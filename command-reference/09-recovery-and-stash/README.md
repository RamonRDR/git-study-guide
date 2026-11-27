# 09 Recovery & Stash

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../08-remotes-and-synchronization/README.md) · [Index](../README.md) · [Next](../10-search-and-troubleshooting/README.md)
<!-- /navigation -->

Generated from canonical catalog JSON. Edit the records, not this page.

Reference entries describe commands and operations, not a sequence to run. Use disposable repositories for practice. Hosted operations are optional.

**Total distinct entries: 7**

- [`git reset`](#git-reset)
- [`git revert`](#git-revert)
- [`git reflog`](#git-reflog)
- [`git cherry-pick`](#git-cherry-pick)
- [`git stash push`](#git-stash-push)
- [`git stash apply`](#git-stash-apply)
- [`git stash pop`](#git-stash-pop)

## git-reset

**`git reset`**

**Type:** Native command

**Level:** Advanced

**Find by intent:** Undo changes, Rewrite local history, Unstage changes

**Risk:** Destructive. Mode choice matters: hard can destroy local work, and all commit-level modes can rewrite branch history. Keep examples private and disposable.

**Purpose:** Move the current branch or detached HEAD to a selected commit in the commit-level form; choose how the index and working tree are affected.

**Prerequisites:** Use an owned disposable repository; inspect status, selected refs and fictional identity. Save the original tip and any valuable uncommitted work separately.

**Options:** --soft leaves index and working tree intact; --mixed resets index and leaves working files; --hard resets both and may overwrite or remove obstructing untracked paths. Path-level reset is different and does not move HEAD.

**When to use:** When intentionally reorganizing private commits with a saved tip and explicit choice of mode.

**When to avoid:** Avoid resetting shared history or using --hard with any unpreserved work. Never practice in the guide repository.

**Syntax**

`git reset --soft HEAD~1`

**Basic example**

`git reset --soft HEAD~1`

After saving the private tip, undo its last commit while retaining the index and working files; the tip must have a parent.

**Professional example**

`git reset --mixed HEAD~1`

In a disposable private branch with a saved tip and no valuable uncommitted work, move one commit back and review now-unstaged differences.

**State effects**

- Working tree: Conditional
- Index: Conditional
- Objects / refs / history: Conditional
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** HEAD identifies the selected commit; soft retains staged content, mixed sets index to target, hard sets tracked working content and index to target.

**Effects and side effects:** May move refs and update ORIG\_HEAD and reflogs; mode determines index and file changes. No remote update occurs.

**Common errors:** Confusing reset of a path with moving a branch, or expecting reflog to recover discarded uncommitted edits.

**Alternatives:** Use git restore --staged for path-level unstaging; use git revert to undo a shared commit without removing it from history.

**Recovery:** Inspect saved refs and reflog; create a recovery branch at the verified old tip if it still exists. Discarded unstaged or untracked work may be unrecoverable.

**Version and dependencies:** Standard Git syntax; use Git 2.40 or newer for guide labs. Trusted local configuration and hooks may affect execution.

**Related lessons**

- [history-and-recovery/01-recovery-safety](../../history-and-recovery/01-recovery-safety/README.md)
- [history-and-recovery/03-reset](../../history-and-recovery/03-reset/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-reset>

## git-revert

**`git revert`**

**Type:** Native command

**Level:** Intermediate

**Find by intent:** Undo changes, Protect history

**Risk:** State change. Inverse changes can conflict with later work; review the result and tests. Reverting a secret does not erase it from history.

**Purpose:** Create a new commit reversing the changes introduced by a selected commit.

**Prerequisites:** Use an owned disposable repository; inspect status, selected refs and fictional identity. Save the original tip and any valuable uncommitted work separately.

**Options:** --no-edit uses the generated message; --no-commit prepares changes without committing; reverting a merge requires a carefully chosen mainline parent with -m.

**When to use:** When correcting a recorded change while preserving shared ancestry.

**When to avoid:** Avoid reverting an unreviewed commit or merge without understanding dependencies and future integration effects.

**Syntax**

`git revert HEAD`

**Basic example**

`git revert HEAD`

In a clean practice branch, reverse the latest ordinary commit after verifying it.

**Professional example**

`git revert --no-edit HEAD`

Record an inverse change on an approved local correction branch; inspect the generated message and result.

**State effects**

- Working tree: Conditional
- Index: Conditional
- Objects / refs / history: Conditional
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** On successful ordinary execution, a new inverse-change commit advances HEAD; the original commit remains in history. Conflicts may pause the operation.

**Effects and side effects:** May change files, index, objects, refs and sequencer metadata; no automatic push occurs.

**Common errors:** Expecting the original commit to disappear or the entire repository to become identical to an earlier snapshot.

**Alternatives:** Use a normal corrective commit for selective fixes; reset only for carefully reviewed private history.

**Recovery:** If the operation pauses, inspect status and use its matching --continue after reviewed resolution, or --abort after preserving desired edits. For a completed operation, assess a new corrective commit rather than rewriting shared history.

**Version and dependencies:** Standard Git syntax; use Git 2.40 or newer for guide labs. Trusted local configuration and hooks may affect execution.

**Related lessons**

- [history-and-recovery/01-recovery-safety](../../history-and-recovery/01-recovery-safety/README.md)
- [history-and-recovery/04-revert](../../history-and-recovery/04-revert/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-revert>

## git-reflog

**`git reflog`**

**Type:** Native command

**Level:** Intermediate

**Find by intent:** Recover work, Inspect references, Inspect history

**Risk:** Read-only. Read-only inspection only; reflog output may contain private messages and identities. Recovery is not guaranteed.

**Purpose:** Inspect locally recorded movements of references to locate previous commit IDs.

**Prerequisites:** Use an owned disposable repository; inspect status, selected refs and fictional identity. Save the original tip and any valuable uncommitted work separately.

**Options:** Default invocation shows HEAD reflog; show with a named ref selects that log. Expire and delete are separate modifying operations not used here.

**When to use:** When investigating a previous branch tip after an accidental local ref movement.

**When to avoid:** Do not assume every ref has a reflog or entries persist forever; it is not a backup of unstaged edits.

**Syntax**

`git reflog show HEAD`

**Basic example**

`git reflog`

Inspect recent local HEAD movements after a practice reset.

**Professional example**

`git reflog show main`

Investigate previous tips of the lab main before choosing a recovery branch.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Displays recorded ref movements and associated commit IDs where logs exist; entries can expire.

**Effects and side effects:** Shown inspection does not change files, index, refs, objects or remote; logs belong to the local repository.

**Common errors:** Assuming HEAD@{1} always identifies the desired commit or another clone has identical reflog entries.

**Alternatives:** Inspect saved branch names, tags or backups first when available.

**Recovery:** Verify the candidate with git show and create a recovery branch at the exact ID if available. Do not reset directly to a guessed reflog position.

**Version and dependencies:** Standard Git syntax; use Git 2.40 or newer for guide labs. Trusted local configuration and hooks may affect execution.

**Related lessons**

- [history-and-recovery/01-recovery-safety](../../history-and-recovery/01-recovery-safety/README.md)
- [history-and-recovery/05-reflog](../../history-and-recovery/05-reflog/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-reflog>

## git-cherry-pick

**`git cherry-pick`**

**Type:** Native command

**Level:** Intermediate

**Find by intent:** Integrate changes, Recover work

**Risk:** State change. Review source diff, target context and dependencies; replay can conflict or introduce duplicate behavior.

**Purpose:** Apply the changes introduced by a selected commit to the current branch, ordinarily creating a new commit.

**Prerequisites:** Use an owned disposable repository; inspect status, selected refs and fictional identity. Save the original tip and any valuable uncommitted work separately.

**Options:** -x records the source commit ID in suitable successful commit messages; --no-commit prepares changes without recording a commit. Merge commits need a mainline parent choice.

**When to use:** When transferring a reviewed independent correction without integrating the entire source branch.

**When to avoid:** Avoid selecting commits without checking prerequisites or duplicating changes already integrated.

**Syntax**

`git cherry-pick FIX_ID`

**Basic example**

`git cherry-pick FIX_ID`

Replace FIX\_ID with the reviewed ID of an ordinary commit from another local practice branch.

**Professional example**

`git cherry-pick -x FIX_ID`

In a local backport simulation, substitute a verified independent fix ID and test the result.

**State effects**

- Working tree: Conditional
- Index: Conditional
- Objects / refs / history: Conditional
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** Ordinary success creates a new commit based on current HEAD, typically with a different ID; conflicts or empty changes may pause or require a decision.

**Effects and side effects:** May update working tree, index, objects, refs and sequencer state; source branch is not moved.

**Common errors:** Assuming cherry-pick retains source ancestry or automatically includes prerequisite commits.

**Alternatives:** Use merge if all source ancestry should be integrated; use a manually reviewed correction if the change requires adaptation.

**Recovery:** If the operation pauses, inspect status and use its matching --continue after reviewed resolution, or --abort after preserving desired edits. For a completed operation, assess a new corrective commit rather than rewriting shared history.

**Version and dependencies:** Standard Git syntax; use Git 2.40 or newer for guide labs. Trusted local configuration and hooks may affect execution.

**Related lessons**

- [history-and-recovery/01-recovery-safety](../../history-and-recovery/01-recovery-safety/README.md)
- [history-and-recovery/07-cherry-pick](../../history-and-recovery/07-cherry-pick/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-cherry-pick>

## git-stash-push

**`git stash push`**

**Type:** Subcommand

**Level:** Intermediate

**Find by intent:** Shelve work temporarily, Switch work context

**Risk:** State change. Stash is local temporary storage, not a backup. Applying can conflict; review status and preserve valuable work before changing state.

**Purpose:** Save selected local modifications in a stash entry and roll the corresponding working and index changes back toward HEAD.

**Prerequisites:** Use an owned disposable repository with an existing commit; review status, stash list and the intended entry. Preserve valuable work separately.

**Options:** -m names the entry; -u includes untracked files but not ignored files; -a also includes ignored files and is not used here. --keep-index retains staged changes in the working state.

**When to use:** When temporarily setting aside unfinished work in a controlled local context.

**When to avoid:** Avoid relying on stash as the only copy of important work or stashing sensitive files.

**Syntax**

`git stash push -m "draft notes"`

**Basic example**

`git stash push -m "draft notes"`

Save tracked practice edits temporarily.

**Professional example**

`git stash push -u -m "review draft"`

After checking for sensitive files, also include an intended untracked fictional draft.

**State effects**

- Working tree: Conditional
- Index: Conditional
- Objects / refs / history: Conditional
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** If matching changes exist, a stash entry is recorded; selected changes are removed from working state as options allow. Untracked files remain unless included.

**Effects and side effects:** May create local commit objects and update refs/stash and its reflog, index and working files; current branch tip and remote stay unchanged.

**Common errors:** Assuming a default stash includes untracked and ignored files, or that a clean status proves every desired file was saved.

**Alternatives:** Use a private temporary branch with a reviewed commit for work that needs a more durable named reference.

**Recovery:** Inspect git stash list and git stash show; use apply on the verified entry before dropping it. Missing or expired objects may not be recoverable.

**Version and dependencies:** Standard Git syntax; use Git 2.40 or newer for guide labs. Trusted local configuration and hooks may affect execution.

**Related lessons**

- [history-and-recovery/01-recovery-safety](../../history-and-recovery/01-recovery-safety/README.md)
- [history-and-recovery/06-stash](../../history-and-recovery/06-stash/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-stash>

## git-stash-apply

**`git stash apply`**

**Type:** Subcommand

**Level:** Intermediate

**Find by intent:** Shelve work temporarily, Recover work

**Risk:** State change. Stash is local temporary storage, not a backup. Applying can conflict; review status and preserve valuable work before changing state.

**Purpose:** Reapply a selected stash entry without removing it from the stash list.

**Prerequisites:** Use an owned disposable repository with an existing commit; review status, stash list and the intended entry. Preserve valuable work separately.

**Options:** --index also attempts to restore the staged state; specify the verified entry explicitly. Without --index, the original staging split is not guaranteed.

**When to use:** When restoring shelved work while retaining a copy of its stash entry for verification.

**When to avoid:** Avoid applying over valuable uncommitted changes or selecting an entry by position without verifying it.

**Syntax**

`git stash apply "stash@{0}"`

**Basic example**

`git stash apply "stash@{0}"`

Inspect list and show first, then apply the verified latest practice entry to a clean checkout.

**Professional example**

`git stash apply --index "stash@{0}"`

On a clean compatible lab branch, attempt to restore both staged and unstaged work and inspect their differences.

**State effects**

- Working tree: Conditional
- Index: Conditional
- Objects / refs / history: Conditional
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** Applies saved changes to working state when possible; may conflict. The stash entry remains available after ordinary apply.

**Effects and side effects:** May update working tree and index and conflict metadata; stash ref is not dropped and current branch tip is not advanced.

**Common errors:** Assuming apply also drops the entry or that --index always restores the exact index despite conflicts.

**Alternatives:** Use pop only when successful application should also remove the stash entry; prefer apply while verifying recovered work.

**Recovery:** If application conflicts, inspect unmerged paths and the retained stash; preserve resolution work before cleanup. There is no general stash abort; avoid blind reset or repeated application.

**Version and dependencies:** Standard Git syntax; use Git 2.40 or newer for guide labs. Trusted local configuration and hooks may affect execution.

**Related lessons**

- [history-and-recovery/01-recovery-safety](../../history-and-recovery/01-recovery-safety/README.md)
- [history-and-recovery/06-stash](../../history-and-recovery/06-stash/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-stash>

## git-stash-pop

**`git stash pop`**

**Type:** Subcommand

**Level:** Intermediate

**Find by intent:** Shelve work temporarily, Recover work

**Risk:** Destructive. Pop can remove the named access to the saved work on success. Keep an independent copy or prefer apply if uncertain.

**Purpose:** Reapply a stash entry and remove it from the stash list only when application succeeds.

**Prerequisites:** Use an owned disposable repository with an existing commit; review status, stash list and the intended entry. Preserve valuable work separately.

**Options:** --index attempts to restore staged state too; specify the verified entry. git stash drop removes an entry without applying and requires separate review.

**When to use:** When resuming a verified temporary change and the stash copy is no longer needed after success.

**When to avoid:** Avoid when the stash is the only copy of important work or the target already has unpreserved changes.

**Syntax**

`git stash pop "stash@{0}"`

**Basic example**

`git stash pop "stash@{0}"`

After verifying the disposable stash and clean target, resume work and inspect both status and stash list.

**Professional example**

`git stash pop --index "stash@{0}"`

Restore a reviewed temporary lab entry including its staging state, and confirm the result before continuing.

**State effects**

- Working tree: Conditional
- Index: Conditional
- Objects / refs / history: Conditional
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** Successful application removes the selected entry; a conflict retains it for further review, with possible partial changes in the checkout.

**Effects and side effects:** May change working tree, index, refs/stash and reflog; branch tip and remote are unchanged by normal operation.

**Common errors:** Assuming the stash is removed after a conflict or that successful pop leaves a reusable entry at the same position.

**Alternatives:** Prefer apply, inspect the restored changes and keep the entry until satisfied; only then consider a verified drop.

**Recovery:** If conflict occurs, verify the entry remains and inspect unmerged paths. After success, preserve restored work promptly; recovery of a removed entry from remaining objects is not guaranteed.

**Version and dependencies:** Standard Git syntax; use Git 2.40 or newer for guide labs. Trusted local configuration and hooks may affect execution.

**Related lessons**

- [history-and-recovery/01-recovery-safety](../../history-and-recovery/01-recovery-safety/README.md)
- [history-and-recovery/06-stash](../../history-and-recovery/06-stash/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-stash>


---

<!-- navigation-footer -->
[Previous](../08-remotes-and-synchronization/README.md) · [Index](../README.md) · [Next](../10-search-and-troubleshooting/README.md)
<!-- /navigation-footer -->
