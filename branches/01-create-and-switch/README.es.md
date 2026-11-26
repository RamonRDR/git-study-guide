# Crear y cambiar ramas locales

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Módulo anterior](../../basic-commands/README.es.md) · [Índice](../README.es.md) · [Siguiente](../02-start-points-and-comparison/README.es.md)
<!-- /navigation -->

**Nivel:** principiante · **Tiempo estimado:** 35 min

**Requisitos previos:** [Configuración aislada del lab](../../getting-started/03-first-repository/README.es.md) · [Primer commit](../../getting-started/05-first-commit/README.es.md) · [Comandos básicos](../../basic-commands/README.es.md)

**Objetivo:** Crear referencias de rama y comprobar cuál selecciona HEAD.

## Qué es y por qué

Una rama local es referencia móvil a commit, no segunda carpeta ni copia completa. Crear rama en HEAD añade referencia sin cambiar index o working tree. Cambiar selecciona rama destino y actualiza archivos rastreados/index según necesidad. Commit normalmente avanza solo rama activa. `git branch NAME [START]` crea sin cambiar; `git switch NAME` cambia; `git switch -c NAME [START]` crea y cambia. Switch apareció en Git 2.23; lab exige 2.40+ del módulo 00. Tutoriales antiguos usan checkout para cambio y otras operaciones; guía prefiere switch por claridad.

## Práctica

Inicie NUEVO repo desechable con configuración aislada del módulo 00 capítulo 03 y primer commit del capítulo 05. No use repo del guía. Mantenga shell dedicado hasta fin del módulo. Esperado exactamente un commit en main con note.txt que contiene practice y status limpio. Compruebe raíz, status e identidades antes de continuar.

```text
git rev-parse --show-toplevel
git status --short
git log --oneline
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Si raíz no es lab, status no limpio o identidad no ficticia, deténgase. Si correcto ejecute:

```text
git branch feat/note
git branch --list
git symbolic-ref HEAD
git rev-parse main feat/note
git switch feat/note
git branch --show-current
git status --short
```

Al inicio IDs iguales y HEAD refs/heads/main; tras switch HEAD nombra feat/note. Archivo aún contiene practice. Diagrama textual: HEAD -> feat/note -> C1; main -> C1. Ambos nombres apuntan C1. Edite note.txt a feature (una línea, salto final), guarde y prepare solo archivo:

```text
git add -- note.txt
git diff --cached -- note.txt
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Solo si cambio preparado y ambas identidades correctas:

```text
git commit -m "docs: revise feature note"
git log --oneline --all --graph --decorate
git switch main
git show HEAD:note.txt
git status --short
git switch feat/note
git show HEAD:note.txt
```

Esperado: main aún C1 con practice; feat/note C2 con feature. Diagrama: main -> C1; HEAD -> feat/note -> C2 -> C1 (última flecha es historial de padres). Cambiar no es fusionar.

## Errores comunes y seguridad

Compruebe status antes de cambiar; ediciones sin registrar compatibles pueden acompañar cambio, conflictivas pueden bloquearlo. No use fuerza/descarte. No cree ramas desde HEAD indeseado. No hay remoto en lab.

## Ejercicio y autoevaluación

Prediga commit de main tras commit de feature. Respuesta: sin cambio. Apruebe si branch --show-current y versiones coinciden. Uso profesional: aislar cambio pequeño antes de review.

## Referencia rápida

`git branch NAME [START]`: crear; `git switch NAME`: seleccionar; `git switch -c NAME [START]`: crear y seleccionar; `git branch --show-current`: rama activa.

## Fuentes oficiales

- [Git: git-branch](https://git-scm.com/docs/git-branch)
- [Git: git-switch](https://git-scm.com/docs/git-switch)
- [Git: git-symbolic-ref](https://git-scm.com/docs/git-symbolic-ref)

---

<!-- navigation-footer -->
[Módulo anterior](../../basic-commands/README.es.md) · [Índice](../README.es.md) · [Siguiente](../02-start-points-and-comparison/README.es.md)
<!-- /navigation-footer -->
