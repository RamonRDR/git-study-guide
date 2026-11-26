# Roadmap educacional e de engenharia

[English](roadmap.md) · [Português](roadmap.pt-BR.md) · [Español](roadmap.es.md)

Fundação aprovada e integrada pelo PR #1 em 25/11/2026. Mudanças seguintes exigem revisão e aprovação explícita do mantenedor.

## Currículo (18 módulos)

| Ordem | Caminho | Tema | Escopo |
| --- | --- | --- | --- |
| 00 | `getting-started/` | Primeiros passos | Instalação Windows/Linux/macOS, terminal, identidade local, ajuda, VS Code e GUI opcional, primeiro repositório e commit; introdução ao vocabulário básico. |
| 01 | `fundamentals/` | História e fundamentos | Linux, Linus Torvalds, BitKeeper, VCS centralizado/distribuído, Git versus GitHub/GitLab; por que o histórico local importa. |
| 02 | `git-architecture/` | Arquitetura Git | Working tree, index, repositório, conceito de remote, snapshots, HEAD, refs e estados de arquivos. |
| 03 | `basic-commands/` | Comandos básicos | init, status, add, commit, diff, log, show, rm, mv, config, help, regras de ignore; inspecionar antes de alterar. |
| 04 | `branches/` | Gerenciamento de branches | Criar a partir de refs, trocar, renomear, comparar, exclusão local, detached HEAD, nomenclatura; adiar prática de exclusão remota/tracking para 06. |
| 05 | `merge-and-conflicts/` | Merge e conflitos | Fast-forward, merge commits, squash, rebase, rebase interativo, resolução de conflitos, abort/continue; reescrita apenas local; inspecionar estado. |
| 06 | `remote-repositories/` | Repositórios remotos | clone, remote, fetch, pull, push, origin/upstream, tracking, divergência, exclusão remota, refspecs quando úteis; apresentar autenticação segura antes da prática online. |
| 07 | `history-and-recovery/` | Histórico e recuperação | restore, reset, revert, reflog, stash, cherry-pick, amend, limites de recuperação e reescrita; operações destrutivas apenas em ambientes descartáveis. |
| 08 | `github/` | GitHub | Repositórios, forks, PRs, issues, reviews, discussions, releases, projects, rulesets, proteção de branches, open source, CLI opcional. |
| 09 | `gitlab/` | GitLab | Projects/groups, MRs, issues, review, runners, releases, branches protegidas, colaboração e comparação com GitHub. |
| 10 | `ci-cd/` | CI/CD e automação | Integração/entrega/deploy, GitHub Actions, GitLab CI/CD, YAML, jobs, steps, pipelines, artifacts, cache, environments, secrets, runners e quality gates; permissões seguras primeiro. |
| 11 | `professional-workflows/` | Fluxos profissionais | Git Flow, GitHub Flow, trunk-based, feature branches, Conventional Commits, SemVer, code review, SDD/TDD, apoio de IA, releases. |
| 12 | `security/` | Segurança e governança | SSH, HTTPS, tokens, credential managers, secrets, permissões, proteção de branches, rulesets, CODEOWNERS, assinatura, cadeia de suprimentos, exposição acidental, menor privilégio. |
| 13 | `advanced-git/` | Git avançado | bisect, worktree, submodules, subtree, hooks, rerere, sparse-checkout, partial/shallow clone, blame, grep, archive, bundle e trade-offs. |
| 14 | `git-internals/` | Internals do Git | Blobs, trees, commits, tags, hashes, refs, object database, packfiles, garbage collection, reflogs, porcelain/plumbing. |
| 15 | `command-reference/` | Referência de comandos | Catálogo pesquisável por operação e intenção, 100+ entradas relevantes; distinguir subcomandos, opções, usos, combinações e operações de plataformas. |
| 16 | `practical-projects/` | Projetos práticos | Oito projetos integrados: My First Repository; Two Developers, One Project; Merge Conflict Laboratory; The Lost Commit; Open Source Contribution; Automated Quality Pipeline; Release Management; Professional Engineering Workflow. |
| 17 | `exercises/` | Desafios e entrevistas | Exercícios, quizzes, troubleshooting, desafios, entrevistas, simulações profissionais e rubricas de autoavaliação; mapear pré-requisitos primeiro. |

Política de pré-requisitos: módulo 00 apresenta apenas vocabulário mínimo para o primeiro commit; 01–03 aprofundam. Módulo 04 ensina branches locais; prática de tracking/exclusão remota aguarda 06. Explicar recuperação/abort seguros antes de merge ou rebase de risco em 05, aprofundar em 07. Ensinar tratamento seguro de credenciais antes de 06 e menor privilégio antes de 10; módulo 12 consolida segurança. Introduzir conceitos de objetos/refs antes de tarefas avançadas. Referenciar ensino anterior antes da avaliação; módulos 00–05 têm aulas; índices seguintes são planejados.

## Engenharia (20 sprints)

| Sprint | Fase | Entrega |
| --- | --- | --- |
| 00 | I | Fundação, auditoria, SDD, ADRs, contrato preliminar, índices, README provisório |
| 01 | I | AGENTS, AUTHORS, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, SUPPORT, orientação de IA e templates de issue/PR |
| 02 | I | Estrutura, navegação, validadores, testes, CI; status checks obrigatórios após execuções observadas e aprovação separada |
| 03 | II | Módulos 00–01: primeiros passos, história e fundamentos |
| 04 | II | Módulos 02–03: arquitetura Git e comandos básicos |
| 05 | II | Módulo 04: gerenciamento de branches |
| 06 | III | Módulo 05: merge, squash, rebase e conflitos |
| 07 | III | Módulo 06: remotes e colaboração |
| 08 | III | Módulo 07: histórico e recuperação |
| 09 | IV | Módulo 08: GitHub |
| 10 | IV | Módulo 09: GitLab |
| 11 | IV | Módulo 10: CI/CD e automação |
| 12 | IV | Módulo 11: fluxos profissionais |
| 13 | IV | Módulo 12: segurança e governança |
| 14 | V | Módulos 13–14: Git avançado e internals |
| 15 | V | Módulo 15: referência de comandos |
| 16 | V | Módulo 16: oito projetos práticos |
| 17 | V | Módulo 17: desafios, quizzes e entrevistas; piloto de registros estruturados |
| 18 | VI | Finalizar contrato, manifestos, schemas, fixtures do consumidor; avaliar playground opcional separadamente |
| 19 | VI | Identidade fornecida pelo mantenedor, README final, QA, handoff |

Fases: I Fundação; II Essenciais; III Colaboração e recuperação; IV Plataformas e engenharia; V Avançado e prática; VI Learning Hub e release. Sprints 00–05 integradas pelos PRs #1–6; Sprint 06 submetida para revisão; Sprints 07–19 planejadas. Dividir sprints grandes em PRs focados sem alterar escopo. Não confundir numeração de sprints com módulos.

## Documentos relacionados

- [Especificação](specs/project-foundation/specification.pt-BR.md)
- [Plano de implementação](specs/project-foundation/implementation-plan.pt-BR.md)
- [Critérios de aceite](specs/project-foundation/acceptance-criteria.pt-BR.md)

- [Trilha](learning-path.pt-BR.md)
