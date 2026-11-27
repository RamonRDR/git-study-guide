# Fluxo de engenharia profissional

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../07-release-management/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo módulo](../../exercises/README.pt-BR.md)
<!-- /navigation -->

**Nível:** avançado · **Tempo estimado:** 90 min

**Pré-requisitos:** [professional-workflows/13-integrated-professional-workflow-lab](../../professional-workflows/13-integrated-professional-workflow-lab/README.pt-BR.md) · Git 2.40+ · Bash/Git Bash · cmp

**Objetivo:** Escreva spec e plano curtos fora do checkout. Faça dois commits privados de feature, falhe teste da base, passe teste da feature, registre SHA exato revisado e revise diff. Simule autorização do mantenedor e crie commit squash de pai único na main, confira igualdade da tree e marque resultado testado.

## Cenário

Serviço fictício de notas tem requisito R1: alterar status de draft para ready, e AC1: arquivo registrado é exatamente status: ready. Draft existente é base, não contrato público de versão. Simule SDD, teste red/green, revisão, squash local autorizado e evidência de release.

## Preparação descartável

Use apenas a seção Preparação descartável de [Meu primeiro repositório](../01-my-first-repository/README.pt-BR.md). Abra shell Bash/Git Bash dedicado novo; confira raiz impressa, identidades fictícias e ausência de remotos antes de prosseguir. Não execute desafio 01. Git 2.40+. Execute um comando por vez, pare em falha inesperada e nunca execute no guia.

## Desafio

Escreva spec e plano curtos fora do checkout. Faça dois commits privados de feature, falhe teste da base, passe teste da feature, registre SHA exato revisado e revise diff. Simule autorização do mantenedor e crie commit squash de pai único na main, confira igualdade da tree e marque resultado testado. Tente antes de ler a solução.

## Dicas progressivas

Mantenha main inalterada até revisão; teste conteúdo registrado, não arquivo mutável. Squash prepara mudanças sem criar MERGE_HEAD nem mover HEAD. Confira pai único e tree igual antes da tag. Simulação não é aprovação independente real.

## Solução de referência

Escreva R1, AC1, escopo, checks esperados e política de rollback em caderno ou arquivo fora do checkout. Estabeleça base e teste red/green, depois conclua dois commits pontuais. Continue só se red e green se comportarem como esperado.

```bash
printf '%s\n' 'status: draft' > notes.txt
git add notes.txt
git commit -m 'docs: initialize notes'
base=$(git rev-parse HEAD)
printf '%s\n' 'status: ready' > "$sandbox/expected.txt"
check_revision() {
  git show "$1:notes.txt" > "$sandbox/actual.txt" &&
    cmp -s "$sandbox/expected.txt" "$sandbox/actual.txt"
}
git switch -c feat/ready-notes
if check_revision HEAD; then echo 'UNEXPECTED PASS'; else echo 'RED'; fi
printf '%s\n' 'status: ready' > notes.txt
git add notes.txt
git commit -m 'feat: mark notes ready'
printf '%s\n' 'R1: notes are ready' > review.txt
git add review.txt
git commit -m 'docs: record readiness requirement'
check_revision HEAD
git diff --check main...HEAD
git diff main...HEAD
reviewed=$(git rev-parse HEAD)
reviewed_tree=$(git rev-parse 'HEAD^{tree}')
```

Registre evidência de revisão e limites fora do checkout. Simule autorização explícita só após conferir SHA exato revisado e testes. Vá à main, confira que não moveu e feature corresponde ao ID revisado. Faça squash local só neste laboratório descartável. Pare em qualquer teste falho.

```bash
git switch main
test "$(git rev-parse HEAD)" = "$base"
test "$(git rev-parse feat/ready-notes)" = "$reviewed"
test -z "$(git status --porcelain)"
git merge --squash feat/ready-notes
test "$(git rev-parse HEAD)" = "$base"
git diff --cached --check
git diff --cached
git commit -m 'feat: deliver reviewed notes'
test "$(git rev-parse HEAD^1)" = "$base"
test "$(git rev-parse 'HEAD^{tree}')" = "$reviewed_tree"
test "$(git rev-list --count HEAD)" = 2
check_revision HEAD
git tag -a v1.0.0 -m 'First reviewed notes release'
test "$(git rev-parse 'v1.0.0^{commit}')" = "$(git rev-parse HEAD)"
git status --porcelain
git remote
```

## Critérios de sucesso

Revise ponta exata da feature, dois commits pontuais de feature, base inalterada até squash, main tem dois commits incluindo base original, tree final de pai único igual à feature revisada, AC1 passa, tag resolve a commit final, sem remoto e status limpo. Registre evidência como PR simulado. Não é CI hospedado, revisão real ou deploy.

Teste fixo de manutenção (não código de aluno): `tests/test_git_practical_projects.py::test_professional_workflow`.

## Recuperação e limpeza

Se squash conflitar, pare e inspecione: MERGE_HEAD comum não é criado, portanto não presuma merge --abort funcional. Preserve edições desejadas antes de escolher limpeza segura ou recriar sandbox. Após commit compartilhado ruim, prefira commit corretivo/revert revisado em vez de reescrever histórico. Nunca execute contra o guia. Feche o shell dedicado e remova só o sandbox impresso verificado pelo gerenciador de arquivos. Preserve trabalho desejado antes.

## Fontes oficiais

- <https://git-scm.com/docs/git-branch>
- <https://git-scm.com/docs/git-diff>
- <https://git-scm.com/docs/git-merge>
- <https://git-scm.com/docs/git-tag>
- <https://git-scm.com/docs/git-revert>

---

<!-- navigation-footer -->
[Anterior](../07-release-management/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo módulo](../../exercises/README.pt-BR.md)
<!-- /navigation-footer -->
