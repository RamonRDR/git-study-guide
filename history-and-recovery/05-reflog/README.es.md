# Reflog y recuperación de commits perdidos

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../04-revert/README.es.md) · [Índice](../README.es.md) · [Siguiente](../06-stash/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 30 min

**Requisitos previos:** [Laboratorio aislado](../../getting-started/03-first-repository/README.es.md) · [Primer commit](../../getting-started/05-first-commit/README.es.md) · [Merge y conflictos](../../merge-and-conflicts/README.es.md) · [Remotos](../../remote-repositories/README.es.md) · [Revert sin reescribir historial](../04-revert/README.es.md)

**Objetivo:** Encontrar commit desplazado en reflog local y recuperarlo con nueva rama.

## Qué y por qué

Reflog registra actualizaciones de refs locales, incluidos movimientos HEAD. A diferencia de git log, que recorre ascendencia, reflog puede mostrar puntas ya no alcanzables desde rama actual. `HEAD@{1}` refiere a valor anterior de HEAD, no necesariamente padre; usa comillas en shell. Entradas locales pueden caducar y objetos inalcanzables pueden recolectarse después. Diagrama: main C1; antes main C2 -> C1; reflog registra C2 aunque main ya no apunta. Crear rama de rescate en commit verificado lo hace alcanzable de nuevo.

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

Edita note.txt en editor de texto plano a exactamente una línea `rescue me` con salto final. Guarda y vuelve a la sesión dedicada.

```text
git add -- note.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Solo si el diff staged y ambas identidades son correctos, continúa:

```text
git commit -m "docs: add rescue note"
git rev-parse HEAD HEAD^
git status --short
git reflog -n 3
```

Registra C2 en privado. Confirma raíz, main limpia, sin remoto, exactamente dos commits y datos desechables. El siguiente comando mueve main de C2 intencionalmente y restablece index/archivos; no uses en trabajo real.

```text
git reset --hard HEAD^
git log --oneline
git reflog -n 4
git show 'HEAD@{1}':note.txt
git rev-parse 'HEAD@{1}'
```

Esperado log solo C1, reflog incluye C2, show devuelve rescue me. Selector solo vale si aún resuelve a C2 registrado; si no, inspecciona reflog y elige ID completo correcto sin adivinar. Tras verificar crea rama de rescate:

```text
git branch rescue/note 'HEAD@{1}'
git show rescue/note:note.txt
git log --all --oneline --graph
git merge --ff-only rescue/note
git rev-parse HEAD rescue/note
git status --short
```

Esperado ambas refs en C2, ID original recuperado, estado limpio. Uso profesional: conserva ref candidata antes de nuevos cambios; inspecciona contenido e integra solo tras revisión.

Tras el ejercicio, cierra editores y sesión dedicada. Elimina solo el padre temporal exacto registrado mediante gestor de archivos si ya no lo necesitas; nunca guía, home o repo de trabajo.

## Errores comunes y seguridad

Reflog no es respaldo remoto ni garantiza recuperación. No ejecutes reflog expire, gc o limpieza destructiva en incidente; conserva copias independientes. Contenido nunca confirmado/registrado puede no estar disponible.

## Ejercicio y autoevaluación

¿Por qué log no ve C2 tras reset pero reflog puede encontrarlo? Respuesta: ascendencia frente a movimiento de ref. Aprueba si ID rescatado igual a C2 original, no solo contenido.

## Referencia rápida

- `git reflog`
- `git show COMMIT`
- `git branch rescue/note COMMIT`

## Fuentes oficiales

- [Git: git-reflog](https://git-scm.com/docs/git-reflog)
- [Git: git-reset](https://git-scm.com/docs/git-reset)
- [Git: git-branch](https://git-scm.com/docs/git-branch)
- [Git: git-gc](https://git-scm.com/docs/git-gc)
