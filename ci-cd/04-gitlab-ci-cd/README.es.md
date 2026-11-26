# Pipelines de GitLab CI/CD

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../03-github-actions/README.es.md) · [Índice](../README.es.md) · [Siguiente](../05-runners-and-execution-environments/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 45 min

**Requisitos previos:** [GitHub](../../github/README.es.md) · [GitLab](../../gitlab/README.es.md) · [Workflows de GitHub Actions](../03-github-actions/README.es.md)

**Objetivo:** Leer pipeline GitLab y mapear conceptos a GitHub Actions sin confundir sintaxis.

## Qué es y por qué

GitLab normalmente lee `.gitlab-ci.yml` en raíz. `workflow: rules` determina creación de pipeline; `rules` de job puede decidir inclusión individual. Stages ordenan grupos de jobs por defecto; job tiene `script` de comandos. Executor del runner define entorno real. `image` se usa por ejecutores de contenedor compatibles, no todos. Ejemplo requiere runner Linux aislado compatible con contenedor, Alpine y herramientas shell BusyBox. GitLab normalmente hace checkout de revisión antes de script. Ejemplo usa etiqueta de versión legible deliberadamente; etiquetas de imagen son mutables, por lo que política de producción debe verificar y fijar digest confiable. Jobs GitLab reciben credenciales automáticas de job incluso sin secretos definidos por usuario; restrinja acceso del job token y ámbito de runner según corresponda.

```yaml
workflow:
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
    - if: '$CI_PIPELINE_SOURCE == "push" && $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH'
stages:
  - test
quality:
  stage: test
  image: alpine:3.22
  timeout: 5m
  script:
    - test -s catalog.txt
    - "grep -Fxq 'status: ready' catalog.txt"
```

## Práctica

Sin conexión, rastree evento MR, push a rama predeterminada y push a otra rama sin MR. Configuración crea pipelines en los dos primeros, no tercero. Compare checks con capítulo 03 y haga mismo laboratorio sin conexión del capítulo 10. Opcional: CI Lint puede validar configuración en proyecto desechable autorizado sin ejecutar jobs; compruebe permisos y cuota gratuita disponible antes de operación alojada. No exige registrar runner ni uso pago.

## Errores comunes y seguridad

No ejecute pipelines de MR de fork en proyecto padre privilegiado con secretos o recursos protegidos. Revise cambios en `.gitlab-ci.yml`, includes y acceso de token. Si no aparece pipeline, inspeccione origen, workflow rules y validez antes de cambiar acceso o repetir.

## Ejercicio y autoevaluación

Apruebe si distingue workflow rules, stages, jobs, scripts y executor; explique credenciales automáticas y por qué YAML no es intercambiable.

## Referencia rápida

`workflow` / `rules` / `stages` / `script`

## Fuentes oficiales

- <https://docs.gitlab.com/ci/yaml/>
- <https://docs.gitlab.com/ci/yaml/lint/>
- <https://docs.gitlab.com/ci/pipelines/merge_request_pipelines/>
- <https://docs.gitlab.com/ci/jobs/ci_job_token/>

---

<!-- navigation-footer -->
[Anterior](../03-github-actions/README.es.md) · [Índice](../README.es.md) · [Siguiente](../05-runners-and-execution-environments/README.es.md)
<!-- /navigation-footer -->
