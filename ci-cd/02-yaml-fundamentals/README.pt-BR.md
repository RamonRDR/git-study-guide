# YAML e leitura de configuração

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../01-ci-delivery-and-deployment/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../03-github-actions/README.pt-BR.md)
<!-- /navigation -->

**Nível:** iniciante · **Tempo estimado:** 30 min

**Pré-requisitos:** [GitHub](../../github/README.pt-BR.md) · [GitLab](../../gitlab/README.pt-BR.md) · [Integração, entrega e implantação contínuas](../01-ci-delivery-and-deployment/README.pt-BR.md)

**Objetivo:** Ler mapeamentos, sequências, escalares e comandos multilinha antes de editar automação.

## O que é e por quê

YAML é formato de serialização de dados; plataforma atribui significado às chaves. Mapeamento associa chaves e valores; sequência usa hífens; escalares representam valores individuais. Indente consistentemente com espaços, nunca tabs para indentação. Use aspas quando pontuação ou tipos implícitos forem ambíguos. Escalar de bloco `|` preserva quebras de linha, enquanto `>` dobra várias quebras em espaços. Chaves duplicadas e aninhamento incorreto são defeitos mesmo se parser permissivo aceitar. Versões/parsers YAML podem interpretar palavras simples diferentemente; chave `on` de workflow é válida no GitHub, mas parser YAML 1.1 pode interpretá-la como booleano. Arquivo sintaticamente válido ainda pode violar schema da plataforma.

```yaml
project:
  name: "catalog"
  attempts: 2
  tasks:
    - check
    - report
  message: |
    First line
    Second line
```

## Prática

Offline, inspecione exemplo neutro abaixo. Encontre mapeamento, lista, string e inteiro; explique por que `check` pertence a `tasks`. Desenhe árvore antes e após desindentar `tasks` por engano. São apenas dados, não configuração CI.

## Erros comuns e segurança

Nunca cole segredos em YAML. Valide com schema da plataforma, não apenas parser genérico; nenhum editor externo é exigido. Inspecione diff e corrija indentação em cópia descartável.

## Exercício e autocorreção

`project` contém mapeamento; `tasks` contém sequência; `check` é item; `attempts` é inteiro. Passe se distinguir sintaxe de semântica da plataforma.

## Referência rápida

mapping / sequence / scalar

## Fontes oficiais

- <https://yaml.org/spec/1.2.2/>
- <https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax>
- <https://docs.gitlab.com/ci/yaml/>
