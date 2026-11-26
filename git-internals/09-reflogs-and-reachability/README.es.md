# Reflogs y alcanzabilidad

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../08-gc-and-maintenance/README.es.md) · [Índice](../README.es.md) · [Siguiente](../10-porcelain-and-plumbing/README.es.md)
<!-- /navigation -->

**Nivel:** avanzado · **Tiempo estimado:** 45 min

**Requisitos:** [14 Funcionamiento interno de Git](../README.es.md) · [Git avanzado](../../advanced-git/README.es.md)

**Objetivo:** Objeto es alcanzable desde raíz al recorrer aristas relevantes (padres, trees, blobs y destinos tag).

## Qué es y por qué

Objeto es alcanzable desde raíz al recorrer aristas relevantes (padres, trees, blobs y destinos tag). Reflogs registran localmente actualizaciones de refs, a menudo manteniendo tips anteriores recuperables tras mover rama; expiran y generalmente no se transfieren al clonar. Alcanzabilidad por refs actuales difiere de incluir reflogs e índice.

```text
refs/heads/main -> C -> B -> A
reflog old tip --> D -> B -> A
                 (D may not be reachable from current refs)
```

Las flechas muestran relaciones de referencias u operaciones, no rutas de archivos.

## Práctica

Cree laboratorio aislado nuevo desde índice vinculado de Git avanzado antes de cada práctica. Ejecute comandos individualmente y pare ante resultado inesperado. Compruebe raíz y sandbox impreso. Base Git 2.34+, Bash (Git Bash en Windows).

Inspeccione refs actuales, reflog y grafo alcanzable en laboratorio. Lea HEAD@{1} solo tras confirmar entrada en reflog. En recuperación real, cree rama nueva en commit perdido verificado en vez de reescribir main. Nunca expire reflogs ni prune objetos para recuperar.

```bash
git show-ref
git reflog show HEAD
git rev-list --all
git rev-list --all --reflog
git show --stat 'HEAD@{1}'
```

## Errores comunes y seguridad

Use solo laboratorio desechable. Nunca modifique archivos de objetos/refs a mano, fuerce prune ni experimente en repo real. Si estado difiere, inspeccione status, log y plumbing de lectura; cierre shell dedicado y elimine solo sandbox anotado mediante gestor de archivos tras revisar contenido.

## Ejercicio y autocorrección

¿Reflog garantiza recuperación meses después? No; expiración, config, eliminación o limpieza de objetos pueden quitar evidencia.

## Referencia rápida

- `git show-ref`
- `git reflog show HEAD`
- `git rev-list --all`
- `git rev-list --all --reflog`

## Fuentes oficiales

- [https://git-scm.com/docs/git-reflog](https://git-scm.com/docs/git-reflog)
- [https://git-scm.com/docs/git-rev-list](https://git-scm.com/docs/git-rev-list)
- [https://git-scm.com/docs/git-fsck](https://git-scm.com/docs/git-fsck)

---

<!-- navigation-footer -->
[Anterior](../08-gc-and-maintenance/README.es.md) · [Índice](../README.es.md) · [Siguiente](../10-porcelain-and-plumbing/README.es.md)
<!-- /navigation-footer -->
