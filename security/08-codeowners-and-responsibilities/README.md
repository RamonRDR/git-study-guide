# CODEOWNERS and responsibilities

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../07-branch-protection-and-rulesets/README.md) · [Index](../README.md) · [Next](../09-commit-and-tag-signing/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 35 min

**Prerequisites:** [Professional workflows](../../professional-workflows/README.md) · [Branch protection and rulesets](../07-branch-protection-and-rulesets/README.md)

**Objective:** Explain owner patterns and review enforcement.

## What and why

CODEOWNERS maps file patterns to responsible reviewers in hosting platforms. Git itself does not enforce it. GitHub searches `.github/CODEOWNERS`, root `CODEOWNERS`, then `docs/CODEOWNERS` in that order, using the first found on the base branch for PR review; later matching patterns override earlier ones. GitHub owners need write access; review requests are not mandatory approvals unless protection requires them. GitLab has its own file locations, syntax, sections and approval requirements; code owner approval depends on protected-branch settings and availability. Protect ownership rules themselves to reduce unauthorized changes. Treat patterns and team handles below as documentation only, not active configuration.

## Practice

For the fictional GitHub-style patterns below, choose owners for `docs/guide.md`, `.github/workflows/quality.yml` and `.github/CODEOWNERS`. Explain why a reviewer request alone cannot enforce a gate; check actual policy. Do not create teams or a CODEOWNERS file in the guide.

```text
* @fictional-org/maintainers
/docs/ @fictional-org/docs
/.github/workflows/ @fictional-org/security
/.github/CODEOWNERS @fictional-org/security
```

## Risks and recovery

Avoid copying this example into a real repository: fictional handles do not resolve. Validate matching order, owner access and enforceable rules with authorized maintainers; do not assume GitLab uses identical matching behavior.

## Exercise and self-check

Docs: docs team; workflow: security team; ownership file: security team. Mandatory approval is a separate configured policy.

## Quick reference

CODEOWNERS / pattern / owner / required review

## References

- <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners>
- <https://docs.gitlab.com/user/project/codeowners/>
