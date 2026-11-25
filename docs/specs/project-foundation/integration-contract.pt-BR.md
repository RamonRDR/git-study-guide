# Contrato preliminar de integração Learning Hub

[English](integration-contract.md) · [Português](integration-contract.pt-BR.md) · [Español](integration-contract.es.md)

Direção normativa preliminar para pilotos; sem schema publicado ou consumidor implementado. Finalizar na Sprint 18 após pilotos da Sprint 17 e revisão coordenada com Python Study Guide.

## Versão e transporte

Importar Markdown/JSON UTF-8 em build time de um SHA Git imutável aprovado. Registrar revision e schema_version; rejeitar versões major desconhecidas, registros inválidos e revisões misturadas. Sem scraping HTML ou API GitHub por visitante. Default en, suportados en/pt-BR/es; campos visíveis exigem locale maps. IDs ASCII minúsculos com pontos/hífens, estáveis independentemente da ordem; únicos por tipo de entidade. Tupla proposta no consumidor (guide_id, entity_type, id), guide_id=git-study-guide; não altera unilateralmente contrato Python. Ordens explícitas não negativas únicas entre irmãos. Apenas caminhos POSIX relativos ao repositório: rejeitar traversal, caminhos absolutos, barras invertidas, esquemas e escapes por symlink; verificar existência, resolver na mesma revisão, sanitizar Markdown/HTML. Anterior/próximo segue ordem curricular, null nas extremidades.

## Campos propostos

| Entity | Fields |
| --- | --- |
| Curriculum | schema_version, default_locale, supported_locales, modules |
| Module | id, order, slug, title, index, chapters |
| Chapter | id, order, slug, title, content, assets, previous_id, next_id, exercise_ids, quiz_ids, interview_ids, execution |
| Quiz | id, chapter_id, difficulty, type, prompt, choices, answer, explanation, hints, xp |
| Exercise | id, chapter_id, difficulty, estimated_minutes, title, prompt, concepts, constraints, examples, starter_path or starter text, hints, solution_path, explanation, tests, execution, allowed_dependencies |
| Interview question | id, topic, level, prompt, expected_answer, explanation, intent, common_errors, follow_ups, examples, rubric |
| Mock | id, level, duration_minutes, question_ids, exercise_ids, scoring rubric |
| Command entry | id, category, command, intent_tags, purpose, syntax, prerequisites, options, examples, expected_state, risk, recovery, references |

Campos candidatos, não um schema. Preservar nomes comuns compatíveis do Python; prosa localizada inclui títulos, prompts, escolhas, dicas, explicações e rubricas. Dificuldade easy/medium/hard. Tipos de quiz objetivo e valores aceitos explícitos; XP apenas orientativo. Registros de comandos complementam campos FR-04. Testes Git descrevem preparação, operações permitidas, estado esperado e limites; comparar refs, ancestralidade, index, arquivos rastreados/não rastreados e conteúdos conforme aplicável, não hashes incidentais, horários, defaults de branch ou saída localizada. Testar estados incorretos representativos. Questões abertas usam respostas de referência e autoavaliação; soluções públicas são inspecionáveis.

## Execução e responsabilidades

Manter valores de execução compatíveis com Python: browser_compatible (somente após validação de runtime fixado), local_only (motivo obrigatório), unverified (padrão, sem execução automática no navegador). Propor metadados opcionais Git para simulação versus Git real e atividades com conta; finalizar após piloto, nunca inferir suporte. Labs Git nativos permanecem locais; sem site/runtime aqui. Avaliação do playground deve abordar fidelidade, operações suportadas, segurança, isolamento, persistência, acessibilidade, compatibilidade, cancelamento/limites de tempo/saída e custo adicional zero. Worker sozinho não é fronteira de segurança. Nunca executar comandos arbitrários privilegiados ou avaliação semântica por IA. Guia responde por conteúdo, metadados, soluções, testes e validação; site por renderização segura, UI, isolamento de runtime, progresso, acessibilidade e deploy. Progresso local do navegador é específico do dispositivo e pode ser apagado. Sem sincronização obrigatória via backend.

Referência (snapshot consultado): [Python contract](https://github.com/RamonRDR/python-study-guide/blob/9102bbbf8f8dd846f2fb9682dd3f55bcacc10c95/docs/specs/learning-hub-foundation/integration-contract.md).

## Documentos relacionados

- [Especificação](specification.pt-BR.md)
- [Decisões arquiteturais](../../adr/README.pt-BR.md)
