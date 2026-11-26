# Integración por squash

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../04-conflict-resolution/README.es.md) · [Índice](../README.es.md) · [Siguiente](../06-rebase-and-conflicts/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 30 min

**Requisitos previos:** [Resolver y abortar conflictos de merge](../04-conflict-resolution/README.es.md)

**Objetivo:** Combinar cambios en un nuevo commit sin unir ascendencia de origen.

## Qué es y por qué

`git merge --squash SOURCE` prepara working tree e index combinados como merge pero no mueve HEAD, crea commit ni define MERGE_HEAD. Commit normal posterior tiene un padre, punta previa destino. Commits origen siguen en rama; cambios pueden estar en nuevo snapshot sin ascendencia original. Squash merge GitHub es opción de integración de plataforma con topología similar de un commit, no literalmente este comando local ni garantía de metadatos iguales.

## Práctica

Cree NUEVO lab desechable aislado según módulo 00 capítulo 03 y lección de primer commit. Mantenga shell dedicado original, no terminal del editor. Main inicial debe tener exactamente un commit, note.txt = practice, estado limpio. Cierre shell del lab anterior antes de empezar. Siga verificaciones del capítulo 01 antes de cada operación que cambia historial.

[Configuración aislada del lab](../../getting-started/03-first-repository/README.es.md) · [Primer commit](../../getting-started/05-first-commit/README.es.md) · [Seguridad y recuperación antes de integrar](../01-integration-safety/README.es.md)

```text
git rev-parse --show-toplevel
git branch --show-current
git status --short
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Deténgase si raíz no es lab desechable, rama actual no es la indicada, estado no está limpio antes de iniciar operación o identidades no empiezan con `Study Guide Example <learner@example.invalid>`. Antes de cada commit compruebe también diff preparado; deténgase ante salida inesperada.

```text
git switch -c feat/note
```

En editor de texto plano, cree o edite note.txt con exactamente una línea: feature, con salto final. Guarde y prepare en shell dedicado:

```text
git add -- note.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Si diff y ambas identidades son correctos, haga commit:

```text
git commit -m "docs: revise feature note"
```

En editor de texto plano, cree o edite detail.txt con exactamente una línea: detail, con salto final. Guarde y prepare en shell dedicado:

```text
git add -- detail.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Si diff y ambas identidades son correctos, haga commit:

```text
git commit -m "docs: add detail"
```

```text
git switch main
```

En editor de texto plano, cree o edite overview.txt con exactamente una línea: overview, con salto final. Guarde y prepare en shell dedicado:

```text
git add -- overview.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Si diff y ambas identidades son correctos, haga commit:

```text
git commit -m "docs: add overview"
```

```text
git rev-parse --show-toplevel
git branch --show-current
git status --short
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Confirme main limpia e identidades. Anote IDs main y feature. Prepare squash sin commit aún:

```text
git rev-parse main feat/note
git merge --squash feat/note
git rev-parse HEAD
git diff --cached
git status --short
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

HEAD sin cambio; modificación note y adición detail preparadas. Si conflicto o estado inesperado, deténgase; merge --abort no deshace squash. En lab descarte solo carpeta desechable comprobada y reinicie. Si correcto, registre:

```text
git commit -m "docs: integrate feature changes"
git rev-list --parents -1 HEAD
git log --oneline main..feat/note
git show HEAD:note.txt
git show HEAD:detail.txt
git show HEAD:overview.txt
git status --short
```

Esperado un padre, dos commits origen aún en main..feat/note, tres contenidos presentes y estado limpio. Diagrama: main -> S -> C4 -> C1; feat/note -> C3 -> C2 -> C1. S contiene cambios feature pero C3 no es padre/ancestro de S en lab.

## Errores comunes y seguridad

No use squash para borrar secreto de historial existente. Ascendencia origen permanece en rama origen. Borrado protegido puede rechazar tras squash; compruebe contenido y política en vez de forzar. Sin operación compartida.

Tras cada lab independiente, cierre editor y shell dedicado, luego borre solo carpeta padre temporal exacta anotada en módulo 00 mediante gestor si no necesita. Nunca borre guía, carpeta personal o repo laboral.

## Ejercicio y autoevaluación

¿Commit squash es merge de dos padres? No. Apruebe si HEAD queda igual hasta commit, nuevo commit tiene un padre y cambios origen presentes. Uso profesional: combinar commits pequeños en cambio lógico bajo política acordada.

## Referencia rápida

- `git merge --squash SOURCE`
- `git diff --cached`
- `git commit -m MESSAGE`

## Fuentes oficiales

- [Git: git-merge](https://git-scm.com/docs/git-merge)
- [Git: git-commit](https://git-scm.com/docs/git-commit)
- [Git: git-rev-list](https://git-scm.com/docs/git-rev-list)
- [Git: git-log](https://git-scm.com/docs/git-log)

---

<!-- navigation-footer -->
[Anterior](../04-conflict-resolution/README.es.md) · [Índice](../README.es.md) · [Siguiente](../06-rebase-and-conflicts/README.es.md)
<!-- /navigation-footer -->
