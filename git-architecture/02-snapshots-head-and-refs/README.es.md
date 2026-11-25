# Snapshots, HEAD y referencias

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../01-three-locations/README.es.md) · [Índice](../README.es.md) · [Siguiente](../03-file-states/README.es.md)
<!-- /navigation -->

**Nivel:** principiante · **Tiempo estimado:** 25 min

**Requisitos previos:** [Working tree, index y repositorio](../01-three-locations/README.es.md)

**Objetivo:** Explicar qué representan commit y referencia de rama.

## Qué es y por qué

Commit apunta a árbol que representa snapshot del proyecto y normalmente a commit(s) padre(s), con metadatos de identidad y mensaje. Git almacena objetos direccionados por contenido; contenido igual puede compartir objeto. Git calcula diferencias entre snapshots; commit no es solo parche. Ref es nombre que apunta a objeto (rama, a commit). HEAD normalmente refiere simbólicamente a rama actual; en detached HEAD apunta directamente a commit, tratado después. Antes del primer commit HEAD puede nombrar rama sin commit.

## Práctica

Continúe lab aislado de capítulo 01. Antes de commit compruebe raíz, contenido preparado y ambas identidades. Registre solo versión second preparada:

```text
git rev-parse --show-toplevel
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
git diff --cached
```

Deténgase si raíz incorrecta, identidades no ficticias o diff inesperado. Si todo correcto:

```text
git commit -m "docs: revise note"
git symbolic-ref HEAD
git rev-parse HEAD
git rev-parse refs/heads/main
git log -2 --oneline
git show HEAD:note.txt
git status --short
```

Esperado: refs/heads/main; ambos rev-parse devuelven mismo ID de objeto, variable entre labs. Segundo commit apunta al primero como padre. HEAD:note.txt contiene second; archivo sigue third y status muestra espacio seguido de M. Diagrama: HEAD -> main -> C2 -> C1, última flecha sigue historial de padres.

## Errores comunes y seguridad

No memorice IDs ni suponga main universal. Nunca mueva refs editando .git. IDs dependen de snapshot, padres y metadatos; cambiar historial cambia IDs. No se requiere operación destructiva.

## Ejercicio y autoevaluación

Explique HEAD frente a main frente a ID. Pista: uno apunta rama, otro nombra commit, otro identifica objeto. Respuesta: HEAD normalmente nombra rama actual; rama avanza al commit; ID identifica contenido inmutable del commit. Apruebe si comprueba ambos rev-parse.

## Referencia rápida

- `git rev-parse`
- `git symbolic-ref`
- `git log`
- `git show`
- `gitglossary`

## Fuentes oficiales

- [Git: git-rev-parse](https://git-scm.com/docs/git-rev-parse)
- [Git: git-symbolic-ref](https://git-scm.com/docs/git-symbolic-ref)
- [Git: git-log](https://git-scm.com/docs/git-log)
- [Git: git-show](https://git-scm.com/docs/git-show)
- [Git: gitglossary](https://git-scm.com/docs/gitglossary)
