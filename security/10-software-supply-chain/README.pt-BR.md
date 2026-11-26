# Segurança da cadeia de suprimentos de software

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../09-commit-and-tag-signing/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../11-credential-exposure-and-incident-response/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 45 min

**Pré-requisitos:** [Fluxos profissionais](../../professional-workflows/README.pt-BR.md) · [Assinatura de commits e tags](../09-commit-and-tag-signing/README.pt-BR.md)

**Objetivo:** Identificar controles de supply chain e riscos residuais.

## O que é e por quê

Cadeia inclui fonte, dependências, ferramentas build, actions CI, imagens, runners, registries e artifacts distribuídos. Lockfiles registram versões resolvidas; não provam segurança. SBOM inventaria componentes; proveniência descreve onde/como artifact foi construído; atestado é declaração verificável sobre objeto. Verifique fontes confiáveis, revise dependências, fixe actions GitHub em SHAs completos verificados e imagens em digests verificados quando possível, atualize periodicamente por mudanças revisadas. Pinagem não remove vulnerabilidades nem garante transitivas seguras. Use menor privilégio e CI não confiável isolado; não implante artifacts de jobs não confiáveis sem fronteira verificada.

[Automação de qualidade](../../docs/quality-automation.pt-BR.md)

## Prática

Desenhe fonte -> build revisado -> artifact -> promoção verificada. Em PR fictício trocando action de SHA revisado por tag móvel, identifique referência mutável e peça revisão verificada independentemente. Adicione inventário, checksum/proveniência esperados e responsável por atualização ao checklist. Leia política de quality workflow do guia sem alterar.

## Riscos e recuperação

Não execute dependências não revisadas, CI privilegiado de terceiros ou artifacts arbitrários. Se dependência comprometida, pare jobs/releases afetados, siga incidente, verifique substituição e reconstrua com entradas confiáveis. Nunca afirme scanner provar ausência de vulnerabilidades.

## Exercício e autocorreção

Revisões fixadas verificadas, atualizações revisadas, build isolado, inventário e proveniência reduzem riscos diferentes. Nenhum controle garante confiança.

## Referência rápida

lockfile / SBOM / provenance / attestation

## Referências

- <https://docs.github.com/en/actions/reference/security/secure-use>
- <https://slsa.dev/spec/v1.0/>
- <https://www.cisa.gov/sbom>
