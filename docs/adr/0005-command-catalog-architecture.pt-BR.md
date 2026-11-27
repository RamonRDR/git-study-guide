# ADR 0005: Arquitetura do catálogo de comandos

[English](0005-command-catalog-architecture.md) · [Português](0005-command-catalog-architecture.pt-BR.md) · [Español](0005-command-catalog-architecture.es.md)

Status: implementação da Sprint 15 aprovada pelo mantenedor; integração pendente de revisão.

## Decisão

Manter um documento JSON UTF-8 canônico por categoria registrada de command-reference, com versão de schema local, IDs estáveis em minúsculas, valores técnicos compartilhados e mapas explícitos en/pt-BR/es para textos educacionais. Gerar as três páginas da categoria e o índice do módulo deterministicamente com a biblioteca padrão Python. Versionar o Markdown gerado para leitura direta no GitHub; não editá-lo separadamente. Usar o registro curricular e as funções canônicas de navegação existentes. Construir índices por categoria e intenção a partir dos mesmos registros.

Validar quantidade (mínimo de 101 operações relevantes, meta de 120), unicidade, campos, riscos, fontes, referências a capítulos, mapas de idiomas e igualdade do conteúdo gerado. Distinguir comandos nativos, subcomandos, usos de opções, fluxos, ferramentas externas e operações de plataforma. Não executar automaticamente os comandos do catálogo.

## Alternativas e consequências

Manter JSON e Markdown manualmente duplica conteúdo; um catálogo exclusivo do site impede a leitura independente no GitHub. Nenhuma dessas opções foi adotada. Validação estrutural não comprova precisão técnica ou tradução semântica. Revisar separadamente exemplos reais, requisitos de versão e fontes oficiais. Este é um piloto interno, não um schema definitivo ou consumidor do Learning Hub; a Sprint 18 continua responsável pelo contrato final. Sem serviço pago ou dependência adicional.

- [Índice de ADRs](README.pt-BR.md)
- [Contrato de integração](../specs/project-foundation/integration-contract.pt-BR.md)
