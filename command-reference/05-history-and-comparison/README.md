# 05 History & Comparison

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../04-commits-and-tags/README.md) · [Index](../README.md) · [Next](../06-branch-management/README.md)
<!-- /navigation -->

Generated from canonical catalog JSON. Edit the records, not this page.

Reference entries describe commands and operations, not a sequence to run. Use disposable repositories for practice. Hosted operations are optional.

**Total distinct entries: 10**

- [`git log`](#git-log)
- [`git log --graph`](#git-log-graph)
- [`git log -- path`](#git-log-path)
- [`git show`](#git-show)
- [`git diff`](#git-diff)
- [`git diff --cached`](#git-diff-cached)
- [`git diff A B`](#git-diff-two-revisions)
- [`git diff --stat`](#git-diff-stat)
- [`git diff A...B`](#git-diff-three-dot)
- [`git range-diff`](#git-range-diff)

## git-log

**`git log`**

**Type:** Native command

**Level:** Beginner

**Find by intent:** Inspect history

**Risk:** Read-only. Read-only in the shown configuration; output may contain private paths, messages or file contents. Use a trusted local repository and review before sharing.

**Purpose:** Inspect commits reachable from a starting revision, normally HEAD.

**Prerequisites:** Use a trusted practice repository with the referenced commits available locally.

**Options:** -5 limits the number of displayed commits; --oneline gives abbreviated IDs and subjects.

**When to use:** When investigating what has been recorded and by whom.

**When to avoid:** Do not use the default log to infer every branch or uncommitted edit.

**Syntax**

`git log -5`

**Basic example**

`git log -3`

Inspect three recent commits in a practice history.

**Professional example**

`git log --oneline main..feature`

Inspect commits reachable from a local feature branch but not main; both refs must exist.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Commit metadata is displayed for the selected reachable history; a pager may open.

**Effects and side effects:** Under normal built-in display behavior, no working files, index, commit refs or remote are changed.

**Common errors:** Assuming default log includes unreachable commits or every remote branch.

**Alternatives:** Use git show for one commit or git reflog to investigate local ref movements.

**Recovery:** No repository recovery is needed after inspection; check the selected revisions or paths and repeat the comparison if necessary.

**Version and dependencies:** Use standard Git in a trusted local repository; no optional viewer is required. A configured pager may open.

**Related lessons**

- [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.md)
- [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-log>

## git-log-graph

**`git log --graph`**

**Type:** Option usage

**Level:** Intermediate

**Find by intent:** Inspect history, Manage branches

**Risk:** Read-only. Read-only in the shown configuration; output may contain private paths, messages or file contents. Use a trusted local repository and review before sharing.

**Purpose:** Visualize parent relationships and divergence in commit history.

**Prerequisites:** Use a trusted practice repository with the referenced commits available locally.

**Options:** --graph draws ancestry lines; --oneline condenses each commit; --all starts from local refs and HEAD.

**When to use:** When reviewing branch topology and merge history.

**When to avoid:** Do not treat graph column position or vertical spacing as an exact timeline.

**Syntax**

`git log --oneline --graph --all`

**Basic example**

`git log --oneline --graph`

View the current branch ancestry.

**Professional example**

`git log --oneline --graph --all --decorate`

Review local branch and tag topology before integrating work.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** A textual graph displays selected commits and parent connections.

**Effects and side effects:** Under normal built-in display behavior, no working files, index, commit refs or remote are changed.

**Common errors:** Assuming --all fetches remote state or includes unreachable objects.

**Alternatives:** Use git merge-base for a shared ancestor or git log without graph for detailed messages.

**Recovery:** No repository recovery is needed after inspection; check the selected revisions or paths and repeat the comparison if necessary.

**Version and dependencies:** Use standard Git in a trusted local repository; no optional viewer is required. A configured pager may open.

**Related lessons**

- [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.md)
- [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.md)
- [branches/02-start-points-and-comparison](../../branches/02-start-points-and-comparison/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-log>

## git-log-path

**`git log -- path`**

**Type:** Option usage

**Level:** Intermediate

**Find by intent:** Inspect history, Inspect files

**Risk:** Read-only. Read-only in the shown configuration; output may contain private paths, messages or file contents. Use a trusted local repository and review before sharing.

**Purpose:** Inspect history selected by changes to a given path.

**Prerequisites:** Use a trusted practice repository with the referenced commits available locally.

**Options:** -- separates revisions from paths; --follow tracks history beyond renames for a single file with limitations.

**When to use:** When investigating the evolution of a particular file or directory.

**When to avoid:** Do not assume default history simplification lists every relevant merge or follows every rename.

**Syntax**

`git log -- notes.txt`

**Basic example**

`git log -- notes.txt`

Inspect changes in a fictional tracked notes file.

**Professional example**

`git log --follow -- docs/setup.md`

Investigate a single documentation file across detected renames.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Shows commits selected by path history and simplification rules, not current uncommitted edits.

**Effects and side effects:** Under normal built-in display behavior, no working files, index, commit refs or remote are changed.

**Common errors:** Omitting -- when a path name can also name a revision.

**Alternatives:** Use git blame for line attribution or git log --full-history with a path when investigating merges.

**Recovery:** No repository recovery is needed after inspection; check the selected revisions or paths and repeat the comparison if necessary.

**Version and dependencies:** Use standard Git in a trusted local repository; no optional viewer is required. A configured pager may open.

**Related lessons**

- [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.md)
- [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-log>

## git-show

**`git show`**

**Type:** Native command

**Level:** Beginner

**Find by intent:** Inspect history, Review changes, Inspect Git objects

**Risk:** Read-only. Read-only with built-in diff behavior; inspect sensitive output and avoid untrusted external diff drivers, text conversion filters or pagers.

**Purpose:** Display a Git object; for a normal commit this includes its metadata and patch by default.

**Prerequisites:** Use a trusted practice repository with the referenced commits available locally.

**Options:** --stat summarizes changes; revision:path selects a blob at a historical path.

**When to use:** When reviewing a specific commit, tag or historical file snapshot.

**When to avoid:** Do not assume a merge commit display shows every parent difference by default.

**Syntax**

`git show HEAD`

**Basic example**

`git show HEAD`

Review the latest committed change.

**Professional example**

`git show HEAD:notes.txt`

Inspect the committed content of a fictional file without checking it out.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Displays the requested object in a representation appropriate to its type; HEAD is the default.

**Effects and side effects:** Under normal built-in display behavior, no working files, index, commit refs or remote are changed.

**Common errors:** Confusing git show HEAD:path with the current working file.

**Alternatives:** Use git diff for two snapshots or git cat-file for lower-level object inspection.

**Recovery:** No repository recovery is needed after inspection; check the selected revisions or paths and repeat the comparison if necessary.

**Version and dependencies:** Use standard Git in a trusted local repository; no optional viewer is required. A configured pager may open.

**Related lessons**

- [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.md)
- [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.md)
- [git-internals/02-blobs-and-trees](../../git-internals/02-blobs-and-trees/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-show>

## git-diff

**`git diff`**

**Type:** Native command

**Level:** Beginner

**Find by intent:** Compare changes, Review changes

**Risk:** State change. An inspection operation with possible index metadata writes, not a staging operation; avoid untrusted external diff drivers and review sensitive output before sharing.

**Purpose:** Compare tracked working-tree content with the index.

**Prerequisites:** Use a trusted practice repository with a working tree and index; review git status first.

**Options:** -- separates options and revisions from paths; --stat summarizes changes.

**When to use:** Before staging changes, to review unstaged differences.

**When to avoid:** Do not rely on this form alone to review staged changes or untracked files.

**Syntax**

`git diff -- notes.txt`

**Basic example**

`git diff`

Review an unstaged tracked edit.

**Professional example**

`git diff -- notes.txt`

Review a single tracked file before staging.

**State effects**

- Working tree: Unchanged
- Index: Conditional
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Displays unstaged differences for tracked paths; empty output may mean no such differences.

**Effects and side effects:** Working files, staged blob IDs, commit refs and remote stay unchanged under built-in behavior; diff.autoRefreshIndex can refresh cached file stat metadata in the index.

**Common errors:** Assuming an empty diff means the entire repository is clean.

**Alternatives:** Use git diff --cached for staged changes and git status for untracked files.

**Recovery:** No repository recovery is needed after inspection; check the selected revisions or paths and repeat the comparison if necessary.

**Version and dependencies:** Use standard Git in a trusted local repository; no optional viewer is required. A configured pager may open.

**Related lessons**

- [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.md)
- [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-diff>
- <https://git-scm.com/docs/git-config/2.36.3.html>

## git-diff-cached

**`git diff --cached`**

**Type:** Option usage

**Level:** Beginner

**Find by intent:** Compare changes, Review changes, Stage changes

**Risk:** Read-only. Read-only with built-in diff behavior; inspect sensitive output and avoid untrusted external diff drivers, text conversion filters or pagers.

**Purpose:** Compare the index with HEAD to review staged changes.

**Prerequisites:** Use a trusted practice repository with a working tree and index; review git status first.

**Options:** --staged is a synonym for --cached; -- followed by a path limits output.

**When to use:** Immediately before committing the staged snapshot.

**When to avoid:** Do not use this form to inspect changes made after staging unless staged again.

**Syntax**

`git diff --cached`

**Basic example**

`git diff --cached`

Inspect changes already selected for commit.

**Professional example**

`git diff --cached -- notes.txt`

Confirm only the intended portion of a partially staged file is in the index.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Shows the staged difference from HEAD; on an unborn branch it shows all staged changes when no commit is supplied.

**Effects and side effects:** Under normal built-in display behavior, no working files, index, commit refs or remote are changed.

**Common errors:** Confusing cached differences with working-tree differences.

**Alternatives:** Use git diff to see what is not yet staged or git status to inspect both states.

**Recovery:** No repository recovery is needed after inspection; check the selected revisions or paths and repeat the comparison if necessary.

**Version and dependencies:** Use standard Git in a trusted local repository; no optional viewer is required. A configured pager may open.

**Related lessons**

- [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.md)
- [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-diff>

## git-diff-two-revisions

**`git diff A B`**

**Type:** Option usage

**Level:** Intermediate

**Find by intent:** Compare changes, Review changes

**Risk:** Read-only. Read-only with built-in diff behavior; inspect sensitive output and avoid untrusted external diff drivers, text conversion filters or pagers.

**Purpose:** Compare two committed snapshots directly, regardless of their ancestry.

**Prerequisites:** Use a trusted practice repository with the referenced commits available locally.

**Options:** Supply two revisions; A..B is equivalent for git diff, unlike a git log commit range.

**When to use:** When checking end-state differences between branches, tags or commits.

**When to avoid:** Avoid interpreting this as a list of individual commits or as only changes introduced by feature.

**Syntax**

`git diff main feature`

**Basic example**

`git diff HEAD~1 HEAD`

Compare a non-root commit to its first parent.

**Professional example**

`git diff main feature`

Compare tips of existing local main and feature branches.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Displays the patch from the first snapshot to the second; reversing inputs reverses the comparison.

**Effects and side effects:** Under normal built-in display behavior, no working files, index, commit refs or remote are changed.

**Common errors:** Treating two-dot diff syntax as a revision set like git log A..B.

**Alternatives:** Use git diff A...B to compare from a merge base to B or git log A..B to list commits.

**Recovery:** No repository recovery is needed after inspection; check the selected revisions or paths and repeat the comparison if necessary.

**Version and dependencies:** Use standard Git in a trusted local repository; no optional viewer is required. A configured pager may open.

**Related lessons**

- [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.md)
- [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.md)
- [branches/02-start-points-and-comparison](../../branches/02-start-points-and-comparison/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-diff>

## git-diff-stat

**`git diff --stat`**

**Type:** Option usage

**Level:** Beginner

**Find by intent:** Compare changes, Review changes

**Risk:** State change. An inspection operation with possible index metadata writes, not a staging operation; avoid untrusted external diff drivers and review sensitive output before sharing.

**Purpose:** Summarize the scope of a diff by affected files and change counts.

**Prerequisites:** Use a trusted practice repository with a working tree and index; review git status first.

**Options:** --stat requests a summary; combine with --cached or two revisions to choose another comparison.

**When to use:** When estimating the review scope before reading a full patch.

**When to avoid:** Do not treat line counts as a measure of correctness, complexity or developer productivity.

**Syntax**

`git diff --stat`

**Basic example**

`git diff --stat`

Summarize unstaged changes.

**Professional example**

`git diff --cached --stat`

Estimate staged review scope before reading the patch.

**State effects**

- Working tree: Unchanged
- Index: Conditional
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Displays per-file summaries and totals for the selected comparison; binary files have different summaries.

**Effects and side effects:** Working files, staged blob IDs, commit refs and remote stay unchanged under built-in behavior; diff.autoRefreshIndex can refresh cached file stat metadata in the index.

**Common errors:** Assuming --stat changes the comparison endpoints or replaces reading the patch.

**Alternatives:** Use git diff --name-status for file status codes or a full git diff for content review.

**Recovery:** No repository recovery is needed after inspection; check the selected revisions or paths and repeat the comparison if necessary.

**Version and dependencies:** Use standard Git in a trusted local repository; no optional viewer is required. A configured pager may open.

**Related lessons**

- [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.md)
- [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-diff>
- <https://git-scm.com/docs/git-config/2.36.3.html>

## git-diff-three-dot

**`git diff A...B`**

**Type:** Option usage

**Level:** Intermediate

**Find by intent:** Compare changes, Review changes, Inspect history

**Risk:** Read-only. Read-only with built-in diff behavior; inspect sensitive output and avoid untrusted external diff drivers, text conversion filters or pagers.

**Purpose:** Compare the snapshot at a merge base of A and B with the snapshot at B.

**Prerequisites:** Use a trusted local repository with both refs and a suitable common ancestor; verify the merge base first.

**Options:** Three dots select a merge base as the first endpoint; the right-hand revision is the second endpoint.

**When to use:** When reviewing branch changes relative to a common ancestor, especially after divergence.

**When to avoid:** Avoid assuming this is symmetric or always identical to a hosted pull request diff; inspect ambiguous merge bases.

**Syntax**

`git diff main...feature`

**Basic example**

`git diff main...feature`

Review an existing local feature branch relative to its common base with main.

**Professional example**

`git diff main...feature -- notes.txt`

Review branch changes for one fictional file after checking the merge base.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Shows the net difference from the selected common base to the right-hand snapshot, not changes exclusive to the left branch.

**Effects and side effects:** Under normal built-in display behavior, no working files, index, commit refs or remote are changed.

**Common errors:** Confusing git diff A...B with symmetric difference of commit sets in git log A...B.

**Alternatives:** Use git diff A B for tip-to-tip comparison or inspect git merge-base --all A B before selecting an explicit base.

**Recovery:** No repository recovery is needed after inspection; check the selected revisions or paths and repeat the comparison if necessary.

**Version and dependencies:** Use standard Git in a trusted local repository; no optional viewer is required. A configured pager may open.

**Related lessons**

- [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.md)
- [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.md)
- [branches/02-start-points-and-comparison](../../branches/02-start-points-and-comparison/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-diff>

## git-range-diff

**`git range-diff`**

**Type:** Native command

**Level:** Advanced

**Find by intent:** Compare changes, Review changes, Rewrite local history

**Risk:** Read-only. Read-only with built-in diff behavior; inspect sensitive output and avoid untrusted external diff drivers, text conversion filters or pagers.

**Purpose:** Compare the patches and messages of two versions of a commit series.

**Prerequisites:** Use a trusted local repository with both nonempty commit ranges; retain the old tip before rewriting history.

**Options:** Pass two explicit revision ranges; --no-color disables coloring for reading plain output.

**When to use:** When reviewing changes to a private patch series after corrections or rebase.

**When to avoid:** Do not use it as a proof of semantic equivalence or a stable machine-readable API; merge commits are ignored by default.

**Syntax**

`git range-diff main..old-series main..feature`

**Basic example**

`git range-diff main..old-series main..feature`

Compare two existing local series based on main.

**Professional example**

`git range-diff --no-color main..old-series main..feature`

Review a saved pre-rebase series against its revised version; confirm actual changes separately.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Displays approximate correspondence between commits and changes in their patches and metadata; unmatched commits are identified.

**Effects and side effects:** Under normal built-in display behavior, no working files, index, commit refs or remote are changed.

**Common errors:** Comparing only final snapshots and missing changes to individual commits, or trusting matching as a proof of correctness.

**Alternatives:** Use git diff between the two tips to compare final content and run relevant tests.

**Recovery:** No repository recovery is needed after inspection; check the selected revisions or paths and repeat the comparison if necessary.

**Version and dependencies:** Requires Git 2.19 or newer; use a trusted local configuration. Output is intended for humans, not a stable parser.

**Related lessons**

- [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.md)
- [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.md)
- [merge-and-conflicts/07-interactive-rebase](../../merge-and-conflicts/07-interactive-rebase/README.md)
- [professional-workflows/08-code-review](../../professional-workflows/08-code-review/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-range-diff>


---

<!-- navigation-footer -->
[Previous](../04-commits-and-tags/README.md) · [Index](../README.md) · [Next](../06-branch-management/README.md)
<!-- /navigation-footer -->
