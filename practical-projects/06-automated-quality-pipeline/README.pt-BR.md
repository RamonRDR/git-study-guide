# Pipeline automatizado de qualidade

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../05-open-source-contribution/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../07-release-management/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 60 min

**Pré-requisitos:** [ci-cd/10-integrated-quality-pipeline-lab](../../ci-cd/10-integrated-quality-pipeline-lab/README.pt-BR.md) · Git 2.40+ · Bash/Git Bash · cmp

**Objetivo:** Registre base com falha, mostre que correção não preparada não passa gate de estado registrado, registre correção em feature, confira patch e integre só após revisão exata passar. Teste recusa de snapshots vazios e com linhas extras.

## Cenário

Catálogo fictício deve conter exatamente uma linha, status: ready. Pequeno controle de qualidade local determinístico verifica snapshot registrado, não arquivo de trabalho sujo. É modelo de gate CI, não serviço CI implantado.

## Preparação descartável

Use apenas a seção Preparação descartável de [Meu primeiro repositório](../01-my-first-repository/README.pt-BR.md). Abra shell Bash/Git Bash dedicado novo; confira raiz impressa, identidades fictícias e ausência de remotos antes de prosseguir. Não execute desafio 01. Git 2.40+. Execute um comando por vez, pare em falha inesperada e nunca execute no guia.

## Desafio

Registre base com falha, mostre que correção não preparada não passa gate de estado registrado, registre correção em feature, confira patch e integre só após revisão exata passar. Teste recusa de snapshots vazios e com linhas extras. Tente antes de ler a solução.

## Dicas progressivas

Use git show REV:catalog.txt e compare bytes com cmp; substituição de comando shell isolada remove quebras finais. git diff --check detecta problemas de formatação introduzidos, mas não é teste completo.

## Solução de referência

Prepare base e gate local. Gate relata falha se arquivo registrado não puder ser lido ou diferir byte a byte da linha esperada. Dois arquivos de comparação ficam fora do checkout.

```bash
printf '%s\n' 'status: ready' > "$sandbox/expected.txt"
check_revision() {
  git show "$1:catalog.txt" > "$sandbox/actual.txt" &&
    cmp -s "$sandbox/expected.txt" "$sandbox/actual.txt"
}
printf '%s\n' 'status: draft' > catalog.txt
git add catalog.txt
git commit -m 'docs: initialize catalog'
git switch -c feat/ready-catalog
if check_revision HEAD; then echo 'UNEXPECTED PASS'; else echo 'RED'; fi
printf '%s\n' 'status: ready' > catalog.txt
if check_revision HEAD; then echo 'UNEXPECTED PASS'; else echo 'RED: unstaged fix'; fi
git add catalog.txt
git diff --cached --check
git commit -m 'feat: mark catalog ready'
check_revision HEAD
echo 'GREEN: committed snapshot'
```

Só continue se ambos casos red falharam e green passou. Use branch descartável de teste negativo para confirmar recusa de estados registrados vazio e com linha extra. Volte à main e revise branch boa conhecida; não integre branch negativa.

```bash
git switch -c test/invalid-catalog
: > catalog.txt
git add catalog.txt
git commit -m 'test: empty catalog'
if check_revision HEAD; then echo 'UNEXPECTED PASS'; else echo 'EMPTY REJECTED'; fi
printf '%s\n' 'status: ready' 'extra: invalid' > catalog.txt
git add catalog.txt
git commit -m 'test: extra catalog line'
if check_revision HEAD; then echo 'UNEXPECTED PASS'; else echo 'EXTRA REJECTED'; fi
git switch main
git diff --check main...feat/ready-catalog
git diff main...feat/ready-catalog
check_revision feat/ready-catalog
git merge --ff-only feat/ready-catalog
check_revision HEAD
git status --porcelain
```

## Critérios de sucesso

Draft, correção só suja, revisões registradas vazia e com linha extra falham; revisão registrada só ready passa. Main aponta para revisão feature testada, não branch negativa. Status limpo. Pare em qualquer UNEXPECTED PASS. Opcional: relacione gate local à aula GitHub Actions ou GitLab CI anterior, sem execução hospedada obrigatória.

Teste fixo de manutenção (não código de aluno): `tests/test_git_practical_projects.py::test_quality_pipeline`.

## Recuperação e limpeza

Inspecione commit exato e saída do gate; não enfraqueça condição para obter verde. Mantenha candidatos falhos separados. Nunca habilite deploy ou execução privilegiada neste exercício. Feche o shell dedicado e remova só o sandbox impresso verificado pelo gerenciador de arquivos. Preserve trabalho desejado antes.

## Fontes oficiais

- <https://git-scm.com/docs/git-diff>
- <https://git-scm.com/docs/git-show>
- <https://git-scm.com/docs/git-commit>

---

<!-- navigation-footer -->
[Anterior](../05-open-source-contribution/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../07-release-management/README.pt-BR.md)
<!-- /navigation-footer -->
