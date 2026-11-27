# 02 Inspeção do repositório

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../01-setup-and-configuration/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../03-working-tree-and-staging/README.pt-BR.md)
<!-- /navigation -->

Gerado a partir do JSON canônico. Edite os registros, não esta página.

As entradas descrevem comandos e operações, não uma sequência a executar. Pratique em repositórios descartáveis. Operações hospedadas são opcionais.

**Total de entradas distintas: 9**

- [`git status`](#git-status)
- [`git status --porcelain`](#git-status-porcelain)
- [`git rev-parse --show-toplevel`](#git-rev-parse-show-toplevel)
- [`git rev-parse --git-dir`](#git-rev-parse-git-dir)
- [`git rev-parse --is-bare-repository`](#git-rev-parse-is-bare)
- [`git ls-files`](#git-ls-files)
- [`git check-ignore`](#git-check-ignore)
- [`git show-ref`](#git-show-ref)
- [`git count-objects`](#git-count-objects)

## git-status

**`git status`**

**Tipo:** Comando nativo

**Nível:** Iniciante

**Pesquisar por intenção:** Inspecionar estado do repositório

**Risco:** Alteração de estado. Inspecione o resultado em privado; nomes de arquivos, caminhos ou histórico podem revelar informações do projeto.

**Finalidade:** Resumir alterações no staging, fora dele e arquivos não rastreados.

**Pré-requisitos:** Use um repositório próprio descartável; execute no diretório de trabalho.

**Opções:** --short dá status compacto; --branch inclui informações da branch.

**Quando utilizar:** Antes de preparar, commitar ou trocar de branch.

**Quando evitar:** Não trate status limpo como prova de testes aprovados ou sincronização remota.

**Sintaxe**

`git status [--short]`

**Exemplo básico**

`git status`

Inspecione o relatório completo antes de preparar um arquivo alterado.

**Exemplo profissional**

`git status --short`

Revise um relatório compacto antes de entregar para code review.

**Impacto no estado**

- Working tree: Inalterado
- Index: Condicional
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Informa caminhos por estado; uma árvore limpa não tem alterações visíveis pendentes.

**Impactos e efeitos colaterais:** Pode atualizar metadados stat do index sem mudar conteúdo preparado; não altera commits.

**Erros comuns:** Interpretar mal as duas colunas do status curto; ignorados geralmente ficam ocultos.

**Alternativas:** Use git diff e git diff --cached para inspecionar alterações reais.

**Recuperação:** Não é necessário recuperar histórico; corrija o contexto e repita a inspeção.

**Versão e dependências:** Sem ferramenta opcional; os exemplos usam sintaxe tradicional do Git.

**Capítulos relacionados**

- [basic-commands/02-status-add-commit](../../basic-commands/02-status-add-commit/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-status>

## git-status-porcelain

**`git status --porcelain`**

**Tipo:** Uso de opção

**Nível:** Intermediário

**Pesquisar por intenção:** Automatizar fluxo

**Risco:** Alteração de estado. Inspecione o resultado em privado; nomes de arquivos, caminhos ou histórico podem revelar informações do projeto.

**Finalidade:** Inspecionar status da working tree e index em formato para máquinas.

**Pré-requisitos:** Use um repositório próprio descartável; execute no diretório de trabalho.

**Opções:** --porcelain=v1 seleciona formato v1 estável; -z usa terminadores NUL.

**Quando utilizar:** Quando scripts precisam de saída de status reproduzível.

**Quando evitar:** Não analise saída humana nem divida registros NUL por espaços.

**Sintaxe**

`git status --porcelain[=v1] [-z]`

**Exemplo básico**

`git status --porcelain=v1`

Compare o relatório v1 com git status normal.

**Exemplo profissional**

`git status --porcelain=v1 -z`

Capture registros NUL como bytes para verificação prévia; não os imprima como texto.

**Impacto no estado**

- Working tree: Inalterado
- Index: Condicional
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Emite status compacto legível por máquina; relatório vazio indica ausência de alterações relatadas.

**Impactos e efeitos colaterais:** Pode atualizar metadados stat do index; não prepara conteúdo nem move refs.

**Erros comuns:** Esperar código não zero para árvore suja; ignorar formato de renomeação.

**Alternativas:** Use git diff --quiet para comparação específica rastreada; não inclui não rastreados.

**Recuperação:** Não é necessário recuperar histórico; corrija o contexto e repita a inspeção.

**Versão e dependências:** Sem ferramenta opcional; os exemplos usam sintaxe tradicional do Git.

**Capítulos relacionados**

- [git-architecture/03-file-states](../../git-architecture/03-file-states/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-status>

## git-rev-parse-show-toplevel

**`git rev-parse --show-toplevel`**

**Tipo:** Uso de opção

**Nível:** Iniciante

**Pesquisar por intenção:** Inspecionar estado do repositório

**Risco:** Somente leitura. Inspecione o resultado em privado; nomes de arquivos, caminhos ou histórico podem revelar informações do projeto.

**Finalidade:** Encontrar a raiz da working tree atual.

**Pré-requisitos:** Use um repositório próprio descartável; execute no diretório de trabalho.

**Opções:** --show-toplevel informa o caminho raiz; -C muda o diretório inicial do comando.

**Quando utilizar:** Antes de operar em repositório a partir de subdiretório.

**Quando evitar:** Não use para localizar working tree em repositório bare.

**Sintaxe**

`git rev-parse --show-toplevel`

**Exemplo básico**

`git rev-parse --show-toplevel`

Confirme a raiz antes de inspecionar arquivos.

**Exemplo profissional**

`git -C src rev-parse --show-toplevel`

Se src existir, confirme qual repositório uma ferramenta ali acessaria.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Imprime o caminho raiz ou falha quando indisponível.

**Impactos e efeitos colaterais:** Lê informações de descoberta sem alterar refs ou arquivos.

**Erros comuns:** Presumir que o diretório atual do shell é sempre a raiz.

**Alternativas:** Use git rev-parse --git-dir para localizar metadados Git.

**Recuperação:** Não é necessário recuperar histórico; corrija o contexto e repita a inspeção.

**Versão e dependências:** Sem ferramenta opcional; os exemplos usam sintaxe tradicional do Git.

**Capítulos relacionados**

- [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-rev-parse>

## git-rev-parse-git-dir

**`git rev-parse --git-dir`**

**Tipo:** Uso de opção

**Nível:** Intermediário

**Pesquisar por intenção:** Inspecionar estado do repositório

**Risco:** Somente leitura. Inspecione o resultado em privado; nomes de arquivos, caminhos ou histórico podem revelar informações do projeto.

**Finalidade:** Localizar metadados sem presumir que .git é diretório.

**Pré-requisitos:** Use um repositório próprio descartável; execute no diretório de trabalho.

**Opções:** --git-dir pode informar caminho relativo; --absolute-git-dir solicita caminho absoluto.

**Quando utilizar:** Diagnosticar worktrees, submódulos ou repositórios bare.

**Quando evitar:** Não edite metadados diretamente com base nesse resultado.

**Sintaxe**

`git rev-parse --git-dir`

**Exemplo básico**

`git rev-parse --git-dir`

Inspecione o caminho de metadados em clone normal.

**Exemplo profissional**

`git rev-parse --absolute-git-dir`

Confira caminho absoluto dos metadados ao diagnosticar worktree vinculado.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Informa o diretório Git deste contexto.

**Impactos e efeitos colaterais:** Lê localização dos metadados; sem alteração de estado.

**Erros comuns:** Confundir diretório Git por worktree com o diretório comum compartilhado.

**Alternativas:** Use git rev-parse --git-common-dir para inspecionar localização compartilhada.

**Recuperação:** Não é necessário recuperar histórico; corrija o contexto e repita a inspeção.

**Versão e dependências:** Sem ferramenta opcional; os exemplos usam sintaxe tradicional do Git.

**Capítulos relacionados**

- [git-internals/01-object-database](../../git-internals/01-object-database/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-rev-parse>

## git-rev-parse-is-bare

**`git rev-parse --is-bare-repository`**

**Tipo:** Uso de opção

**Nível:** Intermediário

**Pesquisar por intenção:** Inspecionar estado do repositório

**Risco:** Somente leitura. Inspecione o resultado em privado; nomes de arquivos, caminhos ou histórico podem revelar informações do projeto.

**Finalidade:** Determinar se Git considera o repositório bare.

**Pré-requisitos:** Use um repositório próprio descartável; execute no diretório de trabalho.

**Opções:** --is-bare-repository imprime booleano; -C seleciona diretório.

**Quando utilizar:** Antes de tentar comandos de working tree em origin local.

**Quando evitar:** Não deduza permissão de escrita ou acesso remoto a partir do resultado bare.

**Sintaxe**

`git rev-parse --is-bare-repository`

**Exemplo básico**

`git rev-parse --is-bare-repository`

Confira repositório normal; espere false.

**Exemplo profissional**

`git -C origin.git rev-parse --is-bare-repository`

Em pai descartável com origin.git, confirme que o origin é bare.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Imprime true ou false para contexto válido.

**Impactos e efeitos colaterais:** Não altera configuração nem conteúdo do repositório.

**Erros comuns:** Tratar false como prova de que o diretório atual é a raiz.

**Alternativas:** Use git rev-parse --is-inside-work-tree para testar contexto de working tree.

**Recuperação:** Não é necessário recuperar histórico; corrija o contexto e repita a inspeção.

**Versão e dependências:** Sem ferramenta opcional; os exemplos usam sintaxe tradicional do Git.

**Capítulos relacionados**

- [remote-repositories/01-remote-concepts](../../remote-repositories/01-remote-concepts/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-rev-parse>

## git-ls-files

**`git ls-files`**

**Tipo:** Comando nativo

**Nível:** Intermediário

**Pesquisar por intenção:** Inspecionar arquivos

**Risco:** Somente leitura. Inspecione o resultado em privado; nomes de arquivos, caminhos ou histórico podem revelar informações do projeto.

**Finalidade:** Listar caminhos indexados ou outros caminhos selecionados da working tree.

**Pré-requisitos:** Use um repositório próprio descartável; execute no diretório de trabalho.

**Opções:** --stage mostra entradas do index; --others lista não rastreados; --exclude-standard aplica regras comuns de ignore.

**Quando utilizar:** Auditar caminhos rastreados ou identificar candidatos não rastreados sem preparar.

**Quando evitar:** Não interprete caminhos do index como prova de que arquivos de trabalho existem.

**Sintaxe**

`git ls-files [--stage] [--others --exclude-standard]`

**Exemplo básico**

`git ls-files`

Liste caminhos indexados após preparar um arquivo.

**Exemplo profissional**

`git ls-files --others --exclude-standard`

Inspecione caminhos não rastreados e não ignorados antes de empacotar arquivos.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Lista caminhos do modo selecionado; padrão lista caminhos rastreados do index.

**Impactos e efeitos colaterais:** Lê index e possivelmente working tree sem preparar alterações.

**Erros comuns:** Esperar arquivos ignorados numa lista com --exclude-standard.

**Alternativas:** Use git status para visão geral e git ls-tree para árvore commitada.

**Recuperação:** Não é necessário recuperar histórico; corrija o contexto e repita a inspeção.

**Versão e dependências:** Sem ferramenta opcional; os exemplos usam sintaxe tradicional do Git.

**Capítulos relacionados**

- [git-architecture/03-file-states](../../git-architecture/03-file-states/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-ls-files>

## git-check-ignore

**`git check-ignore`**

**Tipo:** Comando nativo

**Nível:** Intermediário

**Pesquisar por intenção:** Ignorar arquivos

**Risco:** Somente leitura. Inspecione o resultado em privado; nomes de arquivos, caminhos ou histórico podem revelar informações do projeto.

**Finalidade:** Explicar se caminho corresponde a regras de ignore e qual regra se aplica.

**Pré-requisitos:** Use um repositório próprio descartável; execute no diretório de trabalho.

**Opções:** -v informa origem e padrão; --no-index ignora a verificação usual de caminho rastreado.

**Quando utilizar:** Diagnosticar caminho inesperadamente ausente do status de não rastreados.

**Quando evitar:** Não presuma que caminho ignorado está protegido contra acesso ou removido do histórico.

**Sintaxe**

`git check-ignore [-v] [--no-index] pathname`

**Exemplo básico**

`git check-ignore notes.tmp`

Crie regra descartável para notes.tmp e confira correspondência.

**Exemplo profissional**

`git check-ignore -v build/output.log`

Explique qual padrão de ignore exclui um log de build ilustrativo.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Informa caminhos ignorados correspondentes; código de saída distingue correspondência, ausência e erros.

**Impactos e efeitos colaterais:** Lê regras de ignore e index sem alterar conteúdo rastreado.

**Erros comuns:** Esperar que check-ignore comum informe caminhos já rastreados.

**Alternativas:** Use git status --ignored para inspecionar caminhos ignorados em geral.

**Recuperação:** Não é necessário recuperar histórico; corrija o contexto e repita a inspeção.

**Versão e dependências:** Sem ferramenta opcional; os exemplos usam sintaxe tradicional do Git.

**Capítulos relacionados**

- [basic-commands/05-ignore-and-review](../../basic-commands/05-ignore-and-review/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-check-ignore>

## git-show-ref

**`git show-ref`**

**Tipo:** Comando nativo

**Nível:** Intermediário

**Pesquisar por intenção:** Inspecionar referências

**Risco:** Somente leitura. Inspecione o resultado em privado; nomes de arquivos, caminhos ou histórico podem revelar informações do projeto.

**Finalidade:** Inspecionar referências locais e IDs de objetos.

**Pré-requisitos:** Use um repositório próprio descartável; execute no diretório de trabalho.

**Opções:** --heads limita a refs de branches; --tags limita tags; --verify exige caminho exato.

**Quando utilizar:** Verificar referência antes de operação dependente dela.

**Quando evitar:** Não interprete refs de rastreamento remoto locais como estado remoto ao vivo.

**Sintaxe**

`git show-ref [--heads] [--tags]`

**Exemplo básico**

`git show-ref --heads`

Liste refs locais após o primeiro commit.

**Exemplo profissional**

`git show-ref --verify refs/heads/main`

Verifique ref exata main em repositório de integração descartável.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Imprime IDs e nomes correspondentes; verificação falha se ref exata não existe.

**Impactos e efeitos colaterais:** Lê refs sem criá-las ou movê-las.

**Erros comuns:** Usar nome curto com --verify ou verificar branch sem commit.

**Alternativas:** Use git for-each-ref para formato personalizado ou git ls-remote para refs remotas.

**Recuperação:** Não é necessário recuperar histórico; corrija o contexto e repita a inspeção.

**Versão e dependências:** Sem ferramenta opcional; os exemplos usam sintaxe tradicional do Git.

**Capítulos relacionados**

- [git-internals/05-refs-and-head](../../git-internals/05-refs-and-head/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-show-ref>

## git-count-objects

**`git count-objects`**

**Tipo:** Comando nativo

**Nível:** Avançado

**Pesquisar por intenção:** Inspecionar objetos Git

**Risco:** Somente leitura. Inspecione o resultado em privado; nomes de arquivos, caminhos ou histórico podem revelar informações do projeto.

**Finalidade:** Medir quantidade de objetos soltos e estatísticas de armazenamento.

**Pré-requisitos:** Use um repositório próprio descartável; execute no diretório de trabalho.

**Opções:** -v inclui estatísticas de packs e lixo; -H mostra tamanhos legíveis.

**Quando utilizar:** Diagnosticar crescimento do banco de objetos antes de considerar manutenção.

**Quando evitar:** Não trate contagens como prova de corrupção ou uso exato de disco do repositório inteiro.

**Sintaxe**

`git count-objects [-v] [-H]`

**Exemplo básico**

`git count-objects`

Inspecione contagens após alguns commits locais.

**Exemplo profissional**

`git count-objects -vH`

Registre estatísticas detalhadas antes de propor manutenção em clone descartável.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Informa objetos soltos e tamanhos; saída detalhada inclui estatísticas de packs.

**Impactos e efeitos colaterais:** Lê armazenamento de objetos sem podar nem reempacotar.

**Erros comuns:** Confundir quantidade de objetos soltos com total de commits.

**Alternativas:** Use git fsck para diagnóstico de integridade e ferramentas do sistema para uso total de disco.

**Recuperação:** Não é necessário recuperar histórico; corrija o contexto e repita a inspeção.

**Versão e dependências:** Sem ferramenta opcional; os exemplos usam sintaxe tradicional do Git.

**Capítulos relacionados**

- [git-internals/07-loose-objects-and-packfiles](../../git-internals/07-loose-objects-and-packfiles/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-count-objects>


---

<!-- navigation-footer -->
[Anterior](../01-setup-and-configuration/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../03-working-tree-and-staging/README.pt-BR.md)
<!-- /navigation-footer -->
