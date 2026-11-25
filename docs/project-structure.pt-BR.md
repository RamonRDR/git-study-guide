# Estrutura do projeto

[English](project-structure.md) · [Português](project-structure.pt-BR.md) · [Español](project-structure.es.md)

A raiz contém governança, licença MIT e 18 índices estáveis de módulos. docs/ contém arquitetura, especificações, traduções e orientações de engenharia. scripts/ contém validação com biblioteca padrão e registro interno do currículo; tests/ contém fixtures determinísticas. .github/ contém templates e CI. Assets serão adicionados somente quando necessários. O registro é interno, não o schema final do Learning Hub.

Capítulos usam NN-topic/README.md, README.pt-BR.md e README.es.md. Registrar slugs em scripts/curriculum.json em ordem numérica; vinculá-los no bloco chapters e usar o bloco navigation para anterior, índice e próximo. Extremos não possuem link na direção ausente. A navegação dos módulos segue o roadmap. Manter caminhos estáveis e não criar diretórios vazios.

- [Trilha](learning-path.pt-BR.md)
- [Automação de qualidade](quality-automation.pt-BR.md)
