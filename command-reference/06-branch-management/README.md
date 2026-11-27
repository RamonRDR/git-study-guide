# 06 Branch Management

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../05-history-and-comparison/README.md) · [Index](../README.md) · [Next](../07-merge-rebase-and-conflicts/README.md)
<!-- /navigation -->

Generated from canonical catalog JSON. Edit the records, not this page.

Reference entries describe commands and operations, not a sequence to run. Use disposable repositories for practice. Hosted operations are optional.

**Total distinct entries: 10**

- [`git branch --list`](#git-branch-list)
- [`git branch NAME`](#git-branch-create)
- [`git branch --show-current`](#git-branch-show-current)
- [`git switch`](#git-switch)
- [`git switch -c`](#git-switch-create)
- [`git switch --detach`](#git-switch-detach)
- [`git branch -m`](#git-branch-rename)
- [`git branch -d`](#git-branch-delete)
- [`git branch --merged`](#git-branch-merged)
- [`git branch --set-upstream-to`](#git-branch-upstream)

## git-branch-list

**`git branch --list`**

**Type:** Option usage

**Level:** Beginner

**Find by intent:** Manage branches, Inspect references

**Risk:** Read-only. Read-only inspection; check branch names before sharing output.

**Purpose:** List local branch names, optionally filtered by a pattern.

**Prerequisites:** Use an owned disposable repository with an existing commit. Inspect status and refs before operating.

**Options:** --list selects listing explicitly; -a includes remote-tracking refs and -vv shows upstream information and other details.

**When to use:** When inspecting available branches before selecting or cleaning up work.

**When to avoid:** Do not treat the local list as live remote inventory.

**Syntax**

`git branch --list "feat/*"`

**Basic example**

`git branch --list`

Inspect local branches.

**Professional example**

`git branch --list "feat/*"`

Inspect local feature branches without creating one.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Displays matching branches; the checked-out local branch is marked with an asterisk in normal output.

**Effects and side effects:** No tracked content, staged snapshot, local refs or remote state is changed by this inspection.

**Common errors:** Omitting --list with a name or pattern can be interpreted as branch creation.

**Alternatives:** Use git branch --show-current for only the current branch or git show-ref to inspect IDs.

**Recovery:** No recovery is needed for listing; inspect the selected reference or filter if output is unexpected.

**Version and dependencies:** Standard Git syntax documented for Git 2.34; no optional tool is required.

**Related lessons**

- [branches/01-create-and-switch](../../branches/01-create-and-switch/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-branch/2.34.0>

## git-branch-create

**`git branch NAME`**

**Type:** Option usage

**Level:** Beginner

**Find by intent:** Manage branches, Work in parallel

**Risk:** State change. Verify the name and start point; do not use force to resolve name collisions.

**Purpose:** Create a named local branch at an existing commit without switching to it.

**Prerequisites:** Use an owned disposable repository with an existing commit. Inspect status and refs before operating.

**Options:** Supply a new name and optional start point; without a start point use HEAD. --no-track prevents automatic upstream configuration.

**When to use:** When preparing an independent line of work or preserving a commit.

**When to avoid:** Avoid creating a branch from an unverified revision or overwriting an existing branch with -f.

**Syntax**

`git branch feat/notes main`

**Basic example**

`git branch feat/notes`

Create a local branch at current HEAD.

**Professional example**

`git branch feat/review main`

Create a branch at the verified existing main tip.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Changes
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** A new local ref points to the selected commit; HEAD remains where it was.

**Effects and side effects:** Adds a branch ref and possibly its reflog or tracking configuration; working files and index are unchanged.

**Common errors:** Assuming creating a branch also switches to it or copies a folder.

**Alternatives:** Use git switch -c to create and select in one operation.

**Recovery:** Inspect both refs; if a new unused branch is mistaken, remove it only after confirming its tip is reachable from an intended surviving ref.

**Version and dependencies:** Standard Git syntax documented for Git 2.34; no optional tool is required.

**Related lessons**

- [branches/01-create-and-switch](../../branches/01-create-and-switch/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-branch/2.34.0>

## git-branch-show-current

**`git branch --show-current`**

**Type:** Option usage

**Level:** Beginner

**Find by intent:** Inspect repository state, Manage branches

**Risk:** Read-only. Read-only inspection; check branch names before sharing output.

**Purpose:** Print the current local branch name when HEAD is attached.

**Prerequisites:** Use an owned disposable repository with an existing commit. Inspect status and refs before operating.

**Options:** --show-current selects this single-name output; it is empty in detached HEAD.

**When to use:** When confirming the active branch before a commit or switch.

**When to avoid:** Do not assume empty output is a branch name or proof of command failure.

**Syntax**

`git branch --show-current`

**Basic example**

`git branch --show-current`

Check which branch is active.

**Professional example**

`git branch --show-current`

Before committing, verify the expected feature branch is selected.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Displays the branch name or no name if HEAD is detached.

**Effects and side effects:** No tracked content, staged snapshot, local refs or remote state is changed by this inspection.

**Common errors:** Assuming it returns the commit ID or remote upstream.

**Alternatives:** Use git symbolic-ref --quiet --short HEAD for a symbolic HEAD check, or git rev-parse HEAD for the commit ID.

**Recovery:** No recovery is needed for listing; inspect the selected reference or filter if output is unexpected.

**Version and dependencies:** Git 2.22 or newer supports --show-current; the guide uses Git 2.40 or newer for labs.

**Related lessons**

- [branches/01-create-and-switch](../../branches/01-create-and-switch/README.md)
- [branches/05-detached-head](../../branches/05-detached-head/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-branch/2.34.0>

## git-switch

**`git switch`**

**Type:** Native command

**Level:** Beginner

**Find by intent:** Switch work context, Manage branches

**Risk:** State change. Compatible edits can carry over; conflicting edits can block switching. Do not use force or discard options.

**Purpose:** Select an existing branch for subsequent work.

**Prerequisites:** Use an owned disposable repository with clean status, an existing commit and trusted local hooks. Preserve valuable work first.

**Options:** --no-guess disables automatic creation based on a unique matching remote-tracking branch; - is shorthand for the previous checkout.

**When to use:** When changing between existing local lines of work.

**When to avoid:** Avoid switching away from unsaved detached commits or forcing past conflicting edits.

**Syntax**

`git switch main`

**Basic example**

`git switch main`

Return to existing local main after preserving work.

**Professional example**

`git switch --no-guess feat/notes`

Select a verified existing local feature branch without automatic tracking branch creation.

**State effects**

- Working tree: Conditional
- Index: Conditional
- Objects / refs / history: Changes
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** HEAD points to the selected branch; tracked files and index reflect the new context with compatible edits preserved when possible.

**Effects and side effects:** Selects HEAD and updates the index and working files as needed; configured post-checkout hooks may affect other local state. No push or merge occurs.

**Common errors:** Confusing switching with merging or expecting all uncommitted edits to remain on the old branch.

**Alternatives:** Older Git uses git checkout with a verified branch name; prefer switch for clarity in current labs.

**Recovery:** If a switch fails, inspect status and preserve edits; do not force it. Return to the original branch when clean and save any desired detached commits first.

**Version and dependencies:** Git 2.23 introduced switch; the guide's practice baseline is Git 2.40 or newer. The shown syntax is documented in the Git 2.35 manual.

**Related lessons**

- [branches/01-create-and-switch](../../branches/01-create-and-switch/README.md)
- [branches/03-switch-safety-and-naming](../../branches/03-switch-safety-and-naming/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-switch/2.35.0>

## git-switch-create

**`git switch -c`**

**Type:** Option usage

**Level:** Beginner

**Find by intent:** Manage branches, Switch work context, Work in parallel

**Risk:** State change. Compatible edits can carry over; conflicting edits can block switching. Do not use force or discard options.

**Purpose:** Create a new local branch and switch to it as one operation.

**Prerequisites:** Use an owned disposable repository with clean status, an existing commit and trusted local hooks. Preserve valuable work first.

**Options:** -c requires a new name and accepts an optional start point; do not confuse it with -C, which can reset an existing branch.

**When to use:** When starting an isolated task or naming a detached commit before leaving it.

**When to avoid:** Avoid using an unverified start point or overwriting an existing name.

**Syntax**

`git switch -c feat/notes main`

**Basic example**

`git switch -c feat/notes`

Start a task at the current commit.

**Professional example**

`git switch -c feat/review main`

Start a review task from a verified local main commit.

**State effects**

- Working tree: Conditional
- Index: Conditional
- Objects / refs / history: Changes
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** On success, the new branch points at the chosen start point and HEAD selects it; if switching fails the branch is not created.

**Effects and side effects:** Selects HEAD and updates the index and working files as needed; configured post-checkout hooks may affect other local state. No push or merge occurs.

**Common errors:** Using -C to bypass a collision or assuming the new branch always starts at main.

**Alternatives:** Use git branch NAME START and git switch NAME separately when creation without switching is useful.

**Recovery:** Verify HEAD and both refs; preserve any new commits before returning to the original branch or cleaning up.

**Version and dependencies:** Git 2.23 introduced switch; the guide's practice baseline is Git 2.40 or newer. The shown syntax is documented in the Git 2.35 manual.

**Related lessons**

- [branches/01-create-and-switch](../../branches/01-create-and-switch/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-switch/2.35.0>

## git-switch-detach

**`git switch --detach`**

**Type:** Option usage

**Level:** Intermediate

**Find by intent:** Switch work context, Inspect history, Recover work

**Risk:** State change. Detached commits may become unreachable; recovery is not guaranteed. Preserve them before switching away.

**Purpose:** Select a commit directly without attaching HEAD to a branch.

**Prerequisites:** Use an owned disposable repository with clean status, an existing commit and trusted local hooks. Preserve valuable work first.

**Options:** --detach explicitly requests detached HEAD; use a verified commit or tag that resolves to a commit.

**When to use:** When inspecting historical snapshots or performing a disposable experiment.

**When to avoid:** Avoid leaving desired commits unnamed or treating detached work as updates to main.

**Syntax**

`git switch --detach HEAD~1`

**Basic example**

`git switch --detach HEAD~1`

Inspect the first parent of a non-root current commit.

**Professional example**

`git switch --detach v1.0.0`

Inspect an existing local version tag that resolves to a commit.

**State effects**

- Working tree: Conditional
- Index: Conditional
- Objects / refs / history: Changes
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** HEAD points directly at the commit; branch tips are unchanged and --show-current prints no name.

**Effects and side effects:** Selects HEAD and updates the index and working files as needed; configured post-checkout hooks may affect other local state. No push or merge occurs.

**Common errors:** Assuming commits created while detached advance the previously selected branch.

**Alternatives:** Create a temporary named branch instead if changes are expected to be retained.

**Recovery:** Before leaving, use git switch -c with an unused name to retain desired commits; if already left, inspect reflog and name the verified commit if available.

**Version and dependencies:** Git 2.23 introduced switch; the guide's practice baseline is Git 2.40 or newer. The shown syntax is documented in the Git 2.35 manual.

**Related lessons**

- [branches/05-detached-head](../../branches/05-detached-head/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-switch/2.35.0>

## git-branch-rename

**`git branch -m`**

**Type:** Option usage

**Level:** Intermediate

**Find by intent:** Manage branches

**Risk:** State change. Check both names and downstream dependencies; avoid force replacement.

**Purpose:** Rename a local branch and move its associated configuration and reflog when present.

**Prerequisites:** Use an owned disposable repository with an existing commit. Inspect status and refs before operating.

**Options:** -m accepts old and new names or just a new name for the current branch; -M forces replacement and is not used here.

**When to use:** When correcting a private branch name to match team conventions.

**When to avoid:** Avoid renaming shared branches without coordination or using -M to replace another branch.

**Syntax**

`git branch -m feat/old feat/new`

**Basic example**

`git branch -m feat/notes feat/docs`

Rename an existing private branch to an unused name.

**Professional example**

`git branch -m feat/review`

Rename the currently checked-out private branch to an unused name.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Changes
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** The new local name identifies the same tip; the old name disappears. If current, HEAD follows the renamed branch.

**Effects and side effects:** Moves local refs, configuration and reflog where present, not commit contents or remote branch names.

**Common errors:** Expecting the remote branch or upstream target name to be renamed automatically.

**Alternatives:** Keep the existing name when collaborators or automation depend on it.

**Recovery:** Verify the tip, upstream and free original name before renaming back with -m; coordinate if already shared.

**Version and dependencies:** Standard Git syntax documented for Git 2.34; no optional tool is required.

**Related lessons**

- [branches/03-switch-safety-and-naming](../../branches/03-switch-safety-and-naming/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-branch/2.34.0>

## git-branch-delete

**`git branch -d`**

**Type:** Option usage

**Level:** Intermediate

**Find by intent:** Manage branches, Protect history

**Risk:** Destructive. Deletion can remove the last convenient name for work; never use -D to bypass a refusal without separate assessment. Recovery is not guaranteed.

**Purpose:** Delete a local branch with a merged-status safeguard.

**Prerequisites:** Use an owned disposable repository; verify the target branch is not checked out in any worktree and its tip is reachable from the intended surviving branch. Record its ID.

**Options:** -d checks full merge into its configured upstream, or HEAD if no upstream exists; -D bypasses that guard and is not an alternative when unsure.

**When to use:** When cleaning up private branches whose commits are retained by the intended target.

**When to avoid:** Avoid deleting work not verified as reachable, or forcing deletion after a squash merge without reviewing the content and history.

**Syntax**

`git branch -d feat/notes`

**Basic example**

`git branch -d feat/notes`

With main selected, remove only a verified contained private branch without upstream.

**Professional example**

`git branch -d feat/review`

After confirming ancestry, upstream and worktree status, remove the local review branch.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Changes
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** The local ref and its branch reflog, if present, are removed on success; otherwise Git may refuse.

**Effects and side effects:** Removes a local name and associated metadata; does not immediately erase commit objects or remove remote branches.

**Common errors:** Assuming -d always checks main or that squash merging preserves commit ancestry.

**Alternatives:** Keep the branch if uncertain; inspect git branch --merged main and git log main..NAME first.

**Recovery:** If the recorded commit still exists, recreate a branch at its verified ID; old configuration and reflog are not automatically restored.

**Version and dependencies:** Standard Git syntax documented for Git 2.34; no optional tool is required.

**Related lessons**

- [branches/04-safe-local-deletion](../../branches/04-safe-local-deletion/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-branch/2.34.0>

## git-branch-merged

**`git branch --merged`**

**Type:** Option usage

**Level:** Intermediate

**Find by intent:** Manage branches, Inspect history, Protect history

**Risk:** Read-only. Read-only inspection; check branch names before sharing output.

**Purpose:** List branches whose tip commits are reachable from a selected commit.

**Prerequisites:** Use an owned disposable repository with an existing commit. Inspect status and refs before operating.

**Options:** --merged defaults to HEAD; --no-merged selects the opposite set. Supply an explicit target such as main.

**When to use:** When reviewing ancestry before local branch cleanup.

**When to avoid:** Do not equate absence from the list with absence of equivalent changes after squash or cherry-pick.

**Syntax**

`git branch --merged main`

**Basic example**

`git branch --merged main`

Inspect local tips contained in existing main.

**Professional example**

`git branch --no-merged main`

Identify local tips not contained in main before reviewing cleanup candidates.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Shows selected branch tips that are ancestors of the target or equal to it.

**Effects and side effects:** No tracked content, staged snapshot, local refs or remote state is changed by this inspection.

**Common errors:** Assuming the list proves a branch can be deleted regardless of worktrees or upstream configuration.

**Alternatives:** Use git merge-base --is-ancestor NAME main to test one verified branch against main.

**Recovery:** No recovery is needed for listing; inspect the selected reference or filter if output is unexpected.

**Version and dependencies:** Standard Git syntax documented for Git 2.34; no optional tool is required.

**Related lessons**

- [branches/04-safe-local-deletion](../../branches/04-safe-local-deletion/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-branch/2.34.0>

## git-branch-upstream

**`git branch --set-upstream-to`**

**Type:** Option usage

**Level:** Intermediate

**Find by intent:** Manage branches, Synchronize repositories, Configure Git

**Risk:** State change. Wrong tracking can affect later pull and push behavior depending on configuration; verify git branch -vv before synchronizing.

**Purpose:** Configure which branch an existing local branch tracks as upstream.

**Prerequisites:** Use an owned disposable clone or local remote lab. Verify local branch, existing remote-tracking ref and intended upstream relationship; do not contact a real service for practice.

**Options:** -u is short for --set-upstream-to; omit the local branch argument to configure the current branch. --unset-upstream removes tracking configuration.

**When to use:** When a branch needs an explicit verified tracking relationship for status and synchronization.

**When to avoid:** Avoid selecting a different integration target accidentally or assuming it performs a fetch or push.

**Syntax**

`git branch --set-upstream-to=origin/main main`

**Basic example**

`git branch --set-upstream-to=origin/main main`

In a local clone lab, connect existing main to its verified origin/main tracking ref.

**Professional example**

`git branch -u origin/feat/notes feat/notes`

After checking both existing refs, correct a private feature branch tracking setting in the local lab.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Changes

**Expected result:** Local tracking configuration identifies the chosen upstream; git branch -vv can display the relationship.

**Effects and side effects:** Changes local branch configuration; no ref movement, checkout or network transfer is required.

**Common errors:** Confusing an upstream setting with remote publication or expecting tracking alone to keep refs current.

**Alternatives:** Use explicit remote and ref arguments for fetch or push when tracking defaults are not desired.

**Recovery:** Record the previous upstream; restore it explicitly or use git branch --unset-upstream for the local branch if none existed.

**Version and dependencies:** Standard Git syntax documented for Git 2.34; no optional tool is required.

**Related lessons**

- [remote-repositories/02-fetch-and-tracking](../../remote-repositories/02-fetch-and-tracking/README.md)
- [remote-repositories/03-pull-push-and-divergence](../../remote-repositories/03-pull-push-and-divergence/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-branch/2.34.0>


---

<!-- navigation-footer -->
[Previous](../05-history-and-comparison/README.md) · [Index](../README.md) · [Next](../07-merge-rebase-and-conflicts/README.md)
<!-- /navigation-footer -->
