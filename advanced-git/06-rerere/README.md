# Rerere: reuse conflict resolutions

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../05-hooks/README.md) · [Index](../README.md) · [Next](../07-sparse-checkout/README.md)
<!-- /navigation -->

**Level:** advanced · **Estimated time:** 45 min

**Prerequisites:** [13 Advanced Git](../README.md) · [Security & Governance](../../security/README.md)

**Objective:** Rerere records a conflicted preimage and a resolved postimage so Git may apply a matching resolution later.

## What and why

Rerere records a conflicted preimage and a resolved postimage so Git may apply a matching resolution later. It does not prove that the old resolution still matches current business intent. With rerere.autoupdate=false, inspect the working file and explicitly stage it. Teams can reduce repeated conflict work during long-lived integration.

## Practice

Create a fresh isolated fixture using the module index before each practice. Run one command at a time; stop on unexpected results. Check the printed sandbox and repository root before any changes. Use Git 2.34+ as the practice baseline; check command help and skip unavailable optional features. No commands on production repositories.

Use two branches from the fixture's current HEAD. Create conflicting changes to the same line. First merge must conflict; resolve with chosen text, run rerere and commit. Inspect status and history. This records a resolution; do not assume any future auto-resolution is correct. If stopping in a conflict, use merge --abort in the lab.

The second merge is expected to report an unresolved conflict, but rerere should have restored `reviewed` in the working file. Because automatic staging is disabled, `git ls-files -u` still shows unmerged entries. Inspect the content; abort this repeated merge after the check. If either merge unexpectedly succeeds or the content differs, stop and recreate the fixture.

```bash
git config --local rerere.enabled true
git config --local rerere.autoupdate false
git switch -c side
printf '%s\n' 'side' > src/state.txt
git add -- src/state.txt
git commit -m "docs: side state"
git switch main
printf '%s\n' 'main' > src/state.txt
git add -- src/state.txt
git commit -m "docs: main state"
before=$(git rev-parse HEAD)
git merge side
git rerere status
printf '%s\n' 'reviewed' > src/state.txt
git rerere
git add -- src/state.txt
git commit -m "merge: reviewed resolution"
git switch -c repeat "$before"
git merge side
git ls-files -u -- src/state.txt
git diff -- src/state.txt
test "$(cat src/state.txt)" = reviewed
git merge --abort
git status --short
```

## Common mistakes and safety

Use only the disposable fixture and fictional data. If state differs, stop; inspect status and the relevant operation before aborting or recreating the fixture. Close the dedicated shell and remove only the recorded sandbox through the file manager after reviewing its contents.

## Exercise and self-check

Does rerere replace code review? No; verify resulting content and tests before staging.

## Quick reference

- `git config --local rerere.enabled true`
- `git config --local rerere.autoupdate false`
- `git switch -c side`
- `git add -- src/state.txt`

## Official sources

- [https://git-scm.com/docs/git-rerere](https://git-scm.com/docs/git-rerere)
- [https://git-scm.com/docs/git-merge](https://git-scm.com/docs/git-merge)

---

<!-- navigation-footer -->
[Previous](../05-hooks/README.md) · [Index](../README.md) · [Next](../07-sparse-checkout/README.md)
<!-- /navigation-footer -->
