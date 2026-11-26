# Commit and tag signing

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../08-codeowners-and-responsibilities/README.md) · [Index](../README.md) · [Next](../10-software-supply-chain/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 40 min

**Prerequisites:** [Professional workflows](../../professional-workflows/README.md) · [CODEOWNERS and responsibilities](../08-codeowners-and-responsibilities/README.md)

**Objective:** Interpret signatures and their limits.

## What and why

A cryptographic signature binds a Git object to a signing key and can be verified with appropriate trust configuration. Git supports OpenPGP, SSH and X.509 signing formats depending on version and tooling. A signed commit and an annotated signed tag are different objects; an annotated tag without a signature is not signed. `git verify-commit` and `git verify-tag` verify signatures with suitable key/trust configuration. A host's Verified badge follows its own verification policy; it is not proof that code is safe, approved or deployed. A new commit created by rebase or squash has a different identity and does not inherit the original commit signature. SSH authentication and SSH signing are separate uses.

## Practice

Offline: compare unsigned commit A, validly signed commit B from an unknown key, and signed commit C with a trusted key but failing tests. Identify what each piece of evidence proves. Sketch verification of an annotated signed release tag and its target commit. No keys need to be generated or uploaded.

## Risks and recovery

Never expose private signing keys, ignore untrusted keys or treat a green badge as a review. On key compromise, revoke/rotate, assess affected signatures and coordinate trust-policy updates; do not rewrite public history unilaterally.

## Exercise and self-check

A has no signature evidence; B needs trusted identity verification; C still fails quality gates. Signature and review are independent.

## Quick reference

`git verify-commit` / `git verify-tag` / trust

## References

- <https://git-scm.com/docs/git-verify-commit>
- <https://git-scm.com/docs/git-verify-tag>
- <https://git-scm.com/docs/git-config>
- <https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification>
