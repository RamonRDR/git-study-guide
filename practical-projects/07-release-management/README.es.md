# Gestión de lanzamientos

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../06-automated-quality-pipeline/README.es.md) · [Índice](../README.es.md) · [Siguiente](../08-professional-engineering-workflow/README.es.md)
<!-- /navigation -->

**Nivel:** avanzado · **Tiempo estimado:** 60 min

**Prerrequisitos:** [professional-workflows/12-release-management](../../professional-workflows/12-release-management/README.es.md) · Git 2.40+ · Bash/Git Bash · tar

**Objetivo:** Confirma y etiqueta versión 1.0.0, añade ready sin quitar draft, revisa y etiqueta 1.1.0, luego prepara archivo de código de instantánea etiquetada. Haz cambio posterior y demuestra que etiqueta sigue apuntando al commit anterior.

## Escenario

Catálogo ficticio de texto declara contrato público de estado. Lanzamiento inicial admite draft; ejemplo adicional ready retrocompatible motiva lanzamiento minor. Etiquetas anotadas locales identifican revisiones exactas; no se publica lanzamiento de plataforma.

## Preparación desechable

Usa solo la sección Preparación desechable de [Mi primer repositorio](../01-my-first-repository/README.es.md). Abre shell Bash/Git Bash dedicada nueva; comprueba raíz impresa, identidades ficticias y ausencia de remotos antes de seguir. No ejecutes desafío 01. Git 2.40+. Ejecuta un comando a la vez, detente ante fallo inesperado y nunca ejecutes en el guía.

## Desafío

Confirma y etiqueta versión 1.0.0, añade ready sin quitar draft, revisa y etiqueta 1.1.0, luego prepara archivo de código de instantánea etiquetada. Haz cambio posterior y demuestra que etiqueta sigue apuntando al commit anterior. Intenta antes de leer la solución.

## Pistas progresivas

SemVer minor significa funcionalidad pública retrocompatible bajo contrato declarado, no cantidad de ediciones. Etiquetas anotadas son objetos resolubles a commits; usa git archive para contenido de instantánea e inspecciona archivo.

## Solución de referencia

Confirma dos versiones con notas explícitas en mensajes de etiquetas. Comprueba conservación de funcionalidad draft existente.

```bash
printf '%s\n' 'status: draft' > catalog.txt
git add catalog.txt
git commit -m 'docs: initialize catalog'
git tag -a v1.0.0 -m 'Initial draft contract'
printf '%s\n' 'status: draft' 'status: ready' > catalog.txt
git add catalog.txt
git diff --cached --check
git diff --cached
git commit -m 'feat: add ready status'
git tag -a v1.1.0 -m 'Add backward-compatible ready status'
released=$(git rev-parse 'v1.1.0^{commit}')
git cat-file -t v1.1.0
git archive --format=tar --output="$sandbox/catalog-v1.1.0.tar" v1.1.0
tar -tf "$sandbox/catalog-v1.1.0.tar"
tar -xOf "$sandbox/catalog-v1.1.0.tar" catalog.txt
```

Avanza main local con cambio futuro separado; demuestra etiqueta inmutable por convención, no protegida automáticamente por Git local.

```bash
printf '%s\n' 'future work' > future.txt
git add future.txt
git commit -m 'docs: begin future work'
test "$(git rev-parse 'v1.1.0^{commit}')" = "$released"
test "$(git rev-parse HEAD)" != "$released"
git show v1.0.0:catalog.txt
git show v1.1.0:catalog.txt
git status --porcelain
```

## Criterios de éxito

Ambas etiquetas anotadas; v1.1.0 conserva draft y añade ready, y tar contiene solo catalog.txt con contenido exacto, sin .git o future.txt. Etiqueta no se mueve cuando main avanza. Explica por qué no es lanzamiento publicado en plataforma.

Prueba fija de mantenimiento (no código de estudiante): `tests/test_git_practical_projects.py::test_release_management`.

## Recuperación y limpieza

Comprueba versiones y destinos antes de etiquetar. No sobrescribas etiqueta publicada; usa política de corrección de lanzamiento. Borrador alojado opcional solo en repositorio propio autorizado con etiqueta existente verificada y sin requisito de pago. Cierra la shell dedicada y elimina solo el sandbox impreso verificado mediante gestor de archivos. Conserva antes trabajo deseado.

## Fuentes oficiales

- <https://git-scm.com/docs/git-tag>
- <https://git-scm.com/docs/git-archive>
- <https://git-scm.com/docs/git-show>
- <https://semver.org/spec/v2.0.0.html>

---

<!-- navigation-footer -->
[Anterior](../06-automated-quality-pipeline/README.es.md) · [Índice](../README.es.md) · [Siguiente](../08-professional-engineering-workflow/README.es.md)
<!-- /navigation-footer -->
