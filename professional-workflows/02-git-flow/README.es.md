# Git Flow

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../01-feature-branch-workflow/README.es.md) · [Índice](../README.es.md) · [Siguiente](../03-github-flow/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 40 min

**Requisitos previos:** [CI/CD](../../ci-cd/README.es.md) · [Flujo con ramas de funcionalidad](../01-feature-branch-workflow/README.es.md)

**Objetivo:** Explicar caminos de release/hotfix y sus costes.

## Qué es y por qué

Git Flow es convención orientada a releases programadas. En modelo clásico, `main` mantiene historial publicado, `develop` acumula trabajo futuro, features salen y vuelven a develop, ramas de release preparan lanzamiento y hotfixes tratan correcciones urgentes desde main. Release integra en main y cambios regresan a develop; commit de release recibe tag. Hotfixes también deben llegar a línea de desarrollo y release activa relevante según política. Nombres y métodos exactos son convenciones de equipo, no requisitos Git. Puede apoyar versiones mantenidas en paralelo o ventanas controladas, pero refs duraderas aumentan coste de sincronización, conflictos y review.

```text
feature -> develop -> release preparation -> main/tag
hotfix from affected release -> corrected release + compatible propagation
```

## Práctica

Dibuje release 2.0.0 del catálogo en estabilización mientras develop contiene trabajo 2.1. Bug crítico aparece en 1.9 publicada. Decida dónde iniciar hotfix (revisión real 1.9 de producción o línea mantenida), pruebe, etiquete release corregida y propague corrección compatible a demás líneas relevantes. En modelo clásico con main en 1.9, dibuje hotfix -> main y hotfix -> develop; considere release activa también.

## Riesgos y recuperación

No suponga main siempre igual a producción desplegada; compruebe identificador de release. Nunca sobrescriba tags publicados ni integre features futuras ajenas en hotfix. Si backport genera conflictos, resuelva y pruebe por separado cada línea mantenida. Evite Git Flow cuando ramas extra generan coste sin necesidad de release.

## Ejercicio y autoevaluación

Hotfix comienza en revisión mantenida afectada, no en develop arbitraria. Registre tag de release probada y caminos compatibles de propagación.

## Referencia rápida

main / develop / feature / release / hotfix

## Fuentes

- <https://nvie.com/posts/a-successful-git-branching-model/>
- <https://www.atlassian.com/git/tutorials/comparing-workflows>
- <https://git-scm.com/docs/gitworkflows>
