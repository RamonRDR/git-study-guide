# Hooks: local automation and trust

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../04-subtree/README.md) · [Index](../README.md) · [Next](../06-rerere/README.md)
<!-- /navigation -->

**Level:** advanced · **Estimated time:** 40 min

**Prerequisites:** [13 Advanced Git](../README.md) · [Security & Governance](../../security/README.md)

**Objective:** Hooks are programs invoked at selected Git lifecycle events, e.g.

## What and why

Hooks are programs invoked at selected Git lifecycle events, e.g. pre-commit. A nonzero pre-commit result aborts the commit. Hooks are not normally copied by clone; core.hooksPath can change where they are read. Local checks improve feedback but cannot replace server-side required checks. Never run a hook from an untrusted source.

## Practice

Create a fresh isolated fixture using the module index before each practice. Run one command at a time; stop on unexpected results. Check the printed sandbox and repository root before any changes. Use Git 2.34+ as the practice baseline; check command help and skip unavailable optional features. No commands on production repositories.

In the fresh fixture, create your own inert hook that always rejects a commit, only in a fresh sibling folder. `chmod` applies to Bash environments that support executable scripts. Check the rejected commit leaves HEAD unchanged and staged content intact; if execution is unsupported, stop. Unset only the lab-local configuration afterward; never bypass a real project's checks.

```bash
mkdir "$sandbox/hooks"
printf '%s\n' '#!/bin/sh' 'exit 1' > "$sandbox/hooks/pre-commit"
chmod +x "$sandbox/hooks/pre-commit"
git config --local core.hooksPath "$sandbox/hooks"
before=$(git rev-parse HEAD)
printf '%s\n' 'review' > docs/review.txt
git add -- docs/review.txt
git commit -m "docs: hook practice"
test "$(git rev-parse HEAD)" = "$before"
git diff --cached --name-only
git config --local --unset core.hooksPath
```

## Common mistakes and safety

Use only the disposable fixture and fictional data. If state differs, stop; inspect status and the relevant operation before aborting or recreating the fixture. Close the dedicated shell and remove only the recorded sandbox through the file manager after reviewing its contents.

## Exercise and self-check

Why must CI independently enforce a check? Hooks are local, configurable and not a trusted enforcement boundary.

## Quick reference

- `git config --local core.hooksPath "<sandbox>/hooks"`
- `git add -- docs/review.txt`
- `git commit -m "docs: hook practice"`
- `git diff --cached --name-only`

## Official sources

- [https://git-scm.com/docs/githooks](https://git-scm.com/docs/githooks)
- [https://git-scm.com/docs/git-config](https://git-scm.com/docs/git-config)

---

<!-- navigation-footer -->
[Previous](../04-subtree/README.md) · [Index](../README.md) · [Next](../06-rerere/README.md)
<!-- /navigation-footer -->
