# Cherry-pick de commits seleccionados

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../06-stash/README.es.md) · [Índice](../README.es.md) · [Siguiente](../08-amend/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 40 min

**Requisitos previos:** [Laboratorio aislado](../../getting-started/03-first-repository/README.es.md) · [Primer commit](../../getting-started/05-first-commit/README.es.md) · [Merge y conflictos](../../merge-and-conflicts/README.es.md) · [Remotos](../../remote-repositories/README.es.md) · [Stash: trabajo temporal](../06-stash/README.es.md)

**Objetivo:** Transferir commit seleccionado entre ramas divergentes sin fusionar todo historial.

## Qué y por qué

Cherry-pick aplica cambio introducido por commit a rama actual y normalmente crea nuevo commit con padre/ID diferente. No integra toda rama fuente. Úsalo para corrección independiente/backport tras comprobar dependencias; evita sustituir integración normal. `-x` registra ID fuente en mensaje cuando aplica, útil para backports públicos; `--no-commit` aplica sin crear commit aún. Commit de merge exige elección mainline; no practicado. Diagrama: C1 -> F2 en fix; C1 -> M2 en main; tras pick main M2 -> P3, fix permanece F2.

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

```text
git switch -c fix/note
```

Edita note.txt en editor de texto plano a exactamente una línea `fixed` con salto final. Guarda y vuelve a la sesión dedicada.

```text
git add -- note.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Solo si el diff staged y ambas identidades son correctos, continúa:

```text
git commit -m "docs: fix note"
git switch main
```

Crea overview.txt con línea `overview` y salto final en main. Inspecciona raíz, rama, estado e identidades.

```text
git add -- overview.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Solo si el diff staged y ambas identidades son correctos, continúa:

```text
git commit -m "docs: add overview"
git log --all --oneline --graph
git show fix/note
git status --short
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Confirma main limpia, corrección independiente e identidades ficticias. Punta fuente es único commit de corrección. Ejecuta:

```text
git cherry-pick -x fix/note
git log --all --oneline --graph
git rev-parse HEAD fix/note
git show HEAD:note.txt
git show HEAD:overview.txt
git status --short
```

Esperado IDs diferentes, fixed y overview conservados, estado limpio. Commit fuente permanece en fix/note; main tiene nuevo commit con padre M2. En backports reales inspecciona requisitos y prueba antes de publicar.

Tras el ejercicio, cierra editores y sesión dedicada. Elimina solo el padre temporal exacto registrado mediante gestor de archivos si ya no lo necesitas; nunca guía, home o repo de trabajo.

## Errores comunes y seguridad

Ediciones solapadas pueden generar conflicto. Inspecciona estado y marcadores, añade rutas resueltas y usa cherry-pick --continue, o cherry-pick --abort para intentar restaurar estado previo a secuencia. No apliques dos veces a ciegas; parche puede ya existir. No reescribas historial compartido para quitar duplicados.

## Ejercicio y autoevaluación

¿Commit fuente es ancestro de nueva punta main solo porque se seleccionó cambio? Respuesta: no necesariamente; lab tiene ascendencia distinta. Aprueba si ambos archivos sobreviven, IDs difieren y ref fuente no cambia.

## Referencia rápida

- `git cherry-pick COMMIT`
- `git cherry-pick -x COMMIT`
- `git cherry-pick --continue`
- `git cherry-pick --abort`

## Fuentes oficiales

- [Git: git-cherry-pick](https://git-scm.com/docs/git-cherry-pick)
- [Git: git-merge-base](https://git-scm.com/docs/git-merge-base)
