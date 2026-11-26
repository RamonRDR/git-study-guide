# Seguridad y recuperación antes de integrar

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
— · [Índice](../README.es.md) · [Siguiente](../02-fast-forward/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 25 min

**Requisitos previos:** [Gestión de ramas](../../branches/README.es.md) · [Configuración aislada del lab](../../getting-started/03-first-repository/README.es.md) · [Primer commit](../../getting-started/05-first-commit/README.es.md)

**Objetivo:** Identificar operación, requisitos y salida segura antes de combinar historiales.

## Qué es y por qué

Integración combina cambios de líneas de historial distintas. Merge puede avanzar rama o crear commit con múltiples padres. Squash prepara contenido combinado sin registrar ascendencia de origen. Rebase reaplica commits sobre otra base y normalmente produce IDs nuevos. Conflicto ocurre cuando Git no puede decidir resultado combinado con seguridad. Estado inicial limpio, refs conocidas, identidad ficticia y referencias locales de respaldo facilitan inspección. Ninguna operación envía cambios a servidor.

## Práctica

Cree NUEVO lab desechable aislado según módulo 00 capítulo 03 y lección de primer commit. Mantenga shell dedicado original, no terminal del editor. Main inicial debe tener exactamente un commit, note.txt = practice, estado limpio. Cierre shell del lab anterior antes de empezar. Siga verificaciones del capítulo 01 antes de cada operación que cambia historial.

```text
git rev-parse --show-toplevel
git branch --show-current
git status --short
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Deténgase si raíz no es lab desechable, rama actual no es la indicada, estado no está limpio antes de iniciar operación o identidades no empiezan con `Study Guide Example <learner@example.invalid>`. Antes de cada commit compruebe también diff preparado; deténgase ante salida inesperada.

```text
git log --oneline --all --graph --decorate
git branch --list
git remote -v
```

Antes de rebase, cree rama separada en punta original (p. ej. backup/feature). Conserva ref nombrada de trabajo registrado, no archivos sin commit ni respaldo externo. Cuando merge normal se detiene por conflicto, compruebe status; `git merge --abort` intenta restaurar estado previo. Cuando rebase se detiene, `git rebase --abort` vuelve a rama/estado original; `git rebase --continue` reanuda tras resolver. Use abort de operación en curso. Empiece limpio; abort no garantiza reconstrucción de cambios previos sin commit. `git merge --squash` no crea MERGE_HEAD, así que abort de merge normal no es undo general del squash. Si falla lab squash, deténgase y descarte solo ese lab tras comprobar ubicación. Recuperación de operaciones completas más adelante.

## Errores comunes y seguridad

Nunca haga rebase de historial compartido/publicado en ejercicios; nunca force push, reset hard ni ejecute contra guía. Abort no deshace operación completa. Ante estado inesperado, deténgase e inspeccione en vez de apilar comandos.

Tras cada lab independiente, cierre editor y shell dedicado, luego borre solo carpeta padre temporal exacta anotada en módulo 00 mediante gestor si no necesita. Nunca borre guía, carpeta personal o repo laboral.

## Ejercicio y autoevaluación

Elija paso seguro en merge conflictivo: status, luego merge --abort o resolver y continuar. Para rebase, rebase --abort/--continue. Apruebe si explica por qué inicio limpio y ref respaldo importan. Uso profesional: acordar política antes de tocar historial compartido.

## Referencia rápida

- `git status`
- `git merge --abort`
- `git rebase --abort`
- `git rebase --continue`

## Fuentes oficiales

- [Git: git-merge](https://git-scm.com/docs/git-merge)
- [Git: git-rebase](https://git-scm.com/docs/git-rebase)
- [Git: git-status](https://git-scm.com/docs/git-status)
- [Git: git-branch](https://git-scm.com/docs/git-branch)
