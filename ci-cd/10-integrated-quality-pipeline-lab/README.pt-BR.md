# Laboratório de pipeline de qualidade integrado

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../09-quality-gates-and-troubleshooting/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo módulo](../../professional-workflows/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 45 min

**Pré-requisitos:** [GitHub](../../github/README.pt-BR.md) · [GitLab](../../gitlab/README.pt-BR.md) · [Quality gates e diagnóstico](../09-quality-gates-and-troubleshooting/README.pt-BR.md)

**Objetivo:** Reproduzir checks aprovados e falhos offline e conectá-los a pipeline profissional.

## O que é e por quê

Pipeline pode combinar lint e testes sem dependência de linguagem de programação. Catálogo fictício deve ser não vazio e conter linha exata `status: ready`. Primeiro comando é verificação estrutural, segundo assertiva simples de conteúdo; nenhum é lint abrangente ou teste de aplicação. Mesmos checks shell aparecem nos exemplos GitHub/GitLab dos capítulos 03 e 04. Execute só exemplo local limitado abaixo em Bash no Linux/macOS ou Git Bash no Windows, não PowerShell ou cmd. Cria diretório temporário isolado, dispensa configuração Git, rede, Python, credenciais e hospedagem, e remove apenas dois arquivos que criou e diretório temporário vazio. Reporta três resultados esperados; casos falhos são testados deliberadamente, não suprimidos como checks de conteúdo aprovados.

```bash
(
  set -eu
  sandbox=$(mktemp -d)
  printf 'Sandbox: %s\n' "$sandbox"
  trap 'rm -f -- "$sandbox/catalog.txt" "$sandbox/empty.txt"; rmdir -- "$sandbox"' EXIT
  check_catalog() {
    test -s "$1" && grep -Fxq 'status: ready' "$1"
  }
  printf '%s\n' 'status: ready' > "$sandbox/catalog.txt"
  check_catalog "$sandbox/catalog.txt"
  printf '%s\n' 'PASS ready'
  printf '%s\n' 'status: draft' > "$sandbox/catalog.txt"
  if check_catalog "$sandbox/catalog.txt"; then
    exit 1
  fi
  printf '%s\n' 'PASS wrong rejected'
  : > "$sandbox/empty.txt"
  if check_catalog "$sandbox/empty.txt"; then
    exit 1
  fi
  printf '%s\n' 'PASS empty rejected'
)
```

## Prática

Leia script e execute bloco inteiro como escrito em shell descartável. Saída esperada: `PASS ready`, `PASS wrong rejected`, `PASS empty rejected`, status de saída zero. Primeiro teste usa arquivo ready; segundo arquivo não vazio incorreto; terceiro vazio. Equipe profissional versionaria só checks revisados, usaria ferramentas reais de lint/teste adequadas, exigiria ambos ambientes se necessário, inspecionaria revisões exatas e separaria implantação de produção. Prática hospedada opcional não exigida; use só repositório descartável próprio se uso gratuito e isolamento forem verificados, nunca habilite implantação.

## Erros comuns e segurança

Se setup falhar, pare. Nunca substitua diretório temporário por caminho de projeto real. Trap de limpeza remove só arquivos conhecidos; se falhar, inspecione caminho temporário impresso, não use remoção recursiva em caminhos desconhecidos. Se check passar ou falhar inesperadamente, inspecione conteúdo e código de saída; não enfraqueça assertiva. Aula manual, não arquivo executado automaticamente pelo guia.

## Exercício e autocorreção

Passe se três mensagens esperadas aparecerem, explicar por que entradas incorreta/vazia falham e identificar mesmos comandos nos dois YAMLs. Sandbox aprovado não prova execução hospedada.

## Referência rápida

`test -s` / `grep -Fxq` / exit status

## Fontes oficiais

- <https://www.gnu.org/software/bash/manual/html_node/Exit-Status.html>
- <https://www.gnu.org/software/grep/manual/grep.html>
- <https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax>
- <https://docs.gitlab.com/ci/yaml/>

---

<!-- navigation-footer -->
[Anterior](../09-quality-gates-and-troubleshooting/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo módulo](../../professional-workflows/README.pt-BR.md)
<!-- /navigation-footer -->
