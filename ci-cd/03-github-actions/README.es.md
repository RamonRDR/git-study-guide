# Workflows de GitHub Actions

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../02-yaml-fundamentals/README.es.md) · [Índice](../README.es.md) · [Siguiente](../04-gitlab-ci-cd/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 45 min

**Requisitos previos:** [GitHub](../../github/README.es.md) · [GitLab](../../gitlab/README.es.md) · [YAML y lectura de configuración](../02-yaml-fundamentals/README.es.md)

**Objetivo:** Explicar eventos, workflow, jobs, steps y permisos mínimos con ejemplo de inspección.

## Qué es y por qué

GitHub descubre archivos de workflow en `.github/workflows/`. Evento selecciona ejecución; job corre en runner y steps ejecutan en secuencia. `uses` invoca action; `run` invoca comando shell. En pull_request, checkout predeterminado normalmente prueba ref de merge generada; en push, revisión enviada. Inspeccione checkout y evento reales. `permissions: contents: read` minimiza concesión de token predeterminado; deshabilitar persistencia de credenciales de checkout reduce exposición posterior. Fije actions propias y de terceros a SHA completos verificados, revise actualizaciones y no trate fijación como garantía de seguridad.

Ejemplo abajo es configuración didáctica completa para catálogo ficticio; SHA de checkout proviene del workflow revisado del guía, no versión inventada. Verifique revisión de action antes de reutilizar. No usa despliegue ni secretos del usuario.

```yaml
name: Sandbox quality
on:
  pull_request:
    branches: [main]
  push:
    branches: [main]
permissions:
  contents: read
jobs:
  quality:
    runs-on: ubuntu-latest
    timeout-minutes: 5
    steps:
      - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1
        with:
          persist-credentials: false
      - name: Check catalog
        shell: bash
        run: |
          test -s catalog.txt
          grep -Fxq 'status: ready' catalog.txt
```

## Práctica

Lea YAML sin instalarlo. En laboratorio sin conexión del capítulo 10, ejecute dos comprobaciones contra su archivo de catálogo temporal. Prediga éxito con línea ready exacta y fallo en archivo vacío o incorrecto. Uso alojado opcional: solo en sandbox desechable propio tras revisar código, disponibilidad de runner, cuotas y permisos; no use guía ni habilite uso pago. No se necesita ejecución alojada.

## Errores comunes y seguridad

Nunca ejecute código de PR no confiable en workflow `pull_request_target` privilegiado. No interpole texto no confiable de evento en scripts shell. Step fallido exige inspeccionar logs; corrija fuente y repita checks en nueva revisión, no ejecución exitosa ajena.

## Ejercicio y autoevaluación

Apruebe si nombra ambos eventos, identifica runner/job/steps, explica permisos del token y predice resultados.

## Referencia rápida

`on` / `jobs` / `steps` / `permissions`

## Fuentes oficiales

- <https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax>
- <https://docs.github.com/en/actions/reference/security/secure-use>
- <https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows>
