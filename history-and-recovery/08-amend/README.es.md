# Amend de un commit no publicado

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../07-cherry-pick/README.es.md) · [Índice](../README.es.md) · [Siguiente módulo](../../github/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 25 min

**Requisitos previos:** [Laboratorio aislado](../../getting-started/03-first-repository/README.es.md) · [Primer commit](../../getting-started/05-first-commit/README.es.md) · [Merge y conflictos](../../merge-and-conflicts/README.es.md) · [Remotos](../../remote-repositories/README.es.md) · [Cherry-pick de commits seleccionados](../07-cherry-pick/README.es.md)

**Objetivo:** Corregir punta privada manteniendo padre original y ref de recuperación.

## Qué y por qué

`git commit --amend` sustituye punta por commit basado en index y normalmente conserva padres; puede cambiar mensaje y/o contenido. Contenido o mensaje cambiado genera nuevo ID. `--no-edit` conserva mensaje. No edita objeto commit in situ. Usa solo commits no publicados; en ramas compartidas añade commit correctivo o revert. Diagrama: C1 -> C2 (antiguo); main pasa a C2' con mismo padre C1; respaldo queda en C2.

## Práctica

Inicia un NUEVO lab desechable independiente según las lecciones enlazadas de configuración y primer commit. Mantén la sesión Bash o PowerShell dedicada en la carpeta repo registrada, con configuración Git system/global aislada, variables Git heredadas limpiadas y plantillas vacías. Usa Git 2.40 o posterior. Main inicial debe tener exactamente un commit con note.txt = practice, sin remotos y estado limpio. Ejecuta cada comando individualmente. Antes de cada cambio repite la inspección: raíz debe ser el repo desechable registrado, rama la indicada, remotos vacíos, estado exactamente descrito; ambas identidades deben empezar por `Study Guide Example <learner@example.invalid>`. Antes de cada commit inspecciona cambios staged y ambas identidades. Detente ante salida o fallo inesperado. Nunca ejecutes estos labs en la guía o proyecto real.

```text
git rev-parse --show-toplevel
git branch --show-current
git remote -v
git status --short
git diff
git diff --cached
git log --oneline --all --graph --decorate
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Edita note.txt en editor de texto plano a exactamente una línea `draft version` con salto final. Guarda y vuelve a la sesión dedicada.

```text
git add -- note.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Solo si el diff staged y ambas identidades son correctos, continúa:

```text
git commit -m "docs: add draft"
git branch backup/draft
git rev-parse HEAD HEAD^
git status --short
```

Edita note.txt en editor de texto plano a exactamente una línea `final version` con salto final. Guarda y vuelve a la sesión dedicada.

```text
git add -- note.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Solo si el diff staged y ambas identidades son correctos, continúa:

```text
git commit --amend -m "docs: add final version"
git rev-parse HEAD backup/draft
git rev-parse HEAD^ backup/draft^
git show HEAD:note.txt
git show backup/draft:note.txt
git rev-list --count HEAD
git status --short
```

Esperado puntas diferentes, padres iguales, dos commits alcanzables de main, final version en HEAD y draft version en respaldo. Uso profesional: corregir archivo olvidado o error antes de publicar. Para corregir solo mensaje confirma index sin cambios antes de amend.

Tras el ejercicio, cierra editores y sesión dedicada. Elimina solo el padre temporal exacto registrado mediante gestor de archivos si ya no lo necesitas; nunca guía, home o repo de trabajo.

## Errores comunes y seguridad

Amend incluye cambios staged incluso ajenos a corrección. Inspecciona antes. Nunca hagas force push de rama compartida para publicar amend. Si punta privada equivocada fue sustituida, inspecciona respaldo/reflog y conserva rama de rescate antes de nuevos cambios.

## Ejercicio y autoevaluación

¿Por qué dos commits con mismo padre pueden tener IDs diferentes? Respuesta: contenido/mensaje o metadatos difieren. Aprueba si punta original queda en respaldo y punta actual tiene contenido previsto y mismo padre.

## Referencia rápida

- `git commit --amend -m MESSAGE`
- `git commit --amend --no-edit`
- `git branch backup/draft`

## Fuentes oficiales

- [Git: git-commit](https://git-scm.com/docs/git-commit)
- [Git: git-reflog](https://git-scm.com/docs/git-reflog)
- [Git: git-revert](https://git-scm.com/docs/git-revert)

---

<!-- navigation-footer -->
[Anterior](../07-cherry-pick/README.es.md) · [Índice](../README.es.md) · [Siguiente módulo](../../github/README.es.md)
<!-- /navigation-footer -->
