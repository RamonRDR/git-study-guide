# Integrated security lab

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../12-governance-audit-and-traceability/README.md) · [Index](../README.md) · —
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 50 min

**Prerequisites:** [Professional workflows](../../professional-workflows/README.md) · [Governance, audit and traceability](../12-governance-audit-and-traceability/README.md)

**Objective:** Verify safe local staging and rehearse a response.

## What and why

This offline prevention exercise uses only harmless settings, not secrets. It illustrates ignore rules and explicit staging in a new temporary repository. The accompanying tabletop exercise rehearses access control and incident response; it does not create credentials, alter a hosted policy, sign a commit, deploy or test a real incident. Use Git 2.28+ and Bash (Linux/macOS or Git Bash on Windows), with an ordinary clean shell. The block isolates normal Git system/global configuration and leaves the printed sandbox for later inspection; it is not a hardened boundary against a malicious environment.

## Practice

Before running, predict that `local-settings.txt` is ignored and `.gitignore` plus `settings.example.txt` are staged. Execute the entire block below only in a disposable shell. Expected: ignore check prints the local filename, staged names list exactly the two public files, and PASS. Then role-play a hypothetical exposure with no credential value: choose revocation, notification, impact review and correction; draft an access matrix and a merge gate for the fictional catalog. No remote is needed.

```bash
(
  set -eu
  sandbox=$(mktemp -d)
  printf 'Sandbox: %s\n' "$sandbox"
  unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE GIT_COMMON_DIR GIT_CONFIG_PARAMETERS
  export GIT_CONFIG_NOSYSTEM=1 GIT_CONFIG_GLOBAL="$sandbox/global-config" GIT_CONFIG_COUNT=0
  git init -b main "$sandbox/catalog"
  cd "$sandbox/catalog"
  printf '%s\n' 'local-settings.txt' > .gitignore
  printf '%s\n' 'mode=local' > local-settings.txt
  printf '%s\n' 'mode=example' > settings.example.txt
  git check-ignore -- local-settings.txt
  git add -- .gitignore settings.example.txt
  test -z "$(git ls-files -- local-settings.txt)"
  test "$(git ls-files -- settings.example.txt)" = 'settings.example.txt'
  git diff --cached --check
  git diff --cached --name-only
  test -z "$(git remote)"
  printf '%s\n' 'PASS: local file ignored, template staged, no remote'
)
```

## Risks and recovery

Do not substitute a real project path or credential file. If a command fails, stop and inspect the printed sandbox with read-only status/diff commands. Remove it using your file manager only after confirming its exact path. Passing filename checks does not prove content is secret-free; real projects also need content review and appropriate scanning.

## Exercise and self-check

Pass if local file remains untracked, template is staged, no remote exists, and the tabletop response prioritizes revocation before history cleanup. Explain what was not tested: real credentials, platform enforcement, signing, hosted CI and deployment.

## Quick reference

`git check-ignore` / `git add --` / `git diff --cached`

## References

- <https://git-scm.com/docs/gitignore>
- <https://git-scm.com/docs/git-check-ignore>
- <https://git-scm.com/docs/git-ls-files>
- <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository>
