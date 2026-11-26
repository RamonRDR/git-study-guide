# Assinatura de commits e tags

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../08-codeowners-and-responsibilities/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../10-software-supply-chain/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 40 min

**Pré-requisitos:** [Fluxos profissionais](../../professional-workflows/README.pt-BR.md) · [CODEOWNERS e responsabilidades](../08-codeowners-and-responsibilities/README.pt-BR.md)

**Objetivo:** Interpretar assinaturas e limites.

## O que é e por quê

Assinatura criptográfica vincula objeto Git a chave de assinatura e pode ser verificada com configuração de confiança adequada. Git suporta formatos OpenPGP, SSH e X.509 conforme versão e ferramentas. Commit assinado e tag anotada assinada são objetos distintos; tag anotada sem assinatura não é assinada. `git verify-commit` e `git verify-tag` verificam assinaturas com chave/confiança adequadas. Badge Verified segue política do host; não prova código seguro, aprovado ou implantado. Novo commit de rebase/squash tem identidade diferente e não herda assinatura original. Autenticação e assinatura SSH são usos separados.

## Prática

Offline: compare commit A sem assinatura, B com assinatura válida de chave desconhecida e C assinado por chave confiável mas testes falhos. Identifique o que cada evidência prova. Esboce verificação de tag anotada assinada e commit alvo. Não precisa gerar ou enviar chaves.

## Riscos e recuperação

Nunca exponha chaves privadas de assinatura, ignore chaves não confiáveis ou trate badge verde como review. Se chave comprometida, revogue/rotacione, avalie assinaturas afetadas e coordene política de confiança; não reescreva histórico público unilateralmente.

## Exercício e autocorreção

A não tem evidência de assinatura; B exige verificação de identidade confiável; C ainda falha gates. Assinatura e review independentes.

## Referência rápida

`git verify-commit` / `git verify-tag` / trust

## Referências

- <https://git-scm.com/docs/git-verify-commit>
- <https://git-scm.com/docs/git-verify-tag>
- <https://git-scm.com/docs/git-config>
- <https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification>
