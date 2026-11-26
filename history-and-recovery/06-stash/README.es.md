# Stash: trabajo temporal

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../05-reflog/README.es.md) · [Índice](../README.es.md) · [Siguiente](../07-cherry-pick/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 35 min

**Requisitos previos:** [Laboratorio aislado](../../getting-started/03-first-repository/README.es.md) · [Primer commit](../../getting-started/05-first-commit/README.es.md) · [Merge y conflictos](../../merge-and-conflicts/README.es.md) · [Remotos](../../remote-repositories/README.es.md) · [Reflog y recuperación de commits perdidos](../05-reflog/README.es.md)

**Objetivo:** Guardar temporalmente trabajo staged, unstaged y untracked y restaurarlo deliberadamente.

## Qué y por qué

Stash guarda trabajo local seleccionado como objetos Git referenciados por refs/stash y normalmente devuelve árbol/index afectados a HEAD. Push predeterminado guarda cambios rastreados staged/unstaged, no untracked ni ignorados. `-u` incluye untracked; `-a` incluye ignorados y puede capturar secretos, evítalo sin inspección. `apply` conserva stash, `pop` elimina si aplicación exitosa; `--index` intenta restaurar estado staged. `drop` elimina entrada. Stash es local, no respaldo externo duradero; aplicar sobre historial cambiado puede generar conflicto.

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

Edita note.txt en editor de texto plano a exactamente una línea `staged note` con salto final. Guarda y vuelve a la sesión dedicada.

```text
git add -- note.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Edita note.txt en editor de texto plano a exactamente una línea `working note` con salto final. Guarda y vuelve a la sesión dedicada.

Crea draft.txt untracked con solo `temporary` y salto final. Verifica solo estos cambios ficticios y lista stash vacía; registra HEAD.

```text
git status --short
git stash list
git rev-parse HEAD
git stash push -u -m "lab: temporary notes"
git status --short
git stash list
git stash show --stat --include-untracked 'stash@{0}'
git rev-parse HEAD
```

Esperado estado limpio, un stash, HEAD igual. Confirma entrada exacta y estado limpio antes de aplicar.

```text
git stash apply --index 'stash@{0}'
git status --short
git diff
git diff --cached
git show :note.txt
git stash list
```

Esperado staged note en index, working note en disco, draft.txt untracked, stash aún listado. Lee draft.txt en editor y comprueba temporary. Solo tras confirmar todos datos esperados y que único stash es prescindible, descártalo; no descartes trabajo valioso.

```text
git stash drop 'stash@{0}'
git stash list
git status --short
git rev-parse HEAD
```

Esperado lista vacía, ediciones restauradas iguales, HEAD original. Uso profesional: cambiar tarea brevemente sin confirmar trabajo incompleto; usa rama privada apropiada y respaldo para trabajo duradero.

Tras el ejercicio, cierra editores y sesión dedicada. Elimina solo el padre temporal exacto registrado mediante gestor de archivos si ya no lo necesitas; nunca guía, home o repo de trabajo.

## Errores comunes y seguridad

Si apply/pop genera conflicto, inspecciona estado; stash normalmente se conserva tras pop conflictivo. No hay stash --abort general. Resuelve con cuidado o busca ayuda; no uses hard reset en proyecto real para limpiar conflicto. Entradas eliminadas pueden quedar inalcanzables; recuperación no garantizada.

## Ejercicio y autoevaluación

¿Por qué preferir apply antes de drop en recuperación incierta? Respuesta: inspecciona conservando estado guardado. Aprueba si versiones staged/unstaged y archivo untracked vuelven y HEAD no cambia.

## Referencia rápida

- `git stash push -u -m MESSAGE`
- `git stash list`
- `git stash apply --index 'stash@{0}'`
- `git stash pop`
- `git stash drop 'stash@{0}'`

## Fuentes oficiales

- [Git: git-stash](https://git-scm.com/docs/git-stash)
- [Git: git-status](https://git-scm.com/docs/git-status)

---

<!-- navigation-footer -->
[Anterior](../05-reflog/README.es.md) · [Índice](../README.es.md) · [Siguiente](../07-cherry-pick/README.es.md)
<!-- /navigation-footer -->
