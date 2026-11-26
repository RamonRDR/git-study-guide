# Start points and branch comparison

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../01-create-and-switch/README.md) · [Index](../README.md) · [Next](../03-switch-safety-and-naming/README.md)
<!-- /navigation -->

**Level:** beginner · **Estimated time:** 30 min

**Prerequisites:** [Create and switch local branches](../01-create-and-switch/README.md)

**Objective:** Choose a start commit and compare branch histories and snapshots.

## What and why

Branches may start at a named local branch or a commit ID, rather than current HEAD. HEAD~1 means the first parent of HEAD. A branch diverges when both sides have commits absent from the other. `git log A..B` lists commits reachable from B but not A; reversing the names changes the set. `git diff A B` compares the endpoint trees, not the count of commits. `git diff A..B` also compares endpoints; `git diff A...B` compares the merge base (a best common ancestor) to B. Merge and rebase behavior will be taught next module; these commands only inspect.

## Practice

Continue with clean feat/note (C2). Create a new branch from its parent C1, and select a new docs branch starting at main. Verify root and clean status first:

```text
git branch archive/base HEAD~1
git rev-parse archive/base main
git switch -c docs/overview main
git branch --show-current
git status --short
```

Expected: archive/base and main same ID, current docs/overview at C1. Create overview.txt with overview plus final newline. Stage and inspect:

```text
git add -- overview.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Only with expected diff and fictional identities:

```text
git commit -m "docs: add overview"
git log --all --graph --oneline --decorate
git log --oneline feat/note..docs/overview
git log --oneline docs/overview..feat/note
git diff --name-status feat/note docs/overview
git diff --name-status feat/note...docs/overview
git merge-base feat/note docs/overview
git rev-parse main
```

Expected: one distinct commit in each log range. Endpoint diff shows modified note.txt and added overview.txt; three-dot diff shows only added overview.txt. Both final IDs from merge-base/main match. Diagram: feat/note -> C2 -> C1; docs/overview -> C3 -> C1; main and archive/base -> C1. No history changed during comparison.

## Common mistakes and safety

Never assume log ranges and diff ranges have the same meaning. A branch name can move; inspect rev-parse before choosing a base. If expected IDs differ, inspect the graph instead of moving references by force.

## Exercise and self-check

Which comparison isolates commits made on docs/overview but not feat/note? Answer: git log feat/note..docs/overview. Which diff shows docs/overview changes since their common ancestor? Answer: git diff feat/note...docs/overview. Pass if both outputs match the graph. Professional use: inspect review scope.

## Quick reference

`git branch NAME START`: create at start; `git log A..B`: commits exclusive to B relative to A; `git diff A B`: trees; `git diff A...B`: base to B.

## Official sources

- [Git: git-branch](https://git-scm.com/docs/git-branch)
- [Git: git-log](https://git-scm.com/docs/git-log)
- [Git: git-diff](https://git-scm.com/docs/git-diff)
- [Git: git-merge-base](https://git-scm.com/docs/git-merge-base)
- [Git: gitrevisions](https://git-scm.com/docs/gitrevisions)

---

<!-- navigation-footer -->
[Previous](../01-create-and-switch/README.md) · [Index](../README.md) · [Next](../03-switch-safety-and-naming/README.md)
<!-- /navigation-footer -->
