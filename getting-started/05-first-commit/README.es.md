# Primer commit

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../04-editor-and-gui/README.es.md) · [Índice](../README.es.md) · [Siguiente módulo](../../fundamentals/README.es.md)
<!-- /navigation -->

**Nivel:** principiante · **Tiempo estimado:** 35 min

**Requisitos previos:** [VS Code e interfaces gráficas](../04-editor-and-gui/README.es.md)

**Objetivo:** Preparar y registrar archivo de texto; comprobar historial local.

## Qué es y por qué

Commit registra snapshot del contenido preparado con información histórica. Working tree contiene archivos editables; staging area (index) guarda contenido seleccionado para próximo commit; repo local guarda historial. Editar tras stage no cambia index automáticamente. Commit no es subida.

## Práctica

Use shell dedicado original del capítulo 03. Si se cerró, repita capítulo en lab nuevo. Compruebe raíz y ambas identidades efectivas con `git var GIT_AUTHOR_IDENT` y `git var GIT_COMMITTER_IDENT`. Ambas deben comenzar con `Study Guide Example <learner@example.invalid>`; si alguna difiere, deténgase. No haga commit desde editor ni terminal integrada.

Use mismo lab desechable, compruebe raíz y status, y cree note.txt nuevo con línea practice y salto final. Comandos sobrescriben archivos; no ejecute si note.txt ya existe.

```powershell
Set-Content -Path note.txt -Value "practice" -Encoding ascii
```

```bash
printf 'practice\n' > note.txt
```

Ejecute por separado; compruebe cada resultado:

```text
git status
git add note.txt
git status
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
git commit -m "docs: add note"
git status
git log -1 --oneline
git show HEAD:note.txt
git log -1 --format=fuller
```

Deténgase inmediatamente antes del commit si alguna identidad difiere de la ficticia; no ejecute comandos restantes. Log final muestra autor y committer, ambos ficticios. Antes de add: archivo no rastreado; después: archivo nuevo preparado; diff cached: línea practice; tras commit: status limpio, un commit con mensaje, practice almacenado. HEAD identifica checkout actual, normalmente rama actual. Hashes, fechas, salidas localizadas y avisos de finales varían. Flujo: archivo de trabajo -> add -> index -> commit -> historial local.

## Errores comunes y seguridad

Si falta autoría, compruebe configuración local. Si nada preparado, mire status y seleccione solo archivo deseado. Evite `git add .` en proyectos desconocidos. Si preparó contenido incorrecto, deténgase y cree lab nuevo en vez de comandos destructivos. No eluda políticas de firma o hooks. Conserve lab y shell original para módulo 01. Tras práctica, cierre editor y terminal dedicada (descartando entorno aislado); borre solo carpeta padre temporal anotada mediante gestor si ya no necesita. Nunca borre proyectos ni configuración normal.

## Ejercicio y autoevaluación

Prediga status tras escribir, add y commit. Pista: siga tres ubicaciones. Apruebe cuando log muestre mensaje, show devuelva practice y status limpio. Explique por qué edición tras add necesita otro add para inclusión. Hábito profesional: revisar diff preparado antes de registrar.

## Referencia rápida

- `git status`
- `git add note.txt`
- `git diff --cached`
- `git commit -m "docs: add note"`
- `git log -1 --oneline`
- `git show HEAD:note.txt`

## Fuentes oficiales

- [https://git-scm.com/docs/gittutorial](https://git-scm.com/docs/gittutorial)
- [https://git-scm.com/docs/git-add](https://git-scm.com/docs/git-add)
- [https://git-scm.com/docs/git-commit](https://git-scm.com/docs/git-commit)
- [https://git-scm.com/docs/git-status](https://git-scm.com/docs/git-status)

---

<!-- navigation-footer -->
[Anterior](../04-editor-and-gui/README.es.md) · [Índice](../README.es.md) · [Siguiente módulo](../../fundamentals/README.es.md)
<!-- /navigation-footer -->
