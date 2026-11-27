# Release Management

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../06-automated-quality-pipeline/README.md) · [Index](../README.md) · [Next](../08-professional-engineering-workflow/README.md)
<!-- /navigation -->

**Level:** advanced · **Estimated time:** 60 min

**Prerequisites:** [professional-workflows/12-release-management](../../professional-workflows/12-release-management/README.md) · Git 2.40+ · Bash/Git Bash · tar

**Objective:** Record and tag version 1.0.0, add ready without removing draft, review and tag 1.1.0, then prepare a source archive of that tagged snapshot. Make a later change and demonstrate that the release tag still points to the earlier commit.

## Scenario

A fictional text catalog declares a public status contract. The initial release supports draft; an additive, backward-compatible ready example motivates a minor release. Local annotated tags identify exact revisions; no platform release is published.

## Disposable setup

Use only the Disposable setup section of [My First Repository](../01-my-first-repository/README.md). Start a fresh dedicated Bash/Git Bash shell; verify printed sandbox root, fictional identities and no remotes before proceeding. Do not run project 01's challenge. Git 2.40+. Run one command at a time, stop on any unexpected failure and never run these commands in the guide.

## Challenge

Record and tag version 1.0.0, add ready without removing draft, review and tag 1.1.0, then prepare a source archive of that tagged snapshot. Make a later change and demonstrate that the release tag still points to the earlier commit. Try before reading the solution.

## Progressive hints

SemVer minor means backward-compatible public functionality under the stated contract, not simply number of edits. Annotated tags are objects that peel to commits; use git archive for snapshot content and inspect the archive.

## Reference solution

Record the two versions with explicit release notes in the tag messages. Verify existing draft functionality is retained.

```bash
printf '%s\n' 'status: draft' > catalog.txt
git add catalog.txt
git commit -m 'docs: initialize catalog'
git tag -a v1.0.0 -m 'Initial draft contract'
printf '%s\n' 'status: draft' 'status: ready' > catalog.txt
git add catalog.txt
git diff --cached --check
git diff --cached
git commit -m 'feat: add ready status'
git tag -a v1.1.0 -m 'Add backward-compatible ready status'
released=$(git rev-parse 'v1.1.0^{commit}')
git cat-file -t v1.1.0
git archive --format=tar --output="$sandbox/catalog-v1.1.0.tar" v1.1.0
tar -tf "$sandbox/catalog-v1.1.0.tar"
tar -xOf "$sandbox/catalog-v1.1.0.tar" catalog.txt
```

Advance local main with a separate future change; prove the tag is immutable by convention, not automatically protected by local Git.

```bash
printf '%s\n' 'future work' > future.txt
git add future.txt
git commit -m 'docs: begin future work'
test "$(git rev-parse 'v1.1.0^{commit}')" = "$released"
test "$(git rev-parse HEAD)" != "$released"
git show v1.0.0:catalog.txt
git show v1.1.0:catalog.txt
git status --porcelain
```

## Success checks

Both tags are annotated; v1.1.0 retains draft and adds ready, and its tar archive contains only catalog.txt with that exact content, no .git or future.txt. The tag does not move when main advances. Explain why this is not a release published on a hosting platform.

Fixed maintainer test (not learner code): `tests/test_git_practical_projects.py::test_release_management`.

## Recovery and cleanup

Verify version names and targets before tagging. Do not overwrite a published tag; use the project's release-correction policy. Optional hosted draft release only in an authorized owned repository with an existing verified tag and no paid prerequisite. Close the dedicated shell and remove only the verified printed sandbox using a file manager. Preserve desired work first.

## Official sources

- <https://git-scm.com/docs/git-tag>
- <https://git-scm.com/docs/git-archive>
- <https://git-scm.com/docs/git-show>
- <https://semver.org/spec/v2.0.0.html>

---

<!-- navigation-footer -->
[Previous](../06-automated-quality-pipeline/README.md) · [Index](../README.md) · [Next](../08-professional-engineering-workflow/README.md)
<!-- /navigation-footer -->
