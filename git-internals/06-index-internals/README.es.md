# Internals del índice: entradas preparadas

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../05-refs-and-head/README.es.md) · [Índice](../README.es.md) · [Siguiente](../07-loose-objects-and-packfiles/README.es.md)
<!-- /navigation -->

**Nivel:** avanzado · **Tiempo estimado:** 45 min

**Requisitos:** [14 Funcionamiento interno de Git](../README.es.md) · [Git avanzado](../../advanced-git/README.es.md)

**Objetivo:** Índice registra rutas, modos, IDs y metadatos del tree futuro.

## Qué es y por qué

Índice registra rutas, modos, IDs y metadatos del tree futuro. Entradas normales tienen stage 0; merge sin resolver puede tener stages 1 (base), 2 (ours) y 3 (theirs), según conflicto. `write-tree` materializa tree del índice resuelto sin commit. Evite editar índice binario directamente.

```text
working tree --add--> index --write-tree--> tree object
                       |                      |
                       +--- git commit ------> commit -> branch ref advances
```

Archivo → add → índice (stage 0) → write-tree → objeto tree; commit también avanza rama actual.

## Práctica

Cree laboratorio aislado nuevo desde índice vinculado de Git avanzado antes de cada práctica. Ejecute comandos individualmente y pare ante resultado inesperado. Compruebe raíz y sandbox impreso. Base Git 2.34+, Bash (Git Bash en Windows).

Prepare una edición ficticia en laboratorio nuevo. Compare IDs blob preparado y HEAD. `git write-tree` escribe o reutiliza trees; no mueve HEAD. Use `git ls-files -u` para inspeccionar entradas en laboratorio de conflicto, no para crear conflictos aquí. Restaure archivo preparado y trabajo solo en este laboratorio desechable.

```bash
before=$(git rev-parse HEAD)
git ls-files --stage
printf '%s\n' reviewed > src/state.txt
git add -- src/state.txt
git ls-files --stage -- src/state.txt
git diff --cached -- src/state.txt
git write-tree
test "$(git rev-parse HEAD)" = "$before"
git restore --staged --worktree -- src/state.txt
git status --short
```

## Errores comunes y seguridad

Use solo laboratorio desechable. Nunca modifique archivos de objetos/refs a mano, fuerce prune ni experimente en repo real. Si estado difiere, inspeccione status, log y plumbing de lectura; cierre shell dedicado y elimine solo sandbox anotado mediante gestor de archivos tras revisar contenido.

## Ejercicio y autocorrección

Archivo → add → índice (stage 0) → write-tree → objeto tree; commit también avanza rama actual. ¿Por qué write-tree puede fallar en conflictos? Índice tiene entradas sin resolver.

## Referencia rápida

- `git ls-files --stage`
- `git add -- src/state.txt`
- `git ls-files --stage -- src/state.txt`
- `git diff --cached -- src/state.txt`

## Fuentes oficiales

- [https://git-scm.com/docs/git-ls-files](https://git-scm.com/docs/git-ls-files)
- [https://git-scm.com/docs/git-write-tree](https://git-scm.com/docs/git-write-tree)
- [https://git-scm.com/docs/gitformat-index](https://git-scm.com/docs/gitformat-index)

---

<!-- navigation-footer -->
[Anterior](../05-refs-and-head/README.es.md) · [Índice](../README.es.md) · [Siguiente](../07-loose-objects-and-packfiles/README.es.md)
<!-- /navigation-footer -->
