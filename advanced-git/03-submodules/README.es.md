# Submodules: dependencias fijadas por commit

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../02-worktree/README.es.md) · [Índice](../README.es.md) · [Siguiente](../04-subtree/README.es.md)
<!-- /navigation -->

**Nivel:** avanzado · **Tiempo estimado:** 45 min

**Requisitos:** [13 Git avanzado](../README.es.md) · [Seguridad y gobernanza](../../security/README.es.md)

**Objetivo:** El superproyecto registra gitlink (modo 160000) hacia un commit específico de otro repositorio; .gitmodules registra ruta y URL.

## Qué es y por qué

El superproyecto registra gitlink (modo 160000) hacia un commit específico de otro repositorio; .gitmodules registra ruta y URL. Actualizar dependencia exige commit del nuevo gitlink en el padre. Checkout del submódulo suele quedar en detached HEAD. Use para historiales separados y revisiones fijadas; evite si bastan archivos normales.

## Práctica

Cree laboratorio aislado nuevo desde índice del módulo antes de cada práctica. Ejecute un comando por vez; pare ante resultado inesperado. Compruebe sandbox impreso y raíz antes de cambiar. Use Git 2.34+ como base de práctica; consulte ayuda y omita funciones opcionales no disponibles. No ejecute en repositorios de producción.

Clone solo el laboratorio propio en carpeta hermana local y añádalo como submódulo. Permiso file limitado al comando es solo para este laboratorio local conocido, nunca ajuste global. Inspeccione .gitmodules preparado y modo 160000. Antes de registrar dependencia real, revise URL, licencia y commit; no inicialice recursivamente repositorios desconocidos.

```bash
git clone --no-hardlinks . "$sandbox/library"
git -c protocol.file.allow=always submodule add "$sandbox/library" vendor/library
git diff --cached -- .gitmodules
git ls-files --stage -- vendor/library
git submodule status
```

## Errores comunes y seguridad

Use solo laboratorio desechable y datos ficticios. Si estado difiere, pare; inspeccione estado y operación antes de abortar o recrear laboratorio. Cierre shell dedicado y elimine solo sandbox anotado mediante gestor de archivos tras revisar contenido.

## Ejercicio y autocorrección

¿Qué guarda el padre? ID de commit, no copia de todos los archivos hijos. Un clon nuevo requiere inicialización/actualización explícita.

## Referencia rápida

- `git clone --no-hardlinks . "$sandbox/library"`
- `git -c protocol.file.allow=always submodule add "$sandbox/library" vendor/library`
- `git diff --cached -- .gitmodules`
- `git ls-files --stage -- vendor/library`

## Fuentes oficiales

- [https://git-scm.com/docs/git-submodule](https://git-scm.com/docs/git-submodule)
- [https://git-scm.com/docs/gitsubmodules](https://git-scm.com/docs/gitsubmodules)

---

<!-- navigation-footer -->
[Anterior](../02-worktree/README.es.md) · [Índice](../README.es.md) · [Siguiente](../04-subtree/README.es.md)
<!-- /navigation-footer -->
