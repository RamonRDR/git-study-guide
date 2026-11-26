# Tags Git e releases do GitLab

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../06-pipelines-and-runners/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../08-gitlab-cli-and-platform-comparison/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 25 min

**Pré-requisitos:** [GitHub](../../github/README.pt-BR.md) · [Remotos](../../remote-repositories/README.pt-BR.md)

**Objetivo:** Distinguir refs de versão de metadados de publicação e validar revisão pretendida.

## O que é e por quê

Tag Git nomeia objeto, geralmente commit; tag leve referencia objeto diretamente, tag anotada acrescenta objeto tag com metadados e mensagem. Release GitLab associa tag a notas e assets ou links de assets. Tags ficam no Git; notas e anexos são metadados hospedados, não incluídos automaticamente no clone. Release profissional identifica commit revisado, resume mudanças e descreve limitações. Tag protegida pode restringir operações conforme configuração; não suponha que proteção de branch protege tags. Evite mover tag publicada: consumidores podem já tê-la obtido. Prefira nova versão corrigida conforme política de release.

## Prática

Repita exercício local seguro de tags de [tags e releases GitHub](../../github/07-tags-and-releases/README.pt-BR.md) no repositório descartável, sem publicar. Compare `git show v1.0.0` (se essa tag existir) com nota fictícia descrevendo instalação do catálogo e limitação conhecida. Use `git tag --list` para inspecionar tags antes de escolher uma. Opcional: inspecione release pública existente do GitLab sem baixar ou executar assets. Compare tag e notas; não crie release hospedada.

## Erros comuns e segurança

Nunca publique tag apontando para commit não revisado nem inclua segredos em notas/assets. Se release referencia commit errado, interrompa distribuição, avise mantenedores e siga política de correção; não reescreva tags públicas silenciosamente.

## Exercício e autocorreção

Passe se tag identifica revisão, notas comunicam mudanças e asset não é confiável apenas porque existe release. Exercício offline não exige conta.

## Fontes oficiais

- <https://docs.gitlab.com/user/project/releases/>
- <https://git-scm.com/docs/git-tag>
