# 13 Segurança e manutenção

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../12-internals-and-plumbing/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../14-platforms-and-automation/README.pt-BR.md)
<!-- /navigation -->

Gerado a partir do JSON canônico. Edite os registros, não esta página.

As entradas descrevem comandos e operações, não uma sequência a executar. Pratique em repositórios descartáveis. Operações hospedadas são opcionais.

**Total de entradas distintas: 8**

- [`git commit -S`](#git-commit-sign)
- [`git tag -s`](#git-tag-sign)
- [`git verify-commit`](#git-verify-commit)
- [`git verify-tag`](#git-verify-tag)
- [`git credential reject`](#git-credential-reject)
- [`git fsck`](#git-fsck)
- [`git gc`](#git-gc)
- [`git maintenance run`](#git-maintenance-run)

## git-commit-sign

**`git commit -S`**

**Tipo:** Uso de opção

**Nível:** Intermediário

**Pesquisar por intenção:** Registrar alterações, Verificar assinaturas

**Risco:** Alteração de estado. Proteja chaves de assinatura; nunca coloque material privado em arquivos rastreados.

**Finalidade:** Criar commit assinado criptograficamente.

**Pré-requisitos:** Use repositório completo próprio descartável, referências verificadas, trabalho salvo e configuração confiável. Nunca use credenciais reais ou chaves pessoais em laboratórios.

**Opções:** -S solicita assinatura; ID de chave opcional fica unido à opção curta. -s minúsculo adiciona trailer sign-off.

**Quando utilizar:** Quando commits assinados são exigidos por política.

**Quando evitar:** Evite assinar mudanças não revisadas ou usar chaves não autorizadas.

**Sintaxe**

`git commit -S -m "Signed notes"`

**Exemplo básico**

`git commit -S -m "Signed notes"`

Registre conteúdo preparado revisado com chave descartável configurada.

**Exemplo profissional**

`git commit -S -m "docs: review notes"`

Registre commit privado assinado de documentação.

**Impacto no estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / histórico: Altera
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** Commit bem-sucedido inclui assinatura e avança referência; falha de assinatura pode impedir criação.

**Impactos e efeitos colaterais:** Cria objeto assinado e atualiza referência; ferramentas de assinatura e hooks podem alterar estado local. Não há push.

**Erros comuns:** Confundir -S com sign-off ou presumir assinatura prova qualidade.

**Alternativas:** Use commit comum só se política permitir; confira commits assinados com git verify-commit.

**Recuperação:** Confira configuração de assinatura e disponibilidade de chave antes de tentar novamente; verifique commit resultante antes de compartilhar.

**Versão e dependências:** Exige backend de assinatura ou verificação configurado, como GnuPG ou OpenSSH com suporte a assinatura SSH, chaves e configuração de confiança adequadas. Use chaves descartáveis de laboratório.

**Capítulos relacionados**

- [security/09-commit-and-tag-signing](../../security/09-commit-and-tag-signing/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-commit>

## git-tag-sign

**`git tag -s`**

**Tipo:** Uso de opção

**Nível:** Intermediário

**Pesquisar por intenção:** Gerenciar tags, Verificar assinaturas

**Risco:** Alteração de estado. Verifique destino e assinante; nunca sobrescreva tags publicadas para ocultar erro.

**Finalidade:** Criar tag anotada assinada e referência local.

**Pré-requisitos:** Use repositório completo próprio descartável, referências verificadas, trabalho salvo e configuração confiável. Nunca use credenciais reais ou chaves pessoais em laboratórios.

**Opções:** -s solicita assinatura; -m fornece mensagem; objeto final opcional nomeia destino.

**Quando utilizar:** Ao marcar revisão revisada sob política de assinatura de release.

**Quando evitar:** Evite destinos presumidos ou mover tags de versão publicadas.

**Sintaxe**

`git tag -s v1.0.0 -m "Practice release"`

**Exemplo básico**

`git tag -s v1.0.0 -m "Practice release"`

Assine tag de versão livre em HEAD verificado.

**Exemplo profissional**

`git tag -s v1.1.0 -m "Reviewed release" main`

Assine tag de versão livre na main local revisada.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Altera
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** Cria objeto tag assinado e referência local; não publica release nem assina commit alvo.

**Impactos e efeitos colaterais:** Adiciona objeto tag e referência; backend pode mudar metadados locais; ponta da branch não muda.

**Erros comuns:** Presumir tag assinada verifica todo artefato ou commit.

**Alternativas:** Use tag anotada não assinada só quando política permitir; verifique com git verify-tag.

**Recuperação:** Se tag privada incorreta, registre ID e revise exclusão antes de substituir; siga política de correção para tags publicadas.

**Versão e dependências:** Exige backend de assinatura ou verificação configurado, como GnuPG ou OpenSSH com suporte a assinatura SSH, chaves e configuração de confiança adequadas. Use chaves descartáveis de laboratório.

**Capítulos relacionados**

- [security/09-commit-and-tag-signing](../../security/09-commit-and-tag-signing/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-tag>

## git-verify-commit

**`git verify-commit`**

**Tipo:** Comando nativo

**Nível:** Intermediário

**Pesquisar por intenção:** Verificar assinaturas

**Risco:** Alteração de estado. Assinatura não estabelece segurança do código nem aprovação de revisão. Proteja chaves privadas; verifique objeto exato e confiança no assinante independentemente.

**Finalidade:** Verificar assinatura criptográfica de commit selecionado usando backend configurado.

**Pré-requisitos:** Use repositório completo próprio descartável, referências verificadas, trabalho salvo e configuração confiável. Nunca use credenciais reais ou chaves pessoais em laboratórios.

**Opções:** Informe referências ou IDs de commits; --verbose exibe conteúdo antes da verificação.

**Quando utilizar:** Ao conferir commit assinado conforme política de identidade confiável.

**Quando evitar:** Não aceite assinatura como prova de código seguro ou aprovação de revisão.

**Sintaxe**

`git verify-commit HEAD`

**Exemplo básico**

`git verify-commit HEAD`

Verifique commit de prática assinado existente.

**Exemplo profissional**

`git verify-commit main`

Verifique main assinada do laboratório conforme política de confiança.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** Relata resultado; falha retorna não zero e configuração de confiança afeta aceitação.

**Impactos e efeitos colaterais:** Não altera referências ou arquivos Git; backend externo pode atualizar metadados próprios.

**Erros comuns:** Conferir resultado criptográfico ignorando política de assinante confiável.

**Alternativas:** Use git log --show-signature para contexto; mantenha exigência de ID exato e resultado de verificação.

**Recuperação:** Em falha, inspecione status, objeto selecionado, backend e configuração de chave ou confiança; não contorne assinatura ou verificação obrigatória.

**Versão e dependências:** Exige backend de assinatura ou verificação configurado, como GnuPG ou OpenSSH com suporte a assinatura SSH, chaves e configuração de confiança adequadas. Use chaves descartáveis de laboratório.

**Capítulos relacionados**

- [security/09-commit-and-tag-signing](../../security/09-commit-and-tag-signing/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-verify-commit>

## git-verify-tag

**`git verify-tag`**

**Tipo:** Comando nativo

**Nível:** Intermediário

**Pesquisar por intenção:** Verificar assinaturas, Gerenciar tags

**Risco:** Alteração de estado. Assinatura não estabelece segurança do código nem aprovação de revisão. Proteja chaves privadas; verifique objeto exato e confiança no assinante independentemente.

**Finalidade:** Verificar assinatura de objeto tag assinado.

**Pré-requisitos:** Use repositório completo próprio descartável, referências verificadas, trabalho salvo e configuração confiável. Nunca use credenciais reais ou chaves pessoais em laboratórios.

**Opções:** Informe nomes de tags assinadas ou IDs de objetos tag; --verbose exibe conteúdo.

**Quando utilizar:** Ao conferir marcadores de release assinados sob política de confiança.

**Quando evitar:** Não espere assinatura em tags leves nem confie automaticamente em artefatos alheios.

**Sintaxe**

`git verify-tag v1.0.0`

**Exemplo básico**

`git verify-tag v1.0.0`

Verifique tag anotada assinada existente de laboratório.

**Exemplo profissional**

`git verify-tag v1.1.0`

Verifique marcador de versão antes de revisar destino e artefatos.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** Relata resultado; configuração de confiança afeta aceitação.

**Impactos e efeitos colaterais:** Não move referências nem edita arquivos rastreados; backend pode modificar metadados próprios.

**Erros comuns:** Verificar nome da tag sem conferir destino exato ou tratar como verificação de assinatura do commit alvo.

**Alternativas:** Use git verify-commit separadamente quando necessário e revise proveniência de artefatos independentemente.

**Recuperação:** Em falha, inspecione status, objeto selecionado, backend e configuração de chave ou confiança; não contorne assinatura ou verificação obrigatória.

**Versão e dependências:** Exige backend de assinatura ou verificação configurado, como GnuPG ou OpenSSH com suporte a assinatura SSH, chaves e configuração de confiança adequadas. Use chaves descartáveis de laboratório.

**Capítulos relacionados**

- [security/09-commit-and-tag-signing](../../security/09-commit-and-tag-signing/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-verify-tag>

## git-credential-reject

**`git credential reject`**

**Tipo:** Subcomando

**Nível:** Avançado

**Pesquisar por intenção:** Autenticar com segurança, Diagnosticar configuração

**Risco:** Sensível. Pode apagar várias contas correspondentes; use só helper simulado e identificadores fictícios em laboratórios.

**Finalidade:** Solicitar que helpers configurados apaguem credenciais armazenadas correspondentes.

**Pré-requisitos:** Isole configuração Git, desative helpers herdados e use só helper simulado registrando eventos erase sem credenciais reais.

**Opções:** Lê linhas chave=valor terminadas por linha vazia; correspondência depende de helper e campos.

**Quando utilizar:** Ao ensaiar remoção de entrada local de autenticação obsoleta.

**Quando evitar:** Evite correspondência ampla, helpers desconhecidos e credenciais reais na prática.

**Sintaxe**

`git credential reject`

**Exemplo básico**

`git credential reject`

Com só helper simulado, digite protocol=https, host=example.invalid, username=student em linhas separadas, depois linha vazia.

**Exemplo profissional**

`git credential reject`

Repita com identificadores fictícios no laboratório simulado e inspecione evento erase.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Condicional

**Resultado esperado:** Helpers configurados recebem solicitação erase; remoção depende de comportamento. Validade de token no servidor não muda.

**Impactos e efeitos colaterais:** Pode remover registros locais; não revoga tokens do provedor nem muda histórico Git.

**Erros comuns:** Confundir exclusão local com revogação de token no servidor.

**Alternativas:** Use processo oficial de revogação e rotação do provedor em exposição real.

**Recuperação:** Se registro local necessário removido, reautentique por fluxo aprovado. Nunca restaure token exposto.

**Versão e dependências:** Use Git 2.40 ou superior nos laboratórios; confira configuração e disponibilidade locais.

**Capítulos relacionados**

- [security/04-credential-managers](../../security/04-credential-managers/README.pt-BR.md)
- [security/11-credential-exposure-and-incident-response](../../security/11-credential-exposure-and-incident-response/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-credential>

## git-fsck

**`git fsck`**

**Tipo:** Comando nativo

**Nível:** Avançado

**Pesquisar por intenção:** Verificar integridade, Inspecionar objetos Git

**Risco:** Somente leitura. Somente leitura nas formas mostradas; sucesso de integridade não prova correção da aplicação.

**Finalidade:** Verificar validade e conectividade de objetos.

**Pré-requisitos:** Use repositório completo próprio descartável, referências verificadas, trabalho salvo e configuração confiável. Nunca use credenciais reais ou chaves pessoais em laboratórios.

**Opções:** --full inclui objetos empacotados e alternates; --strict aplica checagens mais estritas; --lost-found grava arquivos e não é usado aqui.

**Quando utilizar:** Ao investigar integridade ou revisar cópia completa antes de manutenção.

**Quando evitar:** Não trate objetos dangling isoladamente como corrupção nem dependa de fsck como backup.

**Sintaxe**

`git fsck --full`

**Exemplo básico**

`git fsck --full`

Inspecione conectividade e validade em repositório local completo de prática.

**Exemplo profissional**

`git fsck --full --strict`

Execute inspeção de integridade mais estrita antes de manutenção.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Inalterado

**Resultado esperado:** Relata achados de integridade detectados e pode listar objetos dangling.

**Impactos e efeitos colaterais:** Formas mostradas inspecionam repositório local completo sem alterar intencionalmente objetos, referências ou arquivos.

**Erros comuns:** Executar limpeza após corrupção e perder dados potencialmente recuperáveis.

**Alternativas:** Use git count-objects para estatísticas; repare a partir de backups verificados ou cópias saudáveis.

**Recuperação:** Pare gravações em erros graves, preserve cópia e investigue antes de reparo.

**Versão e dependências:** Use Git 2.40 ou superior nos laboratórios; confira configuração e disponibilidade locais.

**Capítulos relacionados**

- [git-internals/07-loose-objects-and-packfiles](../../git-internals/07-loose-objects-and-packfiles/README.pt-BR.md)
- [git-internals/08-gc-and-maintenance](../../git-internals/08-gc-and-maintenance/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-fsck>

## git-gc

**`git gc`**

**Tipo:** Comando nativo

**Nível:** Avançado

**Pesquisar por intenção:** Manter um repositório, Proteger histórico

**Risco:** Destrutivo. Limpeza pode remover trabalho inalcançável permanentemente. Preserve referências de recuperação e backups antes de executar.

**Finalidade:** Executar manutenção como empacotamento e expiração configurada de dados.

**Pré-requisitos:** Use repositório completo próprio descartável, referências verificadas, trabalho salvo e configuração confiável. Nunca use credenciais reais ou chaves pessoais em laboratórios.

**Opções:** --auto verifica necessidade; --no-prune evita poda comum; não use --prune=now em laboratórios.

**Quando utilizar:** Quando repositório local saudável exige manutenção sob retenção revisada.

**Quando evitar:** Evite gravações concorrentes, investigações de recuperação ou trabalho inalcançável não preservado.

**Sintaxe**

`git gc`

**Exemplo básico**

`git gc`

Em repositório descartável ocioso com referências de recuperação salvas, execute manutenção comum.

**Exemplo profissional**

`git gc --no-prune`

Pule etapa comum de poda; revise também outras configurações de expiração.

**Impacto no estado**

- Working tree: Inalterado
- Index: Condicional
- Objetos / refs / histórico: Condicional
- Repositório remoto: Inalterado
- Outros estados: Altera

**Resultado esperado:** Pode consolidar objetos e referências, expirar reflogs e remover dados inalcançáveis elegíveis.

**Impactos e efeitos colaterais:** Altera armazenamento e metadados de manutenção; não reescreve intencionalmente pontas nem publica mudanças.

**Erros comuns:** Presumir --no-prune preserva todos dados de recuperação ou gc repara objetos corrompidos.

**Alternativas:** Use tarefa restrita de git maintenance run quando apropriado.

**Recuperação:** Confira referências e integridade após manutenção; recupere objetos necessários ausentes de backups verificados se possível.

**Versão e dependências:** Use Git 2.40 ou superior nos laboratórios; confira configuração e disponibilidade locais.

**Capítulos relacionados**

- [git-internals/08-gc-and-maintenance](../../git-internals/08-gc-and-maintenance/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-gc>

## git-maintenance-run

**`git maintenance run`**

**Tipo:** Subcomando

**Nível:** Avançado

**Pesquisar por intenção:** Manter um repositório

**Risco:** Alteração de estado. Selecione tarefas deliberadamente; não presuma manutenção arbitrária sem efeitos destrutivos ou de rede.

**Finalidade:** Executar tarefas de manutenção explicitamente selecionadas.

**Pré-requisitos:** Use repositório completo próprio descartável, referências verificadas, trabalho salvo e configuração confiável. Nunca use credenciais reais ou chaves pessoais em laboratórios.

**Opções:** --task=commit-graph seleciona manutenção de grafo; --auto pode executar tarefas configuradas necessárias. Outras tarefas têm efeitos diferentes.

**Quando utilizar:** Ao atualizar metadados locais de aceleração com tarefa direcionada.

**Quando evitar:** Evite tarefas amplas não revisadas ou agendamento global em ambiente compartilhado.

**Sintaxe**

`git maintenance run --task=commit-graph`

**Exemplo básico**

`git maintenance run --task=commit-graph`

Execute só manutenção commit-graph em repositório de prática ocioso.

**Exemplo profissional**

`git maintenance run --task=commit-graph`

Atualize metadados de grafo e inspecione depois.

**Impacto no estado**

- Working tree: Inalterado
- Index: Inalterado
- Objetos / refs / histórico: Inalterado
- Repositório remoto: Inalterado
- Outros estados: Altera

**Resultado esperado:** Tarefa selecionada atualiza metadados commit-graph conforme necessário sem mudar pontas.

**Impactos e efeitos colaterais:** Tarefa mostrada grava metadados de grafo; outras podem alterar armazenamento ou contatar remotos.

**Erros comuns:** Presumir run estabelece agendamento persistente ou toda tarefa é somente leitura.

**Alternativas:** Use git commit-graph verify para inspecionar validade de grafo.

**Recuperação:** Inspecione falha e integridade; repita só tarefa restrita após tratar causa.

**Versão e dependências:** Use Git 2.40 ou superior nos laboratórios; confira configuração e disponibilidade locais.

**Capítulos relacionados**

- [git-internals/08-gc-and-maintenance](../../git-internals/08-gc-and-maintenance/README.pt-BR.md)

**Documentação oficial**

- <https://git-scm.com/docs/git-maintenance>


---

<!-- navigation-footer -->
[Anterior](../12-internals-and-plumbing/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../14-platforms-and-automation/README.pt-BR.md)
<!-- /navigation-footer -->
