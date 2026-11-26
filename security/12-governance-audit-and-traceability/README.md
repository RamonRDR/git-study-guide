# Governance, audit and traceability

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../11-credential-exposure-and-incident-response/README.md) · [Index](../README.md) · [Next](../13-integrated-security-lab/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 40 min

**Prerequisites:** [Professional workflows](../../professional-workflows/README.md) · [Credential exposure and incident response](../11-credential-exposure-and-incident-response/README.md)

**Objective:** Record verifiable approval and audit evidence.

## What and why

Governance defines who may decide, perform and review actions; audit evidence records what actually happened. A commit history is useful but does not capture every hosting or administrative action. Audit logs, PR/MR records, workflow logs, artifact metadata and approval evidence complement it, subject to access and retention policies. Record exact head/base, tested merge revision, results and limitations, reviewer findings, authorization, integrated commit/tree, branch cleanup and post-merge checks. Separate policy design, effective enforcement and observed results. Do not invent evidence or preserve private information in public audit notes.

[Task register](../../docs/specs/project-foundation/tasks.md)

## Practice

Create a fictional audit register: requirement, PR identifier, reviewed SHA placeholder, Linux/Windows status, unresolved findings, human decision, merge tree comparison and residual risk. Suppose Windows is pending: mark the gate pending, not passed. Compare against the guide's contribution and task policies.

## Risks and recovery

Do not conflate review request with approval, or audit log availability with completeness. Restrict sensitive evidence to authorized retention and channels. Never alter rules or merge on assumed approval; record gaps and escalate.

## Exercise and self-check

Windows pending blocks the gate; authorization and observed results must refer to the exact revision. Record limitations honestly.

## Quick reference

revision / evidence / decision / residual risk

## References

- <https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/reviewing-the-audit-log-for-your-organization>
- <https://docs.gitlab.com/user/compliance/audit_events/>
