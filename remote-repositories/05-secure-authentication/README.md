# Secure authentication and hosting platforms

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../04-remote-branch-lifecycle/README.md) · [Index](../README.md) · [Next module](../../history-and-recovery/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 20 min

**Prerequisites:** [Remote branch lifecycle and pruning](../04-remote-branch-lifecycle/README.md)

**Objective:** Choose safe access methods without creating or exposing credentials.

## What and why

Authentication proves who can access a service; authorization controls what actions are allowed. Commit author identity is metadata, not authentication. HTTPS uses TLS to protect transport; providers may require tokens or browser-based sign-in rather than account passwords. SSH uses a private/public key pair; the private key stays private, and the service receives the public key. Verify server host keys against independently trusted official fingerprints before accepting; never disable host verification or TLS verification. A credential helper or manager can store/retrieve credentials; prefer OS-backed secure storage, not plaintext credential storage. Tokens should be scoped to the minimum repository/action, expire when practical, and be revoked if no longer needed.

## Practice

No online operation is required. In the completed local lab, no authentication to an external service was needed. For a hypothetical read-only clone, compare these fictional URL shapes (do not execute): `https://example.invalid/team/project.git` and `git@example.invalid:team/project.git`. HTTPS and SSH change how Git connects, not commit IDs, refs or merge semantics. Before optional future online practice, use the provider's official setup instructions and your own authorized disposable repository. Check fetch and push destinations privately, confirm host and permissions, then choose least privilege. Do not put tokens in URLs, command arguments, source files, screenshots or logs. Do not paste private keys or tokens into this guide or AI tools. Git implements clone/fetch/push; hosted pull requests, merge requests, required checks and branch protections are GitHub/GitLab features, covered later. A remote may reject an otherwise valid update because of server permissions or policy. A native Git bare repository can also apply hooks/policies, but it does not provide a hosted PR interface by itself.

## Common mistakes and safety

If authentication fails, verify URL, account, credential expiry and permissions through official documentation; do not increase access indiscriminately. If a credential leaks, revoke/rotate immediately and notify the appropriate owner; deleting a file or commit alone is insufficient. Do not print full configuration or credential contents for troubleshooting. No external authentication was tested in this module.

## Exercise and self-check

A teammate needs to read one repository. Should you share a broad token or private SSH key? Hint: identity and least privilege. Answer: neither; grant authorized individual access with minimal permissions. Pass if you explain authentication versus author metadata, HTTPS versus SSH, and why a PR is not a Git command.

## Quick reference

- `git remote get-url origin`
- `git remote get-url --push origin`
- `git help credentials`

## Official sources

- [Git: gitcredentials](https://git-scm.com/docs/gitcredentials)
- [Git: git-clone](https://git-scm.com/docs/git-clone)
- [Git: git-config](https://git-scm.com/docs/git-config)
- [GitHub: authentication](https://docs.github.com/en/authentication)
- [GitLab: SSH](https://docs.gitlab.com/user/ssh/)
- [GitLab: access tokens](https://docs.gitlab.com/user/profile/personal_access_tokens/)

---

<!-- navigation-footer -->
[Previous](../04-remote-branch-lifecycle/README.md) · [Index](../README.md) · [Next module](../../history-and-recovery/README.md)
<!-- /navigation-footer -->
