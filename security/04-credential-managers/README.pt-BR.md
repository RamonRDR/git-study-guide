# Credential managers e escopo de configuração

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../03-https-and-access-tokens/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../05-secrets-and-disclosure-prevention/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 35 min

**Pré-requisitos:** [Fluxos profissionais](../../professional-workflows/README.pt-BR.md) · [HTTPS e tokens de acesso](../03-https-and-access-tokens/README.pt-BR.md)

**Objetivo:** Distinguir armazenamento de helper e revogação.

## O que é e por quê

Helpers Git obtêm e armazenam credenciais para HTTPS; Git Credential Manager pode usar autenticação do provedor e armazenamento do SO adequado conforme configuração. Helper `cache` guarda temporariamente em memória; `store` salva texto claro em disco, inadequado para credenciais sensíveis duradouras. Configuração system, global e local têm escopos diferentes; múltiplos helpers podem estar ativos. `git config --show-origin --get-all credential.helper` é diagnóstico somente leitura, mas pode revelar comando customizado ou caminhos sensíveis. Inspecione localmente, nunca compartilhe saída bruta. Agentes SSH e helpers HTTPS são mecanismos distintos.

## Prática

Offline: compare cache memória, texto claro e gerenciador aprovado do SO. Dada credencial salva obsoleta fictícia, descreva remoção segura e nova autenticação pela interface documentada do gerenciador. Distinga esquecer credencial local de revogar remotamente.

## Riscos e recuperação

Não execute comandos de recuperação para imprimir senhas/tokens. Não altere helpers globais neste exercício. Use fluxo de remoção/logout suportado para conta e host corretos; revogue credenciais comprometidas no emissor também.

## Exercício e autocorreção

Prefira armazenamento protegido aprovado; remoção local não revoga credencial do emissor. Sem credenciais reais.

## Referência rápida

helper / cache / store / credential manager

## Referências

- <https://git-scm.com/docs/gitcredentials>
- <https://git-scm.com/docs/git-credential-store>
- <https://git-scm.com/docs/git-credential-cache>
- <https://github.com/git-ecosystem/git-credential-manager>

---

<!-- navigation-footer -->
[Anterior](../03-https-and-access-tokens/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../05-secrets-and-disclosure-prevention/README.pt-BR.md)
<!-- /navigation-footer -->
