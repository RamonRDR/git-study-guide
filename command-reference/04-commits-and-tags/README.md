# 04 Commits & Tags

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../03-working-tree-and-staging/README.md) · [Index](../README.md) · [Next](../05-history-and-comparison/README.md)
<!-- /navigation -->

Generated from canonical catalog JSON. Edit the records, not this page.

Reference entries describe commands and operations, not a sequence to run. Use disposable repositories for practice. Hosted operations are optional.

**Total distinct entries: 8**

- [`git commit`](#git-commit)
- [`git commit -a`](#git-commit-all)
- [`git commit --amend`](#git-commit-amend)
- [`git commit --fixup`](#git-commit-fixup)
- [`git tag`](#git-tag)
- [`git tag -a`](#git-tag-annotated)
- [`git tag -d`](#git-tag-delete)
- [`git tag -l`](#git-tag-list)

## git-commit

**`git commit`**

**Type:** Native command

**Level:** Beginner

**Find by intent:** Commit changes

**Risk:** State change. Review git diff --cached, identity and hooks; the commit can retain sensitive content locally.

**Purpose:** Record the reviewed staged snapshot as a new commit.

**Prerequisites:** Use an owned disposable repository with a configured fictional identity and reviewed staged changes.

**Options:** -m supplies the message instead of opening an editor; -v shows a diff in the editor.

**When to use:** When staged changes form a coherent unit of work.

**When to avoid:** Do not commit secrets, unrelated changes or unresolved conflicts.

**Syntax**

`git commit -m "message"`

**Basic example**

`git commit -m "Add notes"`

After staging a fictional notes file.

**Professional example**

`git commit -m "docs: explain setup"`

Record a reviewed documentation change.

**State effects**

- Working tree: Conditional
- Index: Conditional
- Objects / refs / history: Changes
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** A successful ordinary commit records the index and advances the current branch or detached HEAD.

**Effects and side effects:** Normally no working-file content changes; index metadata and local hooks may change state. No push occurs.

**Common errors:** Assuming unstaged edits are included or that a commit publishes changes.

**Alternatives:** Use git add -p before committing to select individual hunks.

**Recovery:** Inspect git show HEAD; amend an unpublished mistake or consider git revert for a shared commit after review.

**Version and dependencies:** Standard Git syntax documented for Git 2.34; no optional tool needed for the shown command. Local hooks or signing configuration may affect execution.

**Related lessons**

- [basic-commands/02-status-add-commit](../../basic-commands/02-status-add-commit/README.md)
- [getting-started/05-first-commit](../../getting-started/05-first-commit/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-commit/2.34.0>

## git-commit-all

**`git commit -a`**

**Type:** Option usage

**Level:** Intermediate

**Find by intent:** Commit changes, Stage changes

**Risk:** State change. May capture more than intended; inspect staged and unstaged differences and configure fictional identity first.

**Purpose:** Stage modified and deleted tracked files and create a commit in one operation.

**Prerequisites:** Use an owned disposable repository; inspect status first and preserve valuable work.

**Options:** -a includes tracked modifications and deletions; -m sets the message.

**When to use:** When every tracked change and already staged addition belongs in one commit.

**When to avoid:** Avoid when unrelated tracked edits or deletions are present.

**Syntax**

`git commit -a -m "message"`

**Basic example**

`git commit -a -m "Update notes"`

Edit an already tracked notes file first.

**Professional example**

`git commit -a -m "docs: fix typos"`

Only after reviewing all tracked changes and the index.

**State effects**

- Working tree: Conditional
- Index: Changes
- Objects / refs / history: Changes
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** The new commit includes tracked updates and existing staged content; new unstaged files remain untracked.

**Effects and side effects:** Updates the index and history; working-file contents normally stay unchanged, subject to hooks.

**Common errors:** Expecting untracked files to be included or overlooking tracked deletions.

**Alternatives:** Use explicit git add paths and git commit for precise scope.

**Recovery:** Inspect the resulting commit; correct unpublished history carefully or revert a shared commit.

**Version and dependencies:** Standard Git syntax documented for Git 2.34; no optional tool needed for the shown command. Local hooks or signing configuration may affect execution.

**Related lessons**

- [basic-commands/02-status-add-commit](../../basic-commands/02-status-add-commit/README.md)
- [getting-started/05-first-commit](../../getting-started/05-first-commit/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-commit/2.34.0>

## git-commit-amend

**`git commit --amend`**

**Type:** Option usage

**Level:** Intermediate

**Find by intent:** Rewrite local history, Commit changes

**Risk:** History rewrite. History rewriting can disrupt collaborators; keep this example local and unpublished.

**Purpose:** Replace the current tip commit with a newly created commit.

**Prerequisites:** Use an owned disposable repository with an existing unpublished HEAD, reviewed index and a saved reference to the old commit.

**Options:** --no-edit keeps the message; -m supplies a replacement; both use the staged snapshot.

**When to use:** Correct a private tip commit before sharing it.

**When to avoid:** Do not rewrite shared history casually or amend with unrelated staged changes.

**Syntax**

`git commit --amend -m "message"`

**Basic example**

`git commit --amend -m "Clarify notes"`

Use a private tip and verify an empty staged diff for a message-only correction.

**Professional example**

`git commit --amend --no-edit`

After staging a missed documentation change for an unpublished tip.

**State effects**

- Working tree: Conditional
- Index: Conditional
- Objects / refs / history: Changes
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** The replacement normally has a different ID and the same parents as the previous tip.

**Effects and side effects:** Moves the local branch or detached HEAD; the old commit may remain reachable through another ref or reflog. Hooks can change local state.

**Common errors:** Treating --no-edit as message-only or assuming the old ID stays valid for the new tip.

**Alternatives:** Create a follow-up commit instead when preserving existing history matters.

**Recovery:** Inspect git reflog and the saved ref; create a recovery branch at the verified old ID if still available. Do not reset blindly.

**Version and dependencies:** Standard Git syntax documented for Git 2.34; no optional tool needed for the shown command. Local hooks or signing configuration may affect execution.

**Related lessons**

- [history-and-recovery/08-amend](../../history-and-recovery/08-amend/README.md)
- [basic-commands/02-status-add-commit](../../basic-commands/02-status-add-commit/README.md)
- [getting-started/05-first-commit](../../getting-started/05-first-commit/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-commit/2.34.0>

## git-commit-fixup

**`git commit --fixup`**

**Type:** Option usage

**Level:** Advanced

**Find by intent:** Commit changes, Rewrite local history

**Risk:** State change. Creating the fixup does not rewrite history, but the later autosquash can; save a ref before rebasing.

**Purpose:** Create a separate correction commit marked for a later autosquash rebase.

**Prerequisites:** Use an owned disposable repository with a reviewed staged correction and an existing target commit in unpublished history.

**Options:** --fixup HEAD targets the current tip; a verified earlier commit ID can also be supplied.

**When to use:** When preparing review corrections to fold into private commits later.

**When to avoid:** Avoid targeting the wrong commit or planning autosquash on shared history without coordination.

**Syntax**

`git commit --fixup HEAD`

**Basic example**

`git commit --fixup HEAD`

Stage a small correction for the current private commit.

**Professional example**

`git commit --fixup HEAD~1`

After verifying that the previous parent is the reviewed correction target.

**State effects**

- Working tree: Conditional
- Index: Conditional
- Objects / refs / history: Changes
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** A new ordinary commit with a fixup! subject is created; the target is not replaced yet.

**Effects and side effects:** The index snapshot is committed and HEAD advances; only a later rebase rewrites history. Hooks may affect local state.

**Common errors:** Assuming --fixup itself squashes the correction into the target.

**Alternatives:** Use a normal follow-up commit when preserving every public correction is desired.

**Recovery:** Inspect git log; if the target was wrong, review and correct the unpublished fixup before attempting autosquash.

**Version and dependencies:** Standard Git syntax documented for Git 2.34; no optional tool needed for the shown command. Local hooks or signing configuration may affect execution.

**Related lessons**

- [merge-and-conflicts/07-interactive-rebase](../../merge-and-conflicts/07-interactive-rebase/README.md)
- [basic-commands/02-status-add-commit](../../basic-commands/02-status-add-commit/README.md)
- [getting-started/05-first-commit](../../getting-started/05-first-commit/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-commit/2.34.0>

## git-tag

**`git tag`**

**Type:** Native command

**Level:** Beginner

**Find by intent:** Manage tags, Manage releases

**Risk:** State change. Verify the target and existing names; examples assume tag.gpgSign is disabled to create a lightweight tag.

**Purpose:** Create a lightweight local tag pointing directly to a Git object, normally a commit.

**Prerequisites:** Use an owned disposable repository with an existing target commit; inspect existing tags and the target first.

**Options:** Provide a name and optionally a target revision; without a target Git uses HEAD.

**When to use:** Mark a local milestone without a separate annotated tag object.

**When to avoid:** Avoid lightweight tags when the release policy requires annotations or signatures.

**Syntax**

`git tag v0.1.0`

**Basic example**

`git tag v0.1.0`

Mark the current fictional practice commit.

**Professional example**

`git tag review-ready HEAD`

Mark a locally reviewed milestone, not a published release.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Changes
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** A new refs/tags reference points at the target; commit ancestry stays unchanged.

**Effects and side effects:** Changes a local ref only; neither checkout nor push occurs under ordinary unsigned configuration.

**Common errors:** Assuming the tag moves with a branch or automatically creates a hosted release.

**Alternatives:** Use git tag -a for a tag object with metadata and message.

**Recovery:** If an unpublished tag is wrong, record its current target, delete it locally and recreate at the verified target.

**Version and dependencies:** Standard syntax documented in Git 2.31; the official manual records no changes through Git 2.34.8. No optional tool needed for the shown unsigned operation.

**Related lessons**

- [git-internals/03-commits-and-tags](../../git-internals/03-commits-and-tags/README.md)
- [professional-workflows/12-release-management](../../professional-workflows/12-release-management/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-tag/2.31.0>

## git-tag-annotated

**`git tag -a`**

**Type:** Option usage

**Level:** Intermediate

**Find by intent:** Manage tags, Manage releases

**Risk:** State change. Configure fictional tagger identity; check target, message and signing policy. Annotation may expose identity when shared.

**Purpose:** Create a local annotated tag object and a reference to it.

**Prerequisites:** Use an owned disposable repository with an existing target commit; inspect existing tags and the target first.

**Options:** -a requests annotation; -m supplies the annotation message; -s requests a signature separately.

**When to use:** When marking a release with tagger metadata and a message.

**When to avoid:** Avoid replacing an already published version tag or using annotation as proof of signature.

**Syntax**

`git tag -a v1.0.0 -m "Release 1.0.0"`

**Basic example**

`git tag -a v1.0.0 -m "Release 1.0.0"`

Mark the current reviewed practice commit.

**Professional example**

`git tag -a v1.2.0 -m "Stable release" HEAD`

After checking the target and local release checklist.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Changes
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** A refs/tags reference points to a tag object that identifies its target and carries annotation metadata.

**Effects and side effects:** Creates an object and local ref; commit ancestry, working files, index and remote are not modified.

**Common errors:** Confusing an annotated tag with a signed tag or a hosted release.

**Alternatives:** Use a lightweight git tag for a temporary local marker where policy permits it.

**Recovery:** Inspect git show on the tag; if unpublished, preserve the old object ID before correcting the tag. For published tags coordinate a new version.

**Version and dependencies:** Standard syntax documented in Git 2.31; the official manual records no changes through Git 2.34.8. No optional tool needed for the shown unsigned operation.

**Related lessons**

- [git-internals/03-commits-and-tags](../../git-internals/03-commits-and-tags/README.md)
- [professional-workflows/12-release-management](../../professional-workflows/12-release-management/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-tag/2.31.0>

## git-tag-delete

**`git tag -d`**

**Type:** Option usage

**Level:** Intermediate

**Find by intent:** Manage tags, Undo changes

**Risk:** Destructive. Deletion loses a reference; record git rev-parse refs/tags/name before deletion. Recovery is not guaranteed.

**Purpose:** Remove a named local tag reference.

**Prerequisites:** Use an owned disposable repository; verify an existing unpublished tag and save its exact ref object ID first.

**Options:** -d deletes one or more named local tags; it is not a remote deletion.

**When to use:** When removing an obsolete private practice marker.

**When to avoid:** Avoid removing published version tags or the only reference to important objects without a recovery plan.

**Syntax**

`git tag -d v0.1.0`

**Basic example**

`git tag -d v0.1.0`

Remove a verified disposable local tag.

**Professional example**

`git tag -d review-ready`

Remove a private review marker after preserving its target ID.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Changes
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** The named local ref no longer exists; remote tags are unchanged.

**Effects and side effects:** May leave a tag object or target unreachable if no other references retain it; objects are not immediately erased by this command.

**Common errors:** Assuming a local deletion also deletes the remote tag or that the exact annotated object is easy to reconstruct.

**Alternatives:** Leave the tag intact and create a new version marker when it has been shared.

**Recovery:** If the exact object is still available, recreate the verified ref using git update-ref; an annotated tag cannot be faithfully restored merely by tagging its commit again.

**Version and dependencies:** Standard syntax documented in Git 2.31; the official manual records no changes through Git 2.34.8. No optional tool needed for the shown unsigned operation.

**Related lessons**

- [git-internals/03-commits-and-tags](../../git-internals/03-commits-and-tags/README.md)
- [professional-workflows/12-release-management](../../professional-workflows/12-release-management/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-tag/2.31.0>

## git-tag-list

**`git tag -l`**

**Type:** Option usage

**Level:** Beginner

**Find by intent:** Manage tags, Inspect references

**Risk:** Read-only. Read-only listing; it does not fetch tags or verify release contents.

**Purpose:** List local tag names, optionally matching a pattern.

**Prerequisites:** Use an owned repository; a matching tag is optional.

**Options:** -l enables listing; quote glob patterns so the shell passes them to Git; --sort can select a sort key.

**When to use:** When checking existing local release names or selecting a comparison point.

**When to avoid:** Do not treat the local list as an authoritative list of remote tags.

**Syntax**

`git tag -l "v1.*"`

**Basic example**

`git tag -l`

Inspect all local tag names.

**Professional example**

`git tag -l "v1.*" --sort=version:refname`

List matching fictional version tags in version order.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Matching tag names are displayed; an unmatched pattern produces no names.

**Effects and side effects:** No local refs, objects or remote state are modified.

**Common errors:** Leaving a wildcard unquoted or assuming lexical order equals version order.

**Alternatives:** Use git show-ref --tags to inspect tag refs and object IDs.

**Recovery:** No recovery is needed for listing; inspect the pattern and local refs if results are unexpected.

**Version and dependencies:** Standard syntax documented in Git 2.31; the official manual records no changes through Git 2.34.8. No optional tool needed for the shown unsigned operation.

**Related lessons**

- [git-internals/03-commits-and-tags](../../git-internals/03-commits-and-tags/README.md)
- [professional-workflows/12-release-management](../../professional-workflows/12-release-management/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-tag/2.31.0>


---

<!-- navigation-footer -->
[Previous](../03-working-tree-and-staging/README.md) · [Index](../README.md) · [Next](../05-history-and-comparison/README.md)
<!-- /navigation-footer -->
