# Blobs y trees: nombres y contenido

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../01-object-database/README.es.md) · [Índice](../README.es.md) · [Siguiente](../03-commits-and-tags/README.es.md)
<!-- /navigation -->

**Nivel:** avanzado · **Tiempo estimado:** 45 min

**Requisitos:** [14 Funcionamiento interno de Git](../README.es.md) · [Git avanzado](../../advanced-git/README.es.md)

**Objetivo:** Blob contiene contenido, no ruta ni nombre.

## Qué es y por qué

Blob contiene contenido, no ruta ni nombre. Tree asocia nombre y modo con ID de objeto; subdirectorios usan trees. Mismos bytes pueden compartir blob con nombres distintos. Tree Git es estructura de snapshot, no lista de parches. Revisión profesional puede comparar trees independientemente del checkout.

```text
tree T
  docs/  -> tree D -> guide.txt -> blob A
  src/   -> tree S -> state.txt -> blob B
```

Las flechas muestran relaciones de referencias u operaciones, no rutas de archivos.

## Práctica

Cree laboratorio aislado nuevo desde índice vinculado de Git avanzado antes de cada práctica. Ejecute comandos individualmente y pare ante resultado inesperado. Compruebe raíz y sandbox impreso. Base Git 2.34+, Bash (Git Bash en Windows).

Lea tree y blob por revisión:ruta; compare IDs del blob de estado entre dos commits. IDs difieren porque bytes cambiaron. No manipule archivos de objetos directamente; use comandos Git.

```bash
git ls-tree HEAD
git ls-tree -r HEAD
git cat-file -t HEAD:src/state.txt
git cat-file -p HEAD:src/state.txt
git rev-parse HEAD:src/state.txt
git rev-parse HEAD~1:src/state.txt
git diff HEAD~1 HEAD -- src/state.txt
```

## Errores comunes y seguridad

Use solo laboratorio desechable. Nunca modifique archivos de objetos/refs a mano, fuerce prune ni experimente en repo real. Si estado difiere, inspeccione status, log y plumbing de lectura; cierre shell dedicado y elimine solo sandbox anotado mediante gestor de archivos tras revisar contenido.

## Ejercicio y autocorrección

¿Renombrar archivo sin cambiar contenido puede preservar qué ID? Blob; trees que contienen nombres cambian.

## Referencia rápida

- `git ls-tree HEAD`
- `git ls-tree -r HEAD`
- `git cat-file -t HEAD:src/state.txt`
- `git cat-file -p HEAD:src/state.txt`

## Fuentes oficiales

- [https://git-scm.com/docs/git-ls-tree](https://git-scm.com/docs/git-ls-tree)
- [https://git-scm.com/docs/git-cat-file](https://git-scm.com/docs/git-cat-file)
- [https://git-scm.com/docs/git-diff](https://git-scm.com/docs/git-diff)

---

<!-- navigation-footer -->
[Anterior](../01-object-database/README.es.md) · [Índice](../README.es.md) · [Siguiente](../03-commits-and-tags/README.es.md)
<!-- /navigation-footer -->
