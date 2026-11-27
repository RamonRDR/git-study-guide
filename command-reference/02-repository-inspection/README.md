# 02 Repository Inspection

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../01-setup-and-configuration/README.md) · [Index](../README.md) · [Next](../03-working-tree-and-staging/README.md)
<!-- /navigation -->

Generated from canonical catalog JSON. Edit the records, not this page.

Reference entries describe commands and operations, not a sequence to run. Use disposable repositories for practice. Hosted operations are optional.

**Total distinct entries: 9**

- [`git status`](#git-status)
- [`git status --porcelain`](#git-status-porcelain)
- [`git rev-parse --show-toplevel`](#git-rev-parse-show-toplevel)
- [`git rev-parse --git-dir`](#git-rev-parse-git-dir)
- [`git rev-parse --is-bare-repository`](#git-rev-parse-is-bare)
- [`git ls-files`](#git-ls-files)
- [`git check-ignore`](#git-check-ignore)
- [`git show-ref`](#git-show-ref)
- [`git count-objects`](#git-count-objects)

## git-status

**`git status`**

**Type:** Native command

**Level:** Beginner

**Find by intent:** Inspect repository state

**Risk:** State change. Inspect the result privately; file names, paths or history may reveal project information.

**Purpose:** Summarize staged, unstaged and untracked changes.

**Prerequisites:** Use an owned disposable repository; run from its working directory.

**Options:** --short gives compact status; --branch adds branch information.

**When to use:** Before staging, committing or switching branches.

**When to avoid:** Do not treat a clean status as proof of passing tests or remote synchronization.

**Syntax**

`git status [--short]`

**Basic example**

`git status`

Inspect the full report before staging a changed file.

**Professional example**

`git status --short`

Review a compact report before a code review handoff.

**State effects**

- Working tree: Unchanged
- Index: Conditional
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Reports paths by state; a clean tree has no pending visible changes.

**Effects and side effects:** May refresh index stat metadata without changing staged content; does not change commits.

**Common errors:** Misreading the two short-status columns; ignored files are usually hidden.

**Alternatives:** Use git diff and git diff --cached to inspect actual changes.

**Recovery:** No history recovery is necessary; correct the context and repeat the inspection.

**Version and dependencies:** No optional tool required; examples use longstanding Git syntax.

**Related lessons**

- [basic-commands/02-status-add-commit](../../basic-commands/02-status-add-commit/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-status>

## git-status-porcelain

**`git status --porcelain`**

**Type:** Option usage

**Level:** Intermediate

**Find by intent:** Automate workflow

**Risk:** State change. Inspect the result privately; file names, paths or history may reveal project information.

**Purpose:** Inspect machine-oriented working-tree and index status.

**Prerequisites:** Use an owned disposable repository; run from its working directory.

**Options:** --porcelain=v1 selects stable v1 format; -z uses NUL terminators.

**When to use:** When scripts need reproducible status output.

**When to avoid:** Do not parse human-oriented output or split NUL records by whitespace.

**Syntax**

`git status --porcelain[=v1] [-z]`

**Basic example**

`git status --porcelain=v1`

Compare the v1 report with normal git status.

**Professional example**

`git status --porcelain=v1 -z`

Capture NUL-delimited records as bytes for a preflight check; do not print them as text.

**State effects**

- Working tree: Unchanged
- Index: Conditional
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Outputs compact machine-readable status; an empty report indicates no reported changes.

**Effects and side effects:** Can refresh index stat metadata; does not stage content or move refs.

**Common errors:** Expecting a nonzero exit status for a dirty tree; ignoring rename record format.

**Alternatives:** Use git diff --quiet for a specific tracked-change comparison; it does not cover untracked files.

**Recovery:** No history recovery is necessary; correct the context and repeat the inspection.

**Version and dependencies:** No optional tool required; examples use longstanding Git syntax.

**Related lessons**

- [git-architecture/03-file-states](../../git-architecture/03-file-states/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-status>

## git-rev-parse-show-toplevel

**`git rev-parse --show-toplevel`**

**Type:** Option usage

**Level:** Beginner

**Find by intent:** Inspect repository state

**Risk:** Read-only. Inspect the result privately; file names, paths or history may reveal project information.

**Purpose:** Find the root of the current working tree.

**Prerequisites:** Use an owned disposable repository; run from its working directory.

**Options:** --show-toplevel reports the top-level path; -C changes the command's starting directory.

**When to use:** Before operating on a repository from a nested directory.

**When to avoid:** Do not use it to locate a working tree in a bare repository.

**Syntax**

`git rev-parse --show-toplevel`

**Basic example**

`git rev-parse --show-toplevel`

Confirm the root before inspecting files.

**Professional example**

`git -C src rev-parse --show-toplevel`

If src exists, confirm which repository a tool running there would address.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Prints the top-level working-tree path or fails when unavailable.

**Effects and side effects:** Reads repository discovery information without modifying refs or files.

**Common errors:** Assuming the shell's current directory is always the repository root.

**Alternatives:** Use git rev-parse --git-dir to locate Git metadata instead.

**Recovery:** No history recovery is necessary; correct the context and repeat the inspection.

**Version and dependencies:** No optional tool required; examples use longstanding Git syntax.

**Related lessons**

- [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-rev-parse>

## git-rev-parse-git-dir

**`git rev-parse --git-dir`**

**Type:** Option usage

**Level:** Intermediate

**Find by intent:** Inspect repository state

**Risk:** Read-only. Inspect the result privately; file names, paths or history may reveal project information.

**Purpose:** Locate repository metadata without assuming .git is a directory.

**Prerequisites:** Use an owned disposable repository; run from its working directory.

**Options:** --git-dir may report a relative path; --absolute-git-dir requests an absolute path.

**When to use:** Diagnose worktrees, submodules or bare repositories.

**When to avoid:** Do not edit metadata directly based on this result.

**Syntax**

`git rev-parse --git-dir`

**Basic example**

`git rev-parse --git-dir`

Inspect the metadata path in a normal clone.

**Professional example**

`git rev-parse --absolute-git-dir`

Check an absolute metadata path while diagnosing a linked worktree.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Reports the Git directory for this repository context.

**Effects and side effects:** Reads metadata location; no repository state changes.

**Common errors:** Confusing per-worktree Git directory with the shared common directory.

**Alternatives:** Use git rev-parse --git-common-dir to inspect shared metadata location.

**Recovery:** No history recovery is necessary; correct the context and repeat the inspection.

**Version and dependencies:** No optional tool required; examples use longstanding Git syntax.

**Related lessons**

- [git-internals/01-object-database](../../git-internals/01-object-database/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-rev-parse>

## git-rev-parse-is-bare

**`git rev-parse --is-bare-repository`**

**Type:** Option usage

**Level:** Intermediate

**Find by intent:** Inspect repository state

**Risk:** Read-only. Inspect the result privately; file names, paths or history may reveal project information.

**Purpose:** Determine whether Git considers the repository bare.

**Prerequisites:** Use an owned disposable repository; run from its working directory.

**Options:** --is-bare-repository prints a boolean; -C selects a directory.

**When to use:** Before attempting working-tree commands in a local origin.

**When to avoid:** Do not infer write permission or remote access from a bare result.

**Syntax**

`git rev-parse --is-bare-repository`

**Basic example**

`git rev-parse --is-bare-repository`

Check a normal repository; expect false.

**Professional example**

`git -C origin.git rev-parse --is-bare-repository`

From a disposable parent containing origin.git, verify the origin is bare.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Prints true or false for a valid repository context.

**Effects and side effects:** Does not change repository configuration or contents.

**Common errors:** Treating false as proof that the current directory is the tree root.

**Alternatives:** Use git rev-parse --is-inside-work-tree to test working-tree context.

**Recovery:** No history recovery is necessary; correct the context and repeat the inspection.

**Version and dependencies:** No optional tool required; examples use longstanding Git syntax.

**Related lessons**

- [remote-repositories/01-remote-concepts](../../remote-repositories/01-remote-concepts/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-rev-parse>

## git-ls-files

**`git ls-files`**

**Type:** Native command

**Level:** Intermediate

**Find by intent:** Inspect files

**Risk:** Read-only. Inspect the result privately; file names, paths or history may reveal project information.

**Purpose:** List indexed paths or selected other working-tree paths.

**Prerequisites:** Use an owned disposable repository; run from its working directory.

**Options:** --stage shows index entries; --others lists untracked paths; --exclude-standard applies common ignore rules.

**When to use:** Audit tracked paths or identify untracked candidates without staging.

**When to avoid:** Do not interpret index paths as proof that their working files currently exist.

**Syntax**

`git ls-files [--stage] [--others --exclude-standard]`

**Basic example**

`git ls-files`

List indexed paths after staging a file.

**Professional example**

`git ls-files --others --exclude-standard`

Inspect nonignored untracked paths before packaging project files.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Lists paths matching the selected mode; default lists tracked index paths.

**Effects and side effects:** Reads index and possibly working-tree information without staging changes.

**Common errors:** Expecting ignored untracked files in a list using --exclude-standard.

**Alternatives:** Use git status for an overview of changes and git ls-tree for a committed tree.

**Recovery:** No history recovery is necessary; correct the context and repeat the inspection.

**Version and dependencies:** No optional tool required; examples use longstanding Git syntax.

**Related lessons**

- [git-architecture/03-file-states](../../git-architecture/03-file-states/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-ls-files>

## git-check-ignore

**`git check-ignore`**

**Type:** Native command

**Level:** Intermediate

**Find by intent:** Ignore files

**Risk:** Read-only. Inspect the result privately; file names, paths or history may reveal project information.

**Purpose:** Explain whether a path matches ignore rules and which rule applies.

**Prerequisites:** Use an owned disposable repository; run from its working directory.

**Options:** -v reports rule source and pattern; --no-index bypasses the usual tracked-path check.

**When to use:** Troubleshoot a path unexpectedly missing from untracked status.

**When to avoid:** Do not assume an ignored path is protected from access or already removed from history.

**Syntax**

`git check-ignore [-v] [--no-index] pathname`

**Basic example**

`git check-ignore notes.tmp`

Create a disposable ignore rule for notes.tmp and check the match.

**Professional example**

`git check-ignore -v build/output.log`

Explain which ignore pattern excludes an illustrative build log.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Reports matching ignored paths; exit status distinguishes matches, no match and errors.

**Effects and side effects:** Reads ignore rules and index information without changing tracked content.

**Common errors:** Expecting ordinary check-ignore to report already tracked paths.

**Alternatives:** Use git status --ignored to inspect ignored paths more broadly.

**Recovery:** No history recovery is necessary; correct the context and repeat the inspection.

**Version and dependencies:** No optional tool required; examples use longstanding Git syntax.

**Related lessons**

- [basic-commands/05-ignore-and-review](../../basic-commands/05-ignore-and-review/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-check-ignore>

## git-show-ref

**`git show-ref`**

**Type:** Native command

**Level:** Intermediate

**Find by intent:** Inspect references

**Risk:** Read-only. Inspect the result privately; file names, paths or history may reveal project information.

**Purpose:** Inspect local references and their object IDs.

**Prerequisites:** Use an owned disposable repository; run from its working directory.

**Options:** --heads limits output to branch refs; --tags limits tags; --verify requires an exact ref path.

**When to use:** Verify a reference before an operation depending on it.

**When to avoid:** Do not interpret local remote-tracking refs as live remote state.

**Syntax**

`git show-ref [--heads] [--tags]`

**Basic example**

`git show-ref --heads`

List local branch refs after the first commit.

**Professional example**

`git show-ref --verify refs/heads/main`

Verify the exact main branch ref in a disposable integration repository.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Prints matching object IDs and ref names; verification fails for a missing exact ref.

**Effects and side effects:** Reads refs without creating or moving them.

**Common errors:** Using a short branch name with --verify or checking an unborn branch.

**Alternatives:** Use git for-each-ref for custom formatting or git ls-remote for remote refs.

**Recovery:** No history recovery is necessary; correct the context and repeat the inspection.

**Version and dependencies:** No optional tool required; examples use longstanding Git syntax.

**Related lessons**

- [git-internals/05-refs-and-head](../../git-internals/05-refs-and-head/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-show-ref>

## git-count-objects

**`git count-objects`**

**Type:** Native command

**Level:** Advanced

**Find by intent:** Inspect Git objects

**Risk:** Read-only. Inspect the result privately; file names, paths or history may reveal project information.

**Purpose:** Measure loose object counts and object storage statistics.

**Prerequisites:** Use an owned disposable repository; run from its working directory.

**Options:** -v includes pack and garbage statistics; -H displays human-readable sizes.

**When to use:** Diagnose object database growth before considering maintenance.

**When to avoid:** Do not treat counts as proof of corruption or exact disk usage of the entire repository.

**Syntax**

`git count-objects [-v] [-H]`

**Basic example**

`git count-objects`

Inspect counts after a few local commits.

**Professional example**

`git count-objects -vH`

Record verbose storage statistics before proposing maintenance on a disposable clone.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Reports loose objects and sizes; verbose output includes pack statistics.

**Effects and side effects:** Reads object storage information without pruning or repacking.

**Common errors:** Confusing loose object count with total commit count.

**Alternatives:** Use git fsck for integrity diagnosis and operating-system tools for overall disk use.

**Recovery:** No history recovery is necessary; correct the context and repeat the inspection.

**Version and dependencies:** No optional tool required; examples use longstanding Git syntax.

**Related lessons**

- [git-internals/07-loose-objects-and-packfiles](../../git-internals/07-loose-objects-and-packfiles/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-count-objects>


---

<!-- navigation-footer -->
[Previous](../01-setup-and-configuration/README.md) · [Index](../README.md) · [Next](../03-working-tree-and-staging/README.md)
<!-- /navigation-footer -->
