# 01 Inicialização e configuração

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Módulo anterior](../../git-internals/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../02-repository-inspection/README.pt-BR.md)
<!-- /navigation -->

Gerado a partir do JSON canônico. Edite os registros, não esta página.

As entradas descrevem comandos e operações, não uma sequência a executar. Pratique em repositórios descartáveis. Operações hospedadas são opcionais.

**Total de entradas distintas: 8**

- [`git --version`](#git-version)
- [`git help`](#git-help)
- [`git init`](#git-init)
- [`git init --bare`](#git-init-bare)
- [`git config --local`](#git-config-local)
- [`git config --global`](#git-config-global)
- [`git config --list --show-origin`](#git-config-show-origin)
- [`git config --get`](#git-config-get)

## git-version

**`git --version`**

**Tipo:** Uso de opção

**Nível:** Iniciante

**Pesquisar por intenção:** Verificar versão do Git, Configurar Git

**Risco:** Somente leitura. Não altera o repositório; a versão sozinha não garante comportamento.

**Finalidade:** Identificar o executável Git instalado e a versão informada.

**Pré-requisitos:** Git instalado e acessível no shell atual.

**Opções:** --version informa a versão; não atualiza o Git.

**Quando utilizar:** Verificar compatibilidade antes de seguir instruções ou relatar um erro.

**Quando evitar:** Não considerar a versão como prova de instalação de uma extensão opcional.

**Sintaxe**

`git --version`

**Exemplo básico**

`git --version`

Execute em um terminal novo e anote a versão.

**Exemplo profissional**

`git --version`

Registre a versão do Git do runner em um relatório de diagnóstico de CI sem presumir que todos sejam iguais.

**Impacto no estado**

- Working tree: Não se aplica
- Index: Não se aplica
- Objetos / refs / histórico: Não se aplica
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Exibe uma versão; não exige repositório.

**Impactos e efeitos colaterais:** Lê informações do executável sem alterar o estado do Git.

**Erros comuns:** Executável ausente ou PATH incorreto impede a execução; instalações múltiplas podem resolver de modo diferente.

**Alternativas:** Use o mecanismo do sistema operacional para identificar o binário Git selecionado.

**Recuperação:** Não há recuperação de repositório; corrija a instalação ou o PATH se necessário.

**Versão e dependências:** Sem dependência opcional; compare a versão informada com o mínimo documentado da funcionalidade.

**Capítulos relacionados**

- [getting-started/01-install-git](../../getting-started/01-install-git/README.pt-BR.md)
- [getting-started/02-terminal-and-help](../../getting-started/02-terminal-and-help/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git>

## git-help

**`git help`**

**Tipo:** Comando nativo

**Nível:** Iniciante

**Pesquisar por intenção:** Encontrar ajuda, Verificar versão do Git

**Risco:** Somente leitura. O visualizador pode iniciar um processo ou abrir um navegador; os dados do Git não são alterados.

**Finalidade:** Abrir a ajuda de um comando Git ou listar comandos disponíveis.

**Pré-requisitos:** Git instalado; a ajuda detalhada exige um visualizador de documentação disponível.

**Opções:** -a lista comandos disponíveis; -w solicita ajuda em formato web.

**Quando utilizar:** Conferir sintaxe e comportamento documentado de uma operação desconhecida.

**Quando evitar:** Não confundir a ajuda instalada localmente com a documentação de outra versão do Git.

**Sintaxe**

`git help [command]`

**Exemplo básico**

`git help status`

Leia o manual de status antes de interpretar sua saída.

**Exemplo profissional**

`git help -a`

Liste comandos em uma nova estação de desenvolvimento para descobrir extensões instaladas.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Exibe documentação ou uma lista de comandos.

**Impactos e efeitos colaterais:** Não altera o repositório; o visualizador ou navegador selecionado pode iniciar um processo.

**Erros comuns:** A falta de visualizador de manuais ou arquivos de documentação pode impedir a abertura da página completa.

**Alternativas:** Use git COMMAND -h para sintaxe resumida ou o manual oficial versionado online.

**Recuperação:** Feche o visualizador; use a ajuda resumida ou o manual oficial se indisponível.

**Versão e dependências:** A disponibilidade do visualizador depende da instalação e do sistema operacional.

**Capítulos relacionados**

- [getting-started/02-terminal-and-help](../../getting-started/02-terminal-and-help/README.pt-BR.md)
- [basic-commands/01-init-config-help](../../basic-commands/01-init-config-help/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-help>

## git-init

**`git init`**

**Tipo:** Comando nativo

**Nível:** Iniciante

**Pesquisar por intenção:** Criar repositório, Configurar Git

**Risco:** Alteração de estado. Cria metadados do repositório; confira o destino primeiro.

**Finalidade:** Criar um repositório Git local ou reinicializar um existente.

**Pré-requisitos:** Diretório próprio com permissão de escrita ou diretório pai gravável para um novo.

**Opções:** -b seleciona o nome da branch inicial; o diretório opcional seleciona o destino.

**Quando utilizar:** Começar a versionar um projeto local novo sem remoto.

**Quando evitar:** Não inicialize o diretório errado nem crie um repositório aninhado involuntariamente.

**Sintaxe**

`git init [-b branch] [directory]`

**Exemplo básico**

`git init -b main notes-lab`

Em um diretório pai próprio e descartável, crie um repositório de notas na main.

**Exemplo profissional**

`git init -b main prototype-lab`

Crie um repositório separado para um protótipo em vez de inicializar por engano o diretório de uma aplicação existente.

**Impacto no estado**

- Working tree: Condicional
- Index: Inalterado
- Objetos / refs / histórico: Altera
- Repositório remoto: Inalterado
- Outros estados: Altera

**Resultado esperado:** Em um repositório novo, os metadados existem e HEAD aponta simbolicamente para uma branch ainda sem commit; nenhum commit é criado.

**Impactos e efeitos colaterais:** Pode criar diretório e metadados; arquivos não entram no staging automaticamente.

**Erros comuns:** Inicializar um diretório pai ou aninhado por engano confunde os limites do repositório.

**Alternativas:** Use git clone quando precisar de um repositório existente e seu histórico.

**Recuperação:** Inspecione o caminho e faça backup; não remova metadados sem verificar que o repositório é descartável e o histórico é desnecessário.

**Versão e dependências:** -b / --initial-branch requer Git 2.28 ou posterior.

**Capítulos relacionados**

- [getting-started/03-first-repository](../../getting-started/03-first-repository/README.pt-BR.md)
- [basic-commands/01-init-config-help](../../basic-commands/01-init-config-help/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-init>
- <https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup>

## git-init-bare

**`git init --bare`**

**Tipo:** Uso de opção

**Nível:** Intermediário

**Pesquisar por intenção:** Criar repositório, Simular colaboração

**Risco:** Alteração de estado. Um origin bare pode conter histórico valioso; nunca o exclua apenas porque não há arquivos em checkout.

**Finalidade:** Inicializar um repositório sem working tree de checkout, adequado como origin compartilhado local.

**Pré-requisitos:** Destino descartável e gravável; escolha deliberadamente a branch inicial.

**Opções:** --bare cria o layout de metadados bare; -b escolhe a branch inicial.

**Quando utilizar:** Criar um origin local para um exercício de colaboração com dois clones.

**Quando evitar:** Não use como repositório normal onde pretende editar e colocar arquivos no staging.

**Sintaxe**

`git init --bare [-b branch] [directory]`

**Exemplo básico**

`git init --bare -b main origin.git`

Crie um origin bare local em um diretório pai descartável.

**Exemplo profissional**

`git init --bare -b main collaboration.git`

Use um origin bare local para ensaiar push e fetch com dois clones separados sem conta de hospedagem.

**Impacto no estado**

- Working tree: Não se aplica
- Index: Não se aplica
- Objetos / refs / histórico: Altera
- Repositório remoto: Inalterado
- Outros estados: Altera

**Resultado esperado:** O repositório bare existe; HEAD é simbólico e inicialmente não há commit.

**Impactos e efeitos colaterais:** Não cria working tree nem fluxo comum de staging; refs e objetos ficam no diretório do repositório.

**Erros comuns:** Comandos de working tree em repositório bare falham ou não fazem sentido.

**Alternativas:** Use git init comum para editar; clone o origin bare para trabalhar nos arquivos.

**Recuperação:** Proteja refs e objetos existentes; remova apenas um origin descartável verificado após todos terminarem.

**Versão e dependências:** -b requer Git 2.28 ou posterior; sem serviço hospedado.

**Capítulos relacionados**

- [remote-repositories/01-remote-concepts](../../remote-repositories/01-remote-concepts/README.pt-BR.md)
- [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-init>
- <https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup>

## git-config-local

**`git config --local`**

**Tipo:** Uso de opção

**Nível:** Iniciante

**Pesquisar por intenção:** Configurar Git, Configurar identidade

**Risco:** Alteração de estado. Configuração pode afetar commits futuros ou comportamento de execução; use identidade fictícia apenas nos labs.

**Finalidade:** Definir um valor de configuração local do repositório, como identidade de commit.

**Pré-requisitos:** Repositório próprio e motivo claro para a configuração; inspecione valores existentes primeiro.

**Opções:** --local seleciona a configuração do repositório; --get lê um valor; --unset remove uma chave de valor único.

**Quando utilizar:** Definir identidade ou comportamento específico do projeto sem alterar outros repositórios.

**Quando evitar:** Não armazene tokens de acesso ou chaves privadas em valores comuns de configuração.

**Sintaxe**

`git config --local name value`

**Exemplo básico**

`git config --local user.name "Alice Example"`

Em um repositório descartável, defina um nome de autor fictício.

**Exemplo profissional**

`git config --local user.email alice@example.invalid`

Defina um e-mail fictício em um projeto descartável para separar sua identidade de commit da identidade normal da estação.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Altera

**Resultado esperado:** A chave especificada tem o valor local solicitado; operações futuras podem utilizá-lo.

**Impactos e efeitos colaterais:** Altera configuração, não commits existentes nem arquivos no staging; identidade vale para commits futuros.

**Erros comuns:** Usar --global por engano afeta outros repositórios; sem repositório, --local não funciona.

**Alternativas:** Use git -c para sobrescrita pontual ou --global para um padrão intencional do usuário.

**Recuperação:** Restaure o valor local anterior ou remova a chave apenas se antes estava ausente; confira a configuração efetiva depois.

**Versão e dependências:** Sem dependência opcional; exemplos usam a forma tradicional nome/valor.

**Capítulos relacionados**

- [getting-started/03-first-repository](../../getting-started/03-first-repository/README.pt-BR.md)
- [basic-commands/01-init-config-help](../../basic-commands/01-init-config-help/README.pt-BR.md)
- [security/09-commit-and-tag-signing](../../security/09-commit-and-tag-signing/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-config>

## git-config-global

**`git config --global`**

**Tipo:** Uso de opção

**Nível:** Iniciante

**Pesquisar por intenção:** Configurar Git, Configurar identidade

**Risco:** Alteração de estado. Alteração ampla do usuário; o exemplo de escrita é apenas para home descartável isolado.

**Finalidade:** Ler ou definir configuração Git do usuário compartilhada entre repositórios.

**Pré-requisitos:** Conta sob seu controle; para praticar escrita, isole primeiro o home/caminho de configuração.

**Opções:** --global seleciona o escopo do usuário; --get lê em vez de escrever; --unset remove chave de valor único.

**Quando utilizar:** Inspecionar padrões do usuário ou definir intencionalmente uma preferência geral.

**Quando evitar:** Evite gravar identidade fictícia do lab na configuração global normal ou alterar uma máquina gerenciada/compartilhada.

**Sintaxe**

`git config --global name value`

**Exemplo básico**

`git config --global --get user.name`

Inspecione o nome de autor global sem alterar; ausência pode retornar código não zero.

**Exemplo profissional**

`git config --global user.name "Alice Example"`

Somente em home/config de lab isolado separadamente, defina identidade fictícia geral para comparar com uma sobrescrita local.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** A leitura informa o valor se presente; a escrita atualiza a configuração do usuário, sujeita a sobrescritas de maior precedência.

**Impactos e efeitos colaterais:** Pode afetar operações futuras em vários repositórios; objetos de commits existentes não mudam.

**Erros comuns:** Confundir escopo global com sobrescrita específica de repositório pode gerar identidade ou comportamento inesperado.

**Alternativas:** Use git config --local para configurações do projeto ou git -c para uma execução.

**Recuperação:** Registre o valor anterior antes de alterar; restaure-o ou remova apenas chave recém-criada. Confira escopo e valor efetivo.

**Versão e dependências:** Sem dependência opcional; a localização do arquivo global depende do Git e da configuração do ambiente.

**Capítulos relacionados**

- [getting-started/03-first-repository](../../getting-started/03-first-repository/README.pt-BR.md)
- [basic-commands/01-init-config-help](../../basic-commands/01-init-config-help/README.pt-BR.md)
- [security/05-secrets-and-disclosure-prevention](../../security/05-secrets-and-disclosure-prevention/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-config>

## git-config-show-origin

**`git config --list --show-origin`**

**Tipo:** Uso de opção

**Nível:** Intermediário

**Pesquisar por intenção:** Inspecionar configuração, Diagnosticar configuração

**Risco:** Sensível. Saída sensível; revise e remova dados sensíveis antes de compartilhar.

**Finalidade:** Inspecionar entradas de configuração junto com sua origem.

**Pré-requisitos:** Git instalado; execute dentro de um repositório para incluir configurações locais relevantes.

**Opções:** --list enumera entradas; --show-origin informa a origem; --show-scope acrescenta o escopo.

**Quando utilizar:** Diagnosticar conflitos entre configurações do usuário e repositório antes de alterar algo.

**Quando evitar:** Não cole a listagem bruta em issues ou logs públicos; valores e caminhos podem ser sensíveis.

**Sintaxe**

`git config --list --show-origin [--show-scope]`

**Exemplo básico**

`git config --list --show-origin`

Inspecione origens das configurações em privado num repositório descartável.

**Exemplo profissional**

`git config --list --show-origin --show-scope`

Diagnostique qual escopo fornece uma identidade inesperada sem expor a listagem completa em um chamado.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Imprime entradas com origem e, opcionalmente, escopo; chaves repetidas podem aparecer.

**Impactos e efeitos colaterais:** Não altera dados Git, mas a saída pode expor caminhos pessoais, identidade ou configuração sensível.

**Erros comuns:** Presumir que o primeiro valor impresso sempre prevalece ignora precedência e configurações multivaloradas.

**Alternativas:** Use git config --get para uma chave ou restrinja com --local ou --global.

**Recuperação:** Não exige recuperação Git; se segredos foram divulgados, siga o procedimento de incidente de credenciais.

**Versão e dependências:** --show-origin disponível desde Git 2.8; --show-scope desde Git 2.26.

**Capítulos relacionados**

- [basic-commands/01-init-config-help](../../basic-commands/01-init-config-help/README.pt-BR.md)
- [security/05-secrets-and-disclosure-prevention](../../security/05-secrets-and-disclosure-prevention/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-config>
- <https://git-scm.com/docs/git-config/2.8.6>
- <https://git-scm.com/docs/git-config/2.26.0>

## git-config-get

**`git config --get`**

**Tipo:** Uso de opção

**Nível:** Iniciante

**Pesquisar por intenção:** Inspecionar configuração, Configurar identidade

**Risco:** Sensível. Consulta específica reduz divulgação em relação à lista completa, mas ainda revise a saída.

**Finalidade:** Consultar uma chave de configuração Git específica sem modificá-la.

**Pré-requisitos:** Git instalado; --local exige repositório.

**Opções:** --get lê um valor; --get-all obtém múltiplos valores; opções de escopo restringem a consulta.

**Quando utilizar:** Conferir identidade efetiva ou inspecionar uma chave antes de alterá-la.

**Quando evitar:** Não consulte nem compartilhe valores de configuração sensíveis sem necessidade.

**Sintaxe**

`git config [--local|--global] --get name`

**Exemplo básico**

`git config --get user.name`

Leia o nome de autor efetivo num repositório descartável.

**Exemplo profissional**

`git config --local --get user.email`

Confira se um projeto tem e-mail de autor local antes do primeiro commit; não publique o endereço real.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Imprime um valor se encontrado; chave ausente produz código de saída não zero.

**Impactos e efeitos colaterais:** Não altera o repositório; valores consultados podem conter dados pessoais ou sensíveis.

**Erros comuns:** Presumir que chave ausente é um valor vazio configurado ou tratar código não zero como falha sem relação.

**Alternativas:** Use --get-all para chaves multivaloradas ou --list --show-origin para investigar a origem.

**Recuperação:** Não há recuperação do repositório; confira a grafia da chave e o escopo se não encontrada.

**Versão e dependências:** Sem dependência opcional; use a sintaxe tradicional --get para ampla compatibilidade Git.

**Capítulos relacionados**

- [basic-commands/01-init-config-help](../../basic-commands/01-init-config-help/README.pt-BR.md)
- [remote-repositories/05-secure-authentication](../../remote-repositories/05-secure-authentication/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-config>


---

<!-- navigation-footer -->
[Módulo anterior](../../git-internals/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../02-repository-inspection/README.pt-BR.md)
<!-- /navigation-footer -->
