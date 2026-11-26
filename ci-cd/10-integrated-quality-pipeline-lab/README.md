# Integrated quality pipeline lab

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../09-quality-gates-and-troubleshooting/README.md) · [Index](../README.md) · —
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 45 min

**Prerequisites:** [GitHub](../../github/README.md) · [GitLab](../../gitlab/README.md) · [Quality gates and troubleshooting](../09-quality-gates-and-troubleshooting/README.md)

**Objective:** Reproduce passing and failing checks offline and connect them to a professional pipeline.

## What and why

A pipeline can combine lint and tests without a programming language dependency. The fictional catalog must be nonempty and contain an exact line `status: ready`. The first command is a structural check, the second a simple content assertion; neither is comprehensive lint or application testing. The same shell checks appear in the GitHub and GitLab examples in chapters 03 and 04. Run only the bounded local example below in Bash on Linux/macOS or Git Bash on Windows, not PowerShell or cmd. It creates an isolated temporary directory, does not require Git configuration, network, Python, credentials, or hosting, and removes only the two files it created and the empty temporary directory. It reports three expected outcomes; the failing cases are tested deliberately, not suppressed as successful content checks.

```bash
(
  set -eu
  sandbox=$(mktemp -d)
  printf 'Sandbox: %s\n' "$sandbox"
  trap 'rm -f -- "$sandbox/catalog.txt" "$sandbox/empty.txt"; rmdir -- "$sandbox"' EXIT
  check_catalog() {
    test -s "$1" && grep -Fxq 'status: ready' "$1"
  }
  printf '%s\n' 'status: ready' > "$sandbox/catalog.txt"
  check_catalog "$sandbox/catalog.txt"
  printf '%s\n' 'PASS ready'
  printf '%s\n' 'status: draft' > "$sandbox/catalog.txt"
  if check_catalog "$sandbox/catalog.txt"; then
    exit 1
  fi
  printf '%s\n' 'PASS wrong rejected'
  : > "$sandbox/empty.txt"
  if check_catalog "$sandbox/empty.txt"; then
    exit 1
  fi
  printf '%s\n' 'PASS empty rejected'
)
```

## Practice

Read the script, then run the entire block as written in a disposable shell. Expected output: `PASS ready`, `PASS wrong rejected`, `PASS empty rejected`, with exit status zero. The first test uses a ready file; the second a nonempty wrong file; the third an empty file. A professional team would commit only reviewed checks, use appropriate real lint/test tools, require both environments if needed, inspect exact revisions and separate production deployment. Optional hosted practice is not required; use only an owned disposable repository if free usage and isolation are verified, and never enable deployment.

## Common mistakes and safety

If setup fails, stop. Never substitute a real project path for the temporary directory. The cleanup trap removes only known files; if cleanup fails, inspect the printed temporary path, do not use recursive removal against unknown paths. If a check unexpectedly passes or fails, inspect file content and command exit code; do not weaken the assertion. This is a manual lesson, not a file automatically executed by the guide.

## Exercise and self-check

Pass if all three expected messages appear, you can explain why wrong/empty inputs fail, and you can identify where the same commands appear in both YAML examples. A passing sandbox does not prove the hosted configuration has been executed.

## Quick reference

`test -s` / `grep -Fxq` / exit status

## Official sources

- <https://www.gnu.org/software/bash/manual/html_node/Exit-Status.html>
- <https://www.gnu.org/software/grep/manual/grep.html>
- <https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax>
- <https://docs.gitlab.com/ci/yaml/>
