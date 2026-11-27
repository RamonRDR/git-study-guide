# Laboratorio de conflictos de merge

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../02-two-developers-one-project/README.es.md) · [Índice](../README.es.md) · [Siguiente](../04-the-lost-commit/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 45 min

**Prerrequisitos:** [merge-and-conflicts/04-conflict-resolution](../../merge-and-conflicts/04-conflict-resolution/README.es.md) · Git 2.40+ · Bash/Git Bash

**Objetivo:** Crea ramas divergentes, reproduce conflicto, inspecciona etapas no fusionadas, resuelve a status: reviewed y termina commit de merge con dos padres.

## Escenario

Dos ramas revisan la misma línea ficticia de estado de formas distintas. Integración debe conservar resolución combinada intencional.

## Preparación desechable

Usa solo la sección Preparación desechable de [Mi primer repositorio](../01-my-first-repository/README.es.md). Abre shell Bash/Git Bash dedicada nueva; comprueba raíz impresa, identidades ficticias y ausencia de remotos antes de seguir. No ejecutes desafío 01. Git 2.40+. Ejecuta un comando a la vez, detente ante fallo inesperado y nunca ejecutes en el guía.

## Desafío

Crea ramas divergentes, reproduce conflicto, inspecciona etapas no fusionadas, resuelve a status: reviewed y termina commit de merge con dos padres. Intenta antes de leer la solución.

## Pistas progresivas

Ambos lados deben editar misma línea original. Resultado no cero esperado de merge no es integración exitosa. Prepara resolución elegida antes de confirmar.

## Solución de referencia

Crea base común y puntas divergentes.

```bash
printf '%s\n' 'status: draft' > notes.txt
git add notes.txt
git commit -m 'docs: initialize notes'
git switch -c feat/review
printf '%s\n' 'status: ready' > notes.txt
git add notes.txt
git commit -m 'docs: propose ready'
git switch main
printf '%s\n' 'status: checked' > notes.txt
git add notes.txt
git commit -m 'docs: record check'
before=$(git rev-parse HEAD)
feature=$(git rev-parse feat/review)
git merge feat/review
```

El último comando debe fallar con conflicto. Continúa solo si MERGE_HEAD existe y notes.txt tiene etapas no fusionadas. Inspecciona, luego reemplaza archivo ficticio entero y confirma.

```bash
git rev-parse --verify MERGE_HEAD
git status --short
git ls-files -u -- notes.txt
git show :1:notes.txt
git show :2:notes.txt
git show :3:notes.txt
printf '%s\n' 'status: reviewed' > notes.txt
git add notes.txt
git diff --cached --check
git commit -m 'merge: reconcile review status'
test "$(git rev-parse HEAD^1)" = "$before"
test "$(git rev-parse HEAD^2)" = "$feature"
git status --porcelain
git show HEAD:notes.txt
```

## Criterios de éxito

Etapas 1/2/3 existían antes de resolver; merge final tiene dos padres esperados en orden, contenido reviewed e index y tree limpios. Marcador de conflicto solo no es resultado correcto.

Prueba fija de mantenimiento (no código de estudiante): `tests/test_git_practical_projects.py::test_conflict_resolution`.

## Recuperación y limpieza

Durante merge ordinario activo, conserva ediciones deseadas antes de git merge --abort. Tras finalizar inspecciona padres; no restablezcas historial compartido. Recrea laboratorio desechable si hace falta. Cierra la shell dedicada y elimina solo el sandbox impreso verificado mediante gestor de archivos. Conserva antes trabajo deseado.

## Fuentes oficiales

- <https://git-scm.com/docs/git-merge>
- <https://git-scm.com/docs/git-status>
- <https://git-scm.com/docs/git-ls-files>

---

<!-- navigation-footer -->
[Anterior](../02-two-developers-one-project/README.es.md) · [Índice](../README.es.md) · [Siguiente](../04-the-lost-commit/README.es.md)
<!-- /navigation-footer -->
