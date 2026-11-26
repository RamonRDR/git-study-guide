# Commits y tags anotados

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../02-blobs-and-trees/README.es.md) · [Índice](../README.es.md) · [Siguiente](../04-object-hashes/README.es.md)
<!-- /navigation -->

**Nivel:** avanzado · **Tiempo estimado:** 45 min

**Requisitos:** [14 Funcionamiento interno de Git](../README.es.md) · [Git avanzado](../../advanced-git/README.es.md)

**Objetivo:** Commit contiene ID de tree raíz, cero o más padres, autor, committer, fechas y mensaje.

## Qué es y por qué

Commit contiene ID de tree raíz, cero o más padres, autor, committer, fechas y mensaje. Merge tiene varios padres; raíz ninguno. Tags anotados son objetos con metadatos y destino; ligeros son refs sin objeto tag. Firma es metadato adicional, no prueba automática de identidad.

```text
refs/tags/annotated -> tag object -> commit C -> tree T
refs/tags/lightweight ---------------> commit C
refs/heads/main ---------------------> commit C
                                      |
                                      +-> parent P
```

Objeto tag → commit → tree; ref rama → commit.

## Práctica

Cree laboratorio aislado nuevo desde índice vinculado de Git avanzado antes de cada práctica. Ejecute comandos individualmente y pare ante resultado inesperado. Compruebe raíz y sandbox impreso. Base Git 2.34+, Bash (Git Bash en Windows).

Cree tags ficticios sin firma solo en laboratorio. Inspeccione tipos y compare tag anotado resuelto (`^{commit}`) con HEAD. Revisión de release debe registrar commit resuelto en vez de confiar en nombre mostrado. No fuerce tags publicados.

```bash
git cat-file -p HEAD
git rev-list --parents -1 HEAD
git tag lightweight
git tag -a annotated -m "Example release"
git cat-file -t lightweight
git cat-file -t annotated
git cat-file -p annotated
test "$(git rev-parse annotated^{commit})" = "$(git rev-parse HEAD)"
```

## Errores comunes y seguridad

Use solo laboratorio desechable. Nunca modifique archivos de objetos/refs a mano, fuerce prune ni experimente en repo real. Si estado difiere, inspeccione status, log y plumbing de lectura; cierre shell dedicado y elimine solo sandbox anotado mediante gestor de archivos tras revisar contenido.

## Ejercicio y autocorrección

Objeto tag → commit → tree; ref rama → commit. ¿Qué cambia al avanzar main? Ref de rama; tags no avanzan automáticamente.

## Referencia rápida

- `git cat-file -p HEAD`
- `git rev-list --parents -1 HEAD`
- `git tag lightweight`
- `git tag -a annotated -m "Example release"`

## Fuentes oficiales

- [https://git-scm.com/docs/git-commit-tree](https://git-scm.com/docs/git-commit-tree)
- [https://git-scm.com/docs/git-tag](https://git-scm.com/docs/git-tag)
- [https://git-scm.com/docs/git-rev-parse](https://git-scm.com/docs/git-rev-parse)

---

<!-- navigation-footer -->
[Anterior](../02-blobs-and-trees/README.es.md) · [Índice](../README.es.md) · [Siguiente](../04-object-hashes/README.es.md)
<!-- /navigation-footer -->
