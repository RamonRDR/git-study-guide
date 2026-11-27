# 12 Internals e plumbing

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../11-advanced-git-operations/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../13-security-and-maintenance/README.pt-BR.md)
<!-- /navigation -->

Gerado a partir do JSON canônico. Edite os registros, não esta página.

As entradas descrevem comandos e operações, não uma sequência a executar. Pratique em repositórios descartáveis. Operações hospedadas são opcionais.

**Total de entradas distintas: 8**

- [`git cat-file -t`](#git-cat-file-type)
- [`git cat-file -p`](#git-cat-file-pretty)
- [`git hash-object`](#git-hash-object)
- [`git ls-tree`](#git-ls-tree)
- [`git rev-list`](#git-rev-list)
- [`git symbolic-ref HEAD`](#git-symbolic-ref-read)
- [`git for-each-ref`](#git-for-each-ref)
- [`git ls-files --stage`](#git-ls-files-stage)

## git-cat-file-type

**`git cat-file -t`**

**Tipo:** Uso de opção

**Nível:** Avançado

**Pesquisar por intenção:** Inspecionar objetos Git

**Risco:** Somente leitura. Somente leitura nas formas mostradas em repositório local completo; não divulgue caminhos, conteúdo de objetos ou metadados sensíveis.

**Finalidade:** Identificar tipo de objeto Git existente.

**Pré-requisitos:** Use repositório próprio descartável com objetos indicados existentes e configuração local confiável. Confira repositório antes dos comandos.

**Opções:** -t exibe tipo do objeto; -s relata tamanho; use nome de objeto resolvível.

**Quando utilizar:** Ao distinguir blobs, trees, commits e objetos de tags anotadas antes de inspecionar.

**Quando evitar:** Não use ID de objeto ambíguo ou presumido, nem espere que tipo prove integridade do conteúdo.

**Sintaxe**

`git cat-file -t HEAD`

**Exemplo básico**

`git cat-file -t HEAD`

Identifique tipo do objeto nomeado por HEAD.

**Exemplo profissional**

`git cat-file -t HEAD:notes.txt`

Identifique blob de arquivo comum existente no commit.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Exibe tipo do objeto, como commit, tree, blob ou tag, ou relata falha de resolução.

**Impactos e efeitos colaterais:** No laboratório local completo, inspeção mostrada não grava objetos, altera referências, edita arquivos nem atualiza index. Clones parciais podem buscar objetos ausentes.

**Erros comuns:** Presumir que todo nome de tag aponta para objeto tag; tags leves nomeiam outros objetos diretamente.

**Alternativas:** Use git cat-file -p para inspecionar conteúdo do objeto resolvido, ou git fsck para checagem de integridade.

**Recuperação:** Não é necessário desfazer inspeção mostrada. Se saída inesperada, verifique objeto, referência, intervalo de revisões ou caminho e inspecione erros antes de prosseguir.

**Versão e dependências:** Sintaxe padrão Git; use Git 2.40 ou superior nos laboratórios. IDs de objetos dependem do formato de objetos do repositório.

**Capítulos relacionados**

- [git-internals/01-object-database](../../git-internals/01-object-database/README.pt-BR.md)
- [git-internals/10-porcelain-and-plumbing](../../git-internals/10-porcelain-and-plumbing/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-cat-file>

## git-cat-file-pretty

**`git cat-file -p`**

**Tipo:** Uso de opção

**Nível:** Avançado

**Pesquisar por intenção:** Inspecionar objetos Git, Inspecionar histórico

**Risco:** Somente leitura. Somente leitura nas formas mostradas em repositório local completo; não divulgue caminhos, conteúdo de objetos ou metadados sensíveis.

**Finalidade:** Exibir conteúdo de objeto em forma adequada ao seu tipo.

**Pré-requisitos:** Use repositório próprio descartável com objetos indicados existentes e configuração local confiável. Confira repositório antes dos comandos.

**Opções:** -p exibe conforme tipo de objeto; use -t antes se tipo incerto.

**Quando utilizar:** Ao examinar estrutura armazenada de objeto em vez de resumo formatado de mudanças.

**Quando evitar:** Evite despejar blobs binários desconhecidos no terminal ou publicar conteúdo histórico sensível.

**Sintaxe**

`git cat-file -p HEAD`

**Exemplo básico**

`git cat-file -p HEAD`

Inspecione metadados do commit e IDs de tree e pais.

**Exemplo profissional**

`git cat-file -p HEAD:notes.txt`

Leia blob de texto registrado após conferir caminho e tipo.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Exibe cabeçalhos e mensagem de commit, entradas de tree formatadas, bytes de blob ou conteúdo de tag conforme aplicável.

**Impactos e efeitos colaterais:** No laboratório local completo, inspeção mostrada não grava objetos, altera referências, edita arquivos nem atualiza index. Clones parciais podem buscar objetos ausentes.

**Erros comuns:** Confundir IDs de pais do commit armazenado com diff ou presumir saída de blob inclui nomes de arquivos.

**Alternativas:** Use git show para revisão de commit orientada a pessoas ou git ls-tree para listagens estruturadas de tree.

**Recuperação:** Não é necessário desfazer inspeção mostrada. Se saída inesperada, verifique objeto, referência, intervalo de revisões ou caminho e inspecione erros antes de prosseguir.

**Versão e dependências:** Sintaxe padrão Git; use Git 2.40 ou superior nos laboratórios. IDs de objetos dependem do formato de objetos do repositório.

**Capítulos relacionados**

- [git-internals/02-blobs-and-trees](../../git-internals/02-blobs-and-trees/README.pt-BR.md)
- [git-internals/03-commits-and-tags](../../git-internals/03-commits-and-tags/README.pt-BR.md)
- [git-internals/10-porcelain-and-plumbing](../../git-internals/10-porcelain-and-plumbing/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-cat-file>

## git-hash-object

**`git hash-object`**

**Tipo:** Comando nativo

**Nível:** Avançado

**Pesquisar por intenção:** Inspecionar objetos Git

**Risco:** Somente leitura. Somente leitura nas formas mostradas em repositório local completo; não divulgue caminhos, conteúdo de objetos ou metadados sensíveis.

**Finalidade:** Calcular ID de objeto para conteúdo fornecido sem armazená-lo por padrão.

**Pré-requisitos:** Use repositório próprio descartável com objetos indicados existentes e configuração local confiável. Confira repositório antes dos comandos.

**Opções:** --no-filters calcula hash de entrada bruta sem filtros de caminho; -w grava objeto e não é usado nos exemplos; -t seleciona tipo de objeto.

**Quando utilizar:** Ao estudar endereçamento por conteúdo ou comparar arquivo bruto com ID de blob armazenado.

**Quando evitar:** Não presuma ID como checksum simples do arquivo ou operação padrão preparando arquivo.

**Sintaxe**

`git hash-object --no-filters notes.txt`

**Exemplo básico**

`git hash-object --no-filters notes.txt`

Calcule ID de blob de arquivo bruto sem gravá-lo.

**Exemplo profissional**

`git hash-object --no-filters docs/notes.txt`

Compare ID calculado de blob bruto com blob armazenado esperado, considerando filtros.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Exibe ID calculado usando estrutura de objeto Git e formato de hash do repositório; nenhum objeto é gravado nas formas mostradas.

**Impactos e efeitos colaterais:** Formas mostradas leem entrada e calculam ID sem gravar objeto; -w é escolha separada que altera estado.

**Erros comuns:** Comparar com checksum SHA comum sem considerar cabeçalho de objeto Git, filtros ou algoritmo de hash.

**Alternativas:** Use git rev-parse HEAD:path para localizar blob registrado existente, ou git add para staging intencional.

**Recuperação:** Não é necessário desfazer inspeção mostrada. Se saída inesperada, verifique objeto, referência, intervalo de revisões ou caminho e inspecione erros antes de prosseguir.

**Versão e dependências:** Sintaxe padrão Git; use Git 2.40 ou superior nos laboratórios. IDs de objetos dependem do formato de objetos do repositório.

**Capítulos relacionados**

- [git-internals/04-object-hashes](../../git-internals/04-object-hashes/README.pt-BR.md)
- [git-internals/02-blobs-and-trees](../../git-internals/02-blobs-and-trees/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-hash-object>

## git-ls-tree

**`git ls-tree`**

**Tipo:** Comando nativo

**Nível:** Avançado

**Pesquisar por intenção:** Inspecionar objetos Git, Inspecionar arquivos

**Risco:** Somente leitura. Somente leitura nas formas mostradas em repositório local completo; não divulgue caminhos, conteúdo de objetos ou metadados sensíveis.

**Finalidade:** Listar entradas de tree registrada selecionada com modos, tipos, IDs e caminhos.

**Pré-requisitos:** Use repositório próprio descartável com objetos indicados existentes e configuração local confiável. Confira repositório antes dos comandos.

**Opções:** -r percorre subtrees; -z usa saída terminada em NUL para parsing; --name-only seleciona caminhos.

**Quando utilizar:** Ao inspecionar snapshot histórico independentemente de arquivos atuais.

**Quando evitar:** Não use como prova de que working tree corresponde ao commit ou inclui arquivos não rastreados.

**Sintaxe**

`git ls-tree HEAD`

**Exemplo básico**

`git ls-tree HEAD`

Liste entradas da tree raiz do commit atual.

**Exemplo profissional**

`git ls-tree -r HEAD -- docs/`

Inspecione entradas registradas recursivamente sob diretório nomeado.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Exibe entradas da tree selecionada e referências de objetos; não ocorre checkout.

**Impactos e efeitos colaterais:** No laboratório local completo, inspeção mostrada não grava objetos, altera referências, edita arquivos nem atualiza index. Clones parciais podem buscar objetos ausentes.

**Erros comuns:** Confundir modos executável e gitlink armazenados com permissões completas do sistema operacional.

**Alternativas:** Use git ls-files --stage para conteúdo do index ou git status para estado de trabalho.

**Recuperação:** Não é necessário desfazer inspeção mostrada. Se saída inesperada, verifique objeto, referência, intervalo de revisões ou caminho e inspecione erros antes de prosseguir.

**Versão e dependências:** Sintaxe padrão Git; use Git 2.40 ou superior nos laboratórios. IDs de objetos dependem do formato de objetos do repositório.

**Capítulos relacionados**

- [git-internals/02-blobs-and-trees](../../git-internals/02-blobs-and-trees/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-ls-tree>

## git-rev-list

**`git rev-list`**

**Tipo:** Comando nativo

**Nível:** Avançado

**Pesquisar por intenção:** Inspecionar histórico, Inspecionar objetos Git

**Risco:** Somente leitura. Somente leitura nas formas mostradas em repositório local completo; não divulgue caminhos, conteúdo de objetos ou metadados sensíveis.

**Finalidade:** Enumerar alcance de commits ou contagens para conjuntos de revisões especificados.

**Pré-requisitos:** Use repositório próprio descartável com objetos indicados existentes e configuração local confiável. Confira repositório antes dos comandos.

**Opções:** --count relata contagem; --left-right distingue lados da diferença simétrica; --objects inclui travessia de objetos.

**Quando utilizar:** Ao automatizar contagens de ancestralidade ou inspecionar divergência de referências conhecidas.

**Quando evitar:** Não trate contagens iguais como conteúdo de arquivos equivalente, nem presuma histórico raso completo.

**Sintaxe**

`git rev-list --count HEAD`

**Exemplo básico**

`git rev-list --count HEAD`

Conte commits alcançáveis a partir de HEAD atual.

**Exemplo profissional**

`git rev-list --left-right --count main...feature`

Compare commits alcançáveis exclusivos de cada branch local verificada.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Retorna IDs ou contagens para conjunto de alcance solicitado; no exemplo bilateral as contagens representam commits exclusivos de cada lado.

**Impactos e efeitos colaterais:** No laboratório local completo, inspeção mostrada não grava objetos, altera referências, edita arquivos nem atualiza index. Clones parciais podem buscar objetos ausentes.

**Erros comuns:** Confundir A..B com A...B ou comparar contagem de commits em vez de snapshots.

**Alternativas:** Use git log para histórico orientado a pessoas ou git diff para comparar conteúdo de snapshots.

**Recuperação:** Não é necessário desfazer inspeção mostrada. Se saída inesperada, verifique objeto, referência, intervalo de revisões ou caminho e inspecione erros antes de prosseguir.

**Versão e dependências:** Sintaxe padrão Git; use Git 2.40 ou superior nos laboratórios. IDs de objetos dependem do formato de objetos do repositório.

**Capítulos relacionados**

- [git-internals/03-commits-and-tags](../../git-internals/03-commits-and-tags/README.pt-BR.md)
- [git-internals/09-reflogs-and-reachability](../../git-internals/09-reflogs-and-reachability/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-rev-list>

## git-symbolic-ref-read

**`git symbolic-ref HEAD`**

**Tipo:** Uso de opção

**Nível:** Avançado

**Pesquisar por intenção:** Inspecionar referências, Inspecionar estado do repositório

**Risco:** Somente leitura. Somente leitura nas formas mostradas em repositório local completo; não divulgue caminhos, conteúdo de objetos ou metadados sensíveis.

**Finalidade:** Ler destino de referência simbólica, aqui HEAD.

**Pré-requisitos:** Use repositório próprio descartável com objetos indicados existentes e configuração local confiável. Confira repositório antes dos comandos.

**Opções:** --short abrevia nome da referência; --quiet suprime erro para referência não simbólica mantendo status 1; fornecer novo destino é forma separada de gravação.

**Quando utilizar:** Ao determinar se HEAD está associado a branch nomeada.

**Quando evitar:** Evite forma de gravação para alternância comum; ela não faz checkout normal.

**Sintaxe**

`git symbolic-ref HEAD`

**Exemplo básico**

`git symbolic-ref HEAD`

Inspecione referência selecionada por HEAD associado.

**Exemplo profissional**

`git symbolic-ref --quiet --short HEAD`

Confira associação de branch em script; trate código de saída de HEAD destacado.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Exibe destino simbólico quando associado; HEAD destacado causa resultado não zero.

**Impactos e efeitos colaterais:** No laboratório local completo, inspeção mostrada não grava objetos, altera referências, edita arquivos nem atualiza index. Clones parciais podem buscar objetos ausentes.

**Erros comuns:** Presumir que symbolic-ref retorna ID de commit ou que mudar HEAD manualmente atualiza arquivos.

**Alternativas:** Use git branch --show-current para nome de branch ou git rev-parse HEAD para ID de commit.

**Recuperação:** Não é necessário desfazer inspeção mostrada. Se saída inesperada, verifique objeto, referência, intervalo de revisões ou caminho e inspecione erros antes de prosseguir.

**Versão e dependências:** Sintaxe padrão Git; use Git 2.40 ou superior nos laboratórios. IDs de objetos dependem do formato de objetos do repositório.

**Capítulos relacionados**

- [git-internals/05-refs-and-head](../../git-internals/05-refs-and-head/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-symbolic-ref>

## git-for-each-ref

**`git for-each-ref`**

**Tipo:** Comando nativo

**Nível:** Avançado

**Pesquisar por intenção:** Inspecionar referências, Automatizar fluxo

**Risco:** Somente leitura. Somente leitura nas formas mostradas em repositório local completo; não divulgue caminhos, conteúdo de objetos ou metadados sensíveis.

**Finalidade:** Enumerar referências com formatação e ordenação configuráveis.

**Pré-requisitos:** Use repositório próprio descartável com objetos indicados existentes e configuração local confiável. Confira repositório antes dos comandos.

**Opções:** --format seleciona campos; --sort ordena resultados; padrões de referência restringem namespace.

**Quando utilizar:** Ao produzir inventários estruturados de referências locais para revisão ou automação.

**Quando evitar:** Não presuma referências locais de rastreamento refletem estado atual do servidor nem use saída não validada como código shell.

**Sintaxe**

`git for-each-ref --format='%(refname) %(objectname)' refs/heads/`

**Exemplo básico**

`git for-each-ref --format='%(refname) %(objectname)' refs/heads/`

Liste nomes e IDs de referências de branches locais.

**Exemplo profissional**

`git for-each-ref --sort=-committerdate --format='%(refname:short)' refs/heads/`

Inspecione nomes de branches locais ordenados por data do committer da ponta.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Exibe registros formatados de referências locais correspondentes; não ocorre alteração de referência.

**Impactos e efeitos colaterais:** No laboratório local completo, inspeção mostrada não grava objetos, altera referências, edita arquivos nem atualiza index. Clones parciais podem buscar objetos ausentes.

**Erros comuns:** Confundir nomes de referências com branches selecionadas ou interpretar data de committer como criação da branch.

**Alternativas:** Use git show-ref para listagem simples de nome e ID ou git branch para inspeção orientada a branches.

**Recuperação:** Não é necessário desfazer inspeção mostrada. Se saída inesperada, verifique objeto, referência, intervalo de revisões ou caminho e inspecione erros antes de prosseguir.

**Versão e dependências:** Sintaxe padrão Git; use Git 2.40 ou superior nos laboratórios. IDs de objetos dependem do formato de objetos do repositório.

**Capítulos relacionados**

- [git-internals/05-refs-and-head](../../git-internals/05-refs-and-head/README.pt-BR.md)
- [git-internals/10-porcelain-and-plumbing](../../git-internals/10-porcelain-and-plumbing/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-for-each-ref>

## git-ls-files-stage

**`git ls-files --stage`**

**Tipo:** Uso de opção

**Nível:** Avançado

**Pesquisar por intenção:** Inspecionar internals do index, Inspecionar objetos Git

**Risco:** Somente leitura. Somente leitura nas formas mostradas em repositório local completo; não divulgue caminhos, conteúdo de objetos ou metadados sensíveis.

**Finalidade:** Inspecionar entradas do index com modo, ID de objeto, estágio e caminho.

**Pré-requisitos:** Use repositório próprio descartável com objetos indicados existentes e configuração local confiável. Confira repositório antes dos comandos.

**Opções:** --stage ou -s exibe metadados da entrada; -z é útil para parsing robusto de caminhos.

**Quando utilizar:** Ao estudar snapshot preparado, gitlinks ou estágios de conflito.

**Quando evitar:** Não interprete index como último snapshot registrado ou como todos arquivos do diretório de trabalho.

**Sintaxe**

`git ls-files --stage -- notes.txt`

**Exemplo básico**

`git ls-files --stage -- notes.txt`

Inspecione entrada do index para arquivo de prática existente.

**Exemplo profissional**

`git ls-files --stage`

Inspecione modos preparados, IDs de objetos e estágios de conflito no repositório descartável.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Exibe entradas incluindo estágio 0 para caminhos comuns mesclados e estágios maiores para conflitos não resolvidos quando presentes.

**Impactos e efeitos colaterais:** No laboratório local completo, inspeção mostrada não grava objetos, altera referências, edita arquivos nem atualiza index. Clones parciais podem buscar objetos ausentes.

**Erros comuns:** Presumir estágio 0 significa ausência de mudanças não preparadas ou gitlink é blob de arquivo comum.

**Alternativas:** Use git ls-tree HEAD para comparar entradas registradas da tree, ou git ls-files --unmerged para isolar conflitos.

**Recuperação:** Não é necessário desfazer inspeção mostrada. Se saída inesperada, verifique objeto, referência, intervalo de revisões ou caminho e inspecione erros antes de prosseguir.

**Versão e dependências:** Sintaxe padrão Git; use Git 2.40 ou superior nos laboratórios. IDs de objetos dependem do formato de objetos do repositório.

**Capítulos relacionados**

- [git-internals/06-index-internals](../../git-internals/06-index-internals/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-ls-files>


---

<!-- navigation-footer -->
[Anterior](../11-advanced-git-operations/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../13-security-and-maintenance/README.pt-BR.md)
<!-- /navigation-footer -->
