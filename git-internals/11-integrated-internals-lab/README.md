# Integrated Git internals lab

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../10-porcelain-and-plumbing/README.md) · [Index](../README.md) · [Next module](../../command-reference/README.md)
<!-- /navigation -->

**Level:** advanced · **Estimated time:** 55 min

**Prerequisites:** [14 Git Internals](../README.md) · [Advanced Git](../../advanced-git/README.md)

**Objective:** Inspect a snapshot from its branch ref through commit, root tree and blob.

## What and why

Inspect a snapshot from its branch ref through commit, root tree and blob. Then compare staged state with HEAD without committing, and verify that packing does not change identity. This is a diagnostic exercise, not a manual object repair. A professional investigation records object IDs and exact commands, not private contents.

```text
HEAD -> refs/heads/main -> commit -> root tree -> subtree -> blob
index ---------------------------> prospective tree (write-tree)
```

Pass when all tests exit zero.

## Practice

Create a fresh isolated fixture from the linked Advanced Git module index before each practice. Run commands individually and stop on unexpected results. Confirm root and printed sandbox. Git 2.34+ practice baseline, Bash (Git Bash on Windows).

Use the fresh fixture. The expected types are commit, tree and blob; staged tree differs from the original, HEAD stays fixed, and restore returns a clean state. Repack without deletion flags; assert original blob remains readable. Stop at any failed test, inspect state and discard only the lab if necessary.

```bash
commit=$(git rev-parse HEAD)
tree=$(git rev-parse HEAD^{tree})
blob=$(git rev-parse HEAD:src/state.txt)
test "$(git cat-file -t "$commit")" = commit
test "$(git cat-file -t "$tree")" = tree
test "$(git cat-file -t "$blob")" = blob
test "$(git cat-file -p "$blob")" = bad
printf '%s\n' reviewed > src/state.txt
git add -- src/state.txt
staged=$(git write-tree)
test "$staged" != "$tree"
test "$(git rev-parse HEAD)" = "$commit"
git restore --staged --worktree -- src/state.txt
git repack -a
test "$(git rev-parse HEAD)" = "$commit"
test "$(git cat-file -p "$blob")" = bad
test -z "$(git status --porcelain)"
test -z "$(git remote)"
```

## Common mistakes and safety

Use the disposable fixture only. Never modify object or ref files by hand, force pruning, or run experiments against a real repository. If state differs, inspect with status, log and read-only plumbing; close the dedicated shell and remove only the recorded sandbox through the file manager after reviewing contents.

## Exercise and self-check

Pass when all tests exit zero. Explain the graph: HEAD → branch → commit → tree → blob; index → prospective tree. Why is repack transparent to this graph? IDs do not depend on storage encoding.

## Quick reference

- `git add -- src/state.txt`
- `git restore --staged --worktree -- src/state.txt`
- `git repack -a`

## Official sources

- [https://git-scm.com/docs/git-cat-file](https://git-scm.com/docs/git-cat-file)
- [https://git-scm.com/docs/git-write-tree](https://git-scm.com/docs/git-write-tree)
- [https://git-scm.com/docs/git-repack](https://git-scm.com/docs/git-repack)
- [https://git-scm.com/docs/git-rev-parse](https://git-scm.com/docs/git-rev-parse)

---

<!-- navigation-footer -->
[Previous](../10-porcelain-and-plumbing/README.md) · [Index](../README.md) · [Next module](../../command-reference/README.md)
<!-- /navigation-footer -->
