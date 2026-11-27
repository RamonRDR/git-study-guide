# 08 Remotes & Synchronization

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../07-merge-rebase-and-conflicts/README.md) · [Index](../README.md) · [Next](../09-recovery-and-stash/README.md)
<!-- /navigation -->

Generated from canonical catalog JSON. Edit the records, not this page.

Reference entries describe commands and operations, not a sequence to run. Use disposable repositories for practice. Hosted operations are optional.

**Total distinct entries: 7**

- [`git clone`](#git-clone)
- [`git remote add`](#git-remote-add)
- [`git fetch`](#git-fetch)
- [`git pull --ff-only`](#git-pull-ff-only)
- [`git push`](#git-push)
- [`git push --delete`](#git-push-delete)
- [`git push --force-with-lease`](#git-push-force-with-lease)

## git-clone

**`git clone`**

**Type:** Native command

**Level:** Beginner

**Find by intent:** Create a repository, Synchronize repositories

**Risk:** State change. Verify the source and destination; treat checked-out code and local configuration as untrusted until reviewed.

**Purpose:** Create a local repository from an existing repository and normally check out its initial branch.

**Prerequisites:** Use an owned disposable parent directory, an existing trusted local source and an unused destination name.

**Options:** Supply source and optional destination; --no-checkout skips initial checkout; --branch selects an initial branch or tag.

**When to use:** When obtaining an independent working copy of an existing project.

**When to avoid:** Avoid cloning untrusted repositories into important directories or treating a clone as a complete copy of all server data.

**Syntax**

`git clone origin.git learner`

**Basic example**

`git clone origin.git learner`

From a disposable parent directory, clone an existing populated local bare repository.

**Professional example**

`git clone --branch main origin.git reviewer`

Create a second local clone for a review simulation; main must exist.

**State effects**

- Working tree: Changes
- Index: Changes
- Objects / refs / history: Changes
- Remote repository: Unchanged
- Other state: Changes

**Expected result:** Normally creates a destination with Git objects, origin configuration, remote-tracking refs and a checked-out branch; empty repositories and options may differ.

**Effects and side effects:** Creates a new repository and working files locally; does not publish changes to the source.

**Common errors:** Assuming clone copies issues, permissions, CI settings or every remote ref.

**Alternatives:** Use git init with an explicit remote when starting a new project instead of copying an existing one.

**Recovery:** If a clone fails, inspect the error and destination; retry into a new empty directory without deleting unrelated files.

**Version and dependencies:** Standard Git syntax; use Git 2.40 or newer for this guide's labs. Hosted services may require authentication and permissions; these examples use only local paths.

**Related lessons**

- [remote-repositories/01-remote-concepts](../../remote-repositories/01-remote-concepts/README.md)
- [remote-repositories/02-fetch-and-tracking](../../remote-repositories/02-fetch-and-tracking/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-clone>

## git-remote-add

**`git remote add`**

**Type:** Subcommand

**Level:** Beginner

**Find by intent:** Manage remotes, Configure Git

**Risk:** State change. Confirm the remote and exact destination ref. Never practice against the guide or a real shared service; do not publish secrets.

**Purpose:** Register a named remote and its default fetch mapping in local configuration.

**Prerequisites:** Use only an owned disposable local remote lab. Verify repository, remote path, refs, status and fictional identity before operating.

**Options:** Supply an unused remote name and URL or path; git remote -v displays configured URLs; -f would also fetch.

**When to use:** When connecting an existing local repository to an owned remote.

**When to avoid:** Avoid embedding credentials in URLs or adding an unverified destination.

**Syntax**

`git remote add origin ../origin.git`

**Basic example**

`git remote add origin ../origin.git`

Connect the current practice repository to a sibling bare repository.

**Professional example**

`git remote add review ../review.git`

Register a second owned lab remote without fetching or publishing.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Changes

**Expected result:** Local configuration contains the remote name, URL and fetch mapping; ordinary add does not contact it.

**Effects and side effects:** Changes local configuration only for the shown form; no objects are transferred or remote refs changed.

**Common errors:** Trying to add an existing origin or assuming adding automatically uploads commits.

**Alternatives:** Use git remote set-url to correct a verified existing remote; inspect git remote get-url first.

**Recovery:** If incorrectly added and unused, verify the name and remove it with git remote remove; removal can also delete associated tracking refs and configuration.

**Version and dependencies:** Standard Git syntax; use Git 2.40 or newer for this guide's labs. Hosted services may require authentication and permissions; these examples use only local paths.

**Related lessons**

- [remote-repositories/01-remote-concepts](../../remote-repositories/01-remote-concepts/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-remote>

## git-fetch

**`git fetch`**

**Type:** Native command

**Level:** Beginner

**Find by intent:** Synchronize repositories, Inspect references

**Risk:** State change. Confirm the remote and exact destination ref. Never practice against the guide or a real shared service; do not publish secrets.

**Purpose:** Obtain remote objects and update local references according to the fetch mapping.

**Prerequisites:** Use only an owned disposable local remote lab. Verify repository, remote path, refs, status and fictional identity before operating.

**Options:** Specify the remote; --prune removes stale destination refs according to refspecs, normally remote-tracking branches; inspect custom mappings first.

**When to use:** When inspecting remote progress before deciding how to integrate it.

**When to avoid:** Avoid unreviewed custom refspecs or assuming fetched code is trustworthy.

**Syntax**

`git fetch origin`

**Basic example**

`git fetch origin`

Update tracking refs from the owned local bare remote.

**Professional example**

`git fetch --prune origin`

With standard branch mapping verified, remove stale tracking refs after approved remote cleanup.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Conditional
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** Ordinary fetch updates configured remote-tracking refs and FETCH\_HEAD as applicable; current local branch and working files normally remain unchanged.

**Effects and side effects:** Can add objects, update refs and run maintenance; the shown ordinary fetch does not integrate into the checked-out branch or update source refs.

**Common errors:** Confusing origin/main with live remote state or assuming fetch updates main itself.

**Alternatives:** Use git pull --ff-only when a verified fast-forward integration is also intended.

**Recovery:** If a fetch updates an unexpected ref, inspect mapping and saved IDs; do not blindly reset. Pruned refs can be fetched again only if available at the source or recovered from retained objects.

**Version and dependencies:** Standard Git syntax; use Git 2.40 or newer for this guide's labs. Hosted services may require authentication and permissions; these examples use only local paths.

**Related lessons**

- [remote-repositories/02-fetch-and-tracking](../../remote-repositories/02-fetch-and-tracking/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-fetch>

## git-pull-ff-only

**`git pull --ff-only`**

**Type:** Option usage

**Level:** Intermediate

**Find by intent:** Synchronize repositories, Integrate changes, Protect history

**Risk:** State change. Confirm the remote and exact destination ref. Never practice against the guide or a real shared service; do not publish secrets.

**Purpose:** Fetch remote changes and integrate only when a fast-forward or already-contained result is possible.

**Prerequisites:** Use only an owned disposable local remote lab. Verify repository, remote path, refs, status and fictional identity before operating.

**Options:** --ff-only rejects divergent integration; explicit remote and branch avoid relying on upstream defaults.

**When to use:** When a clean local branch should advance linearly to its reviewed upstream.

**When to avoid:** Avoid pulling into the wrong branch, with unpreserved edits or when divergence needs a separate decision.

**Syntax**

`git pull --ff-only origin main`

**Basic example**

`git pull --ff-only origin main`

From clean local main in the lab, integrate a known linear remote update.

**Professional example**

`git pull --ff-only origin main`

After inspecting remote progress, enforce linear synchronization of the local lab main.

**State effects**

- Working tree: Conditional
- Index: Conditional
- Objects / refs / history: Conditional
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** Fetch may update tracking refs even if integration refuses; current branch advances only when allowed.

**Effects and side effects:** Can update objects, tracking refs, working tree and index; no remote branch update is inherent.

**Common errors:** Assuming failure means no local state changed, or treating pull as fetch only.

**Alternatives:** Separate git fetch and git merge --ff-only to inspect the incoming commits before integrating.

**Recovery:** If integration refuses, inspect status, tracking refs and divergence; do not force or discard local commits. If an unwanted advance occurred, consult the saved tip and shared-history policy.

**Version and dependencies:** Standard Git syntax; use Git 2.40 or newer for this guide's labs. Hosted services may require authentication and permissions; these examples use only local paths.

**Related lessons**

- [remote-repositories/03-pull-push-and-divergence](../../remote-repositories/03-pull-push-and-divergence/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-pull>

## git-push

**`git push`**

**Type:** Native command

**Level:** Intermediate

**Find by intent:** Synchronize repositories, Manage remotes

**Risk:** Remote change. Confirm the remote and exact destination ref. Never practice against the guide or a real shared service; do not publish secrets.

**Purpose:** Send necessary objects and request updates of specified remote refs.

**Prerequisites:** Use only an owned disposable local remote lab. Verify repository, remote path, refs, status and fictional identity before operating.

**Options:** Specify remote and branch; -u sets upstream for successfully pushed or up-to-date branches; --dry-run previews without updating remote refs.

**When to use:** When publishing reviewed commits to an authorized target branch.

**When to avoid:** Avoid publishing unreviewed commits, secrets or direct changes to protected branches.

**Syntax**

`git push origin feat/notes`

**Basic example**

`git push -u origin feat/notes`

Publish an existing private feature branch to the disposable local remote and configure tracking.

**Professional example**

`git push origin feat/review`

After reviewing committed content, publish only the named feature branch in the lab.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Conditional
- Remote repository: Conditional
- Other state: Conditional

**Expected result:** On acceptance, remote refs reflect the requested updates; ordinary pushes of branches reject non-fast-forward updates unless configured or explicitly overridden.

**Effects and side effects:** May update remote objects and refs, local tracking refs and upstream configuration with -u; trusted hooks may run.

**Common errors:** Expecting push to upload unstaged files, or assuming success proves code quality or grants review approval.

**Alternatives:** Use git push --dry-run with explicit destination for a preview; use a pull request for protected integration.

**Recovery:** If rejected, inspect remote changes and policy. For a mistaken accepted push, coordinate correction; deleting a ref does not guarantee removal of exposed data.

**Version and dependencies:** Standard Git syntax; use Git 2.40 or newer for this guide's labs. Hosted services may require authentication and permissions; these examples use only local paths.

**Related lessons**

- [remote-repositories/03-pull-push-and-divergence](../../remote-repositories/03-pull-push-and-divergence/README.md)
- [remote-repositories/04-remote-branch-lifecycle](../../remote-repositories/04-remote-branch-lifecycle/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-push>

## git-push-delete

**`git push --delete`**

**Type:** Option usage

**Level:** Intermediate

**Find by intent:** Manage remotes, Manage branches, Protect history

**Risk:** Remote change. Confirm the remote and exact destination ref. Never practice against the guide or a real shared service; do not publish secrets.

**Purpose:** Request deletion of a named remote ref, here a remote branch.

**Prerequisites:** Use only an owned disposable local remote lab. Verify repository, remote path, refs, status and fictional identity before operating.

**Options:** --delete marks the named destination ref for deletion; local branch deletion is a separate operation.

**When to use:** When an authorized obsolete remote feature branch has verified retained work and no remaining dependents.

**When to avoid:** Avoid deleting protected, active or unverified refs, or branches with open reviews that still need them.

**Syntax**

`git push origin --delete feat/notes`

**Basic example**

`git push origin --delete feat/notes`

Remove only an obsolete verified feature ref from the local bare lab remote.

**Professional example**

`git push origin --delete feat/review`

After confirming integration, saved tip and no consumers, clean up the disposable remote branch.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Conditional
- Remote repository: Conditional
- Other state: Conditional

**Expected result:** If accepted, named remote ref disappears; local branch remains and tracking refs may need pruning in other clones.

**Effects and side effects:** Changes remote refs and possibly local tracking metadata; objects are not immediately guaranteed to be erased.

**Common errors:** Assuming local branch deletion and remote branch deletion are interchangeable, or deleting before reviewing ancestry and dependencies.

**Alternatives:** Keep the remote branch when unsure; prune stale local tracking refs after authorized server cleanup.

**Recovery:** Record the exact remote tip beforehand. If the object is retained and policy permits, coordinate recreation at the verified ID; recovery is not guaranteed.

**Version and dependencies:** Standard Git syntax; use Git 2.40 or newer for this guide's labs. Hosted services may require authentication and permissions; these examples use only local paths.

**Related lessons**

- [remote-repositories/04-remote-branch-lifecycle](../../remote-repositories/04-remote-branch-lifecycle/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-push>

## git-push-force-with-lease

**`git push --force-with-lease`**

**Type:** Option usage

**Level:** Advanced

**Find by intent:** Rewrite local history, Protect history, Synchronize repositories

**Risk:** Remote change. This is a remote history replacement, not a safe default. A matching lease does not prevent losing changes already present at the expected tip; never bypass project protections.

**Purpose:** Request a non-fast-forward remote update only if the remote ref still matches an explicitly expected value.

**Prerequisites:** Use only an owned disposable local remote lab. Verify repository, remote path, refs, status and fictional identity before operating.

**Options:** Use --force-with-lease=ref:expected with an exact reviewed object ID; the shorthand without an explicit expectation may be affected by background fetches.

**When to use:** Only in an authorized disposable simulation of replacing a private branch after rewriting and reviewing its history.

**When to avoid:** Never use on the guide, protected branches or shared work without explicit agreement; do not retry with a new lease just to defeat a refusal.

**Syntax**

`git push --force-with-lease=refs/heads/feat/notes:EXPECTED origin feat/notes`

**Basic example**

`git push --force-with-lease=refs/heads/feat/notes:EXPECTED origin feat/notes`

In the disposable local lab only, replace EXPECTED with the full previously reviewed remote tip ID after saving it and checking all remote-only commits.

**Professional example**

`git push --force-with-lease=refs/heads/feat/review:EXPECTED origin feat/review`

Simulate a coordinated private rewrite; substitute the saved verified ID, and stop if the lease rejects the update.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Conditional
- Remote repository: Conditional
- Other state: Conditional

**Expected result:** Accepts the requested ref update only if expected old value matches and server policy permits; stale expectation causes refusal.

**Effects and side effects:** Can replace a remote branch tip, transfer objects and update local tracking refs; remote-only commits may become unreachable.

**Common errors:** Treating a matching lease as proof of content safety or assuming it protects every other ref and collaborator.

**Alternatives:** Prefer an ordinary push or follow-up commit preserving history; if a lease fails, fetch and review the remote-only work before any decision.

**Recovery:** Keep a durable ref to the previous remote tip before the simulation. If an incorrect replacement is accepted, coordinate recovery from retained objects and protect new work; restoration is not guaranteed.

**Version and dependencies:** Standard Git syntax; use Git 2.40 or newer for this guide's labs. Hosted services may require authentication and permissions; these examples use only local paths.

**Related lessons**

- [remote-repositories/03-pull-push-and-divergence](../../remote-repositories/03-pull-push-and-divergence/README.md)
- [remote-repositories/04-remote-branch-lifecycle](../../remote-repositories/04-remote-branch-lifecycle/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-push>


---

<!-- navigation-footer -->
[Previous](../07-merge-rebase-and-conflicts/README.md) · [Index](../README.md) · [Next](../09-recovery-and-stash/README.md)
<!-- /navigation-footer -->
