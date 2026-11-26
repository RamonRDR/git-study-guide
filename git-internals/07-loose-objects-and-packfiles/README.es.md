# Objetos sueltos y packfiles

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../06-index-internals/README.es.md) · [Índice](../README.es.md) · [Siguiente](../08-gc-and-maintenance/README.es.md)
<!-- /navigation -->

**Nivel:** avanzado · **Tiempo estimado:** 40 min

**Requisitos:** [14 Funcionamiento interno de Git](../README.es.md) · [Git avanzado](../../advanced-git/README.es.md)

**Objetivo:** Objetos pueden estar individuales o en packs con índices y compresión delta.

## Qué es y por qué

Objetos pueden estar individuales o en packs con índices y compresión delta. Empaquetar cambia representación, no identidad ni grafo lógico. Git usa deltas para compresión aunque snapshots lógicos sean trees. Use count-objects para inspeccionar tamaño sin deducir historial del disco.

```text
logical object ID B
       |
       +-> loose object (before repack)
       +-> pack + index (after repack)
          same logical bytes
```

Las flechas muestran relaciones de referencias u operaciones, no rutas de archivos.

## Práctica

Cree laboratorio aislado nuevo desde índice vinculado de Git avanzado antes de cada práctica. Ejecute comandos individualmente y pare ante resultado inesperado. Compruebe raíz y sandbox impreso. Base Git 2.34+, Bash (Git Bash en Windows).

En laboratorio pequeño nuevo, ejecute `git repack -a` (sin opción de eliminación). Compare HEAD y mismo contenido blob antes/después. Conteos y tamaños varían; no suponga número exacto de packs. Use herramientas solo en repos propios y nunca borre packfiles manualmente.

```bash
before=$(git rev-parse HEAD)
git count-objects -v
git repack -a
git count-objects -v
test "$(git rev-parse HEAD)" = "$before"
git cat-file -p HEAD:src/state.txt
```

## Errores comunes y seguridad

Use solo laboratorio desechable. Nunca modifique archivos de objetos/refs a mano, fuerce prune ni experimente en repo real. Si estado difiere, inspeccione status, log y plumbing de lectura; cierre shell dedicado y elimine solo sandbox anotado mediante gestor de archivos tras revisar contenido.

## Ejercicio y autocorrección

¿Blob almacenado como delta se lee normalmente? Sí; Git reconstruye bytes originales.

## Referencia rápida

- `git count-objects -v`
- `git repack -a`
- `git count-objects -v`
- `git cat-file -p HEAD:src/state.txt`

## Fuentes oficiales

- [https://git-scm.com/docs/git-repack](https://git-scm.com/docs/git-repack)
- [https://git-scm.com/docs/git-count-objects](https://git-scm.com/docs/git-count-objects)
- [https://git-scm.com/docs/gitformat-pack](https://git-scm.com/docs/gitformat-pack)

---

<!-- navigation-footer -->
[Anterior](../06-index-internals/README.es.md) · [Índice](../README.es.md) · [Siguiente](../08-gc-and-maintenance/README.es.md)
<!-- /navigation-footer -->
