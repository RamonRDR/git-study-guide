# 14 Plataformas e automação

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../13-security-and-maintenance/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo módulo](../../practical-projects/README.pt-BR.md)
<!-- /navigation -->

Gerado a partir do JSON canônico. Edite os registros, não esta página.

As entradas descrevem comandos e operações, não uma sequência a executar. Pratique em repositórios descartáveis. Operações hospedadas são opcionais.

**Total de entradas distintas: 8**

- [`gh pr create`](#gh-pr-create)
- [`gh pr view`](#gh-pr-view)
- [`gh pr checks`](#gh-pr-checks)
- [`gh run view`](#gh-run-view)
- [`gh release create`](#gh-release-create)
- [`glab mr create`](#glab-mr-create)
- [`glab mr view`](#glab-mr-view)
- [`glab ci status`](#glab-ci-status)

## gh-pr-create

**`gh pr create`**

**Tipo:** Ferramenta externa

**Nível:** Intermediário

**Pesquisar por intenção:** Revisar alterações, Automatizar fluxo

**Risco:** Alteração remota. Cria estado na plataforma e pode notificar pessoas ou acionar automação. Não execute exemplos fictícios contra repositórios reais; exija autorização e verifique destino.

**Finalidade:** Criar pull request GitHub para integração proposta de branch.

**Pré-requisitos:** Exemplos são modelos fictícios, não exercícios em serviço real. Substitua apenas por repositório sandbox explicitamente autorizado, conta, referências e IDs verificados. Confira versão e autenticação da CLI antes.

**Opções:** --base e --head identificam referências; --draft abre draft; --head explícito evita fork ou push implícito. --dry-run ainda pode fazer push.

**Quando utilizar:** Quando branch de feature autorizada publicada está pronta para revisão ou feedback preliminar.

**Quando evitar:** Evite repositório errado, conteúdo sensível não revisado ou contornar controles de revisão.

**Sintaxe**

`gh pr create -R example-org/example-repo --base main --head feat/notes --title "Review notes" --body "Fictional review" --draft`

**Exemplo básico**

`gh pr create -R example-org/example-repo --base main --head feat/notes --title "Review notes" --body "Fictional review" --draft`

Ilustre abertura de draft de branch autorizada já publicada; substitua só pelo repositório sandbox.

**Exemplo profissional**

`gh pr create -R example-org/example-repo --base main --head feat/docs --title "Review documentation" --body "Describe changes and test evidence"`

Ilustre solicitação de revisão de mudanças registradas revisadas com head e base explícitos.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Condicional
- Outros estados: Condicional

**Resultado esperado:** Retorna URL do PR criado em sucesso; criação isolada não integra branch.

**Impactos e efeitos colaterais:** Cria metadados remotos de PR e pode acionar CI ou notificações. Head explícito mostrado exige branch já publicada; formas implícitas podem fazer push ou fork.

**Erros comuns:** Confundir criação de PR com aprovação de merge ou esperar dry run garantir ausência de gravações na rede.

**Alternativas:** Use interface web da plataforma para inspecionar e criar solicitação autorizada manualmente.

**Recuperação:** Inspecione URL criada e referências exatas; se incorreto, coordene correção ou fechamento autorizado do PR errado. Fechar não apaga histórico.

**Versão e dependências:** Exige GitHub CLI (gh) compatível atual, autenticação autorizada, rede e permissões relevantes. Confira gh help para flags instaladas.

**Capítulos relacionados**

- [github/04-pull-requests-and-review](../../github/04-pull-requests-and-review/README.pt-BR.md)
- [github/08-github-cli](../../github/08-github-cli/README.pt-BR.md)

**Documentação oficial**

- <https://cli.github.com/manual/gh_pr_create>

## gh-pr-view

**`gh pr view`**

**Tipo:** Ferramenta externa

**Nível:** Intermediário

**Pesquisar por intenção:** Revisar alterações, Inspecionar estado do repositório

**Risco:** Somente leitura. Inspeção não é autorização de merge. Proteja metadados privados e logs; não exponha credenciais.

**Finalidade:** Inspecionar pull request GitHub e metadados de revisão ou merge.

**Pré-requisitos:** Exemplos são modelos fictícios, não exercícios em serviço real. Substitua apenas por repositório sandbox explicitamente autorizado, conta, referências e IDs verificados. Confira versão e autenticação da CLI antes.

**Opções:** --json seleciona campos; --comments exibe comentários e revisões; --web abre página.

**Quando utilizar:** Ao conferir PR exato e head em revisão.

**Quando evitar:** Não deduza autorização de merge apenas de campo de mergeabilidade.

**Sintaxe**

`gh pr view 42 -R example-org/example-repo`

**Exemplo básico**

`gh pr view 42 -R example-org/example-repo`

Inspecione PR fictício número 42 em modelo de sandbox autorizado.

**Exemplo profissional**

`gh pr view 42 -R example-org/example-repo --json headRefOid,reviewDecision,mergeStateStatus`

Inspecione head exato e estado de revisão, depois confira checks obrigatórios independentemente.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Exibe snapshot dos metadados do PR; cálculo e estado de revisão podem mudar.

**Impactos e efeitos colaterais:** Lê metadados da plataforma pela rede; não altera intencionalmente referências Git, index, checkout ou recursos da plataforma na forma mostrada.

**Erros comuns:** Ler aprovação de head anterior como aprovação de mudanças novas.

**Alternativas:** Use interface web e gh pr checks para inspecionar checks e discussão.

**Recuperação:** Inspeção não exige desfazer. Verifique repositório, ID, permissões e associação ao commit exato; atualize status se incompleto ou obsoleto.

**Versão e dependências:** Exige GitHub CLI (gh) compatível atual, autenticação autorizada, rede e permissões relevantes. Confira gh help para flags instaladas.

**Capítulos relacionados**

- [github/04-pull-requests-and-review](../../github/04-pull-requests-and-review/README.pt-BR.md)
- [github/08-github-cli](../../github/08-github-cli/README.pt-BR.md)

**Documentação oficial**

- <https://cli.github.com/manual/gh_pr_view>

## gh-pr-checks

**`gh pr checks`**

**Tipo:** Ferramenta externa

**Nível:** Intermediário

**Pesquisar por intenção:** Inspecionar CI, Revisar alterações

**Risco:** Somente leitura. Inspeção não é autorização de merge. Proteja metadados privados e logs; não exponha credenciais.

**Finalidade:** Inspecionar resultados de checks CI associados ao pull request GitHub.

**Pré-requisitos:** Exemplos são modelos fictícios, não exercícios em serviço real. Substitua apenas por repositório sandbox explicitamente autorizado, conta, referências e IDs verificados. Confira versão e autenticação da CLI antes.

**Opções:** --required restringe a checks obrigatórios; --watch aguarda atualizações; checks pendentes têm código de saída distinto na CLI atual.

**Quando utilizar:** Ao determinar se checks obrigatórios terminaram para mudança revisada.

**Quando evitar:** Evite declarar sucesso com resultados incompletos, ausentes ou obsoletos.

**Sintaxe**

`gh pr checks 42 -R example-org/example-repo`

**Exemplo básico**

`gh pr checks 42 -R example-org/example-repo`

Inspecione checks de PR fictício de sandbox autorizado.

**Exemplo profissional**

`gh pr checks 42 -R example-org/example-repo --required`

Inspecione checks obrigatórios e confirme correspondência ao head revisado mais recente.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Exibe estados relatados dos checks; código não zero pode indicar pendência ou falha, conforme código.

**Impactos e efeitos colaterais:** Lê metadados da plataforma pela rede; não altera intencionalmente referências Git, index, checkout ou recursos da plataforma na forma mostrada.

**Erros comuns:** Tratar ausência de checks relatados ou checks antigos aprovados como sinal verde atual.

**Alternativas:** Inspecione head do PR e execuções individuais de workflow, incluindo checks obrigatórios e logs.

**Recuperação:** Inspeção não exige desfazer. Verifique repositório, ID, permissões e associação ao commit exato; atualize status se incompleto ou obsoleto.

**Versão e dependências:** Exige GitHub CLI (gh) compatível atual, autenticação autorizada, rede e permissões relevantes. Confira gh help para flags instaladas.

**Capítulos relacionados**

- [github/04-pull-requests-and-review](../../github/04-pull-requests-and-review/README.pt-BR.md)
- [ci-cd/09-quality-gates-and-troubleshooting](../../ci-cd/09-quality-gates-and-troubleshooting/README.pt-BR.md)

**Documentação oficial**

- <https://cli.github.com/manual/gh_pr_checks>

## gh-run-view

**`gh run view`**

**Tipo:** Ferramenta externa

**Nível:** Intermediário

**Pesquisar por intenção:** Inspecionar CI

**Risco:** Somente leitura. Inspeção não é autorização de merge. Proteja metadados privados e logs; não exponha credenciais.

**Finalidade:** Inspecionar execução específica de workflow GitHub Actions e informações disponíveis de jobs.

**Pré-requisitos:** Exemplos são modelos fictícios, não exercícios em serviço real. Substitua apenas por repositório sandbox explicitamente autorizado, conta, referências e IDs verificados. Confira versão e autenticação da CLI antes.

**Opções:** --log-failed solicita logs de etapas com falha; --exit-status retorna não zero para execução falha; ID de execução não é número de PR.

**Quando utilizar:** Ao diagnosticar tentativa identificada de workflow para commit específico.

**Quando evitar:** Não presuma execução alheia aprovada prova aprovação de checks obrigatórios.

**Sintaxe**

`gh run view 123456 -R example-org/example-repo`

**Exemplo básico**

`gh run view 123456 -R example-org/example-repo`

Inspecione ID fictício de execução de workflow em modelo sandbox.

**Exemplo profissional**

`gh run view 123456 -R example-org/example-repo --log-failed`

Inspecione logs de etapas com falha sem publicar saída sensível.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Retorna detalhes ou logs disponíveis; execuções incompletas e logs expirados podem não fornecer evidência final.

**Impactos e efeitos colaterais:** Lê metadados da plataforma pela rede; não altera intencionalmente referências Git, index, checkout ou recursos da plataforma na forma mostrada.

**Erros comuns:** Confundir ID de execução, ID de job e número de PR ou ignorar tentativa e SHA do head.

**Alternativas:** Use gh pr checks para checks do PR e interface Actions para contexto completo da tentativa.

**Recuperação:** Inspeção não exige desfazer. Verifique repositório, ID, permissões e associação ao commit exato; atualize status se incompleto ou obsoleto.

**Versão e dependências:** Exige GitHub CLI (gh) compatível atual, autenticação autorizada, rede e permissões relevantes. Confira gh help para flags instaladas.

**Capítulos relacionados**

- [ci-cd/03-github-actions](../../ci-cd/03-github-actions/README.pt-BR.md)
- [ci-cd/09-quality-gates-and-troubleshooting](../../ci-cd/09-quality-gates-and-troubleshooting/README.pt-BR.md)

**Documentação oficial**

- <https://cli.github.com/manual/gh_run_view>

## gh-release-create

**`gh release create`**

**Tipo:** Ferramenta externa

**Nível:** Avançado

**Pesquisar por intenção:** Gerenciar releases, Gerenciar tags

**Risco:** Alteração remota. Cria estado na plataforma e pode notificar pessoas ou acionar automação. Não execute exemplos fictícios contra repositórios reais; exija autorização e verifique destino.

**Finalidade:** Criar metadados de release associados a tag GitHub, opcionalmente como draft.

**Pré-requisitos:** Exemplos são modelos fictícios, não exercícios em serviço real. Substitua apenas por repositório sandbox explicitamente autorizado, conta, referências e IDs verificados. Confira versão e autenticação da CLI antes.

**Opções:** --verify-tag exige tag remota existente; sem ele a CLI pode criar tag ausente. --draft adia publicação; --notes-file fornece notas.

**Quando utilizar:** Ao preparar release autorizada revisada após verificar tag de versão.

**Quando evitar:** Evite destinos não verificados, aprovação ausente, artefatos sensíveis ou criação implícita de tag.

**Sintaxe**

`gh release create v1.0.0 -R example-org/example-repo --verify-tag --draft --title "Practice release" --notes "Fictional release notes"`

**Exemplo básico**

`gh release create v1.0.0 -R example-org/example-repo --verify-tag --draft --title "Practice release" --notes "Fictional release notes"`

Ilustre draft usando tag remota autorizada existente em sandbox.

**Exemplo profissional**

`gh release create v1.1.0 -R example-org/example-repo --verify-tag --draft --notes-file release-notes.md`

Prepare draft só após revisar tag existente, arquivo de notas e política de release.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Condicional
- Outros estados: Condicional

**Resultado esperado:** Cria draft de release para tag remota existente nas formas mostradas; publicação exige ação separada.

**Impactos e efeitos colaterais:** Grava metadados remotos de draft; forma --verify-tag mostrada exige tag existente e não a cria. Outras formas podem criar tags ou publicar artefatos.

**Erros comuns:** Confundir verificação de existência de tag com verificação de assinatura ou publicar antes de aprovações.

**Alternativas:** Use interface Releases para preparar draft e revisar manualmente; verifique assinaturas e artefatos separadamente.

**Recuperação:** Inspecione draft criado e tag associada. Coordene edições autorizadas ou remoção do draft se incorreto; não reescreva tag publicada.

**Versão e dependências:** Exige GitHub CLI (gh) compatível atual, autenticação autorizada, rede e permissões relevantes. Confira gh help para flags instaladas.

**Capítulos relacionados**

- [github/07-tags-and-releases](../../github/07-tags-and-releases/README.pt-BR.md)
- [professional-workflows/12-release-management](../../professional-workflows/12-release-management/README.pt-BR.md)

**Documentação oficial**

- <https://cli.github.com/manual/gh_release_create>

## glab-mr-create

**`glab mr create`**

**Tipo:** Ferramenta externa

**Nível:** Intermediário

**Pesquisar por intenção:** Revisar alterações, Automatizar fluxo

**Risco:** Alteração remota. Cria estado na plataforma e pode notificar pessoas ou acionar automação. Não execute exemplos fictícios contra repositórios reais; exija autorização e verifique destino.

**Finalidade:** Abrir merge request GitLab para integração proposta.

**Pré-requisitos:** Exemplos são modelos fictícios, não exercícios em serviço real. Substitua apenas por repositório sandbox explicitamente autorizado, conta, referências e IDs verificados. Confira versão e autenticação da CLI antes.

**Opções:** --source-branch e --target-branch selecionam branches; --draft cria draft; --push pode publicar commits locais e é omitido aqui.

**Quando utilizar:** Quando branch de origem autorizada publicada está pronta para revisão.

**Quando evitar:** Evite mudanças não revisadas, projeto alvo errado ou contornar política de branches protegidas.

**Sintaxe**

`glab mr create -R example-group/example-project --source-branch feat/notes --target-branch main --title "Review notes" --description "Fictional review" --draft`

**Exemplo básico**

`glab mr create -R example-group/example-project --source-branch feat/notes --target-branch main --title "Review notes" --description "Fictional review" --draft`

Ilustre abertura de draft de branch de origem sandbox publicada.

**Exemplo profissional**

`glab mr create -R example-group/example-project --source-branch feat/docs --target-branch main --title "Review documentation" --description "Describe changes and test evidence"`

Ilustre solicitação autorizada de revisão com branches de origem e destino explícitas.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Condicional
- Outros estados: Condicional

**Resultado esperado:** Cria MR e retorna informações; não integra branch de origem.

**Impactos e efeitos colaterais:** Grava metadados de MR; pode acionar pipelines ou notificações. Formas mostradas usam referências publicadas existentes sem --push.

**Erros comuns:** Tratar criação de MR como aprovação ou presumir que nenhuma automação é acionada.

**Alternativas:** Use interface web GitLab para criação e revisão autorizadas de MR.

**Recuperação:** Verifique link do MR e origem e destino. Se incorreto, coordene edição ou fechamento autorizado; fechar não apaga histórico do MR.

**Versão e dependências:** Exige GitLab CLI (glab) compatível atual, autenticação autorizada, rede e permissões relevantes. Confira glab help e compatibilidade do servidor.

**Capítulos relacionados**

- [gitlab/04-merge-requests-review-and-forks](../../gitlab/04-merge-requests-review-and-forks/README.pt-BR.md)
- [gitlab/08-gitlab-cli-and-platform-comparison](../../gitlab/08-gitlab-cli-and-platform-comparison/README.pt-BR.md)

**Documentação oficial**

- <https://docs.gitlab.com/cli/mr/create/>

## glab-mr-view

**`glab mr view`**

**Tipo:** Ferramenta externa

**Nível:** Intermediário

**Pesquisar por intenção:** Revisar alterações, Inspecionar estado do repositório

**Risco:** Somente leitura. Inspeção não é autorização de merge. Proteja metadados privados e logs; não exponha credenciais.

**Finalidade:** Inspecionar detalhes e estado relatado de merge request GitLab.

**Pré-requisitos:** Exemplos são modelos fictícios, não exercícios em serviço real. Substitua apenas por repositório sandbox explicitamente autorizado, conta, referências e IDs verificados. Confira versão e autenticação da CLI antes.

**Opções:** --output json seleciona saída estruturada; --comments inclui discussões; --web abre página da plataforma.

**Quando utilizar:** Ao verificar MR revisado e estado atual de integração.

**Quando evitar:** Não dependa de flag de conflito enquanto servidor ainda calcula mergeabilidade.

**Sintaxe**

`glab mr view 42 -R example-group/example-project`

**Exemplo básico**

`glab mr view 42 -R example-group/example-project`

Inspecione MR fictício 42 do sandbox.

**Exemplo profissional**

`glab mr view 42 -R example-group/example-project --output json`

Inspecione metadados estruturados do MR; verifique SHA atual e estado de merge antes de decidir.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Exibe informações solicitadas; mergeabilidade e aprovações podem mudar ou estar temporariamente desconhecidas.

**Impactos e efeitos colaterais:** Lê metadados da plataforma pela rede; não altera intencionalmente referências Git, index, checkout ou recursos da plataforma na forma mostrada.

**Erros comuns:** Tratar MR sem conflitos ou aprovação antiga como prova de todos controles aprovados.

**Alternativas:** Inspecione detalhes web do MR e pipeline associado à revisão exata revisada.

**Recuperação:** Inspeção não exige desfazer. Verifique repositório, ID, permissões e associação ao commit exato; atualize status se incompleto ou obsoleto.

**Versão e dependências:** Exige GitLab CLI (glab) compatível atual, autenticação autorizada, rede e permissões relevantes. Confira glab help e compatibilidade do servidor.

**Capítulos relacionados**

- [gitlab/04-merge-requests-review-and-forks](../../gitlab/04-merge-requests-review-and-forks/README.pt-BR.md)
- [gitlab/08-gitlab-cli-and-platform-comparison](../../gitlab/08-gitlab-cli-and-platform-comparison/README.pt-BR.md)

**Documentação oficial**

- <https://docs.gitlab.com/cli/mr/view/>

## glab-ci-status

**`glab ci status`**

**Tipo:** Ferramenta externa

**Nível:** Intermediário

**Pesquisar por intenção:** Inspecionar CI

**Risco:** Somente leitura. Inspeção não é autorização de merge. Proteja metadados privados e logs; não exponha credenciais.

**Finalidade:** Inspecionar status de pipeline CI/CD GitLab para branch.

**Pré-requisitos:** Exemplos são modelos fictícios, não exercícios em serviço real. Substitua apenas por repositório sandbox explicitamente autorizado, conta, referências e IDs verificados. Confira versão e autenticação da CLI antes.

**Opções:** --branch seleciona branch; --compact condensa saída; --live ou --wait aguarda atualizações ou conclusão.

**Quando utilizar:** Ao revisar pipeline relatado da branch e investigar progresso CI.

**Quando evitar:** Não presuma pipeline mais recente da branch seja pipeline exato do head do MR, especialmente entre forks.

**Sintaxe**

`glab ci status -R example-group/example-project --branch=main`

**Exemplo básico**

`glab ci status -R example-group/example-project --branch=main`

Inspecione status relatado de pipeline de branch fictícia sandbox.

**Exemplo profissional**

`glab ci status -R example-group/example-project --branch=feat/docs --compact`

Inspecione status condensado de pipeline da branch e verifique commit e associação ao MR.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Exibe estado relatado do pipeline; conclusão e associação ao commit devem ser conferidas separadamente antes de merge.

**Impactos e efeitos colaterais:** Lê metadados da plataforma pela rede; não altera intencionalmente referências Git, index, checkout ou recursos da plataforma na forma mostrada.

**Erros comuns:** Confundir pipeline pendente ou alheio da branch com check obrigatório do MR aprovado.

**Alternativas:** Use página web do MR e pipeline vinculado para inspecionar resultados e logs exatos de jobs.

**Recuperação:** Inspeção não exige desfazer. Verifique repositório, ID, permissões e associação ao commit exato; atualize status se incompleto ou obsoleto.

**Versão e dependências:** Exige GitLab CLI (glab) compatível atual, autenticação autorizada, rede e permissões relevantes. Confira glab help e compatibilidade do servidor.

**Capítulos relacionados**

- [gitlab/06-pipelines-and-runners](../../gitlab/06-pipelines-and-runners/README.pt-BR.md)
- [ci-cd/04-gitlab-ci-cd](../../ci-cd/04-gitlab-ci-cd/README.pt-BR.md)

**Documentação oficial**

- <https://docs.gitlab.com/cli/ci/status/>


---

<!-- navigation-footer -->
[Anterior](../13-security-and-maintenance/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo módulo](../../practical-projects/README.pt-BR.md)
<!-- /navigation-footer -->
