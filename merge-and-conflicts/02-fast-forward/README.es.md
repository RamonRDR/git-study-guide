# Merge fast-forward

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../01-integration-safety/README.es.md) · [Índice](../README.es.md) · [Siguiente](../03-merge-commit/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 25 min

**Requisitos previos:** [Seguridad y recuperación antes de integrar](../01-integration-safety/README.es.md)

**Objetivo:** Avanzar rama sin crear commit de merge y comprobar ascendencia.

## Qué es y por qué

Si punta destino es ancestro de origen, integración puede hacer fast-forward: mover rama destino al commit origen y actualizar index/working tree. No requiere commit nuevo. `git merge --ff-only SOURCE` rechaza si fast-forward imposible. En gráfico divergente evita commit merge inesperado. Use flags explícitas en vez de depender de configuración.

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
git log --all --oneline --graph --decorate
git rev-parse main feat/note
git status --short
```

Confirme main limpia en C1, origen C2; C2 tiene C1 como padre. Luego:

```text
git merge --ff-only feat/note
git rev-parse main feat/note
git rev-list --count main
git show HEAD:note.txt
git status --short
```

Esperado: IDs iguales, dos commits en main, contenido feature y estado limpio. Antes: main -> C1; feat/note -> C2 -> C1. Después: main y feat/note -> C2 -> C1. Sin tercer commit.

## Errores comunes y seguridad

Si --ff-only rechaza, compruebe gráfico; no fuerce movimiento. No use --abort tras fast-forward completo: no hay merge en curso. Conserve refs origen hasta verificar.

Tras cada lab independiente, cierre editor y shell dedicado, luego borre solo carpeta padre temporal exacta anotada en módulo 00 mediante gestor si no necesita. Nunca borre guía, carpeta personal o repo laboral.

## Ejercicio y autoevaluación

¿Fast-forward añade commit? Respuesta: no; main mueve al C2 existente. Apruebe si main y feat/note resuelven mismo ID. Uso profesional: exigir integración lineal cuando destino no tiene commits exclusivos.

## Referencia rápida

- `git merge --ff-only SOURCE`
- `git rev-parse main SOURCE`

## Fuentes oficiales

- [Git: git-merge](https://git-scm.com/docs/git-merge)
- [Git: git-rev-parse](https://git-scm.com/docs/git-rev-parse)
- [Git: git-rev-list](https://git-scm.com/docs/git-rev-list)

---

<!-- navigation-footer -->
[Anterior](../01-integration-safety/README.es.md) · [Índice](../README.es.md) · [Siguiente](../03-merge-commit/README.es.md)
<!-- /navigation-footer -->
