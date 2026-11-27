# Interview questions

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../02-challenges/README.md) · [Index](../README.md) · [Next](../04-mock-assessments/README.md)
<!-- /navigation -->

Try first, consult the public solutions afterward. Quizzes use exact choices; interviews and mocks require honest self-assessment. Challenges use only fresh disposable local repositories and fixed state checks, not automatic execution of learner commands. All records form an internal pilot, not the final Learning Hub contract.

## Version control

ID: interview-version-control

**Difficulty:** easy

**Prerequisites:** [fundamentals/01-version-control](../../fundamentals/01-version-control/README.md)

Explain why Git is useful even when working alone.

**Hints:**

- Explain the relevant state or policy before naming commands.
- Name snapshots and comparison.

**Expected answer:** Git records intentional snapshots, permits comparison of revisions and supports isolated experimentation. It does not automatically save every edit or replace backups.

**Rubric:**

- Name snapshots and comparison.
- Explain the limit for uncommitted work.

**Follow-ups:**

- How would you inspect a previous revision?

**Explanation:** Compare your reasoning with the expected answer. The rubric measures explicit concepts, not exact wording; award one point per criterion met, zero otherwise.

## Three Git locations

ID: interview-three-states

**Difficulty:** easy

**Prerequisites:** [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.md)

Explain working tree, index and HEAD using one edited file.

**Hints:**

- Explain the relevant state or policy before naming commands.
- Define all three locations accurately.

**Expected answer:** Working tree is editable content, index prepares the next ordinary commit, HEAD resolves the current revision. Stage A, edit B, commit: A is recorded, B remains unstaged.

**Rubric:**

- Define all three locations accurately.
- Trace A and B without conflating them.

**Follow-ups:**

- Which diff shows A relative to HEAD?

**Explanation:** Compare your reasoning with the expected answer. The rubric measures explicit concepts, not exact wording; award one point per criterion met, zero otherwise.

## Branch as a ref

ID: interview-branch

**Difficulty:** easy

**Prerequisites:** [branches/01-create-and-switch](../../branches/01-create-and-switch/README.md)

What is a branch and what happens when you commit on it?

**Hints:**

- Explain the relevant state or policy before naming commands.
- Describe the ref, not a physical folder copy.

**Expected answer:** A local branch is a movable ref to a commit. When HEAD is attached, a normal commit updates the current branch while other refs normally stay unchanged.

**Rubric:**

- Describe the ref, not a physical folder copy.
- Distinguish branch creation from selection.

**Follow-ups:**

- What differs under detached HEAD?

**Explanation:** Compare your reasoning with the expected answer. The rubric measures explicit concepts, not exact wording; award one point per criterion met, zero otherwise.

## Inspect before commit

ID: interview-status-diff

**Difficulty:** easy

**Prerequisites:** [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.md)

How do you review what will enter a normal commit?

**Hints:**

- Explain the relevant state or policy before naming commands.
- Identify the staged comparison.

**Expected answer:** Use git status to identify state, git diff for unstaged tracked edits, and git diff --cached to inspect the index against HEAD. Stage only intended files and recheck.

**Rubric:**

- Identify the staged comparison.
- Mention untracked files and selective staging.

**Follow-ups:**

- Why might git diff be empty while staged changes exist?

**Explanation:** Compare your reasoning with the expected answer. The rubric measures explicit concepts, not exact wording; award one point per criterion met, zero otherwise.

## Ignore vs tracking

ID: interview-ignore

**Difficulty:** easy

**Prerequisites:** [basic-commands/05-ignore-and-review](../../basic-commands/05-ignore-and-review/README.md)

Why can a tracked file still appear after adding an ignore rule?

**Hints:**

- Explain the relevant state or policy before naming commands.
- Distinguish ignored from tracked.

**Expected answer:** Ignore rules normally filter untracked paths. Existing tracked files remain in the index until intentionally removed from tracking. Review effects before committing such removal.

**Rubric:**

- Distinguish ignored from tracked.
- Explain that history is not erased.

**Follow-ups:**

- What does git rm --cached change?

**Explanation:** Compare your reasoning with the expected answer. The rubric measures explicit concepts, not exact wording; award one point per criterion met, zero otherwise.

## Init and clone

ID: interview-clone-init

**Difficulty:** easy

**Prerequisites:** [remote-repositories/01-remote-concepts](../../remote-repositories/01-remote-concepts/README.md)

When would you choose init instead of clone?

**Hints:**

- Explain the relevant state or policy before naming commands.
- Explain new versus existing history.

**Expected answer:** Init starts Git metadata in a chosen repository; clone obtains an existing repository's history and normally configures an origin and a checkout. Avoid initializing or cloning into the wrong directory.

**Rubric:**

- Explain new versus existing history.
- Identify origin as a usual clone configuration.

**Follow-ups:**

- How do you verify the repository root?

**Explanation:** Compare your reasoning with the expected answer. The rubric measures explicit concepts, not exact wording; award one point per criterion met, zero otherwise.

## Communicate a change

ID: interview-commit-message

**Difficulty:** easy

**Prerequisites:** [professional-workflows/06-conventional-commits](../../professional-workflows/06-conventional-commits/README.md)

What makes a useful commit message?

**Hints:**

- Explain the relevant state or policy before naming commands.
- Give a scoped example such as docs: clarify notes.

**Expected answer:** Describe a focused intent and, where useful, why it matters. Conventional Commits are a team convention, not a native Git requirement. Do not include secrets or unrelated changes.

**Rubric:**

- Give a scoped example such as docs: clarify notes.
- Separate convention from Git requirements.

**Follow-ups:**

- When should two changes be separate commits?

**Explanation:** Compare your reasoning with the expected answer. The rubric measures explicit concepts, not exact wording; award one point per criterion met, zero otherwise.

## Git vs platform

ID: interview-platform

**Difficulty:** easy

**Prerequisites:** [fundamentals/03-distributed-and-platforms](../../fundamentals/03-distributed-and-platforms/README.md)

Can Git work without GitHub or GitLab? Explain.

**Hints:**

- Explain the relevant state or policy before naming commands.
- Identify native local operations.

**Expected answer:** Yes. Git stores and manipulates repositories locally and can exchange objects with remotes. Hosting adds access control, PR/MR reviews and CI services; accounts are not required for local practice.

**Rubric:**

- Identify native local operations.
- Name platform-specific collaboration features.

**Follow-ups:**

- How can two developers practice offline?

**Explanation:** Compare your reasoning with the expected answer. The rubric measures explicit concepts, not exact wording; award one point per criterion met, zero otherwise.

## Fetch vs pull

ID: interview-fetch-pull

**Difficulty:** medium

**Prerequisites:** [remote-repositories/02-fetch-and-tracking](../../remote-repositories/02-fetch-and-tracking/README.md)

Your tracking ref is stale. How would you update it before deciding integration?

**Hints:**

- Explain the relevant state or policy before naming commands.
- Distinguish fetching from integrating.

**Expected answer:** Fetch origin, inspect divergence of local main and origin/main, then choose an integration policy. Pull combines fetching with integration according to options/config; ff-only refuses divergence.

**Rubric:**

- Distinguish fetching from integrating.
- Describe a safe decision on divergence.

**Follow-ups:**

- Why might pull fail even after fetch succeeds?

**Explanation:** Compare your reasoning with the expected answer. The rubric measures explicit concepts, not exact wording; award one point per criterion met, zero otherwise.

## Merge or rebase

ID: interview-merge-rebase

**Difficulty:** medium

**Prerequisites:** [merge-and-conflicts/06-rebase-and-conflicts](../../merge-and-conflicts/06-rebase-and-conflicts/README.md)

Contrast merge and rebase for a feature branch.

**Hints:**

- Explain the relevant state or policy before naming commands.
- Explain topology and identity differences.

**Expected answer:** Merge joins histories, sometimes via fast-forward or a merge commit. Rebase replays commits onto a new base and normally changes replayed IDs. Avoid rewriting shared history without coordination.

**Rubric:**

- Explain topology and identity differences.
- Discuss team policy and shared history.

**Follow-ups:**

- When is fast-forward possible?

**Explanation:** Compare your reasoning with the expected answer. The rubric measures explicit concepts, not exact wording; award one point per criterion met, zero otherwise.

## Conflict triage

ID: interview-resolve

**Difficulty:** medium

**Prerequisites:** [merge-and-conflicts/04-conflict-resolution](../../merge-and-conflicts/04-conflict-resolution/README.md)

Describe a safe process for resolving a merge conflict.

**Hints:**

- Explain the relevant state or policy before naming commands.
- Explain inspection and intentional resolution.

**Expected answer:** Inspect status and unmerged entries, understand base/ours/theirs, choose semantically correct content, stage the resolution, run tests and finish the operation. Preserve desired edits before aborting.

**Rubric:**

- Explain inspection and intentional resolution.
- Mention testing and safe abort limits.

**Follow-ups:**

- Why is deleting conflict markers insufficient?

**Explanation:** Compare your reasoning with the expected answer. The rubric measures explicit concepts, not exact wording; award one point per criterion met, zero otherwise.

## Reset vs revert

ID: interview-reset-revert

**Difficulty:** medium

**Prerequisites:** [history-and-recovery/03-reset](../../history-and-recovery/03-reset/README.md)

How would you undo a private commit versus a published commit?

**Hints:**

- Explain the relevant state or policy before naming commands.
- Contrast moving refs and creating a new commit.

**Expected answer:** For private history, inspect state and choose reset mode only with a known target and preserved work. For published history, prefer a new revert/corrective commit under review. Hard reset can discard local edits.

**Rubric:**

- Contrast moving refs and creating a new commit.
- State destructive risks and shared-history policy.

**Follow-ups:**

- What does soft reset preserve?

**Explanation:** Compare your reasoning with the expected answer. The rubric measures explicit concepts, not exact wording; award one point per criterion met, zero otherwise.

## Stash limitations

ID: interview-stash

**Difficulty:** medium

**Prerequisites:** [history-and-recovery/06-stash](../../history-and-recovery/06-stash/README.md)

What should you check before using stash to change tasks?

**Hints:**

- Explain the relevant state or policy before naming commands.
- Mention untracked/ignored scope.

**Expected answer:** Inspect staged, unstaged and untracked files; choose stash scope deliberately, record the entry, verify clean state, and inspect conflicts when applying. A stash is local and not a substitute for durable backups.

**Rubric:**

- Mention untracked/ignored scope.
- Distinguish apply and pop on success/conflict.

**Follow-ups:**

- Why might an apply conflict?

**Explanation:** Compare your reasoning with the expected answer. The rubric measures explicit concepts, not exact wording; award one point per criterion met, zero otherwise.

## Fork contribution

ID: interview-fork

**Difficulty:** medium

**Prerequisites:** [github/05-forks-and-open-source](../../github/05-forks-and-open-source/README.md)

Describe a contribution workflow when you cannot push upstream.

**Hints:**

- Explain the relevant state or policy before naming commands.
- Distinguish origin and upstream destinations.

**Expected answer:** Fork or use an authorized contributor repository, clone it, name upstream separately, base a feature branch on a known upstream revision, publish only to your fork and request review. Respect contribution policy and verify exact diff.

**Rubric:**

- Distinguish origin and upstream destinations.
- Describe permission and review boundaries.

**Follow-ups:**

- How would you synchronize your fork safely?

**Explanation:** Compare your reasoning with the expected answer. The rubric measures explicit concepts, not exact wording; award one point per criterion met, zero otherwise.

## CI quality gate

ID: interview-ci-gate

**Difficulty:** medium

**Prerequisites:** [ci-cd/09-quality-gates-and-troubleshooting](../../ci-cd/09-quality-gates-and-troubleshooting/README.md)

A CI job fails after a push. How do you diagnose it?

**Hints:**

- Explain the relevant state or policy before naming commands.
- Use actual logs and exact revision.

**Expected answer:** Identify the exact SHA, failing job and step, inspect logs, reproduce in an isolated environment where possible, correct the cause and rerun checks on the new SHA. Do not disable gates to get green.

**Rubric:**

- Use actual logs and exact revision.
- Require rerun after changes.

**Follow-ups:**

- Can a green test establish deployment success?

**Explanation:** Compare your reasoning with the expected answer. The rubric measures explicit concepts, not exact wording; award one point per criterion met, zero otherwise.

## Release versioning

ID: interview-release

**Difficulty:** medium

**Prerequisites:** [professional-workflows/07-semantic-versioning](../../professional-workflows/07-semantic-versioning/README.md)

How do you decide a SemVer version and identify the release revision?

**Hints:**

- Explain the relevant state or policy before naming commands.
- Ground version choice in the public contract.

**Expected answer:** Given a defined public API/contract, choose major for incompatible changes, minor for backward-compatible functionality, patch for backward-compatible fixes. Review and test the exact revision, then create an annotated tag per policy. A hosted release is distinct.

**Rubric:**

- Ground version choice in the public contract.
- Distinguish tag from platform release.

**Follow-ups:**

- What if a published tag is incorrect?

**Explanation:** Compare your reasoning with the expected answer. The rubric measures explicit concepts, not exact wording; award one point per criterion met, zero otherwise.

## Object model

ID: interview-objects

**Difficulty:** hard

**Prerequisites:** [git-internals/02-blobs-and-trees](../../git-internals/02-blobs-and-trees/README.md)

Trace a commit to its stored file contents.

**Hints:**

- Explain the relevant state or policy before naming commands.
- Describe commit, tree and blob roles.

**Expected answer:** A commit references a root tree and parent commits. Trees record names, modes and object IDs, recursively referring to trees/blobs. Blobs hold file bytes, not names. Refs name commits independently of physical storage.

**Rubric:**

- Describe commit, tree and blob roles.
- Explain why identical content may share a blob.

**Follow-ups:**

- What does a commit hash depend on besides tree?

**Explanation:** Compare your reasoning with the expected answer. The rubric measures explicit concepts, not exact wording; award one point per criterion met, zero otherwise.

## Recoverability

ID: interview-recovery

**Difficulty:** hard

**Prerequisites:** [git-internals/09-reflogs-and-reachability](../../git-internals/09-reflogs-and-reachability/README.md)

A private branch tip disappeared after reset. Explain recovery and its limits.

**Hints:**

- Explain the relevant state or policy before naming commands.
- Explain recovery via verified ref.

**Expected answer:** Stop destructive operations; inspect reflog and known IDs, confirm candidate content and ancestry, create a recovery ref and verify. Reflogs expire and unreachable objects may be pruned; uncommitted edits may never have been recorded.

**Rubric:**

- Explain recovery via verified ref.
- Explicitly reject guaranteed recovery.

**Follow-ups:**

- Why avoid gc during recovery?

**Explanation:** Compare your reasoning with the expected answer. The rubric measures explicit concepts, not exact wording; award one point per criterion met, zero otherwise.

## Concurrent remote update

ID: interview-lease

**Difficulty:** hard

**Prerequisites:** [remote-repositories/03-pull-push-and-divergence](../../remote-repositories/03-pull-push-and-divergence/README.md)

Explain why force-with-lease is safer than force, but not sufficient policy.

**Hints:**

- Explain the relevant state or policy before naming commands.
- Describe conditional ref comparison.

**Expected answer:** A lease condition compares the remote ref with an expected value and refuses a mismatch. Explicit expectations avoid relying on tracking refs refreshed by background fetch. Even a successful lease can discard history, so require ownership, coordination and branch policy.

**Rubric:**

- Describe conditional ref comparison.
- Explain why successful lease is not consent.

**Follow-ups:**

- What should happen when the lease fails?

**Explanation:** Compare your reasoning with the expected answer. The rubric measures explicit concepts, not exact wording; award one point per criterion met, zero otherwise.

## Parallel checkout

ID: interview-worktree

**Difficulty:** hard

**Prerequisites:** [advanced-git/02-worktree](../../advanced-git/02-worktree/README.md)

How can you inspect a release while continuing feature development?

**Hints:**

- Explain the relevant state or policy before naming commands.
- Identify shared versus independent state.

**Expected answer:** A linked worktree provides separate files, HEAD and index while sharing objects and many refs. Create a suitable separate branch or detached worktree, verify its path and remove only a clean owned worktree when done.

**Rubric:**

- Identify shared versus independent state.
- Explain safe branch/path selection and cleanup.

**Follow-ups:**

- Why not check out the same branch twice by default?

**Explanation:** Compare your reasoning with the expected answer. The rubric measures explicit concepts, not exact wording; award one point per criterion met, zero otherwise.

## Pinned dependency

ID: interview-submodules

**Difficulty:** hard

**Prerequisites:** [advanced-git/03-submodules](../../advanced-git/03-submodules/README.md)

Explain what a submodule update means for reproducibility.

**Hints:**

- Explain the relevant state or policy before naming commands.
- Explain gitlink and configuration roles.

**Expected answer:** The superproject stores a gitlink to a specific submodule commit and .gitmodules describes configuration. A reproducible checkout needs that commit available and appropriate initialization/update. Updating a nested checkout alone is not a committed superproject dependency change.

**Rubric:**

- Explain gitlink and configuration roles.
- Mention availability and committing the pin.

**Follow-ups:**

- What happens if the referenced commit is unavailable?

**Explanation:** Compare your reasoning with the expected answer. The rubric measures explicit concepts, not exact wording; award one point per criterion met, zero otherwise.

## Regression search

ID: interview-bisect

**Difficulty:** hard

**Prerequisites:** [advanced-git/01-bisect](../../advanced-git/01-bisect/README.md)

How would you design a reliable git bisect experiment?

**Hints:**

- Explain the relevant state or policy before naming commands.
- Define good/bad and reliable test.

**Expected answer:** Establish a known good/bad boundary, use a stable deterministic classification of each revision, skip genuinely untestable commits, record environment and evidence, then verify the candidate and reset bisect state. Nonmonotonic behavior can complicate results.

**Rubric:**

- Define good/bad and reliable test.
- Discuss skip, verification and cleanup.

**Follow-ups:**

- What if the test is flaky?

**Explanation:** Compare your reasoning with the expected answer. The rubric measures explicit concepts, not exact wording; award one point per criterion met, zero otherwise.

## Evidence-based integration

ID: interview-audit

**Difficulty:** hard

**Prerequisites:** [security/12-governance-audit-and-traceability](../../security/12-governance-audit-and-traceability/README.md)

How do you prove an integrated squash commit matches the reviewed change?

**Hints:**

- Explain the relevant state or policy before naming commands.
- Tie review evidence to exact SHA and base.

**Expected answer:** Record reviewed head/tree and base, verify checks/review and authorization for that SHA, require expected head on merge. If base is unchanged and feature includes it, compare integrated tree to reviewed tree and sole parent to base; verify post-merge checks and metadata.

**Rubric:**

- Tie review evidence to exact SHA and base.
- Explain tree equality conditional on unchanged base.

**Follow-ups:**

- Why can a different base require new review?

**Explanation:** Compare your reasoning with the expected answer. The rubric measures explicit concepts, not exact wording; award one point per criterion met, zero otherwise.

## Credential incident

ID: interview-secret-incident

**Difficulty:** hard

**Prerequisites:** [security/11-credential-exposure-and-incident-response](../../security/11-credential-exposure-and-incident-response/README.md)

Respond to a credential accidentally committed and pushed publicly.

**Hints:**

- Explain the relevant state or policy before naming commands.
- Prioritize revocation before history cleanup.

**Expected answer:** Treat it as compromised: revoke/rotate, limit exposure and notify appropriate owners, investigate use, remove the secret from current files and coordinate any history cleanup. Copies may persist; prevention includes scanning and least privilege.

**Rubric:**

- Prioritize revocation before history cleanup.
- Recognize persistent copies and incident coordination.

**Follow-ups:**

- Why is deleting a file insufficient?

**Explanation:** Compare your reasoning with the expected answer. The rubric measures explicit concepts, not exact wording; award one point per criterion met, zero otherwise.

---

<!-- navigation-footer -->
[Previous](../02-challenges/README.md) · [Index](../README.md) · [Next](../04-mock-assessments/README.md)
<!-- /navigation-footer -->
