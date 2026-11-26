# Remote branch lifecycle and pruning

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../03-pull-push-and-divergence/README.md) · [Index](../README.md) · [Next](../05-secure-authentication/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 30 min

**Prerequisites:** [Pull, push and divergent histories](../03-pull-push-and-divergence/README.md)

**Objective:** Publish, track, integrate and remove a disposable remote branch while retaining work.

## What and why

`git push -u origin BRANCH` publishes and sets upstream on successful or already-current push. `git switch --track origin/BRANCH` creates a local branch tracking the named remote-tracking ref. `git push --delete origin BRANCH` removes a remote branch ref, not necessarily the underlying objects; collaborators can retain stale tracking refs until fetch --prune. Prune uses the fetch refspec and does not remove ordinary local branches with the default clone mapping. Nonstandard refspecs can prune other refs, including tags; inspect configuration.

## Practice

Continue chapter 03 with synchronized clean clones in the recorded parent. Repeat chapter 02 checks for each actor before changes. After switching Alice to feat/summary, create alice/summary.txt with `summary ready` and final newline; inspect staged diff and both identities before commit. Run the following in order, pausing at switch before creating the file.
```text
git -C alice switch -c feat/summary
git -C alice add -- summary.txt
git -C alice diff --cached
git -C alice commit -m "docs: add summary"
git -C alice push -u origin feat/summary
git -C alice branch -vv
git -C bob fetch origin
git -C bob switch --track origin/feat/summary
git -C bob branch -vv
git -C bob switch main
git -C alice switch main
git -C alice merge --ff-only feat/summary
git -C alice push origin main
git -C bob pull --ff-only origin main
```
Expected: Bob's local branch tracks origin/feat/summary; main now contains summary commit in both clones. For deletion, first confirm all collaborators agree (Alice and Bob in this isolated lab), no additional work exists on feature, and remote feature is an ancestor of remote main. Run first four inspection commands below separately; ancestry must exit 0 and both refs returned by ls-remote must match the fetched refs. Only then delete feat/summary, never main. No concurrent actor may change these refs during this exercise; in real teams recheck and use hosting protection and agreed workflow.
```text
git -C alice fetch origin
git -C alice merge-base --is-ancestor origin/feat/summary origin/main
git -C alice ls-remote --heads origin refs/heads/main refs/heads/feat/summary
git -C alice rev-parse origin/main origin/feat/summary
```

Stop here unless the ancestry and both IDs match the checks above. With the verified local origin and only the agreed disposable branch, run:

```text
git -C alice push --delete origin feat/summary
git -C bob ls-remote --heads origin refs/heads/feat/summary
git -C bob branch -r
git -C bob fetch --prune origin
git -C bob branch -r
git -C bob branch -vv
git -C bob branch -d feat/summary
git -C alice branch -d feat/summary
git -C alice rev-parse main
git -C bob rev-parse main
git -C origin.git rev-parse refs/heads/main
git -C bob show HEAD:summary.txt
git -C bob status --short
git -C alice status --short
```
Expected: remote branch absent after deletion; Bob's cached origin/feat/summary can still exist before prune and disappears after. His local branch remains until -d; both local main tips equal origin main and summary ready survives. Local deletion may refuse if unmerged; stop rather than forcing. Professional use: clean integrated branches after review, not before. Verify no remaining work is needed. Close editors and dedicated shell; delete only the exact recorded temporary parent via file manager, never the guide, home or work repo.

## Common mistakes and safety

Remote deletion can disrupt collaborators or remove the last named reference to work. Ancestry verification is valid for this fast-forward/merge lab; squash integration may require separate content and review evidence. Prune is not a server deletion. Recovery requires an available commit and authorization to republish; not guaranteed.

## Exercise and self-check

After deleting remote feature, why can Bob still see it? Hint: cached ref. Answer: fetch --prune removes obsolete tracking ref, not Bob's local branch. Pass if remote and cached feature are absent after prune, main retains summary and status is clean.

## Quick reference

- `git push -u origin feat/summary`
- `git switch --track origin/feat/summary`
- `git push --delete origin feat/summary`
- `git fetch --prune origin`

## Official sources

- [Git: git-push](https://git-scm.com/docs/git-push)
- [Git: git-fetch](https://git-scm.com/docs/git-fetch)
- [Git: git-switch](https://git-scm.com/docs/git-switch)
- [Git: git-branch](https://git-scm.com/docs/git-branch)
- [Git: git-ls-remote](https://git-scm.com/docs/git-ls-remote)
- [Git: git-merge-base](https://git-scm.com/docs/git-merge-base)

---

<!-- navigation-footer -->
[Previous](../03-pull-push-and-divergence/README.md) · [Index](../README.md) · [Next](../05-secure-authentication/README.md)
<!-- /navigation-footer -->
