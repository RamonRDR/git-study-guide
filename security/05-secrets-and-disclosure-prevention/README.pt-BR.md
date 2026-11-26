# Secrets e prevenção de vazamentos

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../04-credential-managers/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../06-permissions-and-least-privilege/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 40 min

**Pré-requisitos:** [Fluxos profissionais](../../professional-workflows/README.pt-BR.md) · [Credential managers e escopo de configuração](../04-credential-managers/README.pt-BR.md)

**Objetivo:** Prevenir exposição acidental e inspecionar tracking.

## O que é e por quê

Secret é material confidencial de autenticação ou outro valor sensível. Guarde segredos reais em gerenciador aprovado fora do versionamento. Publique só templates sanitizados com exemplos não secretos. `.gitignore` corresponde a caminhos não rastreados; não remove arquivos já no índice nem apaga histórico. `git check-ignore -- path` verifica regras para caminho não rastreado; `git ls-files -- path` inspeciona entradas rastreadas. Check de nomes staged ajuda prevenir adições acidentais mas não inspeciona conteúdo. Secret scanning e push protection são defesas heurísticas dependentes do provedor, não prova de ausência. Redija logs/artifacts; nunca publique segredos reais nem em repos privados.

## Prática

Use capítulo 13 com valores inofensivos `mode=local` e `mode=example`. Preveja caminhos ignorados e staged. Para arquivo local hipotético já rastreado, explique por que adicioná-lo a ignore não basta; correção autorizada precisa removê-lo do tracking e avaliar exposição anterior.

## Riscos e recuperação

Nunca crie token falso com aparência real, cole segredo real em scanner ou use force-add para contornar ignore. Em exposição, priorize revogação e incidente; excluir arquivo apenas não basta.

## Exercício e autocorreção

Ignore e tracking são distintos; template é seguro só por conteúdo não sensível deliberado. Scanning é defesa em profundidade.

## Referência rápida

`git check-ignore` / `git ls-files` / `.gitignore`

## Referências

- <https://git-scm.com/docs/gitignore>
- <https://git-scm.com/docs/git-check-ignore>
- <https://git-scm.com/docs/git-ls-files>
- <https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning>
