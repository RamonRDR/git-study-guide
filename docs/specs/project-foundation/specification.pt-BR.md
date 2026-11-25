# Especificação da fundação

[English](specification.md) · [Português](specification.pt-BR.md) · [Español](specification.es.md)

Proposta para revisão do mantenedor; não autoriza iniciar a Sprint 01.

Objetivo: Git Study Guide público, prático, MIT, do iniciante à engenharia avançada. Baseline main: b4bd782519ebc8e52e6751362443aa634e86e56d. Referência Python: 9102bbbf8f8dd846f2fb9682dd3f55bcacc10c95.

## Requisitos funcionais

- FR-01 — Publicar conteúdo independente EN/PT-BR/ES com seletores de idioma, navegação anterior/índice/próximo, caminhos estáveis e pré-requisitos explícitos. Seguir o roadmap sem exigir Python.
- FR-02 — Ensinar história, arquitetura, operações locais, branches, remotes, estratégias de merge, recuperação, plataformas, CI/CD, fluxos profissionais, segurança e internals. Distinguir Git nativo de recursos de hospedagem e explicar mudanças de estado.
- FR-03 — Cada lição aplicável inclui objetivo, nível, pré-requisitos, tempo de estudo, definição, razão/problema, sintaxe, quando usar/evitar, relações, internals, exemplos básico/profissional, erros, risco/recuperação, exercício, checklist, referência rápida e fontes oficiais. Adaptar com justificativa; não introduzir termos indefinidos.
- FR-04 — Catalogar 100+ comandos/operações relevantes; ID estável, categoria, objetivo, sintaxe, pré-requisitos, opções, uso/evitar, exemplo e resultado, estado afetado, efeitos colaterais, risco, alternativas, erros, recuperação, versão mínima quando relevante, referências oficiais e tags de intenção. Não inflar contagem de subcomandos distintos.
- FR-05 — Usar diagramas acessíveis com explicações localizadas para estado, refs, histórico, branch/merge/rebase, divergência, cherry-pick, reflog, objetos, colaboração e CI/CD. Avaliar Mermaid/SVG; validar topologia e alternativas textuais.
- FR-06 — Oferecer oito projetos práticos com repositórios temporários, origin bare e clones Alice/Bob; atividades exclusivas de plataformas opcionais. Incluir preparação, condições de sucesso, inspeção, limpeza e recuperação segura.
- FR-07 — Fornecer quizzes, desafios e registros de entrevistas com IDs estáveis, três idiomas, pré-requisitos, dicas progressivas, respostas de referência, verificações determinísticas de estado e rubricas objetivas; respostas abertas por autoavaliação.
- FR-08 — Implementar governança, orientação trilíngue de desenvolvimento assistido por IA, templates e quality gates automatizados; README provisório agora, identidade e README final na Sprint 19 com badges verificáveis.
- FR-09 — Fornecer manifesto versionado, schemas, locale maps, IDs estáveis, caminhos relativos seguros, capacidades de exercícios, fixtures validadas e handoff de revisão aprovada; alinhar ao contrato Python sem decisões unilaterais de schema universal.

## Requisitos não funcionais

- NFR-01 — Custo adicional zero; sem serviços pagos ou IA obrigatória. Verificar limites gratuitos antes de depender de serviços externos.
- NFR-02 — Paridade conceitual em toda documentação pública, inclusive templates; preservar MIT, autoria e caminhos publicados; sem informações privadas.
- NFR-03 — Validar links, estrutura, navegação, exemplos, estado, conflitos, recuperação, Linux/Windows, schemas, IDs, referências e segredos; macOS quando justificado. Usar exemplos confiáveis em allowlist, diretórios temporários e menor privilégio; sem CI privilegiado não confiável.
- NFR-04 — Sem runtime obrigatório do site, avaliação por IA, servidores pagos ou execução arbitrária privilegiada. Playground no navegador opcional e não verificado até avaliação.
- NFR-05 — Revisar e registrar evidências reais de validação; nunca inventar métricas, aprovações ou resultados. Manter exemplos originais e independência de fornecedores oficiais.

## Escopo e fontes

Sprint 00: somente fundação, sem lições, site, runtime, logomarca, outros repositórios, alterações administrativas ou mudanças no Python. Sprints seguintes exigem dependências aprovadas. Priorizar [documentação Git](https://git-scm.com/docs), [Pro Git](https://git-scm.com/book/en/v2), [GitHub Docs](https://docs.github.com/) e [GitLab Docs](https://docs.gitlab.com/); verificar fatos mutáveis antes de publicar. Guias futuros e template reutilizável ficam adiados até amadurecimento de Python e Git.

## Documentos relacionados

- [Constitution](../constitution.pt-BR.md)
- [Plano de implementação](implementation-plan.pt-BR.md)
- [Tarefas](tasks.pt-BR.md)
- [Critérios de aceite](acceptance-criteria.pt-BR.md)
- [Contrato de integração](integration-contract.pt-BR.md)
- [Guias relacionados](related-guides.pt-BR.md)
- [Decisões arquiteturais](../../adr/README.pt-BR.md)
- [Roadmap](../../roadmap.pt-BR.md)
- [Auditoria inicial](audit.pt-BR.md)
