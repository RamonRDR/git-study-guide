# Credential exposure and incident response

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../10-software-supply-chain/README.md) · [Index](../README.md) · [Next](../12-governance-audit-and-traceability/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 45 min

**Prerequisites:** [Professional workflows](../../professional-workflows/README.md) · [Software supply chain security](../10-software-supply-chain/README.md)

**Objective:** Prioritize containment and coordinated remediation.

## What and why

Treat a suspected exposed credential as compromised until assessed. First contain: revoke or rotate at the issuer promptly, stop affected automation and notify authorized responders privately. Preserve safe evidence (revision, time range, affected system, not the secret itself) and assess scope: history, clones, forks, caches, logs, artifacts and access records. Restore service with narrowly scoped replacement credentials through approved channels. Removing a file or reverting a commit does not revoke a credential or erase reachable history. History cleanup may require coordinated rewriting, changed object IDs, lost signatures, collaborator cleanup and host support; cannot guarantee removal from all copies. Follow authorized incident procedures before any destructive cleanup.

[Security policy](../../SECURITY.md)

## Practice

Tabletop only: a fictional catalog deployment credential appears in a public commit. No credential value is provided. Order containment, notification, investigation, replacement, cleanup decision and lessons learned. Draft a private report with affected component, revision placeholder, risk and proposed mitigation; never put sensitive details in a public issue. Consult the guide's security policy.

## Risks and recovery

Never test whether another person's exposed credential works. Do not paste it into chat or scanners, or force-push history as first response. If no verified private reporting route exists, establish one without disclosing details publicly.

## Exercise and self-check

Revoke/rotate and contain first; investigate and coordinate cleanup afterward. Recovery does not guarantee all copies disappear.

## Quick reference

revoke / rotate / contain / investigate

## References

- <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository>
- <https://csrc.nist.gov/pubs/sp/800/61/r3/final>

---

<!-- navigation-footer -->
[Previous](../10-software-supply-chain/README.md) · [Index](../README.md) · [Next](../12-governance-audit-and-traceability/README.md)
<!-- /navigation-footer -->
