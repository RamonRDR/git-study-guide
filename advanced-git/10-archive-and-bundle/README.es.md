# Archive y bundle: distribuir snapshots o historial

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../09-blame-and-grep/README.es.md) · [Índice](../README.es.md) · [Siguiente](../11-integrated-advanced-lab/README.es.md)
<!-- /navigation -->

**Nivel:** avanzado · **Tiempo estimado:** 40 min

**Requisitos:** [13 Git avanzado](../README.es.md) · [Seguridad y gobernanza](../../security/README.es.md)

**Objetivo:** Archive exporta tree seleccionado (sujeto a atributos) sin historial; bundle empaqueta refs y objetos Git y sirve como fuente de transferencia sin conexión.

## Qué es y por qué

Archive exporta tree seleccionado (sujeto a atributos) sin historial; bundle empaqueta refs y objetos Git y sirve como fuente de transferencia sin conexión. Bundles pueden ser incrementales y exigir prerrequisitos. Ninguno es copia completa de archivos no rastreados, ajustes locales o secretos; revise permisos de distribución.

## Práctica

Cree laboratorio aislado nuevo desde índice del módulo antes de cada práctica. Ejecute un comando por vez; pare ante resultado inesperado. Compruebe sandbox impreso y raíz antes de cambiar. Use Git 2.34+ como base de práctica; consulte ayuda y omita funciones opcionales no disponibles. No ejecute en repositorios de producción.

Escriba ambas salidas fuera del repo en sandbox nuevo. Verifique bundle, clone en otra carpeta propia, compare HEAD e inspeccione lista del archive con unzip si disponible. No publique artefactos automáticamente; bundle puede contener datos sensibles históricos.

```bash
git archive --format=zip -o "$sandbox/snapshot.zip" HEAD
git bundle create "$sandbox/history.bundle" main
git bundle verify "$sandbox/history.bundle"
git clone -b main "$sandbox/history.bundle" "$sandbox/recovered"
test "$(git rev-parse HEAD)" = "$(git -C "$sandbox/recovered" rev-parse HEAD)"
```

## Errores comunes y seguridad

Use solo laboratorio desechable y datos ficticios. Si estado difiere, pare; inspeccione estado y operación antes de abortar o recrear laboratorio. Cierre shell dedicado y elimine solo sandbox anotado mediante gestor de archivos tras revisar contenido.

## Ejercicio y autocorrección

¿Qué salida permite clon Git de la rama elegida? Bundle completo, no archive zip.

## Referencia rápida

- `git archive --format=zip -o "$sandbox/snapshot.zip" HEAD`
- `git bundle create "$sandbox/history.bundle" main`
- `git bundle verify "$sandbox/history.bundle"`
- `git clone -b main "$sandbox/history.bundle" "$sandbox/recovered"`

## Fuentes oficiales

- [https://git-scm.com/docs/git-archive](https://git-scm.com/docs/git-archive)
- [https://git-scm.com/docs/git-bundle](https://git-scm.com/docs/git-bundle)

---

<!-- navigation-footer -->
[Anterior](../09-blame-and-grep/README.es.md) · [Índice](../README.es.md) · [Siguiente](../11-integrated-advanced-lab/README.es.md)
<!-- /navigation-footer -->
