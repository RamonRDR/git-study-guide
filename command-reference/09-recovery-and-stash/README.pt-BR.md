# 09 Recuperação e stash

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../08-remotes-and-synchronization/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../10-search-and-troubleshooting/README.pt-BR.md)
<!-- /navigation -->

Gerado a partir do JSON canônico. Edite os registros, não esta página.

As entradas descrevem comandos e operações, não uma sequência a executar. Pratique em repositórios descartáveis. Operações hospedadas são opcionais.

**Total de entradas distintas: 7**

- [`git reset`](#git-reset)
- [`git revert`](#git-revert)
- [`git reflog`](#git-reflog)
- [`git cherry-pick`](#git-cherry-pick)
- [`git stash push`](#git-stash-push)
- [`git stash apply`](#git-stash-apply)
- [`git stash pop`](#git-stash-pop)

## git-reset

**`git reset`**

**Tipo:** Comando nativo

**Nível:** Avançado

**Pesquisar por intenção:** Desfazer alterações, Reescrever histórico local, Retirar alterações do staging

**Risco:** Destrutivo. Escolha de modo importa: hard pode destruir trabalho local e todos modos por commit podem reescrever histórico. Mantenha exemplos privados e descartáveis.

**Finalidade:** Mover branch atual ou HEAD destacado para commit selecionado na forma por commit; escolher como index e working tree são afetados.

**Pré-requisitos:** Use repositório próprio descartável; inspecione status, referências selecionadas e identidade fictícia. Salve ponta original e trabalho não registrado valioso separadamente.

**Opções:** --soft mantém index e working tree; --mixed redefine index e mantém arquivos; --hard redefine ambos e pode sobrescrever ou remover caminhos não rastreados obstrutivos. Reset por caminho é diferente e não move HEAD.

**Quando utilizar:** Ao reorganizar intencionalmente commits privados com ponta salva e escolha explícita de modo.

**Quando evitar:** Evite redefinir histórico compartilhado ou usar --hard com trabalho não preservado. Nunca pratique no repositório do guia.

**Sintaxe**

`git reset --soft HEAD~1`

**Exemplo básico**

`git reset --soft HEAD~1`

Após salvar ponta privada, desfaça último commit mantendo index e arquivos; a ponta deve ter pai.

**Exemplo profissional**

`git reset --mixed HEAD~1`

Em branch privada descartável com ponta salva e sem trabalho não registrado valioso, volte um commit e revise diferenças agora não preparadas.

**Impacto no estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / histórico: Condicional
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** HEAD identifica commit selecionado; soft mantém conteúdo preparado, mixed ajusta index ao destino, hard ajusta conteúdo rastreado e index ao destino.

**Impactos e efeitos colaterais:** Pode mover referências e atualizar ORIG\_HEAD e reflogs; modo determina mudanças de index e arquivos. Não ocorre atualização remota.

**Erros comuns:** Confundir reset por caminho com movimento de branch ou esperar reflog recuperar edições não registradas descartadas.

**Alternativas:** Use git restore --staged para retirar caminho do staging; use git revert para desfazer commit compartilhado sem removê-lo do histórico.

**Recuperação:** Inspecione referências salvas e reflog; crie branch de recuperação na ponta antiga verificada se ainda existir. Trabalho não preparado ou não rastreado descartado pode ser irrecuperável.

**Versão e dependências:** Sintaxe padrão Git; use Git 2.40 ou superior nos laboratórios do guia. Configuração local confiável e hooks podem afetar execução.

**Capítulos relacionados**

- [history-and-recovery/01-recovery-safety](../../history-and-recovery/01-recovery-safety/README.pt-BR.md)
- [history-and-recovery/03-reset](../../history-and-recovery/03-reset/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-reset>

## git-revert

**`git revert`**

**Tipo:** Comando nativo

**Nível:** Intermediário

**Pesquisar por intenção:** Desfazer alterações, Proteger histórico

**Risco:** Alteração de estado. Mudanças inversas podem conflitar com trabalho posterior; revise resultado e testes. Reverter segredo não o apaga do histórico.

**Finalidade:** Criar novo commit revertendo mudanças introduzidas por commit selecionado.

**Pré-requisitos:** Use repositório próprio descartável; inspecione status, referências selecionadas e identidade fictícia. Salve ponta original e trabalho não registrado valioso separadamente.

**Opções:** --no-edit usa mensagem gerada; --no-commit prepara mudanças sem commit; reverter merge exige pai principal cuidadosamente escolhido com -m.

**Quando utilizar:** Ao corrigir mudança registrada preservando ancestralidade compartilhada.

**Quando evitar:** Evite reverter commit ou merge não revisado sem compreender dependências e efeitos em integrações futuras.

**Sintaxe**

`git revert HEAD`

**Exemplo básico**

`git revert HEAD`

Em branch de prática limpa, reverta último commit comum após verificá-lo.

**Exemplo profissional**

`git revert --no-edit HEAD`

Registre mudança inversa em branch local aprovada de correção; inspecione mensagem gerada e resultado.

**Impacto no estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / histórico: Condicional
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** Em execução comum bem-sucedida, novo commit de mudança inversa avança HEAD; commit original permanece no histórico. Conflitos podem pausar operação.

**Impactos e efeitos colaterais:** Pode alterar arquivos, index, objetos, referências e metadados de sequência; não ocorre push automático.

**Erros comuns:** Esperar desaparecimento do commit original ou repositório inteiro idêntico a snapshot anterior.

**Alternativas:** Use commit corretivo comum para correções seletivas; reset só para histórico privado cuidadosamente revisado.

**Recuperação:** Se operação pausar, inspecione status e use --continue correspondente após resolução revisada, ou --abort após preservar edições desejadas. Para operação concluída, avalie novo commit corretivo em vez de reescrever histórico compartilhado.

**Versão e dependências:** Sintaxe padrão Git; use Git 2.40 ou superior nos laboratórios do guia. Configuração local confiável e hooks podem afetar execução.

**Capítulos relacionados**

- [history-and-recovery/01-recovery-safety](../../history-and-recovery/01-recovery-safety/README.pt-BR.md)
- [history-and-recovery/04-revert](../../history-and-recovery/04-revert/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-revert>

## git-reflog

**`git reflog`**

**Tipo:** Comando nativo

**Nível:** Intermediário

**Pesquisar por intenção:** Recuperar trabalho, Inspecionar referências, Inspecionar histórico

**Risco:** Somente leitura. Somente inspeção de leitura; saída de reflog pode conter mensagens e identidades privadas. Recuperação não é garantida.

**Finalidade:** Inspecionar movimentos registrados localmente de referências para localizar IDs anteriores de commits.

**Pré-requisitos:** Use repositório próprio descartável; inspecione status, referências selecionadas e identidade fictícia. Salve ponta original e trabalho não registrado valioso separadamente.

**Opções:** Invocação padrão mostra reflog de HEAD; show com referência nomeada seleciona esse log. Expire e delete são operações modificadoras separadas não usadas aqui.

**Quando utilizar:** Ao investigar ponta anterior de branch após movimento local acidental de referência.

**Quando evitar:** Não presuma que toda referência tem reflog ou entradas persistem para sempre; não é backup de edições não preparadas.

**Sintaxe**

`git reflog show HEAD`

**Exemplo básico**

`git reflog`

Inspecione movimentos locais recentes de HEAD após reset de prática.

**Exemplo profissional**

`git reflog show main`

Investigue pontas anteriores da main do laboratório antes de escolher branch de recuperação.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Exibe movimentos registrados e IDs de commits associados onde logs existem; entradas podem expirar.

**Impactos e efeitos colaterais:** Inspeção mostrada não altera arquivos, index, referências, objetos ou remoto; logs pertencem ao repositório local.

**Erros comuns:** Presumir que HEAD@{1} sempre identifica commit desejado ou outro clone tem entradas idênticas.

**Alternativas:** Inspecione nomes de branches, tags ou backups salvos primeiro quando disponíveis.

**Recuperação:** Verifique candidato com git show e crie branch de recuperação no ID exato se disponível. Não redefina diretamente para posição presumida de reflog.

**Versão e dependências:** Sintaxe padrão Git; use Git 2.40 ou superior nos laboratórios do guia. Configuração local confiável e hooks podem afetar execução.

**Capítulos relacionados**

- [history-and-recovery/01-recovery-safety](../../history-and-recovery/01-recovery-safety/README.pt-BR.md)
- [history-and-recovery/05-reflog](../../history-and-recovery/05-reflog/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-reflog>

## git-cherry-pick

**`git cherry-pick`**

**Tipo:** Comando nativo

**Nível:** Intermediário

**Pesquisar por intenção:** Integrar alterações, Recuperar trabalho

**Risco:** Alteração de estado. Revise diff de origem, contexto de destino e dependências; reaplicação pode conflitar ou introduzir comportamento duplicado.

**Finalidade:** Aplicar mudanças introduzidas por commit selecionado à branch atual, normalmente criando novo commit.

**Pré-requisitos:** Use repositório próprio descartável; inspecione status, referências selecionadas e identidade fictícia. Salve ponta original e trabalho não registrado valioso separadamente.

**Opções:** -x registra ID de origem em mensagens de commit bem-sucedidas adequadas; --no-commit prepara mudanças sem commit. Merges exigem escolha de pai principal.

**Quando utilizar:** Ao transferir correção independente revisada sem integrar toda branch de origem.

**Quando evitar:** Evite selecionar commits sem conferir dependências ou duplicar mudanças já integradas.

**Sintaxe**

`git cherry-pick FIX_ID`

**Exemplo básico**

`git cherry-pick FIX_ID`

Substitua FIX\_ID pelo ID revisado de commit comum de outra branch local de prática.

**Exemplo profissional**

`git cherry-pick -x FIX_ID`

Em simulação local de backport, substitua ID de correção independente verificada e teste resultado.

**Impacto no estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / histórico: Condicional
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** Sucesso comum cria commit novo baseado em HEAD atual, tipicamente com ID diferente; conflitos ou mudanças vazias podem pausar ou exigir decisão.

**Impactos e efeitos colaterais:** Pode atualizar working tree, index, objetos, referências e estado de sequência; branch de origem não é movida.

**Erros comuns:** Presumir que cherry-pick mantém ancestralidade de origem ou inclui commits pré-requisitos automaticamente.

**Alternativas:** Use merge se toda ancestralidade de origem deve ser integrada; use correção revisada manualmente se mudança exige adaptação.

**Recuperação:** Se operação pausar, inspecione status e use --continue correspondente após resolução revisada, ou --abort após preservar edições desejadas. Para operação concluída, avalie novo commit corretivo em vez de reescrever histórico compartilhado.

**Versão e dependências:** Sintaxe padrão Git; use Git 2.40 ou superior nos laboratórios do guia. Configuração local confiável e hooks podem afetar execução.

**Capítulos relacionados**

- [history-and-recovery/01-recovery-safety](../../history-and-recovery/01-recovery-safety/README.pt-BR.md)
- [history-and-recovery/07-cherry-pick](../../history-and-recovery/07-cherry-pick/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-cherry-pick>

## git-stash-push

**`git stash push`**

**Tipo:** Subcomando

**Nível:** Intermediário

**Pesquisar por intenção:** Guardar trabalho temporariamente, Trocar contexto de trabalho

**Risco:** Alteração de estado. Stash é armazenamento temporário local, não backup. Aplicar pode gerar conflitos; revise status e preserve trabalho valioso antes de alterar estado.

**Finalidade:** Salvar modificações locais selecionadas em entrada de stash e reverter mudanças correspondentes de trabalho e index em direção a HEAD.

**Pré-requisitos:** Use repositório próprio descartável com commit existente; revise status, lista de stash e entrada pretendida. Preserve trabalho valioso separadamente.

**Opções:** -m nomeia entrada; -u inclui arquivos não rastreados mas não ignorados; -a inclui ignorados também e não é usado aqui. --keep-index mantém mudanças preparadas no estado de trabalho.

**Quando utilizar:** Ao guardar temporariamente trabalho inacabado em contexto local controlado.

**Quando evitar:** Evite depender do stash como única cópia de trabalho importante ou guardar arquivos sensíveis.

**Sintaxe**

`git stash push -m "draft notes"`

**Exemplo básico**

`git stash push -m "draft notes"`

Guarde edições rastreadas de prática temporariamente.

**Exemplo profissional**

`git stash push -u -m "review draft"`

Após conferir arquivos sensíveis, inclua também rascunho fictício não rastreado pretendido.

**Impacto no estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / histórico: Condicional
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** Se mudanças correspondentes existem, entrada de stash é registrada; mudanças selecionadas são removidas do estado de trabalho conforme opções. Arquivos não rastreados permanecem salvo inclusão.

**Impactos e efeitos colaterais:** Pode criar objetos de commit locais e atualizar refs/stash e reflog, index e arquivos; ponta atual e remoto ficam inalterados.

**Erros comuns:** Presumir stash padrão inclui arquivos não rastreados e ignorados ou status limpo prova que todo arquivo desejado foi salvo.

**Alternativas:** Use branch temporária privada com commit revisado para trabalho que exige referência nomeada mais durável.

**Recuperação:** Inspecione git stash list e git stash show; use apply na entrada verificada antes de removê-la. Objetos ausentes ou expirados podem não ser recuperáveis.

**Versão e dependências:** Sintaxe padrão Git; use Git 2.40 ou superior nos laboratórios do guia. Configuração local confiável e hooks podem afetar execução.

**Capítulos relacionados**

- [history-and-recovery/01-recovery-safety](../../history-and-recovery/01-recovery-safety/README.pt-BR.md)
- [history-and-recovery/06-stash](../../history-and-recovery/06-stash/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-stash>

## git-stash-apply

**`git stash apply`**

**Tipo:** Subcomando

**Nível:** Intermediário

**Pesquisar por intenção:** Guardar trabalho temporariamente, Recuperar trabalho

**Risco:** Alteração de estado. Stash é armazenamento temporário local, não backup. Aplicar pode gerar conflitos; revise status e preserve trabalho valioso antes de alterar estado.

**Finalidade:** Reaplicar entrada de stash selecionada sem removê-la da lista de stash.

**Pré-requisitos:** Use repositório próprio descartável com commit existente; revise status, lista de stash e entrada pretendida. Preserve trabalho valioso separadamente.

**Opções:** --index também tenta restaurar estado preparado; informe entrada verificada explicitamente. Sem --index, divisão original de staging não é garantida.

**Quando utilizar:** Ao restaurar trabalho guardado mantendo cópia da entrada de stash para verificação.

**Quando evitar:** Evite aplicar sobre mudanças não registradas valiosas ou selecionar entrada por posição sem verificar.

**Sintaxe**

`git stash apply "stash@{0}"`

**Exemplo básico**

`git stash apply "stash@{0}"`

Inspecione list e show antes, depois aplique última entrada de prática verificada em checkout limpo.

**Exemplo profissional**

`git stash apply --index "stash@{0}"`

Em branch de laboratório limpa compatível, tente restaurar trabalho preparado e não preparado e inspecione diferenças.

**Impacto no estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / histórico: Condicional
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** Aplica mudanças salvas ao estado de trabalho quando possível; pode conflitar. Entrada de stash permanece disponível após apply comum.

**Impactos e efeitos colaterais:** Pode atualizar working tree, index e metadados de conflito; referência de stash não é removida e ponta da branch atual não avança.

**Erros comuns:** Presumir apply remove entrada ou --index sempre restaura index exato apesar de conflitos.

**Alternativas:** Use pop só quando aplicação bem-sucedida também deve remover entrada; prefira apply ao verificar trabalho recuperado.

**Recuperação:** Se aplicação conflitar, inspecione caminhos não mesclados e stash preservado; preserve resolução antes de limpar. Não há stash abort genérico; evite reset às cegas ou reaplicação repetida.

**Versão e dependências:** Sintaxe padrão Git; use Git 2.40 ou superior nos laboratórios do guia. Configuração local confiável e hooks podem afetar execução.

**Capítulos relacionados**

- [history-and-recovery/01-recovery-safety](../../history-and-recovery/01-recovery-safety/README.pt-BR.md)
- [history-and-recovery/06-stash](../../history-and-recovery/06-stash/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-stash>

## git-stash-pop

**`git stash pop`**

**Tipo:** Subcomando

**Nível:** Intermediário

**Pesquisar por intenção:** Guardar trabalho temporariamente, Recuperar trabalho

**Risco:** Destrutivo. Pop pode remover acesso nomeado ao trabalho salvo em sucesso. Mantenha cópia independente ou prefira apply em dúvida.

**Finalidade:** Reaplicar entrada de stash e removê-la da lista apenas quando aplicação tiver sucesso.

**Pré-requisitos:** Use repositório próprio descartável com commit existente; revise status, lista de stash e entrada pretendida. Preserve trabalho valioso separadamente.

**Opções:** --index tenta restaurar estado preparado também; informe entrada verificada. git stash drop remove entrada sem aplicar e exige revisão separada.

**Quando utilizar:** Ao retomar mudança temporária verificada cuja cópia de stash não é mais necessária após sucesso.

**Quando evitar:** Evite quando stash é única cópia de trabalho importante ou destino já tem mudanças não preservadas.

**Sintaxe**

`git stash pop "stash@{0}"`

**Exemplo básico**

`git stash pop "stash@{0}"`

Após verificar stash descartável e destino limpo, retome trabalho e inspecione status e lista de stash.

**Exemplo profissional**

`git stash pop --index "stash@{0}"`

Restaure entrada temporária revisada de laboratório incluindo estado de staging e confirme resultado antes de continuar.

**Impacto no estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / histórico: Condicional
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** Aplicação bem-sucedida remove entrada selecionada; conflito a preserva para revisão, com possíveis mudanças parciais no checkout.

**Impactos e efeitos colaterais:** Pode alterar working tree, index, refs/stash e reflog; ponta da branch e remoto não mudam na operação normal.

**Erros comuns:** Presumir stash removido após conflito ou pop bem-sucedido deixa entrada reutilizável na mesma posição.

**Alternativas:** Prefira apply, inspecione mudanças restauradas e mantenha entrada até estar satisfeito; só então considere drop verificado.

**Recuperação:** Se conflito ocorrer, confirme entrada preservada e inspecione caminhos não mesclados. Após sucesso, preserve trabalho restaurado prontamente; recuperação de entrada removida por objetos restantes não é garantida.

**Versão e dependências:** Sintaxe padrão Git; use Git 2.40 ou superior nos laboratórios do guia. Configuração local confiável e hooks podem afetar execução.

**Capítulos relacionados**

- [history-and-recovery/01-recovery-safety](../../history-and-recovery/01-recovery-safety/README.pt-BR.md)
- [history-and-recovery/06-stash](../../history-and-recovery/06-stash/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-stash>


---

<!-- navigation-footer -->
[Anterior](../08-remotes-and-synchronization/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../10-search-and-troubleshooting/README.pt-BR.md)
<!-- /navigation-footer -->
