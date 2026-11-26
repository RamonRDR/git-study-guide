# 13 Advanced Git

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../security/README.md) · [Index](../docs/learning-path.md) · [Next](../git-internals/README.md)
<!-- /navigation -->

**Status: lessons included in Sprint 14.** 470 min. Prerequisite: security and prior workflow modules. Git 2.34+ recommended; Bash (Git Bash on Windows), optional subtree helper. No online credentials.

## Disposable practice fixture

Open a new dedicated Bash shell (`bash --noprofile --norc`) before each chapter; do not run in your normal shell. Run commands individually, stopping on any failure. Before committing, verify both identities start with `Study Guide Example <learner@example.invalid>`; otherwise stop. Verify the printed sandbox and root, no remote and clean status. The three commits deliberately change a fictional catalog; first two are good, last is bad. Do not reuse an old sandbox.

```bash
sandbox=$(mktemp -d)
printf 'Sandbox: %s\n' "$sandbox"
while IFS= read -r name; do unset "$name"; done < <(compgen -e GIT_)
mkdir "$sandbox/home" "$sandbox/template"
export HOME="$sandbox/home" USERPROFILE="$sandbox/home"
export GIT_CONFIG_GLOBAL="$sandbox/gitconfig" GIT_CONFIG_NOSYSTEM=1
export GIT_CONFIG_COUNT=0 GIT_TEMPLATE_DIR="$sandbox/template"
export GIT_ALLOW_PROTOCOL=file GIT_TERMINAL_PROMPT=0
git init -b main "$sandbox/repo"
cd "$sandbox/repo"
git config --local user.name "Study Guide Example"
git config --local user.email learner@example.invalid
git config --local commit.gpgsign false
git config --local tag.gpgsign false
git config --local core.autocrlf false
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
mkdir docs src
printf '%s\n' ok > src/state.txt
printf '%s\n' catalog > docs/guide.txt
git add -- docs/guide.txt src/state.txt
git commit -m "docs: initial catalog"
printf '%s\n' reviewed > docs/guide.txt
git add -- docs/guide.txt
git commit -m "docs: review guide"
printf '%s\n' bad > src/state.txt
git add -- src/state.txt
git commit -m "docs: regression fixture"
git rev-parse --show-toplevel
git log --oneline -3
git status --short
git remote
```

Use only the disposable fixture and fictional data. If state differs, stop; inspect status and the relevant operation before aborting or recreating the fixture. Close the dedicated shell and remove only the recorded sandbox through the file manager after reviewing its contents.

## Chapters

<!-- chapters -->
- 01 [Bisect: isolate a regression](01-bisect/README.md)
- 02 [Worktrees: parallel working directories](02-worktree/README.md)
- 03 [Submodules: pinned repository dependencies](03-submodules/README.md)
- 04 [Subtree: vendor content into a repository](04-subtree/README.md)
- 05 [Hooks: local automation and trust](05-hooks/README.md)
- 06 [Rerere: reuse conflict resolutions](06-rerere/README.md)
- 07 [Sparse checkout: select working files](07-sparse-checkout/README.md)
- 08 [Partial and shallow clones](08-partial-and-shallow-clone/README.md)
- 09 [Blame and grep: investigate changes](09-blame-and-grep/README.md)
- 10 [Archive and bundle: distribute snapshots or history](10-archive-and-bundle/README.md)
- 11 [Integrated advanced Git lab](11-integrated-advanced-lab/README.md)
<!-- /chapters -->

---

<!-- navigation-footer -->
[Previous](../security/README.md) · [Index](../docs/learning-path.md) · [Next](../git-internals/README.md)
<!-- /navigation-footer -->
