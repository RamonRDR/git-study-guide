# 01 Setup & Configuration

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous module](../../git-internals/README.md) · [Index](../README.md) · [Next](../02-repository-inspection/README.md)
<!-- /navigation -->

Generated from canonical catalog JSON. Edit the records, not this page.

Reference entries describe commands and operations, not a sequence to run. Use disposable repositories for practice. Hosted operations are optional.

**Total distinct entries: 8**

- [`git --version`](#git-version)
- [`git help`](#git-help)
- [`git init`](#git-init)
- [`git init --bare`](#git-init-bare)
- [`git config --local`](#git-config-local)
- [`git config --global`](#git-config-global)
- [`git config --list --show-origin`](#git-config-show-origin)
- [`git config --get`](#git-config-get)

## git-version

**`git --version`**

**Type:** Option usage

**Level:** Beginner

**Find by intent:** Check Git version, Configure Git

**Risk:** Read-only. No repository change; version alone does not guarantee behavior.

**Purpose:** Identify the installed Git executable and its reported version.

**Prerequisites:** Git must be installed and discoverable in the current shell.

**Options:** --version reports the version; it does not update Git.

**When to use:** Check compatibility before following instructions or reporting a bug.

**When to avoid:** Do not treat a version string as proof that a particular optional extension is installed.

**Syntax**

`git --version`

**Basic example**

`git --version`

Run in a fresh terminal and note the version.

**Professional example**

`git --version`

Record the runner's Git version in a CI troubleshooting report without assuming all runners match.

**State effects**

- Working tree: Not applicable
- Index: Not applicable
- Objects / refs / history: Not applicable
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** A version string is printed; no repository is required.

**Effects and side effects:** Reads executable information without changing Git state.

**Common errors:** A missing executable or incorrect PATH prevents invocation; multiple installations may resolve differently.

**Alternatives:** Use the operating system's executable lookup to identify which Git binary is selected.

**Recovery:** No repository recovery is needed; repair installation or PATH if necessary.

**Version and dependencies:** No optional dependency; compare the reported version with the feature's documented minimum.

**Related lessons**

- [getting-started/01-install-git](../../getting-started/01-install-git/README.md)
- [getting-started/02-terminal-and-help](../../getting-started/02-terminal-and-help/README.md)

**Official documentation**

- <https://git-scm.com/docs/git>

## git-help

**`git help`**

**Type:** Native command

**Level:** Beginner

**Find by intent:** Find help, Check Git version

**Risk:** Read-only. The viewer may start a process or open a browser; Git data is not modified.

**Purpose:** Open the help for a Git command or enumerate available commands.

**Prerequisites:** Git installed; detailed help requires an available documentation viewer.

**Options:** -a lists available commands; -w requests web-format help.

**When to use:** Check syntax and documented behavior for an unfamiliar operation.

**When to avoid:** Do not confuse locally installed help with documentation for a different Git release.

**Syntax**

`git help [command]`

**Basic example**

`git help status`

Read the status manual before interpreting its output.

**Professional example**

`git help -a`

List commands on a new development workstation to discover installed extensions.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Displays command documentation or an inventory of commands.

**Effects and side effects:** No repository mutation; the selected viewer or browser may start a process.

**Common errors:** A missing manual viewer or documentation files can prevent the full page from opening.

**Alternatives:** Use git COMMAND -h for short usage or the official versioned online manual.

**Recovery:** Close the viewer; use the short usage or official manual if help is unavailable.

**Version and dependencies:** Viewer availability depends on installation and operating system.

**Related lessons**

- [getting-started/02-terminal-and-help](../../getting-started/02-terminal-and-help/README.md)
- [basic-commands/01-init-config-help](../../basic-commands/01-init-config-help/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-help>

## git-init

**`git init`**

**Type:** Native command

**Level:** Beginner

**Find by intent:** Create a repository, Configure Git

**Risk:** State change. Creates repository metadata; verify the target path first.

**Purpose:** Create a local Git repository, or reinitialize an existing one.

**Prerequisites:** Writable, owned directory or a writable parent for a new directory.

**Options:** -b selects the initial branch name; an optional directory selects the target.

**When to use:** Start tracking a new local project without a remote.

**When to avoid:** Do not initialize the wrong directory or create an unintended nested repository.

**Syntax**

`git init [-b branch] [directory]`

**Basic example**

`git init -b main notes-lab`

From an owned disposable parent, create a notes repository on main.

**Professional example**

`git init -b main prototype-lab`

Create a separate prototype repository instead of initializing an existing application directory by accident.

**State effects**

- Working tree: Conditional
- Index: Unchanged
- Objects / refs / history: Changes
- Remote repository: Unchanged
- Other state: Changes

**Expected result:** In a new repository, metadata exists and HEAD names an unborn branch; no commit is created.

**Effects and side effects:** May create the directory and metadata; files are not staged automatically.

**Common errors:** Initializing a parent or nested directory unintentionally makes repository boundaries confusing.

**Alternatives:** Use git clone when you need an existing repository and its history.

**Recovery:** Inspect the path and back up data; do not remove metadata unless you have verified the repository is disposable and its history is unnecessary.

**Version and dependencies:** -b / --initial-branch requires Git 2.28 or later.

**Related lessons**

- [getting-started/03-first-repository](../../getting-started/03-first-repository/README.md)
- [basic-commands/01-init-config-help](../../basic-commands/01-init-config-help/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-init>
- <https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup>

## git-init-bare

**`git init --bare`**

**Type:** Option usage

**Level:** Intermediate

**Find by intent:** Create a repository, Simulate collaboration

**Risk:** State change. A bare origin can hold valuable history; never delete it simply because no files are checked out.

**Purpose:** Initialize a repository without a checked-out working tree, suitable as a local shared origin.

**Prerequisites:** Writable disposable target directory; choose an initial branch name deliberately.

**Options:** --bare creates bare metadata layout; -b chooses the initial branch.

**When to use:** Create a local origin for a two-clone collaboration exercise.

**When to avoid:** Do not use it as the normal repository where you intend to edit and stage files.

**Syntax**

`git init --bare [-b branch] [directory]`

**Basic example**

`git init --bare -b main origin.git`

Create a local bare origin in a disposable parent directory.

**Professional example**

`git init --bare -b main collaboration.git`

Use a local bare origin to rehearse push and fetch with two separate clones without a hosting account.

**State effects**

- Working tree: Not applicable
- Index: Not applicable
- Objects / refs / history: Changes
- Remote repository: Unchanged
- Other state: Changes

**Expected result:** The bare repository exists; HEAD is symbolic and initially has no commit.

**Effects and side effects:** No working tree or ordinary staging workflow is created; refs and objects live in the repository directory.

**Common errors:** Running working-tree commands in a bare repository fails or does not make sense.

**Alternatives:** Use ordinary git init for an editing repository; clone the bare origin to work on files.

**Recovery:** Keep existing refs and objects safe; remove only a verified disposable origin after all participants finish.

**Version and dependencies:** -b requires Git 2.28 or later; no hosted service needed.

**Related lessons**

- [remote-repositories/01-remote-concepts](../../remote-repositories/01-remote-concepts/README.md)
- [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-init>
- <https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup>

## git-config-local

**`git config --local`**

**Type:** Option usage

**Level:** Beginner

**Find by intent:** Configure Git, Configure identity

**Risk:** State change. Configuration can affect future commits or execution behavior; use fictitious identity only in labs.

**Purpose:** Set a repository-local configuration value, such as commit identity.

**Prerequisites:** An owned repository and a clear reason for the setting; inspect existing values first.

**Options:** --local targets repository configuration; --get reads a value; --unset removes a single-valued key.

**When to use:** Choose a project-specific identity or behavior without changing other repositories.

**When to avoid:** Do not store access tokens or private keys in ordinary configuration values.

**Syntax**

`git config --local name value`

**Basic example**

`git config --local user.name "Alice Example"`

In a disposable repository, set a fictional local author name.

**Professional example**

`git config --local user.email alice@example.invalid`

Set a fictional email in a disposable project to separate its commit identity from the normal workstation identity.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Changes

**Expected result:** The specified key has the requested local value; future operations may use it.

**Effects and side effects:** Changes configuration, not existing commits or staged files; identity applies to future commits.

**Common errors:** Using --global by accident affects other repositories; a missing repository prevents --local.

**Alternatives:** Use command-scoped git -c for a one-off override or --global for an intentional user default.

**Recovery:** Restore the prior local value or unset the key only if it was previously absent; inspect effective configuration afterward.

**Version and dependencies:** No optional dependency; examples use the long-standing name/value form.

**Related lessons**

- [getting-started/03-first-repository](../../getting-started/03-first-repository/README.md)
- [basic-commands/01-init-config-help](../../basic-commands/01-init-config-help/README.md)
- [security/09-commit-and-tag-signing](../../security/09-commit-and-tag-signing/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-config>

## git-config-global

**`git config --global`**

**Type:** Option usage

**Level:** Beginner

**Find by intent:** Configure Git, Configure identity

**Risk:** State change. User-wide change; the write example is for an isolated disposable home only.

**Purpose:** Read or set user-level Git configuration shared across repositories.

**Prerequisites:** A user account under your control; for write practice isolate the home/config path first.

**Options:** --global selects the user scope; --get reads rather than writes; --unset removes a single-valued key.

**When to use:** Inspect user defaults or intentionally establish a user-wide preference.

**When to avoid:** Avoid writing fictional lab identity to your normal global configuration or changing a managed/shared machine.

**Syntax**

`git config --global name value`

**Basic example**

`git config --global --get user.name`

Inspect the global author name without changing it; an absent value may return a nonzero status.

**Professional example**

`git config --global user.name "Alice Example"`

Only in a separately isolated lab home/config, set a fictional user-wide identity to compare with a local override.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Conditional

**Expected result:** A read reports the configured value if present; a write updates user configuration, subject to higher-precedence overrides.

**Effects and side effects:** May affect future operations across repositories; existing commit objects are unchanged.

**Common errors:** Confusing global scope with a repository-specific override can create surprising identity or behavior.

**Alternatives:** Use git config --local for project-specific settings or git -c for one invocation.

**Recovery:** Record the previous value before changing it; restore it or remove only a newly introduced key. Verify scope and effective value.

**Version and dependencies:** No optional dependency; global file location depends on Git and environment configuration.

**Related lessons**

- [getting-started/03-first-repository](../../getting-started/03-first-repository/README.md)
- [basic-commands/01-init-config-help](../../basic-commands/01-init-config-help/README.md)
- [security/05-secrets-and-disclosure-prevention](../../security/05-secrets-and-disclosure-prevention/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-config>

## git-config-show-origin

**`git config --list --show-origin`**

**Type:** Option usage

**Level:** Intermediate

**Find by intent:** Inspect configuration, Troubleshoot configuration

**Risk:** Sensitive. Sensitive output; review and redact before sharing.

**Purpose:** Inspect configuration entries together with where they came from.

**Prerequisites:** Git installed; run inside a repository to include its relevant local settings.

**Options:** --list enumerates entries; --show-origin reports origin; --show-scope adds scope information.

**When to use:** Diagnose conflicting user and repository settings before changing anything.

**When to avoid:** Do not paste the raw listing into public issues or logs; values and paths may be sensitive.

**Syntax**

`git config --list --show-origin [--show-scope]`

**Basic example**

`git config --list --show-origin`

Inspect configuration origins privately in a disposable repository.

**Professional example**

`git config --list --show-origin --show-scope`

Diagnose which scope supplies an unexpected identity without exposing the full listing in a ticket.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Prints configuration entries with their origin and optionally scope; repeated keys may appear.

**Effects and side effects:** No Git data changes, but output can expose personal paths, identity or sensitive configuration.

**Common errors:** Assuming the first printed value always wins ignores precedence and multi-valued settings.

**Alternatives:** Use git config --get for a single key or restrict inspection with --local or --global.

**Recovery:** No Git recovery needed; if secrets were disclosed, follow the credential incident procedure.

**Version and dependencies:** --show-origin available since Git 2.8; --show-scope since Git 2.26.

**Related lessons**

- [basic-commands/01-init-config-help](../../basic-commands/01-init-config-help/README.md)
- [security/05-secrets-and-disclosure-prevention](../../security/05-secrets-and-disclosure-prevention/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-config>
- <https://git-scm.com/docs/git-config/2.8.6>
- <https://git-scm.com/docs/git-config/2.26.0>

## git-config-get

**`git config --get`**

**Type:** Option usage

**Level:** Beginner

**Find by intent:** Inspect configuration, Configure identity

**Risk:** Sensitive. A specific query limits disclosure relative to a full list, but still review output.

**Purpose:** Query a particular Git configuration key without modifying it.

**Prerequisites:** Git installed; a repository is required for --local.

**Options:** --get reads a value; --get-all retrieves multiple values; scope options restrict the query.

**When to use:** Check the effective identity or inspect a specific key before changing it.

**When to avoid:** Do not query or share sensitive configuration values unnecessarily.

**Syntax**

`git config [--local|--global] --get name`

**Basic example**

`git config --get user.name`

Read the effective author name in a disposable repository.

**Professional example**

`git config --local --get user.email`

Verify whether a project has a local author email before a first commit; do not publish the real address.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Prints a value if found; a missing key produces a nonzero exit status.

**Effects and side effects:** No repository mutation; queried values can contain personal or sensitive information.

**Common errors:** Assuming a missing key is an empty configured value or treating nonzero status as an unrelated failure.

**Alternatives:** Use --get-all for multivalued keys or --list --show-origin to investigate origin.

**Recovery:** No repository recovery; check the key spelling and selected scope if not found.

**Version and dependencies:** No optional dependency; use the legacy --get syntax for broad Git compatibility.

**Related lessons**

- [basic-commands/01-init-config-help](../../basic-commands/01-init-config-help/README.md)
- [remote-repositories/05-secure-authentication](../../remote-repositories/05-secure-authentication/README.md)

**Official documentation**

- <https://git-scm.com/docs/git-config>


---

<!-- navigation-footer -->
[Previous module](../../git-internals/README.md) · [Index](../README.md) · [Next](../02-repository-inspection/README.md)
<!-- /navigation-footer -->
