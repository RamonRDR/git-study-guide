# Commits and annotated tags

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../02-blobs-and-trees/README.md) · [Index](../README.md) · [Next](../04-object-hashes/README.md)
<!-- /navigation -->

**Level:** advanced · **Estimated time:** 45 min

**Prerequisites:** [14 Git Internals](../README.md) · [Advanced Git](../../advanced-git/README.md)

**Objective:** A commit object contains a root tree ID, zero or more parents, author, committer, timestamps and a message.

## What and why

A commit object contains a root tree ID, zero or more parents, author, committer, timestamps and a message. A merge has multiple parents; a root commit has none. Annotated tags are objects containing metadata and a target; lightweight tags are refs without a tag object. A signature is additional metadata, not automatic proof of identity.

```text
refs/tags/annotated -> tag object -> commit C -> tree T
refs/tags/lightweight ---------------> commit C
refs/heads/main ---------------------> commit C
                                      |
                                      +-> parent P
```

Tag object → commit → tree; branch ref → commit.

## Practice

Create a fresh isolated fixture from the linked Advanced Git module index before each practice. Run commands individually and stop on unexpected results. Confirm root and printed sandbox. Git 2.34+ practice baseline, Bash (Git Bash on Windows).

Create unsigned fictional tags in the fixture only. Inspect their types and compare the peeled annotated tag (`^{commit}`) with HEAD. A release review should record the resolved commit rather than trust a display name. Do not force-update published tags.

```bash
git cat-file -p HEAD
git rev-list --parents -1 HEAD
git tag lightweight
git tag -a annotated -m "Example release"
git cat-file -t lightweight
git cat-file -t annotated
git cat-file -p annotated
test "$(git rev-parse annotated^{commit})" = "$(git rev-parse HEAD)"
```

## Common mistakes and safety

Use the disposable fixture only. Never modify object or ref files by hand, force pruning, or run experiments against a real repository. If state differs, inspect with status, log and read-only plumbing; close the dedicated shell and remove only the recorded sandbox through the file manager after reviewing contents.

## Exercise and self-check

Tag object → commit → tree; branch ref → commit. What changes when main advances? The branch ref; neither tag moves automatically.

## Quick reference

- `git cat-file -p HEAD`
- `git rev-list --parents -1 HEAD`
- `git tag lightweight`
- `git tag -a annotated -m "Example release"`

## Official sources

- [https://git-scm.com/docs/git-commit-tree](https://git-scm.com/docs/git-commit-tree)
- [https://git-scm.com/docs/git-tag](https://git-scm.com/docs/git-tag)
- [https://git-scm.com/docs/git-rev-parse](https://git-scm.com/docs/git-rev-parse)

---

<!-- navigation-footer -->
[Previous](../02-blobs-and-trees/README.md) · [Index](../README.md) · [Next](../04-object-hashes/README.md)
<!-- /navigation-footer -->
