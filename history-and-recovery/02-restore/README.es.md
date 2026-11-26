# Restore: archivos de trabajo e index

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../01-recovery-safety/README.es.md) · [Índice](../README.es.md) · [Siguiente](../03-reset/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 25 min

**Requisitos previos:** [Laboratorio aislado](../../getting-started/03-first-repository/README.es.md) · [Primer commit](../../getting-started/05-first-commit/README.es.md) · [Merge y conflictos](../../merge-and-conflicts/README.es.md) · [Remotos](../../remote-repositories/README.es.md) · [Inspecciona antes de deshacer](../01-recovery-safety/README.es.md)

**Objetivo:** Distinguir quitar del stage de descartar edición.

## Qué y por qué

Con ruta, `git restore -- PATH` copia del index al árbol de trabajo por defecto. `git restore --staged -- PATH` usa HEAD como fuente predeterminada y cambia solo el index. `--source=COMMIT` elige otro árbol; `--staged --worktree` cambia ambos destinos. No hay nuevo commit ni movimiento de rama. Archivo rastreado ausente en fuente puede eliminarse. Usa restore específico tras inspeccionar diferencias; evita restauración masiva con trabajo valioso.

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

Edita note.txt en editor de texto plano a exactamente una línea `staged draft` con salto final. Guarda y vuelve a la sesión dedicada.

```text
git add -- note.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Edita note.txt en editor de texto plano a exactamente una línea `working draft` con salto final. Guarda y vuelve a la sesión dedicada.

```text
git status --short
git diff
git diff --cached
git show :note.txt
git show HEAD:note.txt
```

Espera staged draft en index, working draft en disco y practice en HEAD. El próximo comando descarta intencionalmente SOLO la edición de trabajo. Detente si borradores no son desechables o raíz no está verificada.

```text
git restore -- note.txt
git status --short
git diff
git diff --cached
git restore --staged -- note.txt
git status --short
git diff
git diff --cached
```

Tras primer restore, disco = staged draft; tras quitar stage, index = practice y disco sigue staged draft. Confirma ausencia de trabajo útil antes del paso destructivo final.

```text
git restore -- note.txt
git status --short
git rev-list --count HEAD
git show HEAD:note.txt
```

Esperado estado limpio, un commit, contenido practice. Uso profesional: quita cambios seleccionados por error sin perder edición.

Tras el ejercicio, cierra editores y sesión dedicada. Elimina solo el padre temporal exacto registrado mediante gestor de archivos si ya no lo necesitas; nunca guía, home o repo de trabajo.

## Errores comunes y seguridad

Restore puede descartar ediciones unstaged permanentemente. Reflog no registra ediciones del árbol. Si restauraste trabajo útil, detente y comprueba respaldos independientes o historial del editor; recuperación no garantizada.

## Ejercicio y autoevaluación

¿Qué comando quita archivo del stage conservando edición? Respuesta: restore --staged -- note.txt. Aprueba si diff staged vacío y diff normal aún muestra edición.

## Referencia rápida

- `git restore -- PATH`
- `git restore --staged -- PATH`
- `git restore --source=COMMIT -- PATH`

## Fuentes oficiales

- [Git: git-restore](https://git-scm.com/docs/git-restore)
- [Git: git-diff](https://git-scm.com/docs/git-diff)

---

<!-- navigation-footer -->
[Anterior](../01-recovery-safety/README.es.md) · [Índice](../README.es.md) · [Siguiente](../03-reset/README.es.md)
<!-- /navigation-footer -->
