# Hooks: automatización local y confianza

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../04-subtree/README.es.md) · [Índice](../README.es.md) · [Siguiente](../06-rerere/README.es.md)
<!-- /navigation -->

**Nivel:** avanzado · **Tiempo estimado:** 40 min

**Requisitos:** [13 Git avanzado](../README.es.md) · [Seguridad y gobernanza](../../security/README.es.md)

**Objetivo:** Hooks son programas invocados en eventos de Git, como pre-commit.

## Qué es y por qué

Hooks son programas invocados en eventos de Git, como pre-commit. Resultado distinto de cero en pre-commit aborta el commit. Hooks normalmente no se copian al clonar; core.hooksPath cambia ubicación. Checks locales mejoran feedback, pero no sustituyen checks obligatorios del servidor. Nunca ejecute hooks de origen no confiable.

## Práctica

Cree laboratorio aislado nuevo desde índice del módulo antes de cada práctica. Ejecute un comando por vez; pare ante resultado inesperado. Compruebe sandbox impreso y raíz antes de cambiar. Use Git 2.34+ como base de práctica; consulte ayuda y omita funciones opcionales no disponibles. No ejecute en repositorios de producción.

En laboratorio nuevo, cree hook propio inocuo que siempre rechaza commit, solo en carpeta hermana nueva. `chmod` aplica a Bash con scripts ejecutables. Compruebe HEAD intacto y contenido preparado tras rechazo; si ejecución no se admite, pare. Quite solo configuración local del laboratorio después; nunca eluda checks de proyecto real.

```bash
mkdir "$sandbox/hooks"
printf '%s\n' '#!/bin/sh' 'exit 1' > "$sandbox/hooks/pre-commit"
chmod +x "$sandbox/hooks/pre-commit"
git config --local core.hooksPath "$sandbox/hooks"
before=$(git rev-parse HEAD)
printf '%s\n' 'review' > docs/review.txt
git add -- docs/review.txt
git commit -m "docs: hook practice"
test "$(git rev-parse HEAD)" = "$before"
git diff --cached --name-only
git config --local --unset core.hooksPath
```

## Errores comunes y seguridad

Use solo laboratorio desechable y datos ficticios. Si estado difiere, pare; inspeccione estado y operación antes de abortar o recrear laboratorio. Cierre shell dedicado y elimine solo sandbox anotado mediante gestor de archivos tras revisar contenido.

## Ejercicio y autocorrección

¿Por qué CI debe exigir un check de forma independiente? Hooks son locales, configurables y no son frontera fiable de cumplimiento.

## Referencia rápida

- `git config --local core.hooksPath "<sandbox>/hooks"`
- `git add -- docs/review.txt`
- `git commit -m "docs: hook practice"`
- `git diff --cached --name-only`

## Fuentes oficiales

- [https://git-scm.com/docs/githooks](https://git-scm.com/docs/githooks)
- [https://git-scm.com/docs/git-config](https://git-scm.com/docs/git-config)

---

<!-- navigation-footer -->
[Anterior](../04-subtree/README.es.md) · [Índice](../README.es.md) · [Siguiente](../06-rerere/README.es.md)
<!-- /navigation-footer -->
