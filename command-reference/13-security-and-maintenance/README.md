# 13 Security & Maintenance

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../12-internals-and-plumbing/README.md) · [Index](../README.md) · [Next](../14-platforms-and-automation/README.md)
<!-- /navigation -->

Generated from canonical catalog JSON. Edit the records, not this page.

Reference entries describe commands and operations, not a sequence to run. Use disposable repositories for practice. Hosted operations are optional.

**Total distinct entries: 8**

- [`git commit -S`](#git-commit-sign)
- [`git tag -s`](#git-tag-sign)
- [`git verify-commit`](#git-verify-commit)
- [`git verify-tag`](#git-verify-tag)
- [`git credential reject`](#git-credential-reject)
- [`git fsck`](#git-fsck)
- [`git gc`](#git-gc)
- [`git maintenance run`](#git-maintenance-run)

## git-commit-sign

**`git commit -S`**

**Type:** Option usage

**Level:** Intermediate

**Find by intent:** Commit changes, Verify signatures

**Risk:** State change. Protect signing keys; never place private key material in tracked files.

**Purpose:** Create a cryptographically signed commit.

**Prerequisites:** Use an owned complete disposable repository, verified refs, saved work and trusted configuration. Never use real credentials or personal keys in labs.

**Options:** -S requests signing; an optional key ID attaches to the short option. Lowercase -s adds a sign-off trailer instead.

**When to use:** When signed commits are required by policy.

**When to avoid:** Avoid signing unreviewed changes or using unauthorized keys.

**Syntax**

`git commit -S -m "Signed notes"`

**Basic example**

`git commit -S -m "Signed notes"`

Record reviewed staged lab content with the configured disposable key.

**Professional example**

`git commit -S -m "docs: review notes"`

Record a signed private documentation commit.

**State effects**

- Working tree: Conditional
- Index: Conditional
- Objects / refs / history: Changes
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** Successful commit embeds a signature and advances the selected ref; signing failure can prevent creation.

**Effects and side effects:** Creates signed commit object and updates ref; signing tools and hooks may change local state. No push occurs.

**Common errors:** Confusing -S with sign-off or assuming signatures prove code quality.

**Alternatives:** Use ordinary commit only if policy permits; check signed commits with git verify-commit.

**Recovery:** Check signing configuration and key availability before retrying; verify resulting commit before sharing.

**Version and dependencies:** Requires a configured signing or verification backend, such as GnuPG or OpenSSH with SSH signing support, appropriate keys and trust configuration. Use disposable lab keys.

**Related lessons**

- [security/09-commit-and-tag-signing](../../security/09-commit-and-tag-signing/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-commit>

## git-tag-sign

**`git tag -s`**

**Type:** Option usage

**Level:** Intermediate

**Find by intent:** Manage tags, Verify signatures

**Risk:** State change. Verify target and signer; never overwrite published version tags to conceal a mistake.

**Purpose:** Create a signed annotated tag and its local ref.

**Prerequisites:** Use an owned complete disposable repository, verified refs, saved work and trusted configuration. Never use real credentials or personal keys in labs.

**Options:** -s requests signing; -m supplies message; an optional final object names the target.

**When to use:** When marking a reviewed revision under a release signing policy.

**When to avoid:** Avoid guessed targets or moving published version tags.

**Syntax**

`git tag -s v1.0.0 -m "Practice release"`

**Basic example**

`git tag -s v1.0.0 -m "Practice release"`

Sign an unused version tag at verified HEAD.

**Professional example**

`git tag -s v1.1.0 -m "Reviewed release" main`

Sign an unused version tag at reviewed local main.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Changes
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** Creates signed tag object and local ref; does not publish a release or sign its target commit.

**Effects and side effects:** Adds tag object and ref; backend may change local metadata; branch tip stays unchanged.

**Common errors:** Assuming signed tag also verifies every artifact or commit.

**Alternatives:** Use annotated unsigned tag only when policy allows; verify with git verify-tag.

**Recovery:** If a private tag is incorrect, record its ID and review deletion before replacement; follow release correction policy for published tags.

**Version and dependencies:** Requires a configured signing or verification backend, such as GnuPG or OpenSSH with SSH signing support, appropriate keys and trust configuration. Use disposable lab keys.

**Related lessons**

- [security/09-commit-and-tag-signing](../../security/09-commit-and-tag-signing/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-tag>

## git-verify-commit

**`git verify-commit`**

**Type:** Native command

**Level:** Intermediate

**Find by intent:** Verify signatures

**Risk:** State change. A signature does not establish code safety or review approval. Protect private keys; verify exact object and signer trust independently.

**Purpose:** Verify the cryptographic signature of a selected commit using the configured backend.

**Prerequisites:** Use an owned complete disposable repository, verified refs, saved work and trusted configuration. Never use real credentials or personal keys in labs.

**Options:** Supply commit refs or IDs; --verbose displays commit content before verification output.

**When to use:** When checking a signed commit against trusted identity policy.

**When to avoid:** Do not accept a signature as proof of safe code or review approval.

**Syntax**

`git verify-commit HEAD`

**Basic example**

`git verify-commit HEAD`

Verify an existing signed practice commit.

**Professional example**

`git verify-commit main`

Verify signed lab main against configured trust policy.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** Reports verification result; failure returns nonzero and trust configuration affects acceptance.

**Effects and side effects:** Does not change Git refs or files; an external verification backend may update its own metadata.

**Common errors:** Checking a cryptographic result while ignoring trusted signer policy.

**Alternatives:** Use git log --show-signature for context; still enforce exact ID and verification status.

**Recovery:** On failure, inspect status, selected object, backend and key or trust configuration; do not bypass required signing or verification.

**Version and dependencies:** Requires a configured signing or verification backend, such as GnuPG or OpenSSH with SSH signing support, appropriate keys and trust configuration. Use disposable lab keys.

**Related lessons**

- [security/09-commit-and-tag-signing](../../security/09-commit-and-tag-signing/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-verify-commit>

## git-verify-tag

**`git verify-tag`**

**Type:** Native command

**Level:** Intermediate

**Find by intent:** Verify signatures, Manage tags

**Risk:** State change. A signature does not establish code safety or review approval. Protect private keys; verify exact object and signer trust independently.

**Purpose:** Verify the signature of a signed tag object.

**Prerequisites:** Use an owned complete disposable repository, verified refs, saved work and trusted configuration. Never use real credentials or personal keys in labs.

**Options:** Supply signed tag names or tag object IDs; --verbose displays tag content.

**When to use:** When checking signed release markers under a trust policy.

**When to avoid:** Do not expect lightweight tags to contain signatures or trust unrelated artifacts automatically.

**Syntax**

`git verify-tag v1.0.0`

**Basic example**

`git verify-tag v1.0.0`

Verify an existing signed annotated lab tag.

**Professional example**

`git verify-tag v1.1.0`

Verify a version marker before reviewing its target and artifacts.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** Reports verification result; trust configuration affects acceptance.

**Effects and side effects:** Does not move refs or edit tracked files; verification backend may modify its own metadata.

**Common errors:** Verifying a tag name without checking exact target or treating it as verification of the target commit signature.

**Alternatives:** Use git verify-commit separately when needed and review artifact provenance independently.

**Recovery:** On failure, inspect status, selected object, backend and key or trust configuration; do not bypass required signing or verification.

**Version and dependencies:** Requires a configured signing or verification backend, such as GnuPG or OpenSSH with SSH signing support, appropriate keys and trust configuration. Use disposable lab keys.

**Related lessons**

- [security/09-commit-and-tag-signing](../../security/09-commit-and-tag-signing/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-verify-tag>

## git-credential-reject

**`git credential reject`**

**Type:** Subcommand

**Level:** Advanced

**Find by intent:** Authenticate safely, Troubleshoot configuration

**Risk:** Sensitive. May erase multiple matching accounts; use only a mock helper and fictional identifiers in labs.

**Purpose:** Request that configured credential helpers erase matching stored credentials.

**Prerequisites:** Isolate Git configuration, disable inherited helpers and use only a mock helper recording erase events without real credentials.

**Options:** Reads key=value lines terminated by a blank line; matching depends on helper and supplied fields.

**When to use:** When rehearsing removal of a stale local authentication entry.

**When to avoid:** Avoid broad matching, unknown helpers and real credentials in practice.

**Syntax**

`git credential reject`

**Basic example**

`git credential reject`

With only a mock helper, enter protocol=https, host=example.invalid, username=student on separate lines, then a blank line.

**Professional example**

`git credential reject`

Repeat with fictional identifiers in the mock lab and inspect the erase event.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** Configured helpers receive an erase request; removal depends on helper behavior. Server token validity is unchanged.

**Effects and side effects:** May remove local credential records; does not revoke provider tokens or change Git history.

**Common errors:** Confusing local erasure with server-side token revocation.

**Alternatives:** Use provider's official revocation and rotation process for actual exposure.

**Recovery:** If a needed local record was removed, reauthenticate through approved workflow. Never restore an exposed token.

**Version and dependencies:** Use Git 2.40 or newer for guide labs; check local configuration and command availability.

**Related lessons**

- [security/04-credential-managers](../../security/04-credential-managers/README.md)
- [security/11-credential-exposure-and-incident-response](../../security/11-credential-exposure-and-incident-response/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-credential>

## git-fsck

**`git fsck`**

**Type:** Native command

**Level:** Advanced

**Find by intent:** Verify integrity, Inspect Git objects

**Risk:** Read-only. Read-only for shown forms; integrity success is not evidence of application correctness.

**Purpose:** Check object validity and connectivity.

**Prerequisites:** Use an owned complete disposable repository, verified refs, saved work and trusted configuration. Never use real credentials or personal keys in labs.

**Options:** --full includes packed objects and alternates; --strict applies stricter checks; --lost-found writes files and is not used here.

**When to use:** When investigating integrity or reviewing a complete copy before maintenance.

**When to avoid:** Do not treat dangling objects alone as corruption or rely on fsck as backup.

**Syntax**

`git fsck --full`

**Basic example**

`git fsck --full`

Inspect connectivity and validity in a complete local practice repository.

**Professional example**

`git fsck --full --strict`

Run stricter integrity inspection before maintenance.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Reports detected integrity findings and may list dangling objects.

**Effects and side effects:** Shown forms inspect a complete local repository without intentionally changing objects, refs or files.

**Common errors:** Running cleanup after corruption and losing potentially recoverable data.

**Alternatives:** Use git count-objects for storage statistics; repair from verified backups or healthy copies.

**Recovery:** Stop writes on serious errors, preserve a copy and investigate before repair.

**Version and dependencies:** Use Git 2.40 or newer for guide labs; check local configuration and command availability.

**Related lessons**

- [git-internals/07-loose-objects-and-packfiles](../../git-internals/07-loose-objects-and-packfiles/README.md)
- [git-internals/08-gc-and-maintenance](../../git-internals/08-gc-and-maintenance/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-fsck>

## git-gc

**`git gc`**

**Type:** Native command

**Level:** Advanced

**Find by intent:** Maintain a repository, Protect history

**Risk:** Destructive. Cleanup may permanently remove unreachable work. Preserve recovery refs and backups before running.

**Purpose:** Perform housekeeping such as packing and configured expiration of repository data.

**Prerequisites:** Use an owned complete disposable repository, verified refs, saved work and trusted configuration. Never use real credentials or personal keys in labs.

**Options:** --auto checks whether needed; --no-prune avoids ordinary prune step; do not use --prune=now in labs.

**When to use:** When healthy local repository requires maintenance under reviewed retention settings.

**When to avoid:** Avoid concurrent writes, recovery investigations or unpreserved unreachable work.

**Syntax**

`git gc`

**Basic example**

`git gc`

In an idle disposable repository with saved recovery refs, run ordinary housekeeping.

**Professional example**

`git gc --no-prune`

Skip ordinary prune step; review other expiration settings too.

**State effects**

- Working tree: Unchanged
- Index: Conditional
- Objects / refs / history: Conditional
- Remote repository: Unchanged
- Other state: Changes

**Expected result:** May consolidate objects and refs, expire reflogs and remove eligible unreachable data.

**Effects and side effects:** Changes object storage and maintenance metadata; does not intentionally rewrite branch tips or publish changes.

**Common errors:** Assuming --no-prune preserves all recovery data or gc repairs corrupted objects.

**Alternatives:** Use a narrowly scoped git maintenance run task when appropriate.

**Recovery:** Verify refs and integrity after maintenance; recover missing required objects from verified backups if possible.

**Version and dependencies:** Use Git 2.40 or newer for guide labs; check local configuration and command availability.

**Related lessons**

- [git-internals/08-gc-and-maintenance](../../git-internals/08-gc-and-maintenance/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-gc>

## git-maintenance-run

**`git maintenance run`**

**Type:** Subcommand

**Level:** Advanced

**Find by intent:** Maintain a repository

**Risk:** State change. Select tasks deliberately; do not assume arbitrary maintenance is free of destructive or network effects.

**Purpose:** Run explicitly selected repository maintenance tasks.

**Prerequisites:** Use an owned complete disposable repository, verified refs, saved work and trusted configuration. Never use real credentials or personal keys in labs.

**Options:** --task=commit-graph selects graph maintenance; --auto may run configured needed tasks. Other tasks have different effects.

**When to use:** When updating local acceleration metadata with a targeted task.

**When to avoid:** Avoid unreviewed broad tasks or global scheduling in shared environments.

**Syntax**

`git maintenance run --task=commit-graph`

**Basic example**

`git maintenance run --task=commit-graph`

Run only commit-graph maintenance in an idle practice repository.

**Professional example**

`git maintenance run --task=commit-graph`

Update graph metadata and inspect it afterward.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Changes

**Expected result:** Selected task updates commit-graph metadata as needed without changing branch tips.

**Effects and side effects:** Shown task writes graph metadata; other tasks may change storage or contact remotes.

**Common errors:** Assuming run establishes a persistent schedule or every maintenance task is read-only.

**Alternatives:** Use git commit-graph verify to inspect graph validity.

**Recovery:** Inspect failure and repository integrity; retry only scoped task after addressing cause.

**Version and dependencies:** Use Git 2.40 or newer for guide labs; check local configuration and command availability.

**Related lessons**

- [git-internals/08-gc-and-maintenance](../../git-internals/08-gc-and-maintenance/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-maintenance>


---

<!-- navigation-footer -->
[Previous](../12-internals-and-plumbing/README.md) · [Index](../README.md) · [Next](../14-platforms-and-automation/README.md)
<!-- /navigation-footer -->
