# 11 Operações avançadas

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../10-search-and-troubleshooting/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../12-internals-and-plumbing/README.pt-BR.md)
<!-- /navigation -->

Gerado a partir do JSON canônico. Edite os registros, não esta página.

As entradas descrevem comandos e operações, não uma sequência a executar. Pratique em repositórios descartáveis. Operações hospedadas são opcionais.

**Total de entradas distintas: 9**

- [`git worktree add`](#git-worktree-add)
- [`git submodule add`](#git-submodule-add)
- [`git submodule update --init --recursive`](#git-submodule-update)
- [`git subtree add`](#git-subtree-add)
- [`git rerere`](#git-rerere)
- [`git sparse-checkout set`](#git-sparse-checkout-set)
- [`git clone --filter`](#git-clone-filter)
- [`git archive`](#git-archive)
- [`git bundle create`](#git-bundle-create)

## git-worktree-add

**`git worktree add`**

**Tipo:** Subcomando

**Nível:** Avançado

**Pesquisar por intenção:** Trabalhar em paralelo, Gerenciar branches

**Risco:** Alteração de estado. Revise caminhos, referências e configuração local antes. Preserve trabalho valioso; nunca teste contra o guia ou serviço compartilhado.

**Finalidade:** Criar checkout vinculado adicional compartilhando objetos e maioria das referências.

**Pré-requisitos:** Use repositório próprio descartável limpo com trabalho salvo, caminhos locais e referências verificados e configuração confiável. Use só origens locais próprias.

**Opções:** -b cria branch; --detach usa checkout destacado; git worktree list exibe worktrees registradas.

**Quando utilizar:** Ao trabalhar em tarefas independentes sem alternar repetidamente checkout original.

**Quando evitar:** Evite reutilizar caminho ocupado ou forçar mesma branch em múltiplas worktrees.

**Sintaxe**

`git worktree add -b feat/notes ../notes-lab main`

**Exemplo básico**

`git worktree add -b feat/notes ../notes-lab main`

Crie worktree vinculada em caminho vizinho livre e branch nova.

**Exemplo profissional**

`git worktree add --detach ../review-lab main`

Inspecione main verificada em checkout destacado separado.

**Impacto no estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / histórico: Condicional
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** Cria checkout vinculado com HEAD e index próprios; branch nova opcional é compartilhada entre worktrees.

**Impactos e efeitos colaterais:** Cria arquivos e metadados de worktree, possivelmente referência nova; conteúdo do checkout original não muda na forma mostrada.

**Erros comuns:** Tratar worktrees vinculadas como clones independentes ou excluir diretórios manualmente.

**Alternativas:** Use clone separado quando referências e armazenamento de objetos independentes forem necessários.

**Recuperação:** Preserve edições da worktree vinculada, confira status limpo nela, depois use git worktree remove com caminho exato; inspecione worktree list depois.

**Versão e dependências:** Use Git 2.40 ou superior nos laboratórios do guia; verifique disponibilidade na ajuda local Git.

**Capítulos relacionados**

- [advanced-git/02-worktree](../../advanced-git/02-worktree/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-worktree>

## git-submodule-add

**`git submodule add`**

**Tipo:** Subcomando

**Nível:** Avançado

**Pesquisar por intenção:** Gerenciar dependências de repositórios

**Risco:** Alteração de estado. Revise caminhos, referências e configuração local antes. Preserve trabalho valioso; nunca teste contra o guia ou serviço compartilhado.

**Finalidade:** Registrar repositório separado como submódulo fixado por gitlink no projeto pai.

**Pré-requisitos:** Use repositório próprio descartável limpo com trabalho salvo, caminhos locais e referências verificados e configuração confiável. Use só origens locais próprias. Para a URL relativa mostrada, garanta que a biblioteca seja vizinha do remoto padrão do pai (ou do repositório pai local se não houver remoto padrão).

**Opções:** Informe repositório e caminho; -b define preferência de branch para atualizações remotas, não substitui gitlink registrado. URLs relativas são resolvidas em relação ao remoto padrão do repositório pai, ou ao repositório local quando não há remoto padrão configurado; organize origens bare vizinhas para simulações de clone.

**Quando utilizar:** Quando dependência deve manter histórico independente e versão explicitamente fixada.

**Quando evitar:** Evite URLs de submódulos não confiáveis, arquivos valiosos no destino ou liberações amplas de protocolo.

**Sintaxe**

`git submodule add ../library.git vendor/library`

**Exemplo básico**

`git submodule add ../library.git vendor/library`

Adicione repositório de biblioteca local próprio populado em caminho livre; transporte file local pode exigir permissão explícita no laboratório.

**Exemplo profissional**

`git -c protocol.file.allow=always submodule add ../library.git vendor/library`

Só no laboratório isolado confiável, permita origem local própria nesta invocação.

**Impacto no estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / histórico: Condicional
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** Normalmente cria checkout de submódulo, prepara .gitmodules e gitlink; commit pai ainda exige revisão e registro.

**Impactos e efeitos colaterais:** Altera arquivos, index e configuração ou objetos locais de submódulo; não publica projeto pai.

**Erros comuns:** Presumir submódulo como arquivos comuns copiados ou mudanças não registradas incluídas no commit pai.

**Alternativas:** Use integração subtree ou gerenciador de pacotes quando checkout separado for indesejado.

**Recuperação:** Inspecione .gitmodules, gitlink preparado e status do submódulo; preserve commits do submódulo antes de fluxo revisado de remoção. Não exclua metadados simplesmente.

**Versão e dependências:** Use Git 2.40 ou superior nos laboratórios do guia; verifique disponibilidade na ajuda local Git.

**Capítulos relacionados**

- [advanced-git/03-submodules](../../advanced-git/03-submodules/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-submodule>

## git-submodule-update

**`git submodule update --init --recursive`**

**Tipo:** Uso de opção

**Nível:** Avançado

**Pesquisar por intenção:** Gerenciar dependências de repositórios, Sincronizar repositórios

**Risco:** Alteração de estado. Revise caminhos, referências e configuração local antes. Preserve trabalho valioso; nunca teste contra o guia ou serviço compartilhado.

**Finalidade:** Popular submódulos registrados e atualizar checkouts, normalmente para commits registrados pelo pai.

**Pré-requisitos:** Use repositório próprio descartável limpo com trabalho salvo, caminhos locais e referências verificados e configuração confiável. Use só origens locais próprias. Revise URLs relativas resolvidas antes de inicializar; no laboratório, clone de uma origem bare pai vizinha para que a URL relativa da biblioteca seja resolvida corretamente.

**Opções:** --init inicializa submódulos não inicializados; --recursive desce aos aninhados; procedimento padrão de checkout normalmente destaca HEAD do submódulo.

**Quando utilizar:** Ao preparar checkout consistente de projeto com dependências fixadas.

**Quando evitar:** Evite URLs aninhadas não revisadas, mudanças de submódulos não preservadas ou --force para contornar recusa.

**Sintaxe**

`git submodule update --init --recursive`

**Exemplo básico**

`git submodule update --init --recursive`

Inicialize e atualize submódulos confiáveis registrados para commits registrados no laboratório.

**Exemplo profissional**

`git -c protocol.file.allow=always submodule update --init --recursive`

Só para URLs de submódulos locais próprios revisados, permita transporte file local nesta invocação.

**Impacto no estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / histórico: Condicional
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** Pode clonar submódulos ausentes, buscar objetos e selecionar commits registrados; estratégias configuradas podem diferir.

**Impactos e efeitos colaterais:** Altera arquivos, index, referências e configuração de submódulo; normalmente não move ponta da branch pai.

**Erros comuns:** Esperar versões mais novas de branches remotas em vez de commits registrados ou presumir status pai prova checkouts aninhados limpos.

**Alternativas:** Use git submodule status --recursive para inspecionar sem atualizar.

**Recuperação:** Inspecione caminhos com falha e pontas salvas de submódulos; preserve commits destacados com branch nomeada antes de tentar novamente. Não force às cegas.

**Versão e dependências:** Use Git 2.40 ou superior nos laboratórios do guia; verifique disponibilidade na ajuda local Git.

**Capítulos relacionados**

- [advanced-git/03-submodules](../../advanced-git/03-submodules/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-submodule>

## git-subtree-add

**`git subtree add`**

**Tipo:** Ferramenta externa

**Nível:** Avançado

**Pesquisar por intenção:** Gerenciar dependências de repositórios, Integrar alterações

**Risco:** Alteração de estado. Revise caminhos, referências e configuração local antes. Preserve trabalho valioso; nunca teste contra o guia ou serviço compartilhado.

**Finalidade:** Importar conteúdo de outro repositório em diretório do projeto atual com helper subtree opcional.

**Pré-requisitos:** Use repositório próprio descartável limpo com trabalho salvo, caminhos locais e referências verificados e configuração confiável. Use só origens locais próprias.

**Opções:** --prefix seleciona destino; --squash combina histórico importado em vez de manter todo commit de origem na ancestralidade do destino.

**Quando utilizar:** Ao versionar conteúdo de dependência diretamente no checkout pai mantendo fluxo de sincronização.

**Quando evitar:** Evite prefixo ocupado, estado sujo ou importação sem revisar licença e conteúdo.

**Sintaxe**

`git subtree add --prefix=vendor/library ../library.git main --squash`

**Exemplo básico**

`git subtree add --prefix=vendor/library ../library.git main --squash`

Importe branch de origem local própria em prefixo livre.

**Exemplo profissional**

`git subtree add --prefix=vendor/tools ../tools.git main --squash`

Integre snapshot local de ferramentas revisado sob diretório novo.

**Impacto no estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / histórico: Condicional
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** Em sucesso cria histórico de integração e importa conteúdo de origem sob prefixo selecionado.

**Impactos e efeitos colaterais:** Pode buscar objetos, criar commits, avançar branch atual e atualizar index e working tree.

**Erros comuns:** Confundir subtree com submódulo ou presumir --squash não produz commit de integração.

**Alternativas:** Use submódulo para checkout fixado separado ou gerenciador de pacotes para dependências publicadas.

**Recuperação:** Inspecione ponta original salva e ancestralidade resultante; se inadequada, preserve trabalho e escolha recuperação privada revisada ou correção compartilhada.

**Versão e dependências:** Git subtree é helper distribuído opcional; verifique disponibilidade de git subtree antes de usar. Use Git 2.40 ou superior em laboratórios.

**Capítulos relacionados**

- [advanced-git/04-subtree](../../advanced-git/04-subtree/README.pt-BR.md)

**Documentação oficial**

- <https://github.com/git/git/tree/master/contrib/subtree>

## git-rerere

**`git rerere`**

**Tipo:** Comando nativo

**Nível:** Avançado

**Pesquisar por intenção:** Resolver conflitos

**Risco:** Alteração de estado. Revise caminhos, referências e configuração local antes. Preserve trabalho valioso; nunca teste contra o guia ou serviço compartilhado.

**Finalidade:** Registrar e reutilizar resoluções para padrões de conflito correspondentes.

**Pré-requisitos:** Use repositório próprio descartável limpo com trabalho salvo, caminhos locais e referências verificados e configuração confiável. Use só origens locais próprias.

**Opções:** Habilite rerere.enabled localmente no laboratório; git rerere status e diff inspecionam registros atuais; autoupdate pode preparar resultados reutilizados.

**Quando utilizar:** Ao resolver repetidamente conflitos semelhantes em fluxos privados de integração.

**Quando evitar:** Evite aceitar resoluções reutilizadas às cegas ou compartilhar cache com material sensível.

**Sintaxe**

`git rerere`

**Exemplo básico**

`git rerere`

Em laboratório descartável de conflitos repetidos, inspecione e registre ou reutilize resolução conforme apropriado.

**Exemplo profissional**

`git rerere`

Após revisar conflito repetido, permita rerere habilitado reutilizar resolução registrada e inspecione-a.

**Impacto no estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / histórico: Condicional
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** Pode registrar conflitos e resoluções ou aplicar correspondência registrada; index pode atualizar conforme configuração.

**Impactos e efeitos colaterais:** Pode alterar cache de resolução e arquivos, e possivelmente index; rerere comum não cria commit novo na branch.

**Erros comuns:** Presumir texto de conflito correspondente garante correção semântica.

**Alternativas:** Resolva manualmente e revise diff e testes quando reutilização for insegura.

**Recuperação:** Inspecione rerere diff e status; corrija e prepare conteúdo revisado. Use rerere forget só para caminho afetado verificado ao substituir resolução registrada ruim.

**Versão e dependências:** Use Git 2.40 ou superior nos laboratórios do guia; verifique disponibilidade na ajuda local Git.

**Capítulos relacionados**

- [advanced-git/06-rerere](../../advanced-git/06-rerere/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-rerere>

## git-sparse-checkout-set

**`git sparse-checkout set`**

**Tipo:** Subcomando

**Nível:** Avançado

**Pesquisar por intenção:** Limitar checkout ou clone, Inspecionar arquivos

**Risco:** Alteração de estado. Revise caminhos, referências e configuração local antes. Preserve trabalho valioso; nunca teste contra o guia ou serviço compartilhado.

**Finalidade:** Configurar working tree esparsa contendo caminhos selecionados em vez de todo caminho rastreado.

**Pré-requisitos:** Use repositório próprio descartável limpo com trabalho salvo, caminhos locais e referências verificados e configuração confiável. Use só origens locais próprias.

**Opções:** --cone seleciona regras por diretório; list exibe seleções; disable retorna a checkout completo.

**Quando utilizar:** Quando apenas parte de repositório grande é necessária ao trabalho atual.

**Quando evitar:** Evite alterar padrões esparsos com edições valiosas não salvas ou presumir caminhos omitidos excluídos do histórico.

**Sintaxe**

`git sparse-checkout set --cone docs`

**Exemplo básico**

`git sparse-checkout set --cone docs`

Selecione diretório docs existente em checkout descartável limpo.

**Exemplo profissional**

`git sparse-checkout set --cone src tests`

Limite conteúdo materializado aos diretórios de código e testes existentes selecionados, mais regras cone.

**Impacto no estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / histórico: Condicional
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** Working tree materializa caminhos selecionados conforme regras cone, incluindo alguns arquivos de níveis ancestrais; outros caminhos rastreados podem faltar.

**Impactos e efeitos colaterais:** Atualiza configuração esparsa, index e working tree; não reescreve histórico registrado em repositório local completo comum.

**Erros comuns:** Confundir checkout esparso com clone raso ou parcial e presumir só diretórios nomeados visíveis.

**Alternativas:** Use checkout completo se ferramentas exigirem todos arquivos rastreados; clone parcial controla transferência de objetos separadamente.

**Recuperação:** Preserve edições, inspecione sparse-checkout list e use sparse-checkout disable para restaurar materialização completa quando seguro.

**Versão e dependências:** Use Git 2.40 ou superior nos laboratórios do guia; verifique disponibilidade na ajuda local Git.

**Capítulos relacionados**

- [advanced-git/07-sparse-checkout](../../advanced-git/07-sparse-checkout/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-sparse-checkout>

## git-clone-filter

**`git clone --filter`**

**Tipo:** Uso de opção

**Nível:** Avançado

**Pesquisar por intenção:** Limitar checkout ou clone, Criar repositório

**Risco:** Alteração de estado. Revise caminhos, referências e configuração local antes. Preserve trabalho valioso; nunca teste contra o guia ou serviço compartilhado.

**Finalidade:** Solicitar clone parcial que omite inicialmente tipos de objeto selecionados quando origem suporta filtro.

**Pré-requisitos:** Use diretório pai descartável, destino livre e origem bare própria configurada localmente com uploadpack.allowFilter=true; verifique caminho e capacidade.

**Opções:** --filter=blob:none solicita omissão de blobs até necessários; --no-checkout evita checkout inicial; --no-local usa transporte em vez de otimização de cópia local.

**Quando utilizar:** Ao reduzir transferência inicial de objetos de origem grande compatível.

**Quando evitar:** Evite depender de objetos ausentes disponíveis offline ou presumir todo servidor respeita filtros.

**Sintaxe**

`git clone --no-local --filter=blob:none --no-checkout origin.git partial-lab`

**Exemplo básico**

`git clone --no-local --filter=blob:none --no-checkout origin.git partial-lab`

De diretório pai descartável, clone origem bare local própria configurada para permitir filtro.

**Exemplo profissional**

`git clone --no-local --filter=blob:none origin.git review-lab`

Clone origem própria capaz de filtro; checkout pode buscar blobs necessários imediatamente.

**Impacto no estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / histórico: Condicional
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** Cria clone parcial local com configuração promisor quando suportado; objetos ausentes necessários podem ser buscados depois.

**Impactos e efeitos colaterais:** Cria repositório local e pode materializar arquivos e buscar blobs; não altera referências de origem.

**Erros comuns:** Confundir --filter com --depth ou tratar sucesso do clone como prova de aplicação do filtro.

**Alternativas:** Use clone completo para acesso offline confiável a objetos; use sparse-checkout para seleção de working tree.

**Recuperação:** Inspecione avisos de clone e configuração promisor; se filtro não for suportado, use destino novo limpo com clone completo ou origem compatível verificada.

**Versão e dependências:** Use Git 2.40 ou superior nos laboratórios do guia; verifique disponibilidade na ajuda local Git.

**Capítulos relacionados**

- [advanced-git/08-partial-and-shallow-clone](../../advanced-git/08-partial-and-shallow-clone/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-clone>

## git-archive

**`git archive`**

**Tipo:** Comando nativo

**Nível:** Avançado

**Pesquisar por intenção:** Empacotar histórico ou arquivos

**Risco:** Alteração de estado. Revise caminhos, referências e configuração local antes. Preserve trabalho valioso; nunca teste contra o guia ou serviço compartilhado.

**Finalidade:** Exportar conteúdo de árvore registrada selecionada como arquivo sem histórico Git.

**Pré-requisitos:** Use repositório próprio descartável limpo com trabalho salvo, caminhos locais e referências verificados e configuração confiável. Use só origens locais próprias.

**Opções:** --format seleciona formato; --output nomeia saída; --prefix adiciona prefixo aos caminhos; atributos export-ignore podem omitir caminhos.

**Quando utilizar:** Ao preparar snapshot de código revisado para distribuição ou inspeção.

**Quando evitar:** Evite sobrescrever artefatos existentes, exportar segredos ou presumir conteúdo de submódulo incluído recursivamente.

**Sintaxe**

`git archive --format=tar --output=../snapshot.tar HEAD`

**Exemplo básico**

`git archive --format=tar --output=../snapshot.tar HEAD`

Grave arquivo da árvore registrada verificada em arquivo vizinho livre.

**Exemplo profissional**

`git archive --format=zip --prefix=release/ --output=../release.zip v1.0.0`

Empacote tag de versão existente verificada em ZIP local novo.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Altera

**Resultado esperado:** Cria arquivo da árvore selecionada com atributos de exportação aplicáveis; edições não registradas e metadados Git não são incluídos.

**Impactos e efeitos colaterais:** Grava arquivo externo nomeado; operação mostrada não altera referências, index ou arquivos rastreados.

**Erros comuns:** Tratar arquivo como backup de repositório ou presumir inclusão de edições do working tree.

**Alternativas:** Use git bundle para transferir referências selecionadas e histórico de commits.

**Recuperação:** Verifique conteúdo do arquivo e destino; recrie com nome novo se necessário. Não exclua arquivos alheios.

**Versão e dependências:** Use Git 2.40 ou superior nos laboratórios do guia; verifique disponibilidade na ajuda local Git.

**Capítulos relacionados**

- [advanced-git/10-archive-and-bundle](../../advanced-git/10-archive-and-bundle/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-archive>

## git-bundle-create

**`git bundle create`**

**Tipo:** Subcomando

**Nível:** Avançado

**Pesquisar por intenção:** Empacotar histórico ou arquivos, Recuperar trabalho

**Risco:** Alteração de estado. Revise caminhos, referências e configuração local antes. Preserve trabalho valioso; nunca teste contra o guia ou serviço compartilhado.

**Finalidade:** Empacotar referências Git selecionadas e objetos alcançáveis para transporte offline.

**Pré-requisitos:** Use repositório próprio descartável limpo com trabalho salvo, caminhos locais e referências verificados e configuração confiável. Use só origens locais próprias.

**Opções:** --all seleciona referências amplamente; intervalos podem criar bundles incrementais exigindo objetos pré-requisitos; git bundle verify confere aplicabilidade.

**Quando utilizar:** Ao transferir histórico registrado selecionado sem conexão remota ativa.

**Quando evitar:** Evite empacotar histórico privado não revisado ou tratar como backup completo de configuração e trabalho não registrado.

**Sintaxe**

`git bundle create ../main.bundle main`

**Exemplo básico**

`git bundle create ../main.bundle main`

Crie bundle da referência main local verificada em caminho livre.

**Exemplo profissional**

`git bundle create ../transfer.bundle --all`

Após revisar toda referência selecionada e histórico quanto a conteúdo sensível, crie bundle local de transferência.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Altera

**Resultado esperado:** Cria bundle com referências anunciadas selecionadas e dados de objetos necessários; formas incrementais podem exigir objetos base existentes.

**Impactos e efeitos colaterais:** Grava artefato de saída fora do checkout; criação mostrada não atualiza referências atuais ou remoto.

**Erros comuns:** Presumir --all captura arquivos não rastreados, reflogs, hooks e metadados da plataforma.

**Alternativas:** Use archive para snapshot de código; use backup separado verificado para todos dados de repositório e trabalho.

**Recuperação:** Execute git bundle verify e inspecione referências anunciadas; teste clone ou fetch em destino descartável antes de depender do artefato.

**Versão e dependências:** Use Git 2.40 ou superior nos laboratórios do guia; verifique disponibilidade na ajuda local Git.

**Capítulos relacionados**

- [advanced-git/10-archive-and-bundle](../../advanced-git/10-archive-and-bundle/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-bundle>


---

<!-- navigation-footer -->
[Anterior](../10-search-and-troubleshooting/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../12-internals-and-plumbing/README.pt-BR.md)
<!-- /navigation-footer -->
