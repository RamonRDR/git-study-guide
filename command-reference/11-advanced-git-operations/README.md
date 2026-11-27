# 11 Advanced Git Operations

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../10-search-and-troubleshooting/README.md) · [Index](../README.md) · [Next](../12-internals-and-plumbing/README.md)
<!-- /navigation -->

Generated from canonical catalog JSON. Edit the records, not this page.

Reference entries describe commands and operations, not a sequence to run. Use disposable repositories for practice. Hosted operations are optional.

**Total distinct entries: 9**

- [`git worktree add`](#git-worktree-add)
- [`git submodule add`](#git-submodule-add)
- [`git submodule update --init --recursive`](#git-submodule-update)
- [`git subtree add`](#git-subtree-add)
- [`git rerere`](#git-rerere)
- [`git sparse-checkout set`](#git-sparse-checkout-set)
- [`git clone --filter`](#git-clone-filter)
- [`git archive`](#git-archive)
- [`git bundle create`](#git-bundle-create)

## git-worktree-add

**`git worktree add`**

**Type:** Subcommand

**Level:** Advanced

**Find by intent:** Work in parallel, Manage branches

**Risk:** State change. Review paths, refs and local configuration first. Preserve valuable work; never test against the guide or a shared service.

**Purpose:** Create an additional linked checkout sharing a repository's objects and most refs.

**Prerequisites:** Use a clean owned disposable repository with saved work, verified local paths and refs, and trusted configuration. Use only owned local sources.

**Options:** -b creates a branch; --detach uses a detached checkout; git worktree list shows registered worktrees.

**When to use:** When working on independent tasks without repeatedly switching the original checkout.

**When to avoid:** Avoid reusing an occupied path or forcing the same branch into multiple worktrees.

**Syntax**

`git worktree add -b feat/notes ../notes-lab main`

**Basic example**

`git worktree add -b feat/notes ../notes-lab main`

Create a linked worktree at an unused sibling path and new branch.

**Professional example**

`git worktree add --detach ../review-lab main`

Inspect verified main in a separate detached checkout.

**State effects**

- Working tree: Conditional
- Index: Conditional
- Objects / refs / history: Conditional
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** Creates a linked checkout with its own HEAD and index; optional new branch is shared across worktrees.

**Effects and side effects:** Creates files and worktree metadata, possibly a new ref; original checkout content is unchanged in the shown form.

**Common errors:** Treating linked worktrees as independent clones or deleting their directories manually.

**Alternatives:** Use a separate clone when independent refs and object storage are required.

**Recovery:** Preserve any linked worktree edits, verify clean status there, then use git worktree remove with its exact path; inspect worktree list afterward.

**Version and dependencies:** Use Git 2.40 or newer for the guide's labs; verify availability with local Git help.

**Related lessons**

- [advanced-git/02-worktree](../../advanced-git/02-worktree/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-worktree>

## git-submodule-add

**`git submodule add`**

**Type:** Subcommand

**Level:** Advanced

**Find by intent:** Manage repository dependencies

**Risk:** State change. Review paths, refs and local configuration first. Preserve valuable work; never test against the guide or a shared service.

**Purpose:** Register a separate repository as a submodule pinned by a gitlink in the parent project.

**Prerequisites:** Use a clean owned disposable repository with saved work, verified local paths and refs, and trusted configuration. Use only owned local sources. For the shown relative URL, ensure the library is a sibling of the parent default remote (or of the local parent repository if no default remote exists).

**Options:** Specify repository and path; -b sets a branch preference for remote updates, not a replacement for the recorded gitlink. Relative URLs resolve against the parent repository's default remote, or its local repository when no default remote is configured; arrange sibling bare origins for clone simulations.

**When to use:** When a dependency should retain independent history and an explicit version pin.

**When to avoid:** Avoid untrusted submodule URLs, existing valuable destination files or broad protocol overrides.

**Syntax**

`git submodule add ../library.git vendor/library`

**Basic example**

`git submodule add ../library.git vendor/library`

Add an owned populated local library repository at an unused path; local file transport may need explicit lab permission.

**Professional example**

`git -c protocol.file.allow=always submodule add ../library.git vendor/library`

Only in the trusted isolated lab, allow the owned local source for this invocation.

**State effects**

- Working tree: Conditional
- Index: Conditional
- Objects / refs / history: Conditional
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** Normally creates a submodule checkout, stages .gitmodules and a gitlink; parent commit still requires review and commit.

**Effects and side effects:** Changes working files, index and local submodule configuration or objects; does not publish the parent.

**Common errors:** Assuming a submodule is copied ordinary source files or that its uncommitted changes are included in the parent commit.

**Alternatives:** Use subtree integration or a package manager when a separate checkout is undesirable.

**Recovery:** Inspect .gitmodules, staged gitlink and submodule status; preserve submodule commits before following a reviewed removal workflow. Do not simply delete its metadata.

**Version and dependencies:** Use Git 2.40 or newer for the guide's labs; verify availability with local Git help.

**Related lessons**

- [advanced-git/03-submodules](../../advanced-git/03-submodules/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-submodule>

## git-submodule-update

**`git submodule update --init --recursive`**

**Type:** Option usage

**Level:** Advanced

**Find by intent:** Manage repository dependencies, Synchronize repositories

**Risk:** State change. Review paths, refs and local configuration first. Preserve valuable work; never test against the guide or a shared service.

**Purpose:** Populate registered submodules and update their checkouts, normally to the commits recorded by the parent.

**Prerequisites:** Use a clean owned disposable repository with saved work, verified local paths and refs, and trusted configuration. Use only owned local sources. Review the resolved relative URLs before initializing; in the lab, clone from a sibling bare parent origin so that the relative library URL resolves correctly.

**Options:** --init initializes uninitialized submodules; --recursive descends into nested ones; default checkout procedure usually detaches submodule HEAD.

**When to use:** When preparing a consistent checkout of a project with pinned dependencies.

**When to avoid:** Avoid unreviewed nested URLs, unpreserved submodule changes or using --force to bypass a refusal.

**Syntax**

`git submodule update --init --recursive`

**Basic example**

`git submodule update --init --recursive`

Initialize and update registered trusted submodules to recorded commits in the lab.

**Professional example**

`git -c protocol.file.allow=always submodule update --init --recursive`

Only for reviewed owned local submodule URLs, permit local file transport for this lab invocation.

**State effects**

- Working tree: Conditional
- Index: Conditional
- Objects / refs / history: Conditional
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** May clone missing submodules, fetch objects and check out recorded commits; configured update strategies can differ.

**Effects and side effects:** Changes submodule files, index, refs and configuration; normally does not move the parent branch tip.

**Common errors:** Expecting latest remote branch versions instead of recorded commits or assuming parent status proves every nested checkout is clean.

**Alternatives:** Use git submodule status --recursive to inspect without updating.

**Recovery:** Inspect failed paths and saved submodule tips; preserve any detached commits with a named branch before retrying. Do not force blindly.

**Version and dependencies:** Use Git 2.40 or newer for the guide's labs; verify availability with local Git help.

**Related lessons**

- [advanced-git/03-submodules](../../advanced-git/03-submodules/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-submodule>

## git-subtree-add

**`git subtree add`**

**Type:** External tool

**Level:** Advanced

**Find by intent:** Manage repository dependencies, Integrate changes

**Risk:** State change. Review paths, refs and local configuration first. Preserve valuable work; never test against the guide or a shared service.

**Purpose:** Import another repository's content into a directory of the current project using the optional subtree helper.

**Prerequisites:** Use a clean owned disposable repository with saved work, verified local paths and refs, and trusted configuration. Use only owned local sources.

**Options:** --prefix selects destination; --squash combines imported history rather than retaining every source commit in target ancestry.

**When to use:** When versioning dependency content directly within the parent checkout while retaining a synchronization workflow.

**When to avoid:** Avoid an occupied prefix, dirty state or import without reviewing licensing and source content.

**Syntax**

`git subtree add --prefix=vendor/library ../library.git main --squash`

**Basic example**

`git subtree add --prefix=vendor/library ../library.git main --squash`

Import an owned local source branch at an unused prefix.

**Professional example**

`git subtree add --prefix=vendor/tools ../tools.git main --squash`

Integrate a reviewed local tools snapshot under a new directory.

**State effects**

- Working tree: Conditional
- Index: Conditional
- Objects / refs / history: Conditional
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** On success creates integration history and imports source content under the selected prefix.

**Effects and side effects:** May fetch objects, create commits, advance current branch and update index and working tree.

**Common errors:** Confusing subtree with submodule or assuming --squash produces no integration commit.

**Alternatives:** Use submodule for separate pinned checkout or a package manager for published dependencies.

**Recovery:** Inspect saved original tip and resulting ancestry; if unsuitable, preserve work and choose a reviewed private recovery or shared correction.

**Version and dependencies:** Git subtree is an optional distributed helper; verify git subtree availability before use. Use Git 2.40 or newer for labs.

**Related lessons**

- [advanced-git/04-subtree](../../advanced-git/04-subtree/README.md)

**Official documentation**

- <https://github.com/git/git/tree/master/contrib/subtree>

## git-rerere

**`git rerere`**

**Type:** Native command

**Level:** Advanced

**Find by intent:** Resolve conflicts

**Risk:** State change. Review paths, refs and local configuration first. Preserve valuable work; never test against the guide or a shared service.

**Purpose:** Record and reuse conflict resolutions for matching conflict patterns.

**Prerequisites:** Use a clean owned disposable repository with saved work, verified local paths and refs, and trusted configuration. Use only owned local sources.

**Options:** Enable rerere.enabled locally in the lab; git rerere status and diff inspect current records; autoupdate may stage reused results.

**When to use:** When repeatedly resolving similar conflicts in private integration workflows.

**When to avoid:** Avoid blindly accepting reused resolutions or sharing a resolution cache containing sensitive material.

**Syntax**

`git rerere`

**Basic example**

`git rerere`

In a disposable repeated-conflict lab, inspect and record or reuse resolution as appropriate.

**Professional example**

`git rerere`

After reviewing a repeated conflict, let enabled rerere reuse a recorded resolution and inspect it.

**State effects**

- Working tree: Conditional
- Index: Conditional
- Objects / refs / history: Conditional
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** May record conflict preimages and resolutions or apply a previously recorded match; index may update depending on configuration.

**Effects and side effects:** May change resolution cache and working files, and possibly index; ordinary rerere does not create a new branch commit.

**Common errors:** Assuming matching conflict text guarantees semantic correctness.

**Alternatives:** Resolve manually and review diff and tests when reuse is unsafe.

**Recovery:** Inspect rerere diff and status; correct and stage reviewed content. Use rerere forget only for the verified affected path when replacing a bad recorded resolution.

**Version and dependencies:** Use Git 2.40 or newer for the guide's labs; verify availability with local Git help.

**Related lessons**

- [advanced-git/06-rerere](../../advanced-git/06-rerere/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-rerere>

## git-sparse-checkout-set

**`git sparse-checkout set`**

**Type:** Subcommand

**Level:** Advanced

**Find by intent:** Limit checkout or clone, Inspect files

**Risk:** State change. Review paths, refs and local configuration first. Preserve valuable work; never test against the guide or a shared service.

**Purpose:** Configure a sparse working tree containing selected paths instead of every tracked path.

**Prerequisites:** Use a clean owned disposable repository with saved work, verified local paths and refs, and trusted configuration. Use only owned local sources.

**Options:** --cone selects directory-based rules; list displays selections; disable returns to a full checkout.

**When to use:** When only part of a large repository is needed for current work.

**When to avoid:** Avoid changing sparse patterns with unsaved valuable edits or assuming omitted paths were deleted from history.

**Syntax**

`git sparse-checkout set --cone docs`

**Basic example**

`git sparse-checkout set --cone docs`

Select an existing docs directory in a clean disposable checkout.

**Professional example**

`git sparse-checkout set --cone src tests`

Limit materialized directory content to selected existing source and test trees, plus cone rules.

**State effects**

- Working tree: Conditional
- Index: Conditional
- Objects / refs / history: Conditional
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** Working tree materializes selected paths according to cone rules, including some ancestor-level files; other tracked paths may be absent.

**Effects and side effects:** Updates sparse configuration, index and working tree; does not rewrite committed history in ordinary complete local repository.

**Common errors:** Confusing sparse checkout with shallow or partial clone and assuming only the named directories will be visible.

**Alternatives:** Use a full checkout if tools need all tracked files; partial clone controls object transfer separately.

**Recovery:** Preserve edits, inspect sparse-checkout list and use sparse-checkout disable to restore full materialization when safe.

**Version and dependencies:** Use Git 2.40 or newer for the guide's labs; verify availability with local Git help.

**Related lessons**

- [advanced-git/07-sparse-checkout](../../advanced-git/07-sparse-checkout/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-sparse-checkout>

## git-clone-filter

**`git clone --filter`**

**Type:** Option usage

**Level:** Advanced

**Find by intent:** Limit checkout or clone, Create a repository

**Risk:** State change. Review paths, refs and local configuration first. Preserve valuable work; never test against the guide or a shared service.

**Purpose:** Request a partial clone that omits selected object types initially when the source supports filtering.

**Prerequisites:** Use a disposable parent, unused destination and owned bare source configured locally with uploadpack.allowFilter=true; verify source path and capability.

**Options:** --filter=blob:none requests omission of blobs until needed; --no-checkout avoids initial checkout; --no-local uses transport rather than local copy optimization.

**When to use:** When reducing initial object transfer from a supported large source.

**When to avoid:** Avoid relying on missing objects being available offline or assuming every server honors filters.

**Syntax**

`git clone --no-local --filter=blob:none --no-checkout origin.git partial-lab`

**Basic example**

`git clone --no-local --filter=blob:none --no-checkout origin.git partial-lab`

From a disposable parent, clone an owned local bare source configured to permit filtering.

**Professional example**

`git clone --no-local --filter=blob:none origin.git review-lab`

Clone an owned filter-capable source; checkout may fetch needed blobs immediately.

**State effects**

- Working tree: Conditional
- Index: Conditional
- Objects / refs / history: Conditional
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** Creates a local partial clone with promisor configuration when supported; required missing objects may be fetched later.

**Effects and side effects:** Creates local repository and may materialize files and fetch blobs; does not change source refs.

**Common errors:** Confusing --filter with --depth, or treating successful clone as proof the server applied the filter.

**Alternatives:** Use full clone for reliable offline object access; use sparse-checkout for working tree selection.

**Recovery:** Inspect clone warnings and promisor configuration; if filtering is unsupported, use a new clean destination with a full clone or verified capable source.

**Version and dependencies:** Use Git 2.40 or newer for the guide's labs; verify availability with local Git help.

**Related lessons**

- [advanced-git/08-partial-and-shallow-clone](../../advanced-git/08-partial-and-shallow-clone/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-clone>

## git-archive

**`git archive`**

**Type:** Native command

**Level:** Advanced

**Find by intent:** Package history or files

**Risk:** State change. Review paths, refs and local configuration first. Preserve valuable work; never test against the guide or a shared service.

**Purpose:** Export selected committed tree content as a file archive without Git history.

**Prerequisites:** Use a clean owned disposable repository with saved work, verified local paths and refs, and trusted configuration. Use only owned local sources.

**Options:** --format selects archive format; --output names output file; --prefix prepends paths; export-ignore attributes can omit paths.

**When to use:** When preparing a reviewed source snapshot for distribution or inspection.

**When to avoid:** Avoid overwriting existing artifacts, exporting secrets or assuming submodule content is included recursively.

**Syntax**

`git archive --format=tar --output=../snapshot.tar HEAD`

**Basic example**

`git archive --format=tar --output=../snapshot.tar HEAD`

Write an archive of the verified committed tree to an unused sibling file.

**Professional example**

`git archive --format=zip --prefix=release/ --output=../release.zip v1.0.0`

Package an existing verified version tag in a new local ZIP.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Changes

**Expected result:** Creates archive of selected tree with applicable export attributes; uncommitted edits and Git metadata are not included.

**Effects and side effects:** Writes the named external output file; shown operation does not change refs, index or tracked working files.

**Common errors:** Treating an archive as repository backup or assuming it includes working tree edits.

**Alternatives:** Use git bundle to transfer selected refs and commit history.

**Recovery:** Verify archive contents and destination; recreate under a new filename if needed. Do not delete unrelated files.

**Version and dependencies:** Use Git 2.40 or newer for the guide's labs; verify availability with local Git help.

**Related lessons**

- [advanced-git/10-archive-and-bundle](../../advanced-git/10-archive-and-bundle/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-archive>

## git-bundle-create

**`git bundle create`**

**Type:** Subcommand

**Level:** Advanced

**Find by intent:** Package history or files, Recover work

**Risk:** State change. Review paths, refs and local configuration first. Preserve valuable work; never test against the guide or a shared service.

**Purpose:** Package selected Git refs and reachable objects for offline transport.

**Prerequisites:** Use a clean owned disposable repository with saved work, verified local paths and refs, and trusted configuration. Use only owned local sources.

**Options:** --all selects refs broadly; revision ranges can create incremental bundles requiring prerequisite objects; git bundle verify checks applicability.

**When to use:** When transferring selected committed history without a live remote connection.

**When to avoid:** Avoid bundling unreviewed private history or treating it as a full backup of repository configuration and uncommitted work.

**Syntax**

`git bundle create ../main.bundle main`

**Basic example**

`git bundle create ../main.bundle main`

Create a bundle of the verified local main ref at an unused path.

**Professional example**

`git bundle create ../transfer.bundle --all`

After reviewing every selected ref and its history for sensitive content, create a local transfer bundle.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Changes

**Expected result:** Creates a bundle containing selected advertised refs and necessary object data; incremental forms may require existing base objects.

**Effects and side effects:** Writes output artifact outside the checkout; shown creation does not update current refs or remote.

**Common errors:** Assuming --all captures untracked files, reflogs, hooks and platform metadata.

**Alternatives:** Use archive for a source snapshot; use a separate verified backup for all repository and working data.

**Recovery:** Run git bundle verify and inspect advertised refs; test clone or fetch in a disposable destination before relying on the artifact.

**Version and dependencies:** Use Git 2.40 or newer for the guide's labs; verify availability with local Git help.

**Related lessons**

- [advanced-git/10-archive-and-bundle](../../advanced-git/10-archive-and-bundle/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-bundle>


---

<!-- navigation-footer -->
[Previous](../10-search-and-troubleshooting/README.md) · [Index](../README.md) · [Next](../12-internals-and-plumbing/README.md)
<!-- /navigation-footer -->
