# Educational and engineering roadmap

[English](roadmap.md) · [Português](roadmap.pt-BR.md) · [Español](roadmap.es.md)

Foundation approved and integrated via PR #1 on 2026-11-25. Subsequent changes require review and explicit maintainer approval.

## Curriculum (18 modules)

| Order | Path | Topic | Scope |
| --- | --- | --- | --- |
| 00 | `getting-started/` | Getting Started | Install Git on Windows/Linux/macOS, terminal, local identity, help, VS Code and optional GUI, first repository and commit; preview basic vocabulary. |
| 01 | `fundamentals/` | History & Fundamentals | Linux, Linus Torvalds, BitKeeper, centralized/distributed VCS, Git versus GitHub/GitLab; why local history matters. |
| 02 | `git-architecture/` | Git Architecture | Working tree, index, repository, remote concept, snapshots, HEAD, refs and file states. |
| 03 | `basic-commands/` | Basic Git Commands | init, status, add, commit, diff, log, show, rm, mv, config, help, ignore rules; inspect before changing. |
| 04 | `branches/` | Branch Management | Create from refs, switch, rename, compare, local deletion, detached HEAD, naming; defer remote deletion/tracking execution to 06. |
| 05 | `merge-and-conflicts/` | Merge & Conflicts | Fast-forward, merge commits, squash, rebase, interactive rebase, conflict resolution, abort/continue; local-only history rewriting; inspect state. |
| 06 | `remote-repositories/` | Remote Repositories | clone, remote, fetch, pull, push, origin/upstream, tracking, divergence, remote deletion, refspecs where useful; introduce safe authentication before online practice. |
| 07 | `history-and-recovery/` | History & Recovery | restore, reset, revert, reflog, stash, cherry-pick, amend, recovery and rewriting limits; disposable practice only for destructive operations. |
| 08 | `github/` | GitHub | Repositories, forks, PRs, issues, reviews, discussions, releases, projects, rulesets, branch protection, open source, optional CLI. |
| 09 | `gitlab/` | GitLab | Projects/groups, MRs, issues, review, runners, releases, protected branches, collaboration and comparison with GitHub. |
| 10 | `ci-cd/` | CI/CD & Automation | Integration/delivery/deployment, GitHub Actions, GitLab CI/CD, YAML, jobs, steps, pipelines, artifacts, cache, environments, secrets, runners and quality gates; safe permissions first. |
| 11 | `professional-workflows/` | Professional Workflows | Git Flow, GitHub Flow, trunk-based, feature branches, Conventional Commits, SemVer, code review, SDD/TDD, AI assistance, releases. |
| 12 | `security/` | Security & Governance | SSH, HTTPS, tokens, credential managers, secrets, permissions, branch protection, rulesets, CODEOWNERS, signing, supply chain, accidental disclosure, least privilege. |
| 13 | `advanced-git/` | Advanced Git | bisect, worktree, submodules, subtree, hooks, rerere, sparse-checkout, partial/shallow clone, blame, grep, archive, bundle and trade-offs. |
| 14 | `git-internals/` | Git Internals | Blobs, trees, commits, tags, hashes, refs, object database, packfiles, garbage collection, reflogs, porcelain/plumbing. |
| 15 | `command-reference/` | Command Reference | Searchable catalog by operation and intent, 100+ meaningful entries; distinguish subcommands, flags, usages, combinations and hosting operations. |
| 16 | `practical-projects/` | Practical Projects | Eight integrated projects: My First Repository; Two Developers, One Project; Merge Conflict Laboratory; The Lost Commit; Open Source Contribution; Automated Quality Pipeline; Release Management; Professional Engineering Workflow. |
| 17 | `exercises/` | Challenges & Interviews | Exercises, quizzes, troubleshooting, challenges, interview questions, professional simulations and self-assessment rubrics; map prerequisites first. |

Prerequisite policy: module 00 introduces only the minimum vocabulary needed for a first commit; modules 01–03 deepen it. Module 04 teaches local branches; remote tracking/deletion practice waits for 06. Explain safe recovery/abort before any risky merge or rebase in 05, then deepen in 07. Teach safe credential handling before 06 and least privilege before 10; module 12 consolidates security. Introduce relevant object/ref concepts before advanced tasks. Link earlier instruction before assessment; modules 00–04 have lessons; later module indexes are planned.

## Engineering (20 sprints)

| Sprint | Phase | Deliverable |
| --- | --- | --- |
| 00 | I | Foundation, audit, SDD, ADRs, preliminary contract, indexes, provisional README |
| 01 | I | AGENTS, AUTHORS, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, SUPPORT, AI guidance and issue/PR templates |
| 02 | I | Structure, navigation, validators, tests, CI; required status checks after observed runs and separate approval |
| 03 | II | Modules 00–01: onboarding, history and fundamentals |
| 04 | II | Modules 02–03: Git architecture and basic commands |
| 05 | II | Module 04: branch management |
| 06 | III | Module 05: merge, squash, rebase and conflicts |
| 07 | III | Module 06: remotes and collaboration |
| 08 | III | Module 07: history and recovery |
| 09 | IV | Module 08: GitHub |
| 10 | IV | Module 09: GitLab |
| 11 | IV | Module 10: CI/CD and automation |
| 12 | IV | Module 11: professional workflows |
| 13 | IV | Module 12: security and governance |
| 14 | V | Modules 13–14: advanced Git and internals |
| 15 | V | Module 15: command reference |
| 16 | V | Module 16: eight practical projects |
| 17 | V | Module 17: challenges, quizzes and interviews; pilot structured records |
| 18 | VI | Finalize content contract, manifests, schemas, consumer fixtures; evaluate optional playground separately |
| 19 | VI | Maintainer-supplied identity, final README, QA, release handoff |

Phases: I Foundation; II Essentials; III Collaboration and recovery; IV Platforms and engineering; V Advanced and practice; VI Learning Hub and release. Sprints 00–04 integrated via PRs #1–5; Sprint 05 submitted for review; Sprints 06–19 planned. Split large sprints into focused PRs without changing scope. Do not confuse engineering sprint numbers with educational modules.

## Related documents

- [Specification](specs/project-foundation/specification.md)
- [Implementation plan](specs/project-foundation/implementation-plan.md)
- [Acceptance criteria](specs/project-foundation/acceptance-criteria.md)

- [Learning path](learning-path.md)
