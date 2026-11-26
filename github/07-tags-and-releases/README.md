# Tags and GitHub Releases

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../06-protection-and-rulesets/README.md) · [Index](../README.md) · [Next](../08-github-cli/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 30 min

**Prerequisites:** [Remotes](../../remote-repositories/README.md) · [History & recovery](../../history-and-recovery/README.md) · [Branch protection, rulesets and quality gates](../06-protection-and-rulesets/README.md) · [First repository](../../getting-started/03-first-repository/README.md) · [First commit](../../getting-started/05-first-commit/README.md)

**Objective:** Distinguish Git version refs from release metadata and verify a release target.

## What and why

A tag is a Git ref naming an object, normally a commit. A lightweight tag points directly; an annotated tag stores a tag object with metadata and message. Branches normally advance; release tags should remain stable. GitHub Release adds hosted notes, downloadable assets and draft/prerelease state associated with a tag. Publishing a release is not automatic deployment. SemVer uses MAJOR.MINOR.PATCH for public API compatibility; v0.1.0 is a common tag spelling for early development, not a guarantee of stability. Release assets are separate from source Git history; verify origin, integrity and permissions before use.

## Practice

Offline local lab: start a fresh isolated repository using module 00 first-repository and first-commit lessons. Confirm recorded disposable root, clean main with one fictional commit, no remotes, no tags, and fictional effective identities. Run commands individually and stop on unexpected output. The commands below create an annotated local tag, inspect its type and compare the peeled commit with HEAD. No push. Draft release notes with scope, verification and limitations. Optional read-only: inspect a public release and its tag, without downloading or executing assets.

```text
git rev-parse --show-toplevel
git branch --show-current
git status --short
git remote -v
git tag --list
git rev-list --count HEAD
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Only proceed if every precondition above is satisfied.

```text
git tag -a v0.1.0 -m "Release 0.1.0"
git cat-file -t v0.1.0
git rev-parse 'v0.1.0^{commit}' HEAD
git show v0.1.0
git status --short
```


## Common mistakes and safety

Do not move or delete a published release tag to silently change an artifact. Publish a reviewed correction under a new version where appropriate. Never upload secrets or unverified binaries. Close the dedicated shell and delete only the recorded disposable parent if no longer needed; no hosted release is created.

## Exercise and self-check

Pass if tag object type is tag, the two resolved commit IDs match, main is unchanged and you explain why release notes are not Git commits. If practicing only on paper, predict the output instead.

## Quick reference

- `git tag -a TAG -m MESSAGE`
- `git cat-file -t TAG`
- `git rev-parse 'TAG^{commit}'`

## Official sources

- <https://git-scm.com/docs/git-tag>
- <https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases>
- <https://semver.org/>

---

<!-- navigation-footer -->
[Previous](../06-protection-and-rulesets/README.md) · [Index](../README.md) · [Next](../08-github-cli/README.md)
<!-- /navigation-footer -->
