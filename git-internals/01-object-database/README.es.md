# Base de objetos: almacenamiento del repositorio

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Módulo anterior](../../advanced-git/README.es.md) · [Índice](../README.es.md) · [Siguiente](../02-blobs-and-trees/README.es.md)
<!-- /navigation -->

**Nivel:** avanzado · **Tiempo estimado:** 40 min

**Requisitos:** [14 Funcionamiento interno de Git](../README.es.md) · [Git avanzado](../../advanced-git/README.es.md)

**Objetivo:** Git almacena objetos tipados identificados por contenido: blob (contenido de archivo), tree (entradas de directorio), commit (snapshot y ascendencia), tag anotado (metadatos de objeto nombrado).

## Qué es y por qué

Git almacena objetos tipados identificados por contenido: blob (contenido de archivo), tree (entradas de directorio), commit (snapshot y ascendencia), tag anotado (metadatos de objeto nombrado). Refs nombran objetos; working tree e índice no son base de objetos. Use distinción al diagnosticar datos ausentes o explicar por qué checkout no es copia.

```text
refs/heads/main -> commit C -> tree T -> tree S -> blob B
                     |
                     +-> parent P -> tree U
```

Commit → tree raíz → tree de directorio → blob.

## Práctica

Cree laboratorio aislado nuevo desde índice vinculado de Git avanzado antes de cada práctica. Ejecute comandos individualmente y pare ante resultado inesperado. Compruebe raíz y sandbox impreso. Base Git 2.34+, Bash (Git Bash en Windows).

Inspeccione tipo y tamaño de HEAD y liste objetos alcanzables. `git count-objects -v` informa estadísticas de almacenamiento, no número de commits. Observe que commit apunta a tree, no directamente a cada archivo de trabajo.

```bash
git cat-file -t HEAD
git cat-file -s HEAD
git cat-file -p HEAD
git rev-list --objects --all
git count-objects -v
```

## Errores comunes y seguridad

Use solo laboratorio desechable. Nunca modifique archivos de objetos/refs a mano, fuerce prune ni experimente en repo real. Si estado difiere, inspeccione status, log y plumbing de lectura; cierre shell dedicado y elimine solo sandbox anotado mediante gestor de archivos tras revisar contenido.

## Ejercicio y autocorrección

Commit → tree raíz → tree de directorio → blob. Arista padre une commits; refs apuntan a IDs. ¿Qué tipo guarda bytes de archivo? Blob.

## Referencia rápida

- `git cat-file -t HEAD`
- `git cat-file -s HEAD`
- `git cat-file -p HEAD`
- `git rev-list --objects --all`

## Fuentes oficiales

- [https://git-scm.com/docs/git-cat-file](https://git-scm.com/docs/git-cat-file)
- [https://git-scm.com/docs/git-count-objects](https://git-scm.com/docs/git-count-objects)
- [https://git-scm.com/docs/gitrepository-layout](https://git-scm.com/docs/gitrepository-layout)

---

<!-- navigation-footer -->
[Módulo anterior](../../advanced-git/README.es.md) · [Índice](../README.es.md) · [Siguiente](../02-blobs-and-trees/README.es.md)
<!-- /navigation-footer -->
