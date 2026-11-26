# Divergencia y commits de merge

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../02-fast-forward/README.es.md) · [Índice](../README.es.md) · [Siguiente](../04-conflict-resolution/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 35 min

**Requisitos previos:** [Merge fast-forward](../02-fast-forward/README.es.md)

**Objetivo:** Distinguir merge de dos padres de fast-forward y comprobar ambos padres.

## Qué es y por qué

Cuando ambas ramas tienen commits exclusivos, ninguna punta es ancestro de otra. Merge normal de dos puntas combina cambios usando base común. Commit merge exitoso registra snapshot combinado con dos padres (primero: destino anterior; segundo: origen). `--no-ff` solicita commit merge incluso si fast-forward posible, salvo si ya actualizado. `--no-edit` acepta mensaje generado. Merge conserva ascendencia de ambas líneas.

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

Confirme main limpia, identidades ficticias y gráfico divergente previsto. Primero pruebe operación protegida (debe fallar sin cambiar historial):

```text
git log --all --graph --oneline --decorate
git rev-parse main feat/note
git merge --ff-only feat/note
```

Tras rechazo, compruebe puntas y estado sin cambios. Luego integre:

```text
git status --short
git rev-parse main feat/note
git merge --no-ff --no-edit feat/note
git log --all --graph --oneline --decorate
git rev-list --parents -1 HEAD
git show HEAD:note.txt
git show HEAD:overview.txt
git status --short
```

Esperado: nuevo M con dos padres, note feature y overview overview; estado limpio. Antes: C2 -> C1 <- C3 (C2 origen, C3 destino; flechas apuntan a padres). Después: main -> M, M -> C3 y C2, ambos -> C1; feat/note aún -> C2. rev-list muestra tres IDs: M, C3, C2.

## Errores comunes y seguridad

Si conflicto inesperado, use status y abort de merge normal del capítulo 01; no prepare contenido aleatorio. Inspeccione ramas antes; merge exitoso solo no prueba corrección.

Tras cada lab independiente, cierre editor y shell dedicado, luego borre solo carpeta padre temporal exacta anotada en módulo 00 mediante gestor si no necesita. Nunca borre guía, carpeta personal o repo laboral.

## Ejercicio y autoevaluación

¿Por qué rechazó --ff-only? Puntas tienen commits exclusivos. Apruebe si merge tiene dos padres y ambos contenidos. Uso profesional: conservar historial de integración cuando política permite commits merge.

## Referencia rápida

- `git merge --no-ff --no-edit SOURCE`
- `git rev-list --parents -1 HEAD`

## Fuentes oficiales

- [Git: git-merge](https://git-scm.com/docs/git-merge)
- [Git: git-rev-list](https://git-scm.com/docs/git-rev-list)
- [Git: git-log](https://git-scm.com/docs/git-log)
