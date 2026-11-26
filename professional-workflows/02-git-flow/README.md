# Git Flow

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../01-feature-branch-workflow/README.md) · [Index](../README.md) · [Next](../03-github-flow/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 40 min

**Prerequisites:** [CI/CD](../../ci-cd/README.md) · [Feature Branch Workflow](../01-feature-branch-workflow/README.md)

**Objective:** Explain release and hotfix paths and their cost.

## What and why

Git Flow is a branching convention designed around scheduled releases. In the classic model, `main` holds released history, `develop` accumulates upcoming work, feature branches originate from and return to develop, release branches prepare a release, and hotfix branches address urgent production fixes from main. A release is merged into main and its changes back into develop; the release commit is tagged. Hotfixes must also reach the development line and any relevant active release according to policy. Names and exact integration methods are team conventions, not Git requirements. This can support parallel maintained versions or controlled release windows, but extra long-lived refs increase synchronization, conflict and review overhead.

```text
feature -> develop -> release preparation -> main/tag
hotfix from affected release -> corrected release + compatible propagation
```

## Practice

Draw a catalog release at 2.0.0 being stabilized while develop contains 2.1 work. A critical bug appears in released 1.9. Decide where to start the hotfix (the actual 1.9 production revision or supported maintenance line), test it, tag the corrected release and propagate the compatible fix to other relevant lines. If using the classic model with main at 1.9, draw hotfix -> main and hotfix -> develop; account for the active release as well.

## Risks and recovery

Do not assume main always equals deployed production; verify the release identifier. Never overwrite published tags or merge unrelated future features into a hotfix. If backporting causes conflicts, resolve and retest separately on each supported line. Avoid Git Flow when its extra branches add cost without a release need.

## Exercise and self-check

The hotfix begins at the affected supported revision, not arbitrary develop. Record the tested release tag and compatible propagation paths.

## Quick reference

main / develop / feature / release / hotfix

## Sources

- <https://nvie.com/posts/a-successful-git-branching-model/>
- <https://www.atlassian.com/git/tutorials/comparing-workflows>
- <https://git-scm.com/docs/gitworkflows>
