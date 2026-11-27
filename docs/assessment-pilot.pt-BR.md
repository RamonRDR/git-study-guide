# Schema do piloto de avaliações

[English](assessment-pilot.md) · [Português](assessment-pilot.pt-BR.md) · [Español](assessment-pilot.es.md)

Piloto interno Sprint 17, schema_version 1. Não é contrato publicado Learning Hub. Quatro arquivos canônicos em exercises/ armazenam envelope com schema_version, kind e records. Inglês é primário; cada string de aluno é mapa não vazio exatamente en, pt-BR e es. IDs são tokens minúsculos com hífen prefixados pelo tipo. Dificuldade easy, medium ou hard. Pré-requisitos nomeiam caminhos de módulo/capítulo anteriores registrados. Sem conteúdo executável ou credenciais. Ordem de registros é ordem de apresentação.

## Campos comuns

id, difficulty, prerequisites, title, prompt, hints, explanation. Dicas são mapas localizados ordenados; pré-requisitos resolvem capítulos existentes fora do módulo 17.

- Quiz: type single-choice, três choices com IDs únicos estáveis e texto localizado, answer é ID exato. Sem comparação aproximada.
- Desafio: estimated_minutes, setup, solution (passos localizados ordenados), execution=local_only, execution_reason, checks. Preparação aponta fixture isolada nova; soluções são instruções, não strings executáveis. Checks são predicados de estado tipados permitidos; sem caminhos, opções ou comandos arbitrários.
- Entrevista: expected_answer, rubric, follow_ups. Um ponto por critério de rubrica atendido, zero caso contrário; só autoavaliação.
- Simulado: duration_minutes, quiz_ids, challenge_ids, interview_ids, rubric. Referências resolvem tipo correto e mesma dificuldade. Quatro quizzes (4 pontos), um desafio (2), duas entrevistas (4), total 10.

Checks de estado usam status limpo, branch atual, bytes exatos commitados/index/trabalho, caminhos rastreados/não rastreados, igualdade/desigualdade de refs, ancestralidade, igualdade de tree, contagens de pais/commits, tipo de objeto tag e entradas não mescladas. Cada predicado tem conjunto exato de campos permitidos; nomes/valores de fixture restritos. assessment_state aceita somente callbacks controlados de fixtures QA confiáveis; não é sandbox nem executor público. Check final não prova caminho seguido pelo aluno nem segurança de operação intermediária; use evidência manual quando exigida. Não avalie repos não confiáveis nem execute código de aluno. Execução em navegador e contrato final ficam na Sprint 18.

O check assessment-pilot verifica quatro bancos versionados, contagens exatas por dificuldade, IDs globalmente únicos, pré-requisitos e referências de simulados válidos, campos localizados, escolhas, respostas, predicados de estado permitidos e igualdade com Markdown gerado. Edite records.json, prepare JSON e currículo, rode python scripts/render_assessments.py --write; prepare páginas geradas e rode python scripts/validate.py --check assessment-pilot e todos checks/testes. Os 12 cenários fixos de QA exercitam estados Git válidos e incorretos representativos. Nenhum avaliador executa submissões de alunos ou lê repos arbitrários; só fixtures descartáveis confiáveis são suportadas. Validação estrutural não prova tradução semântica ou exatidão educacional.

- [Module 17](../exercises/README.pt-BR.md)
- [Integration contract](specs/project-foundation/integration-contract.pt-BR.md)
- [Quality automation](quality-automation.pt-BR.md)
