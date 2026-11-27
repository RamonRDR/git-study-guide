# Quizzes

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous module](../../practical-projects/README.md) · [Index](../README.md) · [Next](../02-challenges/README.md)
<!-- /navigation -->

Try first, consult the public solutions afterward. Quizzes use exact choices; interviews and mocks require honest self-assessment. Challenges use only fresh disposable local repositories and fixed state checks, not automatic execution of learner commands. All records form an internal pilot, not the final Learning Hub contract.

## Commit snapshot

ID: quiz-snapshot

**Difficulty:** easy

**Prerequisites:** [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.md)

Stage A, edit to B without staging, then commit normally. Which version is recorded?

- a. A
- b. B
- c. Both

**Hints:**

- Consult the prerequisite before deciding.
- Compare index and working file.

**Answer:** a

**Explanation:** The index contains A; B stays unstaged.

## Stage a file

ID: quiz-add

**Difficulty:** easy

**Prerequisites:** [basic-commands/02-status-add-commit](../../basic-commands/02-status-add-commit/README.md)

Which command stages notes.txt?

- a. git add notes.txt
- b. git log
- c. git branch

**Hints:**

- Consult the prerequisite before deciding.
- The destination is the index.

**Answer:** a

**Explanation:** Add copies the current content to the index.

## Staged diff

ID: quiz-diff

**Difficulty:** easy

**Prerequisites:** [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.md)

Which compares index to HEAD?

- a. git diff
- b. git diff --cached
- c. git log

**Hints:**

- Consult the prerequisite before deciding.
- Look for the staged comparison.

**Answer:** b

**Explanation:** Cached diff shows staged changes relative to HEAD.

## Identity scope

ID: quiz-config

**Difficulty:** easy

**Prerequisites:** [basic-commands/01-init-config-help](../../basic-commands/01-init-config-help/README.md)

Which config scope affects only the current repository?

- a. --global
- b. --system
- c. --local

**Hints:**

- Consult the prerequisite before deciding.
- Avoid changing identity in other repositories.

**Answer:** c

**Explanation:** Local settings are repository-specific.

## Create and switch

ID: quiz-switch

**Difficulty:** easy

**Prerequisites:** [branches/01-create-and-switch](../../branches/01-create-and-switch/README.md)

Which creates and selects feat/notes?

- a. git branch feat/notes
- b. git switch -c feat/notes
- c. git switch main

**Hints:**

- Consult the prerequisite before deciding.
- Look for both operations.

**Answer:** b

**Explanation:** Branch creation alone does not select it.

## HEAD

ID: quiz-head

**Difficulty:** easy

**Prerequisites:** [git-architecture/02-snapshots-head-and-refs](../../git-architecture/02-snapshots-head-and-refs/README.md)

When attached to main, what does HEAD reference?

- a. Current branch ref
- b. Remote server
- c. All files

**Hints:**

- Consult the prerequisite before deciding.
- Consider the symbolic reference.

**Answer:** a

**Explanation:** Attached HEAD is symbolic to the checked-out branch.

## Ignore rules

ID: quiz-ignore

**Difficulty:** easy

**Prerequisites:** [basic-commands/05-ignore-and-review](../../basic-commands/05-ignore-and-review/README.md)

Does .gitignore stop tracking an already tracked file?

- a. Always
- b. After fetch
- c. No

**Hints:**

- Consult the prerequisite before deciding.
- Tracking is determined by the index.

**Answer:** c

**Explanation:** Ignore rules do not remove existing index entries.

## Clone

ID: quiz-clone

**Difficulty:** easy

**Prerequisites:** [remote-repositories/01-remote-concepts](../../remote-repositories/01-remote-concepts/README.md)

Which creates a normal local copy of a remote repository?

- a. git init
- b. git clone
- c. git status

**Hints:**

- Consult the prerequisite before deciding.
- Look for copying existing history.

**Answer:** b

**Explanation:** Clone obtains history and usually configures origin.

## Status

ID: quiz-status

**Difficulty:** easy

**Prerequisites:** [basic-commands/02-status-add-commit](../../basic-commands/02-status-add-commit/README.md)

Which inspects working tree and index changes?

- a. git status
- b. git push
- c. git reset --hard

**Hints:**

- Consult the prerequisite before deciding.
- Inspect without discarding edits.

**Answer:** a

**Explanation:** Status reports staged, unstaged and untracked changes.

## Tag movement

ID: quiz-tag

**Difficulty:** easy

**Prerequisites:** [git-internals/03-commits-and-tags](../../git-internals/03-commits-and-tags/README.md)

What happens to a tag when main advances?

- a. Advances
- b. Disappears
- c. Keeps its target

**Hints:**

- Consult the prerequisite before deciding.
- A tag names a revision.

**Answer:** c

**Explanation:** Tags do not automatically advance with branches.

## Hosting feature

ID: quiz-hosting

**Difficulty:** easy

**Prerequisites:** [fundamentals/03-distributed-and-platforms](../../fundamentals/03-distributed-and-platforms/README.md)

Which is a platform feature rather than a Git object?

- a. Commit
- b. Pull request
- c. Blob

**Hints:**

- Consult the prerequisite before deciding.
- Distinguish hosting from native storage.

**Answer:** b

**Explanation:** A pull request is a collaboration record on a platform.

## Remote inspection

ID: quiz-remote

**Difficulty:** easy

**Prerequisites:** [remote-repositories/01-remote-concepts](../../remote-repositories/01-remote-concepts/README.md)

Which lists configured fetch and push URLs?

- a. git remote -v
- b. git branch -d main
- c. git push

**Hints:**

- Consult the prerequisite before deciding.
- Read configuration rather than transmit commits.

**Answer:** a

**Explanation:** Remote -v lists configured URLs without publishing.

## Fetch

ID: quiz-fetch

**Difficulty:** medium

**Prerequisites:** [remote-repositories/02-fetch-and-tracking](../../remote-repositories/02-fetch-and-tracking/README.md)

With the usual fetch refspec, what happens when a new remote main is fetched?

- a. Local main always advances
- b. Tracking ref updates; checked-out main stays put
- c. Local commits vanish

**Hints:**

- Consult the prerequisite before deciding.
- Distinguish tracking ref from local branch.

**Answer:** b

**Explanation:** Fetch updates configured refs; integration is separate.

## Fast-forward only

ID: quiz-ff

**Difficulty:** medium

**Prerequisites:** [merge-and-conflicts/02-fast-forward](../../merge-and-conflicts/02-fast-forward/README.md)

Tips diverged. What does merge --ff-only do?

- a. Refuses
- b. Creates merge commit
- c. Rebases

**Hints:**

- Consult the prerequisite before deciding.
- Check ancestry first.

**Answer:** a

**Explanation:** A fast-forward cannot join divergent histories.

## Merge parents

ID: quiz-parents

**Difficulty:** medium

**Prerequisites:** [merge-and-conflicts/03-merge-commit](../../merge-and-conflicts/03-merge-commit/README.md)

How many parents does an ordinary non-fast-forward two-branch merge commit have?

- a. 1
- b. 3
- c. 2

**Hints:**

- Consult the prerequisite before deciding.
- Both histories remain connected.

**Answer:** c

**Explanation:** The parents are the prior current tip and merged tip.

## Conflict stages

ID: quiz-conflict

**Difficulty:** medium

**Prerequisites:** [merge-and-conflicts/04-conflict-resolution](../../merge-and-conflicts/04-conflict-resolution/README.md)

Which lists unmerged index entries?

- a. git commit
- b. git ls-files -u
- c. git clean -n

**Hints:**

- Consult the prerequisite before deciding.
- Inspect the index, not the commit log.

**Answer:** b

**Explanation:** The index may contain base, ours and theirs stages.

## Unstage

ID: quiz-unstage

**Difficulty:** medium

**Prerequisites:** [history-and-recovery/02-restore](../../history-and-recovery/02-restore/README.md)

With existing HEAD, which unstages notes.txt without discarding working edits?

- a. git restore --staged -- notes.txt
- b. git restore --worktree -- notes.txt
- c. git reset --hard HEAD

**Hints:**

- Consult the prerequisite before deciding.
- The working file must survive.

**Answer:** a

**Explanation:** Restore --staged uses HEAD by default and changes index only.

## Reset soft

ID: quiz-soft

**Difficulty:** medium

**Prerequisites:** [history-and-recovery/03-reset](../../history-and-recovery/03-reset/README.md)

What does reset --soft preserve when moving a private branch?

- a. Only remote state
- b. Nothing
- c. Index and working tree

**Hints:**

- Consult the prerequisite before deciding.
- Different modes affect different locations.

**Answer:** c

**Explanation:** Soft reset moves HEAD/branch and leaves index and files intact.

## Shared undo

ID: quiz-revert

**Difficulty:** medium

**Prerequisites:** [history-and-recovery/04-revert](../../history-and-recovery/04-revert/README.md)

Which normally undoes a shared ordinary commit without rewriting published history?

- a. git reset --hard
- b. git revert
- c. git push --force

**Hints:**

- Consult the prerequisite before deciding.
- Preserve existing ancestry.

**Answer:** b

**Explanation:** Revert records an inverse change in a new commit.

## Stash scope

ID: quiz-stash

**Difficulty:** medium

**Prerequisites:** [history-and-recovery/06-stash](../../history-and-recovery/06-stash/README.md)

Which stash push option includes untracked but not ignored files?

- a. -u
- b. --keep-index
- c. --all

**Hints:**

- Consult the prerequisite before deciding.
- Untracked is not the same as ignored.

**Answer:** a

**Explanation:** -u includes untracked; --all also includes ignored.

## Cherry-pick

ID: quiz-pick

**Difficulty:** medium

**Prerequisites:** [history-and-recovery/07-cherry-pick](../../history-and-recovery/07-cherry-pick/README.md)

Ordinary successful cherry-pick of a nonempty commit onto another tip usually creates what?

- a. New commit with applied changes
- b. Remote branch
- c. Two-parent merge

**Hints:**

- Consult the prerequisite before deciding.
- Consider applying a change rather than merging history.

**Answer:** a

**Explanation:** The patch is applied in a new parent context.

## Reflog

ID: quiz-reflog

**Difficulty:** medium

**Prerequisites:** [history-and-recovery/05-reflog](../../history-and-recovery/05-reflog/README.md)

Does normal push transfer your local reflog?

- a. Yes
- b. No
- c. Only with tags

**Hints:**

- Consult the prerequisite before deciding.
- Distinguish object transfer from local metadata.

**Answer:** b

**Explanation:** Reflogs are local metadata and can expire.

## Review revision

ID: quiz-review

**Difficulty:** medium

**Prerequisites:** [github/04-pull-requests-and-review](../../github/04-pull-requests-and-review/README.md)

A new PR commit arrives after green checks. Which revision needs verification?

- a. First commit
- b. Any green revision
- c. Latest intended head

**Hints:**

- Consult the prerequisite before deciding.
- Evidence must identify the tested SHA.

**Answer:** c

**Explanation:** Checks on old revisions do not cover new changes.

## Exposed credential

ID: quiz-secret

**Difficulty:** medium

**Prerequisites:** [security/05-secrets-and-disclosure-prevention](../../security/05-secrets-and-disclosure-prevention/README.md)

A real token entered public history. What essential action comes first?

- a. Revoke or rotate
- b. Delete file only
- c. Rename branch

**Hints:**

- Consult the prerequisite before deciding.
- Copies outside your repository may persist.

**Answer:** a

**Explanation:** Assume compromise; history cleanup is separate from invalidation.

## Rebase identity

ID: quiz-rebase

**Difficulty:** hard

**Prerequisites:** [merge-and-conflicts/06-rebase-and-conflicts](../../merge-and-conflicts/06-rebase-and-conflicts/README.md)

Rebasing commits onto a different parent normally changes what?

- a. Only permissions
- b. Replayed commit IDs
- c. Remote automatically

**Hints:**

- Consult the prerequisite before deciding.
- Think about the stored parent.

**Answer:** b

**Explanation:** Commit objects include parent IDs; replay creates new objects as needed.

## Squash

ID: quiz-squash

**Difficulty:** hard

**Prerequisites:** [merge-and-conflicts/05-squash-merge](../../merge-and-conflicts/05-squash-merge/README.md)

After successful merge --squash, before commit, what is true?

- a. HEAD moved
- b. MERGE\_HEAD holds second parent
- c. Changes prepared; HEAD unchanged

**Hints:**

- Consult the prerequisite before deciding.
- Commit is a separate step.

**Answer:** c

**Explanation:** Squash prepares changes without creating MERGE\_HEAD or moving HEAD.

## Three-dot diff

ID: quiz-three-dot

**Difficulty:** hard

**Prerequisites:** [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.md)

With one merge base, what does git diff main...feature compare?

- a. Merge base to feature tip
- b. Feature tip to main tip
- c. Index to HEAD

**Hints:**

- Consult the prerequisite before deciding.
- The first endpoint is derived from ancestry.

**Answer:** a

**Explanation:** Three-dot diff compares merge base to the second tip; log differs.

## Force-with-lease

ID: quiz-lease

**Difficulty:** hard

**Prerequisites:** [remote-repositories/03-pull-push-and-divergence](../../remote-repositories/03-pull-push-and-divergence/README.md)

What does an explicit expected-OID lease guard against?

- a. All data loss
- b. Remote ref differing from expected value
- c. All merge conflicts

**Hints:**

- Consult the prerequisite before deciding.
- Compare current ref with the expectation.

**Answer:** b

**Explanation:** A lease is conditional, not a guarantee against harmful rewrites.

## Bisect

ID: quiz-bisect

**Difficulty:** hard

**Prerequisites:** [advanced-git/01-bisect](../../advanced-git/01-bisect/README.md)

What must a useful bisect test classify?

- a. Author popularity
- b. File size
- c. Target property of selected revision

**Hints:**

- Consult the prerequisite before deciding.
- Test the revision rather than unrelated metadata.

**Answer:** c

**Explanation:** Consistent good/bad classification narrows a known boundary; skip uncertainty.

## Blob identity

ID: quiz-blob

**Difficulty:** hard

**Prerequisites:** [git-internals/02-blobs-and-trees](../../git-internals/02-blobs-and-trees/README.md)

Two files have identical stored blob bytes in the same object format. What may differ?

- a. Path and tree entry mode
- b. Stored bytes
- c. Blob object type

**Hints:**

- Consult the prerequisite before deciding.
- Which object stores filenames?

**Answer:** a

**Explanation:** Blob stores content; tree entries store names and modes.

## Tag peeling

ID: quiz-peel

**Difficulty:** hard

**Prerequisites:** [git-internals/03-commits-and-tags](../../git-internals/03-commits-and-tags/README.md)

What does git rev-parse 'v1.0.0^{commit}' request from a tag pointing at a commit?

- a. Tag message
- b. Underlying commit ID
- c. Working path

**Hints:**

- Consult the prerequisite before deciding.
- Distinguish tag object from target.

**Answer:** b

**Explanation:** Peeling resolves to a commit or fails.

## Reachability

ID: quiz-reachable

**Difficulty:** hard

**Prerequisites:** [git-internals/09-reflogs-and-reachability](../../git-internals/09-reflogs-and-reachability/README.md)

Why name a displaced commit found in reflog with a recovery branch?

- a. Disable all GC
- b. Copy uncommitted files
- c. Make commit reachable via a ref

**Hints:**

- Consult the prerequisite before deciding.
- Think of a persistent reference.

**Answer:** c

**Explanation:** A branch makes the commit reachable independently of temporary reflog entries.

## Worktree

ID: quiz-worktree

**Difficulty:** hard

**Prerequisites:** [advanced-git/02-worktree](../../advanced-git/02-worktree/README.md)

What is normally separate for linked worktrees?

- a. Working files, HEAD and index
- b. Every Git object
- c. All branch refs

**Hints:**

- Consult the prerequisite before deciding.
- Distinguish shared storage from checkout state.

**Answer:** a

**Explanation:** Linked worktrees share objects and most refs but have per-worktree HEAD/index/files.

## Gitlink

ID: quiz-gitlink

**Difficulty:** hard

**Prerequisites:** [advanced-git/03-submodules](../../advanced-git/03-submodules/README.md)

What does a superproject gitlink record?

- a. All nested files
- b. Submodule commit ID
- c. Branch name only

**Hints:**

- Consult the prerequisite before deciding.
- A dependency is pinned to a revision.

**Answer:** b

**Explanation:** A gitlink stores the referenced commit, not the nested tree.

## Signature limits

ID: quiz-signature

**Difficulty:** hard

**Prerequisites:** [security/09-commit-and-tag-signing](../../security/09-commit-and-tag-signing/README.md)

Does a valid cryptographic signature alone prove code safety and authorization?

- a. Always
- b. If main
- c. No

**Hints:**

- Consult the prerequisite before deciding.
- Identify what a signature attests.

**Answer:** c

**Explanation:** Cryptographic verification differs from trust policy and code review.

## Partial clone

ID: quiz-partial

**Difficulty:** hard

**Prerequisites:** [advanced-git/08-partial-and-shallow-clone](../../advanced-git/08-partial-and-shallow-clone/README.md)

Why may later file access in a blob:none partial clone require network?

- a. Promised blobs may need lazy fetch
- b. All commits were deleted
- c. All commands are remote API calls

**Hints:**

- Consult the prerequisite before deciding.
- Initial object transfer may be incomplete by design.

**Answer:** a

**Explanation:** Missing promised objects can be fetched on demand.

---

<!-- navigation-footer -->
[Previous module](../../practical-projects/README.md) · [Index](../README.md) · [Next](../02-challenges/README.md)
<!-- /navigation-footer -->
