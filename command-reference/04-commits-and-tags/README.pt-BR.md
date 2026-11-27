# 04 Commits e tags

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../03-working-tree-and-staging/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../05-history-and-comparison/README.pt-BR.md)
<!-- /navigation -->

Gerado a partir do JSON canônico. Edite os registros, não esta página.

As entradas descrevem comandos e operações, não uma sequência a executar. Pratique em repositórios descartáveis. Operações hospedadas são opcionais.

**Total de entradas distintas: 8**

- [`git commit`](#git-commit)
- [`git commit -a`](#git-commit-all)
- [`git commit --amend`](#git-commit-amend)
- [`git commit --fixup`](#git-commit-fixup)
- [`git tag`](#git-tag)
- [`git tag -a`](#git-tag-annotated)
- [`git tag -d`](#git-tag-delete)
- [`git tag -l`](#git-tag-list)

## git-commit

**`git commit`**

**Tipo:** Comando nativo

**Nível:** Iniciante

**Pesquisar por intenção:** Registrar alterações

**Risco:** Alteração de estado. Revise git diff --cached, identidade e hooks; o commit pode reter conteúdo sensível localmente.

**Finalidade:** Registrar o snapshot preparado e revisado como novo commit.

**Pré-requisitos:** Use repositório próprio descartável com identidade fictícia configurada e mudanças preparadas revisadas.

**Opções:** -m fornece a mensagem sem abrir editor; -v mostra um diff no editor.

**Quando utilizar:** Quando as mudanças preparadas formam uma unidade coerente de trabalho.

**Quando evitar:** Não registre segredos, mudanças alheias ou conflitos não resolvidos.

**Sintaxe**

`git commit -m "message"`

**Exemplo básico**

`git commit -m "Add notes"`

Após preparar um arquivo fictício de notas.

**Exemplo profissional**

`git commit -m "docs: explain setup"`

Registre uma mudança de documentação revisada.

**Impacto no estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / histórico: Altera
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** Um commit comum bem-sucedido registra o index e avança a branch atual ou HEAD destacado.

**Impactos e efeitos colaterais:** Normalmente não muda conteúdo dos arquivos; metadados do index e hooks locais podem alterar estado. Não há push.

**Erros comuns:** Presumir que edições não preparadas entram ou que o commit publica mudanças.

**Alternativas:** Use git add -p antes do commit para selecionar trechos individuais.

**Recuperação:** Inspecione git show HEAD; corrija erro não publicado com amend ou considere git revert para commit compartilhado após revisão.

**Versão e dependências:** Sintaxe padrão documentada para Git 2.34; sem ferramenta opcional para o comando mostrado. Hooks locais ou configuração de assinatura podem afetar a execução.

**Capítulos relacionados**

- [basic-commands/02-status-add-commit](../../basic-commands/02-status-add-commit/README.pt-BR.md)
- [getting-started/05-first-commit](../../getting-started/05-first-commit/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-commit/2.34.0>

## git-commit-all

**`git commit -a`**

**Tipo:** Uso de opção

**Nível:** Intermediário

**Pesquisar por intenção:** Registrar alterações, Preparar alterações

**Risco:** Alteração de estado. Pode capturar mais que o desejado; inspecione diferenças preparadas e não preparadas e configure identidade fictícia antes.

**Finalidade:** Preparar arquivos rastreados modificados e excluídos e criar um commit em uma operação.

**Pré-requisitos:** Use um repositório próprio descartável; inspecione o status e preserve trabalho valioso.

**Opções:** -a inclui modificações e exclusões rastreadas; -m define a mensagem.

**Quando utilizar:** Quando toda mudança rastreada e adição já preparada pertence a um commit.

**Quando evitar:** Evite quando houver edições ou exclusões rastreadas alheias.

**Sintaxe**

`git commit -a -m "message"`

**Exemplo básico**

`git commit -a -m "Update notes"`

Edite antes um arquivo de notas já rastreado.

**Exemplo profissional**

`git commit -a -m "docs: fix typos"`

Somente após revisar todas as mudanças rastreadas e o index.

**Impacto no estado**

- Working tree: Condicional
- Index: Altera
- Objetos / refs / histórico: Altera
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** O novo commit inclui atualizações rastreadas e conteúdo já preparado; arquivos novos não preparados continuam não rastreados.

**Impactos e efeitos colaterais:** Atualiza index e histórico; conteúdo dos arquivos normalmente não muda, sujeito a hooks.

**Erros comuns:** Esperar inclusão de arquivos não rastreados ou ignorar exclusões rastreadas.

**Alternativas:** Use caminhos explícitos com git add e git commit para delimitar o escopo.

**Recuperação:** Inspecione o commit resultante; corrija histórico não publicado com cuidado ou reverta commit compartilhado.

**Versão e dependências:** Sintaxe padrão documentada para Git 2.34; sem ferramenta opcional para o comando mostrado. Hooks locais ou configuração de assinatura podem afetar a execução.

**Capítulos relacionados**

- [basic-commands/02-status-add-commit](../../basic-commands/02-status-add-commit/README.pt-BR.md)
- [getting-started/05-first-commit](../../getting-started/05-first-commit/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-commit/2.34.0>

## git-commit-amend

**`git commit --amend`**

**Tipo:** Uso de opção

**Nível:** Intermediário

**Pesquisar por intenção:** Reescrever histórico local, Registrar alterações

**Risco:** Reescrita de histórico. Reescrever histórico pode prejudicar colaboradores; mantenha o exemplo local e não publicado.

**Finalidade:** Substituir o commit atual da ponta por um commit recém-criado.

**Pré-requisitos:** Use repositório próprio descartável com HEAD existente não publicado, index revisado e referência salva ao commit antigo.

**Opções:** --no-edit mantém a mensagem; -m fornece substituição; ambos usam o snapshot preparado.

**Quando utilizar:** Corrigir um commit privado da ponta antes de compartilhá-lo.

**Quando evitar:** Não reescreva histórico compartilhado sem cuidado nem use amend com mudanças preparadas alheias.

**Sintaxe**

`git commit --amend -m "message"`

**Exemplo básico**

`git commit --amend -m "Clarify notes"`

Use ponta privada e confirme diff preparado vazio para corrigir só a mensagem.

**Exemplo profissional**

`git commit --amend --no-edit`

Após preparar mudança de documentação esquecida para uma ponta não publicada.

**Impacto no estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / histórico: Altera
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** A substituição normalmente tem ID diferente e os mesmos pais da ponta anterior.

**Impactos e efeitos colaterais:** Move a branch local ou HEAD destacado; o commit antigo pode continuar alcançável por outra referência ou reflog. Hooks podem alterar estado local.

**Erros comuns:** Tratar --no-edit como alteração só da mensagem ou presumir que o ID antigo continua válido para a nova ponta.

**Alternativas:** Crie um commit complementar quando preservar histórico existente for importante.

**Recuperação:** Inspecione git reflog e a referência salva; crie branch de recuperação no ID antigo verificado se ainda disponível. Não use reset às cegas.

**Versão e dependências:** Sintaxe padrão documentada para Git 2.34; sem ferramenta opcional para o comando mostrado. Hooks locais ou configuração de assinatura podem afetar a execução.

**Capítulos relacionados**

- [history-and-recovery/08-amend](../../history-and-recovery/08-amend/README.pt-BR.md)
- [basic-commands/02-status-add-commit](../../basic-commands/02-status-add-commit/README.pt-BR.md)
- [getting-started/05-first-commit](../../getting-started/05-first-commit/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-commit/2.34.0>

## git-commit-fixup

**`git commit --fixup`**

**Tipo:** Uso de opção

**Nível:** Avançado

**Pesquisar por intenção:** Registrar alterações, Reescrever histórico local

**Risco:** Alteração de estado. Criar fixup não reescreve histórico, mas autosquash posterior pode; salve uma referência antes do rebase.

**Finalidade:** Criar um commit de correção separado marcado para futuro rebase com autosquash.

**Pré-requisitos:** Use repositório próprio descartável com correção preparada revisada e commit de destino existente em histórico não publicado.

**Opções:** --fixup HEAD aponta para a ponta atual; também pode receber ID de commit anterior verificado.

**Quando utilizar:** Ao preparar correções de revisão para incorporar depois em commits privados.

**Quando evitar:** Evite apontar para commit errado ou planejar autosquash em histórico compartilhado sem coordenação.

**Sintaxe**

`git commit --fixup HEAD`

**Exemplo básico**

`git commit --fixup HEAD`

Prepare pequena correção para o commit privado atual.

**Exemplo profissional**

`git commit --fixup HEAD~1`

Após confirmar que o pai anterior é o destino revisado da correção.

**Impacto no estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / histórico: Altera
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** Um novo commit comum com assunto fixup! é criado; o destino ainda não é substituído.

**Impactos e efeitos colaterais:** O snapshot do index é registrado e HEAD avança; só um rebase posterior reescreve histórico. Hooks podem afetar estado local.

**Erros comuns:** Presumir que --fixup já incorpora a correção ao destino.

**Alternativas:** Use commit complementar normal quando for desejável preservar cada correção pública.

**Recuperação:** Inspecione git log; se o destino estava errado, revise e corrija o fixup não publicado antes de tentar autosquash.

**Versão e dependências:** Sintaxe padrão documentada para Git 2.34; sem ferramenta opcional para o comando mostrado. Hooks locais ou configuração de assinatura podem afetar a execução.

**Capítulos relacionados**

- [merge-and-conflicts/07-interactive-rebase](../../merge-and-conflicts/07-interactive-rebase/README.pt-BR.md)
- [basic-commands/02-status-add-commit](../../basic-commands/02-status-add-commit/README.pt-BR.md)
- [getting-started/05-first-commit](../../getting-started/05-first-commit/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-commit/2.34.0>

## git-tag

**`git tag`**

**Tipo:** Comando nativo

**Nível:** Iniciante

**Pesquisar por intenção:** Gerenciar tags, Gerenciar releases

**Risco:** Alteração de estado. Verifique destino e nomes existentes; exemplos pressupõem tag.gpgSign desativado para criar tag leve.

**Finalidade:** Criar tag local leve apontando diretamente para objeto Git, normalmente commit.

**Pré-requisitos:** Use repositório próprio descartável com commit de destino existente; inspecione as tags e o destino antes.

**Opções:** Forneça nome e opcionalmente revisão de destino; sem destino Git usa HEAD.

**Quando utilizar:** Marcar marco local sem objeto de tag anotada separado.

**Quando evitar:** Evite tags leves quando a política de release exige anotações ou assinaturas.

**Sintaxe**

`git tag v0.1.0`

**Exemplo básico**

`git tag v0.1.0`

Marque o commit fictício atual de prática.

**Exemplo profissional**

`git tag review-ready HEAD`

Marque marco revisado localmente, não release publicado.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Altera
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Uma nova referência refs/tags aponta para o destino; a ancestralidade dos commits não muda.

**Impactos e efeitos colaterais:** Altera apenas referência local; não ocorre checkout nem push em configuração comum sem assinatura.

**Erros comuns:** Presumir que a tag acompanha a branch ou cria release hospedado automaticamente.

**Alternativas:** Use git tag -a para objeto de tag com metadados e mensagem.

**Recuperação:** Se tag não publicada estiver errada, registre destino atual, exclua localmente e recrie no destino verificado.

**Versão e dependências:** Sintaxe padrão documentada no Git 2.31; o manual oficial registra ausência de mudanças até Git 2.34.8. Sem ferramenta opcional para a operação sem assinatura mostrada.

**Capítulos relacionados**

- [git-internals/03-commits-and-tags](../../git-internals/03-commits-and-tags/README.pt-BR.md)
- [professional-workflows/12-release-management](../../professional-workflows/12-release-management/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-tag/2.31.0>

## git-tag-annotated

**`git tag -a`**

**Tipo:** Uso de opção

**Nível:** Intermediário

**Pesquisar por intenção:** Gerenciar tags, Gerenciar releases

**Risco:** Alteração de estado. Configure identidade fictícia do autor da tag; verifique destino, mensagem e política de assinatura. Anotação pode expor identidade quando compartilhada.

**Finalidade:** Criar objeto de tag anotada local e referência a ele.

**Pré-requisitos:** Use repositório próprio descartável com commit de destino existente; inspecione as tags e o destino antes.

**Opções:** -a solicita anotação; -m fornece mensagem; -s solicita assinatura separadamente.

**Quando utilizar:** Ao marcar release com metadados de autoria da tag e mensagem.

**Quando evitar:** Evite substituir tag de versão já publicada ou tratar anotação como prova de assinatura.

**Sintaxe**

`git tag -a v1.0.0 -m "Release 1.0.0"`

**Exemplo básico**

`git tag -a v1.0.0 -m "Release 1.0.0"`

Marque o commit de prática atual revisado.

**Exemplo profissional**

`git tag -a v1.2.0 -m "Stable release" HEAD`

Após verificar o destino e checklist local de release.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Altera
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Uma referência refs/tags aponta para objeto de tag que identifica destino e contém metadados da anotação.

**Impactos e efeitos colaterais:** Cria objeto e referência local; ancestralidade dos commits, arquivos, index e remoto não são alterados.

**Erros comuns:** Confundir tag anotada com tag assinada ou release hospedado.

**Alternativas:** Use git tag leve para marcador local temporário quando a política permitir.

**Recuperação:** Inspecione git show na tag; se não publicada, preserve ID antigo do objeto antes de corrigir. Para tags publicadas coordene nova versão.

**Versão e dependências:** Sintaxe padrão documentada no Git 2.31; o manual oficial registra ausência de mudanças até Git 2.34.8. Sem ferramenta opcional para a operação sem assinatura mostrada.

**Capítulos relacionados**

- [git-internals/03-commits-and-tags](../../git-internals/03-commits-and-tags/README.pt-BR.md)
- [professional-workflows/12-release-management](../../professional-workflows/12-release-management/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-tag/2.31.0>

## git-tag-delete

**`git tag -d`**

**Tipo:** Uso de opção

**Nível:** Intermediário

**Pesquisar por intenção:** Gerenciar tags, Desfazer alterações

**Risco:** Destrutivo. Exclusão perde referência; registre git rev-parse refs/tags/name antes de excluir. Recuperação não é garantida.

**Finalidade:** Remover referência de tag local nomeada.

**Pré-requisitos:** Use repositório próprio descartável; verifique tag existente não publicada e salve antes o ID exato do objeto da referência.

**Opções:** -d exclui uma ou mais tags locais nomeadas; não é exclusão remota.

**Quando utilizar:** Ao remover marcador privado de prática obsoleto.

**Quando evitar:** Evite remover tags de versão publicadas ou única referência de objetos importantes sem plano de recuperação.

**Sintaxe**

`git tag -d v0.1.0`

**Exemplo básico**

`git tag -d v0.1.0`

Remova tag local descartável verificada.

**Exemplo profissional**

`git tag -d review-ready`

Remova marcador privado de revisão após preservar ID do destino.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Altera
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** A referência local nomeada deixa de existir; tags remotas não mudam.

**Impactos e efeitos colaterais:** Pode deixar objeto de tag ou destino inalcançável se nenhuma outra referência o mantiver; o comando não apaga objetos imediatamente.

**Erros comuns:** Presumir que exclusão local remove tag remota ou que o objeto anotado exato é fácil de reconstruir.

**Alternativas:** Mantenha a tag intacta e crie novo marcador de versão quando ela foi compartilhada.

**Recuperação:** Se o objeto exato ainda estiver disponível, recrie a referência verificada com git update-ref; tag anotada não é restaurada fielmente apenas marcando o commit novamente.

**Versão e dependências:** Sintaxe padrão documentada no Git 2.31; o manual oficial registra ausência de mudanças até Git 2.34.8. Sem ferramenta opcional para a operação sem assinatura mostrada.

**Capítulos relacionados**

- [git-internals/03-commits-and-tags](../../git-internals/03-commits-and-tags/README.pt-BR.md)
- [professional-workflows/12-release-management](../../professional-workflows/12-release-management/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-tag/2.31.0>

## git-tag-list

**`git tag -l`**

**Tipo:** Uso de opção

**Nível:** Iniciante

**Pesquisar por intenção:** Gerenciar tags, Inspecionar referências

**Risco:** Somente leitura. Listagem somente leitura; não busca tags nem verifica conteúdo de releases.

**Finalidade:** Listar nomes de tags locais, opcionalmente correspondentes a padrão.

**Pré-requisitos:** Use repositório próprio; tag correspondente é opcional.

**Opções:** -l ativa listagem; coloque padrões glob entre aspas para o shell passá-los ao Git; --sort permite selecionar chave de ordenação.

**Quando utilizar:** Ao verificar nomes de releases locais existentes ou selecionar ponto de comparação.

**Quando evitar:** Não trate lista local como lista oficial de tags remotas.

**Sintaxe**

`git tag -l "v1.*"`

**Exemplo básico**

`git tag -l`

Inspecione todos os nomes de tags locais.

**Exemplo profissional**

`git tag -l "v1.*" --sort=version:refname`

Liste tags fictícias de versões correspondentes em ordem de versão.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Nomes de tags correspondentes são exibidos; padrão sem correspondência não produz nomes.

**Impactos e efeitos colaterais:** Nenhuma referência, objeto local ou estado remoto é modificado.

**Erros comuns:** Deixar curinga sem aspas ou presumir que ordem lexical equivale à ordem de versões.

**Alternativas:** Use git show-ref --tags para inspecionar referências de tags e IDs dos objetos.

**Recuperação:** Listagem não exige recuperação; inspecione padrão e referências locais se resultado for inesperado.

**Versão e dependências:** Sintaxe padrão documentada no Git 2.31; o manual oficial registra ausência de mudanças até Git 2.34.8. Sem ferramenta opcional para a operação sem assinatura mostrada.

**Capítulos relacionados**

- [git-internals/03-commits-and-tags](../../git-internals/03-commits-and-tags/README.pt-BR.md)
- [professional-workflows/12-release-management](../../professional-workflows/12-release-management/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-tag/2.31.0>


---

<!-- navigation-footer -->
[Anterior](../03-working-tree-and-staging/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../05-history-and-comparison/README.pt-BR.md)
<!-- /navigation-footer -->
