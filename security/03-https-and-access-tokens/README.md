# HTTPS and access tokens

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../02-ssh-authentication/README.md) · [Index](../README.md) · [Next](../04-credential-managers/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 35 min

**Prerequisites:** [Professional workflows](../../professional-workflows/README.md) · [SSH authentication and host identity](../02-ssh-authentication/README.md)

**Objective:** Choose appropriately scoped HTTPS credentials.

## What and why

HTTPS uses TLS to protect transport and authenticate the server through certificate validation. A personal access token (PAT) is a credential with provider-specific capabilities, resource scope and expiration; it is not an account password. GitHub no longer accepts account passwords for Git operations over HTTPS. Fine-grained GitHub tokens can restrict resources and permissions; classic tokens have broader scopes and may be needed for unsupported cases. GitLab offers different personal, project and group token types subject to settings and tiers. Prefer short-lived, scoped credentials or managed app identities when suitable. A token can still be misused within its granted permissions even when account 2FA is enabled.

## Practice

Design access for a fictional bot that reads one private catalog and never writes. Record required repository, read permission, expiration, owner and revocation path on paper. Use only `https://host.example.invalid/team/catalog.git` as a fictional URL; never insert a credential in it.

## Risks and recovery

Do not disable TLS verification, embed tokens in URLs, commands, files or screenshots, or broaden scope to fix an authentication failure. Check correct host, account, token expiration and policy privately. Revoke and replace any exposed token.

## Exercise and self-check

Read-only access to one repository, shortest practical lifetime and documented revocation; no real token needed.

## Quick reference

TLS / PAT / scope / expiration

## References

- <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens>
- <https://docs.gitlab.com/user/profile/personal_access_tokens/>
- <https://git-scm.com/docs/gitcredentials>
