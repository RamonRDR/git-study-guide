# Laboratório integrado de segurança

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../12-governance-audit-and-traceability/README.pt-BR.md) · [Índice](../README.pt-BR.md) · —
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 50 min

**Pré-requisitos:** [Fluxos profissionais](../../professional-workflows/README.pt-BR.md) · [Governança, auditoria e rastreabilidade](../12-governance-audit-and-traceability/README.pt-BR.md)

**Objetivo:** Verificar staging local seguro e ensaiar resposta.

## O que é e por quê

Exercício offline usa apenas configurações inofensivas, não segredos. Ilustra ignore e staging explícito em repo temporário novo. Simulação complementar ensaia controle de acesso e incidentes; não cria credenciais, altera política hospedada, assina commit, implanta ou testa incidente real. Use Git 2.28+ e Bash (Linux/macOS ou Git Bash no Windows), shell normal limpo. Bloco isola configuração system/global normal e deixa sandbox impresso para inspeção posterior; não é fronteira endurecida contra ambiente malicioso.

## Prática

Antes de executar, preveja `local-settings.txt` ignorado e `.gitignore` e `settings.example.txt` staged. Execute bloco inteiro abaixo apenas em shell descartável. Esperado: check ignore imprime nome local, nomes staged listam exatamente dois arquivos públicos e PASS. Depois simule exposição hipotética sem valor de credencial: escolha revogação, notificação, avaliação e correção; redija matriz de acesso e gate do catálogo fictício. Nenhum remote necessário.

```bash
(
  set -eu
  sandbox=$(mktemp -d)
  printf 'Sandbox: %s\n' "$sandbox"
  unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE GIT_COMMON_DIR GIT_CONFIG_PARAMETERS
  export GIT_CONFIG_NOSYSTEM=1 GIT_CONFIG_GLOBAL="$sandbox/global-config" GIT_CONFIG_COUNT=0
  git init -b main "$sandbox/catalog"
  cd "$sandbox/catalog"
  printf '%s\n' 'local-settings.txt' > .gitignore
  printf '%s\n' 'mode=local' > local-settings.txt
  printf '%s\n' 'mode=example' > settings.example.txt
  git check-ignore -- local-settings.txt
  git add -- .gitignore settings.example.txt
  test -z "$(git ls-files -- local-settings.txt)"
  test "$(git ls-files -- settings.example.txt)" = 'settings.example.txt'
  git diff --cached --check
  git diff --cached --name-only
  test -z "$(git remote)"
  printf '%s\n' 'PASS: local file ignored, template staged, no remote'
)
```

## Riscos e recuperação

Não substitua por projeto real ou arquivo de credenciais. Se comando falhar, pare e inspecione sandbox impresso com status/diff somente leitura. Remova pelo gerenciador de arquivos só após confirmar caminho exato. Checks de nomes aprovados não provam ausência de segredo no conteúdo; projetos reais precisam review de conteúdo e scanning adequado.

## Exercício e autocorreção

Passe se arquivo local não rastreado, template staged, sem remote e resposta simulada prioriza revogação antes de limpar histórico. Explique o não testado: credenciais reais, imposição da plataforma, assinatura, CI hospedado e implantação.

## Referência rápida

`git check-ignore` / `git add --` / `git diff --cached`

## Referências

- <https://git-scm.com/docs/gitignore>
- <https://git-scm.com/docs/git-check-ignore>
- <https://git-scm.com/docs/git-ls-files>
- <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository>
