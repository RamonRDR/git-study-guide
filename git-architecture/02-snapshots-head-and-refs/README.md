# Snapshots, HEAD and references

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../01-three-locations/README.md) · [Index](../README.md) · [Next](../03-file-states/README.md)
<!-- /navigation -->

**Level:** beginner · **Estimated time:** 25 min

**Prerequisites:** [Working tree, index and repository](../01-three-locations/README.md)

**Objective:** Explain what a commit and a branch reference represent.

## What and why

A commit points to a tree representing a project snapshot and usually to its parent commit(s), with metadata such as identity and message. Git stores content-addressed objects; equal file contents can share the same stored object. Git can calculate differences between snapshots; a commit is not just a patch file. A ref is a name pointing to an object (for a branch, a commit). HEAD normally refers symbolically to the current branch; in detached HEAD it points directly to a commit, covered later. Before a first commit HEAD can name a branch that does not yet have a commit.

## Practice

Continue the isolated lab from chapter 01. Before committing, verify root, staged content and both identities. Record only the staged second version:

```text
git rev-parse --show-toplevel
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
git diff --cached
```

Stop if root is wrong, identities are not fictional or diff is unexpected. Otherwise:

```text
git commit -m "docs: revise note"
git symbolic-ref HEAD
git rev-parse HEAD
git rev-parse refs/heads/main
git log -2 --oneline
git show HEAD:note.txt
git status --short
```

Expected: refs/heads/main; both rev-parse commands return the same object ID, which varies between labs. The second commit points to the first as parent. HEAD:note.txt contains second; the working file remains third and status shows space then M. Diagram: HEAD -> main -> C2 -> C1, where the last arrow follows parent history.

## Common mistakes and safety

Do not memorize IDs or assume branch names are always main. Never move refs by editing .git. Commit IDs depend on snapshot, parents and metadata; changing history changes IDs. No destructive operation is needed here.

## Exercise and self-check

Explain HEAD versus main versus a commit ID. Hint: one points to a branch, one names a commit, one identifies an object. Answer: HEAD normally names current branch; branch advances on commit; object ID identifies immutable commit content. Pass if you can verify the two rev-parse results.

## Quick reference

- `git rev-parse`
- `git symbolic-ref`
- `git log`
- `git show`
- `gitglossary`

## Official sources

- [Git: git-rev-parse](https://git-scm.com/docs/git-rev-parse)
- [Git: git-symbolic-ref](https://git-scm.com/docs/git-symbolic-ref)
- [Git: git-log](https://git-scm.com/docs/git-log)
- [Git: git-show](https://git-scm.com/docs/git-show)
- [Git: gitglossary](https://git-scm.com/docs/gitglossary)
