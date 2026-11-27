# 12 Internals & Plumbing

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../11-advanced-git-operations/README.md) · [Index](../README.md) · [Next](../13-security-and-maintenance/README.md)
<!-- /navigation -->

Generated from canonical catalog JSON. Edit the records, not this page.

Reference entries describe commands and operations, not a sequence to run. Use disposable repositories for practice. Hosted operations are optional.

**Total distinct entries: 8**

- [`git cat-file -t`](#git-cat-file-type)
- [`git cat-file -p`](#git-cat-file-pretty)
- [`git hash-object`](#git-hash-object)
- [`git ls-tree`](#git-ls-tree)
- [`git rev-list`](#git-rev-list)
- [`git symbolic-ref HEAD`](#git-symbolic-ref-read)
- [`git for-each-ref`](#git-for-each-ref)
- [`git ls-files --stage`](#git-ls-files-stage)

## git-cat-file-type

**`git cat-file -t`**

**Type:** Option usage

**Level:** Advanced

**Find by intent:** Inspect Git objects

**Risk:** Read-only. Read-only for the shown forms in a complete local repository; do not disclose sensitive paths, object contents or metadata.

**Purpose:** Identify the type of an existing Git object.

**Prerequisites:** Use an owned disposable repository with existing named objects and trusted local configuration. Inspect the repository before running commands.

**Options:** -t prints the object type; -s reports its size; use a resolvable object name.

**When to use:** When distinguishing blobs, trees, commits and annotated tag objects before inspection.

**When to avoid:** Do not use an ambiguous or guessed object ID, or expect the type to prove content integrity.

**Syntax**

`git cat-file -t HEAD`

**Basic example**

`git cat-file -t HEAD`

Identify the type of the object named by HEAD.

**Professional example**

`git cat-file -t HEAD:notes.txt`

Identify an existing ordinary file blob in the commit.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Prints the object's type, such as commit, tree, blob or tag, or reports resolution failure.

**Effects and side effects:** In the complete local lab, the shown inspection does not write objects, change refs, edit files or update index. Partial clones may fetch missing objects.

**Common errors:** Assuming every tag name points to a tag object; lightweight tags name other objects directly.

**Alternatives:** Use git cat-file -p to inspect the resolved object's contents, or git fsck for integrity checks.

**Recovery:** No undo is required for the shown inspection. If output is unexpected, verify the object, ref, revision range or path and inspect errors before proceeding.

**Version and dependencies:** Standard Git syntax; use Git 2.40 or newer for guide labs. Object IDs depend on repository object format.

**Related lessons**

- [git-internals/01-object-database](../../git-internals/01-object-database/README.md)
- [git-internals/10-porcelain-and-plumbing](../../git-internals/10-porcelain-and-plumbing/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-cat-file>

## git-cat-file-pretty

**`git cat-file -p`**

**Type:** Option usage

**Level:** Advanced

**Find by intent:** Inspect Git objects, Inspect history

**Risk:** Read-only. Read-only for the shown forms in a complete local repository; do not disclose sensitive paths, object contents or metadata.

**Purpose:** Display an object's content in a form suitable for its type.

**Prerequisites:** Use an owned disposable repository with existing named objects and trusted local configuration. Inspect the repository before running commands.

**Options:** -p pretty-prints according to object type; use -t first if type is uncertain.

**When to use:** When examining stored object structure rather than a formatted change summary.

**When to avoid:** Avoid dumping unknown binary blobs to a terminal or publishing sensitive historical content.

**Syntax**

`git cat-file -p HEAD`

**Basic example**

`git cat-file -p HEAD`

Inspect commit metadata and its tree and parent IDs.

**Professional example**

`git cat-file -p HEAD:notes.txt`

Read the committed text blob after verifying path and type.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Displays commit headers and message, formatted tree entries, blob bytes or tag object content as applicable.

**Effects and side effects:** In the complete local lab, the shown inspection does not write objects, change refs, edit files or update index. Partial clones may fetch missing objects.

**Common errors:** Confusing the stored commit's parent IDs with a diff or assuming blob output includes filenames.

**Alternatives:** Use git show for human-oriented commit review or git ls-tree for structured tree listings.

**Recovery:** No undo is required for the shown inspection. If output is unexpected, verify the object, ref, revision range or path and inspect errors before proceeding.

**Version and dependencies:** Standard Git syntax; use Git 2.40 or newer for guide labs. Object IDs depend on repository object format.

**Related lessons**

- [git-internals/02-blobs-and-trees](../../git-internals/02-blobs-and-trees/README.md)
- [git-internals/03-commits-and-tags](../../git-internals/03-commits-and-tags/README.md)
- [git-internals/10-porcelain-and-plumbing](../../git-internals/10-porcelain-and-plumbing/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-cat-file>

## git-hash-object

**`git hash-object`**

**Type:** Native command

**Level:** Advanced

**Find by intent:** Inspect Git objects

**Risk:** Read-only. Read-only for the shown forms in a complete local repository; do not disclose sensitive paths, object contents or metadata.

**Purpose:** Calculate the object ID for supplied content without storing it by default.

**Prerequisites:** Use an owned disposable repository with existing named objects and trusted local configuration. Inspect the repository before running commands.

**Options:** --no-filters hashes raw input without path filters; -w writes an object and is not used in these examples; -t selects object type.

**When to use:** When studying content addressing or comparing raw file content with a stored blob ID.

**When to avoid:** Do not assume the ID is a plain file checksum or that the default operation stages a file.

**Syntax**

`git hash-object --no-filters notes.txt`

**Basic example**

`git hash-object --no-filters notes.txt`

Calculate a raw file blob ID without writing it.

**Professional example**

`git hash-object --no-filters docs/notes.txt`

Compare the calculated raw blob ID with the expected stored blob, accounting for filters.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Prints an object ID computed using Git object framing and the repository hash format; no object is written in the shown forms.

**Effects and side effects:** The shown forms read input and calculate an ID without writing an object; -w is a separate state-changing choice.

**Common errors:** Comparing with an ordinary SHA checksum without accounting for Git's object header, filters or hash algorithm.

**Alternatives:** Use git rev-parse HEAD:path to locate an existing committed blob, or git add for intentional staging.

**Recovery:** No undo is required for the shown inspection. If output is unexpected, verify the object, ref, revision range or path and inspect errors before proceeding.

**Version and dependencies:** Standard Git syntax; use Git 2.40 or newer for guide labs. Object IDs depend on repository object format.

**Related lessons**

- [git-internals/04-object-hashes](../../git-internals/04-object-hashes/README.md)
- [git-internals/02-blobs-and-trees](../../git-internals/02-blobs-and-trees/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-hash-object>

## git-ls-tree

**`git ls-tree`**

**Type:** Native command

**Level:** Advanced

**Find by intent:** Inspect Git objects, Inspect files

**Risk:** Read-only. Read-only for the shown forms in a complete local repository; do not disclose sensitive paths, object contents or metadata.

**Purpose:** List entries of a selected committed tree with modes, types, IDs and paths.

**Prerequisites:** Use an owned disposable repository with existing named objects and trusted local configuration. Inspect the repository before running commands.

**Options:** -r recurses into subtrees; -z uses NUL-terminated output for parsing; --name-only selects paths.

**When to use:** When inspecting a historical snapshot independently of current checkout files.

**When to avoid:** Do not use as proof that the working tree matches a commit or includes untracked files.

**Syntax**

`git ls-tree HEAD`

**Basic example**

`git ls-tree HEAD`

List entries of the root tree of the current commit.

**Professional example**

`git ls-tree -r HEAD -- docs/`

Inspect committed entries recursively under the named directory.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Displays selected tree entries and object references; no checkout occurs.

**Effects and side effects:** In the complete local lab, the shown inspection does not write objects, change refs, edit files or update index. Partial clones may fetch missing objects.

**Common errors:** Confusing stored executable and gitlink modes with complete operating system permissions.

**Alternatives:** Use git ls-files --stage for index contents or git status for working state.

**Recovery:** No undo is required for the shown inspection. If output is unexpected, verify the object, ref, revision range or path and inspect errors before proceeding.

**Version and dependencies:** Standard Git syntax; use Git 2.40 or newer for guide labs. Object IDs depend on repository object format.

**Related lessons**

- [git-internals/02-blobs-and-trees](../../git-internals/02-blobs-and-trees/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-ls-tree>

## git-rev-list

**`git rev-list`**

**Type:** Native command

**Level:** Advanced

**Find by intent:** Inspect history, Inspect Git objects

**Risk:** Read-only. Read-only for the shown forms in a complete local repository; do not disclose sensitive paths, object contents or metadata.

**Purpose:** Enumerate commit reachability or counts for specified revision sets.

**Prerequisites:** Use an owned disposable repository with existing named objects and trusted local configuration. Inspect the repository before running commands.

**Options:** --count reports a count; --left-right distinguishes sides of a symmetric difference; --objects includes object traversal.

**When to use:** When scripting ancestry counts or inspecting divergence of known refs.

**When to avoid:** Do not treat equal counts as equivalent file content, or assume shallow history is complete.

**Syntax**

`git rev-list --count HEAD`

**Basic example**

`git rev-list --count HEAD`

Count commits reachable from current HEAD.

**Professional example**

`git rev-list --left-right --count main...feature`

Compare reachable commits unique to each verified local branch.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Returns IDs or counts for the requested reachability set; in the two-sided example the counts represent left-only and right-only commits.

**Effects and side effects:** In the complete local lab, the shown inspection does not write objects, change refs, edit files or update index. Partial clones may fetch missing objects.

**Common errors:** Confusing A..B with A...B, or comparing commit counts instead of snapshots.

**Alternatives:** Use git log for human-oriented history or git diff to compare snapshot content.

**Recovery:** No undo is required for the shown inspection. If output is unexpected, verify the object, ref, revision range or path and inspect errors before proceeding.

**Version and dependencies:** Standard Git syntax; use Git 2.40 or newer for guide labs. Object IDs depend on repository object format.

**Related lessons**

- [git-internals/03-commits-and-tags](../../git-internals/03-commits-and-tags/README.md)
- [git-internals/09-reflogs-and-reachability](../../git-internals/09-reflogs-and-reachability/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-rev-list>

## git-symbolic-ref-read

**`git symbolic-ref HEAD`**

**Type:** Option usage

**Level:** Advanced

**Find by intent:** Inspect references, Inspect repository state

**Risk:** Read-only. Read-only for the shown forms in a complete local repository; do not disclose sensitive paths, object contents or metadata.

**Purpose:** Read the target of a symbolic reference, here HEAD.

**Prerequisites:** Use an owned disposable repository with existing named objects and trusted local configuration. Inspect the repository before running commands.

**Options:** --short abbreviates the ref name; --quiet suppresses the error for a non-symbolic ref while returning status 1; supplying a new target is a separate write form.

**When to use:** When determining whether HEAD is attached to a named branch.

**When to avoid:** Avoid the write form for ordinary switching; it does not perform a normal checkout.

**Syntax**

`git symbolic-ref HEAD`

**Basic example**

`git symbolic-ref HEAD`

Inspect the ref selected by attached HEAD.

**Professional example**

`git symbolic-ref --quiet --short HEAD`

Check branch attachment in a script; handle detached HEAD exit status.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Prints symbolic target when attached; detached HEAD causes a nonzero result.

**Effects and side effects:** In the complete local lab, the shown inspection does not write objects, change refs, edit files or update index. Partial clones may fetch missing objects.

**Common errors:** Assuming symbolic-ref returns a commit ID or that changing HEAD manually updates files.

**Alternatives:** Use git branch --show-current for a branch name or git rev-parse HEAD for a commit ID.

**Recovery:** No undo is required for the shown inspection. If output is unexpected, verify the object, ref, revision range or path and inspect errors before proceeding.

**Version and dependencies:** Standard Git syntax; use Git 2.40 or newer for guide labs. Object IDs depend on repository object format.

**Related lessons**

- [git-internals/05-refs-and-head](../../git-internals/05-refs-and-head/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-symbolic-ref>

## git-for-each-ref

**`git for-each-ref`**

**Type:** Native command

**Level:** Advanced

**Find by intent:** Inspect references, Automate workflow

**Risk:** Read-only. Read-only for the shown forms in a complete local repository; do not disclose sensitive paths, object contents or metadata.

**Purpose:** Enumerate refs with configurable formatting and sorting.

**Prerequisites:** Use an owned disposable repository with existing named objects and trusted local configuration. Inspect the repository before running commands.

**Options:** --format selects fields; --sort orders results; ref patterns restrict the namespace.

**When to use:** When producing structured local reference inventories for review or automation.

**When to avoid:** Do not assume local remote-tracking refs reflect live server state or use unvalidated output as shell code.

**Syntax**

`git for-each-ref --format='%(refname) %(objectname)' refs/heads/`

**Basic example**

`git for-each-ref --format='%(refname) %(objectname)' refs/heads/`

List names and IDs of local branch refs.

**Professional example**

`git for-each-ref --sort=-committerdate --format='%(refname:short)' refs/heads/`

Inspect local branch names ordered by tip committer date.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Prints formatted records for matching local refs; no ref modification occurs.

**Effects and side effects:** In the complete local lab, the shown inspection does not write objects, change refs, edit files or update index. Partial clones may fetch missing objects.

**Common errors:** Confusing refnames with checked-out branches or interpreting committer date as branch creation date.

**Alternatives:** Use git show-ref for simple name and ID listings or git branch for branch-oriented inspection.

**Recovery:** No undo is required for the shown inspection. If output is unexpected, verify the object, ref, revision range or path and inspect errors before proceeding.

**Version and dependencies:** Standard Git syntax; use Git 2.40 or newer for guide labs. Object IDs depend on repository object format.

**Related lessons**

- [git-internals/05-refs-and-head](../../git-internals/05-refs-and-head/README.md)
- [git-internals/10-porcelain-and-plumbing](../../git-internals/10-porcelain-and-plumbing/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-for-each-ref>

## git-ls-files-stage

**`git ls-files --stage`**

**Type:** Option usage

**Level:** Advanced

**Find by intent:** Inspect index internals, Inspect Git objects

**Risk:** Read-only. Read-only for the shown forms in a complete local repository; do not disclose sensitive paths, object contents or metadata.

**Purpose:** Inspect index entries with mode, object ID, stage and path.

**Prerequisites:** Use an owned disposable repository with existing named objects and trusted local configuration. Inspect the repository before running commands.

**Options:** --stage or -s displays entry metadata; -z is useful for robust parsing of paths.

**When to use:** When studying the staged snapshot, gitlinks or conflict stages.

**When to avoid:** Do not interpret the index as the latest committed snapshot or as all working directory files.

**Syntax**

`git ls-files --stage -- notes.txt`

**Basic example**

`git ls-files --stage -- notes.txt`

Inspect the index entry for an existing practice file.

**Professional example**

`git ls-files --stage`

Inspect staged modes, object IDs and conflict stages across the disposable repository.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Displays entries including stage 0 for ordinary merged paths and higher stages for unresolved conflicts when present.

**Effects and side effects:** In the complete local lab, the shown inspection does not write objects, change refs, edit files or update index. Partial clones may fetch missing objects.

**Common errors:** Assuming stage 0 means that a file has no unstaged changes or a gitlink is a normal file blob.

**Alternatives:** Use git ls-tree HEAD to compare committed tree entries, or git ls-files --unmerged to isolate conflict entries.

**Recovery:** No undo is required for the shown inspection. If output is unexpected, verify the object, ref, revision range or path and inspect errors before proceeding.

**Version and dependencies:** Standard Git syntax; use Git 2.40 or newer for guide labs. Object IDs depend on repository object format.

**Related lessons**

- [git-internals/06-index-internals](../../git-internals/06-index-internals/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-ls-files>


---

<!-- navigation-footer -->
[Previous](../11-advanced-git-operations/README.md) · [Index](../README.md) · [Next](../13-security-and-maintenance/README.md)
<!-- /navigation-footer -->
