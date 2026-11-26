# Archive and bundle: distribute snapshots or history

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../09-blame-and-grep/README.md) · [Index](../README.md) · [Next](../11-integrated-advanced-lab/README.md)
<!-- /navigation -->

**Level:** advanced · **Estimated time:** 40 min

**Prerequisites:** [13 Advanced Git](../README.md) · [Security & Governance](../../security/README.md)

**Objective:** Archive exports a selected tree (subject to attributes) without the repository history; bundle packages refs and Git objects and can serve as an offline transfer source.

## What and why

Archive exports a selected tree (subject to attributes) without the repository history; bundle packages refs and Git objects and can serve as an offline transfer source. Bundles may be incremental and require prerequisites. Neither is a full backup of untracked files, all local settings or secrets; review distribution permissions.

## Practice

Create a fresh isolated fixture using the module index before each practice. Run one command at a time; stop on unexpected results. Check the printed sandbox and repository root before any changes. Use Git 2.34+ as the practice baseline; check command help and skip unavailable optional features. No commands on production repositories.

Write both outputs outside the repo in the fresh sandbox. Verify bundle, clone it into another owned folder, compare HEAD and inspect the archive file list with unzip if available. Do not publish either artifact automatically; a bundle can include historical sensitive data.

```bash
git archive --format=zip -o "$sandbox/snapshot.zip" HEAD
git bundle create "$sandbox/history.bundle" main
git bundle verify "$sandbox/history.bundle"
git clone -b main "$sandbox/history.bundle" "$sandbox/recovered"
test "$(git rev-parse HEAD)" = "$(git -C "$sandbox/recovered" rev-parse HEAD)"
```

## Common mistakes and safety

Use only the disposable fixture and fictional data. If state differs, stop; inspect status and the relevant operation before aborting or recreating the fixture. Close the dedicated shell and remove only the recorded sandbox through the file manager after reviewing its contents.

## Exercise and self-check

Which output allows a Git clone of the chosen branch? A complete bundle, not the zip archive.

## Quick reference

- `git archive --format=zip -o "$sandbox/snapshot.zip" HEAD`
- `git bundle create "$sandbox/history.bundle" main`
- `git bundle verify "$sandbox/history.bundle"`
- `git clone -b main "$sandbox/history.bundle" "$sandbox/recovered"`

## Official sources

- [https://git-scm.com/docs/git-archive](https://git-scm.com/docs/git-archive)
- [https://git-scm.com/docs/git-bundle](https://git-scm.com/docs/git-bundle)

---

<!-- navigation-footer -->
[Previous](../09-blame-and-grep/README.md) · [Index](../README.md) · [Next](../11-integrated-advanced-lab/README.md)
<!-- /navigation-footer -->
