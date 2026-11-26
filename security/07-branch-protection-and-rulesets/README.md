# Branch protection and rulesets

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../06-permissions-and-least-privilege/README.md) · [Index](../README.md) · [Next](../08-codeowners-and-responsibilities/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 40 min

**Prerequisites:** [Professional workflows](../../professional-workflows/README.md) · [Permissions and least privilege](../06-permissions-and-least-privilege/README.md)

**Objective:** Distinguish enforceable branch rules and team policy.

## What and why

Native Git branches are refs; hosting services add server-side rules. GitHub branch protection and rulesets can restrict pushes, deletion, force-push, merge methods, checks and reviews; multiple applicable rulesets can combine. GitLab protected branches and merge checks govern allowed push/merge actions and pipeline conditions. Capabilities vary by plan, visibility and settings. Enforced checks must be distinguished from a written team policy: a human authorization protocol may exist even if no numeric approving-review requirement is configured. Verify exact target, enforcement mode, effective actors/bypass, check names and stale-review behavior. Linear history is not a guarantee that every change was reviewed.

## Practice

Offline: design rules for a public catalog: PR required, Ubuntu/Windows checks, no bypass, no direct push, no force-push or deletion on main, squash only, resolved discussions, and separate human authorization. Given an earlier green SHA and a newer untested SHA, decide whether merge is permitted. Read-only inspect public settings only if available; never edit the guide's settings.

## Risks and recovery

Never remove a protection or add a bypass merely to unblock CI. Diagnose actual failed/pending checks; correct the scoped change and revalidate. Administrative changes require separate authorization.

## Exercise and self-check

New SHA has no valid evidence yet. Keep protections and obtain fresh validation and explicit authorization.

## Quick reference

protected branch / ruleset / required checks / bypass

## References

- <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets>
- <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches>
- <https://docs.gitlab.com/user/project/repository/branches/protected/>

---

<!-- navigation-footer -->
[Previous](../06-permissions-and-least-privilege/README.md) · [Index](../README.md) · [Next](../08-codeowners-and-responsibilities/README.md)
<!-- /navigation-footer -->
