# 08 Remotos e sincronização

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../07-merge-rebase-and-conflicts/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../09-recovery-and-stash/README.pt-BR.md)
<!-- /navigation -->

Gerado a partir do JSON canônico. Edite os registros, não esta página.

As entradas descrevem comandos e operações, não uma sequência a executar. Pratique em repositórios descartáveis. Operações hospedadas são opcionais.

**Total de entradas distintas: 7**

- [`git clone`](#git-clone)
- [`git remote add`](#git-remote-add)
- [`git fetch`](#git-fetch)
- [`git pull --ff-only`](#git-pull-ff-only)
- [`git push`](#git-push)
- [`git push --delete`](#git-push-delete)
- [`git push --force-with-lease`](#git-push-force-with-lease)

## git-clone

**`git clone`**

**Tipo:** Comando nativo

**Nível:** Iniciante

**Pesquisar por intenção:** Criar repositório, Sincronizar repositórios

**Risco:** Alteração de estado. Verifique origem e destino; trate código selecionado e configuração local como não confiáveis até revisão.

**Finalidade:** Criar repositório local de repositório existente e normalmente selecionar sua branch inicial.

**Pré-requisitos:** Use diretório pai próprio descartável, origem local confiável existente e nome de destino livre.

**Opções:** Informe origem e destino opcional; --no-checkout pula checkout inicial; --branch seleciona branch ou tag inicial.

**Quando utilizar:** Ao obter cópia de trabalho independente de projeto existente.

**Quando evitar:** Evite clonar repositórios não confiáveis em diretórios importantes ou tratar clone como cópia integral de todos dados do servidor.

**Sintaxe**

`git clone origin.git learner`

**Exemplo básico**

`git clone origin.git learner`

De diretório pai descartável, clone repositório bare local existente e populado.

**Exemplo profissional**

`git clone --branch main origin.git reviewer`

Crie segundo clone local para simulação de revisão; main deve existir.

**Impacto no estado**

- Working tree: Altera
- Index: Altera
- Objetos / refs / histórico: Altera
- Repositório remoto: Inalterado
- Outros estados: Altera

**Resultado esperado:** Normalmente cria destino com objetos Git, configuração origin, referências de rastreamento remoto e branch selecionada; repositórios vazios e opções podem diferir.

**Impactos e efeitos colaterais:** Cria novo repositório e arquivos locais; não publica mudanças na origem.

**Erros comuns:** Presumir que clone copia issues, permissões, configuração CI ou todas referências remotas.

**Alternativas:** Use git init com remoto explícito ao iniciar projeto novo em vez de copiar existente.

**Recuperação:** Se clone falhar, inspecione erro e destino; tente em novo diretório vazio sem excluir arquivos alheios.

**Versão e dependências:** Sintaxe padrão Git; use Git 2.40 ou superior nos laboratórios do guia. Serviços hospedados podem exigir autenticação e permissões; exemplos usam apenas caminhos locais.

**Capítulos relacionados**

- [remote-repositories/01-remote-concepts](../../remote-repositories/01-remote-concepts/README.pt-BR.md)
- [remote-repositories/02-fetch-and-tracking](../../remote-repositories/02-fetch-and-tracking/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-clone>

## git-remote-add

**`git remote add`**

**Tipo:** Subcomando

**Nível:** Iniciante

**Pesquisar por intenção:** Gerenciar remotos, Configurar Git

**Risco:** Alteração de estado. Confirme remoto e referência de destino exata. Nunca pratique contra o guia ou serviço compartilhado real; não publique segredos.

**Finalidade:** Registrar remoto nomeado e mapeamento padrão de fetch na configuração local.

**Pré-requisitos:** Use apenas laboratório próprio descartável com remoto local. Verifique repositório, caminho remoto, referências, status e identidade fictícia antes de operar.

**Opções:** Informe nome remoto livre e URL ou caminho; git remote -v exibe URLs configuradas; -f também faria fetch.

**Quando utilizar:** Ao conectar repositório local existente a remoto próprio.

**Quando evitar:** Evite inserir credenciais em URLs ou adicionar destino não verificado.

**Sintaxe**

`git remote add origin ../origin.git`

**Exemplo básico**

`git remote add origin ../origin.git`

Conecte repositório de prática atual a bare vizinho.

**Exemplo profissional**

`git remote add review ../review.git`

Registre segundo remoto próprio de laboratório sem buscar ou publicar.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Altera

**Resultado esperado:** Configuração local contém nome, URL e mapeamento de fetch; add comum não o contata.

**Impactos e efeitos colaterais:** Altera só configuração local na forma mostrada; não transfere objetos nem altera referências remotas.

**Erros comuns:** Tentar adicionar origin existente ou presumir que adicionar envia commits automaticamente.

**Alternativas:** Use git remote set-url para corrigir remoto existente verificado; inspecione git remote get-url antes.

**Recuperação:** Se adicionado errado e sem uso, verifique nome e remova com git remote remove; remoção também pode excluir referências de rastreamento e configuração associadas.

**Versão e dependências:** Sintaxe padrão Git; use Git 2.40 ou superior nos laboratórios do guia. Serviços hospedados podem exigir autenticação e permissões; exemplos usam apenas caminhos locais.

**Capítulos relacionados**

- [remote-repositories/01-remote-concepts](../../remote-repositories/01-remote-concepts/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-remote>

## git-fetch

**`git fetch`**

**Tipo:** Comando nativo

**Nível:** Iniciante

**Pesquisar por intenção:** Sincronizar repositórios, Inspecionar referências

**Risco:** Alteração de estado. Confirme remoto e referência de destino exata. Nunca pratique contra o guia ou serviço compartilhado real; não publique segredos.

**Finalidade:** Obter objetos remotos e atualizar referências locais conforme mapeamento de fetch.

**Pré-requisitos:** Use apenas laboratório próprio descartável com remoto local. Verifique repositório, caminho remoto, referências, status e identidade fictícia antes de operar.

**Opções:** Informe remoto; --prune remove referências de destino obsoletas conforme refspecs, normalmente branches de rastreamento remoto; inspecione mapeamentos personalizados antes.

**Quando utilizar:** Ao inspecionar progresso remoto antes de decidir como integrá-lo.

**Quando evitar:** Evite refspecs personalizados não revisados ou presumir que código buscado é confiável.

**Sintaxe**

`git fetch origin`

**Exemplo básico**

`git fetch origin`

Atualize referências de rastreamento do bare local próprio.

**Exemplo profissional**

`git fetch --prune origin`

Com mapeamento padrão de branches verificado, remova referências obsoletas após limpeza remota aprovada.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Condicional
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** Fetch comum atualiza referências de rastreamento e FETCH\_HEAD conforme aplicável; branch local atual e arquivos normalmente ficam inalterados.

**Impactos e efeitos colaterais:** Pode adicionar objetos, atualizar referências e executar manutenção; fetch comum mostrado não integra branch selecionada nem atualiza referências de origem.

**Erros comuns:** Confundir origin/main com estado remoto em tempo real ou presumir que fetch atualiza main diretamente.

**Alternativas:** Use git pull --ff-only quando integração fast-forward verificada também for desejada.

**Recuperação:** Se fetch atualizar referência inesperada, inspecione mapeamento e IDs salvos; não redefina às cegas. Referências podadas só podem ser buscadas novamente se disponíveis na origem ou recuperadas de objetos preservados.

**Versão e dependências:** Sintaxe padrão Git; use Git 2.40 ou superior nos laboratórios do guia. Serviços hospedados podem exigir autenticação e permissões; exemplos usam apenas caminhos locais.

**Capítulos relacionados**

- [remote-repositories/02-fetch-and-tracking](../../remote-repositories/02-fetch-and-tracking/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-fetch>

## git-pull-ff-only

**`git pull --ff-only`**

**Tipo:** Uso de opção

**Nível:** Intermediário

**Pesquisar por intenção:** Sincronizar repositórios, Integrar alterações, Proteger histórico

**Risco:** Alteração de estado. Confirme remoto e referência de destino exata. Nunca pratique contra o guia ou serviço compartilhado real; não publique segredos.

**Finalidade:** Buscar mudanças remotas e integrar apenas quando resultado fast-forward ou já contido for possível.

**Pré-requisitos:** Use apenas laboratório próprio descartável com remoto local. Verifique repositório, caminho remoto, referências, status e identidade fictícia antes de operar.

**Opções:** --ff-only recusa integração divergente; remoto e branch explícitos evitam depender de padrões upstream.

**Quando utilizar:** Quando branch local limpa deve avançar linearmente ao upstream revisado.

**Quando evitar:** Evite pull na branch errada, com edições não preservadas ou quando divergência exige decisão separada.

**Sintaxe**

`git pull --ff-only origin main`

**Exemplo básico**

`git pull --ff-only origin main`

Da main local limpa no laboratório, integre atualização remota linear conhecida.

**Exemplo profissional**

`git pull --ff-only origin main`

Após inspecionar progresso remoto, exija sincronização linear da main local do laboratório.

**Impacto no estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / histórico: Condicional
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** Fetch pode atualizar referências de rastreamento mesmo se integração recusar; branch atual só avança quando permitido.

**Impactos e efeitos colaterais:** Pode atualizar objetos, referências de rastreamento, working tree e index; não implica atualização de branch remota.

**Erros comuns:** Presumir que falha significa nenhum estado local alterado ou tratar pull como apenas fetch.

**Alternativas:** Separe git fetch e git merge --ff-only para inspecionar commits recebidos antes de integrar.

**Recuperação:** Se integração recusar, inspecione status, referências de rastreamento e divergência; não force nem descarte commits locais. Se avanço indesejado ocorreu, consulte ponta salva e política de histórico compartilhado.

**Versão e dependências:** Sintaxe padrão Git; use Git 2.40 ou superior nos laboratórios do guia. Serviços hospedados podem exigir autenticação e permissões; exemplos usam apenas caminhos locais.

**Capítulos relacionados**

- [remote-repositories/03-pull-push-and-divergence](../../remote-repositories/03-pull-push-and-divergence/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-pull>

## git-push

**`git push`**

**Tipo:** Comando nativo

**Nível:** Intermediário

**Pesquisar por intenção:** Sincronizar repositórios, Gerenciar remotos

**Risco:** Alteração remota. Confirme remoto e referência de destino exata. Nunca pratique contra o guia ou serviço compartilhado real; não publique segredos.

**Finalidade:** Enviar objetos necessários e solicitar atualização de referências remotas especificadas.

**Pré-requisitos:** Use apenas laboratório próprio descartável com remoto local. Verifique repositório, caminho remoto, referências, status e identidade fictícia antes de operar.

**Opções:** Informe remoto e branch; -u define upstream para branches enviadas com sucesso ou atualizadas; --dry-run simula sem atualizar referências remotas.

**Quando utilizar:** Ao publicar commits revisados em branch de destino autorizada.

**Quando evitar:** Evite publicar commits não revisados, segredos ou mudanças diretas em branches protegidas.

**Sintaxe**

`git push origin feat/notes`

**Exemplo básico**

`git push -u origin feat/notes`

Publique branch privada existente de feature no remoto local descartável e configure rastreamento.

**Exemplo profissional**

`git push origin feat/review`

Após revisar conteúdo registrado, publique apenas branch de feature nomeada no laboratório.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Condicional
- Repositório remoto: Condicional
- Outros estados: Condicional

**Resultado esperado:** Em aceitação, referências remotas refletem atualizações solicitadas; pushes comuns de branches recusam atualizações não fast-forward salvo configuração ou substituição explícita.

**Impactos e efeitos colaterais:** Pode atualizar objetos e referências remotas, referências de rastreamento locais e configuração upstream com -u; hooks confiáveis podem executar.

**Erros comuns:** Esperar que push envie arquivos não preparados ou presumir sucesso como prova de qualidade ou aprovação de revisão.

**Alternativas:** Use git push --dry-run com destino explícito para simulação; use pull request para integração protegida.

**Recuperação:** Se recusado, inspecione mudanças remotas e política. Para push errado aceito, coordene correção; excluir referência não garante remoção de dados expostos.

**Versão e dependências:** Sintaxe padrão Git; use Git 2.40 ou superior nos laboratórios do guia. Serviços hospedados podem exigir autenticação e permissões; exemplos usam apenas caminhos locais.

**Capítulos relacionados**

- [remote-repositories/03-pull-push-and-divergence](../../remote-repositories/03-pull-push-and-divergence/README.pt-BR.md)
- [remote-repositories/04-remote-branch-lifecycle](../../remote-repositories/04-remote-branch-lifecycle/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-push>

## git-push-delete

**`git push --delete`**

**Tipo:** Uso de opção

**Nível:** Intermediário

**Pesquisar por intenção:** Gerenciar remotos, Gerenciar branches, Proteger histórico

**Risco:** Alteração remota. Confirme remoto e referência de destino exata. Nunca pratique contra o guia ou serviço compartilhado real; não publique segredos.

**Finalidade:** Solicitar exclusão de referência remota nomeada, aqui uma branch remota.

**Pré-requisitos:** Use apenas laboratório próprio descartável com remoto local. Verifique repositório, caminho remoto, referências, status e identidade fictícia antes de operar.

**Opções:** --delete marca referência de destino nomeada para exclusão; exclusão de branch local é separada.

**Quando utilizar:** Quando branch remota de feature obsoleta autorizada tem trabalho preservado verificado e sem dependentes restantes.

**Quando evitar:** Evite excluir referências protegidas, ativas ou não verificadas, ou branches com revisões abertas que ainda dependem delas.

**Sintaxe**

`git push origin --delete feat/notes`

**Exemplo básico**

`git push origin --delete feat/notes`

Remova apenas referência de feature obsoleta verificada do bare local de laboratório.

**Exemplo profissional**

`git push origin --delete feat/review`

Após confirmar integração, ponta salva e ausência de consumidores, limpe branch remota descartável.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Condicional
- Repositório remoto: Condicional
- Outros estados: Condicional

**Resultado esperado:** Se aceito, referência remota nomeada desaparece; branch local permanece e referências de rastreamento podem exigir poda em outros clones.

**Impactos e efeitos colaterais:** Altera referências remotas e possivelmente metadados locais de rastreamento; objetos não têm apagamento imediato garantido.

**Erros comuns:** Presumir que excluir branch local e remota são equivalentes ou excluir antes de revisar ancestralidade e dependências.

**Alternativas:** Mantenha a branch remota se houver dúvida; remova referências locais de rastreamento obsoletas após limpeza autorizada do servidor.

**Recuperação:** Registre ponta remota exata antes. Se objeto estiver preservado e política permitir, coordene recriação no ID verificado; recuperação não é garantida.

**Versão e dependências:** Sintaxe padrão Git; use Git 2.40 ou superior nos laboratórios do guia. Serviços hospedados podem exigir autenticação e permissões; exemplos usam apenas caminhos locais.

**Capítulos relacionados**

- [remote-repositories/04-remote-branch-lifecycle](../../remote-repositories/04-remote-branch-lifecycle/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-push>

## git-push-force-with-lease

**`git push --force-with-lease`**

**Tipo:** Uso de opção

**Nível:** Avançado

**Pesquisar por intenção:** Reescrever histórico local, Proteger histórico, Sincronizar repositórios

**Risco:** Alteração remota. Isto é substituição de histórico remoto, não padrão seguro. Lease correspondente não impede perder mudanças já presentes na ponta esperada; nunca contorne proteções do projeto.

**Finalidade:** Solicitar atualização remota não fast-forward apenas se referência remota ainda corresponder a valor explicitamente esperado.

**Pré-requisitos:** Use apenas laboratório próprio descartável com remoto local. Verifique repositório, caminho remoto, referências, status e identidade fictícia antes de operar.

**Opções:** Use --force-with-lease=ref:expected com ID de objeto exato revisado; forma abreviada sem expectativa explícita pode ser afetada por fetch em segundo plano.

**Quando utilizar:** Apenas em simulação descartável autorizada de substituição de branch privada após reescrever e revisar seu histórico.

**Quando evitar:** Nunca use no guia, branches protegidas ou trabalho compartilhado sem acordo explícito; não tente novamente com nova lease só para vencer recusa.

**Sintaxe**

`git push --force-with-lease=refs/heads/feat/notes:EXPECTED origin feat/notes`

**Exemplo básico**

`git push --force-with-lease=refs/heads/feat/notes:EXPECTED origin feat/notes`

Somente no laboratório local descartável, substitua EXPECTED pelo ID completo da ponta remota previamente revisada após salvá-la e conferir todos commits só remotos.

**Exemplo profissional**

`git push --force-with-lease=refs/heads/feat/review:EXPECTED origin feat/review`

Simule reescrita privada coordenada; substitua pelo ID verificado salvo e pare se lease recusar atualização.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Condicional
- Repositório remoto: Condicional
- Outros estados: Condicional

**Resultado esperado:** Aceita atualização solicitada apenas se valor antigo esperado corresponder e política do servidor permitir; expectativa obsoleta causa recusa.

**Impactos e efeitos colaterais:** Pode substituir ponta de branch remota, transferir objetos e atualizar referências de rastreamento locais; commits só remotos podem ficar inalcançáveis.

**Erros comuns:** Tratar lease correspondente como prova de segurança de conteúdo ou presumir proteção de todas outras referências e colaboradores.

**Alternativas:** Prefira push comum ou commit complementar preservando histórico; se lease falhar, busque e revise trabalho só remoto antes de decidir.

**Recuperação:** Mantenha referência durável à ponta remota anterior antes da simulação. Se substituição errada for aceita, coordene recuperação de objetos preservados e proteja trabalho novo; restauração não é garantida.

**Versão e dependências:** Sintaxe padrão Git; use Git 2.40 ou superior nos laboratórios do guia. Serviços hospedados podem exigir autenticação e permissões; exemplos usam apenas caminhos locais.

**Capítulos relacionados**

- [remote-repositories/03-pull-push-and-divergence](../../remote-repositories/03-pull-push-and-divergence/README.pt-BR.md)
- [remote-repositories/04-remote-branch-lifecycle](../../remote-repositories/04-remote-branch-lifecycle/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-push>


---

<!-- navigation-footer -->
[Anterior](../07-merge-rebase-and-conflicts/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../09-recovery-and-stash/README.pt-BR.md)
<!-- /navigation-footer -->
