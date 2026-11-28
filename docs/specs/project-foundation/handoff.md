# Learning Hub handoff

[English](handoff.md) · [Português](handoff.pt-BR.md) · [Español](handoff.es.md)

This handoff separates the immutable content revision from the presentation revision and published release tag. The baseline below was integrated with explicit maintainer authorization in PR #21 and passed both main and manual CI. The handoff was reviewed and integrated in PR #22; v1.0.0 is published. This document does not activate a site lock.

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

The baseline contains 18 modules, 141 entries, 423 localized chapter paths, 54 localized index paths, 120 operations and 75 assessment records. Independent tree comparison covers 503 canonical paths (manifest, registry, indexes, chapters, resources, banks, catalog and schemas); all match the baseline by Git blob ID before final presentation review. At the baseline review, the same 152-test suite and nine validators passed per OS in main CI. The final presentation and release evidence is recorded below. No reciprocal changes to Python or the profile were made before Git publication.

- [PR #22](https://github.com/RamonRDR/git-study-guide/pull/22)
- [Visual identity V1](../../assets/learning-hub/README.md)
- [Audit](audit.md) · [Tasks](tasks.md)

## Sprint 19B closure: official release v1.0.0

The maintainer approved Visual Identity V1, the three rendered READMEs on desktop and mobile, external links and social preview; visual confirmation is maintainer-reported. PRs #22 and #23 passed exact-head CI, Codex Review and Final Pre-Merge Audit, were explicitly authorized and squash merged. Both post-merge main runs passed 156 tests and nine validators per OS; no error/warning markers observed. All 503 canonical paths remained unchanged. Stable latest v1.0.0 was published by the maintainer on 2026-11-28 at 17:41:35 UTC; the tag points directly to `706105ee5ef51befd2282a143e7deafd256c61a8`. Content pin `03c30438a5490d6c8f9b22dbf457a644658e042f`; presentation revision `c26c41fee624a74f7ba7a70ac531063061a6559e`. AC-19 and T19-01 fulfilled; this post-release documentation reconciles the historical in-progress records and does not modify the published tag. Limitations: sampled semantic review, no exhaustive learner lab execution or macOS CI, no verified browser runtime or site deployment, no observed superseded-run cancellation. Reciprocal links to Python and the profile are separate follow-up PRs.

- [Release v1.0.0](https://github.com/RamonRDR/git-study-guide/releases/tag/v1.0.0)
- [Final main CI](https://github.com/RamonRDR/git-study-guide/actions/runs/46170822488)
- [PR #22](https://github.com/RamonRDR/git-study-guide/pull/22) · [PR #23](https://github.com/RamonRDR/git-study-guide/pull/23)
