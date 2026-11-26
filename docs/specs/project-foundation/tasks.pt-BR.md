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
| T03-01 | Módulos 00–01: primeiros passos, história e fundamentos (AC-03; depende de T02-01) | Concluído ([PR #4](https://github.com/RamonRDR/git-study-guide/pull/4)) |
| T04-01 | Módulos 02–03: arquitetura Git e comandos básicos (AC-04; depende de T03-01) | Concluído ([PR #5](https://github.com/RamonRDR/git-study-guide/pull/5)) |
| T05-01 | Módulo 04: gerenciamento de branches (AC-05; depende de T04-01) | Concluído ([PR #6](https://github.com/RamonRDR/git-study-guide/pull/6)) |
| T06-01 | Módulo 05: merge, squash, rebase e conflitos (AC-06; depende de T05-01) | Concluída ([PR #7](https://github.com/RamonRDR/git-study-guide/pull/7)) |
| T07-01 | Módulo 06: remotes e colaboração (AC-07; depende de T06-01) | Concluída ([PR #8](https://github.com/RamonRDR/git-study-guide/pull/8)) |
| T08-01 | Módulo 07: histórico e recuperação (AC-08; depende de T07-01) | Concluída ([PR #9](https://github.com/RamonRDR/git-study-guide/pull/9)) |
| T09-01 | Módulo 08: GitHub (AC-09; depende de T08-01) | Submetida para revisão |
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

Evidência Sprint 03: [PR #4](https://github.com/RamonRDR/git-study-guide/pull/4), [CI](https://github.com/RamonRDR/git-study-guide/actions/runs/45721626737), [main CI](https://github.com/RamonRDR/git-study-guide/actions/runs/45722633012), [Codex](https://github.com/RamonRDR/git-study-guide/pull/4#issuecomment-7177485378), [squash commit](https://github.com/RamonRDR/git-study-guide/commit/ef430abd68aa476fc9fff898bfb7c1e83b4d55da). Main e exclusão da branch verificadas; CI final aprovado, sem avisos de depreciação ou apontamentos pendentes. Instalações limpas, macOS e interação GUI não testados.

Evidência Sprint 04: [PR #5](https://github.com/RamonRDR/git-study-guide/pull/5), [CI](https://github.com/RamonRDR/git-study-guide/actions/runs/45723113329), [Codex](https://github.com/RamonRDR/git-study-guide/pull/5#issuecomment-7177929221), [squash commit](https://github.com/RamonRDR/git-study-guide/commit/6695bea89c76fc6a52499ab4f17e9c89cff37fa1), [main CI](https://github.com/RamonRDR/git-study-guide/actions/runs/45724230029). Main e exclusão da branch verificadas; CI final do PR aprovou seis validadores e 24 testes por plataforma, sem avisos nem apontamentos pendentes. macOS e interação GUI não testados. CI pós-merge aprovado.

Evidência Sprint 05: [PR #6](https://github.com/RamonRDR/git-study-guide/pull/6), [CI](https://github.com/RamonRDR/git-study-guide/actions/runs/45724512229), [Codex](https://github.com/RamonRDR/git-study-guide/pull/6#issuecomment-7178166184), [squash commit](https://github.com/RamonRDR/git-study-guide/commit/da1a8b591e9d0349e4991cc5cef99a7a44a47ee0), [main CI](https://github.com/RamonRDR/git-study-guide/actions/runs/45727648558). Main e exclusão da branch verificadas; CI final do PR aprovou seis validadores e 29 testes por plataforma, sem avisos nem apontamentos pendentes. macOS e interação GUI não testados. CI pós-merge aprovado.

Evidências da Sprint 06: [PR #7](https://github.com/RamonRDR/git-study-guide/pull/7), [CI](https://github.com/RamonRDR/git-study-guide/actions/runs/45728027152), [Codex](https://github.com/RamonRDR/git-study-guide/pull/7#issuecomment-7178708117), [auditoria final](https://github.com/RamonRDR/git-study-guide/pull/7#issuecomment-7178951280), [squash commit](https://github.com/RamonRDR/git-study-guide/commit/3dcd547401632bfbfbcb6105d2ab8b5414b13d01), [main CI](https://github.com/RamonRDR/git-study-guide/actions/runs/45730087351). Main e exclusão da branch verificadas; jobs Linux e Windows pós-merge aprovados.

Evidências da Sprint 07: [PR #8](https://github.com/RamonRDR/git-study-guide/pull/8), [CI](https://github.com/RamonRDR/git-study-guide/actions/runs/45730675180), [Codex](https://github.com/RamonRDR/git-study-guide/pull/8#issuecomment-7179056521), [auditoria final](https://github.com/RamonRDR/git-study-guide/pull/8#issuecomment-7179385728), [squash commit](https://github.com/RamonRDR/git-study-guide/commit/e087764de306010c76f1ee51bcdfe642a2bfab9e), [main CI](https://github.com/RamonRDR/git-study-guide/actions/runs/45733554621). Main e exclusão da branch verificadas; tree revisada idêntica; CI final e pós-merge aprovaram 45 testes e seis validadores por plataforma, sem warnings identificados.

Evidências da Sprint 08: [PR #9](https://github.com/RamonRDR/git-study-guide/pull/9), [CI](https://github.com/RamonRDR/git-study-guide/actions/runs/45736565586), [Codex](https://github.com/RamonRDR/git-study-guide/pull/9#issuecomment-7179928680), [auditoria final](https://github.com/RamonRDR/git-study-guide/pull/9#issuecomment-7180367305), [squash commit](https://github.com/RamonRDR/git-study-guide/commit/9887007c3018f8b80541bfc604705885888e70c8), [main CI](https://github.com/RamonRDR/git-study-guide/actions/runs/45739845408). Main e exclusão da branch verificadas; tree revisada idêntica; CI PR e pós-merge aprovaram 57 testes e seis validadores por plataforma, sem warnings identificados.
