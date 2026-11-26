# Rebase interactivo y elección de estrategia

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../06-rebase-and-conflicts/README.es.md) · [Índice](../README.es.md) · —
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 40 min

**Requisitos previos:** [Rebase, abort y continue](../06-rebase-and-conflicts/README.es.md)

**Objetivo:** Combinar dos commits locales con fixup y comparar estrategias de integración.

## Qué es y por qué

Rebase interactivo abre lista todo de commits (más antiguo primero). `pick` conserva cambio; `reword` cambia mensaje; `edit` pausa; `squash` combina con anterior y permite editar mensaje; `fixup` combina y normalmente descarta segundo mensaje; `drop` omite commit. Reordenar puede causar conflictos. Herramientas reescriben historial, no ediciones normales. Practicamos solo fixup de dos commits locales con rama respaldo. Editor todo controlado por sequence.editor o GIT_SEQUENCE_EDITOR, distinto del editor de mensaje.

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
git branch backup/feature
git log -3 --oneline
git rev-list --count main..HEAD
```

```text
git rev-parse --show-toplevel
git branch --show-current
git status --short
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Confirme dos commits tras main, feat/note limpia, respaldo en punta e identidades ficticias. Use un comando, no ambos. Primero usa editor configurado; CLI opcional VS Code (si `code --version` funciona) es segunda opción. Si editor desconocido, aprenda guardar/salir antes o aplace práctica manual opcional. No configure editor global para lab.

```text
git rebase -i HEAD~2
```

```text
git -c sequence.editor="code --wait" rebase -i HEAD~2
```

En editor todo, conserve primera línea pick; cambie solo palabra pick de segunda línea a fixup. Conserve IDs reales; placeholders ilustran forma, no pegue:

```text
pick FIRST_ID docs: revise feature note
fixup SECOND_ID docs: add detail
```

Guarde y cierre archivo todo. Si lista difiere, cancele sin guardar ediciones; lista intacta puede hacer rebase sin cambios. Si rebase para por conflicto, aborte o resuelva según capítulo 06. Tras éxito:

```text
git rev-list --count main..HEAD
git rev-list --count main..backup/feature
git log -1 --format=%s
git diff HEAD backup/feature
git show HEAD:note.txt
git show HEAD:detail.txt
git status --short
```

Esperado un nuevo commit frente a dos en respaldo, primer mensaje conservado, diff de extremos vacío (mismo snapshot), contenidos feature y detail, estado limpio. Comparación: ff-only = IDs existentes, sin commit merge nuevo; merge commit = dos padres y ambos historiales; squash = un nuevo commit destino sin ascendencia origen; rebase = commits locales recreados sobre nueva base; rebase interactivo = editar secuencia local antes de integrar. Elija por ascendencia, historial de review y política.

## Errores comunes y seguridad

No use drop, reordenar ni reword en historial compartido. Evite editar IDs o saltar cambios a ciegas. Si resultado completo incorrecto, conserve ref respaldo y deténgase; recuperación completa en módulo 07. Interacción manual con editor no cubierta por CI; pruebas deterministas usan editor todo controlado.

Tras cada lab independiente, cierre editor y shell dedicado, luego borre solo carpeta padre temporal exacta anotada en módulo 00 mediante gestor si no necesita. Nunca borre guía, carpeta personal o repo laboral.

## Ejercicio y autoevaluación

¿Cuándo elegir squash en vez de rebase interactivo? Respuesta: squash integra cambios combinados en un commit destino; rebase interactivo cambia secuencia local origen. Apruebe si snapshot final igual respaldo y conteo distinto. Uso profesional: preparar historial local de review sin reescribir commits compartidos.

## Referencia rápida

- `git rebase -i HEAD~2`
- `pick`
- `fixup`
- `git diff HEAD backup/feature`

## Fuentes oficiales

- [Git: git-rebase](https://git-scm.com/docs/git-rebase)
- [Git: git-config](https://git-scm.com/docs/git-config)
- [Git: git-merge](https://git-scm.com/docs/git-merge)
- [Git: git-diff](https://git-scm.com/docs/git-diff)
