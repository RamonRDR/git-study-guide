# 10 Search & Troubleshooting

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../09-recovery-and-stash/README.md) · [Index](../README.md) · [Next](../11-advanced-git-operations/README.md)
<!-- /navigation -->

Generated from canonical catalog JSON. Edit the records, not this page.

Reference entries describe commands and operations, not a sequence to run. Use disposable repositories for practice. Hosted operations are optional.

**Total distinct entries: 8**

- [`git grep`](#git-grep)
- [`git blame`](#git-blame)
- [`git log -S`](#git-log-pickaxe-string)
- [`git log -G`](#git-log-pickaxe-regex)
- [`git log --follow`](#git-log-follow)
- [`git diff --check`](#git-diff-check)
- [`git ls-files --unmerged`](#git-ls-files-unmerged)
- [`git bisect`](#git-bisect)

## git-grep

**`git grep`**

**Type:** Native command

**Level:** Intermediate

**Find by intent:** Search content

**Risk:** Read-only. Read-only in the shown ordinary local context; avoid disclosing sensitive output. Use trusted configuration and complete local objects.

**Purpose:** Search matching lines in tracked files, index or selected trees.

**Prerequisites:** Use a disposable repository with the named files and revisions present; inspect the repository and use trusted configuration.

**Options:** -n prints line numbers; -F treats patterns literally; --cached searches index content; a tree argument searches a committed tree.

**When to use:** When locating a symbol or text within versioned content.

**When to avoid:** Do not assume ignored or untracked files are searched by default.

**Syntax**

`git grep -n -F "TODO"`

**Basic example**

`git grep -n -F "TODO"`

Find literal TODO in tracked practice files.

**Professional example**

`git grep -n -F "timeout" HEAD -- src/`

Search a committed source directory in the lab.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Prints matches with requested context; exit 1 means no matches, not necessarily an execution error.

**Effects and side effects:** The shown inspection does not intentionally modify tracked content, index, refs or remote.

**Common errors:** Confusing regular expressions with literal strings or searching the wrong snapshot.

**Alternatives:** Use a trusted filesystem search for files outside the selected Git scope.

**Recovery:** No undo is needed for inspection; verify the revision, path, search expression and exit status before interpreting results.

**Version and dependencies:** Standard Git syntax; use Git 2.40 or newer for the guide labs.

**Related lessons**

- [advanced-git/09-blame-and-grep](../../advanced-git/09-blame-and-grep/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-grep>

## git-blame

**`git blame`**

**Type:** Native command

**Level:** Intermediate

**Find by intent:** Inspect authorship, Inspect history

**Risk:** Read-only. Read-only in the shown ordinary local context; avoid disclosing sensitive output. Use trusted configuration and complete local objects.

**Purpose:** Trace each selected line to the revision that Git attributes it to.

**Prerequisites:** Use a disposable repository with the named files and revisions present; inspect the repository and use trusted configuration.

**Options:** -L limits line ranges; -w ignores whitespace differences; -M and -C can detect moved or copied lines with additional work.

**When to use:** When investigating the context of a line before making a change.

**When to avoid:** Do not use attribution as proof of fault or original authorship of an idea.

**Syntax**

`git blame HEAD -- notes.txt`

**Basic example**

`git blame HEAD -- notes.txt`

Inspect attribution of committed practice lines.

**Professional example**

`git blame -L 1,10 HEAD -- notes.txt`

Review the first ten lines of the committed file, if present.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Displays attributed commits and lines; the result depends on revision and detection options.

**Effects and side effects:** The shown inspection does not intentionally modify tracked content, index, refs or remote.

**Common errors:** Assuming the most recent attributed author introduced the underlying problem.

**Alternatives:** Inspect git show and earlier history for context; use git log -G for changed lines.

**Recovery:** No undo is needed for inspection; verify the revision, path, search expression and exit status before interpreting results.

**Version and dependencies:** Standard Git syntax; use Git 2.40 or newer for the guide labs.

**Related lessons**

- [advanced-git/09-blame-and-grep](../../advanced-git/09-blame-and-grep/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-blame>

## git-log-pickaxe-string

**`git log -S`**

**Type:** Option usage

**Level:** Advanced

**Find by intent:** Search content, Inspect history

**Risk:** Read-only. Read-only in the shown ordinary local context; avoid disclosing sensitive output. Use trusted configuration and complete local objects.

**Purpose:** Find commits whose diff changes the number of occurrences of a string.

**Prerequisites:** Use a disposable repository with the named files and revisions present; inspect the repository and use trusted configuration.

**Options:** -S uses a string; --pickaxe-regex changes its interpretation; -p shows patches.

**When to use:** When tracing when a literal was introduced or removed.

**When to avoid:** Do not use as a general search for every line edit containing the text.

**Syntax**

`git log -S "timeout" -- notes.txt`

**Basic example**

`git log -S "timeout" -- notes.txt`

Find changes in the occurrence count of timeout.

**Professional example**

`git log -p -S "timeout" -- notes.txt`

Inspect matching patches in the practice file.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Lists matching commits in selected history; edits preserving occurrence count may not match.

**Effects and side effects:** The shown inspection does not intentionally modify tracked content, index, refs or remote.

**Common errors:** Expecting -S and -G to select the same commits or overlooking merge diff settings.

**Alternatives:** Use git log -G to find matching added or removed lines.

**Recovery:** No undo is needed for inspection; verify the revision, path, search expression and exit status before interpreting results.

**Version and dependencies:** Standard Git syntax; use Git 2.40 or newer for the guide labs.

**Related lessons**

- [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.md)
- [advanced-git/09-blame-and-grep](../../advanced-git/09-blame-and-grep/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-log>

## git-log-pickaxe-regex

**`git log -G`**

**Type:** Option usage

**Level:** Advanced

**Find by intent:** Search content, Inspect history

**Risk:** Read-only. Read-only in the shown ordinary local context; avoid disclosing sensitive output. Use trusted configuration and complete local objects.

**Purpose:** Find commits with added or removed patch lines matching a regular expression.

**Prerequisites:** Use a disposable repository with the named files and revisions present; inspect the repository and use trusted configuration.

**Options:** -G accepts a regular expression; -p displays matching commit patches.

**When to use:** When tracing changes to a matching line even if occurrence counts stay equal.

**When to avoid:** Do not assume it searches unchanged lines or every historical snapshot.

**Syntax**

`git log -G "timeout" -- notes.txt`

**Basic example**

`git log -G "timeout" -- notes.txt`

Find patches with added or removed matching lines.

**Professional example**

`git log -p -G "timeout[ ]*=" -- notes.txt`

Inspect matching assignment changes in practice history.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Lists commits with matching diff lines under the selected revision and diff settings.

**Effects and side effects:** The shown inspection does not intentionally modify tracked content, index, refs or remote.

**Common errors:** Using unescaped regex metacharacters unintentionally or expecting default merge diffs to be included.

**Alternatives:** Use -S when the change in occurrence count is the relevant signal.

**Recovery:** No undo is needed for inspection; verify the revision, path, search expression and exit status before interpreting results.

**Version and dependencies:** Standard Git syntax; use Git 2.40 or newer for the guide labs.

**Related lessons**

- [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.md)
- [advanced-git/09-blame-and-grep](../../advanced-git/09-blame-and-grep/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-log>

## git-log-follow

**`git log --follow`**

**Type:** Option usage

**Level:** Intermediate

**Find by intent:** Inspect history, Search content

**Risk:** Read-only. Read-only in the shown ordinary local context; avoid disclosing sensitive output. Use trusted configuration and complete local objects.

**Purpose:** Continue the history of one file across detected renames.

**Prerequisites:** Use a disposable repository with the named files and revisions present; inspect the repository and use trusted configuration.

**Options:** --follow operates on a single path; -p includes patches.

**When to use:** When investigating a file whose path changed.

**When to avoid:** Do not expect complete directory history or perfect tracking through complex renames and merges.

**Syntax**

`git log --follow -- notes.txt`

**Basic example**

`git log --follow -- notes.txt`

Inspect history of one current file across detected renames.

**Professional example**

`git log -p --follow -- docs/notes.txt`

Inspect patches of one documentation file across detected renames.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Displays history of the selected file including detected previous names, subject to history and rename detection.

**Effects and side effects:** The shown inspection does not intentionally modify tracked content, index, refs or remote.

**Common errors:** Passing multiple paths or interpreting absence of a detected rename as proof of no relationship.

**Alternatives:** Inspect git log --name-status and commit diffs for complex file reorganizations.

**Recovery:** No undo is needed for inspection; verify the revision, path, search expression and exit status before interpreting results.

**Version and dependencies:** Standard Git syntax; use Git 2.40 or newer for the guide labs.

**Related lessons**

- [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.md)
- [advanced-git/09-blame-and-grep](../../advanced-git/09-blame-and-grep/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-log>

## git-diff-check

**`git diff --check`**

**Type:** Option usage

**Level:** Intermediate

**Find by intent:** Review changes, Inspect repository state

**Risk:** State change. Inspection may refresh index metadata; it does not fix errors.

**Purpose:** Flag introduced conflict markers and whitespace errors according to configuration.

**Prerequisites:** Use a disposable repository with the named files and revisions present; inspect the repository and use trusted configuration.

**Options:** --check reports problems and exits nonzero when detected; --cached selects staged changes.

**When to use:** When checking a proposed change before commit or review.

**When to avoid:** Do not substitute it for tests or a full conflict inspection.

**Syntax**

`git diff --check`

**Basic example**

`git diff --check`

Check unstaged changes for introduced whitespace errors or conflict markers.

**Professional example**

`git diff --cached --check`

Check staged changes before a reviewed commit.

**State effects**

- Working tree: Unchanged
- Index: Conditional
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Reports offending lines when detected; no automatic correction occurs.

**Effects and side effects:** Does not edit file content; ordinary working-tree diff may refresh index stat metadata.

**Common errors:** Checking only unstaged edits when the intended commit is staged.

**Alternatives:** Use git diff --cached for content review and a project-specific linter for broader formatting rules.

**Recovery:** No undo is needed for inspection; verify the revision, path, search expression and exit status before interpreting results.

**Version and dependencies:** Standard Git syntax; use Git 2.40 or newer for the guide labs.

**Related lessons**

- [basic-commands/05-ignore-and-review](../../basic-commands/05-ignore-and-review/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-diff>

## git-ls-files-unmerged

**`git ls-files --unmerged`**

**Type:** Option usage

**Level:** Intermediate

**Find by intent:** Inspect index internals, Resolve conflicts

**Risk:** Read-only. Read-only in the shown ordinary local context; avoid disclosing sensitive output. Use trusted configuration and complete local objects.

**Purpose:** Inspect index entries that still have unmerged stages.

**Prerequisites:** Use a disposable repository with the named files and revisions present; inspect the repository and use trusted configuration.

**Options:** -u or --unmerged shows unmerged paths with mode, object ID and stage; a pathspec narrows output.

**When to use:** When diagnosing conflicts before staging a resolution.

**When to avoid:** Do not treat empty output as proof that the final resolution is correct.

**Syntax**

`git ls-files --unmerged`

**Basic example**

`git ls-files --unmerged`

Inspect unmerged index entries during a practice conflict.

**Professional example**

`git ls-files -u -- notes.txt`

Inspect conflict stages of a named file in the lab.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Lists available conflict stages; stages 1, 2 and 3 represent base and two sides when present.

**Effects and side effects:** The shown inspection does not intentionally modify tracked content, index, refs or remote.

**Common errors:** Assuming every conflict has all three stages or that ours always means the original feature during rebase.

**Alternatives:** Use git status for a summary and inspect each available stage with git show.

**Recovery:** No undo is needed for inspection; verify the revision, path, search expression and exit status before interpreting results.

**Version and dependencies:** Standard Git syntax; use Git 2.40 or newer for the guide labs.

**Related lessons**

- [merge-and-conflicts/04-conflict-resolution](../../merge-and-conflicts/04-conflict-resolution/README.md)
- [git-internals/06-index-internals](../../git-internals/06-index-internals/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-ls-files>

## git-bisect

**`git bisect`**

**Type:** Workflow

**Level:** Advanced

**Find by intent:** Find a regression, Inspect history

**Risk:** State change. Check out only trusted historical code in an isolated lab; do not automatically run unknown scripts. Keep original work safe.

**Purpose:** Find a regression boundary by repeatedly classifying historical commits.

**Prerequisites:** Use a clean disposable repository with complete history, saved original tip, known good and bad commits and a repeatable safe test.

**Options:** Start, mark bad and good revisions, test each candidate, classify with good or bad, skip untestable commits and finish with git bisect reset.

**When to use:** When a repeatable test distinguishes a known failing revision from an earlier passing revision.

**When to avoid:** Avoid with unpreserved edits or unreliable tests; historical code may be untrusted.

**Syntax**

`git bisect start`

**Basic example**

`git bisect start`

Start a bisect in a clean isolated lab with known good and bad commits; mark them separately.

**Professional example**

`git bisect good`

After testing the checked-out candidate with a repeatable trusted test, mark it good; use bad when it fails.

**State effects**

- Working tree: Conditional
- Index: Conditional
- Objects / refs / history: Conditional
- Remote repository: Unchanged
- Other state: Changes

**Expected result:** Git selects candidates, typically detached, until it identifies a boundary or reports ambiguity; reset returns to the original checkout by default.

**Effects and side effects:** Bisect can select commits, update index and files, and create temporary refs and metadata; test scripts can have independent effects.

**Common errors:** Marking a candidate without testing or leaving bisect state active after investigation.

**Alternatives:** Use git log -G or manual inspection when a reliable test cannot classify revisions.

**Recovery:** Save the result and any desired work; run git bisect reset and verify original checkout and status. Stop and inspect if restoration fails.

**Version and dependencies:** Standard Git syntax; use Git 2.40 or newer for the guide labs.

**Related lessons**

- [advanced-git/01-bisect](../../advanced-git/01-bisect/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-bisect>


---

<!-- navigation-footer -->
[Previous](../09-recovery-and-stash/README.md) · [Index](../README.md) · [Next](../11-advanced-git-operations/README.md)
<!-- /navigation-footer -->
