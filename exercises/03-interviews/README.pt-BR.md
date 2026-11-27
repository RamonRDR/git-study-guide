# Perguntas de entrevista

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../02-challenges/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../04-mock-assessments/README.pt-BR.md)
<!-- /navigation -->

Tente primeiro, consulte as soluções públicas depois. Quizzes usam escolhas exatas; entrevistas e simulados exigem autoavaliação honesta. Desafios usam somente repositórios locais descartáveis novos e checks fixos de estado, sem executar automaticamente comandos de alunos. Registros são piloto interno, não contrato final do Learning Hub.

## Controle de versão

ID: interview-version-control

**Dificuldade:** fácil

**Pré-requisitos:** [fundamentals/01-version-control](../../fundamentals/01-version-control/README.pt-BR.md)

Explique por que Git é útil mesmo trabalhando sozinho.

**Dicas:**

- Explique estado ou política relevante antes de citar comandos.
- Cite snapshots e comparação.

**Resposta esperada:** Git registra snapshots intencionais, permite comparar revisões e experimentar isoladamente. Não salva toda edição automaticamente nem substitui backups.

**Rubrica:**

- Cite snapshots e comparação.
- Explique limite de trabalho sem commit.

**Complementos:**

- Como inspecionaria revisão anterior?

**Explicação:** Compare seu raciocínio à resposta esperada. Rubrica mede conceitos explícitos, não palavras exatas; atribua um ponto por critério atendido, zero caso contrário.

## Três locais do Git

ID: interview-three-states

**Dificuldade:** fácil

**Pré-requisitos:** [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.pt-BR.md)

Explique working tree, index e HEAD usando um arquivo editado.

**Dicas:**

- Explique estado ou política relevante antes de citar comandos.
- Defina corretamente os três locais.

**Resposta esperada:** Working tree é conteúdo editável, index prepara próximo commit comum, HEAD resolve revisão atual. Prepare A, edite B, commit: A registrado, B não preparado.

**Rubrica:**

- Defina corretamente os três locais.
- Rastreie A e B sem confundir.

**Complementos:**

- Qual diff mostra A relativo a HEAD?

**Explicação:** Compare seu raciocínio à resposta esperada. Rubrica mede conceitos explícitos, não palavras exatas; atribua um ponto por critério atendido, zero caso contrário.

## Branch como ref

ID: interview-branch

**Dificuldade:** fácil

**Pré-requisitos:** [branches/01-create-and-switch](../../branches/01-create-and-switch/README.pt-BR.md)

O que é branch e o que ocorre ao registrar commit nela?

**Dicas:**

- Explique estado ou política relevante antes de citar comandos.
- Descreva ref, não cópia de pasta.

**Resposta esperada:** Branch local é ref móvel para commit. Com HEAD anexado, commit comum atualiza branch atual enquanto outras refs normalmente ficam iguais.

**Rubrica:**

- Descreva ref, não cópia de pasta.
- Distinga criação de seleção de branch.

**Complementos:**

- O que difere em detached HEAD?

**Explicação:** Compare seu raciocínio à resposta esperada. Rubrica mede conceitos explícitos, não palavras exatas; atribua um ponto por critério atendido, zero caso contrário.

## Inspecionar antes do commit

ID: interview-status-diff

**Dificuldade:** fácil

**Pré-requisitos:** [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.pt-BR.md)

Como revisar o que entrará em commit comum?

**Dicas:**

- Explique estado ou política relevante antes de citar comandos.
- Identifique comparação preparada.

**Resposta esperada:** Use git status para estado, git diff para edições rastreadas não preparadas e git diff --cached para index contra HEAD. Prepare só arquivos desejados e confira.

**Rubrica:**

- Identifique comparação preparada.
- Mencione não rastreados e staging seletivo.

**Complementos:**

- Por que git diff pode estar vazio com mudanças preparadas?

**Explicação:** Compare seu raciocínio à resposta esperada. Rubrica mede conceitos explícitos, não palavras exatas; atribua um ponto por critério atendido, zero caso contrário.

## Ignore e rastreamento

ID: interview-ignore

**Dificuldade:** fácil

**Pré-requisitos:** [basic-commands/05-ignore-and-review](../../basic-commands/05-ignore-and-review/README.pt-BR.md)

Por que arquivo rastreado ainda aparece após regra ignore?

**Dicas:**

- Explique estado ou política relevante antes de citar comandos.
- Distinga ignorado de rastreado.

**Resposta esperada:** Ignore normalmente filtra caminhos não rastreados. Arquivos rastreados continuam no index até remoção intencional do rastreamento. Revise efeitos antes do commit.

**Rubrica:**

- Distinga ignorado de rastreado.
- Explique que histórico não é apagado.

**Complementos:**

- O que git rm --cached altera?

**Explicação:** Compare seu raciocínio à resposta esperada. Rubrica mede conceitos explícitos, não palavras exatas; atribua um ponto por critério atendido, zero caso contrário.

## Init e clone

ID: interview-clone-init

**Dificuldade:** fácil

**Pré-requisitos:** [remote-repositories/01-remote-concepts](../../remote-repositories/01-remote-concepts/README.pt-BR.md)

Quando escolher init em vez de clone?

**Dicas:**

- Explique estado ou política relevante antes de citar comandos.
- Explique histórico novo versus existente.

**Resposta esperada:** Init inicia metadados Git em repo escolhido; clone obtém histórico de repo existente e normalmente configura origin e checkout. Evite diretório errado.

**Rubrica:**

- Explique histórico novo versus existente.
- Identifique origin como configuração usual.

**Complementos:**

- Como verificar raiz do repo?

**Explicação:** Compare seu raciocínio à resposta esperada. Rubrica mede conceitos explícitos, não palavras exatas; atribua um ponto por critério atendido, zero caso contrário.

## Comunicar mudança

ID: interview-commit-message

**Dificuldade:** fácil

**Pré-requisitos:** [professional-workflows/06-conventional-commits](../../professional-workflows/06-conventional-commits/README.pt-BR.md)

O que torna uma mensagem de commit útil?

**Dicas:**

- Explique estado ou política relevante antes de citar comandos.
- Dê exemplo focado como docs: clarify notes.

**Resposta esperada:** Descreva intenção focada e, quando útil, motivo. Conventional Commits é convenção de equipe, não requisito Git. Não inclua segredos nem mudanças alheias.

**Rubrica:**

- Dê exemplo focado como docs: clarify notes.
- Separe convenção de requisitos Git.

**Complementos:**

- Quando duas mudanças devem ser commits separados?

**Explicação:** Compare seu raciocínio à resposta esperada. Rubrica mede conceitos explícitos, não palavras exatas; atribua um ponto por critério atendido, zero caso contrário.

## Git e plataforma

ID: interview-platform

**Dificuldade:** fácil

**Pré-requisitos:** [fundamentals/03-distributed-and-platforms](../../fundamentals/03-distributed-and-platforms/README.pt-BR.md)

Git funciona sem GitHub ou GitLab? Explique.

**Dicas:**

- Explique estado ou política relevante antes de citar comandos.
- Identifique operações locais nativas.

**Resposta esperada:** Sim. Git armazena e manipula repos locais e troca objetos com remotos. Hospedagem adiciona acesso, revisões PR/MR e CI; contas não são necessárias localmente.

**Rubrica:**

- Identifique operações locais nativas.
- Cite recursos de colaboração da plataforma.

**Complementos:**

- Como dois desenvolvedores praticam offline?

**Explicação:** Compare seu raciocínio à resposta esperada. Rubrica mede conceitos explícitos, não palavras exatas; atribua um ponto por critério atendido, zero caso contrário.

## Fetch e pull

ID: interview-fetch-pull

**Dificuldade:** médio

**Pré-requisitos:** [remote-repositories/02-fetch-and-tracking](../../remote-repositories/02-fetch-and-tracking/README.pt-BR.md)

Ref tracking desatualizada. Como atualizar antes de decidir integração?

**Dicas:**

- Explique estado ou política relevante antes de citar comandos.
- Distinga fetch de integração.

**Resposta esperada:** Faça fetch origin, inspecione divergência de main e origin/main, depois escolha política. Pull combina fetch e integração conforme opções/config; ff-only recusa divergência.

**Rubrica:**

- Distinga fetch de integração.
- Descreva decisão segura em divergência.

**Complementos:**

- Por que pull pode falhar mesmo após fetch passar?

**Explicação:** Compare seu raciocínio à resposta esperada. Rubrica mede conceitos explícitos, não palavras exatas; atribua um ponto por critério atendido, zero caso contrário.

## Merge ou rebase

ID: interview-merge-rebase

**Dificuldade:** médio

**Pré-requisitos:** [merge-and-conflicts/06-rebase-and-conflicts](../../merge-and-conflicts/06-rebase-and-conflicts/README.pt-BR.md)

Compare merge e rebase para branch feature.

**Dicas:**

- Explique estado ou política relevante antes de citar comandos.
- Explique diferenças de topologia e identidade.

**Resposta esperada:** Merge integra históricos, às vezes por fast-forward ou commit merge. Rebase reaplica commits em nova base e normalmente muda IDs reaplicados. Evite reescrever histórico compartilhado sem coordenação.

**Rubrica:**

- Explique diferenças de topologia e identidade.
- Discuta política de equipe e histórico compartilhado.

**Complementos:**

- Quando fast-forward é possível?

**Explicação:** Compare seu raciocínio à resposta esperada. Rubrica mede conceitos explícitos, não palavras exatas; atribua um ponto por critério atendido, zero caso contrário.

## Triagem de conflito

ID: interview-resolve

**Dificuldade:** médio

**Pré-requisitos:** [merge-and-conflicts/04-conflict-resolution](../../merge-and-conflicts/04-conflict-resolution/README.pt-BR.md)

Descreva processo seguro para resolver conflito merge.

**Dicas:**

- Explique estado ou política relevante antes de citar comandos.
- Explique inspeção e resolução intencional.

**Resposta esperada:** Inspecione status e entradas não mescladas, entenda base/ours/theirs, escolha conteúdo correto, prepare resolução, rode testes e conclua. Preserve edições desejadas antes de abortar.

**Rubrica:**

- Explique inspeção e resolução intencional.
- Mencione testes e limites do abort seguro.

**Complementos:**

- Por que excluir marcadores não basta?

**Explicação:** Compare seu raciocínio à resposta esperada. Rubrica mede conceitos explícitos, não palavras exatas; atribua um ponto por critério atendido, zero caso contrário.

## Reset e revert

ID: interview-reset-revert

**Dificuldade:** médio

**Pré-requisitos:** [history-and-recovery/03-reset](../../history-and-recovery/03-reset/README.pt-BR.md)

Como desfazer commit privado versus publicado?

**Dicas:**

- Explique estado ou política relevante antes de citar comandos.
- Compare mover refs e criar novo commit.

**Resposta esperada:** Em histórico privado, inspecione estado e escolha modo reset só com alvo conhecido e trabalho preservado. Em histórico publicado, prefira revert/commit corretivo revisado. Hard reset pode descartar edições.

**Rubrica:**

- Compare mover refs e criar novo commit.
- Cite riscos destrutivos e política compartilhada.

**Complementos:**

- O que reset soft preserva?

**Explicação:** Compare seu raciocínio à resposta esperada. Rubrica mede conceitos explícitos, não palavras exatas; atribua um ponto por critério atendido, zero caso contrário.

## Limites do stash

ID: interview-stash

**Dificuldade:** médio

**Pré-requisitos:** [history-and-recovery/06-stash](../../history-and-recovery/06-stash/README.pt-BR.md)

O que conferir antes de usar stash para trocar tarefas? Explique o escopo de arquivos não rastreados e ignorados e como apply difere de pop em sucesso ou conflito.

**Dicas:**

- Explique estado ou política relevante antes de citar comandos.
- Mencione escopo não rastreado/ignorado.

**Resposta esperada:** Inspecione arquivos preparados, não preparados e não rastreados. Por padrão stash push guarda mudanças rastreadas; -u inclui não rastreados e --all também inclui ignorados. Escolha o escopo deliberadamente, registre a entrada e confira o estado de trabalho. Apply tenta restaurar mudanças mantendo a entrada do stash; pop a remove após aplicação bem-sucedida, mas a mantém se conflitos impedirem a aplicação. Inspecione e resolva conflitos antes de qualquer drop deliberado. Stash é local, não backup durável.

**Rubrica:**

- Mencione escopo não rastreado/ignorado.
- Distinga apply e pop em sucesso/conflito.

**Complementos:**

- Por que apply pode conflitar?

**Explicação:** Compare seu raciocínio à resposta esperada. Rubrica mede conceitos explícitos, não palavras exatas; atribua um ponto por critério atendido, zero caso contrário.

## Contribuição via fork

ID: interview-fork

**Dificuldade:** médio

**Pré-requisitos:** [github/05-forks-and-open-source](../../github/05-forks-and-open-source/README.pt-BR.md)

Descreva fluxo de contribuição sem permissão push upstream.

**Dicas:**

- Explique estado ou política relevante antes de citar comandos.
- Distinga destinos origin e upstream.

**Resposta esperada:** Faça fork ou use repo contribuinte autorizado, clone, nomeie upstream separado, baseie feature em revisão upstream conhecida, publique só no fork e solicite revisão. Respeite política e confira diff exato.

**Rubrica:**

- Distinga destinos origin e upstream.
- Descreva limites de permissão e revisão.

**Complementos:**

- Como sincronizar fork com segurança?

**Explicação:** Compare seu raciocínio à resposta esperada. Rubrica mede conceitos explícitos, não palavras exatas; atribua um ponto por critério atendido, zero caso contrário.

## Gate de qualidade CI

ID: interview-ci-gate

**Dificuldade:** médio

**Pré-requisitos:** [ci-cd/09-quality-gates-and-troubleshooting](../../ci-cd/09-quality-gates-and-troubleshooting/README.pt-BR.md)

Job CI falha após push. Como diagnosticar?

**Dicas:**

- Explique estado ou política relevante antes de citar comandos.
- Use logs reais e revisão exata.

**Resposta esperada:** Identifique SHA, job e step falho, inspecione logs, reproduza em ambiente isolado se possível, corrija causa e rode checks no novo SHA. Não desabilite gates para obter verde.

**Rubrica:**

- Use logs reais e revisão exata.
- Exija nova execução após mudanças.

**Complementos:**

- Teste verde comprova deploy bem-sucedido?

**Explicação:** Compare seu raciocínio à resposta esperada. Rubrica mede conceitos explícitos, não palavras exatas; atribua um ponto por critério atendido, zero caso contrário.

## Versionamento de release

ID: interview-release

**Dificuldade:** médio

**Pré-requisitos:** [professional-workflows/07-semantic-versioning](../../professional-workflows/07-semantic-versioning/README.pt-BR.md)

Como decidir versão SemVer e identificar revisão da release?

**Dicas:**

- Explique estado ou política relevante antes de citar comandos.
- Baseie versão no contrato público.

**Resposta esperada:** Com API/contrato público definido, escolha major para incompatibilidade, minor para funcionalidade retrocompatível, patch para correções compatíveis. Revise e teste revisão exata, depois tag anotada conforme política. Release hospedada é distinta.

**Rubrica:**

- Baseie versão no contrato público.
- Distinga tag de release de plataforma.

**Complementos:**

- E se tag publicada estiver errada?

**Explicação:** Compare seu raciocínio à resposta esperada. Rubrica mede conceitos explícitos, não palavras exatas; atribua um ponto por critério atendido, zero caso contrário.

## Modelo de objetos

ID: interview-objects

**Dificuldade:** difícil

**Pré-requisitos:** [git-internals/02-blobs-and-trees](../../git-internals/02-blobs-and-trees/README.pt-BR.md)

Rastreie commit até conteúdo armazenado dos arquivos.

**Dicas:**

- Explique estado ou política relevante antes de citar comandos.
- Descreva papéis commit, tree e blob.

**Resposta esperada:** Commit referencia tree raiz e pais. Trees registram nomes, modos e IDs, referenciando trees/blobs recursivamente. Blobs guardam bytes, não nomes. Refs nomeiam commits independentemente de armazenamento físico.

**Rubrica:**

- Descreva papéis commit, tree e blob.
- Explique por que conteúdo idêntico pode compartilhar blob.

**Complementos:**

- De que hash de commit depende além da tree?

**Explicação:** Compare seu raciocínio à resposta esperada. Rubrica mede conceitos explícitos, não palavras exatas; atribua um ponto por critério atendido, zero caso contrário.

## Recuperabilidade

ID: interview-recovery

**Dificuldade:** difícil

**Pré-requisitos:** [git-internals/09-reflogs-and-reachability](../../git-internals/09-reflogs-and-reachability/README.pt-BR.md)

Ponta privada sumiu após reset. Explique recuperação e limites.

**Dicas:**

- Explique estado ou política relevante antes de citar comandos.
- Explique recuperação via ref verificada.

**Resposta esperada:** Pare operações destrutivas; inspecione reflog e IDs conhecidos, confira conteúdo e ancestralidade, crie ref de recuperação e verifique. Reflogs expiram e objetos inalcançáveis podem ser podados; edições sem commit talvez nunca registradas.

**Rubrica:**

- Explique recuperação via ref verificada.
- Rejeite explicitamente garantia de recuperação.

**Complementos:**

- Por que evitar gc durante recuperação?

**Explicação:** Compare seu raciocínio à resposta esperada. Rubrica mede conceitos explícitos, não palavras exatas; atribua um ponto por critério atendido, zero caso contrário.

## Atualização remota concorrente

ID: interview-lease

**Dificuldade:** difícil

**Pré-requisitos:** [remote-repositories/03-pull-push-and-divergence](../../remote-repositories/03-pull-push-and-divergence/README.pt-BR.md)

Explique por que force-with-lease é mais seguro que force, mas não política suficiente.

**Dicas:**

- Explique estado ou política relevante antes de citar comandos.
- Descreva comparação condicional de ref.

**Resposta esperada:** Lease compara ref remota com valor esperado e recusa divergência. Expectativa explícita evita depender de refs tracking atualizadas por fetch de fundo. Mesmo lease aceito pode descartar histórico; exija propriedade, coordenação e política.

**Rubrica:**

- Descreva comparação condicional de ref.
- Explique por que lease aceito não é consentimento.

**Complementos:**

- O que fazer se lease falhar?

**Explicação:** Compare seu raciocínio à resposta esperada. Rubrica mede conceitos explícitos, não palavras exatas; atribua um ponto por critério atendido, zero caso contrário.

## Checkout paralelo

ID: interview-worktree

**Dificuldade:** difícil

**Pré-requisitos:** [advanced-git/02-worktree](../../advanced-git/02-worktree/README.pt-BR.md)

Como inspecionar release enquanto desenvolve feature?

**Dicas:**

- Explique estado ou política relevante antes de citar comandos.
- Identifique estado compartilhado e independente.

**Resposta esperada:** Worktree vinculada oferece arquivos, HEAD e index separados, compartilhando objetos e muitas refs. Crie branch separada adequada ou worktree detached, confira caminho e remova só worktree própria limpa.

**Rubrica:**

- Identifique estado compartilhado e independente.
- Explique seleção segura de branch/caminho e limpeza.

**Complementos:**

- Por que não selecionar mesma branch duas vezes por padrão?

**Explicação:** Compare seu raciocínio à resposta esperada. Rubrica mede conceitos explícitos, não palavras exatas; atribua um ponto por critério atendido, zero caso contrário.

## Dependência fixada

ID: interview-submodules

**Dificuldade:** difícil

**Pré-requisitos:** [advanced-git/03-submodules](../../advanced-git/03-submodules/README.pt-BR.md)

Explique o que atualização de submódulo significa para reprodutibilidade.

**Dicas:**

- Explique estado ou política relevante antes de citar comandos.
- Explique papéis gitlink e configuração.

**Resposta esperada:** Superprojeto guarda gitlink para commit específico e .gitmodules descreve configuração. Checkout reproduzível exige commit disponível e inicialização/update adequados. Atualizar checkout aninhado sozinho não registra dependência no superprojeto.

**Rubrica:**

- Explique papéis gitlink e configuração.
- Mencione disponibilidade e commit da fixação.

**Complementos:**

- O que ocorre se commit referenciado indisponível?

**Explicação:** Compare seu raciocínio à resposta esperada. Rubrica mede conceitos explícitos, não palavras exatas; atribua um ponto por critério atendido, zero caso contrário.

## Busca de regressão

ID: interview-bisect

**Dificuldade:** difícil

**Pré-requisitos:** [advanced-git/01-bisect](../../advanced-git/01-bisect/README.pt-BR.md)

Como projetar experimento confiável de git bisect?

**Dicas:**

- Explique estado ou política relevante antes de citar comandos.
- Defina good/bad e teste confiável.

**Resposta esperada:** Estabeleça fronteira good/bad conhecida, use classificação determinística estável por revisão, pule commits realmente não testáveis, registre ambiente/evidência, confira candidato e encerre bisect. Comportamento não monotônico pode complicar resultados.

**Rubrica:**

- Defina good/bad e teste confiável.
- Discuta skip, verificação e limpeza.

**Complementos:**

- E se teste for instável?

**Explicação:** Compare seu raciocínio à resposta esperada. Rubrica mede conceitos explícitos, não palavras exatas; atribua um ponto por critério atendido, zero caso contrário.

## Integração baseada em evidência

ID: interview-audit

**Dificuldade:** difícil

**Pré-requisitos:** [security/12-governance-audit-and-traceability](../../security/12-governance-audit-and-traceability/README.pt-BR.md)

Como provar commit squash integrado corresponde à mudança revisada?

**Dicas:**

- Explique estado ou política relevante antes de citar comandos.
- Associe evidência a SHA e base exatos.

**Resposta esperada:** Registre head/tree revisados e base, confira checks/revisão e autorização para SHA, exija head esperado no merge. Se base não mudou e feature a inclui, compare tree integrada à revisada e pai único à base; confira pós-merge e metadados.

**Rubrica:**

- Associe evidência a SHA e base exatos.
- Explique igualdade de tree condicionada à base inalterada.

**Complementos:**

- Por que base diferente pode exigir nova revisão?

**Explicação:** Compare seu raciocínio à resposta esperada. Rubrica mede conceitos explícitos, não palavras exatas; atribua um ponto por critério atendido, zero caso contrário.

## Incidente de credencial

ID: interview-secret-incident

**Dificuldade:** difícil

**Pré-requisitos:** [security/11-credential-exposure-and-incident-response](../../security/11-credential-exposure-and-incident-response/README.pt-BR.md)

Responda a credencial registrada e publicada por acidente.

**Dicas:**

- Explique estado ou política relevante antes de citar comandos.
- Priorize revogação antes de limpeza do histórico.

**Resposta esperada:** Trate como comprometida: revogue/rotacione, limite exposição e notifique responsáveis, investigue uso, remova segredo de arquivos atuais e coordene limpeza de histórico. Cópias podem persistir; prevenção inclui scanning e menor privilégio.

**Rubrica:**

- Priorize revogação antes de limpeza do histórico.
- Reconheça cópias persistentes e coordenação do incidente.

**Complementos:**

- Por que excluir arquivo não basta?

**Explicação:** Compare seu raciocínio à resposta esperada. Rubrica mede conceitos explícitos, não palavras exatas; atribua um ponto por critério atendido, zero caso contrário.

---

<!-- navigation-footer -->
[Anterior](../02-challenges/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../04-mock-assessments/README.pt-BR.md)
<!-- /navigation-footer -->
