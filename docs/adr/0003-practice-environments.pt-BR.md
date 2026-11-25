# ADR 0003: Ambientes de prática

[English](0003-practice-environments.md) · [Português](0003-practice-environments.pt-BR.md) · [Español](0003-practice-environments.es.md)

Proposta para revisão do mantenedor; não autoriza iniciar a Sprint 01.

## Contexto

Mudanças de estado Git podem destruir trabalho e serviços remotos exigem contas; prática deve permanecer gratuita.

## Decisão

Usar Git instalado em diretórios temporários descartáveis, origin bare e múltiplos clones. Isolar identidade/config, hooks e credenciais; evitar remotes reais por padrão. Marcar tarefas exclusivas de plataformas como opcionais. Inspecionar estado antes de comandos destrutivos e limpar só caminhos temporários próprios; nunca usar o repositório do guia.

## Alternativas

Rejeitar labs hospedados obrigatórios e shell remoto (custo, credenciais, isolamento); adiar simulador/runtime no navegador até ADR separada na Sprint 18.

## Consequências

Verificar estado deterministicamente, testar Linux/Windows, documentar versões suportadas e diferenças de shell. Sem garantia de recuperação após operações destrutivas. Simulador no navegador não deve alegar fidelidade sem teste.

## Documentos relacionados

- [Índice ADR](README.pt-BR.md)
- [Contrato de integração](../specs/project-foundation/integration-contract.pt-BR.md)
