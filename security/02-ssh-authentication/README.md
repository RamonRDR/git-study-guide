# SSH authentication and host identity

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../01-security-foundations/README.md) · [Index](../README.md) · [Next](../03-https-and-access-tokens/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 40 min

**Prerequisites:** [Professional workflows](../../professional-workflows/README.md) · [Git security foundations](../01-security-foundations/README.md)

**Objective:** Explain key pairs and safe host verification.

## What and why

SSH uses a cryptographic key pair: the public key may be registered with the provider, while the private key stays under the user's control. The server also has a host key, whose fingerprint must be verified through a trusted independent source on first connection or unexpected change. A passphrase protects a private key at rest; an agent may hold unlocked keys temporarily. Authentication by SSH does not automatically grant write permission or sign Git commits. `ssh -T git@github.com` is an optional host-specific authentication check after setup; GitHub does not provide an interactive shell and its documented successful authentication may return a nonzero exit status. Use official provider instructions for key generation, supported algorithms, registration and revocation.

## Practice

Offline: label the public key, private key, passphrase and server fingerprint in a fictional connection diagram. Compare `git@host.example.invalid:team/catalog.git` with an HTTPS URL. If the fingerprint changes unexpectedly, write the next safe action. No key generation or network access is required.

## Risks and recovery

Never paste private keys or disable host verification. Do not blindly remove a known-host entry to silence a warning. Verify independently, investigate changes, and revoke an exposed key at each provider where it was authorized.

## Exercise and self-check

Public key can be registered; private key and passphrase stay private; stop on an unexpected fingerprint and verify it independently.

## Quick reference

public key / private key / host fingerprint / agent

## References

- <https://docs.github.com/en/authentication/connecting-to-github-with-ssh>
- <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection>
- <https://docs.gitlab.com/user/ssh/>
