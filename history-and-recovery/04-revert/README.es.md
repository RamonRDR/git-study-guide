# Revert sin reescribir historial

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../03-reset/README.es.md) · [Índice](../README.es.md) · [Siguiente](../05-reflog/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 30 min

**Requisitos previos:** [Laboratorio aislado](../../getting-started/03-first-repository/README.es.md) · [Primer commit](../../getting-started/05-first-commit/README.es.md) · [Merge y conflictos](../../merge-and-conflicts/README.es.md) · [Remotos](../../remote-repositories/README.es.md) · [Reset y sus tres modos](../03-reset/README.es.md)

**Objetivo:** Deshacer cambio confirmado añadiendo historial en vez de reescribirlo.

## Qué y por qué

Revert calcula inverso de commit respecto a su padre y aplica al estado actual, normalmente creando nuevo commit. Útil para corregir historial compartido mediante revisión del equipo. Puede generar conflicto si ediciones posteriores se solapan. `--no-edit` usa mensaje generado; `--no-commit` prepara resultado sin confirmar inmediatamente. Commit de merge exige padre mainline elegido conscientemente (`-m`); revertir merge afecta merges futuros, por lo que la lección no ejecuta esa variante.

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

Edita note.txt en editor de texto plano a exactamente una línea `wrong` con salto final. Guarda y vuelve a la sesión dedicada.

```text
git add -- note.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Solo si el diff staged y ambas identidades son correctos, continúa:

```text
git commit -m "docs: add wrong note"
git log --oneline
git show HEAD
git status --short
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Confirma main limpia, identidades ficticias y HEAD como único cambio incorrecto a revertir. Ejecuta:

```text
git revert --no-edit HEAD
git log --oneline
git rev-list --count HEAD
git show HEAD:note.txt
git diff HEAD~2 HEAD
git status --short
```

Esperado C1 -> C2 -> R3, tres commits; C2 sigue ancestro, snapshot R3 igual a C1, estado limpio. Commit inverso no elimina original. En proyecto real revisa/prueba parche inverso antes de publicar.

Tras el ejercicio, cierra editores y sesión dedicada. Elimina solo el padre temporal exacto registrado mediante gestor de archivos si ya no lo necesitas; nunca guía, home o repo de trabajo.

## Errores comunes y seguridad

Si hay conflicto, inspecciona estado y cambios staged; resuelve y usa revert --continue, o revert --abort durante operación. Revert no elimina secretos expuestos del historial; revoca credenciales aparte. Evita revertir commits sin evaluar dependencias.

## Ejercicio y autoevaluación

¿Revertir C2 elimina su ID? Respuesta: no. Aprueba si historial tiene tres commits y contenido HEAD igual al original.

## Referencia rápida

- `git revert --no-edit COMMIT`
- `git revert --no-commit COMMIT`
- `git revert --abort`
- `git revert --continue`

## Fuentes oficiales

- [Git: git-revert](https://git-scm.com/docs/git-revert)
- [Git: git-log](https://git-scm.com/docs/git-log)

---

<!-- navigation-footer -->
[Anterior](../03-reset/README.es.md) · [Índice](../README.es.md) · [Siguiente](../05-reflog/README.es.md)
<!-- /navigation-footer -->
