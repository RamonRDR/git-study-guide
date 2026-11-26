# Versionamento semântico

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../06-conventional-commits/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../08-code-review/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 35 min

**Pré-requisitos:** [CI/CD](../../ci-cd/README.pt-BR.md) · [Conventional Commits](../06-conventional-commits/README.pt-BR.md)

**Objetivo:** Escolher versão compatível e interpretar precedência.

## O que é e por quê

SemVer 2.0.0 descreve versões conforme API pública declarada (contrato usado por consumidores, não necessariamente API HTTP). Para versões estáveis, incremente MAJOR para mudanças incompatíveis, MINOR para funcionalidades retrocompatíveis e PATCH para correções retrocompatíveis; zere componentes inferiores quando superior aumenta. Major zero é desenvolvimento inicial de API instável. Pré-release `2.0.0-rc.1` tem precedência menor que versão normal correspondente; metadados após `+` não afetam precedência. Conteúdo de versão publicada não deve ser modificado. Tag Git `v1.4.2` pode nomear commit da versão SemVer `1.4.2`; prefixo é convenção de tag, não parte da string SemVer.

## Prática

A partir da API 1.4.2 do catálogo, escolha próxima versão para cada cenário independente: corrigir erro sem mudar API; adicionar campo opcional retrocompatível; remover campo obrigatório de resposta. Compare `2.0.0-rc.1` com `2.0.0` e `1.4.2+build.7` com `1.4.2+build.8`. Declare contrato e identifique impacto real aos consumidores antes de decidir.

## Riscos e recuperação

Tipo de mensagem evidencia intenção, não comprova compatibilidade. Nunca substitua silenciosamente conteúdo publicado ou mova tag de release. Se release incorreta, siga política de remediação e publique nova versão corrigida; comunique consumidores afetados.

## Exercício e autocorreção

Resultados independentes: 1.4.3, 1.5.0, 2.0.0. Release candidate precede versão normal; versões com metadados de build têm precedência igual.

## Referência rápida

MAJOR.MINOR.PATCH / pre-release / build metadata

## Fontes

- <https://semver.org/spec/v2.0.0.html>
- <https://www.conventionalcommits.org/en/v1.0.0/>
- <https://git-scm.com/docs/git-tag>
