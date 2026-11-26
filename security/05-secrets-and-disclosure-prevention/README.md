# Secrets and disclosure prevention

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../04-credential-managers/README.md) · [Index](../README.md) · [Next](../06-permissions-and-least-privilege/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 40 min

**Prerequisites:** [Professional workflows](../../professional-workflows/README.md) · [Credential managers and configuration scope](../04-credential-managers/README.md)

**Objective:** Prevent accidental disclosure and inspect tracking.

## What and why

A secret is confidential authentication material or another sensitive value. Store real secrets in an approved secret manager outside source control. Publish only sanitized templates with non-secret examples. `.gitignore` matches intentionally untracked paths; it does not untrack files already in the index or erase history. `git check-ignore -- path` checks ignore rules for an untracked path; `git ls-files -- path` inspects tracked entries. A staged-name check helps prevent accidental additions but does not inspect content. Secret scanning and push protection are heuristic, provider-dependent defenses, not proof of absence. Remove or mask sensitive values before sharing logs and artifacts; never publish real secrets even in private repositories.

## Practice

Use chapter 13 with harmless `mode=local` and `mode=example` values. Predict which paths are ignored and staged. For a hypothetical already tracked local file, explain why adding it to ignore rules is insufficient; an authorized correction must remove it from tracking and assess prior exposure.

## Risks and recovery

Never create a realistic-looking fake token, paste a real secret into a scanner, or use force-add to bypass ignore rules. On exposure, prioritize revocation and incident response; deleting the file alone is insufficient.

## Exercise and self-check

Ignore and tracking are separate; the example template is safe only because content is deliberately non-sensitive. Scanning is defense in depth.

## Quick reference

`git check-ignore` / `git ls-files` / `.gitignore`

## References

- <https://git-scm.com/docs/gitignore>
- <https://git-scm.com/docs/git-check-ignore>
- <https://git-scm.com/docs/git-ls-files>
- <https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning>
