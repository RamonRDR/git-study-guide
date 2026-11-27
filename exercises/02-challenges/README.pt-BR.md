# Desafios práticos

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../01-quizzes/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../03-interviews/README.pt-BR.md)
<!-- /navigation -->

Tente primeiro, consulte as soluções públicas depois. Quizzes usam escolhas exatas; entrevistas e simulados exigem autoavaliação honesta. Desafios usam somente repositórios locais descartáveis novos e checks fixos de estado, sem executar automaticamente comandos de alunos. Registros são piloto interno, não contrato final do Learning Hub.

## Primeiro snapshot registrado

ID: challenge-first-commit

**Dificuldade:** fácil

**Pré-requisitos:** [practical-projects/01-my-first-repository](../../practical-projects/01-my-first-repository/README.pt-BR.md) · [getting-started/05-first-commit](../../getting-started/05-first-commit/README.pt-BR.md)

Registre notes.txt contendo status: ready; termine limpo na main com um commit.

**Tempo (min):** 10

**Execução:** local_only · Exige Git real em repo descartável novo; sem alegação de runtime navegador.

**Preparação:** Inicie repo local novo usando só Preparação descartável do projeto 01 (pré-requisitos vinculados); confira main, identidade fictícia e nenhum remoto. Git 2.40+ e Bash/Git Bash. Execute comandos individualmente, pare em falha inesperada e use finais LF. Use repo novo vazio.

**Dicas:**

- Arquivo precisa entrar no index primeiro.
- Inspecione conteúdo preparado antes do commit.

**Solução:**

- Escreva exatamente status: ready mais LF final em notes.txt.
- git add notes.txt
- git diff --cached
- git commit -m 'docs: add notes'
- Após conferir resultados, feche shell dedicado e remova só diretório temporário verificado pelo gerenciador de arquivos. Nunca use repo do guia.

**Checks de estado:**

- kind=branch, value=main
- kind=commit-count, value=1
- file=notes.txt, kind=head-content, value=status: ready
- file=notes.txt, kind=tracked
- kind=clean

**Explicação:** Status limpo sozinho não basta: conteúdo registrado e contagem devem corresponder.

## Separar staging e trabalho

ID: challenge-staged-snapshot

**Dificuldade:** fácil

**Pré-requisitos:** [practical-projects/01-my-first-repository](../../practical-projects/01-my-first-repository/README.pt-BR.md) · [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.pt-BR.md)

Deixe HEAD em draft, prepare ready, depois altere arquivo para experiment sem preparar novamente.

**Tempo (min):** 10

**Execução:** local_only · Exige Git real em repo descartável novo; sem alegação de runtime navegador.

**Preparação:** Inicie repo local novo usando só Preparação descartável do projeto 01 (pré-requisitos vinculados); confira main, identidade fictícia e nenhum remoto. Git 2.40+ e Bash/Git Bash. Execute comandos individualmente, pare em falha inesperada e use finais LF. Crie notes.txt com exatamente status: draft e LF final; git add notes.txt; git commit -m 'docs: initialize notes'.

**Dicas:**

- Os três locais podem diferir.
- Inspecione HEAD:notes.txt e :notes.txt.

**Solução:**

- Escreva exatamente status: ready mais LF final em notes.txt.
- git add notes.txt
- Escreva exatamente status: experiment mais LF final em notes.txt.
- git show HEAD:notes.txt
- git show :notes.txt
- git status --short
- Após conferir resultados, feche shell dedicado e remova só diretório temporário verificado pelo gerenciador de arquivos. Nunca use repo do guia.

**Checks de estado:**

- kind=branch, value=main
- kind=commit-count, value=1
- file=notes.txt, kind=head-content, value=status: draft
- file=notes.txt, kind=index-content, value=status: ready
- file=notes.txt, kind=work-content, value=status: experiment

**Explicação:** Não faça commit nem restore; tree suja é resultado exigido aqui.

## Preservar edição de trabalho

ID: challenge-unstage

**Dificuldade:** fácil

**Pré-requisitos:** [practical-projects/01-my-first-repository](../../practical-projects/01-my-first-repository/README.pt-BR.md) · [history-and-recovery/02-restore](../../history-and-recovery/02-restore/README.pt-BR.md)

Retire ready do staging sem perdê-lo do arquivo de trabalho; HEAD e index ainda devem conter draft.

**Tempo (min):** 10

**Execução:** local_only · Exige Git real em repo descartável novo; sem alegação de runtime navegador.

**Preparação:** Inicie repo local novo usando só Preparação descartável do projeto 01 (pré-requisitos vinculados); confira main, identidade fictícia e nenhum remoto. Git 2.40+ e Bash/Git Bash. Execute comandos individualmente, pare em falha inesperada e use finais LF. Crie notes.txt com exatamente status: draft e LF final; git add notes.txt; git commit -m 'docs: initialize notes'.

**Dicas:**

- Só index deve mudar.
- Use restore --staged após preparar conteúdo novo.

**Solução:**

- Escreva exatamente status: ready mais LF final em notes.txt.
- git add notes.txt
- git restore --staged -- notes.txt
- git diff
- Após conferir resultados, feche shell dedicado e remova só diretório temporário verificado pelo gerenciador de arquivos. Nunca use repo do guia.

**Checks de estado:**

- kind=branch, value=main
- kind=commit-count, value=1
- file=notes.txt, kind=head-content, value=status: draft
- file=notes.txt, kind=index-content, value=status: draft
- file=notes.txt, kind=work-content, value=status: ready

**Explicação:** Restore --staged não descarta edição de trabalho com HEAD existente.

## Isolar feature

ID: challenge-feature-branch

**Dificuldade:** fácil

**Pré-requisitos:** [practical-projects/01-my-first-repository](../../practical-projects/01-my-first-repository/README.pt-BR.md) · [branches/01-create-and-switch](../../branches/01-create-and-switch/README.pt-BR.md)

Crie feat/notes a partir de draft e registre ready nela, deixando main no primeiro commit.

**Tempo (min):** 15

**Execução:** local_only · Exige Git real em repo descartável novo; sem alegação de runtime navegador.

**Preparação:** Inicie repo local novo usando só Preparação descartável do projeto 01 (pré-requisitos vinculados); confira main, identidade fictícia e nenhum remoto. Git 2.40+ e Bash/Git Bash. Execute comandos individualmente, pare em falha inesperada e use finais LF. Crie notes.txt com exatamente status: draft e LF final; git add notes.txt; git commit -m 'docs: initialize notes'.

**Dicas:**

- Criar e selecionar branch são conceitos separados.
- Use switch -c antes de editar.

**Solução:**

- git switch -c feat/notes
- Escreva exatamente status: ready mais LF final em notes.txt.
- git add notes.txt
- git commit -m 'docs: update notes'
- git log --oneline --all
- Após conferir resultados, feche shell dedicado e remova só diretório temporário verificado pelo gerenciador de arquivos. Nunca use repo do guia.

**Checks de estado:**

- kind=branch, value=feat/notes
- kind=commit-count, value=2
- kind=same-ref, left=main, right=HEAD^1
- file=notes.txt, kind=head-content, value=status: ready
- kind=clean

**Explicação:** Ref main deve permanecer no pai do commit feature.

## Integrar por fast-forward

ID: challenge-fast-forward

**Dificuldade:** médio

**Pré-requisitos:** [practical-projects/01-my-first-repository](../../practical-projects/01-my-first-repository/README.pt-BR.md) · [merge-and-conflicts/02-fast-forward](../../merge-and-conflicts/02-fast-forward/README.pt-BR.md)

Integre feat/notes na main sem commit merge extra; ambas refs devem coincidir.

**Tempo (min):** 15

**Execução:** local_only · Exige Git real em repo descartável novo; sem alegação de runtime navegador.

**Preparação:** Inicie repo local novo usando só Preparação descartável do projeto 01 (pré-requisitos vinculados); confira main, identidade fictícia e nenhum remoto. Git 2.40+ e Bash/Git Bash. Execute comandos individualmente, pare em falha inesperada e use finais LF. Crie notes.txt com exatamente status: draft e LF final; git add notes.txt; git commit -m 'docs: initialize notes'.

**Dicas:**

- Evite divergência da main.
- Confira feature descendente e use --ff-only.

**Solução:**

- git switch -c feat/notes
- Escreva exatamente status: ready mais LF final em notes.txt.
- git add notes.txt
- git commit -m 'docs: update notes'
- git switch main
- git merge --ff-only feat/notes
- Após conferir resultados, feche shell dedicado e remova só diretório temporário verificado pelo gerenciador de arquivos. Nunca use repo do guia.

**Checks de estado:**

- kind=branch, value=main
- kind=commit-count, value=2
- kind=same-ref, left=main, right=feat/notes
- file=notes.txt, kind=head-content, value=status: ready
- kind=clean

**Explicação:** Fast-forward move ref atual em vez de criar merge novo.

## Resolver conflito

ID: challenge-merge-resolution

**Dificuldade:** médio

**Pré-requisitos:** [practical-projects/01-my-first-repository](../../practical-projects/01-my-first-repository/README.pt-BR.md) · [merge-and-conflicts/04-conflict-resolution](../../merge-and-conflicts/04-conflict-resolution/README.pt-BR.md)

Diverja main e feat/notes de draft, resolva conflito da mesma linha para reviewed e mantenha dois pais.

**Tempo (min):** 20

**Execução:** local_only · Exige Git real em repo descartável novo; sem alegação de runtime navegador.

**Preparação:** Inicie repo local novo usando só Preparação descartável do projeto 01 (pré-requisitos vinculados); confira main, identidade fictícia e nenhum remoto. Git 2.40+ e Bash/Git Bash. Execute comandos individualmente, pare em falha inesperada e use finais LF. Crie notes.txt com exatamente status: draft e LF final; git add notes.txt; git commit -m 'docs: initialize notes'.

**Dicas:**

- Faça mudanças diferentes na mesma linha.
- Inspecione git ls-files -u antes de preparar resolução.

**Solução:**

- git switch -c feat/notes
- Escreva exatamente status: ready mais LF final em notes.txt.
- git add notes.txt
- git commit -m 'docs: update notes'
- git switch main
- Escreva exatamente status: experiment mais LF final em notes.txt.
- git add notes.txt
- git commit -m 'docs: update notes'
- Rode git merge feat/notes; espere conflito, confira MERGE\_HEAD e inspecione git ls-files -u. Pare em outra falha.
- Escreva exatamente status: reviewed mais LF final em notes.txt.
- git add notes.txt
- git diff --cached --check
- git commit -m 'merge: resolve notes'
- Após conferir resultados, feche shell dedicado e remova só diretório temporário verificado pelo gerenciador de arquivos. Nunca use repo do guia.

**Checks de estado:**

- kind=branch, value=main
- kind=commit-count, value=4
- kind=parent-count, value=2
- kind=same-ref, left=HEAD^2, right=feat/notes
- file=notes.txt, kind=head-content, value=status: reviewed
- kind=no-unmerged
- kind=clean

**Explicação:** Se abortar merge comum ativo, preserve edições desejadas antes. Merge bem-sucedido tem dois pais e sem entradas não mescladas.

## Desfazer sem reescrever

ID: challenge-revert

**Dificuldade:** médio

**Pré-requisitos:** [practical-projects/01-my-first-repository](../../practical-projects/01-my-first-repository/README.pt-BR.md) · [history-and-recovery/04-revert](../../history-and-recovery/04-revert/README.pt-BR.md)

Registre ready e desfaça conteúdo com novo commit. Preserve dois commits originais.

**Tempo (min):** 15

**Execução:** local_only · Exige Git real em repo descartável novo; sem alegação de runtime navegador.

**Preparação:** Inicie repo local novo usando só Preparação descartável do projeto 01 (pré-requisitos vinculados); confira main, identidade fictícia e nenhum remoto. Git 2.40+ e Bash/Git Bash. Execute comandos individualmente, pare em falha inesperada e use finais LF. Crie notes.txt com exatamente status: draft e LF final; git add notes.txt; git commit -m 'docs: initialize notes'.

**Dicas:**

- Histórico deve crescer, não reduzir.
- Use revert no último commit comum.

**Solução:**

- Escreva exatamente status: ready mais LF final em notes.txt.
- git add notes.txt
- git commit -m 'docs: update notes'
- git revert --no-edit HEAD
- Após conferir resultados, feche shell dedicado e remova só diretório temporário verificado pelo gerenciador de arquivos. Nunca use repo do guia.

**Checks de estado:**

- kind=branch, value=main
- kind=commit-count, value=3
- kind=parent-count, value=1
- file=notes.txt, kind=head-content, value=status: draft
- kind=clean

**Explicação:** Revert cria mudança inversa nova. Não é reset.

## Preservar trabalho incompleto

ID: challenge-stash

**Dificuldade:** médio

**Pré-requisitos:** [practical-projects/01-my-first-repository](../../practical-projects/01-my-first-repository/README.pt-BR.md) · [history-and-recovery/06-stash](../../history-and-recovery/06-stash/README.pt-BR.md)

Guarde edição ready e review.txt não rastreado no stash, confira estado limpo e aplique stash. Deixe ambos restaurados e HEAD draft.

**Tempo (min):** 15

**Execução:** local_only · Exige Git real em repo descartável novo; sem alegação de runtime navegador.

**Preparação:** Inicie repo local novo usando só Preparação descartável do projeto 01 (pré-requisitos vinculados); confira main, identidade fictícia e nenhum remoto. Git 2.40+ e Bash/Git Bash. Execute comandos individualmente, pare em falha inesperada e use finais LF. Crie notes.txt com exatamente status: draft e LF final; git add notes.txt; git commit -m 'docs: initialize notes'.

**Dicas:**

- Inclua não rastreados explicitamente.
- Use apply em vez de pop para manter stash para inspeção.

**Solução:**

- Escreva exatamente status: ready mais LF final em notes.txt.
- Crie review.txt com exatamente review: done mais LF.
- git stash push -u -m 'practice notes'
- git status --porcelain
- git stash apply
- git stash list
- Após conferir resultados, feche shell dedicado e remova só diretório temporário verificado pelo gerenciador de arquivos. Nunca use repo do guia.

**Checks de estado:**

- kind=branch, value=main
- kind=commit-count, value=1
- file=notes.txt, kind=head-content, value=status: draft
- file=notes.txt, kind=index-content, value=status: draft
- file=notes.txt, kind=work-content, value=status: ready
- file=review.txt, kind=work-content, value=review: done
- file=review.txt, kind=untracked

**Explicação:** Check final não prova operação temporária; registre status limpo intermediário e stash list como evidência manual.

## Recuperar ponta deslocada

ID: challenge-recover-tip

**Dificuldade:** difícil

**Pré-requisitos:** [practical-projects/01-my-first-repository](../../practical-projects/01-my-first-repository/README.pt-BR.md) · [history-and-recovery/05-reflog](../../history-and-recovery/05-reflog/README.pt-BR.md)

Simule perda de ponta registrada em repo descartável. Recupere com recovery/notes mantendo main draft.

**Tempo (min):** 20

**Execução:** local_only · Exige Git real em repo descartável novo; sem alegação de runtime navegador.

**Preparação:** Inicie repo local novo usando só Preparação descartável do projeto 01 (pré-requisitos vinculados); confira main, identidade fictícia e nenhum remoto. Git 2.40+ e Bash/Git Bash. Execute comandos individualmente, pare em falha inesperada e use finais LF. Crie notes.txt com exatamente status: draft e LF final; git add notes.txt; git commit -m 'docs: initialize notes'.

**Dicas:**

- Salve ID da ponta antes da demonstração.
- Confira candidato reflog e crie ref nova, não outro reset.

**Solução:**

- Escreva exatamente status: recovered mais LF final em notes.txt.
- git add notes.txt
- git commit -m 'docs: update notes'
- git rev-parse HEAD; anote ID fora do repo.
- Confira git status --porcelain vazio, depois só neste repo descartável rode git reset --hard HEAD\~1.
- git reflog show HEAD
- Inspecione git show HEAD@{1}; confira ID salvo e então git branch recovery/notes 'HEAD@{1}'.
- Após conferir resultados, feche shell dedicado e remova só diretório temporário verificado pelo gerenciador de arquivos. Nunca use repo do guia.

**Checks de estado:**

- kind=branch, value=main
- kind=commit-count, value=1
- file=notes.txt, kind=head-content, value=status: draft
- kind=ancestor, newer=recovery/notes, older=main
- file=notes.txt, kind=ref-content, ref=recovery/notes, value=status: recovered
- kind=different-ref, left=main, right=recovery/notes
- kind=clean

**Explicação:** Nunca presuma posições reflog ou recuperação garantida; confira IDs e evite comandos destrutivos em trabalho valioso.

## Integrar tree revisada

ID: challenge-squash

**Dificuldade:** difícil

**Pré-requisitos:** [practical-projects/01-my-first-repository](../../practical-projects/01-my-first-repository/README.pt-BR.md) · [merge-and-conflicts/05-squash-merge](../../merge-and-conflicts/05-squash-merge/README.pt-BR.md)

Crie dois commits feature e faça squash na main inalterada. Main deve ter exatamente dois commits e mesma tree da ponta feature.

**Tempo (min):** 20

**Execução:** local_only · Exige Git real em repo descartável novo; sem alegação de runtime navegador.

**Preparação:** Inicie repo local novo usando só Preparação descartável do projeto 01 (pré-requisitos vinculados); confira main, identidade fictícia e nenhum remoto. Git 2.40+ e Bash/Git Bash. Execute comandos individualmente, pare em falha inesperada e use finais LF. Crie notes.txt com exatamente status: draft e LF final; git add notes.txt; git commit -m 'docs: initialize notes'.

**Dicas:**

- Commit squash tem um pai.
- Compare IDs de tree, não commits, após integração.

**Solução:**

- git switch -c feat/notes
- Escreva exatamente status: ready mais LF final em notes.txt.
- git add notes.txt
- git commit -m 'docs: update notes'
- Crie review.txt com exatamente review: done mais LF; git add review.txt; git commit -m 'docs: record review'.
- git diff main...HEAD
- git switch main
- git merge --squash feat/notes
- git diff --cached --check
- git commit -m 'feat: deliver reviewed notes'
- Após conferir resultados, feche shell dedicado e remova só diretório temporário verificado pelo gerenciador de arquivos. Nunca use repo do guia.

**Checks de estado:**

- kind=branch, value=main
- kind=commit-count, value=2
- kind=parent-count, value=1
- file=notes.txt, kind=head-content, value=status: ready
- file=review.txt, kind=head-content, value=review: done
- kind=same-tree, left=main, right=feat/notes
- kind=different-ref, left=main, right=feat/notes
- kind=clean

**Explicação:** Não presuma merge --abort para squash com conflito. Pare, preserve edições e inspecione; recrie fixture descartável se preciso.

## Fixar release

ID: challenge-release-tag

**Dificuldade:** difícil

**Pré-requisitos:** [practical-projects/01-my-first-repository](../../practical-projects/01-my-first-repository/README.pt-BR.md) · [professional-workflows/12-release-management](../../professional-workflows/12-release-management/README.pt-BR.md)

Marque revisão ready com v1.0.0 anotada, depois avance main com future.txt. Tag deve resolver ao commit anterior.

**Tempo (min):** 15

**Execução:** local_only · Exige Git real em repo descartável novo; sem alegação de runtime navegador.

**Preparação:** Inicie repo local novo usando só Preparação descartável do projeto 01 (pré-requisitos vinculados); confira main, identidade fictícia e nenhum remoto. Git 2.40+ e Bash/Git Bash. Execute comandos individualmente, pare em falha inesperada e use finais LF. Crie notes.txt com exatamente status: draft e LF final; git add notes.txt; git commit -m 'docs: initialize notes'.

**Dicas:**

- Tag deve identificar revisão exata.
- Use tag -a e resolva a commit.

**Solução:**

- Escreva exatamente status: ready mais LF final em notes.txt.
- git add notes.txt
- git commit -m 'docs: update notes'
- git tag -a v1.0.0 -m 'Ready notes release'
- Crie future.txt com exatamente future work mais LF; git add future.txt; git commit -m 'docs: future work'.
- git rev-parse 'v1.0.0^{commit}'
- Após conferir resultados, feche shell dedicado e remova só diretório temporário verificado pelo gerenciador de arquivos. Nunca use repo do guia.

**Checks de estado:**

- kind=branch, value=main
- kind=commit-count, value=3
- kind=tag-type, tag=v1.0.0, value=tag
- kind=same-ref, left=v1.0.0, right=HEAD^1
- file=notes.txt, kind=ref-content, ref=v1.0.0, value=status: ready
- file=future.txt, kind=head-content, value=future work
- kind=clean

**Explicação:** Tag Git anotada não é release hospedada; não substitua tags publicadas casualmente.

## Transferir uma mudança

ID: challenge-cherry-pick

**Dificuldade:** difícil

**Pré-requisitos:** [practical-projects/01-my-first-repository](../../practical-projects/01-my-first-repository/README.pt-BR.md) · [history-and-recovery/07-cherry-pick](../../history-and-recovery/07-cherry-pick/README.pt-BR.md)

Registre review.txt em feat/notes, avance main independentemente para ready e faça cherry-pick só do commit review na main. Mantenha feature distinta.

**Tempo (min):** 20

**Execução:** local_only · Exige Git real em repo descartável novo; sem alegação de runtime navegador.

**Preparação:** Inicie repo local novo usando só Preparação descartável do projeto 01 (pré-requisitos vinculados); confira main, identidade fictícia e nenhum remoto. Git 2.40+ e Bash/Git Bash. Execute comandos individualmente, pare em falha inesperada e use finais LF. Crie notes.txt com exatamente status: draft e LF final; git add notes.txt; git commit -m 'docs: initialize notes'.

**Dicas:**

- Use arquivo separado para evitar conflito fabricado.
- Confira contagem de pais e conteúdo final; IDs não precisam coincidir.

**Solução:**

- git switch -c feat/notes
- Crie review.txt com exatamente review: done mais LF; git add review.txt; git commit -m 'docs: record review'.
- git switch main
- Escreva exatamente status: ready mais LF final em notes.txt.
- git add notes.txt
- git commit -m 'docs: update notes'
- git cherry-pick feat/notes
- Após conferir resultados, feche shell dedicado e remova só diretório temporário verificado pelo gerenciador de arquivos. Nunca use repo do guia.

**Checks de estado:**

- kind=branch, value=main
- kind=commit-count, value=3
- kind=parent-count, value=1
- file=notes.txt, kind=head-content, value=status: ready
- file=review.txt, kind=head-content, value=review: done
- file=notes.txt, kind=ref-content, ref=feat/notes, value=status: draft
- kind=different-ref, left=main, right=feat/notes
- kind=clean

**Explicação:** Em conflito inesperado cherry-pick, inspecione e preserve trabalho antes de abortar. Conteúdo aplicado não prova histórico idêntico.

---

<!-- navigation-footer -->
[Anterior](../01-quizzes/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../03-interviews/README.pt-BR.md)
<!-- /navigation-footer -->
