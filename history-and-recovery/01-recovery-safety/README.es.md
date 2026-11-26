# Inspecciona antes de deshacer

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
— · [Índice](../README.es.md) · [Siguiente](../02-restore/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 20 min

**Requisitos previos:** [Laboratorio aislado](../../getting-started/03-first-repository/README.es.md) · [Primer commit](../../getting-started/05-first-commit/README.es.md) · [Merge y conflictos](../../merge-and-conflicts/README.es.md) · [Remotos](../../remote-repositories/README.es.md)

**Objetivo:** Elegir la operación menos destructiva según el estado Git afectado.

## Qué y por qué

Deshacer no es una sola operación. Restore modifica archivo seleccionado del árbol de trabajo o index, no la punta. Reset en modo commit mueve la rama actual; soft conserva index y archivos, mixed restaura index, hard también reemplaza archivos rastreados. Revert crea nuevo commit inverso. Amend sustituye la punta; cherry-pick reaplica cambio seleccionado como nuevo commit en el caso normal. Stash guarda trabajo local temporal. Reflog registra movimientos locales de refs y puede localizar commits retenidos. Diagrama: árbol de trabajo -> index -> commit; rama apunta a commit y HEAD normalmente apunta a rama. Cambiar un lugar no implica cambiar otros. Historial publicado normalmente se corrige con nuevo commit, no se reescribe.

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

Edita note.txt en editor de texto plano a exactamente una línea `draft` con salto final. Guarda y vuelve a la sesión dedicada.

```text
git status --short
git diff
git diff --cached
git show HEAD:note.txt
git reflog -n 3
```

Esperado: cambio unstaged, diff staged vacío, practice confirmado sin cambios. No deshagas aún. Identifica si trabajo es untracked, unstaged, staged, confirmado o compartido. En incidente real, detén escrituras, preserva evidencias y haz respaldo independiente de archivos valiosos antes de elegir comando. Rama de respaldo conserva solo snapshots confirmados; no respalda archivos de trabajo ni index. En este lab el draft es desechable.

Tras el ejercicio, cierra editores y sesión dedicada. Elimina solo el padre temporal exacto registrado mediante gestor de archivos si ya no lo necesitas; nunca guía, home o repo de trabajo.

## Errores comunes y seguridad

Nunca supongas recuperación de archivo untracked o no guardado. Reflogs son locales y pueden caducar; garbage collection puede eliminar objetos inalcanzables. No ejecutes limpieza o garbage collection para resolver pérdida. Busca ayuda antes de modificar historial compartido.

## Ejercicio y autoevaluación

Un commit publicado es incorrecto; ¿qué operación normalmente preserva colaboración? Pista: añade cambio inverso. Respuesta: revert. Aprueba si explicas por qué rama de respaldo no salva archivo unstaged.

## Referencia rápida

- `git status --short`
- `git diff`
- `git diff --cached`
- `git log --all --graph --oneline`

## Fuentes oficiales

- [Git: git-status](https://git-scm.com/docs/git-status)
- [Git: git-diff](https://git-scm.com/docs/git-diff)
- [Git: git-reflog](https://git-scm.com/docs/git-reflog)
- [Git: git-reset](https://git-scm.com/docs/git-reset)
- [Git: git-revert](https://git-scm.com/docs/git-revert)
