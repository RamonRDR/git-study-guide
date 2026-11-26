# Critérios de aceite

[English](acceptance-criteria.md) · [Português](acceptance-criteria.pt-BR.md) · [Español](acceptance-criteria.es.md)

Fundação aprovada e integrada pelo PR #1 em 25/11/2026. Mudanças seguintes exigem revisão e aprovação explícita do mantenedor.

| ID | Sprint | Condição observável de aceite |
| --- | --- | --- |
| AC-00 | 00 | Auditar baseline e ruleset; 11 documentos principais em três idiomas mais índices, auditoria, roadmap e README provisório; requisitos/decisões alinhados; links e presença de idiomas verificados; evidências do último PR, sem CI inventado; aprovação antes do merge. |
| AC-01 | 01 | Documentos de governança e templates localizados; autoria e papéis da IA explícitos; segurança e suporte utilizáveis; sem alegação de afiliação. |
| AC-02 | 02 | Validadores rejeitam idiomas ausentes, links quebrados, caminhos/navegação inválidos e exemplos inseguros ou não aprovados; CI Linux/Windows com menor privilégio; evidência de execução; configuração de status checks aprovada separadamente. |
| AC-03 | 03 | Todos os tópicos 00–01 ensinados; primeiro commit reproduzível; instruções por SO verificadas ou limitações declaradas; história referenciada. |
| AC-04 | 04 | Módulos 02–03 explicam estados e efeitos; testes verificam staging/commit/diff; diagrama acessível. |
| AC-05 | 05 | Exemplos locais do 04 validam refs, troca e detached HEAD; prática remota adiada; avisos de exclusão. |
| AC-06 | 06 | Módulo 05 valida topologias distintas, conflito/abort/continue e efeitos de squash/rebase; sem exercício destrutivo em histórico compartilhado. |
| AC-07 | 07 | Módulo 06 usa origin bare e dois clones; verifica tracking, divergência e sincronização; autenticação online opcional, segura e documentada. |
| AC-08 | 08 | Módulo 07 distingue desfazer e reescrever histórico; testes de recuperação e limites; labs destrutivos descartáveis com inspeção/limpeza. |
| AC-09 | 09 | Módulo 08 cobre recursos GitHub, fluxo PR/review/proteção, distinção de Git; tarefas com conta opcionais e fontes oficiais atuais. |
| AC-10 | 10 | Módulo 09 cobre MRs GitLab, grupos, runners, proteção e comparação; prática hospedada opcional e fontes oficiais atuais. |
| AC-11 | 11 | Módulo 10 distingue CI/entrega/deploy; exemplos YAML seguros das duas plataformas; testar/lint conforme aplicável; sem pipeline privilegiado não confiável. |
| AC-12 | 12 | Módulo 11 compara trade-offs de workflows, SDD/TDD, prática manual, reviews e releases com cenários originais. |
| AC-13 | 13 | Módulo 12 cobre proteção de credenciais, menor privilégio, assinatura, cadeia de suprimentos e resposta a incidentes; nunca expor segredos reais. |
| AC-13.1 | 13.1 | Cada índice de módulo e capítulo tem navegação localizada idêntica no topo e rodapé; extremos dos capítulos levam aos índices dos módulos adjacentes; limites, idioma e ordem corretos garantidos por testes determinísticos de regressão. Conteúdo e caminhos estáveis preservados. |
| AC-14 | 14 | Módulos 13–14 ensinam operações avançadas e internals de objetos/refs; testes seguros e limitados, diagramas corretos; requisitos de versão identificados. |
| AC-15 | 15 | Catálogo com pelo menos 101 IDs de entradas relevantes distintos; reportar contagens por categoria separadamente e validar campos, riscos e fontes. |
| AC-16 | 16 | Oito projetos em três idiomas com preparação, objetivos, estados esperados, limpeza, soluções e testes; tarefas dependentes de conta opcionais. |
| AC-17 | 17 | Desafios e entrevistas mapeiam pré-requisitos, têm dicas, soluções, explicações, rubricas objetivas e checks determinísticos que rejeitam estados incorretos representativos; schema piloto documentado. |
| AC-18 | 18 | Manifesto e schemas versionados rejeitam caminhos inválidos, idiomas ausentes, IDs duplicados, refs pendentes e versões não suportadas; fixture consome revisão imutável; ADR de playground opcional registra compatibilidade, isolamento, limites e custo. |
| AC-19 | 19 | Três READMEs finais e ativos visuais aprovados (ou exceção adiada explícita), badges reais, QA aplicável completo, limitações registradas, handoff revisado, aprovação e evidência da revisão imutável. |

## Definição global de pronto

Todos os documentos públicos afetados alinhados nos três idiomas; fontes/links/estrutura verificados; checks relevantes executados ou ausência declarada; sem apontamentos relevantes pendentes, segredos ou alterações não relacionadas; evidência de tarefas atual; última revisão do PR revisada e mantenedor autoriza squash merge. Checks estruturais não provam paridade conceitual; revisão humana continua necessária. CI ausente não é CI aprovado. Sprint 00 não pode ser marcada integrada antes do merge.

## Documentos relacionados

- [Especificação](specification.pt-BR.md)
- [Tarefas](tasks.pt-BR.md)
