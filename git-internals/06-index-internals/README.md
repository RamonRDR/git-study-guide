# Index internals: staged entries

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../05-refs-and-head/README.md) · [Index](../README.md) · [Next](../07-loose-objects-and-packfiles/README.md)
<!-- /navigation -->

**Level:** advanced · **Estimated time:** 45 min

**Prerequisites:** [14 Git Internals](../README.md) · [Advanced Git](../../advanced-git/README.md)

**Objective:** The index records paths, modes, object IDs and metadata for the prospective tree.

## What and why

The index records paths, modes, object IDs and metadata for the prospective tree. Ordinary entries have stage 0; an unresolved three-way merge may have stages 1 (base), 2 (ours) and 3 (theirs), depending on conflict type. `write-tree` materializes a tree from the fully merged index without making a commit. Avoid directly editing the binary index.

```text
working tree --add--> index --write-tree--> tree object
                       |                      |
                       +--- git commit ------> commit -> branch ref advances
```

Working file → add → index (stage 0) → write-tree → tree object; commit also advances the checked-out branch.

## Practice

Create a fresh isolated fixture from the linked Advanced Git module index before each practice. Run commands individually and stop on unexpected results. Confirm root and printed sandbox. Git 2.34+ practice baseline, Bash (Git Bash on Windows).

Stage one fictional edit in the fresh fixture. Compare staged and HEAD blob IDs. `git write-tree` writes or reuses tree objects; it does not move HEAD. Use `git ls-files -u` to inspect conflict entries in a conflict lab, not to create conflicts here. Restore the staged and working file only in this disposable fixture.

```bash
before=$(git rev-parse HEAD)
git ls-files --stage
printf '%s\n' reviewed > src/state.txt
git add -- src/state.txt
git ls-files --stage -- src/state.txt
git diff --cached -- src/state.txt
git write-tree
test "$(git rev-parse HEAD)" = "$before"
git restore --staged --worktree -- src/state.txt
git status --short
```

## Common mistakes and safety

Use the disposable fixture only. Never modify object or ref files by hand, force pruning, or run experiments against a real repository. If state differs, inspect with status, log and read-only plumbing; close the dedicated shell and remove only the recorded sandbox through the file manager after reviewing contents.

## Exercise and self-check

Working file → add → index (stage 0) → write-tree → tree object; commit also advances the checked-out branch. Why can write-tree fail in conflicts? The index has unresolved entries.

## Quick reference

- `git ls-files --stage`
- `git add -- src/state.txt`
- `git ls-files --stage -- src/state.txt`
- `git diff --cached -- src/state.txt`

## Official sources

- [https://git-scm.com/docs/git-ls-files](https://git-scm.com/docs/git-ls-files)
- [https://git-scm.com/docs/git-write-tree](https://git-scm.com/docs/git-write-tree)
- [https://git-scm.com/docs/gitformat-index](https://git-scm.com/docs/gitformat-index)

---

<!-- navigation-footer -->
[Previous](../05-refs-and-head/README.md) · [Index](../README.md) · [Next](../07-loose-objects-and-packfiles/README.md)
<!-- /navigation-footer -->
