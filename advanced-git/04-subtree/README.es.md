# Subtree: integrar contenido de otro origen

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../03-submodules/README.es.md) · [Índice](../README.es.md) · [Siguiente](../05-hooks/README.es.md)
<!-- /navigation -->

**Nivel:** avanzado · **Tiempo estimado:** 40 min

**Requisitos:** [13 Git avanzado](../README.es.md) · [Seguridad y gobernanza](../../security/README.es.md)

**Objetivo:** A diferencia de un submódulo, subtree guarda archivos rastreados normales bajo un prefijo.

## Qué es y por qué

A diferencia de un submódulo, subtree guarda archivos rastreados normales bajo un prefijo. El auxiliar opcional git subtree importa y sincroniza otro historial; --squash importa snapshot condensado en vez de unir todo historial. Facilita consumo, pero sincronización y procedencia siguen siendo responsabilidades.

## Práctica

Cree laboratorio aislado nuevo desde índice del módulo antes de cada práctica. Ejecute un comando por vez; pare ante resultado inesperado. Compruebe sandbox impreso y raíz antes de cambiar. Use Git 2.34+ como base de práctica; consulte ayuda y omita funciones opcionales no disponibles. No ejecute en repositorios de producción.

Compruebe `git subtree -h` (ayuda puede retornar código distinto de cero). Si no está disponible, limítese a comparación conceptual; no descargue scripts arbitrarios. Clone laboratorio local conocido, importe bajo prefijo nuevo e inspeccione archivos y grafo. Sin red. Revise licencias y evite sobrescribir prefijo existente.

```bash
git clone --no-hardlinks . "$sandbox/library"
git subtree add --prefix=vendor/library "$sandbox/library" main --squash
git ls-files --stage -- vendor/library
git log --oneline --graph --all -6
```

## Errores comunes y seguridad

Use solo laboratorio desechable y datos ficticios. Si estado difiere, pare; inspeccione estado y operación antes de abortar o recrear laboratorio. Cierre shell dedicado y elimine solo sandbox anotado mediante gestor de archivos tras revisar contenido.

## Ejercicio y autocorrección

¿Qué opción mantiene metadatos de checkout independientes? Submódulo; subtree coloca archivos normales en el padre.

## Referencia rápida

- `git clone --no-hardlinks . "$sandbox/library"`
- `git subtree add --prefix=vendor/library "$sandbox/library" main --squash`
- `git ls-files --stage -- vendor/library`
- `git log --oneline --graph --all -6`

## Fuentes oficiales

- [https://git-scm.com/docs/git-merge](https://git-scm.com/docs/git-merge)
- [https://github.com/git/git/blob/master/contrib/subtree/git-subtree.adoc](https://github.com/git/git/blob/master/contrib/subtree/git-subtree.adoc)
- [https://git-scm.com/docs/gitsubmodules](https://git-scm.com/docs/gitsubmodules)

---

<!-- navigation-footer -->
[Anterior](../03-submodules/README.es.md) · [Índice](../README.es.md) · [Siguiente](../05-hooks/README.es.md)
<!-- /navigation-footer -->
