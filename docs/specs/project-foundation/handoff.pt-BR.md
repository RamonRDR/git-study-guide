# Handoff Learning Hub

[English](handoff.md) · [Português](handoff.pt-BR.md) · [Español](handoff.es.md)

Este handoff distingue a revisão imutável de conteúdo da revisão de apresentação e da futura tag da release. A base abaixo foi integrada com autorização explícita do mantenedor no PR #21 e passou CI main e manual. Este documento permanece candidato à release até revisão e integração do PR #22; não ativa lock do site nem publica release.

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

A base contém 18 módulos, 141 entradas, 423 caminhos localizados de capítulos, 54 de índices, 120 operações e 75 registros de avaliação. Comparação independente cobre 503 caminhos canônicos (manifesto, registro, índices, capítulos, recursos, bancos, catálogo e schemas); todos coincidem com a base por ID de blob Git antes da revisão final de apresentação. Mesma suíte de 152 testes e nove validadores passaram por SO no CI main. CI final de apresentação e Codex Review devem passar; renderização visual, autorização explícita de squash, CI pós-merge e autorização separada de release continuam obrigatórios. Sem mudanças recíprocas no Python ou perfil antes da publicação Git.

- [PR #22](https://github.com/RamonRDR/git-study-guide/pull/22)
- [Identidade visual V1](../../assets/learning-hub/README.pt-BR.md)
- [Audit](audit.pt-BR.md) · [Tasks](tasks.pt-BR.md)
