# Desenvolvimento guiado por testes (TDD)

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../09-spec-driven-development/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../11-ai-assisted-development/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 40 min

**Pré-requisitos:** [CI/CD](../../ci-cd/README.pt-BR.md) · [Desenvolvimento guiado por especificação (SDD)](../09-spec-driven-development/README.pt-BR.md)

**Objetivo:** Explicar red, green e refactor sem confundir falha de teste com erro de ferramenta.

## O que é e por quê

TDD é prática iterativa de programação: escreva pequeno teste que falha pelo comportamento ausente pretendido (red), implemente mínimo para passar (green), depois melhore estrutura mantendo testes aprovados (refactor). Refatoração muda estrutura interna sem alterar intencionalmente comportamento observável. Teste posterior à implementação ainda é útil, mas não evidencia ciclo red-first. SDD define o necessário; TDD ajuda implementar e verificar pequenos comportamentos. Nenhum exige linguagem, IA, modelo de branch ou commit automático a cada cor. Assertiva de conteúdo shell ilustra feedback red/green; não é framework abrangente de teste unitário.

```text
red -> green -> refactor -> next test
```

## Prática

Antes do capítulo 13, preveja resultado de `grep -Fxq 'status: ready' catalog.txt` quando arquivo existente contém draft. Depois preveja após escrever linha exata ready. Para refatoração, imagine extrair check em função nomeada mantendo entradas e comportamento de saída; repita casos positivo, valor errado e arquivo ausente. Distinga erro de ferramenta/arquivo ausente de falha significativa da assertiva. Não exige experiência em programação para rastrear resultados.

## Riscos e recuperação

Nunca force green apagando assertiva, aceitando toda entrada ou suprimindo falha. Inspecione motivo; se teste errado, corrija transparentemente. Mantenha integração compartilhada verde; se registrar commits red intermediários localmente, não integre revisão quebrada. Exemplo aprovado não é cobertura exaustiva.

## Exercício e autocorreção

Red esperado: sem correspondência em draft existente (grep saída 1). Green: linha exata encontrada (saída 0). Erro operacional não demonstra red válido. Refatoração deve preservar resultados.

## Referência rápida

red / green / refactor

## Fontes

- <https://agilealliance.org/glossary/tdd/>
- <https://www.gnu.org/software/grep/manual/grep.html>
