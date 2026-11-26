# Laboratório de fluxo profissional integrado

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../12-release-management/README.pt-BR.md) · [Índice](../README.pt-BR.md) · —
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 60 min

**Pré-requisitos:** [CI/CD](../../ci-cd/README.pt-BR.md) · [Gestão de releases](../12-release-management/README.pt-BR.md)

**Objetivo:** Verificar fluxo local seguro da especificação à tag.

## O que é e por quê

Lab offline conecta SDD, demonstração red/green, feature branch, revisão de diff, Conventional Commits, integração e tag anotada local. Neste exercício simplificado, contrato do catálogo permite explicitamente mudar campo status de draft para ready; suponha capacidade nova retrocompatível de prontidão e release anterior hipotética 1.0.0, então rótulo exemplo 1.1.0. Nenhuma tag anterior exigida. Check verifica uma linha exata, não comportamento completo. Primeiro commit representa base, segundo mudança focada. Fast-forward escolhido no exercício local porque main não divergiu; PRs reais do guia usam squash autorizado. Nenhum PR hospedado, review, implantação ou publicação é simulado como evento real de plataforma.

## Prática

Pré-requisitos: Git 2.28+ e Bash com mktemp/grep (Linux, macOS ou Git Bash no Windows); use shell comum limpo, nunca repo do guia. Escreva R1/AC1 do capítulo 09 antes de executar. Execute bloco em shell descartável; pare com saída inesperada. Cria diretório temporário, isola config global/system normal do Git, usa identidade fictícia e deixa sandbox para inspeção. Esperado: mensagem red, diff staged de uma linha, dois commits com main e tag no segundo, PASS final. Registre caminho, checks e limites como PR simulado. Remova sandbox depois pelo gerenciador de arquivos após confirmar caminho impresso. Simule revisor e aprovador de release separados; não infira aprovação real.

```bash
(
  set -eu
  sandbox=$(mktemp -d)
  printf 'Sandbox: %s\n' "$sandbox"
  unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE GIT_COMMON_DIR GIT_CONFIG_PARAMETERS
  export GIT_CONFIG_NOSYSTEM=1 GIT_CONFIG_GLOBAL="$sandbox/global-config" GIT_CONFIG_COUNT=0
  git init -b main "$sandbox/catalog"
  cd "$sandbox/catalog"
  git config user.name 'Catalog Learner'
  git config user.email 'learner@example.invalid'
  git config commit.gpgsign false
  git config tag.gpgsign false
  printf '%s\n' 'status: draft' > catalog.txt
  git add catalog.txt
  git commit -m 'chore: initialize catalog'
  git switch -c feat/ready-catalog
  if grep -Fxq 'status: ready' catalog.txt; then
    exit 1
  else
    test "$?" -eq 1
  fi
  printf '%s\n' 'RED: ready line absent'
  printf '%s\n' 'status: ready' > catalog.txt
  grep -Fxq 'status: ready' catalog.txt
  git diff --check
  git add catalog.txt
  git diff --cached
  git commit -m 'feat: expose catalog readiness'
  git switch main
  test "$(cat catalog.txt)" = 'status: draft'
  git merge --ff-only feat/ready-catalog
  git tag -a v1.1.0 -m 'Release 1.1.0'
  test "$(git rev-parse 'v1.1.0^{commit}')" = "$(git rev-parse HEAD)"
  test -z "$(git status --porcelain)"
  test -z "$(git remote)"
  grep -Fxq 'status: ready' catalog.txt
  git log --oneline --decorate -2
  printf '%s\n' 'PASS: integrated tagged clean revision'
)
```

## Riscos e recuperação

Sem remote, push, release real ou credenciais. Não substitua por caminho real, configure remote ou copie comandos em repo de produção. Não é sandbox endurecido contra ambiente shell malicioso. Se comando falhar, inspecione repo temporário com status e log; não faça reset ou force merge. Antes de integração, diff somente leitura é prática de review, não aprovação independente. Refatoração opcional: extraia check em função em shell descartável separado e verifique códigos de saída equivalentes; bloco demonstra red/green, não ciclo completo de refatoração.

## Exercício e autocorreção

Passe se draft inicial não satisfaz check, ready satisfaz, main fica igual até integração, tag resolve para HEAD, status limpo e sem remote. Explique por que exercício local aprovado não comprova CI hospedada, review formal ou implantação. Compare versão hipotética com contrato do capítulo 07.

## Referência rápida

`git status` / `git diff --cached` / `git merge --ff-only` / `git tag -a`

## Fontes

- <https://git-scm.com/docs/gitworkflows>
- <https://git-scm.com/docs/git-merge>
- <https://git-scm.com/docs/git-tag>
- <https://www.conventionalcommits.org/en/v1.0.0/>
- <https://semver.org/spec/v2.0.0.html>
