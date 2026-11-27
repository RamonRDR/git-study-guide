# Professional Engineering Workflow

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../07-release-management/README.md) · [Index](../README.md) · [Next module](../../exercises/README.md)
<!-- /navigation -->

**Level:** advanced · **Estimated time:** 90 min

**Prerequisites:** [professional-workflows/13-integrated-professional-workflow-lab](../../professional-workflows/13-integrated-professional-workflow-lab/README.md) · Git 2.40+ · Bash/Git Bash · cmp

**Objective:** Write a short spec and plan outside the checkout. Make two private feature commits, fail the baseline check, pass the feature check, record the exact reviewed SHA and review the diff. Role-play maintainer authorization and create a one-parent squash commit on main, verify tree equality, then tag the tested result.

## Scenario

A fictional notes service has requirement R1: change status from draft to ready, and AC1: the committed notes file is exactly status: ready. Existing draft is a baseline, not a public version contract. Simulate SDD, a red/green check, review, authorized local squash and release evidence.

## Disposable setup

Use only the Disposable setup section of [My First Repository](../01-my-first-repository/README.md). Start a fresh dedicated Bash/Git Bash shell; verify printed sandbox root, fictional identities and no remotes before proceeding. Do not run project 01's challenge. Git 2.40+. Run one command at a time, stop on any unexpected failure and never run these commands in the guide.

## Challenge

Write a short spec and plan outside the checkout. Make two private feature commits, fail the baseline check, pass the feature check, record the exact reviewed SHA and review the diff. Role-play maintainer authorization and create a one-parent squash commit on main, verify tree equality, then tag the tested result. Try before reading the solution.

## Progressive hints

Keep main unchanged until review; test committed content, not a mutable working file. Squash prepares changes without creating MERGE_HEAD or moving HEAD. Verify one parent and matching tree before tagging. This role-play is not actual independent approval.

## Reference solution

Write R1, AC1, scope, expected checks and rollback policy in a local notebook or a file outside the checkout. Establish the baseline and red/green test, then complete two scoped commits. Continue only if red and green behave as expected.

```bash
printf '%s\n' 'status: draft' > notes.txt
git add notes.txt
git commit -m 'docs: initialize notes'
base=$(git rev-parse HEAD)
printf '%s\n' 'status: ready' > "$sandbox/expected.txt"
check_revision() {
  git show "$1:notes.txt" > "$sandbox/actual.txt" &&
    cmp -s "$sandbox/expected.txt" "$sandbox/actual.txt"
}
git switch -c feat/ready-notes
if check_revision HEAD; then echo 'UNEXPECTED PASS'; else echo 'RED'; fi
printf '%s\n' 'status: ready' > notes.txt
git add notes.txt
git commit -m 'feat: mark notes ready'
printf '%s\n' 'R1: notes are ready' > review.txt
git add review.txt
git commit -m 'docs: record readiness requirement'
check_revision HEAD
git diff --check main...HEAD
git diff main...HEAD
reviewed=$(git rev-parse HEAD)
reviewed_tree=$(git rev-parse 'HEAD^{tree}')
```

Record review evidence and limitations outside the checkout. Role-play explicit authorization only after verifying the exact reviewed SHA and tests. Switch to main, verify it has not moved and the feature matches the reviewed ID. Perform local squash only in this disposable lab. Stop on any failed test.

```bash
git switch main
test "$(git rev-parse HEAD)" = "$base"
test "$(git rev-parse feat/ready-notes)" = "$reviewed"
test -z "$(git status --porcelain)"
git merge --squash feat/ready-notes
test "$(git rev-parse HEAD)" = "$base"
git diff --cached --check
git diff --cached
git commit -m 'feat: deliver reviewed notes'
test "$(git rev-parse HEAD^1)" = "$base"
test "$(git rev-parse 'HEAD^{tree}')" = "$reviewed_tree"
test "$(git rev-list --count HEAD)" = 2
check_revision HEAD
git tag -a v1.0.0 -m 'First reviewed notes release'
test "$(git rev-parse 'v1.0.0^{commit}')" = "$(git rev-parse HEAD)"
git status --porcelain
git remote
```

## Success checks

Review exact feature tip, two scoped feature commits, baseline unchanged until squash, main has exactly two commits including the original base, final single-parent commit tree equals reviewed feature tree, AC1 passes, tag resolves to final commit, no remote and clean status. Record evidence as a mock PR. This is not hosted CI, an actual review or a deployment.

Fixed maintainer test (not learner code): `tests/test_git_practical_projects.py::test_professional_workflow`.

## Recovery and cleanup

If squash conflicts, stop and inspect: no ordinary MERGE_HEAD is created, so do not assume merge --abort works. Preserve desired edits before choosing a safe cleanup or recreating the sandbox. After a shared bad commit, prefer a reviewed corrective commit/revert over rewriting history. Never perform this lab against the guide. Close the dedicated shell and remove only the verified printed sandbox using a file manager. Preserve desired work first.

## Official sources

- <https://git-scm.com/docs/git-branch>
- <https://git-scm.com/docs/git-diff>
- <https://git-scm.com/docs/git-merge>
- <https://git-scm.com/docs/git-tag>
- <https://git-scm.com/docs/git-revert>

---

<!-- navigation-footer -->
[Previous](../07-release-management/README.md) · [Index](../README.md) · [Next module](../../exercises/README.md)
<!-- /navigation-footer -->
