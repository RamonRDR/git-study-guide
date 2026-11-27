# El commit perdido

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../03-merge-conflict-laboratory/README.es.md) · [Índice](../README.es.md) · [Siguiente](../05-open-source-contribution/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 45 min

**Prerrequisitos:** [history-and-recovery/05-reflog](../../history-and-recovery/05-reflog/README.es.md) · Git 2.40+ · Bash/Git Bash

**Objetivo:** Crea dos commits, registra segundo ID fuera del repositorio, comprueba checkout limpio, retrocede un commit en laboratorio desechable, localiza commit desplazado con reflog y crea rama de recuperación. Mantén main en primer commit.

## Escenario

Una rama privada de práctica pierde su punta tras reset intencional. Recupera contenido confirmado sin mover main otra vez.

## Preparación desechable

Usa solo la sección Preparación desechable de [Mi primer repositorio](../01-my-first-repository/README.es.md). Abre shell Bash/Git Bash dedicada nueva; comprueba raíz impresa, identidades ficticias y ausencia de remotos antes de seguir. No ejecutes desafío 01. Git 2.40+. Ejecuta un comando a la vez, detente ante fallo inesperado y nunca ejecutes en el guía.

## Desafío

Crea dos commits, registra segundo ID fuera del repositorio, comprueba checkout limpio, retrocede un commit en laboratorio desechable, localiza commit desplazado con reflog y crea rama de recuperación. Mantén main en primer commit. Intenta antes de leer la solución.

## Pistas progresivas

Reflog es local y expira. Compara candidato con ID guardado e inspecciona contenido antes de nombrarlo. Referencia de rama protege historial alcanzable mejor que posición recordada de reflog.

## Solución de referencia

Prepara commits ficticios y confirma estado limpio antes de demostración destructiva. Si prueba de estado falla, detente.

```bash
printf '%s\n' 'status: draft' > notes.txt
git add notes.txt
git commit -m 'docs: initialize notes'
base=$(git rev-parse HEAD)
printf '%s\n' 'status: recovered' > notes.txt
git add notes.txt
git commit -m 'docs: preserve recovery example'
git rev-parse HEAD > "$sandbox/saved-tip.txt"
test -z "$(git status --porcelain)"
git reset --hard "$base"
git reflog show HEAD
```

Identifica punta anterior en reflog mostrado. Inmediatamente tras estos pasos exactos, HEAD@{1} es revisión desplazada; comprueba con ID guardado en vez de suponer posición válida en general.

```bash
candidate=$(git rev-parse 'HEAD@{1}')
test "$candidate" = "$(cat "$sandbox/saved-tip.txt")"
git show "$candidate":notes.txt
git branch recovery/notes "$candidate"
test "$(git rev-parse main)" = "$base"
git show recovery/notes:notes.txt
git status --porcelain
```

## Criterios de éxito

Main queda en base y recovery/notes nombra punta guardada exacta con contenido recovered; working tree limpia. Explica por qué ediciones sin confirmar no tendrían recuperación garantizada.

Prueba fija de mantenimiento (no código de estudiante): `tests/test_git_practical_projects.py::test_lost_commit_recovery`.

## Recuperación y limpieza

No ejecutes reset --hard fuera de este laboratorio nuevo. Si candidato difiere, detente e inspecciona reflog e ID guardado; evita recolección durante recuperación. Recuperación no garantizada si desaparecen objetos. Cierra la shell dedicada y elimina solo el sandbox impreso verificado mediante gestor de archivos. Conserva antes trabajo deseado.

## Fuentes oficiales

- <https://git-scm.com/docs/git-reset>
- <https://git-scm.com/docs/git-reflog>
- <https://git-scm.com/docs/git-branch>
- <https://git-scm.com/docs/git-show>

---

<!-- navigation-footer -->
[Anterior](../03-merge-conflict-laboratory/README.es.md) · [Índice](../README.es.md) · [Siguiente](../05-open-source-contribution/README.es.md)
<!-- /navigation-footer -->
