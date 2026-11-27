# Contrato de integração Learning Hub

[English](integration-contract.md) · [Português](integration-contract.pt-BR.md) · [Español](integration-contract.es.md)

Contrato 1.0.0 proposto para revisão da Sprint 18. Escopo: somente Git Study Guide. Repositório público é autoritativo; use JSON/Markdown UTF-8 em build time, nunca scraping HTML ou API GitHub por visitante. Consumidor mantém lock externo aprovado com revision SHA-1 completo de 40 caracteres, guide_id=git-study-guide, manifest_version=1.0.0, assessment_version=1 e command_catalog_version=1. Somente versões exatas; rejeitar revisões ausentes, não suportadas ou misturadas. Sem SHA autoembutido; selecionar commit aprovado após merge e CI da main. Nenhuma tag de release ou pin ativo do site é criado aqui.

## Versão e transporte

curriculum/manifest.json é inventário gerado de 18 módulos e 141 capítulos (423 caminhos localizados de conteúdo). Títulos de módulos vêm de H1 dos índices localizados; títulos de capítulos vêm dos rótulos existentes de índices localizados. IDs congelados são slug do módulo ou module.slug (incluindo slug numerado existente); nunca renumere caminhos ou reutilize IDs quando a ordem mudar. Ordens contíguas, base zero entre irmãos. previous_id/next_id globais percorrem capítulos com null nas extremidades; navegação Markdown mantém índices de módulos adjacentes. Títulos e caminhos têm exatamente en (padrão), pt-BR e es. Kinds: lesson, reference, project e assessment. Assets e resources referenciam arquivos rastreados; resources não são allowlist de execução.

## Fontes canônicas e relações

Quatro bancos referenciam records.json existentes (schema_version inteiro 1); catálogo tem 14 categorias, registros de categorias e intenções e envelopes catalog.json (schema_version inteiro 1). Sem duplicação de corpos. Validadores assessment-pilot e command-catalog permanecem autoritativos para semântica completa. quiz_ids, exercise_ids e interview_ids identificam capítulo do banco e relações de pré-requisitos documentadas, não propriedade inferida de capítulo; mock_ids identifica só capítulo de simulados. command_ids identifica categoria proprietária e capítulos relacionados documentados. Ordem canônica dos bancos. Reconstrução exata valida todas relações; simulados resolvem IDs de quiz/desafio/entrevista e dificuldade igual. Contagens desta revisão: 36 quizzes, 12 desafios, 24 entrevistas, três simulados, 120 operações. Todos públicos, soluções e rubricas visíveis.

## Compatibilidade e migração

Comparado em modo somente leitura ao commit Python Study Guide a8a264f9f36ec276f0ad8e35f10f2d76f82fe211. Convenções comuns: mapas de idiomas, ordem explícita, revisão imutável, relações tipadas, caminhos seguros, rejeição de versões desconhecidas, namespace do guia, autoavaliação orientativa. Manifesto Git adiciona guide_id, command_catalog, kinds reference/assessment e command_ids; descritores apontam registros agregados em vez de índices Python. Tipo quiz Git single-choice e answer string mapeiam explicitamente a multiple_choice e answer.choice_id se adaptados a UI estilo Python; listas ordenadas de mapas de idiomas podem ser transpostas em arrays por idioma. Pré-requisitos Git são muitos-para-muitos; não invente propriedade chapter_id, XP ou campos de teste de código Python. Preserve IDs e versões de bancos existentes. Não importe registros Git como válidos pelo schema Python; use adaptador específico. Nenhuma mudança em Python ou Learning Hub.

## Procedimento e segurança do consumidor

Quatro schemas estruturais Draft 2020-12 documentam manifesto, bancos de avaliação, catálogo e lock externo. Validador Python sem dependências aplica JSON estrito (chaves duplicadas, números não finitos e tokens fracionários rejeitados), manifesto regenerado exato, inventário de idiomas/caminhos, semântica dos bancos, relações tipadas, contagens e versões. Validação estrutural JSON Schema sozinha não comprova existência, unicidade por ID, semântica ou integridade referencial; use checks estruturais e semânticos nas integrações. Autoria: prepare mudanças fonte, rode python scripts/learning_hub_contract.py --write, prepare manifesto, depois python scripts/validate.py --check learning-hub-contract e suíte completa. Sem rede ou nova dependência.

Consumidor de referência confiável scripts/learning_hub_consumer.py recebe lock externo e base de objetos Git SHA-1 local confiável e completa para o snapshot. Verifica commit solicitado, desabilita objetos de substituição e protocolos de rede, lê blobs regulares 100644 por ID sem filtros de checkout, confere tamanhos e hashes de blobs Git, exporta para staging novo isolado, rejeita traversal, symlinks, entradas executáveis/submódulos, colisões, arquivos ausentes/extras/modificados e compara igualdade JSON dos schemas suportados confiáveis fora do snapshot. Usa validadores confiáveis, nunca importa código do snapshot. Limites: 3000 arquivos, 32 MiB snapshot total, 60 s por chamada Git. Valide candidato antes de adotar pin; em falha mantenha anterior aprovado; rollback é reselecionar SHA completo. Testes usam commit real selecionado e dados sintéticos de duas revisões, não site real ou release assinada independentemente. Confie base de objetos, binário Git e staging privado; sem verificação de assinatura ou sandbox para filesystem concorrente hostil. Renderizador deve sanitizar Markdown/HTML, links, assets e URLs; sem execução de conteúdo arbitrário.

## Responsabilidade e execução

Guia possui conteúdo, metadados, soluções públicas, QA de referência e validação de schema. Site possui UI/renderização segura, acessibilidade, progresso, isolamento e deploy. Projetos/desafios Git nativos são local_only com razões localizadas; outros capítulos unverified. Browser_compatible não é suportado no contrato v1; nenhum runtime validado ou introduzido. Quizzes comparam IDs exatos; entrevistas/simulados usam rubrica manual explícita, nunca correção IA. Predicados de desafio são fixtures QA locais confiáveis, não executor arbitrário de alunos; estado final não prova segurança de ações intermediárias. Progresso navegador específico do dispositivo e pode ser apagado. Veja decisão playground opcional.

## Documentos relacionados

- [Manifest](../../../curriculum/manifest.json)
- [Manifest schema](../../../schemas/curriculum-manifest.schema.json)
- [Assessment schema](../../../schemas/assessment-bank.schema.json)
- [Command catalog schema](../../../schemas/command-catalog.schema.json)
- [Revision lock schema](../../../schemas/revision-lock.schema.json)
- [Reference consumer](../../../scripts/learning_hub_consumer.py)
- [Specification](specification.pt-BR.md)
- [ADR 0004](../../adr/0004-learning-hub-integration.pt-BR.md)
- [ADR 0006](../../adr/0006-browser-playground.pt-BR.md)
- [Python reference snapshot](https://github.com/RamonRDR/python-study-guide/blob/a8a264f9f36ec276f0ad8e35f10f2d76f82fe211/docs/specs/learning-hub-foundation/integration-contract.md)
