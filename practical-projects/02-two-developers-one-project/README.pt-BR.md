# Dois desenvolvedores, um projeto

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../01-my-first-repository/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../03-merge-conflict-laboratory/README.pt-BR.md)
<!-- /navigation -->

**Nível:** iniciante · **Tempo estimado:** 60 min

**Pré-requisitos:** [remote-repositories/02-fetch-and-tracking](../../remote-repositories/02-fetch-and-tracking/README.pt-BR.md) · Git 2.40+ · Bash/Git Bash

**Objetivo:** Crie base compartilhada, clone como Alice e Bob, publique mudança de Alice, faça fetch em Bob sem alterar seu checkout, depois integre e publique arquivo separado de Bob. Confira convergência.

## Cenário

Alice e Bob mantêm notas fictícias por meio de origin bare local. Alice publica mudança enquanto Bob trabalha independentemente.

## Preparação descartável

Use apenas a seção Preparação descartável de [Meu primeiro repositório](../01-my-first-repository/README.pt-BR.md). Abra shell Bash/Git Bash dedicado novo; confira raiz impressa, identidades fictícias e ausência de remotos antes de prosseguir. Não execute desafio 01. Git 2.40+. Execute um comando por vez, pare em falha inesperada e nunca execute no guia.

## Desafio

Crie base compartilhada, clone como Alice e Bob, publique mudança de Alice, faça fetch em Bob sem alterar seu checkout, depois integre e publique arquivo separado de Bob. Confira convergência. Tente antes de ler a solução.

## Dicas progressivas

Use repositório bare como origin. Fetch atualiza referências de rastreamento, não branch selecionada. Integre na main limpa antes de criar commit de Bob.

## Solução de referência

Crie revisão inicial e publique localmente. Clone duas vezes; configure cada clone antes de registrar commits.

```bash
printf '%s\n' 'shared: draft' > notes.txt
git add notes.txt
git commit -m 'docs: initialize shared notes'
git init --bare -b main "$sandbox/origin.git"
git remote add origin "$sandbox/origin.git"
git push -u origin main
git clone "$sandbox/origin.git" "$sandbox/alice"
git clone "$sandbox/origin.git" "$sandbox/bob"
for who in alice bob; do
  git -C "$sandbox/$who" config user.name 'Study Guide Example'
  git -C "$sandbox/$who" config user.email learner@example.invalid
  git -C "$sandbox/$who" config commit.gpgsign false
  git -C "$sandbox/$who" config core.autocrlf false
  git -C "$sandbox/$who" config core.hooksPath "$sandbox/no-hooks"
done
```

Publique atualização de Alice; Bob registra HEAD antigo e faz fetch. Inspecione referências distintas antes de integrar.

```bash
printf '%s\n' 'shared: ready' > "$sandbox/alice/notes.txt"
git -C "$sandbox/alice" add notes.txt
git -C "$sandbox/alice" commit -m 'docs: prepare shared notes'
git -C "$sandbox/alice" push origin main
cd "$sandbox/bob"
before=$(git rev-parse HEAD)
git fetch origin
test "$(git rev-parse HEAD)" = "$before"
test "$(git rev-parse origin/main)" != "$before"
git merge --ff-only origin/main
printf '%s\n' 'review: done' > review.txt
git add review.txt
git commit -m 'docs: record review'
git push origin main
git -C "$sandbox/alice" pull --ff-only origin main
test "$(git -C "$sandbox/alice" rev-parse HEAD)" = "$(git rev-parse HEAD)"
git status --porcelain
```

## Critérios de sucesso

HEAD de Bob fica inalterado após fetch; após integração ambos clones e main bare têm mesma ponta, com notas ready e review.txt. Ambos clones limpos. Explique fetch versus pull.

Teste fixo de manutenção (não código de aluno): `tests/test_git_practical_projects.py::test_two_developers_sync`.

## Recuperação e limpeza

Em recusa, inspecione referências buscadas e divergência. Nunca force push para contornar. Confira três repositórios locais antes de excluir sandbox. Feche o shell dedicado e remova só o sandbox impresso verificado pelo gerenciador de arquivos. Preserve trabalho desejado antes.

## Fontes oficiais

- <https://git-scm.com/docs/git-clone>
- <https://git-scm.com/docs/git-fetch>
- <https://git-scm.com/docs/git-push>
- <https://git-scm.com/docs/git-merge>

---

<!-- navigation-footer -->
[Anterior](../01-my-first-repository/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../03-merge-conflict-laboratory/README.pt-BR.md)
<!-- /navigation-footer -->
