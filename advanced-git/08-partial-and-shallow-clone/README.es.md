# Clones parciales y superficiales

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../07-sparse-checkout/README.es.md) · [Índice](../README.es.md) · [Siguiente](../09-blame-and-grep/README.es.md)
<!-- /navigation -->

**Nivel:** avanzado · **Tiempo estimado:** 45 min

**Requisitos:** [13 Git avanzado](../README.es.md) · [Seguridad y gobernanza](../../security/README.es.md)

**Objetivo:** Clon superficial trunca ascendencia visible con --depth; clon parcial pide conjunto filtrado, como --filter=blob:none, y puede buscar objetos omitidos bajo demanda desde remoto promisor.

## Qué es y por qué

Clon superficial trunca ascendencia visible con --depth; clon parcial pide conjunto filtrado, como --filter=blob:none, y puede buscar objetos omitidos bajo demanda desde remoto promisor. Sparse checkout selecciona rutas de trabajo, otra dimensión. Use superficial en CI acotado si historial profundo es innecesario; parcial exige soporte de servidor y conectividad para objetos omitidos.

## Práctica

Cree laboratorio aislado nuevo desde índice del módulo antes de cada práctica. Ejecute un comando por vez; pare ante resultado inesperado. Compruebe sandbox impreso y raíz antes de cambiar. Use Git 2.34+ como base de práctica; consulte ayuda y omita funciones opcionales no disponibles. No ejecute en repositorios de producción.

Use --no-local para practicar depth contra ruta local propia en vez de optimización de clon local. Compruebe un commit visible y shallow=true. `git fetch --unshallow` desde misma fuente completa restaura ascendencia. Clon parcial es comparación conceptual aquí: no contacte servidor ni suponga filtro aceptado.

```bash
git clone --no-local --depth 1 . "$sandbox/shallow"
git -C "$sandbox/shallow" rev-parse --is-shallow-repository
git -C "$sandbox/shallow" rev-list --count HEAD
git -C "$sandbox/shallow" fetch --unshallow
git -C "$sandbox/shallow" rev-list --count HEAD
```

## Errores comunes y seguridad

Use solo laboratorio desechable y datos ficticios. Si estado difiere, pare; inspeccione estado y operación antes de abortar o recrear laboratorio. Cierre shell dedicado y elimine solo sandbox anotado mediante gestor de archivos tras revisar contenido.

## Ejercicio y autocorrección

¿Qué técnica puede omitir blobs manteniendo ascendencia de commits? Clon parcial, si se admite el filtro.

## Referencia rápida

- `git clone --no-local --depth 1 . "$sandbox/shallow"`
- `git -C "$sandbox/shallow" rev-parse --is-shallow-repository`
- `git -C "$sandbox/shallow" rev-list --count HEAD`
- `git -C "$sandbox/shallow" fetch --unshallow`

## Fuentes oficiales

- [https://git-scm.com/docs/git-clone](https://git-scm.com/docs/git-clone)
- [https://git-scm.com/docs/git-fetch](https://git-scm.com/docs/git-fetch)
- [https://git-scm.com/docs/partial-clone](https://git-scm.com/docs/partial-clone)

---

<!-- navigation-footer -->
[Anterior](../07-sparse-checkout/README.es.md) · [Índice](../README.es.md) · [Siguiente](../09-blame-and-grep/README.es.md)
<!-- /navigation-footer -->
