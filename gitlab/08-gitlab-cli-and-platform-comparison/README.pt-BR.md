# CLI GitLab opcional e comparação de plataformas

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../07-tags-and-releases/README.pt-BR.md) · [Índice](../README.pt-BR.md) · —
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 30 min

**Pré-requisitos:** [GitHub](../../github/README.pt-BR.md) · [Remotos](../../remote-repositories/README.pt-BR.md)

**Objetivo:** Escolher Git nativo ou CLI hospedada e mapear conceitos de colaboração sem presumir paridade.

## O que é e por quê

`git` manipula objetos e refs Git; `glab` é CLI separada do GitLab para recursos da plataforma via APIs de rede; `gh` é CLI análoga do GitHub. CLI GitLab pode trabalhar com GitLab.com e hosts Self-Managed configurados; confirme host e conta antes de consultas. Com CLI já instalada, `glab --version` e `glab --help` inspecionam ferramenta local; `glab auth status` verifica estado de autenticação; `glab mr list`, `glab issue list` e `glab release list` consultam projeto selecionado. Não criam nem integram recursos. Para acesso autenticado siga documentação oficial de instalação/autenticação, use armazenamento seguro de credenciais quando suportado e evite expor credenciais ou dados da conta. Disponibilidade, permissões API e flags podem variar por versão.

## Prática

Offline mapeie pares: repositório GitHub ↔ projeto GitLab (contém repositório); organização/equipe ↔ grupo/subgrupo (modelos de permissão diferentes); pull request ↔ merge request; workflow GitHub Actions ↔ pipeline GitLab CI/CD; branch protection/ruleset ↔ branch protegida/branch rule; `gh` ↔ `glab`. Ambos usam Git nativo para commits, branches, tags e clones. Escolha Git para inspecionar histórico, GitLab para listar MRs e plataforma adequada para política de equipe. Opcional: use CLI autorizada existente em sandbox próprio, verifique `git remote -v` localmente sem compartilhar saída e inspecione `glab --help`; rode comandos de listagem somente se host/projeto corretos e autenticação confirmados. Nenhum login, instalação ou operação hospedada exigidos.

## Erros comuns e segurança

Não traduza comandos CLI cegamente nem prometa paridade. Planos gratuitos permitem colaboração básica, mas aprovação obrigatória, cotas e governança avançada diferem por modalidade, plano, versão e configuração. Se consulta falhar, confira ajuda, host e acesso antes de repetir; não amplie credenciais nem use comando de escrita como contorno.

## Exercício e autocorreção

Qual ferramenta lista MRs hospedadas: `git log` ou `glab mr list`? `glab mr list`. Passe se explicar os seis mapeamentos como analogias, não equivalências exatas, e nenhuma atividade paga ou autenticada for necessária.

## Fontes oficiais

- <https://docs.gitlab.com/cli/>
- <https://docs.gitlab.com/cli/authentication/>
- <https://docs.gitlab.com/cli/mr/list/>
- <https://docs.gitlab.com/cli/issue/list/>
- <https://docs.gitlab.com/cli/release/list/>
- <https://docs.github.com/en/github-cli/github-cli/about-github-cli>
