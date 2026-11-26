# Git tags and GitLab releases

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../06-pipelines-and-runners/README.md) · [Index](../README.md) · [Next](../08-gitlab-cli-and-platform-comparison/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 25 min

**Prerequisites:** [GitHub](../../github/README.md) · [Remotes](../../remote-repositories/README.md)

**Objective:** Distinguish version refs from publication metadata and validate the intended revision.

## What and why

A Git tag names an object, commonly a commit; a lightweight tag directly references the object, an annotated tag adds a tag object with metadata and message. A GitLab release associates a tag with release notes and assets or asset links. Tags remain in Git; release notes and attachments are hosted metadata, not automatically included in a clone. A professional release identifies the reviewed commit, summarizes changes and describes limitations. A protected tag can restrict tag operations according to configuration; do not assume branch protection also protects tags. Avoid moving a published tag: consumers may already have fetched it. Prefer a new corrected version according to the release policy.

## Practice

Repeat the safe local tag exercise from [GitHub tags and releases](../../github/07-tags-and-releases/README.md) in its disposable repository, without publishing. Compare `git show v1.0.0` (if that tag exists) with a fictional release note describing catalog setup and a known limitation. Use `git tag --list` to inspect existing tags before selecting one. Optional: inspect an existing public GitLab release without downloading or executing assets. Match its tag and notes; do not create a hosted release.

## Common mistakes and safety

Never publish a tag pointing to an unreviewed commit or include secrets in notes/assets. If a release references the wrong commit, stop distribution, notify maintainers and follow correction policy; do not silently rewrite public tags.

## Exercise and self-check

Pass if a tag identifies a revision, notes communicate changes, and an asset is not trusted merely because a release exists. The offline exercise requires no account.

## Official sources

- <https://docs.gitlab.com/user/project/releases/>
- <https://git-scm.com/docs/git-tag>
