# Resolver y abortar conflictos de merge

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../03-merge-commit/README.es.md) · [Índice](../README.es.md) · [Siguiente](../05-squash-merge/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 45 min

**Requisitos previos:** [Divergencia y commits de merge](../03-merge-commit/README.es.md)

**Objetivo:** Inspeccionar etapas no fusionadas del index, abortar con seguridad, resolver y completar merge.

## Qué es y por qué

Conflicto textual puede ocurrir cuando ramas editan misma línea de modo incompatible. Git pausa con entradas no fusionadas en index: etapa 1 base, 2 lado actual, 3 entrante en merge normal. Marcadores muestran alternativas: <<<<<<< HEAD, =======, >>>>>>> origen. No son contenido final. Resuelva entendiendo ambos cambios; editar/guardar no resuelve index. `git add` marca ruta resuelta. `git merge --continue` concluye merge y puede abrir editor del mensaje; `git commit -m` también concluye si todas rutas resueltas.

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

```text
git switch main
```

En editor de texto plano, cree o edite note.txt con exactamente una línea: main, con salto final. Guarde y prepare en shell dedicado:

```text
git add -- note.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Si diff y ambas identidades son correctos, haga commit:

```text
git commit -m "docs: revise main note"
```

```text
git rev-parse --show-toplevel
git branch --show-current
git status --short
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Confirme main limpia e identidades. Anote ID main en privado. Provoque conflicto intencional:

```text
git rev-parse main
git merge --no-ff --no-edit feat/note
```

Espere no cero y conflicto en note.txt. Deténgase si diferente. Inspeccione, incluso abriendo note.txt en editor simple:

```text
git status --short
git ls-files -u
git show :1:note.txt
git show :2:note.txt
git show :3:note.txt
```

Esperado UU note.txt, tres etapas, base practice, actual main, entrante feature. Aborte primero, con operación en curso:

```text
git merge --abort
git status --short
git rev-parse main
git show HEAD:note.txt
```

Espere main limpia, ID original y contenido main. Repita mismo merge:

```text
git merge --no-ff --no-edit feat/note
```

Tras confirmar mismo conflicto, sustituya note.txt ficticio entero por dos líneas, main y luego feature, salto final; quite marcadores. Compruebe antes de registrar:

```text
git add -- note.txt
git ls-files -u
git diff --cached
git diff --cached --check
git status
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Sin entradas no fusionadas ni errores diff-check; lea archivo real para asegurar ausencia de marcadores. Con contenido esperado e identidades ficticias, concluya con mensaje explícito (o git merge --continue guardando mensaje del editor, no ambos):

```text
git commit -m "docs: resolve note conflict"
git rev-list --parents -1 HEAD
git show HEAD:note.txt
git status --short
```

Esperado dos padres, archivo combinado de dos líneas y estado limpio. Si usa continue y abre editor desconocido, consulte instrucciones; no borre mensaje al azar. Aborte mientras merge siga en curso si duda.

## Errores comunes y seguridad

No elija ours/theirs a ciegas; entienda ediciones. En rebase lados difieren de merge normal. Nunca fuerce resolución ni trate quitar marcadores como validación. Proyecto real necesita pruebas y review; conflictos binarios/borrado/renombre pueden requerir otras decisiones.

Tras cada lab independiente, cierre editor y shell dedicado, luego borre solo carpeta padre temporal exacta anotada en módulo 00 mediante gestor si no necesita. Nunca borre guía, carpeta personal o repo laboral.

## Ejercicio y autoevaluación

¿Qué distingue editado de resuelto? Respuesta: add sustituye etapas no fusionadas por resultado elegido. Apruebe si abort restaura estado, repetición resuelve etapas y commit final tiene dos padres. Uso profesional: conservar intención y probar resolución.

## Referencia rápida

- `git ls-files -u`
- `git show :1:note.txt`
- `git add -- note.txt`
- `git merge --abort`
- `git merge --continue`

## Fuentes oficiales

- [Git: git-merge](https://git-scm.com/docs/git-merge)
- [Git: git-ls-files](https://git-scm.com/docs/git-ls-files)
- [Git: git-show](https://git-scm.com/docs/git-show)
- [Git: git-diff](https://git-scm.com/docs/git-diff)
- [Git: git-commit](https://git-scm.com/docs/git-commit)
