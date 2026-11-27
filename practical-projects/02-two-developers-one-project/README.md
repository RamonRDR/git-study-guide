# Two Developers, One Project

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../01-my-first-repository/README.md) · [Index](../README.md) · [Next](../03-merge-conflict-laboratory/README.md)
<!-- /navigation -->

**Level:** beginner · **Estimated time:** 60 min

**Prerequisites:** [remote-repositories/02-fetch-and-tracking](../../remote-repositories/02-fetch-and-tracking/README.md) · Git 2.40+ · Bash/Git Bash

**Objective:** Create a shared baseline, clone as Alice and Bob, publish Alice's change, fetch from Bob without changing his checkout, then integrate and publish Bob's separate file. Verify both developers converge.

## Scenario

Alice and Bob maintain fictional notes through a local bare origin. Alice publishes a change while Bob works independently.

## Disposable setup

Use only the Disposable setup section of [My First Repository](../01-my-first-repository/README.md). Start a fresh dedicated Bash/Git Bash shell; verify printed sandbox root, fictional identities and no remotes before proceeding. Do not run project 01's challenge. Git 2.40+. Run one command at a time, stop on any unexpected failure and never run these commands in the guide.

## Challenge

Create a shared baseline, clone as Alice and Bob, publish Alice's change, fetch from Bob without changing his checkout, then integrate and publish Bob's separate file. Verify both developers converge. Try before reading the solution.

## Progressive hints

Use a bare repository as origin. Fetch updates tracking refs, not the checked-out branch. Integrate on clean main before creating Bob's commit.

## Reference solution

Create the initial revision and publish it locally. Clone twice; configure each clone before committing.

```bash
printf '%s\n' 'shared: draft' > notes.txt
git add notes.txt
git commit -m 'docs: initialize shared notes'
git init --bare -b main "$sandbox/origin.git"
git remote add origin "$sandbox/origin.git"
git push -u origin main
git clone "$sandbox/origin.git" "$sandbox/alice"
git clone "$sandbox/origin.git" "$sandbox/bob"
for who in alice bob; do
  git -C "$sandbox/$who" config user.name 'Study Guide Example'
  git -C "$sandbox/$who" config user.email learner@example.invalid
  git -C "$sandbox/$who" config commit.gpgsign false
  git -C "$sandbox/$who" config core.autocrlf false
  git -C "$sandbox/$who" config core.hooksPath "$sandbox/no-hooks"
done
```

Publish Alice's update; Bob records his old HEAD and fetches. Inspect the distinct refs before merging.

```bash
printf '%s\n' 'shared: ready' > "$sandbox/alice/notes.txt"
git -C "$sandbox/alice" add notes.txt
git -C "$sandbox/alice" commit -m 'docs: prepare shared notes'
git -C "$sandbox/alice" push origin main
cd "$sandbox/bob"
before=$(git rev-parse HEAD)
git fetch origin
test "$(git rev-parse HEAD)" = "$before"
test "$(git rev-parse origin/main)" != "$before"
git merge --ff-only origin/main
printf '%s\n' 'review: done' > review.txt
git add review.txt
git commit -m 'docs: record review'
git push origin main
git -C "$sandbox/alice" pull --ff-only origin main
test "$(git -C "$sandbox/alice" rev-parse HEAD)" = "$(git rev-parse HEAD)"
git status --porcelain
```

## Success checks

Bob's HEAD stays unchanged after fetch; after integration both clones and bare main have the same tip, containing ready notes and review.txt. Both clones are clean. Explain fetch versus pull.

Fixed maintainer test (not learner code): `tests/test_git_practical_projects.py::test_two_developers_sync`.

## Recovery and cleanup

On rejection, inspect fetched refs and divergence. Never force push to overcome it. Check all three local repositories before deleting the sandbox. Close the dedicated shell and remove only the verified printed sandbox using a file manager. Preserve desired work first.

## Official sources

- <https://git-scm.com/docs/git-clone>
- <https://git-scm.com/docs/git-fetch>
- <https://git-scm.com/docs/git-push>
- <https://git-scm.com/docs/git-merge>

---

<!-- navigation-footer -->
[Previous](../01-my-first-repository/README.md) · [Index](../README.md) · [Next](../03-merge-conflict-laboratory/README.md)
<!-- /navigation-footer -->
