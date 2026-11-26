# Estrutura do projeto

[English](project-structure.md) · [Português](project-structure.pt-BR.md) · [Español](project-structure.es.md)

A raiz contém governança, licença MIT e 18 índices estáveis de módulos. docs/ contém arquitetura, especificações, traduções e orientações de engenharia. scripts/ contém validação com biblioteca padrão e registro interno do currículo; tests/ contém fixtures determinísticas. .github/ contém templates e CI. Assets serão adicionados somente quando necessários. O registro é interno, não o schema final do Learning Hub.

Capítulos usam NN-topic/README.md, README.pt-BR.md e README.es.md. Registrar slugs em scripts/curriculum.json em ordem numérica e vinculá-los no bloco chapters. Cada índice de módulo e capítulo tem navegação localizada idêntica nos blocos navigation e navigation-footer, o primeiro após título e seletor de idioma e o segundo no fim. Usar anterior/índice/próximo nessa ordem. Primeiro e último capítulos apontam aos índices dos módulos adjacentes (inclusive reservados), com rótulos Módulo anterior/Próximo módulo. Só direções ausentes nos extremos do roadmap usam travessão sem link. Índices dos módulos apontam a índices adjacentes e à trilha. As funções navigation_entries e navigation_line do validador definem destinos e rótulos canônicos. Manter caminhos estáveis e não criar diretórios vazios.

- [Trilha](learning-path.pt-BR.md)
- [Automação de qualidade](quality-automation.pt-BR.md)
