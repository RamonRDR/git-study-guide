# 05 Histórico e comparação

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../04-commits-and-tags/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../06-branch-management/README.pt-BR.md)
<!-- /navigation -->

Gerado a partir do JSON canônico. Edite os registros, não esta página.

As entradas descrevem comandos e operações, não uma sequência a executar. Pratique em repositórios descartáveis. Operações hospedadas são opcionais.

**Total de entradas distintas: 10**

- [`git log`](#git-log)
- [`git log --graph`](#git-log-graph)
- [`git log -- path`](#git-log-path)
- [`git show`](#git-show)
- [`git diff`](#git-diff)
- [`git diff --cached`](#git-diff-cached)
- [`git diff A B`](#git-diff-two-revisions)
- [`git diff --stat`](#git-diff-stat)
- [`git diff A...B`](#git-diff-three-dot)
- [`git range-diff`](#git-range-diff)

## git-log

**`git log`**

**Tipo:** Comando nativo

**Nível:** Iniciante

**Pesquisar por intenção:** Inspecionar histórico

**Risco:** Somente leitura. Somente leitura na configuração mostrada; a saída pode conter caminhos, mensagens ou conteúdo privados. Use repositório local confiável e revise antes de compartilhar.

**Finalidade:** Inspecionar commits alcançáveis a partir de uma revisão inicial, normalmente HEAD.

**Pré-requisitos:** Use repositório de prática confiável com os commits referenciados disponíveis localmente.

**Opções:** -5 limita a quantidade de commits exibidos; --oneline mostra IDs abreviados e assuntos.

**Quando utilizar:** Ao investigar o que foi registrado e por quem.

**Quando evitar:** Não use o log padrão para inferir todas as branches ou edições não registradas.

**Sintaxe**

`git log -5`

**Exemplo básico**

`git log -3`

Inspecione três commits recentes em histórico de prática.

**Exemplo profissional**

`git log --oneline main..feature`

Inspecione commits alcançáveis pela branch local feature mas não pela main; ambas devem existir.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Metadados dos commits são exibidos para o histórico alcançável selecionado; um paginador pode abrir.

**Impactos e efeitos colaterais:** Na exibição interna normal, nenhum arquivo de trabalho, index, referência de commit ou remoto é alterado.

**Erros comuns:** Presumir que log padrão inclui commits inalcançáveis ou todas as branches remotas.

**Alternativas:** Use git show para um commit ou git reflog para investigar movimentos de referências locais.

**Recuperação:** Não é preciso recuperar o repositório após inspeção; confira revisões ou caminhos selecionados e repita a comparação se necessário.

**Versão e dependências:** Use Git padrão em repositório local confiável; não exige visualizador opcional. Um paginador configurado pode abrir.

**Capítulos relacionados**

- [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.pt-BR.md)
- [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-log>

## git-log-graph

**`git log --graph`**

**Tipo:** Uso de opção

**Nível:** Intermediário

**Pesquisar por intenção:** Inspecionar histórico, Gerenciar branches

**Risco:** Somente leitura. Somente leitura na configuração mostrada; a saída pode conter caminhos, mensagens ou conteúdo privados. Use repositório local confiável e revise antes de compartilhar.

**Finalidade:** Visualizar relações de pais e divergências no histórico de commits.

**Pré-requisitos:** Use repositório de prática confiável com os commits referenciados disponíveis localmente.

**Opções:** --graph desenha linhas de ancestralidade; --oneline resume cada commit; --all parte de referências locais e HEAD.

**Quando utilizar:** Ao revisar topologia de branches e histórico de merges.

**Quando evitar:** Não trate posição das colunas ou espaçamento vertical como cronologia exata.

**Sintaxe**

`git log --oneline --graph --all`

**Exemplo básico**

`git log --oneline --graph`

Veja a ancestralidade da branch atual.

**Exemplo profissional**

`git log --oneline --graph --all --decorate`

Revise topologia local de branches e tags antes de integrar trabalho.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Um grafo textual exibe commits selecionados e conexões de pais.

**Impactos e efeitos colaterais:** Na exibição interna normal, nenhum arquivo de trabalho, index, referência de commit ou remoto é alterado.

**Erros comuns:** Presumir que --all busca estado remoto ou inclui objetos inalcançáveis.

**Alternativas:** Use git merge-base para ancestral comum ou git log sem grafo para mensagens detalhadas.

**Recuperação:** Não é preciso recuperar o repositório após inspeção; confira revisões ou caminhos selecionados e repita a comparação se necessário.

**Versão e dependências:** Use Git padrão em repositório local confiável; não exige visualizador opcional. Um paginador configurado pode abrir.

**Capítulos relacionados**

- [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.pt-BR.md)
- [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.pt-BR.md)
- [branches/02-start-points-and-comparison](../../branches/02-start-points-and-comparison/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-log>

## git-log-path

**`git log -- path`**

**Tipo:** Uso de opção

**Nível:** Intermediário

**Pesquisar por intenção:** Inspecionar histórico, Inspecionar arquivos

**Risco:** Somente leitura. Somente leitura na configuração mostrada; a saída pode conter caminhos, mensagens ou conteúdo privados. Use repositório local confiável e revise antes de compartilhar.

**Finalidade:** Inspecionar histórico selecionado por mudanças em determinado caminho.

**Pré-requisitos:** Use repositório de prática confiável com os commits referenciados disponíveis localmente.

**Opções:** -- separa revisões de caminhos; --follow acompanha histórico além de renomeações para um único arquivo com limitações.

**Quando utilizar:** Ao investigar a evolução de arquivo ou diretório específico.

**Quando evitar:** Não suponha que simplificação padrão lista todo merge relevante ou acompanha toda renomeação.

**Sintaxe**

`git log -- notes.txt`

**Exemplo básico**

`git log -- notes.txt`

Inspecione mudanças em arquivo fictício de notas rastreado.

**Exemplo profissional**

`git log --follow -- docs/setup.md`

Investigue arquivo único de documentação através de renomeações detectadas.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Exibe commits selecionados por regras de histórico de caminho e simplificação, não edições atuais não registradas.

**Impactos e efeitos colaterais:** Na exibição interna normal, nenhum arquivo de trabalho, index, referência de commit ou remoto é alterado.

**Erros comuns:** Omitir -- quando nome de caminho também pode nomear revisão.

**Alternativas:** Use git blame para atribuição por linha ou git log --full-history com caminho ao investigar merges.

**Recuperação:** Não é preciso recuperar o repositório após inspeção; confira revisões ou caminhos selecionados e repita a comparação se necessário.

**Versão e dependências:** Use Git padrão em repositório local confiável; não exige visualizador opcional. Um paginador configurado pode abrir.

**Capítulos relacionados**

- [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.pt-BR.md)
- [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-log>

## git-show

**`git show`**

**Tipo:** Comando nativo

**Nível:** Iniciante

**Pesquisar por intenção:** Inspecionar histórico, Revisar alterações, Inspecionar objetos Git

**Risco:** Somente leitura. Somente leitura com diff interno; revise saída sensível e evite drivers externos de diff, filtros de conversão de texto ou paginadores não confiáveis.

**Finalidade:** Exibir objeto Git; para commit comum inclui metadados e patch por padrão.

**Pré-requisitos:** Use repositório de prática confiável com os commits referenciados disponíveis localmente.

**Opções:** --stat resume mudanças; revision:path seleciona blob em caminho histórico.

**Quando utilizar:** Ao revisar commit, tag ou snapshot histórico de arquivo específico.

**Quando evitar:** Não presuma que exibição de merge mostra diferenças de todos os pais por padrão.

**Sintaxe**

`git show HEAD`

**Exemplo básico**

`git show HEAD`

Revise a última mudança registrada.

**Exemplo profissional**

`git show HEAD:notes.txt`

Inspecione conteúdo registrado de arquivo fictício sem checkout.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Exibe objeto solicitado em representação adequada ao tipo; HEAD é o padrão.

**Impactos e efeitos colaterais:** Na exibição interna normal, nenhum arquivo de trabalho, index, referência de commit ou remoto é alterado.

**Erros comuns:** Confundir git show HEAD:path com arquivo de trabalho atual.

**Alternativas:** Use git diff para dois snapshots ou git cat-file para inspeção de objetos de baixo nível.

**Recuperação:** Não é preciso recuperar o repositório após inspeção; confira revisões ou caminhos selecionados e repita a comparação se necessário.

**Versão e dependências:** Use Git padrão em repositório local confiável; não exige visualizador opcional. Um paginador configurado pode abrir.

**Capítulos relacionados**

- [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.pt-BR.md)
- [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.pt-BR.md)
- [git-internals/02-blobs-and-trees](../../git-internals/02-blobs-and-trees/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-show>

## git-diff

**`git diff`**

**Tipo:** Comando nativo

**Nível:** Iniciante

**Pesquisar por intenção:** Comparar alterações, Revisar alterações

**Risco:** Alteração de estado. Operação de inspeção com possíveis escritas em metadados do index, não operação de staging; evite drivers externos de diff não confiáveis e revise saída sensível antes de compartilhar.

**Finalidade:** Comparar conteúdo rastreado da working tree com o index.

**Pré-requisitos:** Use repositório de prática confiável com working tree e index; revise git status antes.

**Opções:** -- separa opções e revisões de caminhos; --stat resume mudanças.

**Quando utilizar:** Antes de preparar alterações, para revisar diferenças não preparadas.

**Quando evitar:** Não dependa apenas desta forma para revisar mudanças preparadas ou arquivos não rastreados.

**Sintaxe**

`git diff -- notes.txt`

**Exemplo básico**

`git diff`

Revise edição rastreada não preparada.

**Exemplo profissional**

`git diff -- notes.txt`

Revise um arquivo rastreado antes do staging.

**Impacto no estado**

- Working tree: Inalterado
- Index: Condicional
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Exibe diferenças não preparadas de caminhos rastreados; saída vazia pode indicar ausência dessas diferenças.

**Impactos e efeitos colaterais:** Arquivos de trabalho, IDs dos blobs preparados, referências de commits e remoto permanecem inalterados no comportamento interno; diff.autoRefreshIndex pode atualizar metadados stat de arquivos no index.

**Erros comuns:** Presumir que diff vazio significa repositório inteiramente limpo.

**Alternativas:** Use git diff --cached para mudanças preparadas e git status para arquivos não rastreados.

**Recuperação:** Não é preciso recuperar o repositório após inspeção; confira revisões ou caminhos selecionados e repita a comparação se necessário.

**Versão e dependências:** Use Git padrão em repositório local confiável; não exige visualizador opcional. Um paginador configurado pode abrir.

**Capítulos relacionados**

- [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.pt-BR.md)
- [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-diff>
- <https://git-scm.com/docs/git-config/2.36.3.html>

## git-diff-cached

**`git diff --cached`**

**Tipo:** Uso de opção

**Nível:** Iniciante

**Pesquisar por intenção:** Comparar alterações, Revisar alterações, Preparar alterações

**Risco:** Somente leitura. Somente leitura com diff interno; revise saída sensível e evite drivers externos de diff, filtros de conversão de texto ou paginadores não confiáveis.

**Finalidade:** Comparar index com HEAD para revisar mudanças preparadas.

**Pré-requisitos:** Use repositório de prática confiável com working tree e index; revise git status antes.

**Opções:** --staged é sinônimo de --cached; -- seguido de caminho limita saída.

**Quando utilizar:** Imediatamente antes de registrar o snapshot preparado.

**Quando evitar:** Não use esta forma para inspecionar mudanças posteriores ao staging sem prepará-las novamente.

**Sintaxe**

`git diff --cached`

**Exemplo básico**

`git diff --cached`

Inspecione mudanças já selecionadas para commit.

**Exemplo profissional**

`git diff --cached -- notes.txt`

Confirme que apenas parte desejada de arquivo parcialmente preparado está no index.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Mostra diferença preparada em relação a HEAD; em branch sem primeiro commit mostra todas as mudanças preparadas se nenhum commit for informado.

**Impactos e efeitos colaterais:** Na exibição interna normal, nenhum arquivo de trabalho, index, referência de commit ou remoto é alterado.

**Erros comuns:** Confundir diferenças do cache com diferenças da working tree.

**Alternativas:** Use git diff para ver o que ainda não está preparado ou git status para inspecionar ambos estados.

**Recuperação:** Não é preciso recuperar o repositório após inspeção; confira revisões ou caminhos selecionados e repita a comparação se necessário.

**Versão e dependências:** Use Git padrão em repositório local confiável; não exige visualizador opcional. Um paginador configurado pode abrir.

**Capítulos relacionados**

- [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.pt-BR.md)
- [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-diff>

## git-diff-two-revisions

**`git diff A B`**

**Tipo:** Uso de opção

**Nível:** Intermediário

**Pesquisar por intenção:** Comparar alterações, Revisar alterações

**Risco:** Somente leitura. Somente leitura com diff interno; revise saída sensível e evite drivers externos de diff, filtros de conversão de texto ou paginadores não confiáveis.

**Finalidade:** Comparar diretamente dois snapshots registrados, independentemente da ancestralidade.

**Pré-requisitos:** Use repositório de prática confiável com os commits referenciados disponíveis localmente.

**Opções:** Informe duas revisões; A..B é equivalente em git diff, diferente de intervalo de commits em git log.

**Quando utilizar:** Ao conferir diferenças de estado final entre branches, tags ou commits.

**Quando evitar:** Evite interpretar como lista de commits individuais ou somente mudanças introduzidas por feature.

**Sintaxe**

`git diff main feature`

**Exemplo básico**

`git diff HEAD~1 HEAD`

Compare commit não inicial ao primeiro pai.

**Exemplo profissional**

`git diff main feature`

Compare pontas das branches locais main e feature existentes.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Exibe patch do primeiro snapshot ao segundo; inverter entradas inverte a comparação.

**Impactos e efeitos colaterais:** Na exibição interna normal, nenhum arquivo de trabalho, index, referência de commit ou remoto é alterado.

**Erros comuns:** Tratar sintaxe de dois pontos no diff como conjunto de revisões igual a git log A..B.

**Alternativas:** Use git diff A...B para comparar desde base de merge até B ou git log A..B para listar commits.

**Recuperação:** Não é preciso recuperar o repositório após inspeção; confira revisões ou caminhos selecionados e repita a comparação se necessário.

**Versão e dependências:** Use Git padrão em repositório local confiável; não exige visualizador opcional. Um paginador configurado pode abrir.

**Capítulos relacionados**

- [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.pt-BR.md)
- [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.pt-BR.md)
- [branches/02-start-points-and-comparison](../../branches/02-start-points-and-comparison/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-diff>

## git-diff-stat

**`git diff --stat`**

**Tipo:** Uso de opção

**Nível:** Iniciante

**Pesquisar por intenção:** Comparar alterações, Revisar alterações

**Risco:** Alteração de estado. Operação de inspeção com possíveis escritas em metadados do index, não operação de staging; evite drivers externos de diff não confiáveis e revise saída sensível antes de compartilhar.

**Finalidade:** Resumir escopo de um diff por arquivos afetados e contagens de mudanças.

**Pré-requisitos:** Use repositório de prática confiável com working tree e index; revise git status antes.

**Opções:** --stat solicita resumo; combine com --cached ou duas revisões para escolher outra comparação.

**Quando utilizar:** Ao estimar escopo de revisão antes de ler patch completo.

**Quando evitar:** Não trate contagens de linhas como medida de correção, complexidade ou produtividade.

**Sintaxe**

`git diff --stat`

**Exemplo básico**

`git diff --stat`

Resuma alterações não preparadas.

**Exemplo profissional**

`git diff --cached --stat`

Estime escopo preparado antes de ler o patch.

**Impacto no estado**

- Working tree: Inalterado
- Index: Condicional
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Exibe resumos por arquivo e totais da comparação selecionada; binários têm resumos diferentes.

**Impactos e efeitos colaterais:** Arquivos de trabalho, IDs dos blobs preparados, referências de commits e remoto permanecem inalterados no comportamento interno; diff.autoRefreshIndex pode atualizar metadados stat de arquivos no index.

**Erros comuns:** Presumir que --stat altera pontos da comparação ou substitui leitura do patch.

**Alternativas:** Use git diff --name-status para códigos de estado ou git diff completo para revisar conteúdo.

**Recuperação:** Não é preciso recuperar o repositório após inspeção; confira revisões ou caminhos selecionados e repita a comparação se necessário.

**Versão e dependências:** Use Git padrão em repositório local confiável; não exige visualizador opcional. Um paginador configurado pode abrir.

**Capítulos relacionados**

- [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.pt-BR.md)
- [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-diff>
- <https://git-scm.com/docs/git-config/2.36.3.html>

## git-diff-three-dot

**`git diff A...B`**

**Tipo:** Uso de opção

**Nível:** Intermediário

**Pesquisar por intenção:** Comparar alterações, Revisar alterações, Inspecionar histórico

**Risco:** Somente leitura. Somente leitura com diff interno; revise saída sensível e evite drivers externos de diff, filtros de conversão de texto ou paginadores não confiáveis.

**Finalidade:** Comparar snapshot em uma base de merge de A e B com snapshot em B.

**Pré-requisitos:** Use repositório local confiável com ambas referências e ancestral comum adequado; verifique a base de merge antes.

**Opções:** Três pontos selecionam base de merge como primeiro extremo; revisão à direita é segundo extremo.

**Quando utilizar:** Ao revisar mudanças de branch relativas a ancestral comum, especialmente após divergência.

**Quando evitar:** Evite presumir simetria ou identidade com diff de PR hospedado; inspecione bases de merge ambíguas.

**Sintaxe**

`git diff main...feature`

**Exemplo básico**

`git diff main...feature`

Revise branch feature local existente relativa à base comum com main.

**Exemplo profissional**

`git diff main...feature -- notes.txt`

Revise mudanças da branch em arquivo fictício após conferir base de merge.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Mostra diferença líquida da base comum selecionada ao snapshot da direita, não mudanças exclusivas da branch esquerda.

**Impactos e efeitos colaterais:** Na exibição interna normal, nenhum arquivo de trabalho, index, referência de commit ou remoto é alterado.

**Erros comuns:** Confundir git diff A...B com diferença simétrica de conjuntos de commits em git log A...B.

**Alternativas:** Use git diff A B para comparar pontas ou inspecione git merge-base --all A B antes de selecionar base explícita.

**Recuperação:** Não é preciso recuperar o repositório após inspeção; confira revisões ou caminhos selecionados e repita a comparação se necessário.

**Versão e dependências:** Use Git padrão em repositório local confiável; não exige visualizador opcional. Um paginador configurado pode abrir.

**Capítulos relacionados**

- [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.pt-BR.md)
- [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.pt-BR.md)
- [branches/02-start-points-and-comparison](../../branches/02-start-points-and-comparison/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-diff>

## git-range-diff

**`git range-diff`**

**Tipo:** Comando nativo

**Nível:** Avançado

**Pesquisar por intenção:** Comparar alterações, Revisar alterações, Reescrever histórico local

**Risco:** Somente leitura. Somente leitura com diff interno; revise saída sensível e evite drivers externos de diff, filtros de conversão de texto ou paginadores não confiáveis.

**Finalidade:** Comparar patches e mensagens de duas versões de uma série de commits.

**Pré-requisitos:** Use repositório local confiável com ambos intervalos de commits não vazios; preserve ponta antiga antes de reescrever histórico.

**Opções:** Informe dois intervalos explícitos de revisões; --no-color desativa cores para leitura de saída simples.

**Quando utilizar:** Ao revisar mudanças em série privada de patches após correções ou rebase.

**Quando evitar:** Não use como prova de equivalência semântica ou API estável para máquinas; merges são ignorados por padrão.

**Sintaxe**

`git range-diff main..old-series main..feature`

**Exemplo básico**

`git range-diff main..old-series main..feature`

Compare duas séries locais existentes baseadas em main.

**Exemplo profissional**

`git range-diff --no-color main..old-series main..feature`

Revise série salva pré-rebase contra versão revisada; confirme mudanças reais separadamente.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Exibe correspondência aproximada entre commits e mudanças em patches e metadados; commits sem correspondência são identificados.

**Impactos e efeitos colaterais:** Na exibição interna normal, nenhum arquivo de trabalho, index, referência de commit ou remoto é alterado.

**Erros comuns:** Comparar apenas snapshots finais e perder mudanças individuais, ou confiar em correspondência como prova de correção.

**Alternativas:** Use git diff entre as pontas para comparar conteúdo final e execute testes relevantes.

**Recuperação:** Não é preciso recuperar o repositório após inspeção; confira revisões ou caminhos selecionados e repita a comparação se necessário.

**Versão e dependências:** Exige Git 2.19 ou superior; use configuração local confiável. Saída destinada a humanos, não parser estável.

**Capítulos relacionados**

- [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.pt-BR.md)
- [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.pt-BR.md)
- [merge-and-conflicts/07-interactive-rebase](../../merge-and-conflicts/07-interactive-rebase/README.pt-BR.md)
- [professional-workflows/08-code-review](../../professional-workflows/08-code-review/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-range-diff>


---

<!-- navigation-footer -->
[Anterior](../04-commits-and-tags/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../06-branch-management/README.pt-BR.md)
<!-- /navigation-footer -->
