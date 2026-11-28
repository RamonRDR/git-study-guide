# Learning Hub handoff

[English](handoff.md) · [Português](handoff.pt-BR.md) · [Español](handoff.es.md)

This handoff separates the immutable content revision from the presentation revision and future release tag. The baseline below was integrated with explicit maintainer authorization in PR #21 and passed both main and manual CI. This document remains a release candidate until PR #22 is reviewed and integrated; it does not activate a site lock or publish a release.

## Content and provenance

- [Content revision 03c30438a5490d6c8f9b22dbf457a644658e042f](https://github.com/RamonRDR/git-study-guide/commit/03c30438a5490d6c8f9b22dbf457a644658e042f)
- [Main CI](https://github.com/RamonRDR/git-study-guide/actions/runs/46061260750) · [Manual CI](https://github.com/RamonRDR/git-study-guide/actions/runs/46062482507)
- [Manifest](../../../curriculum/manifest.json) · [Contract](integration-contract.md) · [Reference consumer](../../../scripts/learning_hub_consumer.py)
- [ADR 0006](../../adr/0006-browser-playground.md)

```json
{
  "guide_id": "git-study-guide",
  "revision": "03c30438a5490d6c8f9b22dbf457a644658e042f",
  "manifest_version": "1.0.0",
  "assessment_version": 1,
  "command_catalog_version": 1
}
```

The reference consumer takes an external lock and a trusted full-object SHA-1 Git repository. Use the supported exact versions, never execute snapshot code, and validate before adoption; retain the previous approved pin on failure. The Git adapter is distinct from the Python adapter. Read the integration contract and browser-playground ADR. Native projects and challenges are local_only, other chapters unverified; no browser runtime or site deployment is claimed.

## Validation and release

The baseline contains 18 modules, 141 entries, 423 localized chapter paths, 54 localized index paths, 120 operations and 75 assessment records. Independent tree comparison covers 503 canonical paths (manifest, registry, indexes, chapters, resources, banks, catalog and schemas); all match the baseline by Git blob ID before final presentation review. The same 152-test suite and nine validators passed per OS in main CI. Final presentation CI and Codex Review must pass; visual rendering, explicit squash approval, post-merge CI and a separate release authorization remain required. No reciprocal changes to Python or the profile before Git publication.

- [PR #22](https://github.com/RamonRDR/git-study-guide/pull/22)
- [Visual identity V1](../../assets/learning-hub/README.md)
- [Audit](audit.md) · [Tasks](tasks.md)
