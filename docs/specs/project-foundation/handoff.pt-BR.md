# Handoff Learning Hub

[English](handoff.md) · [Português](handoff.pt-BR.md) · [Español](handoff.es.md)

Este handoff distingue a revisão imutável de conteúdo da revisão de apresentação e da tag publicada. A base abaixo foi integrada com autorização explícita do mantenedor no PR #21 e passou CI main e manual. O handoff foi revisado e integrado no PR #22; v1.0.0 está publicada. Este documento não ativa lock do site.

## Conteúdo e proveniência

- [Content revision 03c30438a5490d6c8f9b22dbf457a644658e042f](https://github.com/RamonRDR/git-study-guide/commit/03c30438a5490d6c8f9b22dbf457a644658e042f)
- [Main CI](https://github.com/RamonRDR/git-study-guide/actions/runs/46061260750) · [Manual CI](https://github.com/RamonRDR/git-study-guide/actions/runs/46062482507)
- [Manifest](../../../curriculum/manifest.json) · [Contract](integration-contract.pt-BR.md) · [Reference consumer](../../../scripts/learning_hub_consumer.py)
- [ADR 0006](../../adr/0006-browser-playground.md)

```json
{
  "guide_id": "git-study-guide",
  "revision": "03c30438a5490d6c8f9b22dbf457a644658e042f",
  "manifest_version": "1.0.0",
  "assessment_version": 1,
  "command_catalog_version": 1
}
```

O consumidor de referência recebe lock externo e repositório Git SHA-1 confiável com objetos completos. Use versões exatas suportadas, jamais execute código do snapshot e valide antes de adotar; preserve o pin aprovado anterior em caso de falha. Adaptador Git distinto do adaptador Python. Leia contrato de integração e ADR de playground. Projetos e desafios nativos são local_only, demais capítulos unverified; nenhum runtime navegador ou deploy do site alegado.

## Validação e release

A base contém 18 módulos, 141 entradas, 423 caminhos localizados de capítulos, 54 de índices, 120 operações e 75 registros de avaliação. Comparação independente cobre 503 caminhos canônicos (manifesto, registro, índices, capítulos, recursos, bancos, catálogo e schemas); todos coincidem com a base por ID de blob Git antes da revisão final de apresentação. Na revisão da base, a mesma suíte de 152 testes e nove validadores passaram por SO no CI main. As evidências finais de apresentação e release constam abaixo. Não houve mudanças recíprocas no Python ou perfil antes da publicação Git.

- [PR #22](https://github.com/RamonRDR/git-study-guide/pull/22)
- [Identidade visual V1](../../assets/learning-hub/README.pt-BR.md)
- [Audit](audit.pt-BR.md) · [Tasks](tasks.pt-BR.md)

## Encerramento da Sprint 19B: release oficial v1.0.0

O mantenedor aprovou a Identidade Visual V1, os três READMEs renderizados em desktop e mobile, links externos e social preview; a confirmação visual foi informada pelo mantenedor. PRs #22 e #23 passaram CI no HEAD exato, Codex Review e Final Pre-Merge Audit, foram explicitamente autorizados e integrados por squash. Ambos os CIs pós-merge na main aprovaram 156 testes e nove validadores por SO; nenhum marcador de erro/aviso observado. Os 503 caminhos canônicos permaneceram intactos. A v1.0.0 estável e latest foi publicada pelo mantenedor em 28/11/2026 às 17:41:35 UTC; a tag aponta diretamente para `706105ee5ef51befd2282a143e7deafd256c61a8`. Pin de conteúdo `03c30438a5490d6c8f9b22dbf457a644658e042f`; revisão de apresentação `c26c41fee624a74f7ba7a70ac531063061a6559e`. AC-19 e T19-01 atendidos; esta documentação pós-release reconcilia os registros históricos em andamento e não modifica a tag publicada. Limitações: revisão semântica amostral, sem execução exaustiva dos labs de estudantes ou CI macOS, sem runtime navegador ou deploy do site verificados, sem cancelamento de execuções substituídas observado. Links recíprocos com Python e perfil são PRs posteriores separados.

- [Release v1.0.0](https://github.com/RamonRDR/git-study-guide/releases/tag/v1.0.0)
- [Final main CI](https://github.com/RamonRDR/git-study-guide/actions/runs/46170822488)
- [PR #22](https://github.com/RamonRDR/git-study-guide/pull/22) · [PR #23](https://github.com/RamonRDR/git-study-guide/pull/23)
