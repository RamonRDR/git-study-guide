# 06 Gerenciamento de branches

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../05-history-and-comparison/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../07-merge-rebase-and-conflicts/README.pt-BR.md)
<!-- /navigation -->

Gerado a partir do JSON canônico. Edite os registros, não esta página.

As entradas descrevem comandos e operações, não uma sequência a executar. Pratique em repositórios descartáveis. Operações hospedadas são opcionais.

**Total de entradas distintas: 10**

- [`git branch --list`](#git-branch-list)
- [`git branch NAME`](#git-branch-create)
- [`git branch --show-current`](#git-branch-show-current)
- [`git switch`](#git-switch)
- [`git switch -c`](#git-switch-create)
- [`git switch --detach`](#git-switch-detach)
- [`git branch -m`](#git-branch-rename)
- [`git branch -d`](#git-branch-delete)
- [`git branch --merged`](#git-branch-merged)
- [`git branch --set-upstream-to`](#git-branch-upstream)

## git-branch-list

**`git branch --list`**

**Tipo:** Uso de opção

**Nível:** Iniciante

**Pesquisar por intenção:** Gerenciar branches, Inspecionar referências

**Risco:** Somente leitura. Inspeção somente leitura; confira nomes de branches antes de compartilhar saída.

**Finalidade:** Listar nomes de branches locais, opcionalmente filtrados por padrão.

**Pré-requisitos:** Use repositório próprio descartável com commit existente. Inspecione status e referências antes de operar.

**Opções:** --list seleciona listagem explicitamente; -a inclui referências de rastreamento remoto e -vv mostra informações de upstream e outros detalhes.

**Quando utilizar:** Ao inspecionar branches disponíveis antes de selecionar ou limpar trabalho.

**Quando evitar:** Não trate lista local como inventário remoto em tempo real.

**Sintaxe**

`git branch --list "feat/*"`

**Exemplo básico**

`git branch --list`

Inspecione branches locais.

**Exemplo profissional**

`git branch --list "feat/*"`

Inspecione branches locais de feature sem criar uma.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Exibe branches correspondentes; a branch local atual é marcada com asterisco na saída normal.

**Impactos e efeitos colaterais:** Nenhum conteúdo rastreado, snapshot preparado, referência local ou estado remoto é alterado por esta inspeção.

**Erros comuns:** Omitir --list com nome ou padrão pode ser interpretado como criação de branch.

**Alternativas:** Use git branch --show-current para apenas a branch atual ou git show-ref para inspecionar IDs.

**Recuperação:** Listagem não exige recuperação; inspecione referência ou filtro selecionado se a saída for inesperada.

**Versão e dependências:** Sintaxe padrão documentada no Git 2.34; não exige ferramenta opcional.

**Capítulos relacionados**

- [branches/01-create-and-switch](../../branches/01-create-and-switch/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-branch/2.34.0>

## git-branch-create

**`git branch NAME`**

**Tipo:** Uso de opção

**Nível:** Iniciante

**Pesquisar por intenção:** Gerenciar branches, Trabalhar em paralelo

**Risco:** Alteração de estado. Verifique nome e ponto inicial; não use força para resolver colisões de nome.

**Finalidade:** Criar branch local nomeada em commit existente sem trocar para ela.

**Pré-requisitos:** Use repositório próprio descartável com commit existente. Inspecione status e referências antes de operar.

**Opções:** Informe nome novo e ponto inicial opcional; sem ponto inicial usa HEAD. --no-track impede configuração automática de upstream.

**Quando utilizar:** Ao preparar linha de trabalho independente ou preservar commit.

**Quando evitar:** Evite criar branch de revisão não verificada ou sobrescrever branch existente com -f.

**Sintaxe**

`git branch feat/notes main`

**Exemplo básico**

`git branch feat/notes`

Crie branch local em HEAD atual.

**Exemplo profissional**

`git branch feat/review main`

Crie branch na ponta existente verificada da main.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Altera
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** Nova referência local aponta para commit selecionado; HEAD permanece onde estava.

**Impactos e efeitos colaterais:** Adiciona referência de branch e possivelmente reflog ou configuração de rastreamento; arquivos de trabalho e index não mudam.

**Erros comuns:** Presumir que criar branch também troca para ela ou copia uma pasta.

**Alternativas:** Use git switch -c para criar e selecionar em uma operação.

**Recuperação:** Inspecione ambas referências; se branch nova sem uso estiver errada, remova só após confirmar ponta alcançável por referência sobrevivente pretendida.

**Versão e dependências:** Sintaxe padrão documentada no Git 2.34; não exige ferramenta opcional.

**Capítulos relacionados**

- [branches/01-create-and-switch](../../branches/01-create-and-switch/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-branch/2.34.0>

## git-branch-show-current

**`git branch --show-current`**

**Tipo:** Uso de opção

**Nível:** Iniciante

**Pesquisar por intenção:** Inspecionar estado do repositório, Gerenciar branches

**Risco:** Somente leitura. Inspeção somente leitura; confira nomes de branches antes de compartilhar saída.

**Finalidade:** Exibir nome da branch local atual quando HEAD está associado.

**Pré-requisitos:** Use repositório próprio descartável com commit existente. Inspecione status e referências antes de operar.

**Opções:** --show-current seleciona saída de nome único; fica vazia em HEAD destacado.

**Quando utilizar:** Ao confirmar branch ativa antes de commit ou troca.

**Quando evitar:** Não presuma que saída vazia é nome de branch ou prova de falha do comando.

**Sintaxe**

`git branch --show-current`

**Exemplo básico**

`git branch --show-current`

Confira qual branch está ativa.

**Exemplo profissional**

`git branch --show-current`

Antes do commit, confirme a branch de feature esperada.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Exibe nome da branch ou nenhum nome se HEAD estiver destacado.

**Impactos e efeitos colaterais:** Nenhum conteúdo rastreado, snapshot preparado, referência local ou estado remoto é alterado por esta inspeção.

**Erros comuns:** Presumir que retorna ID do commit ou upstream remoto.

**Alternativas:** Use git symbolic-ref --quiet --short HEAD para conferir HEAD simbólico, ou git rev-parse HEAD para ID do commit.

**Recuperação:** Listagem não exige recuperação; inspecione referência ou filtro selecionado se a saída for inesperada.

**Versão e dependências:** Git 2.22 ou superior suporta --show-current; o guia usa Git 2.40 ou superior nos laboratórios.

**Capítulos relacionados**

- [branches/01-create-and-switch](../../branches/01-create-and-switch/README.pt-BR.md)
- [branches/05-detached-head](../../branches/05-detached-head/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-branch/2.34.0>

## git-switch

**`git switch`**

**Tipo:** Comando nativo

**Nível:** Iniciante

**Pesquisar por intenção:** Trocar contexto de trabalho, Gerenciar branches

**Risco:** Alteração de estado. Edições compatíveis podem acompanhar a troca; edições conflitantes podem bloqueá-la. Não use opções de força ou descarte.

**Finalidade:** Selecionar branch existente para trabalho posterior.

**Pré-requisitos:** Use repositório próprio descartável com status limpo, commit existente e hooks locais confiáveis. Preserve trabalho valioso primeiro.

**Opções:** --no-guess desativa criação automática baseada em branch de rastreamento remoto correspondente única; - abrevia checkout anterior.

**Quando utilizar:** Ao alternar entre linhas locais de trabalho existentes.

**Quando evitar:** Evite sair de commits destacados não preservados ou forçar diante de edições conflitantes.

**Sintaxe**

`git switch main`

**Exemplo básico**

`git switch main`

Retorne à main local existente após preservar trabalho.

**Exemplo profissional**

`git switch --no-guess feat/notes`

Selecione branch local de feature existente verificada sem criação automática de branch de rastreamento.

**Impacto no estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / histórico: Altera
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** HEAD aponta para branch selecionada; arquivos rastreados e index refletem novo contexto com edições compatíveis preservadas quando possível.

**Impactos e efeitos colaterais:** Seleciona HEAD e atualiza index e arquivos de trabalho conforme necessário; hooks post-checkout configurados podem afetar outros estados locais. Não ocorre push nem merge.

**Erros comuns:** Confundir troca com merge ou esperar que todas edições não registradas fiquem na branch antiga.

**Alternativas:** Git antigo usa git checkout com nome de branch verificado; prefira switch pela clareza nos laboratórios atuais.

**Recuperação:** Se troca falhar, inspecione status e preserve edições; não force. Retorne à branch original quando limpo e salve antes commits destacados desejados.

**Versão e dependências:** Git 2.23 introduziu switch; a base de prática do guia é Git 2.40 ou superior. A sintaxe mostrada está documentada no manual Git 2.35.

**Capítulos relacionados**

- [branches/01-create-and-switch](../../branches/01-create-and-switch/README.pt-BR.md)
- [branches/03-switch-safety-and-naming](../../branches/03-switch-safety-and-naming/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-switch/2.35.0>

## git-switch-create

**`git switch -c`**

**Tipo:** Uso de opção

**Nível:** Iniciante

**Pesquisar por intenção:** Gerenciar branches, Trocar contexto de trabalho, Trabalhar em paralelo

**Risco:** Alteração de estado. Edições compatíveis podem acompanhar a troca; edições conflitantes podem bloqueá-la. Não use opções de força ou descarte.

**Finalidade:** Criar branch local nova e trocar para ela em uma operação.

**Pré-requisitos:** Use repositório próprio descartável com status limpo, commit existente e hooks locais confiáveis. Preserve trabalho valioso primeiro.

**Opções:** -c exige nome novo e aceita ponto inicial opcional; não confunda com -C, que pode redefinir branch existente.

**Quando utilizar:** Ao iniciar tarefa isolada ou nomear commit destacado antes de sair dele.

**Quando evitar:** Evite usar ponto inicial não verificado ou sobrescrever nome existente.

**Sintaxe**

`git switch -c feat/notes main`

**Exemplo básico**

`git switch -c feat/notes`

Inicie tarefa no commit atual.

**Exemplo profissional**

`git switch -c feat/review main`

Inicie tarefa de revisão de commit local verificado da main.

**Impacto no estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / histórico: Altera
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** Em sucesso, branch nova aponta ao ponto inicial escolhido e HEAD a seleciona; se troca falhar a branch não é criada.

**Impactos e efeitos colaterais:** Seleciona HEAD e atualiza index e arquivos de trabalho conforme necessário; hooks post-checkout configurados podem afetar outros estados locais. Não ocorre push nem merge.

**Erros comuns:** Usar -C para contornar colisão ou presumir que branch nova sempre começa na main.

**Alternativas:** Use git branch NAME START e git switch NAME separadamente quando criar sem trocar for útil.

**Recuperação:** Verifique HEAD e ambas referências; preserve commits novos antes de retornar à branch original ou limpar.

**Versão e dependências:** Git 2.23 introduziu switch; a base de prática do guia é Git 2.40 ou superior. A sintaxe mostrada está documentada no manual Git 2.35.

**Capítulos relacionados**

- [branches/01-create-and-switch](../../branches/01-create-and-switch/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-switch/2.35.0>

## git-switch-detach

**`git switch --detach`**

**Tipo:** Uso de opção

**Nível:** Intermediário

**Pesquisar por intenção:** Trocar contexto de trabalho, Inspecionar histórico, Recuperar trabalho

**Risco:** Alteração de estado. Commits destacados podem ficar inalcançáveis; recuperação não é garantida. Preserve antes de trocar.

**Finalidade:** Selecionar commit diretamente sem associar HEAD a branch.

**Pré-requisitos:** Use repositório próprio descartável com status limpo, commit existente e hooks locais confiáveis. Preserve trabalho valioso primeiro.

**Opções:** --detach solicita HEAD destacado explicitamente; use commit verificado ou tag que resolve para commit.

**Quando utilizar:** Ao inspecionar snapshots históricos ou realizar experimento descartável.

**Quando evitar:** Evite deixar commits desejados sem nome ou tratar trabalho destacado como atualizações da main.

**Sintaxe**

`git switch --detach HEAD~1`

**Exemplo básico**

`git switch --detach HEAD~1`

Inspecione o primeiro pai de commit atual não inicial.

**Exemplo profissional**

`git switch --detach v1.0.0`

Inspecione tag local de versão existente que resolve para commit.

**Impacto no estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / histórico: Altera
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** HEAD aponta diretamente para commit; pontas de branches não mudam e --show-current não imprime nome.

**Impactos e efeitos colaterais:** Seleciona HEAD e atualiza index e arquivos de trabalho conforme necessário; hooks post-checkout configurados podem afetar outros estados locais. Não ocorre push nem merge.

**Erros comuns:** Presumir que commits criados em estado destacado avançam branch selecionada anteriormente.

**Alternativas:** Crie branch temporária nomeada se houver expectativa de preservar mudanças.

**Recuperação:** Antes de sair, use git switch -c com nome livre para preservar commits desejados; se já saiu, inspecione reflog e nomeie commit verificado se disponível.

**Versão e dependências:** Git 2.23 introduziu switch; a base de prática do guia é Git 2.40 ou superior. A sintaxe mostrada está documentada no manual Git 2.35.

**Capítulos relacionados**

- [branches/05-detached-head](../../branches/05-detached-head/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-switch/2.35.0>

## git-branch-rename

**`git branch -m`**

**Tipo:** Uso de opção

**Nível:** Intermediário

**Pesquisar por intenção:** Gerenciar branches

**Risco:** Alteração de estado. Confira ambos nomes e dependências; evite substituição forçada.

**Finalidade:** Renomear branch local e mover configuração associada e reflog quando presentes.

**Pré-requisitos:** Use repositório próprio descartável com commit existente. Inspecione status e referências antes de operar.

**Opções:** -m aceita nomes antigo e novo ou só nome novo para branch atual; -M força substituição e não é usado aqui.

**Quando utilizar:** Ao corrigir nome de branch privada conforme convenções da equipe.

**Quando evitar:** Evite renomear branches compartilhadas sem coordenação ou usar -M para substituir outra branch.

**Sintaxe**

`git branch -m feat/old feat/new`

**Exemplo básico**

`git branch -m feat/notes feat/docs`

Renomeie branch privada existente para nome livre.

**Exemplo profissional**

`git branch -m feat/review`

Renomeie branch privada atual para nome livre.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Altera
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** Novo nome local identifica a mesma ponta; nome antigo desaparece. Se atual, HEAD acompanha branch renomeada.

**Impactos e efeitos colaterais:** Move referências locais, configuração e reflog quando presentes, não conteúdo de commits nem nomes de branches remotas.

**Erros comuns:** Esperar que branch remota ou nome do destino upstream seja renomeado automaticamente.

**Alternativas:** Mantenha nome existente quando colaboradores ou automação dependerem dele.

**Recuperação:** Verifique ponta, upstream e nome original livre antes de renomear de volta com -m; coordene se já compartilhada.

**Versão e dependências:** Sintaxe padrão documentada no Git 2.34; não exige ferramenta opcional.

**Capítulos relacionados**

- [branches/03-switch-safety-and-naming](../../branches/03-switch-safety-and-naming/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-branch/2.34.0>

## git-branch-delete

**`git branch -d`**

**Tipo:** Uso de opção

**Nível:** Intermediário

**Pesquisar por intenção:** Gerenciar branches, Proteger histórico

**Risco:** Destrutivo. Exclusão pode remover último nome conveniente do trabalho; nunca use -D para contornar recusa sem avaliação separada. Recuperação não é garantida.

**Finalidade:** Excluir branch local com proteção de estado integrado.

**Pré-requisitos:** Use repositório próprio descartável; verifique que branch alvo não está selecionada em nenhum worktree e ponta é alcançável pela branch sobrevivente pretendida. Registre seu ID.

**Opções:** -d confere integração completa no upstream configurado, ou HEAD se não houver upstream; -D ignora essa proteção e não é alternativa em dúvida.

**Quando utilizar:** Ao limpar branches privadas cujos commits são preservados pelo destino pretendido.

**Quando evitar:** Evite excluir trabalho sem alcance verificado, ou forçar exclusão após squash merge sem revisar conteúdo e histórico.

**Sintaxe**

`git branch -d feat/notes`

**Exemplo básico**

`git branch -d feat/notes`

Com main selecionada, remova apenas branch privada contida verificada sem upstream.

**Exemplo profissional**

`git branch -d feat/review`

Após confirmar ancestralidade, upstream e estado de worktrees, remova branch local de revisão.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Altera
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** Referência local e reflog da branch, se presente, são removidos em sucesso; caso contrário Git pode recusar.

**Impactos e efeitos colaterais:** Remove nome local e metadados associados; não apaga imediatamente objetos de commit nem remove branches remotas.

**Erros comuns:** Presumir que -d sempre confere main ou que squash merge preserva ancestralidade dos commits.

**Alternativas:** Mantenha branch se houver dúvida; inspecione git branch --merged main e git log main..NAME antes.

**Recuperação:** Se commit registrado ainda existir, recrie branch no ID verificado; configuração e reflog antigos não são restaurados automaticamente.

**Versão e dependências:** Sintaxe padrão documentada no Git 2.34; não exige ferramenta opcional.

**Capítulos relacionados**

- [branches/04-safe-local-deletion](../../branches/04-safe-local-deletion/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-branch/2.34.0>

## git-branch-merged

**`git branch --merged`**

**Tipo:** Uso de opção

**Nível:** Intermediário

**Pesquisar por intenção:** Gerenciar branches, Inspecionar histórico, Proteger histórico

**Risco:** Somente leitura. Inspeção somente leitura; confira nomes de branches antes de compartilhar saída.

**Finalidade:** Listar branches cujos commits de ponta são alcançáveis a partir de commit selecionado.

**Pré-requisitos:** Use repositório próprio descartável com commit existente. Inspecione status e referências antes de operar.

**Opções:** --merged usa HEAD por padrão; --no-merged seleciona conjunto oposto. Informe destino explícito como main.

**Quando utilizar:** Ao revisar ancestralidade antes de limpar branches locais.

**Quando evitar:** Não equipare ausência na lista à ausência de mudanças equivalentes após squash ou cherry-pick.

**Sintaxe**

`git branch --merged main`

**Exemplo básico**

`git branch --merged main`

Inspecione pontas locais contidas na main existente.

**Exemplo profissional**

`git branch --no-merged main`

Identifique pontas locais não contidas na main antes de revisar candidatos à limpeza.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Exibe pontas de branches selecionadas ancestrais do destino ou iguais a ele.

**Impactos e efeitos colaterais:** Nenhum conteúdo rastreado, snapshot preparado, referência local ou estado remoto é alterado por esta inspeção.

**Erros comuns:** Presumir que lista prova que branch pode ser excluída independentemente de worktrees ou configuração upstream.

**Alternativas:** Use git merge-base --is-ancestor NAME main para testar branch verificada contra main.

**Recuperação:** Listagem não exige recuperação; inspecione referência ou filtro selecionado se a saída for inesperada.

**Versão e dependências:** Sintaxe padrão documentada no Git 2.34; não exige ferramenta opcional.

**Capítulos relacionados**

- [branches/04-safe-local-deletion](../../branches/04-safe-local-deletion/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-branch/2.34.0>

## git-branch-upstream

**`git branch --set-upstream-to`**

**Tipo:** Uso de opção

**Nível:** Intermediário

**Pesquisar por intenção:** Gerenciar branches, Sincronizar repositórios, Configurar Git

**Risco:** Alteração de estado. Rastreamento errado pode afetar pull e push posteriores conforme configuração; verifique git branch -vv antes de sincronizar.

**Finalidade:** Configurar qual branch uma branch local existente rastreia como upstream.

**Pré-requisitos:** Use clone próprio descartável ou laboratório com remoto local. Verifique branch local, referência de rastreamento remoto existente e relação upstream pretendida; não contate serviço real para prática.

**Opções:** -u abrevia --set-upstream-to; omita argumento de branch local para configurar a atual. --unset-upstream remove configuração de rastreamento.

**Quando utilizar:** Quando branch precisa de relação de rastreamento explícita verificada para status e sincronização.

**Quando evitar:** Evite selecionar destino de integração diferente acidentalmente ou presumir que executa fetch ou push.

**Sintaxe**

`git branch --set-upstream-to=origin/main main`

**Exemplo básico**

`git branch --set-upstream-to=origin/main main`

Em laboratório de clone local, associe main existente à referência origin/main verificada.

**Exemplo profissional**

`git branch -u origin/feat/notes feat/notes`

Após conferir ambas referências existentes, corrija rastreamento de branch privada de feature no laboratório local.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Altera

**Resultado esperado:** Configuração local de rastreamento identifica upstream escolhido; git branch -vv pode exibir relação.

**Impactos e efeitos colaterais:** Altera configuração local de branch; não exige movimento de referência, checkout ou transferência de rede.

**Erros comuns:** Confundir configuração upstream com publicação remota ou esperar que rastreamento sozinho mantenha referências atualizadas.

**Alternativas:** Use argumentos explícitos de remoto e referência para fetch ou push quando padrões de rastreamento não forem desejados.

**Recuperação:** Registre upstream anterior; restaure explicitamente ou use git branch --unset-upstream para branch local se nenhum existia.

**Versão e dependências:** Sintaxe padrão documentada no Git 2.34; não exige ferramenta opcional.

**Capítulos relacionados**

- [remote-repositories/02-fetch-and-tracking](../../remote-repositories/02-fetch-and-tracking/README.pt-BR.md)
- [remote-repositories/03-pull-push-and-divergence](../../remote-repositories/03-pull-push-and-divergence/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-branch/2.34.0>


---

<!-- navigation-footer -->
[Anterior](../05-history-and-comparison/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../07-merge-rebase-and-conflicts/README.pt-BR.md)
<!-- /navigation-footer -->
