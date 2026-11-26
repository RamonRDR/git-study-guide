# Software supply chain security

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../09-commit-and-tag-signing/README.md) · [Index](../README.md) · [Next](../11-credential-exposure-and-incident-response/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 45 min

**Prerequisites:** [Professional workflows](../../professional-workflows/README.md) · [Commit and tag signing](../09-commit-and-tag-signing/README.md)

**Objective:** Identify supply-chain controls and residual risks.

## What and why

The supply chain includes source, dependencies, build tools, CI actions, images, runners, registries and distributed artifacts. Dependency lockfiles record resolved versions; they do not prove safety. A software bill of materials (SBOM) inventories components; provenance describes where/how an artifact was built; an attestation is a verifiable statement about a subject. Verify trusted sources, review dependency changes, pin GitHub actions to verified full commit SHAs and images to verified digests where feasible, and periodically update through reviewed changes. Pinning does not remove vulnerabilities or guarantee transitive dependencies are safe. Use least privilege and isolated untrusted CI; do not deploy artifacts from untrusted jobs without a verified trust boundary.

[Quality automation](../../docs/quality-automation.md)

## Practice

Draw source -> reviewed build -> artifact -> verified promotion. In a fictional PR changing an action from a reviewed SHA to a floating tag, identify the mutable reference and request an independently verified revision. Add an inventory, expected checksum/provenance and update owner to the release checklist. Read the guide's quality workflow policy without modifying it.

## Risks and recovery

Do not execute unreviewed dependencies, privileged third-party CI or arbitrary artifacts. If a dependency is compromised, stop affected jobs/releases, follow incident response, verify replacement and rebuild from trusted inputs. Never claim a scan proves absence of vulnerabilities.

## Exercise and self-check

Pinned verified revisions, reviewed updates, isolated build, component inventory and provenance all reduce different risks. No single control guarantees trust.

## Quick reference

lockfile / SBOM / provenance / attestation

## References

- <https://docs.github.com/en/actions/reference/security/secure-use>
- <https://slsa.dev/spec/v1.0/>
- <https://www.cisa.gov/sbom>
