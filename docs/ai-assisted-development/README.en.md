# AI-assisted development

[English](README.en.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

## Principle and roles

Use AI to expand your capacity to think, learn, build and verify, not to surrender responsibility. ChatGPT may support conversation, tutoring, planning, research and drafting. Codex may inspect repositories, implement, test and review where available. Both can make plausible mistakes. Ramon Rodriguez defines strategy, education, editorial direction and visual assets; AI assists implementation and review; final decisions are human. No student needs an AI account or paid plan.

## Study manually first

Try an exercise in a disposable repository first. Predict which state or reference will change, inspect status/diff/history, run one safe command and compare results. If stuck, ask for one hint, not a finished solution. For example: `I am learning staging. Give me one hint to explain why a new file is not in my next commit. Do not give the command until I try.` Ask for official sources and explain the result back in your own words. Never run suggested destructive commands on a real project. AI is optional; official docs, practice and reference answers remain sufficient.

## From question to implementation brief

A useful prompt provides context, goal, current state, scope, constraints, expected output and validation. Refine with questions, version/OS and evidence; do not hide uncertainty. Example maintenance brief: explain local branch creation for beginners; define refs before usage; use a fictional disposable repo; provide EN/PT-BR/ES; no real remote or destructive commands; verify examples and links; report unrun checks; open a focused PR from current main. Establish specification, plan, tasks and acceptance criteria before implementation; obtain maintainer approval for scope. Do not assume a polished prompt is correct.

## Verification and review

Inspect every changed file and scope. Check official sources, prerequisite map, safety warnings, terminology, original examples and meaning across languages. Test actual Git state in owned disposable directories, including representative failure cases; record command, environment and result. Verify latest PR SHA, CI and Codex feedback when available; a request is not a completed review. Address findings, rerun relevant checks and obtain human approval before squash merge. Never fabricate results or mark absent checks passed. AI semantic grading is not in scope; objective state assertions and self-assessment are preferred.

## Privacy, costs and independence

Never share unauthorized private repos, employer/client processes, credentials, tokens, personal data, private URLs, proprietary code or sensitive logs with AI or public issues. Superficial anonymization may not be enough; create original fictional examples. Product availability, privacy settings and limits change; consult official documentation before relying on a capability. No paid API, server, AI subscription or AI grading is required. This guide is independent and not endorsed by OpenAI or hosting providers.

- [Constitution](../specs/constitution.md)
- [Authorship](../../AUTHORS.md)
- [Contribution guide](../../CONTRIBUTING.md)
- [Repository instructions](../../AGENTS.md)
