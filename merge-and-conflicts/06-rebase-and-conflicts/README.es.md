# Rebase, abort y continue

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../05-squash-merge/README.es.md) · [Índice](../README.es.md) · [Siguiente](../07-interactive-rebase/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 45 min

**Requisitos previos:** [Integración por squash](../05-squash-merge/README.es.md)

**Objetivo:** Reaplicar commit local sobre nueva base, inspeccionar conflictos y conservar historial original con ref respaldo.

## Qué es y por qué

Rebase selecciona commits de rama y reaplica sobre nueva base; al recrearlos IDs cambian por padres/metadatos. Normalmente mueve rama rebased, no destino. Puede parar por commit. En conflicto de rebase normal, ours es lado ya reaplicado (nueva base más trabajo reaplicado) y theirs es commit en reaplicación, no modelo usual feature frente a main entrante. `--abort` restaura rama original; `--continue` reanuda tras preparar resolución. `--skip` omite parche actual y puede perder cambios; no use en lab.

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
git switch feat/note
git branch backup/feature
```

```text
git rev-parse --show-toplevel
git branch --show-current
git status --short
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Compruebe feat/note limpia, identidades ficticias y respaldo en punta actual. Anote puntas antes de rebase. Provoque conflicto esperado:

```text
git rev-parse main feat/note backup/feature
git rebase main
```

Espere conflicto en note.txt. Compruebe etapas/estado; HEAD puede estar detached durante reaplicación:

```text
git status
git ls-files -u
git show :1:note.txt
git show :2:note.txt
git show :3:note.txt
git rebase --abort
git branch --show-current
git rev-parse feat/note backup/feature
git status --short
```

Esperado base practice, etapa 2 main, 3 feature. Tras abort punta original igual respaldo, feat/note activa y estado limpio. Repita rebase:

```text
git rebase main
```

Confirme conflicto otra vez. Sustituya note.txt ficticio por dos líneas main y feature, salto final, quite marcadores. Prepare y compruebe:

```text
git add -- note.txt
git ls-files -u
git diff --cached
git diff --cached --check
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Si todo resuelto, identidades ficticias y diff correcto, ejecute git rebase --continue. Puede abrir editor de mensaje. Guarde mensaje existente y cierre editor. Si CLI opcional VS Code instalada, use segundo comando en vez del primero (no ambos); --wait espera cierre del archivo. Sin editor utilizable, aborte lab en curso en vez de eludir revisión. Solo tras éxito ejecute inspección:

```text
git rebase --continue
```

```text
git -c core.editor="code --wait" rebase --continue
```

```text
git branch --show-current
git rev-parse main HEAD~1
git rev-parse feat/note backup/feature
git log --all --graph --oneline --decorate
git show HEAD:note.txt
git status --short
```

Esperado feat/note activa, main igual HEAD~1, feature rebased difiere respaldo, archivo combinado, estado limpio. Diagrama: main -> C3 -> C1; backup/feature -> C2 -> C1; feat/note -> C2' -> C3. Respaldo intacto. En rebase sin conflicto, reaplicación acaba sin pausa si ediciones compatibles; compruebe padre y contenido en ambos casos.

## Errores comunes y seguridad

Nunca reescriba rama publicada/compartida aquí. No force push, skip ni suponga ours = su feature. Abort solo rebase en curso. Ref respaldo no es respaldo externo; conserve hasta verificar.

Tras cada lab independiente, cierre editor y shell dedicado, luego borre solo carpeta padre temporal exacta anotada en módulo 00 mediante gestor si no necesita. Nunca borre guía, carpeta personal o repo laboral.

## Ejercicio y autoevaluación

¿Por qué commit recreado tiene ID nuevo? Nuevo padre y metadatos/contenido. Apruebe si abort restaura original, continue crea punta feature sobre main y respaldo conserva anterior. Uso profesional: actualizar trabajo no publicado con cambios de base bajo política del equipo.

## Referencia rápida

- `git rebase main`
- `git rebase --abort`
- `git rebase --continue`

## Fuentes oficiales

- [Git: git-rebase](https://git-scm.com/docs/git-rebase)
- [Git: git-branch](https://git-scm.com/docs/git-branch)
- [Git: git-ls-files](https://git-scm.com/docs/git-ls-files)
- [Git: git-config](https://git-scm.com/docs/git-config)
