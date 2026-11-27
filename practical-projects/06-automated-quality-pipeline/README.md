# Automated Quality Pipeline

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../05-open-source-contribution/README.md) · [Index](../README.md) · [Next](../07-release-management/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 60 min

**Prerequisites:** [ci-cd/10-integrated-quality-pipeline-lab](../../ci-cd/10-integrated-quality-pipeline-lab/README.md) · Git 2.40+ · Bash/Git Bash · cmp

**Objective:** Commit a failing baseline, show that an unstaged fix cannot pass the committed-state gate, commit the fix on a feature branch, check its patch and integrate only after the exact revision passes. Test rejection of empty and extra-line snapshots.

## Scenario

A fictional catalog must contain exactly one line, status: ready. A tiny deterministic local quality gate checks the committed snapshot, not a dirty working file. It is a model of a CI gate, not a deployed CI service.

## Disposable setup

Use only the Disposable setup section of [My First Repository](../01-my-first-repository/README.md). Start a fresh dedicated Bash/Git Bash shell; verify printed sandbox root, fictional identities and no remotes before proceeding. Do not run project 01's challenge. Git 2.40+. Run one command at a time, stop on any unexpected failure and never run these commands in the guide.

## Challenge

Commit a failing baseline, show that an unstaged fix cannot pass the committed-state gate, commit the fix on a feature branch, check its patch and integrate only after the exact revision passes. Test rejection of empty and extra-line snapshots. Try before reading the solution.

## Progressive hints

Use git show REV:catalog.txt and compare bytes with cmp; shell command substitution alone strips trailing newlines. git diff --check detects introduced formatting problems but is not a complete test.

## Reference solution

Prepare the baseline and a local gate. The gate reports failure if the committed file cannot be read or differs byte-for-byte from the expected line. The two files used for comparison stay outside the checkout.

```bash
printf '%s\n' 'status: ready' > "$sandbox/expected.txt"
check_revision() {
  git show "$1:catalog.txt" > "$sandbox/actual.txt" &&
    cmp -s "$sandbox/expected.txt" "$sandbox/actual.txt"
}
printf '%s\n' 'status: draft' > catalog.txt
git add catalog.txt
git commit -m 'docs: initialize catalog'
git switch -c feat/ready-catalog
if check_revision HEAD; then echo 'UNEXPECTED PASS'; else echo 'RED'; fi
printf '%s\n' 'status: ready' > catalog.txt
if check_revision HEAD; then echo 'UNEXPECTED PASS'; else echo 'RED: unstaged fix'; fi
git add catalog.txt
git diff --cached --check
git commit -m 'feat: mark catalog ready'
check_revision HEAD
echo 'GREEN: committed snapshot'
```

Only continue if both red cases failed and the green check succeeded. Use a disposable negative-test branch to verify empty and extra-line committed states are rejected. Return to main and review the known-good branch; do not integrate the negative branch.

```bash
git switch -c test/invalid-catalog
: > catalog.txt
git add catalog.txt
git commit -m 'test: empty catalog'
if check_revision HEAD; then echo 'UNEXPECTED PASS'; else echo 'EMPTY REJECTED'; fi
printf '%s\n' 'status: ready' 'extra: invalid' > catalog.txt
git add catalog.txt
git commit -m 'test: extra catalog line'
if check_revision HEAD; then echo 'UNEXPECTED PASS'; else echo 'EXTRA REJECTED'; fi
git switch main
git diff --check main...feat/ready-catalog
git diff main...feat/ready-catalog
check_revision feat/ready-catalog
git merge --ff-only feat/ready-catalog
check_revision HEAD
git status --porcelain
```

## Success checks

Draft, dirty-only fix, empty and extra-line committed revisions fail; ready-only committed revision passes. Main points to the tested feature revision, not the negative-test branch. Clean status. Stop on any UNEXPECTED PASS. Optional: map this local gate to the earlier GitHub Actions or GitLab CI lesson, with no hosted execution required.

Fixed maintainer test (not learner code): `tests/test_git_practical_projects.py::test_quality_pipeline`.

## Recovery and cleanup

Inspect exact commit and gate output; don't weaken the assertion to obtain green. Keep failed candidates separate. Never enable deployment or privileged execution for this exercise. Close the dedicated shell and remove only the verified printed sandbox using a file manager. Preserve desired work first.

## Official sources

- <https://git-scm.com/docs/git-diff>
- <https://git-scm.com/docs/git-show>
- <https://git-scm.com/docs/git-commit>

---

<!-- navigation-footer -->
[Previous](../05-open-source-contribution/README.md) · [Index](../README.md) · [Next](../07-release-management/README.md)
<!-- /navigation-footer -->
