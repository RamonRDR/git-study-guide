# Laboratorio integrado de Git internals

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../10-porcelain-and-plumbing/README.es.md) · [Índice](../README.es.md) · [Siguiente módulo](../../command-reference/README.es.md)
<!-- /navigation -->

**Nivel:** avanzado · **Tiempo estimado:** 55 min

**Requisitos:** [14 Funcionamiento interno de Git](../README.es.md) · [Git avanzado](../../advanced-git/README.es.md)

**Objetivo:** Inspeccione snapshot desde ref rama pasando por commit, tree raíz y blob.

## Qué es y por qué

Inspeccione snapshot desde ref rama pasando por commit, tree raíz y blob. Luego compare stage con HEAD sin commit y compruebe que packing no altera identidad. Es diagnóstico, no reparación manual de objetos. Investigación profesional registra IDs y comandos exactos, no contenido privado.

```text
HEAD -> refs/heads/main -> commit -> root tree -> subtree -> blob
index ---------------------------> prospective tree (write-tree)
```

Apruebe cuando todas pruebas retornen cero.

## Práctica

Cree laboratorio aislado nuevo desde índice vinculado de Git avanzado antes de cada práctica. Ejecute comandos individualmente y pare ante resultado inesperado. Compruebe raíz y sandbox impreso. Base Git 2.34+, Bash (Git Bash en Windows).

Use laboratorio nuevo. Tipos esperados commit, tree y blob; tree preparado difiere del original, HEAD queda fijo y restore devuelve estado limpio. Repack sin opciones de eliminación; confirme blob original legible. Pare ante prueba fallida, inspeccione estado y descarte solo laboratorio si necesario.

```bash
commit=$(git rev-parse HEAD)
tree=$(git rev-parse HEAD^{tree})
blob=$(git rev-parse HEAD:src/state.txt)
test "$(git cat-file -t "$commit")" = commit
test "$(git cat-file -t "$tree")" = tree
test "$(git cat-file -t "$blob")" = blob
test "$(git cat-file -p "$blob")" = bad
printf '%s\n' reviewed > src/state.txt
git add -- src/state.txt
staged=$(git write-tree)
test "$staged" != "$tree"
test "$(git rev-parse HEAD)" = "$commit"
git restore --staged --worktree -- src/state.txt
git repack -a
test "$(git rev-parse HEAD)" = "$commit"
test "$(git cat-file -p "$blob")" = bad
test -z "$(git status --porcelain)"
test -z "$(git remote)"
```

## Errores comunes y seguridad

Use solo laboratorio desechable. Nunca modifique archivos de objetos/refs a mano, fuerce prune ni experimente en repo real. Si estado difiere, inspeccione status, log y plumbing de lectura; cierre shell dedicado y elimine solo sandbox anotado mediante gestor de archivos tras revisar contenido.

## Ejercicio y autocorrección

Apruebe cuando todas pruebas retornen cero. Explique grafo: HEAD → rama → commit → tree → blob; índice → tree futuro. ¿Por qué repack es transparente al grafo? IDs no dependen de codificación de almacenamiento.

## Referencia rápida

- `git add -- src/state.txt`
- `git restore --staged --worktree -- src/state.txt`
- `git repack -a`

## Fuentes oficiales

- [https://git-scm.com/docs/git-cat-file](https://git-scm.com/docs/git-cat-file)
- [https://git-scm.com/docs/git-write-tree](https://git-scm.com/docs/git-write-tree)
- [https://git-scm.com/docs/git-repack](https://git-scm.com/docs/git-repack)
- [https://git-scm.com/docs/git-rev-parse](https://git-scm.com/docs/git-rev-parse)

---

<!-- navigation-footer -->
[Anterior](../10-porcelain-and-plumbing/README.es.md) · [Índice](../README.es.md) · [Siguiente módulo](../../command-reference/README.es.md)
<!-- /navigation-footer -->
