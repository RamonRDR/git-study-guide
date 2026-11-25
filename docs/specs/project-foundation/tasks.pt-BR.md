# Registro de tarefas

[English](tasks.md) · [Português](tasks.pt-BR.md) · [Español](tasks.es.md)

Fundação aprovada e integrada pelo PR #1 em 25/11/2026. Mudanças seguintes exigem revisão e aprovação explícita do mantenedor.

| Task | Descrição | Status |
| --- | --- | --- |
| T00-01 | Auditar repositórios, branches, ruleset e referência Python | Auditoria de leitura concluída; ver auditoria |
| T00-02 | Elaborar Constitution, specification, plano, tarefas, critérios e ADRs trilíngues | Concluído ([PR #1](https://github.com/RamonRDR/git-study-guide/pull/1)) |
| T00-03 | Elaborar contrato, guias relacionados, índices, roadmap e README provisório | Concluído ([PR #1](https://github.com/RamonRDR/git-study-guide/pull/1)) |
| T00-04 | Validar estrutura de idiomas, links, alinhamento e último PR; solicitar Codex Review | Concluído ([PR #1](https://github.com/RamonRDR/git-study-guide/pull/1)) |
| T00-05 | Aprovação do mantenedor, squash merge, verificar main | Concluído ([PR #1](https://github.com/RamonRDR/git-study-guide/pull/1)) |
| T01-01 | AGENTS, AUTHORS, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, SUPPORT, orientação de IA e templates de issue/PR (AC-01; depende de T00-05) | Concluído ([PR #2](https://github.com/RamonRDR/git-study-guide/pull/2)) |
| T02-01 | Estrutura, navegação, validadores, testes, CI; status checks obrigatórios após execuções observadas e aprovação separada (AC-02; depende de T01-01) | Concluído ([PR #3](https://github.com/RamonRDR/git-study-guide/pull/3)) |
| T03-01 | Módulos 00–01: primeiros passos, história e fundamentos (AC-03; depende de T02-01) | Submetido à revisão |
| T04-01 | Módulos 02–03: arquitetura Git e comandos básicos (AC-04; depende de T03-01) | Pendente |
| T05-01 | Módulo 04: gerenciamento de branches (AC-05; depende de T04-01) | Pendente |
| T06-01 | Módulo 05: merge, squash, rebase e conflitos (AC-06; depende de T05-01) | Pendente |
| T07-01 | Módulo 06: remotes e colaboração (AC-07; depende de T06-01) | Pendente |
| T08-01 | Módulo 07: histórico e recuperação (AC-08; depende de T07-01) | Pendente |
| T09-01 | Módulo 08: GitHub (AC-09; depende de T08-01) | Pendente |
| T10-01 | Módulo 09: GitLab (AC-10; depende de T09-01) | Pendente |
| T11-01 | Módulo 10: CI/CD e automação (AC-11; depende de T10-01) | Pendente |
| T12-01 | Módulo 11: fluxos profissionais (AC-12; depende de T11-01) | Pendente |
| T13-01 | Módulo 12: segurança e governança (AC-13; depende de T12-01) | Pendente |
| T14-01 | Módulos 13–14: Git avançado e internals (AC-14; depende de T13-01) | Pendente |
| T15-01 | Módulo 15: referência de comandos (AC-15; depende de T14-01) | Pendente |
| T16-01 | Módulo 16: oito projetos práticos (AC-16; depende de T15-01) | Pendente |
| T17-01 | Módulo 17: desafios, quizzes e entrevistas; piloto de registros estruturados (AC-17; depende de T16-01) | Pendente |
| T18-01 | Finalizar contrato, manifestos, schemas, fixtures do consumidor; avaliar playground opcional separadamente (AC-18; depende de T17-01) | Pendente |
| T19-01 | Identidade fornecida pelo mantenedor, README final, QA, handoff (AC-19; depende de T18-01) | Pendente |

Atualizar evidências em cada PR focado. Entrega proposta ou PR aberto não é conclusão. Usar links reais de checks/reviews e SHAs; após merge aprovado, verificar main e exclusão da branch, registrar handoff na próxima alteração autorizada se necessário.


Evidência Sprint 00: [Codex](https://github.com/RamonRDR/git-study-guide/pull/1#issuecomment-7174894634), [validation](https://github.com/RamonRDR/git-study-guide/pull/1#issuecomment-7174867993), [squash commit](https://github.com/RamonRDR/git-study-guide/commit/38fd45048a036ef377a05ec8429e624464841159). Mantenedor aprovou; main e exclusão da branch verificadas; CI ausente conforme plano.

## Documentos relacionados

- [Plano de implementação](implementation-plan.pt-BR.md)
- [Critérios de aceite](acceptance-criteria.pt-BR.md)
- [Auditoria inicial](audit.pt-BR.md)

Evidência Sprint 01: [PR #2](https://github.com/RamonRDR/git-study-guide/pull/2), [Codex](https://github.com/RamonRDR/git-study-guide/pull/2#issuecomment-7176325295), [squash commit](https://github.com/RamonRDR/git-study-guide/commit/df139992ae109145184a4de86b2a95b7e1187e0b). Última revisão sem apontamentos; main e exclusão de branch verificadas.

Evidência Sprint 02: [PR #3](https://github.com/RamonRDR/git-study-guide/pull/3), [CI](https://github.com/RamonRDR/git-study-guide/actions/runs/45717835244), [main CI](https://github.com/RamonRDR/git-study-guide/actions/runs/45718411371), [Codex](https://github.com/RamonRDR/git-study-guide/pull/3#issuecomment-7176975402), [ruleset](https://github.com/RamonRDR/git-study-guide/rules/28108699). Main e exclusão da branch verificadas; checks Linux e Windows obrigatórios com política estrita de atualização após autorização do mantenedor.
