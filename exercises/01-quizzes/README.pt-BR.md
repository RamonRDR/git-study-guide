# Quizzes

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Módulo anterior](../../practical-projects/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../02-challenges/README.pt-BR.md)
<!-- /navigation -->

Tente primeiro, consulte as soluções públicas depois. Quizzes usam escolhas exatas; entrevistas e simulados exigem autoavaliação honesta. Desafios usam somente repositórios locais descartáveis novos e checks fixos de estado, sem executar automaticamente comandos de alunos. Registros são piloto interno, não contrato final do Learning Hub.

## Snapshot do commit

ID: quiz-snapshot

**Dificuldade:** fácil

**Pré-requisitos:** [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.pt-BR.md)

Prepare A, edite para B sem preparar e faça commit comum. Qual versão é registrada?

- a. A
- b. B
- c. Ambas

**Dicas:**

- Consulte o pré-requisito antes de decidir.
- Compare index e arquivo de trabalho.

**Resposta:** a

**Explicação:** O index contém A; B fica não preparado.

## Preparar arquivo

ID: quiz-add

**Dificuldade:** fácil

**Pré-requisitos:** [basic-commands/02-status-add-commit](../../basic-commands/02-status-add-commit/README.pt-BR.md)

Qual comando prepara notes.txt?

- a. git add notes.txt
- b. git log
- c. git branch

**Dicas:**

- Consulte o pré-requisito antes de decidir.
- O destino é o index.

**Resposta:** a

**Explicação:** Add copia conteúdo atual para o index.

## Diff preparado

ID: quiz-diff

**Dificuldade:** fácil

**Pré-requisitos:** [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.pt-BR.md)

Qual compara index com HEAD?

- a. git diff
- b. git diff --cached
- c. git log

**Dicas:**

- Consulte o pré-requisito antes de decidir.
- Procure a comparação preparada.

**Resposta:** b

**Explicação:** Diff cached mostra mudanças preparadas relativas a HEAD.

## Escopo de identidade

ID: quiz-config

**Dificuldade:** fácil

**Pré-requisitos:** [basic-commands/01-init-config-help](../../basic-commands/01-init-config-help/README.pt-BR.md)

Qual escopo afeta só o repositório atual?

- a. --global
- b. --system
- c. --local

**Dicas:**

- Consulte o pré-requisito antes de decidir.
- Evite alterar identidade de outros repos.

**Resposta:** c

**Explicação:** Configurações locais são específicas do repo.

## Criar e trocar

ID: quiz-switch

**Dificuldade:** fácil

**Pré-requisitos:** [branches/01-create-and-switch](../../branches/01-create-and-switch/README.pt-BR.md)

Qual cria e seleciona feat/notes?

- a. git branch feat/notes
- b. git switch -c feat/notes
- c. git switch main

**Dicas:**

- Consulte o pré-requisito antes de decidir.
- Procure ambas operações.

**Resposta:** b

**Explicação:** Só criar branch não a seleciona.

## HEAD

ID: quiz-head

**Dificuldade:** fácil

**Pré-requisitos:** [git-architecture/02-snapshots-head-and-refs](../../git-architecture/02-snapshots-head-and-refs/README.pt-BR.md)

Quando anexado à main, o que HEAD referencia?

- a. Ref da branch atual
- b. Servidor remoto
- c. Todos arquivos

**Dicas:**

- Consulte o pré-requisito antes de decidir.
- Considere a referência simbólica.

**Resposta:** a

**Explicação:** HEAD anexado é simbólico para branch selecionada.

## Regras de ignore

ID: quiz-ignore

**Dificuldade:** fácil

**Pré-requisitos:** [basic-commands/05-ignore-and-review](../../basic-commands/05-ignore-and-review/README.pt-BR.md)

.gitignore deixa de rastrear arquivo já rastreado?

- a. Sempre
- b. Após fetch
- c. Não

**Dicas:**

- Consulte o pré-requisito antes de decidir.
- Rastreamento depende do index.

**Resposta:** c

**Explicação:** Ignore não remove entradas existentes do index.

## Clonar

ID: quiz-clone

**Dificuldade:** fácil

**Pré-requisitos:** [remote-repositories/01-remote-concepts](../../remote-repositories/01-remote-concepts/README.pt-BR.md)

Qual cria cópia local normal de repo remoto?

- a. git init
- b. git clone
- c. git status

**Dicas:**

- Consulte o pré-requisito antes de decidir.
- Procure cópia de histórico existente.

**Resposta:** b

**Explicação:** Clone obtém histórico e normalmente configura origin.

## Status

ID: quiz-status

**Dificuldade:** fácil

**Pré-requisitos:** [basic-commands/02-status-add-commit](../../basic-commands/02-status-add-commit/README.pt-BR.md)

Qual inspeciona mudanças de working tree e index?

- a. git status
- b. git push
- c. git reset --hard

**Dicas:**

- Consulte o pré-requisito antes de decidir.
- Inspecione sem descartar edições.

**Resposta:** a

**Explicação:** Status relata mudanças preparadas, não preparadas e não rastreadas.

## Movimento da tag

ID: quiz-tag

**Dificuldade:** fácil

**Pré-requisitos:** [git-internals/03-commits-and-tags](../../git-internals/03-commits-and-tags/README.pt-BR.md)

O que ocorre com tag quando main avança?

- a. Avança
- b. Desaparece
- c. Mantém alvo

**Dicas:**

- Consulte o pré-requisito antes de decidir.
- Tag nomeia revisão.

**Resposta:** c

**Explicação:** Tags não avançam automaticamente com branches.

## Recurso de hospedagem

ID: quiz-hosting

**Dificuldade:** fácil

**Pré-requisitos:** [fundamentals/03-distributed-and-platforms](../../fundamentals/03-distributed-and-platforms/README.pt-BR.md)

Qual é recurso de plataforma e não objeto Git?

- a. Commit
- b. Pull request
- c. Blob

**Dicas:**

- Consulte o pré-requisito antes de decidir.
- Distinga hospedagem de armazenamento nativo.

**Resposta:** b

**Explicação:** PR é registro de colaboração na plataforma.

## Inspeção remota

ID: quiz-remote

**Dificuldade:** fácil

**Pré-requisitos:** [remote-repositories/01-remote-concepts](../../remote-repositories/01-remote-concepts/README.pt-BR.md)

Qual lista URLs fetch e push configuradas?

- a. git remote -v
- b. git branch -d main
- c. git push

**Dicas:**

- Consulte o pré-requisito antes de decidir.
- Leia configuração sem transmitir commits.

**Resposta:** a

**Explicação:** Remote -v lista URLs sem publicar.

## Fetch

ID: quiz-fetch

**Dificuldade:** médio

**Pré-requisitos:** [remote-repositories/02-fetch-and-tracking](../../remote-repositories/02-fetch-and-tracking/README.pt-BR.md)

Com refspec usual, o que ocorre ao buscar nova main remota?

- a. Main local sempre avança
- b. Tracking atualiza; main selecionada não muda
- c. Commits locais somem

**Dicas:**

- Consulte o pré-requisito antes de decidir.
- Distinga ref tracking da branch local.

**Resposta:** b

**Explicação:** Fetch atualiza refs configuradas; integração é separada.

## Só fast-forward

ID: quiz-ff

**Dificuldade:** médio

**Pré-requisitos:** [merge-and-conflicts/02-fast-forward](../../merge-and-conflicts/02-fast-forward/README.pt-BR.md)

Pontas divergiram. O que merge --ff-only faz?

- a. Recusa
- b. Cria commit merge
- c. Faz rebase

**Dicas:**

- Consulte o pré-requisito antes de decidir.
- Confira ancestralidade.

**Resposta:** a

**Explicação:** Fast-forward não une históricos divergentes.

## Pais do merge

ID: quiz-parents

**Dificuldade:** médio

**Pré-requisitos:** [merge-and-conflicts/03-merge-commit](../../merge-and-conflicts/03-merge-commit/README.pt-BR.md)

Quantos pais tem commit de merge comum de duas branches sem fast-forward?

- a. 1
- b. 3
- c. 2

**Dicas:**

- Consulte o pré-requisito antes de decidir.
- Ambos históricos permanecem conectados.

**Resposta:** c

**Explicação:** Pais são ponta atual anterior e ponta integrada.

## Estágios de conflito

ID: quiz-conflict

**Dificuldade:** médio

**Pré-requisitos:** [merge-and-conflicts/04-conflict-resolution](../../merge-and-conflicts/04-conflict-resolution/README.pt-BR.md)

Qual lista entradas não mescladas do index?

- a. git commit
- b. git ls-files -u
- c. git clean -n

**Dicas:**

- Consulte o pré-requisito antes de decidir.
- Inspecione index, não log de commits.

**Resposta:** b

**Explicação:** Index pode conter estágios base, ours e theirs.

## Retirar do staging

ID: quiz-unstage

**Dificuldade:** médio

**Pré-requisitos:** [history-and-recovery/02-restore](../../history-and-recovery/02-restore/README.pt-BR.md)

Com HEAD existente, qual retira notes.txt do staging sem descartar edições?

- a. git restore --staged -- notes.txt
- b. git restore --worktree -- notes.txt
- c. git reset --hard HEAD

**Dicas:**

- Consulte o pré-requisito antes de decidir.
- Arquivo de trabalho deve permanecer.

**Resposta:** a

**Explicação:** Restore --staged usa HEAD por padrão e altera só index.

## Reset soft

ID: quiz-soft

**Dificuldade:** médio

**Pré-requisitos:** [history-and-recovery/03-reset](../../history-and-recovery/03-reset/README.pt-BR.md)

O que reset --soft preserva ao mover branch privada?

- a. Só estado remoto
- b. Nada
- c. Index e working tree

**Dicas:**

- Consulte o pré-requisito antes de decidir.
- Modos afetam locais diferentes.

**Resposta:** c

**Explicação:** Reset soft move HEAD/branch e mantém index e arquivos.

## Desfazer compartilhado

ID: quiz-revert

**Dificuldade:** médio

**Pré-requisitos:** [history-and-recovery/04-revert](../../history-and-recovery/04-revert/README.pt-BR.md)

Qual desfaz commit comum compartilhado sem reescrever histórico publicado?

- a. git reset --hard
- b. git revert
- c. git push --force

**Dicas:**

- Consulte o pré-requisito antes de decidir.
- Preserve ancestralidade existente.

**Resposta:** b

**Explicação:** Revert registra mudança inversa em novo commit.

## Escopo stash

ID: quiz-stash

**Dificuldade:** médio

**Pré-requisitos:** [history-and-recovery/06-stash](../../history-and-recovery/06-stash/README.pt-BR.md)

Qual opção stash push inclui não rastreados mas não ignorados?

- a. -u
- b. --keep-index
- c. --all

**Dicas:**

- Consulte o pré-requisito antes de decidir.
- Não rastreado não é igual a ignorado.

**Resposta:** a

**Explicação:** -u inclui não rastreados; --all inclui também ignorados.

## Cherry-pick

ID: quiz-pick

**Dificuldade:** médio

**Pré-requisitos:** [history-and-recovery/07-cherry-pick](../../history-and-recovery/07-cherry-pick/README.pt-BR.md)

Cherry-pick comum bem-sucedido de commit não vazio sobre outra ponta costuma criar o quê?

- a. Novo commit com mudanças aplicadas
- b. Branch remota
- c. Merge com dois pais

**Dicas:**

- Consulte o pré-requisito antes de decidir.
- Considere aplicar mudança em vez de unir histórico.

**Resposta:** a

**Explicação:** Patch aplicado em novo contexto de pai.

## Reflog

ID: quiz-reflog

**Dificuldade:** médio

**Pré-requisitos:** [history-and-recovery/05-reflog](../../history-and-recovery/05-reflog/README.pt-BR.md)

Push normal transfere seu reflog local?

- a. Sim
- b. Não
- c. Só com tags

**Dicas:**

- Consulte o pré-requisito antes de decidir.
- Distinga transferência de objetos de metadados locais.

**Resposta:** b

**Explicação:** Reflogs são metadados locais e podem expirar.

## Revisão da revisão

ID: quiz-review

**Dificuldade:** médio

**Pré-requisitos:** [github/04-pull-requests-and-review](../../github/04-pull-requests-and-review/README.pt-BR.md)

Novo commit chega ao PR após checks verdes. Qual revisão precisa verificação?

- a. Primeiro commit
- b. Qualquer revisão verde
- c. Head pretendido mais recente

**Dicas:**

- Consulte o pré-requisito antes de decidir.
- Evidência deve identificar SHA testado.

**Resposta:** c

**Explicação:** Checks de revisões antigas não cobrem mudanças novas.

## Credencial exposta

ID: quiz-secret

**Dificuldade:** médio

**Pré-requisitos:** [security/05-secrets-and-disclosure-prevention](../../security/05-secrets-and-disclosure-prevention/README.pt-BR.md)

Token real entrou em histórico público. Qual ação essencial vem primeiro?

- a. Revogar ou rotacionar
- b. Só excluir arquivo
- c. Renomear branch

**Dicas:**

- Consulte o pré-requisito antes de decidir.
- Cópias fora do repo podem persistir.

**Resposta:** a

**Explicação:** Presuma comprometimento; limpeza de histórico é separada de invalidação.

## Identidade no rebase

ID: quiz-rebase

**Dificuldade:** difícil

**Pré-requisitos:** [merge-and-conflicts/06-rebase-and-conflicts](../../merge-and-conflicts/06-rebase-and-conflicts/README.pt-BR.md)

Rebase de commits sobre pai diferente normalmente muda o quê?

- a. Só permissões
- b. IDs de commits reaplicados
- c. Remoto automaticamente

**Dicas:**

- Consulte o pré-requisito antes de decidir.
- Pense no pai armazenado.

**Resposta:** b

**Explicação:** Objetos commit incluem IDs de pais; reaplicação cria novos objetos conforme necessário.

## Squash

ID: quiz-squash

**Dificuldade:** difícil

**Pré-requisitos:** [merge-and-conflicts/05-squash-merge](../../merge-and-conflicts/05-squash-merge/README.pt-BR.md)

Após merge --squash bem-sucedido, antes de commit, o que é verdade?

- a. HEAD moveu
- b. MERGE\_HEAD guarda segundo pai
- c. Mudanças preparadas; HEAD inalterado

**Dicas:**

- Consulte o pré-requisito antes de decidir.
- Commit é etapa separada.

**Resposta:** c

**Explicação:** Squash prepara mudanças sem criar MERGE\_HEAD nem mover HEAD.

## Diff de três pontos

ID: quiz-three-dot

**Dificuldade:** difícil

**Pré-requisitos:** [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.pt-BR.md)

Com uma merge base, o que git diff main...feature compara?

- a. Merge base à ponta feature
- b. Ponta feature à main
- c. Index a HEAD

**Dicas:**

- Consulte o pré-requisito antes de decidir.
- Primeiro ponto deriva da ancestralidade.

**Resposta:** a

**Explicação:** Diff três pontos compara merge base à segunda ponta; log difere.

## Force-with-lease

ID: quiz-lease

**Dificuldade:** difícil

**Pré-requisitos:** [remote-repositories/03-pull-push-and-divergence](../../remote-repositories/03-pull-push-and-divergence/README.pt-BR.md)

Contra o que lease de OID esperado explícito protege?

- a. Toda perda de dados
- b. Ref remota diferente do esperado
- c. Todos conflitos merge

**Dicas:**

- Consulte o pré-requisito antes de decidir.
- Compare ref atual com expectativa.

**Resposta:** b

**Explicação:** Lease é condicional, não garantia contra reescritas prejudiciais.

## Bisect

ID: quiz-bisect

**Dificuldade:** difícil

**Pré-requisitos:** [advanced-git/01-bisect](../../advanced-git/01-bisect/README.pt-BR.md)

O que teste útil de bisect precisa classificar?

- a. Popularidade do autor
- b. Tamanho de arquivo
- c. Propriedade alvo da revisão selecionada

**Dicas:**

- Consulte o pré-requisito antes de decidir.
- Teste a revisão, não metadados alheios.

**Resposta:** c

**Explicação:** Classificação good/bad consistente reduz fronteira conhecida; pule incerteza.

## Identidade do blob

ID: quiz-blob

**Dificuldade:** difícil

**Pré-requisitos:** [git-internals/02-blobs-and-trees](../../git-internals/02-blobs-and-trees/README.pt-BR.md)

Dois arquivos têm bytes blob armazenados iguais no mesmo formato. O que pode diferir?

- a. Caminho e modo tree
- b. Bytes armazenados
- c. Tipo objeto blob

**Dicas:**

- Consulte o pré-requisito antes de decidir.
- Qual objeto guarda nomes?

**Resposta:** a

**Explicação:** Blob guarda conteúdo; tree guarda nomes e modos.

## Peeling de tag

ID: quiz-peel

**Dificuldade:** difícil

**Pré-requisitos:** [git-internals/03-commits-and-tags](../../git-internals/03-commits-and-tags/README.pt-BR.md)

O que git rev-parse 'v1.0.0^{commit}' solicita de tag apontando a commit?

- a. Mensagem da tag
- b. ID do commit subjacente
- c. Caminho de trabalho

**Dicas:**

- Consulte o pré-requisito antes de decidir.
- Distinga objeto tag de seu alvo.

**Resposta:** b

**Explicação:** Peeling resolve a commit ou falha.

## Alcançabilidade

ID: quiz-reachable

**Dificuldade:** difícil

**Pré-requisitos:** [git-internals/09-reflogs-and-reachability](../../git-internals/09-reflogs-and-reachability/README.pt-BR.md)

Por que nomear commit deslocado encontrado no reflog com branch de recuperação?

- a. Desabilitar todo GC
- b. Copiar arquivos não registrados
- c. Tornar commit alcançável via ref

**Dicas:**

- Consulte o pré-requisito antes de decidir.
- Pense em referência persistente.

**Resposta:** c

**Explicação:** Branch torna commit alcançável independente de entradas temporárias de reflog.

## Worktree

ID: quiz-worktree

**Dificuldade:** difícil

**Pré-requisitos:** [advanced-git/02-worktree](../../advanced-git/02-worktree/README.pt-BR.md)

O que normalmente é separado em worktrees vinculadas?

- a. Arquivos de trabalho, HEAD e index
- b. Todo objeto Git
- c. Todas refs de branch

**Dicas:**

- Consulte o pré-requisito antes de decidir.
- Distinga armazenamento compartilhado de checkout.

**Resposta:** a

**Explicação:** Worktrees compartilham objetos e maioria das refs, mas têm HEAD/index/arquivos próprios.

## Gitlink

ID: quiz-gitlink

**Dificuldade:** difícil

**Pré-requisitos:** [advanced-git/03-submodules](../../advanced-git/03-submodules/README.pt-BR.md)

O que gitlink de superprojeto registra?

- a. Todos arquivos aninhados
- b. ID de commit do submódulo
- c. Só nome de branch

**Dicas:**

- Consulte o pré-requisito antes de decidir.
- Dependência é fixada a uma revisão.

**Resposta:** b

**Explicação:** Gitlink guarda commit referenciado, não tree aninhada.

## Limites de assinatura

ID: quiz-signature

**Dificuldade:** difícil

**Pré-requisitos:** [security/09-commit-and-tag-signing](../../security/09-commit-and-tag-signing/README.pt-BR.md)

Assinatura criptográfica válida sozinha prova segurança e autorização?

- a. Sempre
- b. Se main
- c. Não

**Dicas:**

- Consulte o pré-requisito antes de decidir.
- Identifique o que assinatura atesta.

**Resposta:** c

**Explicação:** Verificação criptográfica difere de política de confiança e revisão.

## Clone parcial

ID: quiz-partial

**Dificuldade:** difícil

**Pré-requisitos:** [advanced-git/08-partial-and-shallow-clone](../../advanced-git/08-partial-and-shallow-clone/README.pt-BR.md)

Por que acesso posterior a arquivo em clone parcial blob:none pode exigir rede?

- a. Blobs prometidos podem exigir fetch sob demanda
- b. Todos commits foram excluídos
- c. Todos comandos são chamadas API remota

**Dicas:**

- Consulte o pré-requisito antes de decidir.
- Transferência inicial pode ser incompleta por projeto.

**Resposta:** a

**Explicação:** Objetos prometidos ausentes podem ser buscados sob demanda.

---

<!-- navigation-footer -->
[Módulo anterior](../../practical-projects/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../02-challenges/README.pt-BR.md)
<!-- /navigation-footer -->
