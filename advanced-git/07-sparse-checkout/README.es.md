# Sparse checkout: seleccionar archivos de trabajo

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../06-rerere/README.es.md) · [Índice](../README.es.md) · [Siguiente](../08-partial-and-shallow-clone/README.es.md)
<!-- /navigation -->

**Nivel:** avanzado · **Tiempo estimado:** 40 min

**Requisitos:** [13 Git avanzado](../README.es.md) · [Seguridad y gobernanza](../../security/README.es.md)

**Objetivo:** Sparse checkout limita rutas rastreadas presentes en working tree, sin quitarlas de commits.

## Qué es y por qué

Sparse checkout limita rutas rastreadas presentes en working tree, sin quitarlas de commits. Cone mode selecciona directorios; también puede mantener archivos en ancestros. Reduce costo de checkout en monorepo. No es control de acceso ni necesariamente reduce historial descargado u objetos guardados.

## Práctica

Cree laboratorio aislado nuevo desde índice del módulo antes de cada práctica. Ejecute un comando por vez; pare ante resultado inesperado. Compruebe sandbox impreso y raíz antes de cambiar. Use Git 2.34+ como base de práctica; consulte ayuda y omita funciones opcionales no disponibles. No ejecute en repositorios de producción.

Use laboratorio nuevo limpio con docs y src. Seleccione docs e inspeccione tree del commit; src/state.txt sigue en HEAD aunque ausente de working tree. Desactive sparse checkout para restaurar checkout completo; no fuerce con cambios locales.

Para compatibilidad con Git 2.34, inicialice el modo cone explícitamente antes de seleccionar directorios. Confirme `core.sparseCheckoutCone` como true; aquí no se usa la sintaxis combinada más reciente `set --cone`.

```bash
git sparse-checkout init --cone
git sparse-checkout set docs
test "$(git config --bool --get core.sparseCheckoutCone)" = true
git sparse-checkout list
git ls-tree -r --name-only HEAD
test ! -f src/state.txt
git sparse-checkout disable
test -f src/state.txt
git status --short
```

## Errores comunes y seguridad

Use solo laboratorio desechable y datos ficticios. Si estado difiere, pare; inspeccione estado y operación antes de abortar o recrear laboratorio. Cierre shell dedicado y elimine solo sandbox anotado mediante gestor de archivos tras revisar contenido.

## Ejercicio y autocorrección

¿Archivo fuera del cono fue borrado de Git? No; snapshot sigue en el commit.

## Referencia rápida

- `git sparse-checkout init --cone`
- `git sparse-checkout set docs`
- `git config --bool --get core.sparseCheckoutCone`
- `git sparse-checkout list`
- `git ls-tree -r --name-only HEAD`
- `git sparse-checkout disable`

## Fuentes oficiales

- [https://git-scm.com/docs/git-sparse-checkout](https://git-scm.com/docs/git-sparse-checkout)
- [https://git-scm.com/docs/git-sparse-checkout/2.34.0](https://git-scm.com/docs/git-sparse-checkout/2.34.0)
- [https://git-scm.com/docs/git-ls-tree](https://git-scm.com/docs/git-ls-tree)

---

<!-- navigation-footer -->
[Anterior](../06-rerere/README.es.md) · [Índice](../README.es.md) · [Siguiente](../08-partial-and-shallow-clone/README.es.md)
<!-- /navigation-footer -->
