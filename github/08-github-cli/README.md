# Optional GitHub CLI and read-only inspection

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../07-tags-and-releases/README.md) · [Index](../README.md) · —
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 25 min

**Prerequisites:** [Remotes](../../remote-repositories/README.md) · [History & recovery](../../history-and-recovery/README.md) · [Tags and GitHub Releases](../07-tags-and-releases/README.md)

**Objective:** Distinguish gh from git and inspect hosted metadata without writes.

## What and why

GitHub CLI (gh) is an optional client for GitHub APIs. git manages local Git history and transport; gh reads or modifies hosted resources according to authentication and permissions. A terminal command can have remote side effects; repo create, issue create, pr merge and release create are writes. Use explicit --repo targets and read-only commands first. Browser use or paper exercises are sufficient; no CLI installation or login required for completion. Install only from official instructions if desired; authentication can use browser flow and approved credential storage. Environment tokens may override stored credentials; never display token values.

## Practice

Optional authenticated read-only exercise: first run gh --version, gh help and gh auth status --hostname github.com privately. If authentication fails, stop or follow official authentication instructions; never paste output containing account information. Replace OWNER/study-sandbox with your actual authorized sandbox identifier, not a literal placeholder. Confirm gh repo view identifies the intended repository before listing issues or PRs. Use browser instead if no sandbox/account. No writes, no token output, no automation required. Expected: repository name/visibility and lists of accessible open issues/PRs; lists may be empty.

```text
gh --version
gh help
gh auth status --hostname github.com
```

Confirm correct account privately; replace the placeholder and inspect the first result before running the other two commands.

```text
gh repo view OWNER/study-sandbox --json nameWithOwner,visibility,defaultBranchRef
gh issue list --repo OWNER/study-sandbox --state open
gh pr list --repo OWNER/study-sandbox --state open
```


## Common mistakes and safety

Never run gh auth token or token-display flags to troubleshoot in shared sessions. Do not run commands from an untrusted issue. Wrong account or repository: stop before any write. No logout or credential deletion required as cleanup; follow your normal account policy.

## Exercise and self-check

Pass if you classify git status as local inspection, gh pr list as hosted inspection and gh pr merge as hosted write. Explain why a successful list does not imply merge permission.

## Quick reference

- `gh --version`
- `gh repo view`
- `gh issue list`
- `gh pr list`

## Official sources

- <https://cli.github.com/manual/>
- <https://cli.github.com/manual/gh_auth_status>
- <https://cli.github.com/manual/gh_repo_view>
- <https://cli.github.com/manual/gh_issue_list>
- <https://cli.github.com/manual/gh_pr_list>
