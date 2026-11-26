# Credential managers and configuration scope

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../03-https-and-access-tokens/README.md) · [Index](../README.md) · [Next](../05-secrets-and-disclosure-prevention/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 35 min

**Prerequisites:** [Professional workflows](../../professional-workflows/README.md) · [HTTPS and access tokens](../03-https-and-access-tokens/README.md)

**Objective:** Distinguish helper storage and revocation.

## What and why

Git credential helpers retrieve and store credentials for HTTPS operations; Git Credential Manager can use provider authentication and appropriate OS-backed storage depending on configuration. The `cache` helper keeps credentials temporarily in memory; `store` saves them in plaintext on disk and is unsuitable for sensitive long-lived credentials. System, global and repository-local Git configuration have different scopes; multiple helper entries can be active. `git config --show-origin --get-all credential.helper` is a read-only diagnostic but may reveal custom command text or sensitive paths. Inspect locally, never share raw output. SSH agents and HTTPS helpers are different mechanisms.

## Practice

Offline: compare memory cache, plaintext storage and an approved OS-backed manager. Given a stale saved credential for a fictional account, outline a safe removal and reauthentication through the provider's documented manager UI. Distinguish forgetting a local credential from revoking it remotely.

## Risks and recovery

Do not run credential retrieval commands to print passwords or tokens. Do not change global helper settings for this exercise. Use the supported erase/sign-out flow for the intended account and host; revoke compromised credentials at the issuer too.

## Exercise and self-check

Prefer approved protected storage; local removal does not revoke the issuer's credential. No actual credentials are required.

## Quick reference

helper / cache / store / credential manager

## References

- <https://git-scm.com/docs/gitcredentials>
- <https://git-scm.com/docs/git-credential-store>
- <https://git-scm.com/docs/git-credential-cache>
- <https://github.com/git-ecosystem/git-credential-manager>

---

<!-- navigation-footer -->
[Previous](../03-https-and-access-tokens/README.md) · [Index](../README.md) · [Next](../05-secrets-and-disclosure-prevention/README.md)
<!-- /navigation-footer -->
