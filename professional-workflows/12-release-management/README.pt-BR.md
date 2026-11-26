# Gestão de releases

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../11-ai-assisted-development/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../13-integrated-professional-workflow-lab/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 40 min

**Pré-requisitos:** [CI/CD](../../ci-cd/README.pt-BR.md) · [Trabalho profissional assistido por IA](../11-ai-assisted-development/README.pt-BR.md)

**Objetivo:** Preparar release com versão, revisão, evidência e decisão de publicação separada.

## O que é e por quê

Release identifica revisão testada e comunica o que consumidores podem usar. Tag Git é ref, frequentemente anotada com mensagem; release hospedada pode anexar notas e assets à tag. Implantação é ato separado de promover artifact ao ambiente. Parta de revisão integrada aprovada, decida versão conforme contrato público, registre mudanças/migração e limites, verifique checks e proveniência, crie tag anotada no commit escolhido e obtenha autorização de release antes de publicar. Para inspeção local use `git show v1.1.0` e `git rev-parse 'v1.1.0^{commit}'` após capítulo 13. Assinatura e controles de releases imutáveis podem ajudar quando configurados; tag anotada não é automaticamente assinada ou imutável.

```text
tested commit -> annotated tag -> authorized publication -> deployment decision
```

## Prática

Suponha catálogo 1.0.0 com formato público documentado e prontidão como campo novo retrocompatível neste cenário hipotético. Redija notas 1.1.0: feature, comportamento, verificação, migração (nenhuma exigida para consumidores compatíveis), limites (só lab local, sem execução hospedada) e identificador de artifact/revisão. Desenhe gate entre tag, publicação e implantação. Não publique nada no exercício.

## Riscos e recuperação

Não remova/recrie tag publicada nem publique head não revisado. Se release ruim escapar, comunique, pare promoção e siga política rollback/forward-fix; migração de dados pode impedir rollback fácil. Permissões de release e implantação são distintas de merge. Nenhum artifact externo ou implantação real é exigido.

## Exercício e autocorreção

1.1.0 se justifica só pelo contrato compatível declarado. Tag aponta revisão testada; notas informam checks e limites reais; produção permanece igual.

## Referência rápida

tag / release notes / artifact / deployment

## Fontes

- <https://semver.org/spec/v2.0.0.html>
- <https://git-scm.com/docs/git-tag>
- <https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository>
