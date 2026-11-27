# Flujo de ingeniería profesional

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../07-release-management/README.es.md) · [Índice](../README.es.md) · [Siguiente módulo](../../exercises/README.es.md)
<!-- /navigation -->

**Nivel:** avanzado · **Tiempo estimado:** 90 min

**Prerrequisitos:** [professional-workflows/13-integrated-professional-workflow-lab](../../professional-workflows/13-integrated-professional-workflow-lab/README.es.md) · Git 2.40+ · Bash/Git Bash · cmp

**Objetivo:** Escribe spec y plan cortos fuera del checkout. Haz dos commits privados feature, falla prueba de base, aprueba prueba feature, registra SHA exacto revisado y revisa diff. Simula autorización del mantenedor y crea commit squash de padre único en main, comprueba igualdad de tree y etiqueta resultado probado.

## Escenario

Servicio ficticio de notas tiene requisito R1: cambiar estado de draft a ready, y AC1: archivo confirmado es exactamente status: ready. Draft existente es base, no contrato público de versión. Simula SDD, prueba red/green, revisión, squash local autorizado y evidencia de lanzamiento.

## Preparación desechable

Usa solo la sección Preparación desechable de [Mi primer repositorio](../01-my-first-repository/README.es.md). Abre shell Bash/Git Bash dedicada nueva; comprueba raíz impresa, identidades ficticias y ausencia de remotos antes de seguir. No ejecutes desafío 01. Git 2.40+. Ejecuta un comando a la vez, detente ante fallo inesperado y nunca ejecutes en el guía.

## Desafío

Escribe spec y plan cortos fuera del checkout. Haz dos commits privados feature, falla prueba de base, aprueba prueba feature, registra SHA exacto revisado y revisa diff. Simula autorización del mantenedor y crea commit squash de padre único en main, comprueba igualdad de tree y etiqueta resultado probado. Intenta antes de leer la solución.

## Pistas progresivas

Mantén main intacta hasta revisión; prueba contenido confirmado, no archivo mutable. Squash prepara cambios sin crear MERGE_HEAD ni mover HEAD. Comprueba padre único y tree igual antes de etiqueta. Simulación no es aprobación independiente real.

## Solución de referencia

Escribe R1, AC1, alcance, checks esperados y política de rollback en cuaderno o archivo fuera del checkout. Establece base y prueba red/green, luego termina dos commits acotados. Continúa solo si red y green se comportan como esperado.

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

Registra evidencia de revisión y límites fuera del checkout. Simula autorización explícita solo tras comprobar SHA exacto revisado y pruebas. Cambia a main, comprueba que no se movió y feature coincide con ID revisado. Realiza squash local solo en laboratorio desechable. Detente ante prueba fallida.

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

## Criterios de éxito

Revisa punta exacta de feature, dos commits acotados de feature, base intacta hasta squash, main tiene dos commits incluida base original, tree final de padre único igual a feature revisada, AC1 aprueba, etiqueta resuelve a commit final, sin remoto y estado limpio. Registra evidencia como PR simulado. No es CI alojado, revisión real ni despliegue.

Prueba fija de mantenimiento (no código de estudiante): `tests/test_git_practical_projects.py::test_professional_workflow`.

## Recuperación y limpieza

Si squash causa conflicto, detente e inspecciona: no se crea MERGE_HEAD ordinario, no supongas que merge --abort funciona. Conserva ediciones deseadas antes de elegir limpieza segura o recrear sandbox. Tras commit compartido incorrecto, prefiere commit correctivo/revert revisado en vez de reescribir historial. Nunca ejecutes contra el guía. Cierra la shell dedicada y elimina solo el sandbox impreso verificado mediante gestor de archivos. Conserva antes trabajo deseado.

## Fuentes oficiales

- <https://git-scm.com/docs/git-branch>
- <https://git-scm.com/docs/git-diff>
- <https://git-scm.com/docs/git-merge>
- <https://git-scm.com/docs/git-tag>
- <https://git-scm.com/docs/git-revert>

---

<!-- navigation-footer -->
[Anterior](../07-release-management/README.es.md) · [Índice](../README.es.md) · [Siguiente módulo](../../exercises/README.es.md)
<!-- /navigation-footer -->
