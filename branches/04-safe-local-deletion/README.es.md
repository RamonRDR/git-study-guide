# Borrado seguro de ramas locales

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../03-switch-safety-and-naming/README.es.md) · [Índice](../README.es.md) · [Siguiente](../05-detached-head/README.es.md)
<!-- /navigation -->

**Nivel:** principiante · **Tiempo estimado:** 25 min

**Requisitos previos:** [Cambio seguro y nombres de ramas](../03-switch-safety-and-naming/README.es.md)

**Objetivo:** Identificar commits alcanzables y borrar solo rama local ya contenida.

## Qué es y por qué

Borrar rama quita nombre, no inmediatamente todos objetos referenciados. Si commits no alcanzables desde refs supervivientes, limpieza futura puede volverlos irrecuperables. `git branch --merged main` lista ramas cuyas puntas son ancestros de main o main misma; `--no-merged main` lista otras. `git branch -d NAME` comprueba integración en upstream configurado, o HEAD si no existe; no siempre comprueba main. En lab no hay upstream. `-D` omite protección de integración y puede perder único acceso nombrado al trabajo; no ejecute. Rama activa en worktree no puede borrarse así. Compruebe alcance respecto a rama superviviente antes de quitar.

## Práctica

Continúe lab aislado en main con status limpio. archive/base aún C1; feat/note-revision y docs/overview tienen commits separados. Compruebe:

```text
git rev-parse --show-toplevel
git branch --show-current
git status --short
git branch --merged main
git branch --no-merged main
git log --oneline main..archive/base
git log --oneline main..feat/note-revision
```

Esperado: archive/base y main contenidas; feature y docs no. Primer rango vacío; segundo tiene commit. Borre SOLO archive/base tras confirmar contenida y no actual:

```text
git branch -d archive/base
git branch --list
git log -1 --oneline main
```

Nombre antiguo desaparece, C1 sigue en main. Ahora demuestre protección contra borrar trabajo no integrado; NO sustituya por -D:

```text
git branch -d feat/note-revision
```

Rechazo no cero esperado. Compruebe rama existente, commit distinto conservado y main sin cambio:

```text
git branch --list
git log --oneline main..feat/note-revision
git status --short
```

## Errores comunes y seguridad

No fuerce borrado aquí. Squash merge puede preservar contenido sin ancestralidad, así que fallo -d no prueba ausencia de trabajo en otro snapshot; compruebe historial/contenido, pida review y conserve rama si duda. Estrategias merge en módulo 05. Tracking y borrado remoto en 06; sin push en módulo.

## Ejercicio y autoevaluación

¿Qué rama puede quitarse en este lab concreto? Respuesta: archive/base, punta alcanzable desde main. Apruebe si feature sigue tras rechazo. Uso profesional: revisar integración, destino previsto y política antes de limpiar.

## Referencia rápida

`git branch --merged main`: puntas contenidas; `git branch --no-merged main`: otras puntas; `git branch -d NAME`: borrado local protegido.

## Fuentes oficiales

- [Git: git-branch](https://git-scm.com/docs/git-branch)
- [Git: git-log](https://git-scm.com/docs/git-log)
- [Git: gitrevisions](https://git-scm.com/docs/gitrevisions)
