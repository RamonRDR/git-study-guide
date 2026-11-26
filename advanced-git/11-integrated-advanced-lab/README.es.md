# Laboratorio integrado de Git avanzado

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../10-archive-and-bundle/README.es.md) · [Índice](../README.es.md) · [Siguiente módulo](../../git-internals/README.es.md)
<!-- /navigation -->

**Nivel:** avanzado · **Tiempo estimado:** 55 min

**Requisitos:** [13 Git avanzado](../README.es.md) · [Seguridad y gobernanza](../../security/README.es.md)

**Objetivo:** Simule revisión de regresión manteniendo main estable y prepare transferencia offline del historial.

## Qué es y por qué

Simule revisión de regresión manteniendo main estable y prepare transferencia offline del historial. El ejercicio une worktree, inspección y bundle sin cambiar historial de main. En trabajo profesional, guarde evidencia de revisión probada, revise diff y valide recuperación antes de entrega.

## Práctica

Cree laboratorio aislado nuevo desde índice del módulo antes de cada práctica. Ejecute un comando por vez; pare ante resultado inesperado. Compruebe sandbox impreso y raíz antes de cambiar. Use Git 2.34+ como base de práctica; consulte ayuda y omita funciones opcionales no disponibles. No ejecute en repositorios de producción.

Ejecute en laboratorio nuevo, un comando a la vez. Worktree de revisión debe mostrar ok, main bad; clon bundle debe coincidir con main original. Todos checks deben pasar; si no, pare e inspeccione. Sin red ni publicación. Elimine worktree limpio normalmente; conserve sandbox para revisión.

```bash
before=$(git rev-parse HEAD)
git worktree add -b review "$sandbox/review" HEAD~1
test "$(git -C "$sandbox/review" show HEAD:src/state.txt)" = ok
test "$(git show HEAD:src/state.txt)" = bad
git worktree remove "$sandbox/review"
git bundle create "$sandbox/history.bundle" main
git bundle verify "$sandbox/history.bundle"
git clone -b main "$sandbox/history.bundle" "$sandbox/recovered"
test "$(git -C "$sandbox/recovered" rev-parse HEAD)" = "$before"
test "$(git rev-parse HEAD)" = "$before"
test -z "$(git status --porcelain)"
test -z "$(git remote)"
```

## Errores comunes y seguridad

Use solo laboratorio desechable y datos ficticios. Si estado difiere, pare; inspeccione estado y operación antes de abortar o recrear laboratorio. Cierre shell dedicado y elimine solo sandbox anotado mediante gestor de archivos tras revisar contenido.

## Ejercicio y autocorrección

Apruebe cuando cada test retorne cero, main esté limpia y tip recuperado coincida. Explique por qué bundle no es copia de toda estación.

## Referencia rápida

- `git worktree add -b review "<sandbox>/review" HEAD~1`
- `git worktree remove "<sandbox>/review"`
- `git bundle create "<sandbox>/history.bundle" main`
- `git bundle verify "<sandbox>/history.bundle"`

## Fuentes oficiales

- [https://git-scm.com/docs/git-worktree](https://git-scm.com/docs/git-worktree)
- [https://git-scm.com/docs/git-bundle](https://git-scm.com/docs/git-bundle)
- [https://git-scm.com/docs/git-status](https://git-scm.com/docs/git-status)

---

<!-- navigation-footer -->
[Anterior](../10-archive-and-bundle/README.es.md) · [Índice](../README.es.md) · [Siguiente módulo](../../git-internals/README.es.md)
<!-- /navigation-footer -->
