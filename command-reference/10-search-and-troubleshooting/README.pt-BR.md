# 10 Pesquisa e diagnóstico

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../09-recovery-and-stash/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../11-advanced-git-operations/README.pt-BR.md)
<!-- /navigation -->

Gerado a partir do JSON canônico. Edite os registros, não esta página.

As entradas descrevem comandos e operações, não uma sequência a executar. Pratique em repositórios descartáveis. Operações hospedadas são opcionais.

**Total de entradas distintas: 8**

- [`git grep`](#git-grep)
- [`git blame`](#git-blame)
- [`git log -S`](#git-log-pickaxe-string)
- [`git log -G`](#git-log-pickaxe-regex)
- [`git log --follow`](#git-log-follow)
- [`git diff --check`](#git-diff-check)
- [`git ls-files --unmerged`](#git-ls-files-unmerged)
- [`git bisect`](#git-bisect)

## git-grep

**`git grep`**

**Tipo:** Comando nativo

**Nível:** Intermediário

**Pesquisar por intenção:** Pesquisar conteúdo

**Risco:** Somente leitura. Somente leitura no contexto local comum mostrado; evite divulgar saída sensível. Use configuração confiável e objetos locais completos.

**Finalidade:** Buscar linhas correspondentes em arquivos rastreados, index ou árvores selecionadas.

**Pré-requisitos:** Use repositório descartável com arquivos e revisões indicados existentes; confira o repositório e use configuração confiável.

**Opções:** -n exibe números de linha; -F usa padrões literais; --cached busca conteúdo do index; argumento de árvore busca árvore registrada.

**Quando utilizar:** Ao localizar símbolo ou texto em conteúdo versionado.

**Quando evitar:** Não presuma busca padrão em arquivos ignorados ou não rastreados.

**Sintaxe**

`git grep -n -F "TODO"`

**Exemplo básico**

`git grep -n -F "TODO"`

Encontre TODO literal em arquivos rastreados de prática.

**Exemplo profissional**

`git grep -n -F "timeout" HEAD -- src/`

Busque diretório de código registrado no laboratório.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Exibe correspondências com contexto solicitado; saída 1 significa ausência de correspondências, não necessariamente erro de execução.

**Impactos e efeitos colaterais:** A inspeção mostrada não modifica intencionalmente conteúdo rastreado, index, referências ou remoto.

**Erros comuns:** Confundir expressões regulares com literais ou buscar snapshot errado.

**Alternativas:** Use busca confiável no sistema de arquivos para arquivos fora do escopo Git selecionado.

**Recuperação:** Inspeção não exige desfazer; verifique revisão, caminho, expressão de busca e código de saída antes de interpretar resultados.

**Versão e dependências:** Sintaxe padrão Git; use Git 2.40 ou superior nos laboratórios do guia.

**Capítulos relacionados**

- [advanced-git/09-blame-and-grep](../../advanced-git/09-blame-and-grep/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-grep>

## git-blame

**`git blame`**

**Tipo:** Comando nativo

**Nível:** Intermediário

**Pesquisar por intenção:** Inspecionar autoria, Inspecionar histórico

**Risco:** Somente leitura. Somente leitura no contexto local comum mostrado; evite divulgar saída sensível. Use configuração confiável e objetos locais completos.

**Finalidade:** Rastrear cada linha selecionada à revisão à qual Git a atribui.

**Pré-requisitos:** Use repositório descartável com arquivos e revisões indicados existentes; confira o repositório e use configuração confiável.

**Opções:** -L limita intervalos; -w ignora diferenças de espaços; -M e -C podem detectar linhas movidas ou copiadas com trabalho adicional.

**Quando utilizar:** Ao investigar contexto de linha antes de mudar.

**Quando evitar:** Não use atribuição como prova de culpa ou autoria original de ideia.

**Sintaxe**

`git blame HEAD -- notes.txt`

**Exemplo básico**

`git blame HEAD -- notes.txt`

Inspecione atribuição de linhas registradas de prática.

**Exemplo profissional**

`git blame -L 1,10 HEAD -- notes.txt`

Revise primeiras dez linhas do arquivo registrado, se presentes.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Exibe commits atribuídos e linhas; resultado depende de revisão e opções de detecção.

**Impactos e efeitos colaterais:** A inspeção mostrada não modifica intencionalmente conteúdo rastreado, index, referências ou remoto.

**Erros comuns:** Presumir que autor atribuído mais recente introduziu problema subjacente.

**Alternativas:** Inspecione git show e histórico anterior para contexto; use git log -G para linhas alteradas.

**Recuperação:** Inspeção não exige desfazer; verifique revisão, caminho, expressão de busca e código de saída antes de interpretar resultados.

**Versão e dependências:** Sintaxe padrão Git; use Git 2.40 ou superior nos laboratórios do guia.

**Capítulos relacionados**

- [advanced-git/09-blame-and-grep](../../advanced-git/09-blame-and-grep/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-blame>

## git-log-pickaxe-string

**`git log -S`**

**Tipo:** Uso de opção

**Nível:** Avançado

**Pesquisar por intenção:** Pesquisar conteúdo, Inspecionar histórico

**Risco:** Somente leitura. Somente leitura no contexto local comum mostrado; evite divulgar saída sensível. Use configuração confiável e objetos locais completos.

**Finalidade:** Encontrar commits cujo diff altera quantidade de ocorrências de string.

**Pré-requisitos:** Use repositório descartável com arquivos e revisões indicados existentes; confira o repositório e use configuração confiável.

**Opções:** -S usa string; --pickaxe-regex altera interpretação; -p exibe patches.

**Quando utilizar:** Ao rastrear quando literal foi introduzido ou removido.

**Quando evitar:** Não use como busca geral de toda edição de linha contendo texto.

**Sintaxe**

`git log -S "timeout" -- notes.txt`

**Exemplo básico**

`git log -S "timeout" -- notes.txt`

Encontre mudanças na contagem de ocorrências de timeout.

**Exemplo profissional**

`git log -p -S "timeout" -- notes.txt`

Inspecione patches correspondentes no arquivo de prática.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Lista commits correspondentes no histórico selecionado; edições que preservam contagem podem não corresponder.

**Impactos e efeitos colaterais:** A inspeção mostrada não modifica intencionalmente conteúdo rastreado, index, referências ou remoto.

**Erros comuns:** Esperar que -S e -G selecionem mesmos commits ou ignorar configuração de diff de merges.

**Alternativas:** Use git log -G para localizar linhas adicionadas ou removidas correspondentes.

**Recuperação:** Inspeção não exige desfazer; verifique revisão, caminho, expressão de busca e código de saída antes de interpretar resultados.

**Versão e dependências:** Sintaxe padrão Git; use Git 2.40 ou superior nos laboratórios do guia.

**Capítulos relacionados**

- [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.pt-BR.md)
- [advanced-git/09-blame-and-grep](../../advanced-git/09-blame-and-grep/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-log>

## git-log-pickaxe-regex

**`git log -G`**

**Tipo:** Uso de opção

**Nível:** Avançado

**Pesquisar por intenção:** Pesquisar conteúdo, Inspecionar histórico

**Risco:** Somente leitura. Somente leitura no contexto local comum mostrado; evite divulgar saída sensível. Use configuração confiável e objetos locais completos.

**Finalidade:** Encontrar commits com linhas de patch adicionadas ou removidas que correspondem à expressão regular.

**Pré-requisitos:** Use repositório descartável com arquivos e revisões indicados existentes; confira o repositório e use configuração confiável.

**Opções:** -G aceita expressão regular; -p exibe patches dos commits correspondentes.

**Quando utilizar:** Ao rastrear mudanças em linha correspondente mesmo quando contagens ficam iguais.

**Quando evitar:** Não presuma busca em linhas inalteradas ou todos snapshots históricos.

**Sintaxe**

`git log -G "timeout" -- notes.txt`

**Exemplo básico**

`git log -G "timeout" -- notes.txt`

Encontre patches com linhas correspondentes adicionadas ou removidas.

**Exemplo profissional**

`git log -p -G "timeout[ ]*=" -- notes.txt`

Inspecione mudanças de atribuição correspondentes no histórico de prática.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Lista commits com linhas de diff correspondentes conforme revisão e configurações selecionadas.

**Impactos e efeitos colaterais:** A inspeção mostrada não modifica intencionalmente conteúdo rastreado, index, referências ou remoto.

**Erros comuns:** Usar metacaracteres regex sem intenção ou esperar inclusão padrão de diffs de merge.

**Alternativas:** Use -S quando mudança na contagem de ocorrências for sinal relevante.

**Recuperação:** Inspeção não exige desfazer; verifique revisão, caminho, expressão de busca e código de saída antes de interpretar resultados.

**Versão e dependências:** Sintaxe padrão Git; use Git 2.40 ou superior nos laboratórios do guia.

**Capítulos relacionados**

- [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.pt-BR.md)
- [advanced-git/09-blame-and-grep](../../advanced-git/09-blame-and-grep/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-log>

## git-log-follow

**`git log --follow`**

**Tipo:** Uso de opção

**Nível:** Intermediário

**Pesquisar por intenção:** Inspecionar histórico, Pesquisar conteúdo

**Risco:** Somente leitura. Somente leitura no contexto local comum mostrado; evite divulgar saída sensível. Use configuração confiável e objetos locais completos.

**Finalidade:** Continuar histórico de um arquivo através de renomeações detectadas.

**Pré-requisitos:** Use repositório descartável com arquivos e revisões indicados existentes; confira o repositório e use configuração confiável.

**Opções:** --follow opera em caminho único; -p inclui patches.

**Quando utilizar:** Ao investigar arquivo cujo caminho mudou.

**Quando evitar:** Não espere histórico completo de diretório ou rastreamento perfeito em renomeações e merges complexos.

**Sintaxe**

`git log --follow -- notes.txt`

**Exemplo básico**

`git log --follow -- notes.txt`

Inspecione histórico de arquivo atual através de renomeações detectadas.

**Exemplo profissional**

`git log -p --follow -- docs/notes.txt`

Inspecione patches de arquivo de documentação através de renomeações detectadas.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Exibe histórico do arquivo selecionado incluindo nomes anteriores detectados, sujeito a histórico e detecção.

**Impactos e efeitos colaterais:** A inspeção mostrada não modifica intencionalmente conteúdo rastreado, index, referências ou remoto.

**Erros comuns:** Passar vários caminhos ou interpretar ausência de renomeação detectada como prova de falta de relação.

**Alternativas:** Inspecione git log --name-status e diffs de commits para reorganizações complexas.

**Recuperação:** Inspeção não exige desfazer; verifique revisão, caminho, expressão de busca e código de saída antes de interpretar resultados.

**Versão e dependências:** Sintaxe padrão Git; use Git 2.40 ou superior nos laboratórios do guia.

**Capítulos relacionados**

- [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.pt-BR.md)
- [advanced-git/09-blame-and-grep](../../advanced-git/09-blame-and-grep/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-log>

## git-diff-check

**`git diff --check`**

**Tipo:** Uso de opção

**Nível:** Intermediário

**Pesquisar por intenção:** Revisar alterações, Inspecionar estado do repositório

**Risco:** Alteração de estado. Inspeção pode atualizar metadados do index; não corrige erros.

**Finalidade:** Sinalizar marcadores de conflito e erros de espaços introduzidos conforme configuração.

**Pré-requisitos:** Use repositório descartável com arquivos e revisões indicados existentes; confira o repositório e use configuração confiável.

**Opções:** --check relata problemas e retorna código não zero quando detectados; --cached seleciona mudanças preparadas.

**Quando utilizar:** Ao conferir mudança proposta antes de commit ou revisão.

**Quando evitar:** Não substitua testes ou inspeção completa de conflitos por ele.

**Sintaxe**

`git diff --check`

**Exemplo básico**

`git diff --check`

Confira mudanças não preparadas quanto a erros de espaços ou marcadores de conflito introduzidos.

**Exemplo profissional**

`git diff --cached --check`

Confira mudanças preparadas antes de commit revisado.

**Impacto no estado**

- Working tree: Inalterado
- Index: Condicional
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Relata linhas problemáticas quando detectadas; não ocorre correção automática.

**Impactos e efeitos colaterais:** Não edita conteúdo; diff comum de working tree pode atualizar metadados stat do index.

**Erros comuns:** Conferir apenas edições não preparadas quando commit pretendido está preparado.

**Alternativas:** Use git diff --cached para revisão de conteúdo e linter do projeto para regras mais amplas.

**Recuperação:** Inspeção não exige desfazer; verifique revisão, caminho, expressão de busca e código de saída antes de interpretar resultados.

**Versão e dependências:** Sintaxe padrão Git; use Git 2.40 ou superior nos laboratórios do guia.

**Capítulos relacionados**

- [basic-commands/05-ignore-and-review](../../basic-commands/05-ignore-and-review/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-diff>

## git-ls-files-unmerged

**`git ls-files --unmerged`**

**Tipo:** Uso de opção

**Nível:** Intermediário

**Pesquisar por intenção:** Inspecionar internals do index, Resolver conflitos

**Risco:** Somente leitura. Somente leitura no contexto local comum mostrado; evite divulgar saída sensível. Use configuração confiável e objetos locais completos.

**Finalidade:** Inspecionar entradas do index que ainda possuem estágios não mesclados.

**Pré-requisitos:** Use repositório descartável com arquivos e revisões indicados existentes; confira o repositório e use configuração confiável.

**Opções:** -u ou --unmerged exibe caminhos não mesclados com modo, ID de objeto e estágio; pathspec restringe saída.

**Quando utilizar:** Ao diagnosticar conflitos antes de preparar resolução.

**Quando evitar:** Não trate saída vazia como prova de resolução final correta.

**Sintaxe**

`git ls-files --unmerged`

**Exemplo básico**

`git ls-files --unmerged`

Inspecione entradas não mescladas do index durante conflito de prática.

**Exemplo profissional**

`git ls-files -u -- notes.txt`

Inspecione estágios de conflito de arquivo nomeado no laboratório.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Lista estágios de conflito disponíveis; estágios 1, 2 e 3 representam base e dois lados quando presentes.

**Impactos e efeitos colaterais:** A inspeção mostrada não modifica intencionalmente conteúdo rastreado, index, referências ou remoto.

**Erros comuns:** Presumir que todo conflito tem três estágios ou que ours sempre significa feature original durante rebase.

**Alternativas:** Use git status para resumo e inspecione cada estágio disponível com git show.

**Recuperação:** Inspeção não exige desfazer; verifique revisão, caminho, expressão de busca e código de saída antes de interpretar resultados.

**Versão e dependências:** Sintaxe padrão Git; use Git 2.40 ou superior nos laboratórios do guia.

**Capítulos relacionados**

- [merge-and-conflicts/04-conflict-resolution](../../merge-and-conflicts/04-conflict-resolution/README.pt-BR.md)
- [git-internals/06-index-internals](../../git-internals/06-index-internals/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-ls-files>

## git-bisect

**`git bisect`**

**Tipo:** Fluxo

**Nível:** Avançado

**Pesquisar por intenção:** Encontrar regressão, Inspecionar histórico

**Risco:** Alteração de estado. Selecione só código histórico confiável em laboratório isolado; não execute scripts desconhecidos automaticamente. Preserve trabalho original.

**Finalidade:** Encontrar limite de regressão classificando repetidamente commits históricos.

**Pré-requisitos:** Use repositório descartável limpo com histórico completo, ponta original salva, commits good e bad conhecidos e teste seguro repetível.

**Opções:** Inicie, marque revisões bad e good, teste cada candidato, classifique com good ou bad, pule commits não testáveis com skip e finalize com git bisect reset.

**Quando utilizar:** Quando teste repetível distingue revisão com falha conhecida de revisão anterior aprovada.

**Quando evitar:** Evite com edições não preservadas ou testes não confiáveis; código histórico pode não ser confiável.

**Sintaxe**

`git bisect start`

**Exemplo básico**

`git bisect start`

Inicie bisect em laboratório isolado limpo com commits bons e ruins conhecidos; marque-os separadamente.

**Exemplo profissional**

`git bisect good`

Após testar candidato selecionado com teste confiável repetível, marque good; use bad quando falhar.

**Impacto no estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / histórico: Condicional
- Repositório remoto: Inalterado
- Outros estados: Altera

**Resultado esperado:** Git seleciona candidatos, tipicamente destacados, até identificar limite ou relatar ambiguidade; reset retorna ao checkout original por padrão.

**Impactos e efeitos colaterais:** Bisect pode selecionar commits, atualizar index e arquivos e criar referências e metadados temporários; scripts de teste podem ter efeitos independentes.

**Erros comuns:** Marcar candidato sem testar ou deixar estado bisect ativo após investigação.

**Alternativas:** Use git log -G ou inspeção manual quando teste confiável não puder classificar revisões.

**Recuperação:** Salve resultado e trabalho desejado; execute git bisect reset e confira checkout original e status. Pare e inspecione se restauração falhar.

**Versão e dependências:** Sintaxe padrão Git; use Git 2.40 ou superior nos laboratórios do guia.

**Capítulos relacionados**

- [advanced-git/01-bisect](../../advanced-git/01-bisect/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-bisect>


---

<!-- navigation-footer -->
[Anterior](../09-recovery-and-stash/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../11-advanced-git-operations/README.pt-BR.md)
<!-- /navigation-footer -->
