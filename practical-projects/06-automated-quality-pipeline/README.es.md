# Pipeline automatizado de calidad

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../05-open-source-contribution/README.es.md) · [Índice](../README.es.md) · [Siguiente](../07-release-management/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 60 min

**Prerrequisitos:** [ci-cd/10-integrated-quality-pipeline-lab](../../ci-cd/10-integrated-quality-pipeline-lab/README.es.md) · Git 2.40+ · Bash/Git Bash · cmp

**Objetivo:** Confirma base fallida, muestra que corrección sin preparar no pasa gate de estado confirmado, confirma corrección en feature, comprueba parche e integra solo tras aprobar revisión exacta. Prueba rechazo de instantáneas vacías y con líneas extra.

## Escenario

Catálogo ficticio debe contener exactamente una línea, status: ready. Pequeño control local determinista verifica instantánea confirmada, no archivo de trabajo sucio. Es modelo de gate CI, no servicio CI desplegado.

## Preparación desechable

Usa solo la sección Preparación desechable de [Mi primer repositorio](../01-my-first-repository/README.es.md). Abre shell Bash/Git Bash dedicada nueva; comprueba raíz impresa, identidades ficticias y ausencia de remotos antes de seguir. No ejecutes desafío 01. Git 2.40+. Ejecuta un comando a la vez, detente ante fallo inesperado y nunca ejecutes en el guía.

## Desafío

Confirma base fallida, muestra que corrección sin preparar no pasa gate de estado confirmado, confirma corrección en feature, comprueba parche e integra solo tras aprobar revisión exacta. Prueba rechazo de instantáneas vacías y con líneas extra. Intenta antes de leer la solución.

## Pistas progresivas

Usa git show REV:catalog.txt y compara bytes con cmp; sustitución de comando shell sola elimina saltos finales. git diff --check detecta problemas de formato introducidos, pero no es prueba completa.

## Solución de referencia

Prepara base y gate local. Gate informa fallo si archivo confirmado no puede leerse o difiere byte por byte de línea esperada. Dos archivos de comparación quedan fuera del checkout.

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

Continúa solo si ambos casos red fallaron y green aprobó. Usa rama desechable de prueba negativa para comprobar rechazo de estados confirmados vacío y con línea extra. Vuelve a main y revisa rama buena conocida; no integres rama negativa.

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

## Criterios de éxito

Draft, corrección solo sucia, revisiones confirmadas vacía y con línea extra fallan; revisión confirmada solo ready aprueba. Main apunta a revisión feature probada, no rama negativa. Estado limpio. Detente ante cualquier UNEXPECTED PASS. Opcional: relaciona gate local con lección GitHub Actions o GitLab CI anterior, sin ejecución alojada obligatoria.

Prueba fija de mantenimiento (no código de estudiante): `tests/test_git_practical_projects.py::test_quality_pipeline`.

## Recuperación y limpieza

Inspecciona commit exacto y salida del gate; no debilites condición para obtener verde. Mantén candidatos fallidos separados. Nunca habilites despliegue o ejecución privilegiada en ejercicio. Cierra la shell dedicada y elimina solo el sandbox impreso verificado mediante gestor de archivos. Conserva antes trabajo deseado.

## Fuentes oficiales

- <https://git-scm.com/docs/git-diff>
- <https://git-scm.com/docs/git-show>
- <https://git-scm.com/docs/git-commit>

---

<!-- navigation-footer -->
[Anterior](../05-open-source-contribution/README.es.md) · [Índice](../README.es.md) · [Siguiente](../07-release-management/README.es.md)
<!-- /navigation-footer -->
