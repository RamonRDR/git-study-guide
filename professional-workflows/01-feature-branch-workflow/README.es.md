# Flujo con ramas de funcionalidad

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
— · [Índice](../README.es.md) · [Siguiente](../02-git-flow/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 35 min

**Requisitos previos:** [CI/CD](../../ci-cd/README.es.md)

**Objetivo:** Explicar estado de rama de funcionalidad e integración revisada.

## Qué es y por qué

Rama de funcionalidad es línea temporal creada desde base de integración prevista. Commits avanzan su ref sin avanzar main. Pull request (PR) o merge request (MR) es función de alojamiento que propone integración; Git conoce refs y commits, no aprobaciones de review. Mantenga cambios pequeños, comprobables de forma independiente y ligados a requisito. Obtenga e inspeccione destino antes de integrar; actualice rama según política de equipo. Squash merge crea commit combinado nuevo en vez de preservar cada commit de rama; merge normal puede conservar ambos historiales. Elija método conscientemente.

```text
base main -> feature branch -> review -> authorized integration
```

## Práctica

Catálogo ficticio de biblioteca necesita campo de disponibilidad y corrección ortográfica aparte. Dibuje dos ramas desde main, cada una con propósito. Para rama de disponibilidad, prediga `git switch -c feat/ready-catalog`, commit, vuelta a main e integración. Use laboratorio local del capítulo 13 para observar estados; PR alojado es opcional.

## Riesgos y recuperación

Evite agrupar cambios ajenos o mantener rama abierta semanas sin razón. Inspeccione divergencia y resuelva conflictos en rama propia; aborte merge no resuelto en vez de adivinar. No force-push en ramas compartidas ni eluda review obligatorio. Elimine ramas solo tras comprobar integración y retención.

## Ejercicio y autoevaluación

Dos ramas mantienen correcciones independientes. Main no cambia hasta integración. Identifique qué ref avanza y distinga propuesta de review de commit Git.

## Referencia rápida

`git switch -c` / `git diff` / PR / MR

## Fuentes

- <https://git-scm.com/docs/gitworkflows>
- <https://git-scm.com/docs/git-branch>
- <https://git-scm.com/docs/git-merge>
