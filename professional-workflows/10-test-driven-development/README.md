# Test-Driven Development (TDD)

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../09-spec-driven-development/README.md) · [Index](../README.md) · [Next](../11-ai-assisted-development/README.md)
<!-- /navigation -->

**Level:** intermediate · **Estimated time:** 40 min

**Prerequisites:** [CI/CD](../../ci-cd/README.md) · [Spec-Driven Development (SDD)](../09-spec-driven-development/README.md)

**Objective:** Explain red, green and refactor without confusing a test failure with a tooling error.

## What and why

TDD is an iterative programming practice: write a small test that fails for the intended missing behavior (red), implement the minimum behavior to pass (green), then improve structure while keeping tests passing (refactor). A refactor changes internal structure without intentionally changing observable behavior. A test written after implementation can still be useful, but it is not evidence of the red-first cycle. SDD defines what is needed; TDD helps implement and verify small behaviors. Neither requires a particular language, AI, branch model or automatic commit at each color. A shell content assertion in this guide illustrates red/green feedback; it is not a comprehensive unit-testing framework.

```text
red -> green -> refactor -> next test
```

## Practice

Before reading chapter 13, predict the result of `grep -Fxq 'status: ready' catalog.txt` when the existing file contains draft. Then predict after writing the exact ready line. For a refactor exercise, imagine extracting the check into a named helper while keeping its inputs and exit behavior; repeat positive, wrong-value and missing-file cases. Distinguish a missing tool or file error from a meaningful assertion failure. No programming experience is required to trace these outcomes.

## Risks and recovery

Never force green by deleting the assertion, accepting every input or suppressing a failure. Inspect the failure reason; if the test is wrong, correct it transparently. Keep shared integration green; if recording intermediate red commits locally, do not merge a broken revision. A passing example is not exhaustive coverage.

## Exercise and self-check

Expected red: no match in an existing draft file (grep exit 1). Green: exact line matches (exit 0). An operational error is not a valid red demonstration. Refactor must preserve outcomes.

## Quick reference

red / green / refactor

## Sources

- <https://agilealliance.org/glossary/tdd/>
- <https://www.gnu.org/software/grep/manual/grep.html>
