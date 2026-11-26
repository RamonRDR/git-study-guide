# Worktrees: directorios de trabajo paralelos

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../01-bisect/README.es.md) · [Índice](../README.es.md) · [Siguiente](../03-submodules/README.es.md)
<!-- /navigation -->

**Nivel:** avanzado · **Tiempo estimado:** 40 min

**Requisitos:** [13 Git avanzado](../README.es.md) · [Seguridad y gobernanza](../../security/README.es.md)

**Objetivo:** Un worktree vinculado tiene checkout, HEAD e índice propios, pero comparte la mayoría de refs y objetos con el principal.

## Qué es y por qué

Un worktree vinculado tiene checkout, HEAD e índice propios, pero comparte la mayoría de refs y objetos con el principal. Permite un hotfix mientras otra tarea está abierta, sin stash ni clon completo. Git normalmente impide checkout simultáneo de la misma rama. Worktrees no aíslan seguridad ni configuración.

## Práctica

Cree laboratorio aislado nuevo desde índice del módulo antes de cada práctica. Ejecute un comando por vez; pare ante resultado inesperado. Compruebe sandbox impreso y raíz antes de cambiar. Use Git 2.34+ como base de práctica; consulte ayuda y omita funciones opcionales no disponibles. No ejecute en repositorios de producción.

Cree rama review distinta en carpeta hermana; compare HEAD y liste ambos worktrees. Compruebe que el vinculado esté limpio antes de eliminarlo. No fuerce eliminación de worktrees sucios ni borre directorios manualmente; consulte `git worktree list` y reparación oficial si se movió.

```bash
git worktree add -b review "$sandbox/review" HEAD~1
git worktree list
git -C "$sandbox/review" status --short
git -C "$sandbox/review" rev-parse HEAD
git rev-parse HEAD
git worktree remove "$sandbox/review"
git worktree list
```

## Errores comunes y seguridad

Use solo laboratorio desechable y datos ficticios. Si estado difiere, pare; inspeccione estado y operación antes de abortar o recrear laboratorio. Cierre shell dedicado y elimine solo sandbox anotado mediante gestor de archivos tras revisar contenido.

## Ejercicio y autocorrección

¿Un worktree vinculado tiene base de objetos separada? Normalmente no; checkout e índice son separados.

## Referencia rápida

- `git worktree add -b review "$sandbox/review" HEAD~1`
- `git worktree list`
- `git -C "$sandbox/review" status --short`
- `git -C "$sandbox/review" rev-parse HEAD`

## Fuentes oficiales

- [https://git-scm.com/docs/git-worktree](https://git-scm.com/docs/git-worktree)
- [https://git-scm.com/docs/gitrepository-layout](https://git-scm.com/docs/gitrepository-layout)

---

<!-- navigation-footer -->
[Anterior](../01-bisect/README.es.md) · [Índice](../README.es.md) · [Siguiente](../03-submodules/README.es.md)
<!-- /navigation-footer -->
