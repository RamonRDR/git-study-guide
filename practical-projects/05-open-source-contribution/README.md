# Open Source Contribution

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../04-the-lost-commit/README.md) · [Index](../README.md) · [Next](../06-automated-quality-pipeline/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 60 min

**Prerequisites:** [github/05-forks-and-open-source](../../github/05-forks-and-open-source/README.md) · Git 2.40+ · Bash/Git Bash

**Objective:** Prepare an independent fork, make a scoped documentation change on a feature branch, review its diff from upstream/main, publish to the fork only, then role-play the maintainer who fetches and integrates the reviewed branch into upstream.

## Scenario

A fictional open-source project has an upstream and a contributor's fork. Local bare repositories simulate the hosting relationship without accounts.

## Disposable setup

Use only the Disposable setup section of [My First Repository](../01-my-first-repository/README.md). Start a fresh dedicated Bash/Git Bash shell; verify printed sandbox root, fictional identities and no remotes before proceeding. Do not run project 01's challenge. Git 2.40+. Run one command at a time, stop on any unexpected failure and never run these commands in the guide.

## Challenge

Prepare an independent fork, make a scoped documentation change on a feature branch, review its diff from upstream/main, publish to the fork only, then role-play the maintainer who fetches and integrates the reviewed branch into upstream. Try before reading the solution.

## Progressive hints

Clone a bare origin to another bare repository, then clone the fork normally. Use distinct origin and upstream remote names. A local fetch and merge are not a real pull request or an independent human approval.

## Reference solution

Seed the upstream and create the local fork. In the contributor clone, verify the remotes and configure the fictional identity.

```bash
printf '%s\n' 'status: draft' > notes.txt
git add notes.txt
git commit -m 'docs: initialize notes'
git init --bare -b main "$sandbox/upstream.git"
git remote add origin "$sandbox/upstream.git"
git push -u origin main
git clone --bare "$sandbox/upstream.git" "$sandbox/fork.git"
git clone "$sandbox/fork.git" "$sandbox/contributor"
cd "$sandbox/contributor"
git config user.name 'Study Guide Example'
git config user.email learner@example.invalid
git config commit.gpgsign false
git config core.autocrlf false
git config core.hooksPath "$sandbox/no-hooks"
git remote add upstream "$sandbox/upstream.git"
git remote -v
git fetch upstream
git switch -c feat/clarify-notes
printf '%s\n' 'status: ready' > notes.txt
git add notes.txt
git commit -m 'docs: clarify notes'
git diff --check upstream/main...HEAD
git diff upstream/main...HEAD
git push -u origin feat/clarify-notes
```

Write a mock review describing the change, evidence and limitations. Switch roles to the original clone; verify upstream is unchanged and inspect the contribution. In this offline exercise, explicitly choose fast-forward after review; do not confuse it with a hosting PR merge.

```bash
cd "$sandbox/repo"
git fetch origin
test "$(git rev-parse HEAD)" = "$(git rev-parse origin/main)"
git remote add contribution "$sandbox/fork.git"
git fetch contribution
git diff --check main...contribution/feat/clarify-notes
git diff main...contribution/feat/clarify-notes
git merge --ff-only contribution/feat/clarify-notes
git push origin main
git show HEAD:notes.txt
git status --porcelain
```

## Success checks

The fork feature branch contains ready notes and the fork main remains at the draft baseline. Upstream main advances only in the maintainer phase and matches the reviewed contribution. Optional: inspect the real GitHub/GitLab contribution workflow in earlier modules; only use owned authorized test projects, never submit an unwanted PR.

Fixed maintainer test (not learner code): `tests/test_git_practical_projects.py::test_contribution_offline`.

## Recovery and cleanup

If a destination differs from the expected local path, stop before pushing. If review or fast-forward fails, inspect changes without forcing. Keep the contribution branch until its work is verified. Close the dedicated shell and remove only the verified printed sandbox using a file manager. Preserve desired work first.

## Official sources

- <https://git-scm.com/docs/git-clone>
- <https://git-scm.com/docs/git-remote>
- <https://git-scm.com/docs/git-fetch>
- <https://git-scm.com/docs/git-diff>
- <https://git-scm.com/docs/git-merge>

---

<!-- navigation-footer -->
[Previous](../04-the-lost-commit/README.md) · [Index](../README.md) · [Next](../06-automated-quality-pipeline/README.md)
<!-- /navigation-footer -->
