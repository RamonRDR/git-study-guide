# 07 Merge, rebase e conflitos

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../06-branch-management/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../08-remotes-and-synchronization/README.pt-BR.md)
<!-- /navigation -->

Gerado a partir do JSON canônico. Edite os registros, não esta página.

As entradas descrevem comandos e operações, não uma sequência a executar. Pratique em repositórios descartáveis. Operações hospedadas são opcionais.

**Total de entradas distintas: 10**

- [`git merge`](#git-merge)
- [`git merge --ff-only`](#git-merge-ff-only)
- [`git merge --no-ff`](#git-merge-no-ff)
- [`git merge --squash`](#git-merge-squash)
- [`git merge --abort`](#git-merge-abort)
- [`git merge --continue`](#git-merge-continue)
- [`git rebase`](#git-rebase)
- [`git rebase -i`](#git-rebase-interactive)
- [`git rebase --continue`](#git-rebase-continue)
- [`git rebase --abort`](#git-rebase-abort)

## git-merge

**`git merge`**

**Tipo:** Comando nativo

**Nível:** Intermediário

**Pesquisar por intenção:** Integrar alterações

**Risco:** Alteração de estado. Integração pode gerar conflitos ou alterar a ponta atual; verifique destino e revise diff resultante e testes antes de compartilhar.

**Finalidade:** Integrar mudanças de outra revisão à branch atual.

**Pré-requisitos:** Use repositório próprio descartável, status limpo, referências verificadas e identidade fictícia. Salve a ponta original antes da integração.

**Opções:** --ff-only recusa integração não fast-forward; --no-ff solicita commit de merge quando integração é necessária.

**Quando utilizar:** Ao incorporar trabalho revisado de branch ao destino local selecionado.

**Quando evitar:** Evite integrar com edições não registradas valiosas, referências desconhecidas ou operações inacabadas.

**Sintaxe**

`git merge feature`

**Exemplo básico**

`git merge feature`

Na main limpa, integre branch local de prática existente.

**Exemplo profissional**

`git merge feat/docs`

Após verificar destino local e branch revisada de documentação, integre e teste.

**Impacto no estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / histórico: Condicional
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** Pode informar que já está atualizado, avançar por fast-forward, criar commit de merge ou pausar por conflitos, conforme ancestralidade e configuração.

**Impactos e efeitos colaterais:** Pode atualizar arquivos, index, referência atual, objetos e metadados de merge; não implica atualização remota.

**Erros comuns:** Executar na branch de origem em vez do destino ou presumir que merge sempre cria commit.

**Alternativas:** Use --ff-only quando só avanço linear for permitido; use rebase só sob política de histórico adequada.

**Recuperação:** Inspecione status e ponta salva. Se a operação estiver pausada, use o comando abort correspondente quando apropriado. Após conclusão, escolha recuperação conforme histórico compartilhado; não use reset às cegas.

**Versão e dependências:** Sintaxe padrão Git; use a base de laboratório do guia, Git 2.40 ou superior. Editor confiável e hooks locais podem afetar execução.

**Capítulos relacionados**

- [merge-and-conflicts/01-integration-safety](../../merge-and-conflicts/01-integration-safety/README.pt-BR.md)
- [merge-and-conflicts/03-merge-commit](../../merge-and-conflicts/03-merge-commit/README.pt-BR.md)
- [merge-and-conflicts/04-conflict-resolution](../../merge-and-conflicts/04-conflict-resolution/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-merge>

## git-merge-ff-only

**`git merge --ff-only`**

**Tipo:** Uso de opção

**Nível:** Iniciante

**Pesquisar por intenção:** Integrar alterações, Proteger histórico

**Risco:** Alteração de estado. Integração pode gerar conflitos ou alterar a ponta atual; verifique destino e revise diff resultante e testes antes de compartilhar.

**Finalidade:** Integrar apenas se ponta atual puder avançar sem commit de merge ou já estiver atualizada.

**Pré-requisitos:** Use repositório próprio descartável, status limpo, referências verificadas e identidade fictícia. Salve a ponta original antes da integração.

**Opções:** --ff-only recusa integração que exige commit de merge.

**Quando utilizar:** Ao exigir caminho linear de integração sem reescrever commits.

**Quando evitar:** Não use esperando conciliação automática de históricos divergentes.

**Sintaxe**

`git merge --ff-only feature`

**Exemplo básico**

`git merge --ff-only feature`

Integre branch local descendente da main estando na main.

**Exemplo profissional**

`git merge --ff-only feat/docs`

Exija integração local linear após conferir ancestralidade.

**Impacto no estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / histórico: Condicional
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** Avança referência atual até ponta da origem quando possível, mantém se já contida ou recusa divergência.

**Impactos e efeitos colaterais:** Pode atualizar arquivos, index e referência atual; nenhum commit de merge novo é criado.

**Erros comuns:** Tratar recusa como motivo para forçar ou redefinir branch.

**Alternativas:** Inspecione divergência e escolha merge revisado ou rebase privado conforme política.

**Recuperação:** Se recusado, inspecione ancestralidade e status; se avançou incorretamente, use ponta original salva para avaliar recuperação sem sobrescrever histórico compartilhado.

**Versão e dependências:** Sintaxe padrão Git; use a base de laboratório do guia, Git 2.40 ou superior. Editor confiável e hooks locais podem afetar execução.

**Capítulos relacionados**

- [merge-and-conflicts/02-fast-forward](../../merge-and-conflicts/02-fast-forward/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-merge>

## git-merge-no-ff

**`git merge --no-ff`**

**Tipo:** Uso de opção

**Nível:** Intermediário

**Pesquisar por intenção:** Integrar alterações

**Risco:** Alteração de estado. Integração pode gerar conflitos ou alterar a ponta atual; verifique destino e revise diff resultante e testes antes de compartilhar.

**Finalidade:** Preservar limite explícito de merge mesmo quando fast-forward seria possível.

**Pré-requisitos:** Use repositório próprio descartável, status limpo, referências verificadas e identidade fictícia. Salve a ponta original antes da integração.

**Opções:** --no-ff solicita commit de merge quando mudanças precisam de integração; -m fornece mensagem.

**Quando utilizar:** Quando política da equipe exige commit explícito de integração.

**Quando evitar:** Evite em branches que exigem histórico estritamente linear.

**Sintaxe**

`git merge --no-ff feature`

**Exemplo básico**

`git merge --no-ff feature`

Integre branch de prática não contida com limite explícito de merge.

**Exemplo profissional**

`git merge --no-ff -m "Merge documentation" feat/docs`

Registre integração revisada onde commits de merge são permitidos.

**Impacto no estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / histórico: Condicional
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** Em integração bem-sucedida de branch única não contida, cria commit com dois pais; histórico já contido pode ficar igual.

**Impactos e efeitos colaterais:** Pode atualizar working tree, index, objetos e referência; conflitos podem pausar antes de criar commit.

**Erros comuns:** Esperar commit de merge mesmo quando nada precisa ser integrado.

**Alternativas:** Use --ff-only para avanço linear ou fluxo squash revisado quando política exige um commit novo sem ancestralidade de merge.

**Recuperação:** Inspecione status e ponta salva. Se a operação estiver pausada, use o comando abort correspondente quando apropriado. Após conclusão, escolha recuperação conforme histórico compartilhado; não use reset às cegas.

**Versão e dependências:** Sintaxe padrão Git; use a base de laboratório do guia, Git 2.40 ou superior. Editor confiável e hooks locais podem afetar execução.

**Capítulos relacionados**

- [merge-and-conflicts/03-merge-commit](../../merge-and-conflicts/03-merge-commit/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-merge>

## git-merge-squash

**`git merge --squash`**

**Tipo:** Uso de opção

**Nível:** Intermediário

**Pesquisar por intenção:** Integrar alterações, Preparar alterações

**Risco:** Alteração de estado. Revise resultado preparado completo antes do commit; commits de origem podem continuar fora da ancestralidade do destino.

**Finalidade:** Preparar mudanças combinadas de outra branch sem mover HEAD ou registrar ancestralidade de merge.

**Pré-requisitos:** Use repositório próprio descartável, status limpo, referências verificadas e identidade fictícia. Salve a ponta original antes da integração.

**Opções:** --squash prepara resultado de integração; git commit separado registra snapshot preparado.

**Quando utilizar:** Quando integração local revisada deve se tornar um commit comum.

**Quando evitar:** Evite quando for necessário preservar ancestralidade da origem ou index contém edições alheias.

**Sintaxe**

`git merge --squash feature`

**Exemplo básico**

`git merge --squash feature`

Prepare mudanças combinadas de branch de prática existente, depois inspecione antes do commit.

**Exemplo profissional**

`git merge --squash feat/docs`

Prepare documentação revisada para commit único posterior; verifique diff e testes.

**Impacto no estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / histórico: Condicional
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** Em sucesso limpo, working tree e index refletem resultado combinado enquanto HEAD não muda; conflitos podem exigir resolução.

**Impactos e efeitos colaterais:** Não define MERGE\_HEAD; commit comum posterior tem um pai. Objetos locais ou metadados de squash podem ser criados.

**Erros comuns:** Presumir que --squash registra automaticamente ou que git merge --abort sempre funciona para squash.

**Alternativas:** Use merge comum quando preservar ancestralidade for importante.

**Recuperação:** Inspecione status e mudanças preparadas; sem MERGE\_HEAD, não dependa de merge --abort. Em laboratório descartável verificado inicialmente limpo, reset --merge HEAD pode descartar tentativa de integração rastreada após preservar edições necessárias; avalie separadamente se havia trabalho.

**Versão e dependências:** Sintaxe padrão Git; use a base de laboratório do guia, Git 2.40 ou superior. Editor confiável e hooks locais podem afetar execução.

**Capítulos relacionados**

- [merge-and-conflicts/05-squash-merge](../../merge-and-conflicts/05-squash-merge/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-merge>

## git-merge-abort

**`git merge --abort`**

**Tipo:** Uso de opção

**Nível:** Intermediário

**Pesquisar por intenção:** Resolver conflitos, Recuperar trabalho

**Risco:** Destrutivo. Cancelamento descarta trabalho de resolução de conflitos; preserve edições desejadas separadamente antes. Recuperação de trabalho anterior não registrado não é garantida.

**Finalidade:** Tentar cancelar merge comum em andamento e reconstruir estado anterior.

**Pré-requisitos:** Use repositório próprio descartável com a operação indicada já pausada; inspecione git status e preserve edições de resolução necessárias.

**Opções:** --abort opera em merge ativo; não é comando genérico de desfazer.

**Quando utilizar:** Ao abandonar merge comum não resolvido em laboratório descartável inicialmente limpo.

**Quando evitar:** Evite se trabalho de resolução precisa ser preservado ou merge já terminou; squash não possui MERGE\_HEAD.

**Sintaxe**

`git merge --abort`

**Exemplo básico**

`git merge --abort`

Cancele merge comum de prática com conflito deliberado.

**Exemplo profissional**

`git merge --abort`

Após salvar edições desejadas de resolução, abandone integração local inadequada.

**Impacto no estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / histórico: Condicional
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** Tenta restaurar estado pré-merge e encerra merge ativo em sucesso; trabalho sujo anterior pode não ser reconstruído.

**Impactos e efeitos colaterais:** Pode alterar working tree, index e metadados de merge; auto-stash pode ser reaplicado e gerar conflitos.

**Erros comuns:** Usar abort após merge concluído ou presumir recuperação garantida de trabalho não registrado.

**Alternativas:** Resolva e prepare conflitos e use git merge --continue se integração deve terminar.

**Recuperação:** Verifique status e ponta original após abort. Se falhar, pare e inspecione estado restante antes de novas mudanças.

**Versão e dependências:** Sintaxe padrão Git; use a base de laboratório do guia, Git 2.40 ou superior. Editor confiável e hooks locais podem afetar execução.

**Capítulos relacionados**

- [merge-and-conflicts/04-conflict-resolution](../../merge-and-conflicts/04-conflict-resolution/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-merge>

## git-merge-continue

**`git merge --continue`**

**Tipo:** Uso de opção

**Nível:** Intermediário

**Pesquisar por intenção:** Resolver conflitos, Integrar alterações

**Risco:** Alteração de estado. Integração pode gerar conflitos ou alterar a ponta atual; verifique destino e revise diff resultante e testes antes de compartilhar.

**Finalidade:** Finalizar merge comum ativo após resolver e preparar conflitos.

**Pré-requisitos:** Em repositório descartável com operação indicada pausada, resolva conflitos, prepare resoluções desejadas, revise diff preparado e confirme identidade fictícia.

**Opções:** --continue verifica merge ativo e invoca commit; editor ou hooks podem exigir interação.

**Quando utilizar:** Quando todas resoluções desejadas estão preparadas e revisadas.

**Quando evitar:** Não continue enquanto houver caminhos não mesclados ou conteúdo de resolução não revisado.

**Sintaxe**

`git merge --continue`

**Exemplo básico**

`git merge --continue`

Finalize merge de prática após preparar arquivo resolvido.

**Exemplo profissional**

`git merge --continue`

Após revisar diff da resolução e executar testes, conclua merge local.

**Impacto no estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / histórico: Condicional
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** Em sucesso cria commit de merge e limpa estado de merge; caso contrário pode continuar pausado.

**Impactos e efeitos colaterais:** Pode atualizar referência, objetos, metadados de index e estado de merge; hooks podem alterar estado local.

**Erros comuns:** Presumir que remover marcadores de conflito prepara resolução automaticamente.

**Alternativas:** Use git commit para concluir merge comum após inspecionar estado ou abort se abandonar.

**Recuperação:** Inspecione status e ponta salva. Se a operação estiver pausada, use o comando abort correspondente quando apropriado. Após conclusão, escolha recuperação conforme histórico compartilhado; não use reset às cegas.

**Versão e dependências:** Sintaxe padrão Git; use a base de laboratório do guia, Git 2.40 ou superior. Editor confiável e hooks locais podem afetar execução.

**Capítulos relacionados**

- [merge-and-conflicts/04-conflict-resolution](../../merge-and-conflicts/04-conflict-resolution/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-merge>

## git-rebase

**`git rebase`**

**Tipo:** Comando nativo

**Nível:** Avançado

**Pesquisar por intenção:** Integrar alterações, Reescrever histórico local

**Risco:** Reescrita de histórico. Reaplicação pode alterar IDs e prejudicar colaboradores. Use histórico privado, preserve ponta original e verifique resultado antes de compartilhar.

**Finalidade:** Reaplicar commits selecionados em base diferente para reorganizar histórico local.

**Pré-requisitos:** Use repositório próprio descartável, status limpo, referências verificadas e identidade fictícia. Salve a ponta original antes da integração.

**Opções:** Informe revisão upstream; --onto permite nova base separada e exige seleção cuidadosa de intervalo.

**Quando utilizar:** Ao atualizar branch privada de feature sobre base de integração mais nova.

**Quando evitar:** Evite reescrever commits compartilhados sem acordo ou executar rebase com operações inacabadas.

**Sintaxe**

`git rebase main`

**Exemplo básico**

`git rebase main`

De branch privada limpa de feature, reaplique sobre main existente.

**Exemplo profissional**

`git rebase main`

Após salvar ponta privada, atualize base e compare série revisada.

**Impacto no estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / histórico: Condicional
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** Pode reaplicar commits com novos IDs, ignorar mudanças equivalentes, avançar fast-forward, não alterar ou pausar por conflitos.

**Impactos e efeitos colaterais:** Pode alterar arquivos, index, objetos, referência atual e estado de sequência; HEAD pode ficar destacado durante reaplicação.

**Erros comuns:** Presumir que rebase preserva IDs ou executar no destino de integração em vez da branch reaplicada.

**Alternativas:** Use merge para integrar sem substituir commits de origem existentes.

**Recuperação:** Inspecione status e ponta salva. Se a operação estiver pausada, use o comando abort correspondente quando apropriado. Após conclusão, escolha recuperação conforme histórico compartilhado; não use reset às cegas.

**Versão e dependências:** Sintaxe padrão Git; use a base de laboratório do guia, Git 2.40 ou superior. Editor confiável e hooks locais podem afetar execução.

**Capítulos relacionados**

- [merge-and-conflicts/06-rebase-and-conflicts](../../merge-and-conflicts/06-rebase-and-conflicts/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-rebase>

## git-rebase-interactive

**`git rebase -i`**

**Tipo:** Uso de opção

**Nível:** Avançado

**Pesquisar por intenção:** Reescrever histórico local, Revisar alterações

**Risco:** Reescrita de histórico. Reaplicação pode alterar IDs e prejudicar colaboradores. Use histórico privado, preserve ponta original e verifique resultado antes de compartilhar.

**Finalidade:** Editar sequência de commits privados selecionados antes de reaplicá-los.

**Pré-requisitos:** Use repositório próprio descartável, status limpo, referências verificadas e identidade fictícia. Salve a ponta original antes da integração.

**Opções:** -i abre lista de tarefas com ações como pick, reword, edit, squash, fixup e drop; revise ordem e efeitos antes de salvar.

**Quando utilizar:** Ao refinar série de patches não publicada antes de revisão.

**Quando evitar:** Evite alterar histórico compartilhado, descartar commits necessários ou reordenar mudanças dependentes às cegas.

**Sintaxe**

`git rebase -i HEAD~2`

**Exemplo básico**

`git rebase -i HEAD~2`

Com pelo menos dois commits privados após uma base, inspecione lista antes de alterar.

**Exemplo profissional**

`git rebase -i main`

Em série linear privada de feature, revise edições ou ações fixup planejadas e valide depois.

**Impacto no estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / histórico: Condicional
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** Aplica ações escolhidas; pode substituir, combinar, omitir ou pausar em commits. Lista inalterada pode deixar histórico igual.

**Impactos e efeitos colaterais:** Pode modificar histórico, arquivos, index e metadados de rebase; comportamento padrão não preserva topologia de merges.

**Erros comuns:** Confundir ordem da lista com ordem do log mais recente primeiro, ou descartar commit pré-requisito.

**Alternativas:** Use commit complementar comum se histórico precisar permanecer intacto; use range-diff para revisar série revisada.

**Recuperação:** Inspecione status e ponta salva. Se a operação estiver pausada, use o comando abort correspondente quando apropriado. Após conclusão, escolha recuperação conforme histórico compartilhado; não use reset às cegas.

**Versão e dependências:** Sintaxe padrão Git; use a base de laboratório do guia, Git 2.40 ou superior. Editor confiável e hooks locais podem afetar execução.

**Capítulos relacionados**

- [merge-and-conflicts/07-interactive-rebase](../../merge-and-conflicts/07-interactive-rebase/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-rebase>

## git-rebase-continue

**`git rebase --continue`**

**Tipo:** Uso de opção

**Nível:** Avançado

**Pesquisar por intenção:** Resolver conflitos, Reescrever histórico local

**Risco:** Reescrita de histórico. Reaplicação pode alterar IDs e prejudicar colaboradores. Use histórico privado, preserve ponta original e verifique resultado antes de compartilhar.

**Finalidade:** Retomar rebase interrompido após tratar a pausa atual.

**Pré-requisitos:** Em repositório descartável com operação indicada pausada, resolva conflitos, prepare resoluções desejadas, revise diff preparado e confirme identidade fictícia.

**Opções:** --continue retoma sequência ativa; outros conflitos ou pausas de edição podem ocorrer.

**Quando utilizar:** Quando resoluções desejadas ou edições planejadas estão prontas e revisadas.

**Quando evitar:** Evite continuar com caminhos não resolvidos ou usar --skip apenas para silenciar conflito.

**Sintaxe**

`git rebase --continue`

**Exemplo básico**

`git rebase --continue`

Após preparar arquivo de prática resolvido, retome reaplicação.

**Exemplo profissional**

`git rebase --continue`

Revise resolução preparada e teste série privada antes de retomar; repita se pausar novamente.

**Impacto no estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / histórico: Condicional
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** Retoma reaplicação; pode terminar e atualizar branch ou pausar novamente.

**Impactos e efeitos colaterais:** Pode criar commits substitutos, atualizar index e working tree, mover HEAD e alterar metadados de sequência.

**Erros comuns:** Presumir que uma continuação sempre conclui toda a série.

**Alternativas:** Use git rebase --abort para abandonar rebase ativo após preservar resolução necessária.

**Recuperação:** Inspecione status e ponta salva. Se a operação estiver pausada, use o comando abort correspondente quando apropriado. Após conclusão, escolha recuperação conforme histórico compartilhado; não use reset às cegas.

**Versão e dependências:** Sintaxe padrão Git; use a base de laboratório do guia, Git 2.40 ou superior. Editor confiável e hooks locais podem afetar execução.

**Capítulos relacionados**

- [merge-and-conflicts/06-rebase-and-conflicts](../../merge-and-conflicts/06-rebase-and-conflicts/README.pt-BR.md)
- [merge-and-conflicts/07-interactive-rebase](../../merge-and-conflicts/07-interactive-rebase/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-rebase>

## git-rebase-abort

**`git rebase --abort`**

**Tipo:** Uso de opção

**Nível:** Avançado

**Pesquisar por intenção:** Resolver conflitos, Recuperar trabalho

**Risco:** Destrutivo. Cancelamento descarta trabalho de resolução de conflitos; preserve edições desejadas separadamente antes. Recuperação de trabalho anterior não registrado não é garantida.

**Finalidade:** Cancelar rebase ativo e restaurar HEAD à branch original ou posição inicial.

**Pré-requisitos:** Use repositório próprio descartável com a operação indicada já pausada; inspecione git status e preserve edições de resolução necessárias.

**Opções:** --abort cancela reaplicação; --quit encerra acompanhamento da operação sem a mesma restauração de HEAD, index e working tree.

**Quando utilizar:** Ao abandonar rebase privado inacabado por conflitos ou plano inadequados.

**Quando evitar:** Evite abortar se mudanças necessárias de resolução não estão salvas separadamente; não desfaz rebase concluído.

**Sintaxe**

`git rebase --abort`

**Exemplo básico**

`git rebase --abort`

Cancele rebase de prática com conflito iniciado em estado limpo.

**Exemplo profissional**

`git rebase --abort`

Após preservar edições necessárias de resolução, abandone reaplicação privada e verifique ponta original.

**Impacto no estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / histórico: Condicional
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** Restaura posição original de checkout e limpa rebase ativo em sucesso; auto-stash pode complicar restauração.

**Impactos e efeitos colaterais:** Pode descartar estado intermediário de reaplicação e resolução, atualizar arquivos, index e HEAD; objetos criados podem permanecer até limpeza.

**Erros comuns:** Esperar que edições feitas durante resolução sobrevivam ao cancelamento.

**Alternativas:** Resolva e continue quando plano original de integração ainda for adequado.

**Recuperação:** Verifique ponta original salva, status e eventual stash após cancelamento; se restauração falhar, preserve dados restantes e inspecione antes de agir.

**Versão e dependências:** Sintaxe padrão Git; use a base de laboratório do guia, Git 2.40 ou superior. Editor confiável e hooks locais podem afetar execução.

**Capítulos relacionados**

- [merge-and-conflicts/06-rebase-and-conflicts](../../merge-and-conflicts/06-rebase-and-conflicts/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-rebase>


---

<!-- navigation-footer -->
[Anterior](../06-branch-management/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../08-remotes-and-synchronization/README.pt-BR.md)
<!-- /navigation-footer -->
