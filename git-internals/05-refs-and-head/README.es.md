# Refs y HEAD: nombrar IDs de objetos

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../04-object-hashes/README.es.md) · [Índice](../README.es.md) · [Siguiente](../06-index-internals/README.es.md)
<!-- /navigation -->

**Nivel:** avanzado · **Tiempo estimado:** 40 min

**Requisitos:** [14 Funcionamiento interno de Git](../README.es.md) · [Git avanzado](../../advanced-git/README.es.md)

**Objetivo:** Ref de rama normalmente nombra commit y avanza al hacer commit en ella.

## Qué es y por qué

Ref de rama normalmente nombra commit y avanza al hacer commit en ella. HEAD normalmente es ref simbólica hacia rama; detached HEAD identifica commit directamente. Refs pueden empaquetarse o guardarse en backends distintos, así que leer archivo específico en .git no es portable. Use comandos conscientes de refs.

```text
HEAD -> refs/heads/main -> commit C
HEAD (detached) ----------> commit P
```

HEAD → refs/heads/main → commit; HEAD separado → commit.

## Práctica

Cree laboratorio aislado nuevo desde índice vinculado de Git avanzado antes de cada práctica. Ejecute comandos individualmente y pare ante resultado inesperado. Compruebe raíz y sandbox impreso. Base Git 2.34+, Bash (Git Bash en Windows).

Inspeccione HEAD simbólico, refs y commit resuelto. Separe en el padre solo en laboratorio desechable limpio; symbolic-ref -q HEAD retorna distinto de cero. Vuelva a main y compruebe limpieza. Si hay trabajo en detached HEAD, preserve con rama antes de cambiar.

```bash
git symbolic-ref HEAD
git show-ref
git rev-parse HEAD
git switch --detach HEAD~1
git symbolic-ref -q HEAD
git rev-parse HEAD
git switch main
git status --short
```

## Errores comunes y seguridad

Use solo laboratorio desechable. Nunca modifique archivos de objetos/refs a mano, fuerce prune ni experimente en repo real. Si estado difiere, inspeccione status, log y plumbing de lectura; cierre shell dedicado y elimine solo sandbox anotado mediante gestor de archivos tras revisar contenido.

## Ejercicio y autocorrección

HEAD → refs/heads/main → commit; HEAD separado → commit. ¿Qué ref avanza al hacer commit separado? Ninguna rama avanza automáticamente.

## Referencia rápida

- `git symbolic-ref HEAD`
- `git show-ref`
- `git rev-parse HEAD`
- `git switch --detach HEAD~1`

## Fuentes oficiales

- [https://git-scm.com/docs/git-symbolic-ref](https://git-scm.com/docs/git-symbolic-ref)
- [https://git-scm.com/docs/git-show-ref](https://git-scm.com/docs/git-show-ref)
- [https://git-scm.com/docs/git-switch](https://git-scm.com/docs/git-switch)

---

<!-- navigation-footer -->
[Anterior](../04-object-hashes/README.es.md) · [Índice](../README.es.md) · [Siguiente](../06-index-internals/README.es.md)
<!-- /navigation-footer -->
