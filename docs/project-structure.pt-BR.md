# Estrutura do projeto

[English](project-structure.md) · [Português](project-structure.pt-BR.md) · [Español](project-structure.es.md)

A raiz contém governança, licença MIT e 18 índices estáveis de módulos. docs/ contém arquitetura, especificações, traduções e orientações de engenharia. scripts/ contém validação com biblioteca padrão e registro interno do currículo; tests/ contém fixtures determinísticas. .github/ contém templates e CI. Assets serão adicionados somente quando necessários. O registro é interno, não o schema final do Learning Hub.

Capítulos usam NN-topic/README.md, README.pt-BR.md e README.es.md. Registrar slugs em scripts/curriculum.json em ordem numérica e vinculá-los no bloco chapters. Cada índice de módulo e capítulo tem navegação localizada idêntica nos blocos navigation e navigation-footer, o primeiro após título e seletor de idioma e o segundo no fim. Usar anterior/índice/próximo nessa ordem. Primeiro e último capítulos apontam aos índices dos módulos adjacentes (inclusive reservados), com rótulos Módulo anterior/Próximo módulo. Só direções ausentes nos extremos do roadmap usam travessão sem link. Índices dos módulos apontam a índices adjacentes e à trilha. As funções navigation_entries e navigation_line do validador definem destinos e rótulos canônicos. Manter caminhos estáveis e não criar diretórios vazios.

O módulo 15 usa um catalog.json canônico por categoria, mais registros de categorias e intenções em scripts/. As páginas Markdown trilíngues são geradas desses registros com scripts/render_command_reference.py e o registro de navegação existente. Edite JSON em vez das páginas geradas; consulte [ADR 0005](adr/0005-command-catalog-architecture.pt-BR.md). É piloto interno, não contrato final de integração.

O módulo 16 oferece oito projetos trilíngues de execução manual em practical-projects/. Cada um usa ambiente descartável novo, estados explícitos de aceite e solução pública de referência. Preparação compartilhada vem do projeto 01; sem artefatos executáveis de aluno ou novas dependências. Testes fixos em tests/test_git_practical_projects.py reproduzem independentemente os estados pretendidos. Bash/Git Bash para alunos; biblioteca padrão Python para QA do repositório.

- [Trilha](learning-path.pt-BR.md)
- [Automação de qualidade](quality-automation.pt-BR.md)

- [Schema do piloto de avaliações](assessment-pilot.pt-BR.md)

curriculum/ contém manifesto público versionado gerado; schemas/ contém quatro schemas de intercâmbio Draft 2020-12. Registro curricular interno permanece fonte de autoria. Consumidor confiável de referência importa tree Git fixada sem executar seu código. Veja contrato de integração para mapeamento específico e limites.

- [Contrato de integração Learning Hub](specs/project-foundation/integration-contract.pt-BR.md)
