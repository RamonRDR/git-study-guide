# Blame y grep: investigar cambios

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../08-partial-and-shallow-clone/README.es.md) · [Índice](../README.es.md) · [Siguiente](../10-archive-and-bundle/README.es.md)
<!-- /navigation -->

**Nivel:** avanzado · **Tiempo estimado:** 35 min

**Requisitos:** [13 Git avanzado](../README.es.md) · [Seguridad y gobernanza](../../security/README.es.md)

**Objetivo:** Blame atribuye líneas seleccionadas a commits según historial y opciones; no mide responsabilidad ni calidad.

## Qué es y por qué

Blame atribuye líneas seleccionadas a commits según historial y opciones; no mide responsabilidad ni calidad. Grep busca archivos rastreados de trabajo por defecto o tree nombrado con revisión. Combine con show/log para comprender contexto de revisión, no culpar al autor.

## Práctica

Cree laboratorio aislado nuevo desde índice del módulo antes de cada práctica. Ejecute un comando por vez; pare ante resultado inesperado. Compruebe sandbox impreso y raíz antes de cambiar. Use Git 2.34+ como base de práctica; consulte ayuda y omita funciones opcionales no disponibles. No ejecute en repositorios de producción.

Compare búsqueda en HEAD y su padre. grep retorna 1 sin coincidencia; no es necesariamente error de investigación. `git blame` debe identificar cambio de la línea de estado. Evite buscar o publicar datos privados; mantenga salida ficticia.

```bash
git blame -- src/state.txt
git grep -n bad HEAD -- src
git grep -n ok HEAD~1 -- src
git log -p -- src/state.txt
```

## Errores comunes y seguridad

Use solo laboratorio desechable y datos ficticios. Si estado difiere, pare; inspeccione estado y operación antes de abortar o recrear laboratorio. Cierre shell dedicado y elimine solo sandbox anotado mediante gestor de archivos tras revisar contenido.

## Ejercicio y autocorrección

¿Por qué inspeccionar commit tras blame? Atribución de línea sola no explica intención ni contexto.

## Referencia rápida

- `git blame -- src/state.txt`
- `git grep -n bad HEAD -- src`
- `git grep -n ok HEAD~1 -- src`
- `git log -p -- src/state.txt`

## Fuentes oficiales

- [https://git-scm.com/docs/git-blame](https://git-scm.com/docs/git-blame)
- [https://git-scm.com/docs/git-grep](https://git-scm.com/docs/git-grep)
- [https://git-scm.com/docs/git-log](https://git-scm.com/docs/git-log)

---

<!-- navigation-footer -->
[Anterior](../08-partial-and-shallow-clone/README.es.md) · [Índice](../README.es.md) · [Siguiente](../10-archive-and-bundle/README.es.md)
<!-- /navigation-footer -->
