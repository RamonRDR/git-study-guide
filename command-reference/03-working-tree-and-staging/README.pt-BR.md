# 03 Working tree e staging

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../02-repository-inspection/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../04-commits-and-tags/README.pt-BR.md)
<!-- /navigation -->

Gerado a partir do JSON canônico. Edite os registros, não esta página.

As entradas descrevem comandos e operações, não uma sequência a executar. Pratique em repositórios descartáveis. Operações hospedadas são opcionais.

**Total de entradas distintas: 10**

- [`git add`](#git-add)
- [`git add -A`](#git-add-all)
- [`git add -u`](#git-add-update)
- [`git add -p`](#git-add-patch)
- [`git restore`](#git-restore)
- [`git restore --staged`](#git-restore-staged)
- [`git rm`](#git-rm)
- [`git rm --cached`](#git-rm-cached)
- [`git mv`](#git-mv)
- [`git clean -n`](#git-clean-dry-run)

## git-add

**`git add`**

**Tipo:** Comando nativo

**Nível:** Iniciante

**Pesquisar por intenção:** Preparar alterações

**Risco:** Alteração de estado. Revise caminhos exatos e mudanças preparadas; não opere no repositório do guia.

**Finalidade:** Preparar caminhos selecionados para o próximo commit.

**Pré-requisitos:** Use repositório próprio descartável; inspecione git status primeiro e proteja trabalho valioso.

**Opções:** -- encerra opções; especifique um ou mais caminhos.

**Quando utilizar:** Após inspecionar mudanças que deseja commitar.

**Quando evitar:** Não prepare credenciais ou mudanças alheias.

**Sintaxe**

`git add -- path`

**Exemplo básico**

`git add -- notes.txt`

Revise arquivo fictício de notas antes de prepará-lo.

**Exemplo profissional**

`git add -- src/main.py`

Prepare apenas o arquivo fonte revisado para commit focado.

**Impacto no estado**

- Working tree: Inalterado
- Index: Altera
- Objetos / refs / histórico: Condicional
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Entradas do index refletem conteúdo ou exclusões selecionadas.

**Impactos e efeitos colaterais:** Atualiza index e pode armazenar blobs; sem commit ou atualização remota.

**Erros comuns:** Presumir que edições posteriores entram automaticamente no staging.

**Alternativas:** Use git add -p para selecionar trechos.

**Recuperação:** Inspecione git diff --cached depois. Retire mudanças indesejadas do staging com git restore --staged no Git 2.23+ quando HEAD existir; preserve arquivos de trabalho.

**Versão e dependências:** Sem ferramenta opcional; o exemplo usa sintaxe padrão Git.

**Capítulos relacionados**

- [basic-commands/02-status-add-commit](../../basic-commands/02-status-add-commit/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-add>

## git-add-all

**`git add -A`**

**Tipo:** Uso de opção

**Nível:** Iniciante

**Pesquisar por intenção:** Preparar alterações

**Risco:** Alteração de estado. Revise caminhos exatos e mudanças preparadas; não opere no repositório do guia.

**Finalidade:** Preparar adições, modificações e remoções no escopo selecionado.

**Pré-requisitos:** Use repositório próprio descartável; inspecione git status primeiro e proteja trabalho valioso.

**Opções:** -A atualiza todas as entradas correspondentes; pathspec restringe escopo.

**Quando utilizar:** Quando todas as mudanças de um escopo deliberado pertencem juntas.

**Quando evitar:** Evite staging amplo quando houver arquivos alheios ou sensíveis.

**Sintaxe**

`git add -A [-- pathspec]`

**Exemplo básico**

`git add -A`

Em lab de escopo claro, inspecione mudanças antes de prepará-las juntas.

**Exemplo profissional**

`git add -A -- src`

Limite staging amplo ao diretório src revisado.

**Impacto no estado**

- Working tree: Inalterado
- Index: Altera
- Objetos / refs / histórico: Condicional
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Caminhos novos, modificados e excluídos no escopo são preparados, sujeitos a ignore.

**Impactos e efeitos colaterais:** Atualiza index e pode gravar objetos; mantém arquivos de trabalho.

**Erros comuns:** Esquecer que exclusões e arquivos novos podem ser incluídos.

**Alternativas:** Use caminhos explícitos ou git add -p para escopo fino.

**Recuperação:** Inspecione git diff --cached depois. Retire mudanças indesejadas do staging com git restore --staged no Git 2.23+ quando HEAD existir; preserve arquivos de trabalho.

**Versão e dependências:** Sem ferramenta opcional; o exemplo usa sintaxe padrão Git.

**Capítulos relacionados**

- [basic-commands/02-status-add-commit](../../basic-commands/02-status-add-commit/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-add>

## git-add-update

**`git add -u`**

**Tipo:** Uso de opção

**Nível:** Intermediário

**Pesquisar por intenção:** Preparar alterações

**Risco:** Alteração de estado. Revise caminhos exatos e mudanças preparadas; não opere no repositório do guia.

**Finalidade:** Preparar modificações e exclusões de caminhos já indexados sem adicionar novos não rastreados.

**Pré-requisitos:** Use repositório próprio descartável; inspecione git status primeiro e proteja trabalho valioso.

**Opções:** -u atualiza entradas rastreadas; pathspec limita escopo opcionalmente.

**Quando utilizar:** Ao atualizar apenas arquivos rastreados existentes.

**Quando evitar:** Não use quando arquivos novos necessários precisarem entrar automaticamente.

**Sintaxe**

`git add -u [-- pathspec]`

**Exemplo básico**

`git add -u`

Modifique arquivo rastreado e crie outro não rastreado; prepare só mudanças rastreadas.

**Exemplo profissional**

`git add -u -- src`

Prepare mudanças rastreadas em src sem adicionar gerados não rastreados.

**Impacto no estado**

- Working tree: Inalterado
- Index: Altera
- Objetos / refs / histórico: Condicional
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Modificações e remoções rastreadas são preparadas; novos caminhos não rastreados permanecem assim.

**Impactos e efeitos colaterais:** Altera index e pode gravar blobs, não commits.

**Erros comuns:** Omitir arquivo de dependência novo ou preparar exclusões rastreadas por engano.

**Alternativas:** Use git add -A se também incluir caminhos novos deliberadamente.

**Recuperação:** Inspecione git diff --cached depois. Retire mudanças indesejadas do staging com git restore --staged no Git 2.23+ quando HEAD existir; preserve arquivos de trabalho.

**Versão e dependências:** Sem ferramenta opcional; o exemplo usa sintaxe padrão Git.

**Capítulos relacionados**

- [basic-commands/02-status-add-commit](../../basic-commands/02-status-add-commit/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-add>

## git-add-patch

**`git add -p`**

**Tipo:** Uso de opção

**Nível:** Intermediário

**Pesquisar por intenção:** Preparar alterações

**Risco:** Alteração de estado. Revise caminhos exatos e mudanças preparadas; não opere no repositório do guia.

**Finalidade:** Selecionar interativamente trechos do diff para staging.

**Pré-requisitos:** Use repositório próprio descartável; inspecione git status primeiro e proteja trabalho valioso.

**Opções:** -p abre seleção interativa; ações disponíveis aparecem no prompt.

**Quando utilizar:** Quando um arquivo contém mudanças de commits distintos.

**Quando evitar:** Evite confirmação cega; trechos relacionados podem depender uns dos outros.

**Sintaxe**

`git add -p [-- pathspec]`

**Exemplo básico**

`git add -p -- notes.txt`

Edite duas linhas independentes e escolha um trecho quando Git os separar.

**Exemplo profissional**

`git add -p -- src/main.py`

Separe correção de bug de refatoração alheia em arquivo revisado.

**Impacto no estado**

- Working tree: Inalterado
- Index: Altera
- Objetos / refs / histórico: Condicional
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Somente mudanças aceitas entram no index; restantes ficam fora do staging.

**Impactos e efeitos colaterais:** Atualiza conteúdo selecionado do index; arquivo de trabalho permanece.

**Erros comuns:** Preparar metade de mudança dependente ou presumir que trecho selecionado é commit testado.

**Alternativas:** Use caminhos explícitos para arquivos inteiros ou separe trabalho em arquivos.

**Recuperação:** Inspecione git diff --cached depois. Retire mudanças indesejadas do staging com git restore --staged no Git 2.23+ quando HEAD existir; preserve arquivos de trabalho.

**Versão e dependências:** Sem ferramenta opcional; o exemplo usa sintaxe padrão Git.

**Capítulos relacionados**

- [basic-commands/02-status-add-commit](../../basic-commands/02-status-add-commit/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-add>

## git-restore

**`git restore`**

**Tipo:** Comando nativo

**Nível:** Iniciante

**Pesquisar por intenção:** Desfazer alterações

**Risco:** Destrutivo. Pode remover ou sobrescrever arquivos. Use apenas dados descartáveis e faça backup prévio do que for valioso.

**Finalidade:** Restaurar caminho da working tree a partir do index por padrão, descartando diferenças fora do staging.

**Pré-requisitos:** Use repositório próprio descartável; inspecione git status primeiro e proteja trabalho valioso.

**Opções:** --source seleciona árvore explícita; -- encerra opções.

**Quando utilizar:** Somente quando edições não preparadas inspecionadas forem indesejadas.

**Quando evitar:** Não descarte trabalho sem commit que possa precisar; salve antes separadamente.

**Sintaxe**

`git restore [--source=tree] -- path`

**Exemplo básico**

`git restore -- notes.txt`

Em lab descartável, descarte edição intencionalmente indesejada de notas rastreadas.

**Exemplo profissional**

`git restore -- src/main.py`

Após revisar e salvar mudanças, restaure só edição indesejada do fonte em clone descartável.

**Impacto no estado**

- Working tree: Altera
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Caminho selecionado corresponde à fonte; padrão preserva conteúdo preparado.

**Impactos e efeitos colaterais:** Pode sobrescrever ou remover arquivos; não move HEAD nem altera index neste uso.

**Erros comuns:** Confundir fonte padrão com HEAD quando staging difere.

**Alternativas:** Salve patch ou backup antes de descartar; use git restore --staged para retirar do staging.

**Recuperação:** Edições fora do staging podem nunca ter entrado no Git; use backup ou histórico do editor se disponível. Recuperação não é garantida.

**Versão e dependências:** git restore requer Git 2.23 ou posterior.

**Capítulos relacionados**

- [history-and-recovery/02-restore](../../history-and-recovery/02-restore/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-restore>

## git-restore-staged

**`git restore --staged`**

**Tipo:** Uso de opção

**Nível:** Iniciante

**Pesquisar por intenção:** Retirar alterações do staging

**Risco:** Alteração de estado. Revise caminhos exatos e mudanças preparadas; não opere no repositório do guia.

**Finalidade:** Restaurar entrada selecionada do index a partir de HEAD por padrão preservando arquivos de trabalho.

**Pré-requisitos:** Use repositório próprio descartável; inspecione git status primeiro e proteja trabalho valioso.

**Opções:** --staged seleciona index; fonte padrão HEAD; use -- para caminhos.

**Quando utilizar:** Quando existe commit e caminho foi preparado prematuramente.

**Quando evitar:** Não combine com --worktree sem intenção de sobrescrever arquivos também.

**Sintaxe**

`git restore --staged -- path`

**Exemplo básico**

`git restore --staged -- notes.txt`

Retire arquivo rastreado do staging após primeiro commit.

**Exemplo profissional**

`git restore --staged -- src/main.py`

Retire mudança alheia do fonte do commit pendente sem descartar edição.

**Impacto no estado**

- Working tree: Inalterado
- Index: Altera
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Entradas selecionadas correspondem a HEAD; edições de trabalho permanecem.

**Impactos e efeitos colaterais:** Altera apenas index neste uso; não move refs.

**Erros comuns:** Usar fonte HEAD antes do primeiro commit; presumir reconstrução garantida do staging parcial.

**Alternativas:** Use git reset HEAD -- path com HEAD existente em Git antigo.

**Recuperação:** Revise diff de trabalho e prepare mudanças novamente; conteúdo anterior só no staging pode exigir backup.

**Versão e dependências:** git restore requer Git 2.23 ou posterior.

**Capítulos relacionados**

- [history-and-recovery/02-restore](../../history-and-recovery/02-restore/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-restore>

## git-rm

**`git rm`**

**Tipo:** Comando nativo

**Nível:** Iniciante

**Pesquisar por intenção:** Gerenciar arquivos

**Risco:** Destrutivo. Pode remover ou sobrescrever arquivos. Use apenas dados descartáveis e faça backup prévio do que for valioso.

**Finalidade:** Remover caminho rastreado da working tree e preparar sua exclusão.

**Pré-requisitos:** Use repositório próprio descartável; inspecione git status primeiro e proteja trabalho valioso.

**Opções:** -r permite remoção recursiva; --cached remove só index; não force ignorando proteções.

**Quando utilizar:** Quando arquivo rastreado revisado deve ser removido no próximo commit.

**Quando evitar:** Não remova mudanças locais valiosas; evite -f na prática comum.

**Sintaxe**

`git rm -- path`

**Exemplo básico**

`git rm -- old.txt`

Remova texto obsoleto commitado em repositório descartável.

**Exemplo profissional**

`git rm -- src/obsolete.py`

Prepare exclusão de módulo obsoleto revisado em clone descartável.

**Impacto no estado**

- Working tree: Altera
- Index: Altera
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Arquivo rastreado ausente e exclusão preparada se operação for bem-sucedida.

**Impactos e efeitos colaterais:** Altera working tree e index; commits anteriores permanecem.

**Erros comuns:** Presumir que git rm apaga cópias commitadas anteriores do histórico.

**Alternativas:** Use git rm --cached para manter arquivo e remover rastreamento.

**Recuperação:** Se exclusão não foi commitada e HEAD contém arquivo desejado, restaure index e cópia de trabalho explicitamente de HEAD após inspeção; outras edições perdidas podem ser irrecuperáveis.

**Versão e dependências:** Sem ferramenta opcional; o exemplo usa sintaxe padrão Git.

**Capítulos relacionados**

- [basic-commands/04-move-and-remove](../../basic-commands/04-move-and-remove/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-rm>

## git-rm-cached

**`git rm --cached`**

**Tipo:** Uso de opção

**Nível:** Intermediário

**Pesquisar por intenção:** Ignorar arquivos

**Risco:** Alteração de estado. Revise caminhos exatos e mudanças preparadas; não opere no repositório do guia.

**Finalidade:** Remover caminho do rastreamento mantendo cópia de trabalho.

**Pré-requisitos:** Use repositório próprio descartável; inspecione git status primeiro e proteja trabalho valioso.

**Opções:** --cached seleciona só index; -r necessário para remover diretório recursivamente.

**Quando utilizar:** Quando arquivo gerado não sensível já rastreado deve deixar de ser rastreado.

**Quando evitar:** Não use como procedimento de remoção de segredo; commits anteriores ainda contêm arquivo.

**Sintaxe**

`git rm --cached -- path`

**Exemplo básico**

`git rm --cached -- notes.tmp`

Pare de rastrear arquivo temporário inofensivo commitado e inspecione status.

**Exemplo profissional**

`git rm --cached -- local-settings.txt`

Mantenha fixture inofensiva de configuração local em disco enquanto prepara remoção do rastreamento.

**Impacto no estado**

- Working tree: Inalterado
- Index: Altera
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Arquivo permanece; remoção rastreada entra no staging quando HEAD contém caminho.

**Impactos e efeitos colaterais:** Altera index; sem mudança imediata remota ou de histórico commitado.

**Erros comuns:** Adicionar só regra de ignore esperando arquivo já rastreado parar de ser rastreado.

**Alternativas:** Use regra de ignore adequada para futuras cópias não rastreadas; use git rm comum se pretende excluir arquivo.

**Recuperação:** Antes de commitar, inspecione remoção preparada e adicione arquivo novamente se apropriado; conteúdo anterior só no staging pode exigir backup.

**Versão e dependências:** Sem ferramenta opcional; o exemplo usa sintaxe padrão Git.

**Capítulos relacionados**

- [basic-commands/05-ignore-and-review](../../basic-commands/05-ignore-and-review/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-rm>

## git-mv

**`git mv`**

**Tipo:** Comando nativo

**Nível:** Iniciante

**Pesquisar por intenção:** Gerenciar arquivos

**Risco:** Alteração de estado. Revise caminhos exatos e mudanças preparadas; não opere no repositório do guia.

**Finalidade:** Mover ou renomear caminho e atualizar index correspondentemente.

**Pré-requisitos:** Use repositório próprio descartável; inspecione git status primeiro e proteja trabalho valioso.

**Opções:** -- encerra opções; -n simula; evite -f sobrescrevendo destino.

**Quando utilizar:** Ao renomear arquivo rastreado em mudança focada.

**Quando evitar:** Não sobrescreva destino existente nem ignore referências dependentes.

**Sintaxe**

`git mv -- source destination`

**Exemplo básico**

`git mv -- old.txt new.txt`

Renomeie notas commitadas para nome novo não utilizado.

**Exemplo profissional**

`git mv -- src/old.py src/new.py`

Renomeie módulo ilustrativo e revise separadamente imports e testes dependentes.

**Impacto no estado**

- Working tree: Altera
- Index: Altera
- Objetos / refs / histórico: Condicional
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Caminho antigo removido e novo existente; index atualizado; exibição de rename depende de detecção.

**Impactos e efeitos colaterais:** Atualiza caminhos de trabalho e index; Git commita snapshots, não registros explícitos de rename.

**Erros comuns:** Presumir atualização automática de imports ou links de documentação.

**Alternativas:** Mova com ferramentas do sistema e prepare caminhos antigo e novo explicitamente.

**Recuperação:** Inspecione status; reverta rename não commitado com movimento inverso explícito se seguro e destino livre.

**Versão e dependências:** Sem ferramenta opcional; o exemplo usa sintaxe padrão Git.

**Capítulos relacionados**

- [basic-commands/04-move-and-remove](../../basic-commands/04-move-and-remove/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-mv>

## git-clean-dry-run

**`git clean -n`**

**Tipo:** Uso de opção

**Nível:** Intermediário

**Pesquisar por intenção:** Inspecionar arquivos

**Risco:** Somente leitura. Somente simulação; nunca execute variante destrutiva automaticamente.

**Finalidade:** Pré-visualizar caminhos não rastreados que operação clean correspondente removeria.

**Pré-requisitos:** Use repositório próprio descartável; inspecione git status primeiro e proteja trabalho valioso.

**Opções:** -n simula; -d inclui diretórios não rastreados; ignorados normalmente excluídos.

**Quando utilizar:** Antes de considerar limpeza de artefatos descartáveis não rastreados.

**Quando evitar:** Não substitua -n por flag destrutiva sem backup e revisão de escopo separados.

**Sintaxe**

`git clean -n [-d]`

**Exemplo básico**

`git clean -n`

Simule limpeza com arquivo não rastreado inofensivo em lab descartável.

**Exemplo profissional**

`git clean -nd`

Simule diretórios não rastreados em clone descartável antes de decidir sobre limpeza.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Lista candidatos à remoção sem excluí-los.

**Impactos e efeitos colaterais:** Sem remoção no modo de simulação; sem mutação de index ou refs.

**Erros comuns:** Presumir que simulação permanece válida após mudanças em arquivos ou ignore.

**Alternativas:** Use git ls-files --others --exclude-standard para inspecionar não rastreados.

**Recuperação:** Simulação não exige recuperação; exclusão real de não rastreados pode ser irrecuperável sem backup.

**Versão e dependências:** Sem ferramenta opcional; o exemplo usa sintaxe padrão Git.

**Capítulos relacionados**

- [history-and-recovery/01-recovery-safety](../../history-and-recovery/01-recovery-safety/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-clean>


---

<!-- navigation-footer -->
[Anterior](../02-repository-inspection/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../04-commits-and-tags/README.pt-BR.md)
<!-- /navigation-footer -->
