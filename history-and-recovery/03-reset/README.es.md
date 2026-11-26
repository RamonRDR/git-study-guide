# Reset y sus tres modos

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../02-restore/README.es.md) · [Índice](../README.es.md) · [Siguiente](../04-revert/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 40 min

**Requisitos previos:** [Laboratorio aislado](../../getting-started/03-first-repository/README.es.md) · [Primer commit](../../getting-started/05-first-commit/README.es.md) · [Merge y conflictos](../../merge-and-conflicts/README.es.md) · [Remotos](../../remote-repositories/README.es.md) · [Restore: archivos de trabajo e index](../02-restore/README.es.md)

**Objetivo:** Predecir estado de rama, index y árbol en cada modo reset.

## Qué y por qué

Reset en modo commit mueve rama actual al commit objetivo. Con --soft index y árbol no cambian; --mixed (por defecto) restablece index pero conserva archivos; --hard restablece ambos y puede sobrescribir o borrar rutas untracked obstructivas. Reset en modo ruta (ej. `git reset HEAD -- PATH`) cambia index, no rama. Diagrama desde C2 limpio: soft -> main C1, index C2, disco C2; mixed -> main C1, index C1, disco C2; hard -> main C1, index C1, disco C1. Usa solo historial no publicado cuando se pretenda reescritura; usa revert en historial compartido.

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

Edita note.txt en editor de texto plano a exactamente una línea `second` con salto final. Guarda y vuelve a la sesión dedicada.

```text
git add -- note.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Solo si el diff staged y ambas identidades son correctos, continúa:

```text
git commit -m "docs: add second version"
git branch backup/second
git rev-parse HEAD HEAD^ backup/second
git status --short
```

Registra IDs C2 y C1. Confirma main limpia en C2, backup/second en C2, sin remotos. Ejecuta soft primero:

```text
git reset --soft HEAD^
git rev-parse HEAD
git show :note.txt
git diff --cached
git diff
```

Esperado main C1; index/disco second; solo diff staged. Ahora restablece index a HEAD actual sin mover main:

```text
git reset --mixed HEAD
git rev-parse HEAD
git show :note.txt
git diff
git diff --cached
```

Esperado main C1, index practice, disco second; solo diff unstaged. Antes de hard, confirma raíz, main, sin remotos, backup/second aún C2 y único cambio edición desechable de note.txt. No continúes si existe otro trabajo. Lo siguiente descarta intencionalmente la edición.

```text
git reset --hard HEAD
git status --short
git show HEAD:note.txt
git show backup/second:note.txt
git merge --ff-only backup/second
git rev-parse HEAD backup/second
git status --short
```

Esperado practice limpio tras hard; backup conserva second. Fast-forward restaura C2 sin inventar commit. Uso profesional: soft puede reagrupar commits privados, pero comprueba política y respaldo.

Tras el ejercicio, cierra editores y sesión dedicada. Elimina solo el padre temporal exacto registrado mediante gestor de archivos si ya no lo necesitas; nunca guía, home o repo de trabajo.

## Errores comunes y seguridad

Hard no es deshacer genérico ni solución a push rechazado. Rama de respaldo guarda solo datos confirmados. ORIG_HEAD puede registrar punta anterior pero sobrescribirse; usa refs verificadas y reflog si disponible. Nunca cuentes con recuperación garantizada.

## Ejercicio y autoevaluación

Tras mixed de C2 limpio a C1, ¿dónde está edición C2? Respuesta: árbol, no index. Aprueba si predices tres lugares y demuestras punta de respaldo conservada.

## Referencia rápida

- `git reset --soft COMMIT`
- `git reset --mixed COMMIT`
- `git reset --hard COMMIT`
- `git reset HEAD -- PATH`

## Fuentes oficiales

- [Git: git-reset](https://git-scm.com/docs/git-reset)
- [Git: git-merge](https://git-scm.com/docs/git-merge)
- [Git: git-reflog](https://git-scm.com/docs/git-reflog)
