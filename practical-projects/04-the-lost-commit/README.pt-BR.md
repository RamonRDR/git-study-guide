# O commit perdido

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../03-merge-conflict-laboratory/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../05-open-source-contribution/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 45 min

**Pré-requisitos:** [history-and-recovery/05-reflog](../../history-and-recovery/05-reflog/README.pt-BR.md) · Git 2.40+ · Bash/Git Bash

**Objetivo:** Crie dois commits, registre segundo ID fora do repositório, confira checkout limpo, volte um commit neste laboratório descartável, localize commit deslocado com reflog e crie branch de recuperação. Mantenha main no primeiro commit.

## Cenário

Uma branch privada de prática perde sua ponta após reset intencional. Recupere conteúdo registrado sem mover main novamente.

## Preparação descartável

Use apenas a seção Preparação descartável de [Meu primeiro repositório](../01-my-first-repository/README.pt-BR.md). Abra shell Bash/Git Bash dedicado novo; confira raiz impressa, identidades fictícias e ausência de remotos antes de prosseguir. Não execute desafio 01. Git 2.40+. Execute um comando por vez, pare em falha inesperada e nunca execute no guia.

## Desafio

Crie dois commits, registre segundo ID fora do repositório, confira checkout limpo, volte um commit neste laboratório descartável, localize commit deslocado com reflog e crie branch de recuperação. Mantenha main no primeiro commit. Tente antes de ler a solução.

## Dicas progressivas

Reflog é local e expira. Compare candidato ao ID salvo e inspecione conteúdo antes de nomeá-lo. Referência de branch protege histórico alcançável melhor que posição lembrada de reflog.

## Solução de referência

Prepare commits fictícios e confirme estado limpo antes da demonstração destrutiva. Se teste de status falhar, pare.

```bash
printf '%s\n' 'status: draft' > notes.txt
git add notes.txt
git commit -m 'docs: initialize notes'
base=$(git rev-parse HEAD)
printf '%s\n' 'status: recovered' > notes.txt
git add notes.txt
git commit -m 'docs: preserve recovery example'
git rev-parse HEAD > "$sandbox/saved-tip.txt"
test -z "$(git status --porcelain)"
git reset --hard "$base"
git reflog show HEAD
```

Identifique ponta anterior no reflog exibido. Imediatamente após estes passos exatos, HEAD@{1} é revisão deslocada; confira com ID salvo em vez de presumir posição válida em geral.

```bash
candidate=$(git rev-parse 'HEAD@{1}')
test "$candidate" = "$(cat "$sandbox/saved-tip.txt")"
git show "$candidate":notes.txt
git branch recovery/notes "$candidate"
test "$(git rev-parse main)" = "$base"
git show recovery/notes:notes.txt
git status --porcelain
```

## Critérios de sucesso

Main fica na base e recovery/notes nomeia ponta salva exata com conteúdo recovered; working tree limpa. Explique por que edições não registradas não teriam recuperação garantida.

Teste fixo de manutenção (não código de aluno): `tests/test_git_practical_projects.py::test_lost_commit_recovery`.

## Recuperação e limpeza

Não execute reset --hard fora deste laboratório novo. Se candidato divergir, pare e inspecione reflog e ID salvo; evite coleta de lixo durante recuperação. Recuperação não é garantida se objetos desaparecerem. Feche o shell dedicado e remova só o sandbox impresso verificado pelo gerenciador de arquivos. Preserve trabalho desejado antes.

## Fontes oficiais

- <https://git-scm.com/docs/git-reset>
- <https://git-scm.com/docs/git-reflog>
- <https://git-scm.com/docs/git-branch>
- <https://git-scm.com/docs/git-show>

---

<!-- navigation-footer -->
[Anterior](../03-merge-conflict-laboratory/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../05-open-source-contribution/README.pt-BR.md)
<!-- /navigation-footer -->
