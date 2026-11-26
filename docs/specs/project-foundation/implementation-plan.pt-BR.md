# Plano de implementação

[English](implementation-plan.md) · [Português](implementation-plan.pt-BR.md) · [Español](implementation-plan.es.md)

Fundação aprovada e integrada pelo PR #1 em 25/11/2026. Mudanças seguintes exigem revisão e aprovação explícita do mantenedor.

## Sequência de entregas

| Sprint | Branch | Dependência | Entrega |
| --- | --- | --- | --- |
| 00 | `docs/project-foundation` | — | Fundação, auditoria, SDD, ADRs, contrato preliminar, índices, README provisório |
| 01 | `docs/governance` | 00 | AGENTS, AUTHORS, CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, SUPPORT, orientação de IA e templates de issue/PR |
| 02 | `feat/quality-automation` | 01 | Estrutura, navegação, validadores, testes, CI; status checks obrigatórios após execuções observadas e aprovação separada |
| 03 | `feat/getting-started` | 02 | Módulos 00–01: primeiros passos, história e fundamentos |
| 04 | `feat/git-architecture` | 03 | Módulos 02–03: arquitetura Git e comandos básicos |
| 05 | `feat/branch-management` | 04 | Módulo 04: gerenciamento de branches |
| 06 | `feat/merge-and-conflicts` | 05 | Módulo 05: merge, squash, rebase e conflitos |
| 07 | `feat/remote-repositories` | 06 | Módulo 06: remotes e colaboração |
| 08 | `feat/history-and-recovery` | 07 | Módulo 07: histórico e recuperação |
| 09 | `feat/github` | 08 | Módulo 08: GitHub |
| 10 | `feat/gitlab` | 09 | Módulo 09: GitLab |
| 11 | `feat/ci-cd` | 10 | Módulo 10: CI/CD e automação |
| 12 | `feat/professional-workflows` | 11 | Módulo 11: fluxos profissionais |
| 13 | `feat/security-governance` | 12 | Módulo 12: segurança e governança |
| 13.1 | `feat/learning-navigation` | 13 | Complementar: navegação contínua localizada, testes de regressão e documentação |
| 14 | `feat/advanced-git` | 13.1 | Módulos 13–14: Git avançado e internals |
| 15 | `feat/command-reference` | 14 | Módulo 15: referência de comandos |
| 16 | `feat/practical-projects` | 15 | Módulo 16: oito projetos práticos |
| 17 | `feat/challenges-interviews` | 16 | Módulo 17: desafios, quizzes e entrevistas; piloto de registros estruturados |
| 18 | `feat/learning-hub-contract` | 17 | Finalizar contrato, manifestos, schemas, fixtures do consumidor; avaliar playground opcional separadamente |
| 19 | `docs/release-handoff` | 18 | Identidade fornecida pelo mantenedor, README final, QA, handoff |

## Estrutura e workflow

Usar README.md na raiz e docs/localized/README.{pt-BR,es}.md; traduções de governança da raiz em docs/localized/. Pastas de módulos e capítulos usam README.md, README.pt-BR.md, README.es.md, examples/ compartilhado quando necessário. Arquitetura e specs com traduções irmãs. assets/, scripts/, tests/, .github/ e pastas curriculares só quando úteis. Não criar diretórios vazios. Ativos visuais oficiais adiados. Antes de cada sprint, ler main e instruções aplicáveis, delimitar escopo, criar branch da main atual, implementar idiomas, rodar checks disponíveis, revisar cada arquivo, inspecionar privacidade, abrir PR, verificar CI e solicitar Codex Review se disponível, tratar apontamentos e revalidar último SHA, registrar evidências, obter aprovação do mantenedor, squash merge, verificar main e exclusão da branch, preparar handoff.

## Estratégia de validação

Bootstrap Sprint 00: apenas checks documentais, sem CI. Sprint 02 adiciona presença de idiomas, links, navegação, estrutura, exemplos em allowlist, detecção de segredos e jobs Linux/Windows; sprints seguintes adicionam testes determinísticos de estado/conflito/recuperação e validação de schema/ID/referência quando registros existirem. Usar biblioteca padrão quando suficiente, diretórios temporários e configuração Git isolada; verificar refs, index, árvore e arquivos em vez de hashes frágeis ou saída localizada. Nunca executar submissões arbitrárias de estudantes em CI privilegiado. Checks obrigatórios exigem autorização separada após conhecer nomes/execuções reais.

## Documentos relacionados

- [Constitution](../constitution.pt-BR.md)
- [Especificação](specification.pt-BR.md)
- [Tarefas](tasks.pt-BR.md)
- [Critérios de aceite](acceptance-criteria.pt-BR.md)
- [Roadmap](../../roadmap.pt-BR.md)
