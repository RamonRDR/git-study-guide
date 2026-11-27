# Contribuição open source

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../04-the-lost-commit/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../06-automated-quality-pipeline/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 60 min

**Pré-requisitos:** [github/05-forks-and-open-source](../../github/05-forks-and-open-source/README.pt-BR.md) · Git 2.40+ · Bash/Git Bash

**Objetivo:** Prepare fork independente, faça mudança pontual de documentação em branch de feature, revise diff de upstream/main, publique só no fork e depois simule mantenedor que busca e integra branch revisada no upstream.

## Cenário

Um projeto open source fictício tem upstream e fork de contribuinte. Repositórios bare locais simulam a relação de hospedagem sem contas.

## Preparação descartável

Use apenas a seção Preparação descartável de [Meu primeiro repositório](../01-my-first-repository/README.pt-BR.md). Abra shell Bash/Git Bash dedicado novo; confira raiz impressa, identidades fictícias e ausência de remotos antes de prosseguir. Não execute desafio 01. Git 2.40+. Execute um comando por vez, pare em falha inesperada e nunca execute no guia.

## Desafio

Prepare fork independente, faça mudança pontual de documentação em branch de feature, revise diff de upstream/main, publique só no fork e depois simule mantenedor que busca e integra branch revisada no upstream. Tente antes de ler a solução.

## Dicas progressivas

Clone origin bare para outro repositório bare, depois clone fork normalmente. Use nomes distintos origin e upstream. Fetch e merge locais não são PR real nem aprovação humana independente.

## Solução de referência

Crie base upstream e fork local. No clone contribuinte, confira remotos e configure identidade fictícia.

```bash
printf '%s\n' 'status: draft' > notes.txt
git add notes.txt
git commit -m 'docs: initialize notes'
git init --bare -b main "$sandbox/upstream.git"
git remote add origin "$sandbox/upstream.git"
git push -u origin main
git clone --bare "$sandbox/upstream.git" "$sandbox/fork.git"
git clone "$sandbox/fork.git" "$sandbox/contributor"
cd "$sandbox/contributor"
git config user.name 'Study Guide Example'
git config user.email learner@example.invalid
git config commit.gpgsign false
git config core.autocrlf false
git config core.hooksPath "$sandbox/no-hooks"
git remote add upstream "$sandbox/upstream.git"
git remote -v
git fetch upstream
git switch -c feat/clarify-notes
printf '%s\n' 'status: ready' > notes.txt
git add notes.txt
git commit -m 'docs: clarify notes'
git diff --check upstream/main...HEAD
git diff upstream/main...HEAD
git push -u origin feat/clarify-notes
```

Escreva revisão simulada descrevendo mudança, evidência e limites. Alterne papéis para clone original; confira upstream inalterado e inspecione contribuição. Neste exercício offline, escolha fast-forward explicitamente após revisão; não confunda com merge de PR hospedado.

```bash
cd "$sandbox/repo"
git fetch origin
test "$(git rev-parse HEAD)" = "$(git rev-parse origin/main)"
git remote add contribution "$sandbox/fork.git"
git fetch contribution
git diff --check main...contribution/feat/clarify-notes
git diff main...contribution/feat/clarify-notes
git merge --ff-only contribution/feat/clarify-notes
git push origin main
git show HEAD:notes.txt
git status --porcelain
```

## Critérios de sucesso

Branch feature do fork contém ready e main do fork fica na base draft. Main upstream avança só na fase mantenedor e corresponde à contribuição revisada. Opcional: inspecione fluxo GitHub/GitLab nos módulos anteriores; use só projetos próprios autorizados, nunca envie PR indesejado.

Teste fixo de manutenção (não código de aluno): `tests/test_git_practical_projects.py::test_contribution_offline`.

## Recuperação e limpeza

Se destino diferir do caminho local esperado, pare antes do push. Se revisão ou fast-forward falhar, inspecione mudanças sem forçar. Mantenha branch de contribuição até verificar trabalho. Feche o shell dedicado e remova só o sandbox impresso verificado pelo gerenciador de arquivos. Preserve trabalho desejado antes.

## Fontes oficiais

- <https://git-scm.com/docs/git-clone>
- <https://git-scm.com/docs/git-remote>
- <https://git-scm.com/docs/git-fetch>
- <https://git-scm.com/docs/git-diff>
- <https://git-scm.com/docs/git-merge>

---

<!-- navigation-footer -->
[Anterior](../04-the-lost-commit/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../06-automated-quality-pipeline/README.pt-BR.md)
<!-- /navigation-footer -->
