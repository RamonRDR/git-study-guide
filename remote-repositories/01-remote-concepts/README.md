# Remotes, bare repositories and clones

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
— · [Index](../README.md) · [Next](../02-fetch-and-tracking/README.md)
<!-- /navigation -->

**Level:** beginner · **Estimated time:** 35 min

**Prerequisites:** [Isolated lab setup](../../getting-started/03-first-repository/README.md) · [First commit](../../getting-started/05-first-commit/README.md) · [Merge and conflicts](../../merge-and-conflicts/README.md)

**Objective:** Explain remote aliases and create independent clones without an account.

## What and why

A remote is another Git repository, not necessarily an internet server. A bare repository stores history and refs without a normal checked-out working tree. It is useful as a shared exchange point. Clone creates a new repository, downloads history and normally checks out the branch indicated by the remote HEAD. The name origin is a convention created by clone; upstream can be another remote alias, often the original project in a fork workflow. Neither is reserved. An upstream tracking branch is instead a configured relationship between a local branch and another ref. GitHub and GitLab add hosting, review and permission features on top of Git.

## Practice

Create a NEW disposable lab following module 00 chapter 03 and its first-commit lesson. Use Git 2.40+ and the same dedicated Bash or PowerShell shell with isolated system/global config, cleared inherited Git variables and empty template. Verify repo/main has exactly one commit with note.txt = practice, clean status and both fictional identities. Record the temporary parent path privately. Move one level up using `cd ..`; inspect `pwd` (Bash) or `Get-Location` (PowerShell). Stop unless it is exactly that parent and only repo, template and gitconfig exist. Restrict transport in this shell to local files: Bash `export GIT_ALLOW_PROTOCOL=file`, PowerShell `$env:GIT_ALLOW_PROTOCOL = 'file'`. Run commands individually, stop on unexpected errors. After remote -v check both URLs resolve to the newly created origin.git before pushing. Expect true for bare, refs/heads/main for HEAD. The seed repo is used only to publish the initial commit.
```text
git init --bare --initial-branch=main origin.git
git -C origin.git rev-parse --is-bare-repository
git -C origin.git symbolic-ref HEAD
git -C repo remote add origin ../origin.git
git -C repo remote -v
```

Check that both URLs resolve to the newly created local origin.git. Only then continue:

```text
git -C repo push -u origin main
git -C origin.git rev-parse refs/heads/main
git clone --no-local origin.git alice
git clone --no-local origin.git bob
```
Configure local identities in both clones (clone does not copy the seed's local identity).
```text
git -C alice config --local user.name "Study Guide Example"
git -C alice config --local user.email learner@example.invalid
git -C alice config --local commit.gpgsign false
git -C alice config --local core.autocrlf false
git -C bob config --local user.name "Study Guide Example"
git -C bob config --local user.email learner@example.invalid
git -C bob config --local commit.gpgsign false
git -C bob config --local core.autocrlf false
```

```text
git -C alice rev-parse --show-toplevel
git -C bob rev-parse --show-toplevel
git -C alice remote -v
git -C bob remote -v
git -C alice branch -vv
git -C bob branch -vv
git -C alice status --short
git -C bob status --short
```
Both clone roots must be the intended alice/bob folders, origin URLs must resolve to the same local origin.git, main tracks origin/main, and status is clean. All three main tips equal the seed commit. `--no-local` uses the normal Git transport rather than local copy optimizations. Keep the dedicated shell at the parent for chapters 02–04. Diagram: repo (seed) -> origin.git (bare); alice and bob each have their own HEAD, working tree, index and refs; both exchange commits with origin.git. For remote configuration practice, the temporary alias points to the SAME bare repository, not a second server.
```text
git -C alice remote add upstream ../origin.git
git -C alice remote set-url upstream .././origin.git
git -C alice remote rename upstream training
git -C alice remote get-url training
git -C alice remote remove training
git -C alice remote -v
```
Expected: only origin remains; removing an alias removes local configuration and its tracking refs, not the remote repository. Changing a URL does not migrate any history. In a professional fork workflow, origin often names your fork and upstream the original; verify both rather than assuming.

## Common mistakes and safety

Never clone or push to an unknown URL. A clone is not an authentication grant; local identity is not authorization. If paths or identities differ, stop and restart the disposable lab rather than modifying real settings. Do not reuse this shell for real remotes.

## Exercise and self-check

Why does a bare origin have no checked-out note.txt? Hint: distinguish history from the working tree. Answer: the file exists in commit snapshots, not a normal working tree. Pass if both clones show the same initial main ID and independent roots.

## Quick reference

- `git init --bare --initial-branch=main`
- `git clone --no-local`
- `git remote -v`
- `git remote add / set-url / rename / remove`

## Official sources

- [Git: git-init](https://git-scm.com/docs/git-init)
- [Git: git-clone](https://git-scm.com/docs/git-clone)
- [Git: git-remote](https://git-scm.com/docs/git-remote)
