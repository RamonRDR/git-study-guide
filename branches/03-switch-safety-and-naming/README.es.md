# Cambio seguro y nombres de ramas

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../02-start-points-and-comparison/README.es.md) · [Índice](../README.es.md) · [Siguiente](../04-safe-local-deletion/README.es.md)
<!-- /navigation -->

**Nivel:** principiante · **Tiempo estimado:** 25 min

**Requisitos previos:** [Puntos de partida y comparación de ramas](../02-start-points-and-comparison/README.es.md)

**Objetivo:** Reconocer cambio bloqueado y renombrar rama sin perder commits.

## Qué es y por qué

Git puede conservar ediciones locales compatibles al cambiar; normalmente rechaza cambio que sobrescribiría ediciones conflictivas o archivos no rastreados que estorban. Working tree e index no son privados por rama en un checkout. `git branch -m NEW` renombra actual; `git branch -m OLD NEW` renombra otra local. Conserva referencia y mueve config/reflog asociados si existen. Reflog registra movimientos locales de refs; detalles después. Nombres feat/note, fix/typo y docs/overview comunican intención; convenciones no son requisitos Git. `git check-ref-format --branch NAME` valida sintaxis (no disponibilidad). Evite espacios, secuencias reservadas y diferencias solo de mayúsculas por portabilidad.

## Práctica

En mismo lab, comience docs/overview con status limpio. Cambie a feat/note, anote ID, renombre y compruebe ID:

```text
git status --short
git switch feat/note
git rev-parse HEAD
git check-ref-format --branch feat/note-revision
git branch -m feat/note-revision
git branch --show-current
git rev-parse HEAD
git branch --list
```

Esperado: mismo ID, nombre nuevo feat/note-revision, nombre antiguo ausente. Edite note.txt de feature a unfinished y guarde sin preparar. Compruebe, luego intente cambio intencional en lab desechable:

```text
git status --short
git diff -- note.txt
git switch main
```

Rechazo esperado: main contiene practice, así que cambio sobrescribiría note editado. Confirme aún en feat/note-revision y contenido unfinished. Si cambio funciona inesperadamente, deténgase e inspeccione; nunca fuerce. Para continuar, cambie manualmente SOLO note.txt ficticio a feature con salto original (descarte intencional de edición de prueba, no trabajo real). Compruebe status limpio, luego cambie:

```text
git branch --show-current
git status --short
```

Solo tras status vacío:

```text
git switch main
git show HEAD:note.txt
git status --short
```

## Errores comunes y seguridad

No use switch --discard-changes ni branch -M aquí. No borre ediciones reales para cambiar. Consérvelas en commit intencional en rama adecuada o técnica de recuperación revisada después. No renombre rama compartida sin coordinar; renombre/tracking remoto queda para módulo 06.

## Ejercicio y autoevaluación

¿Por qué falló switch? Respuesta: sobrescribiría edición local rastreada. ¿Renombre crea commit? No. Apruebe si nombre e ID comprobados y ninguna edición perdida involuntariamente. Uso profesional: acordar nombres portables y descriptivos.

## Referencia rápida

`git branch -m OLD NEW`: renombrar; `git check-ref-format --branch NAME`: sintaxis; `git status --short`: comprobar antes de cambiar.

## Fuentes oficiales

- [Git: git-switch](https://git-scm.com/docs/git-switch)
- [Git: git-branch](https://git-scm.com/docs/git-branch)
- [Git: git-check-ref-format](https://git-scm.com/docs/git-check-ref-format)
