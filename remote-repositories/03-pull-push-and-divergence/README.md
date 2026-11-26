# Pull, push and divergent histories

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../02-fetch-and-tracking/README.md) · [Index](../README.md) · [Next](../04-remote-branch-lifecycle/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 35 min

**Prerequisites:** [Fetch, references and upstream tracking](../02-fetch-and-tracking/README.md)

**Objective:** Reproduce and safely resolve non-fast-forward rejection.

## What and why

Pull fetches then integrates into the current branch. Explicit `git pull --ff-only origin main` refuses divergent history, although fetch can still update tracking refs. `git pull --no-rebase origin main` chooses merge (may create a two-parent commit); `git pull --rebase origin main` reapplies local commits on the fetched base, normally changing their IDs. Defaults vary with Git version/configuration, so choose explicitly. Push normally refuses a branch update that would discard remote ancestry. A rejection protects shared work, not a problem to bypass.

## Practice

Continue with both clones synchronized on main. Repeat all safety and identity checks from chapter 02 for each actor before operations; inspect each staged diff before committing. Create alice/plan.txt with `shared plan` and bob/bob.txt with `bob update`, each with final newline. First publish Alice, then commit Bob and attempt his push.
```text
git -C alice add -- plan.txt
git -C alice diff --cached
git -C alice commit -m "docs: add plan"
git -C alice push origin main
git -C bob add -- bob.txt
git -C bob diff --cached
git -C bob commit -m "docs: add Bob note"
```

Now deliberately attempt this single push; failure is expected:

```text
git -C bob push origin main
```
Expected: the LAST push fails (non-fast-forward, sometimes described as fetch first). Stop on any earlier failure. Verify origin main still equals Alice's tip, Bob's commit is retained. Then:
```text
git -C bob fetch origin
git -C bob rev-list --left-right --count main...origin/main
git -C bob log --all --graph --oneline --decorate
git -C bob diff main origin/main
```

Verify the divergence, then deliberately attempt the following; failure is expected:

```text
git -C bob pull --ff-only origin main
```
Expected: count 1 1; last pull refuses. Diagram: C2 -> A3 (origin/main); C2 -> B3 (Bob main). Both have unique commits. Verify Bob HEAD is still B3 and status clean. Merge explicitly using the already inspected ref; no conflict is expected because files differ.
```text
git -C bob merge --no-edit origin/main
git -C bob show HEAD:plan.txt
git -C bob show HEAD:bob.txt
git -C bob status --short
git -C bob push origin main
git -C alice pull --ff-only origin main
git -C alice rev-parse HEAD origin/main
git -C bob rev-parse HEAD origin/main
git -C origin.git rev-parse refs/heads/main
```
Expected: merge commit M has parents B3 and A3; both files survive, all main tips equal M, status clean. In a team, choose merge or rebase according to policy. For an unpublished local commit only, rebase after fetch and a backup ref is an alternative; see module 05. Do not execute both strategies in this lab.

## Common mistakes and safety

Do not force push or reset to silence rejection. If an unexpected merge conflict occurs, inspect status and use merge --abort or resolve as in module 05. If rebase is chosen elsewhere, use rebase --abort/--continue. A completed push cannot be recalled by abort; coordinate recovery with collaborators.

## Exercise and self-check

Does a refused ff-only pull imply nothing changed? Hint: fetch phase. Answer: local main stays put, tracking refs may update. Pass if both unique commits are ancestors of final main and both files exist.

## Quick reference

- `git pull --ff-only`
- `git pull --no-rebase`
- `git pull --rebase`
- `git push origin main`

## Official sources

- [Git: git-pull](https://git-scm.com/docs/git-pull)
- [Git: git-push](https://git-scm.com/docs/git-push)
- [Git: git-merge](https://git-scm.com/docs/git-merge)
- [Git: git-rebase](https://git-scm.com/docs/git-rebase)

---

<!-- navigation-footer -->
[Previous](../02-fetch-and-tracking/README.md) · [Index](../README.md) · [Next](../04-remote-branch-lifecycle/README.md)
<!-- /navigation-footer -->
