# 14 Platforms & Automation

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../13-security-and-maintenance/README.md) · [Index](../README.md) · [Next module](../../practical-projects/README.md)
<!-- /navigation -->

Generated from canonical catalog JSON. Edit the records, not this page.

Reference entries describe commands and operations, not a sequence to run. Use disposable repositories for practice. Hosted operations are optional.

**Total distinct entries: 8**

- [`gh pr create`](#gh-pr-create)
- [`gh pr view`](#gh-pr-view)
- [`gh pr checks`](#gh-pr-checks)
- [`gh run view`](#gh-run-view)
- [`gh release create`](#gh-release-create)
- [`glab mr create`](#glab-mr-create)
- [`glab mr view`](#glab-mr-view)
- [`glab ci status`](#glab-ci-status)

## gh-pr-create

**`gh pr create`**

**Type:** External tool

**Level:** Intermediate

**Find by intent:** Review changes, Automate workflow

**Risk:** Remote change. Creates platform state and may notify people or trigger automation. Do not execute fictional examples against real repositories; require authorization and verify the destination.

**Purpose:** Create a GitHub pull request for a proposed branch integration.

**Prerequisites:** Examples are fictional templates, not live exercises. Substitute only an explicitly authorized sandbox repository, verified account, refs and IDs. Inspect the CLI version and authentication first.

**Options:** --base and --head identify refs; --draft opens a draft; explicit --head avoids implicit forking or pushing behavior. --dry-run can still push Git changes.

**When to use:** When an authorized published feature branch is ready for review or draft feedback.

**When to avoid:** Avoid wrong repository, unreviewed sensitive content or bypassing required review gates.

**Syntax**

`gh pr create -R example-org/example-repo --base main --head feat/notes --title "Review notes" --body "Fictional review" --draft`

**Basic example**

`gh pr create -R example-org/example-repo --base main --head feat/notes --title "Review notes" --body "Fictional review" --draft`

Illustrate opening a draft from an already published authorized branch; substitute the sandbox repository only.

**Professional example**

`gh pr create -R example-org/example-repo --base main --head feat/docs --title "Review documentation" --body "Describe changes and test evidence"`

Illustrate a review request for reviewed committed changes with explicit head and base.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Conditional
- Other state: Conditional

**Expected result:** Returns the created PR URL on success; creation alone does not merge the branch.

**Effects and side effects:** Creates remote PR metadata and may trigger CI or notifications. Shown explicit head requires an already published branch; implicit forms can push or fork.

**Common errors:** Confusing PR creation with merge approval or expecting a dry run to guarantee no network writes.

**Alternatives:** Use the platform web interface to inspect and create the authorized review request manually.

**Recovery:** Inspect the created URL and exact refs; if incorrect, coordinate correction or close the mistaken PR with authorization. Closing does not erase its history.

**Version and dependencies:** Requires a current compatible GitHub CLI (gh), authorized authentication, network access and relevant repository permissions. Check gh help for installed flags.

**Related lessons**

- [github/04-pull-requests-and-review](../../github/04-pull-requests-and-review/README.md)
- [github/08-github-cli](../../github/08-github-cli/README.md)

**Official documentation**

- <https://cli.github.com/manual/gh_pr_create>

## gh-pr-view

**`gh pr view`**

**Type:** External tool

**Level:** Intermediate

**Find by intent:** Review changes, Inspect repository state

**Risk:** Read-only. Inspection is not approval to merge. Protect private metadata and logs; do not expose credentials.

**Purpose:** Inspect a GitHub pull request and its review or merge metadata.

**Prerequisites:** Examples are fictional templates, not live exercises. Substitute only an explicitly authorized sandbox repository, verified account, refs and IDs. Inspect the CLI version and authentication first.

**Options:** --json selects fields; --comments displays comments and reviews; --web opens the page.

**When to use:** When checking the exact PR and head under review.

**When to avoid:** Do not infer that a merge is authorized from a mergeability field alone.

**Syntax**

`gh pr view 42 -R example-org/example-repo`

**Basic example**

`gh pr view 42 -R example-org/example-repo`

Inspect fictional PR number 42 in an authorized sandbox template.

**Professional example**

`gh pr view 42 -R example-org/example-repo --json headRefOid,reviewDecision,mergeStateStatus`

Inspect the exact head and review state, then verify required checks independently.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Displays a snapshot of the selected PR metadata; platform calculation and review status may change.

**Effects and side effects:** Reads platform metadata over the network; does not intentionally alter Git refs, index, checkout or platform resources in the shown form.

**Common errors:** Reading a prior head's approval as approval of newly pushed changes.

**Alternatives:** Use the web interface and gh pr checks to inspect checks and review discussion.

**Recovery:** No undo is needed for inspection. Verify repository, ID, permissions and exact commit association; refresh status if incomplete or stale.

**Version and dependencies:** Requires a current compatible GitHub CLI (gh), authorized authentication, network access and relevant repository permissions. Check gh help for installed flags.

**Related lessons**

- [github/04-pull-requests-and-review](../../github/04-pull-requests-and-review/README.md)
- [github/08-github-cli](../../github/08-github-cli/README.md)

**Official documentation**

- <https://cli.github.com/manual/gh_pr_view>

## gh-pr-checks

**`gh pr checks`**

**Type:** External tool

**Level:** Intermediate

**Find by intent:** Inspect CI, Review changes

**Risk:** Read-only. Inspection is not approval to merge. Protect private metadata and logs; do not expose credentials.

**Purpose:** Inspect CI check results associated with a GitHub pull request.

**Prerequisites:** Examples are fictional templates, not live exercises. Substitute only an explicitly authorized sandbox repository, verified account, refs and IDs. Inspect the CLI version and authentication first.

**Options:** --required restricts output to required checks; --watch waits for updates; pending checks have a distinct exit status in current CLI.

**When to use:** When determining whether required checks have completed for the reviewed change.

**When to avoid:** Avoid declaring success from incomplete, missing or stale check results.

**Syntax**

`gh pr checks 42 -R example-org/example-repo`

**Basic example**

`gh pr checks 42 -R example-org/example-repo`

Inspect checks of a fictional authorized sandbox PR.

**Professional example**

`gh pr checks 42 -R example-org/example-repo --required`

Inspect required checks and confirm they correspond to the latest reviewed head.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Displays reported check statuses; nonzero may indicate pending or failed checks, depending on exit status.

**Effects and side effects:** Reads platform metadata over the network; does not intentionally alter Git refs, index, checkout or platform resources in the shown form.

**Common errors:** Treating no reported checks or old successful checks as a current green gate.

**Alternatives:** Inspect the PR head and individual workflow runs, including required checks and logs.

**Recovery:** No undo is needed for inspection. Verify repository, ID, permissions and exact commit association; refresh status if incomplete or stale.

**Version and dependencies:** Requires a current compatible GitHub CLI (gh), authorized authentication, network access and relevant repository permissions. Check gh help for installed flags.

**Related lessons**

- [github/04-pull-requests-and-review](../../github/04-pull-requests-and-review/README.md)
- [ci-cd/09-quality-gates-and-troubleshooting](../../ci-cd/09-quality-gates-and-troubleshooting/README.md)

**Official documentation**

- <https://cli.github.com/manual/gh_pr_checks>

## gh-run-view

**`gh run view`**

**Type:** External tool

**Level:** Intermediate

**Find by intent:** Inspect CI

**Risk:** Read-only. Inspection is not approval to merge. Protect private metadata and logs; do not expose credentials.

**Purpose:** Inspect a particular GitHub Actions workflow run and its available job information.

**Prerequisites:** Examples are fictional templates, not live exercises. Substitute only an explicitly authorized sandbox repository, verified account, refs and IDs. Inspect the CLI version and authentication first.

**Options:** --log-failed requests failed-step logs; --exit-status returns nonzero for failed run; run ID is not a PR number.

**When to use:** When troubleshooting an identified workflow attempt for a specific commit.

**When to avoid:** Do not assume a successful unrelated run proves required checks passed.

**Syntax**

`gh run view 123456 -R example-org/example-repo`

**Basic example**

`gh run view 123456 -R example-org/example-repo`

Inspect a fictional workflow run ID in a sandbox template.

**Professional example**

`gh run view 123456 -R example-org/example-repo --log-failed`

Inspect failed-step logs without publishing sensitive output.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Returns available run details or logs; incomplete runs and expired logs may not provide final evidence.

**Effects and side effects:** Reads platform metadata over the network; does not intentionally alter Git refs, index, checkout or platform resources in the shown form.

**Common errors:** Confusing run ID, job ID and PR number or ignoring run attempt and head SHA.

**Alternatives:** Use gh pr checks for PR-level checks and the Actions web interface for full attempt context.

**Recovery:** No undo is needed for inspection. Verify repository, ID, permissions and exact commit association; refresh status if incomplete or stale.

**Version and dependencies:** Requires a current compatible GitHub CLI (gh), authorized authentication, network access and relevant repository permissions. Check gh help for installed flags.

**Related lessons**

- [ci-cd/03-github-actions](../../ci-cd/03-github-actions/README.md)
- [ci-cd/09-quality-gates-and-troubleshooting](../../ci-cd/09-quality-gates-and-troubleshooting/README.md)

**Official documentation**

- <https://cli.github.com/manual/gh_run_view>

## gh-release-create

**`gh release create`**

**Type:** External tool

**Level:** Advanced

**Find by intent:** Manage releases, Manage tags

**Risk:** Remote change. Creates platform state and may notify people or trigger automation. Do not execute fictional examples against real repositories; require authorization and verify the destination.

**Purpose:** Create release metadata associated with a GitHub tag, optionally as a draft.

**Prerequisites:** Examples are fictional templates, not live exercises. Substitute only an explicitly authorized sandbox repository, verified account, refs and IDs. Inspect the CLI version and authentication first.

**Options:** --verify-tag requires an existing remote tag; without it the CLI can create a missing tag. --draft delays publication; --notes-file supplies release notes.

**When to use:** When preparing an authorized reviewed release after verifying its version tag.

**When to avoid:** Avoid unverified targets, missing approval, sensitive assets or implicit tag creation.

**Syntax**

`gh release create v1.0.0 -R example-org/example-repo --verify-tag --draft --title "Practice release" --notes "Fictional release notes"`

**Basic example**

`gh release create v1.0.0 -R example-org/example-repo --verify-tag --draft --title "Practice release" --notes "Fictional release notes"`

Illustrate a draft using an existing authorized remote tag in a sandbox.

**Professional example**

`gh release create v1.1.0 -R example-org/example-repo --verify-tag --draft --notes-file release-notes.md`

Prepare a draft only after reviewing the existing tag, notes file and release policy.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Conditional
- Other state: Conditional

**Expected result:** Creates a draft release for the existing remote tag in the shown forms; publication requires a separate action.

**Effects and side effects:** Writes remote draft release metadata; the shown --verify-tag form requires an existing tag and does not create it. Other forms can create tags or publish assets.

**Common errors:** Confusing tag verification of existence with cryptographic signature verification or publishing before approvals.

**Alternatives:** Use the Releases web interface for manual draft preparation and review; verify signatures and artifacts separately.

**Recovery:** Inspect the created draft and associated tag. Coordinate authorized edits or removal of the draft if incorrect; do not rewrite a published tag.

**Version and dependencies:** Requires a current compatible GitHub CLI (gh), authorized authentication, network access and relevant repository permissions. Check gh help for installed flags.

**Related lessons**

- [github/07-tags-and-releases](../../github/07-tags-and-releases/README.md)
- [professional-workflows/12-release-management](../../professional-workflows/12-release-management/README.md)

**Official documentation**

- <https://cli.github.com/manual/gh_release_create>

## glab-mr-create

**`glab mr create`**

**Type:** External tool

**Level:** Intermediate

**Find by intent:** Review changes, Automate workflow

**Risk:** Remote change. Creates platform state and may notify people or trigger automation. Do not execute fictional examples against real repositories; require authorization and verify the destination.

**Purpose:** Open a GitLab merge request for a proposed integration.

**Prerequisites:** Examples are fictional templates, not live exercises. Substitute only an explicitly authorized sandbox repository, verified account, refs and IDs. Inspect the CLI version and authentication first.

**Options:** --source-branch and --target-branch select branches; --draft creates a draft; --push can publish local commits and is omitted here.

**When to use:** When an authorized published source branch is ready for review.

**When to avoid:** Avoid unreviewed changes, incorrect target project or bypassing protected branch policy.

**Syntax**

`glab mr create -R example-group/example-project --source-branch feat/notes --target-branch main --title "Review notes" --description "Fictional review" --draft`

**Basic example**

`glab mr create -R example-group/example-project --source-branch feat/notes --target-branch main --title "Review notes" --description "Fictional review" --draft`

Illustrate opening a draft from a published sandbox source branch.

**Professional example**

`glab mr create -R example-group/example-project --source-branch feat/docs --target-branch main --title "Review documentation" --description "Describe changes and test evidence"`

Illustrate an authorized review request with explicit source and target branches.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Conditional
- Other state: Conditional

**Expected result:** Creates an MR and returns information about it; it does not merge the source branch.

**Effects and side effects:** Writes MR metadata; may trigger pipelines or notifications. Shown forms use existing published refs without --push.

**Common errors:** Treating MR creation as approval or assuming no automation is triggered.

**Alternatives:** Use the GitLab web interface for authorized MR creation and review.

**Recovery:** Verify the MR link and source and target. If incorrect, coordinate authorized edit or closure; closing does not erase the MR history.

**Version and dependencies:** Requires a current compatible GitLab CLI (glab), authorized authentication, network access and relevant project permissions. Check glab help and server compatibility.

**Related lessons**

- [gitlab/04-merge-requests-review-and-forks](../../gitlab/04-merge-requests-review-and-forks/README.md)
- [gitlab/08-gitlab-cli-and-platform-comparison](../../gitlab/08-gitlab-cli-and-platform-comparison/README.md)

**Official documentation**

- <https://docs.gitlab.com/cli/mr/create/>

## glab-mr-view

**`glab mr view`**

**Type:** External tool

**Level:** Intermediate

**Find by intent:** Review changes, Inspect repository state

**Risk:** Read-only. Inspection is not approval to merge. Protect private metadata and logs; do not expose credentials.

**Purpose:** Inspect GitLab merge request details and reported status.

**Prerequisites:** Examples are fictional templates, not live exercises. Substitute only an explicitly authorized sandbox repository, verified account, refs and IDs. Inspect the CLI version and authentication first.

**Options:** --output json selects structured output; --comments includes discussions; --web opens the platform page.

**When to use:** When verifying the reviewed MR and current integration status.

**When to avoid:** Do not rely on a conflict flag while the server is still calculating mergeability.

**Syntax**

`glab mr view 42 -R example-group/example-project`

**Basic example**

`glab mr view 42 -R example-group/example-project`

Inspect fictional sandbox MR 42.

**Professional example**

`glab mr view 42 -R example-group/example-project --output json`

Inspect structured MR metadata; verify current SHA and merge status before deciding.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Displays requested MR information; mergeability and approvals may change or be temporarily unknown.

**Effects and side effects:** Reads platform metadata over the network; does not intentionally alter Git refs, index, checkout or platform resources in the shown form.

**Common errors:** Treating a conflict-free MR or old approval as proof all gates passed.

**Alternatives:** Inspect the web MR details and associated pipeline for the exact reviewed revision.

**Recovery:** No undo is needed for inspection. Verify repository, ID, permissions and exact commit association; refresh status if incomplete or stale.

**Version and dependencies:** Requires a current compatible GitLab CLI (glab), authorized authentication, network access and relevant project permissions. Check glab help and server compatibility.

**Related lessons**

- [gitlab/04-merge-requests-review-and-forks](../../gitlab/04-merge-requests-review-and-forks/README.md)
- [gitlab/08-gitlab-cli-and-platform-comparison](../../gitlab/08-gitlab-cli-and-platform-comparison/README.md)

**Official documentation**

- <https://docs.gitlab.com/cli/mr/view/>

## glab-ci-status

**`glab ci status`**

**Type:** External tool

**Level:** Intermediate

**Find by intent:** Inspect CI

**Risk:** Read-only. Inspection is not approval to merge. Protect private metadata and logs; do not expose credentials.

**Purpose:** Inspect GitLab CI/CD pipeline status for a branch.

**Prerequisites:** Examples are fictional templates, not live exercises. Substitute only an explicitly authorized sandbox repository, verified account, refs and IDs. Inspect the CLI version and authentication first.

**Options:** --branch selects the branch; --compact condenses output; --live or --wait waits for updates or completion.

**When to use:** When reviewing the reported branch pipeline and investigating CI progress.

**When to avoid:** Do not assume the latest branch pipeline is the MR's exact head pipeline, especially across forks.

**Syntax**

`glab ci status -R example-group/example-project --branch=main`

**Basic example**

`glab ci status -R example-group/example-project --branch=main`

Inspect reported pipeline status for a fictional sandbox branch.

**Professional example**

`glab ci status -R example-group/example-project --branch=feat/docs --compact`

Inspect condensed branch pipeline status and verify its commit and association to the MR.

**State effects**

- Working tree: Unchanged
- Index: Unchanged
- Objects / refs / history: Unchanged
- Remote repository: Unchanged
- Other state: Unchanged

**Expected result:** Displays reported pipeline status; completion and commit association must be checked separately before merge.

**Effects and side effects:** Reads platform metadata over the network; does not intentionally alter Git refs, index, checkout or platform resources in the shown form.

**Common errors:** Confusing a pending or unrelated branch pipeline with a successful required MR check.

**Alternatives:** Use the MR web page and its linked pipeline to inspect exact job results and logs.

**Recovery:** No undo is needed for inspection. Verify repository, ID, permissions and exact commit association; refresh status if incomplete or stale.

**Version and dependencies:** Requires a current compatible GitLab CLI (glab), authorized authentication, network access and relevant project permissions. Check glab help and server compatibility.

**Related lessons**

- [gitlab/06-pipelines-and-runners](../../gitlab/06-pipelines-and-runners/README.md)
- [ci-cd/04-gitlab-ci-cd](../../ci-cd/04-gitlab-ci-cd/README.md)

**Official documentation**

- <https://docs.gitlab.com/cli/ci/status/>


---

<!-- navigation-footer -->
[Previous](../13-security-and-maintenance/README.md) · [Index](../README.md) · [Next module](../../practical-projects/README.md)
<!-- /navigation-footer -->
