# Practical challenges

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../01-quizzes/README.md) · [Index](../README.md) · [Next](../03-interviews/README.md)
<!-- /navigation -->

Try first, consult the public solutions afterward. Quizzes use exact choices; interviews and mocks require honest self-assessment. Challenges use only fresh disposable local repositories and fixed state checks, not automatic execution of learner commands. All records form an internal pilot, not the final Learning Hub contract.

## First committed snapshot

ID: challenge-first-commit

**Difficulty:** easy

**Prerequisites:** [practical-projects/01-my-first-repository](../../practical-projects/01-my-first-repository/README.md) · [getting-started/05-first-commit](../../getting-started/05-first-commit/README.md)

Commit notes.txt containing status: ready; finish clean on main with one commit.

**Time (min):** 10

**Execution:** local_only · Requires real Git in a fresh disposable repository; no browser/runtime claim.

**Setup:** Start a fresh local repository using only the Disposable setup of project 01 (linked prerequisites); verify main, fictional identity and no remote. Git 2.40+ and Bash/Git Bash. Run commands individually, stop on unexpected failure, and use LF line endings. Use the fresh empty repo.

**Hints:**

- The file must enter the index first.
- Inspect staged content before committing.

**Solution:**

- Write exactly status: ready plus a final LF to notes.txt.
- git add notes.txt
- git diff --cached
- git commit -m 'docs: add notes'
- After checking results, close the dedicated shell and remove only the verified temporary directory with a file manager. Never use the guide repository.

**State checks:**

- kind=branch, value=main
- kind=commit-count, value=1
- file=notes.txt, kind=head-content, value=status: ready
- file=notes.txt, kind=tracked
- kind=clean

**Explanation:** A clean status alone is not sufficient: the committed content and count must match.

## Separate staged and working states

ID: challenge-staged-snapshot

**Difficulty:** easy

**Prerequisites:** [practical-projects/01-my-first-repository](../../practical-projects/01-my-first-repository/README.md) · [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.md)

Leave HEAD at draft, stage ready, then change working file to experiment without staging it again.

**Time (min):** 10

**Execution:** local_only · Requires real Git in a fresh disposable repository; no browser/runtime claim.

**Setup:** Start a fresh local repository using only the Disposable setup of project 01 (linked prerequisites); verify main, fictional identity and no remote. Git 2.40+ and Bash/Git Bash. Run commands individually, stop on unexpected failure, and use LF line endings. Create notes.txt with exactly status: draft and a final LF; git add notes.txt; git commit -m 'docs: initialize notes'.

**Hints:**

- The three locations can differ.
- Inspect HEAD:notes.txt and :notes.txt.

**Solution:**

- Write exactly status: ready plus a final LF to notes.txt.
- git add notes.txt
- Write exactly status: experiment plus a final LF to notes.txt.
- git show HEAD:notes.txt
- git show :notes.txt
- git status --short
- After checking results, close the dedicated shell and remove only the verified temporary directory with a file manager. Never use the guide repository.

**State checks:**

- kind=branch, value=main
- kind=commit-count, value=1
- file=notes.txt, kind=head-content, value=status: draft
- file=notes.txt, kind=index-content, value=status: ready
- file=notes.txt, kind=work-content, value=status: experiment

**Explanation:** Do not commit or restore; a dirty tree is the required result here.

## Preserve a working edit

ID: challenge-unstage

**Difficulty:** easy

**Prerequisites:** [practical-projects/01-my-first-repository](../../practical-projects/01-my-first-repository/README.md) · [history-and-recovery/02-restore](../../history-and-recovery/02-restore/README.md)

Unstage ready without losing it from the working file; HEAD and index must still contain draft.

**Time (min):** 10

**Execution:** local_only · Requires real Git in a fresh disposable repository; no browser/runtime claim.

**Setup:** Start a fresh local repository using only the Disposable setup of project 01 (linked prerequisites); verify main, fictional identity and no remote. Git 2.40+ and Bash/Git Bash. Run commands individually, stop on unexpected failure, and use LF line endings. Create notes.txt with exactly status: draft and a final LF; git add notes.txt; git commit -m 'docs: initialize notes'.

**Hints:**

- Only the index should change.
- Use restore --staged after preparing the new content.

**Solution:**

- Write exactly status: ready plus a final LF to notes.txt.
- git add notes.txt
- git restore --staged -- notes.txt
- git diff
- After checking results, close the dedicated shell and remove only the verified temporary directory with a file manager. Never use the guide repository.

**State checks:**

- kind=branch, value=main
- kind=commit-count, value=1
- file=notes.txt, kind=head-content, value=status: draft
- file=notes.txt, kind=index-content, value=status: draft
- file=notes.txt, kind=work-content, value=status: ready

**Explanation:** Restore --staged does not discard the working edit when HEAD exists.

## Isolate a feature

ID: challenge-feature-branch

**Difficulty:** easy

**Prerequisites:** [practical-projects/01-my-first-repository](../../practical-projects/01-my-first-repository/README.md) · [branches/01-create-and-switch](../../branches/01-create-and-switch/README.md)

Create feat/notes from draft and commit ready there, leaving main at the first commit.

**Time (min):** 15

**Execution:** local_only · Requires real Git in a fresh disposable repository; no browser/runtime claim.

**Setup:** Start a fresh local repository using only the Disposable setup of project 01 (linked prerequisites); verify main, fictional identity and no remote. Git 2.40+ and Bash/Git Bash. Run commands individually, stop on unexpected failure, and use LF line endings. Create notes.txt with exactly status: draft and a final LF; git add notes.txt; git commit -m 'docs: initialize notes'.

**Hints:**

- Branch creation and selection are separate concepts.
- Use switch -c before editing.

**Solution:**

- git switch -c feat/notes
- Write exactly status: ready plus a final LF to notes.txt.
- git add notes.txt
- git commit -m 'docs: update notes'
- git log --oneline --all
- After checking results, close the dedicated shell and remove only the verified temporary directory with a file manager. Never use the guide repository.

**State checks:**

- kind=branch, value=feat/notes
- kind=commit-count, value=2
- kind=same-ref, left=main, right=HEAD^1
- file=notes.txt, kind=head-content, value=status: ready
- kind=clean

**Explanation:** The main reference must remain on the parent of the feature commit.

## Integrate by fast-forward

ID: challenge-fast-forward

**Difficulty:** medium

**Prerequisites:** [practical-projects/01-my-first-repository](../../practical-projects/01-my-first-repository/README.md) · [merge-and-conflicts/02-fast-forward](../../merge-and-conflicts/02-fast-forward/README.md)

Integrate feat/notes into main with no extra merge commit; both refs must match.

**Time (min):** 15

**Execution:** local_only · Requires real Git in a fresh disposable repository; no browser/runtime claim.

**Setup:** Start a fresh local repository using only the Disposable setup of project 01 (linked prerequisites); verify main, fictional identity and no remote. Git 2.40+ and Bash/Git Bash. Run commands individually, stop on unexpected failure, and use LF line endings. Create notes.txt with exactly status: draft and a final LF; git add notes.txt; git commit -m 'docs: initialize notes'.

**Hints:**

- Keep main from diverging.
- Verify the feature is a descendant and use --ff-only.

**Solution:**

- git switch -c feat/notes
- Write exactly status: ready plus a final LF to notes.txt.
- git add notes.txt
- git commit -m 'docs: update notes'
- git switch main
- git merge --ff-only feat/notes
- After checking results, close the dedicated shell and remove only the verified temporary directory with a file manager. Never use the guide repository.

**State checks:**

- kind=branch, value=main
- kind=commit-count, value=2
- kind=same-ref, left=main, right=feat/notes
- file=notes.txt, kind=head-content, value=status: ready
- kind=clean

**Explanation:** Fast-forward moves the current ref rather than creating a new merge commit.

## Resolve a conflict

ID: challenge-merge-resolution

**Difficulty:** medium

**Prerequisites:** [practical-projects/01-my-first-repository](../../practical-projects/01-my-first-repository/README.md) · [merge-and-conflicts/04-conflict-resolution](../../merge-and-conflicts/04-conflict-resolution/README.md)

Diverge main and feat/notes from draft, resolve the same-line conflict to reviewed and retain both parents.

**Time (min):** 20

**Execution:** local_only · Requires real Git in a fresh disposable repository; no browser/runtime claim.

**Setup:** Start a fresh local repository using only the Disposable setup of project 01 (linked prerequisites); verify main, fictional identity and no remote. Git 2.40+ and Bash/Git Bash. Run commands individually, stop on unexpected failure, and use LF line endings. Create notes.txt with exactly status: draft and a final LF; git add notes.txt; git commit -m 'docs: initialize notes'.

**Hints:**

- Make different changes to the same line.
- Inspect git ls-files -u before staging the chosen resolution.

**Solution:**

- git switch -c feat/notes
- Write exactly status: ready plus a final LF to notes.txt.
- git add notes.txt
- git commit -m 'docs: update notes'
- git switch main
- Write exactly status: experiment plus a final LF to notes.txt.
- git add notes.txt
- git commit -m 'docs: update notes'
- Run git merge feat/notes; expect a conflict, verify MERGE\_HEAD and inspect git ls-files -u. Stop on any other failure.
- Write exactly status: reviewed plus a final LF to notes.txt.
- git add notes.txt
- git diff --cached --check
- git commit -m 'merge: resolve notes'
- After checking results, close the dedicated shell and remove only the verified temporary directory with a file manager. Never use the guide repository.

**State checks:**

- kind=branch, value=main
- kind=commit-count, value=4
- kind=parent-count, value=2
- kind=same-ref, left=HEAD^2, right=feat/notes
- file=notes.txt, kind=head-content, value=status: reviewed
- kind=no-unmerged
- kind=clean

**Explanation:** If aborting an active ordinary merge, preserve wanted edits first. A successful merge has two parents and no unmerged entries.

## Undo without rewriting

ID: challenge-revert

**Difficulty:** medium

**Prerequisites:** [practical-projects/01-my-first-repository](../../practical-projects/01-my-first-repository/README.md) · [history-and-recovery/04-revert](../../history-and-recovery/04-revert/README.md)

Commit ready then undo its content with a new commit. Preserve the two original commits.

**Time (min):** 15

**Execution:** local_only · Requires real Git in a fresh disposable repository; no browser/runtime claim.

**Setup:** Start a fresh local repository using only the Disposable setup of project 01 (linked prerequisites); verify main, fictional identity and no remote. Git 2.40+ and Bash/Git Bash. Run commands individually, stop on unexpected failure, and use LF line endings. Create notes.txt with exactly status: draft and a final LF; git add notes.txt; git commit -m 'docs: initialize notes'.

**Hints:**

- The history must grow, not shrink.
- Use revert on the last ordinary commit.

**Solution:**

- Write exactly status: ready plus a final LF to notes.txt.
- git add notes.txt
- git commit -m 'docs: update notes'
- git revert --no-edit HEAD
- After checking results, close the dedicated shell and remove only the verified temporary directory with a file manager. Never use the guide repository.

**State checks:**

- kind=branch, value=main
- kind=commit-count, value=3
- kind=parent-count, value=1
- file=notes.txt, kind=head-content, value=status: draft
- file=notes.txt, kind=ref-content, ref=HEAD^1, value=status: ready
- file=notes.txt, kind=ref-content, ref=HEAD\~2, value=status: draft
- kind=same-tree, left=HEAD, right=HEAD\~2
- kind=clean

**Explanation:** Revert creates a new inverse change. This is not a reset.

## Preserve unfinished work

ID: challenge-stash

**Difficulty:** medium

**Prerequisites:** [practical-projects/01-my-first-repository](../../practical-projects/01-my-first-repository/README.md) · [history-and-recovery/06-stash](../../history-and-recovery/06-stash/README.md)

Stash a ready working edit and an untracked review.txt, verify clean state, then apply the stash. Leave both edits restored and HEAD at draft.

**Time (min):** 15

**Execution:** local_only · Requires real Git in a fresh disposable repository; no browser/runtime claim.

**Setup:** Start a fresh local repository using only the Disposable setup of project 01 (linked prerequisites); verify main, fictional identity and no remote. Git 2.40+ and Bash/Git Bash. Run commands individually, stop on unexpected failure, and use LF line endings. Create notes.txt with exactly status: draft and a final LF; git add notes.txt; git commit -m 'docs: initialize notes'.

**Hints:**

- Include untracked files explicitly.
- Use apply rather than pop so the stash remains for inspection.

**Solution:**

- Write exactly status: ready plus a final LF to notes.txt.
- Create review.txt with exactly review: done plus LF.
- git stash push -u -m 'practice notes'
- git status --porcelain
- git stash apply
- git stash list
- After checking results, close the dedicated shell and remove only the verified temporary directory with a file manager. Never use the guide repository.

**State checks:**

- kind=branch, value=main
- kind=commit-count, value=1
- file=notes.txt, kind=head-content, value=status: draft
- file=notes.txt, kind=index-content, value=status: draft
- file=notes.txt, kind=work-content, value=status: ready
- file=review.txt, kind=work-content, value=review: done
- file=review.txt, kind=untracked

**Explanation:** The final-state check cannot prove the temporary stash operation; record intermediate clean status and stash list as manual evidence.

## Recover a displaced tip

ID: challenge-recover-tip

**Difficulty:** hard

**Prerequisites:** [practical-projects/01-my-first-repository](../../practical-projects/01-my-first-repository/README.md) · [history-and-recovery/05-reflog](../../history-and-recovery/05-reflog/README.md)

Simulate loss of a committed tip in a disposable repo. Recover it with recovery/notes while main stays at draft.

**Time (min):** 20

**Execution:** local_only · Requires real Git in a fresh disposable repository; no browser/runtime claim.

**Setup:** Start a fresh local repository using only the Disposable setup of project 01 (linked prerequisites); verify main, fictional identity and no remote. Git 2.40+ and Bash/Git Bash. Run commands individually, stop on unexpected failure, and use LF line endings. Create notes.txt with exactly status: draft and a final LF; git add notes.txt; git commit -m 'docs: initialize notes'.

**Hints:**

- Save the tip ID before the demonstration.
- Verify the reflog candidate and create a new ref, not another reset.

**Solution:**

- Write exactly status: recovered plus a final LF to notes.txt.
- git add notes.txt
- git commit -m 'docs: update notes'
- git rev-parse HEAD; record the ID outside the repo.
- Verify git status --porcelain is empty, then only in this disposable repository run git reset --hard HEAD\~1.
- git reflog show HEAD
- Inspect git show HEAD@{1}; verify its ID matches the recorded tip, then git branch recovery/notes 'HEAD@{1}'.
- After checking results, close the dedicated shell and remove only the verified temporary directory with a file manager. Never use the guide repository.

**State checks:**

- kind=branch, value=main
- kind=commit-count, value=1
- file=notes.txt, kind=head-content, value=status: draft
- kind=ancestor, newer=recovery/notes, older=main
- file=notes.txt, kind=ref-content, ref=recovery/notes, value=status: recovered
- kind=different-ref, left=main, right=recovery/notes
- kind=clean

**Explanation:** Never assume reflog positions or guaranteed recovery; verify IDs and avoid destructive commands on valuable work.

## Integrate a reviewed tree

ID: challenge-squash

**Difficulty:** hard

**Prerequisites:** [practical-projects/01-my-first-repository](../../practical-projects/01-my-first-repository/README.md) · [merge-and-conflicts/05-squash-merge](../../merge-and-conflicts/05-squash-merge/README.md)

Create two feature commits and squash onto unchanged main. Main must have exactly two commits and the same tree as the feature tip.

**Time (min):** 20

**Execution:** local_only · Requires real Git in a fresh disposable repository; no browser/runtime claim.

**Setup:** Start a fresh local repository using only the Disposable setup of project 01 (linked prerequisites); verify main, fictional identity and no remote. Git 2.40+ and Bash/Git Bash. Run commands individually, stop on unexpected failure, and use LF line endings. Create notes.txt with exactly status: draft and a final LF; git add notes.txt; git commit -m 'docs: initialize notes'.

**Hints:**

- A squash commit has one parent.
- Compare tree IDs, not commit IDs, after integration.

**Solution:**

- git switch -c feat/notes
- Write exactly status: ready plus a final LF to notes.txt.
- git add notes.txt
- git commit -m 'docs: update notes'
- Create review.txt with exactly review: done plus LF; git add review.txt; git commit -m 'docs: record review'.
- git diff main...HEAD
- git switch main
- git merge --squash feat/notes
- git diff --cached --check
- git commit -m 'feat: deliver reviewed notes'
- After checking results, close the dedicated shell and remove only the verified temporary directory with a file manager. Never use the guide repository.

**State checks:**

- kind=branch, value=main
- kind=commit-count, value=2
- kind=parent-count, value=1
- file=notes.txt, kind=head-content, value=status: ready
- file=review.txt, kind=head-content, value=review: done
- kind=same-tree, left=main, right=feat/notes
- kind=different-ref, left=main, right=feat/notes
- kind=ref-commit-count, ref=feat/notes, value=3
- kind=same-ref, left=HEAD^1, right=feat/notes\~2
- file=notes.txt, kind=ref-content, ref=HEAD^1, value=status: draft
- file=notes.txt, kind=ref-content, ref=feat/notes^1, value=status: ready
- kind=clean

**Explanation:** Do not assume merge --abort handles a conflicting squash. Stop, preserve edits and inspect; recreate this disposable fixture if needed.

## Pin a release

ID: challenge-release-tag

**Difficulty:** hard

**Prerequisites:** [practical-projects/01-my-first-repository](../../practical-projects/01-my-first-repository/README.md) · [professional-workflows/12-release-management](../../professional-workflows/12-release-management/README.md)

Tag a ready revision with annotated v1.0.0, then advance main with future.txt. Tag must still resolve to the previous commit.

**Time (min):** 15

**Execution:** local_only · Requires real Git in a fresh disposable repository; no browser/runtime claim.

**Setup:** Start a fresh local repository using only the Disposable setup of project 01 (linked prerequisites); verify main, fictional identity and no remote. Git 2.40+ and Bash/Git Bash. Run commands individually, stop on unexpected failure, and use LF line endings. Create notes.txt with exactly status: draft and a final LF; git add notes.txt; git commit -m 'docs: initialize notes'.

**Hints:**

- A tag should identify an exact revision.
- Use tag -a and peel to a commit.

**Solution:**

- Write exactly status: ready plus a final LF to notes.txt.
- git add notes.txt
- git commit -m 'docs: update notes'
- git tag -a v1.0.0 -m 'Ready notes release'
- Create future.txt with exactly future work plus LF; git add future.txt; git commit -m 'docs: future work'.
- git rev-parse 'v1.0.0^{commit}'
- After checking results, close the dedicated shell and remove only the verified temporary directory with a file manager. Never use the guide repository.

**State checks:**

- kind=branch, value=main
- kind=commit-count, value=3
- kind=tag-type, tag=v1.0.0, value=tag
- kind=same-ref, left=v1.0.0, right=HEAD^1
- file=notes.txt, kind=ref-content, ref=v1.0.0, value=status: ready
- file=future.txt, kind=head-content, value=future work
- kind=clean

**Explanation:** An annotated Git tag is not a hosted release; never replace published tags casually.

## Transfer one change

ID: challenge-cherry-pick

**Difficulty:** hard

**Prerequisites:** [practical-projects/01-my-first-repository](../../practical-projects/01-my-first-repository/README.md) · [history-and-recovery/07-cherry-pick](../../history-and-recovery/07-cherry-pick/README.md)

Commit review.txt on feat/notes, advance main independently to ready, and cherry-pick only the review commit onto main. Keep feature distinct.

**Time (min):** 20

**Execution:** local_only · Requires real Git in a fresh disposable repository; no browser/runtime claim.

**Setup:** Start a fresh local repository using only the Disposable setup of project 01 (linked prerequisites); verify main, fictional identity and no remote. Git 2.40+ and Bash/Git Bash. Run commands individually, stop on unexpected failure, and use LF line endings. Create notes.txt with exactly status: draft and a final LF; git add notes.txt; git commit -m 'docs: initialize notes'.

**Hints:**

- Use a separate file to avoid a manufactured conflict.
- Check parent count and final content; commit IDs need not match.

**Solution:**

- git switch -c feat/notes
- Create review.txt with exactly review: done plus LF; git add review.txt; git commit -m 'docs: record review'.
- git switch main
- Write exactly status: ready plus a final LF to notes.txt.
- git add notes.txt
- git commit -m 'docs: update notes'
- git cherry-pick feat/notes
- After checking results, close the dedicated shell and remove only the verified temporary directory with a file manager. Never use the guide repository.

**State checks:**

- kind=branch, value=main
- kind=commit-count, value=3
- kind=parent-count, value=1
- file=notes.txt, kind=head-content, value=status: ready
- file=review.txt, kind=head-content, value=review: done
- file=notes.txt, kind=ref-content, ref=feat/notes, value=status: draft
- kind=different-ref, left=main, right=feat/notes
- kind=clean

**Explanation:** If an unexpected cherry-pick conflict occurs, inspect and preserve wanted work before aborting. Applied content is not proof of identical history.

---

<!-- navigation-footer -->
[Previous](../01-quizzes/README.md) · [Index](../README.md) · [Next](../03-interviews/README.md)
<!-- /navigation-footer -->
