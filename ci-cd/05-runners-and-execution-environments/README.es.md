# Runners y entornos de ejecución

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../04-gitlab-ci-cd/README.es.md) · [Índice](../README.es.md) · [Siguiente](../06-jobs-steps-stages-and-dependencies/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 35 min

**Requisitos previos:** [GitHub](../../github/README.es.md) · [GitLab](../../gitlab/README.es.md) · [Pipelines de GitLab CI/CD](../04-gitlab-ci-cd/README.es.md)

**Objetivo:** Elegir entorno acotado y diagnosticar problemas de planificación de runners.

## Qué es y por qué

Runner es agente que ejecuta jobs, no rama ni repositorio. GitHub-hosted ofrece entornos gestionados; self-hosted lo controla operador. Runners GitLab usan ejecutores como shell o Docker, y ámbito/tags afectan elegibilidad. Executor shell comparte host más directamente; contenedor no ofrece automáticamente frontera de seguridad suficiente. Prefiera runners desechables aislados con mínimo privilegio y sin acceso a redes internas sensibles para cambios no confiables. SO, shell, arquitectura, herramientas, imagen y versión influyen. Matriz expande combinaciones, como Linux y Windows, en jobs separados. Jobs pueden correr en máquinas distintas; no suponga archivos o procesos compartidos.

## Práctica

Escenario sin conexión: Linux pasa, Windows falla por ruta específica de shell y tercer job queda pendiente por falta de runner elegible. Identifique correcciones distintas: rutas portables o shell explícito, y diagnóstico de planificación/configuración. Lea [automatización de calidad](../../docs/quality-automation.es.md) del guía para ejemplo real de dos SO, sin modificarlo.

## Errores comunes y seguridad

Nunca registre runner en máquina personal o de empresa para esta lección, ejecute Docker privilegiado ni exponga credenciales. Cómputo alojado puede tener cuotas y costes; no se necesita ejecución alojada. Compruebe disponibilidad, labels/tags y límites; no eluda aislamiento.

## Ejercicio y autoevaluación

Apruebe si pendiente no se interpreta como test fallido, fallo Windows no se ignora y no propone runner compartido sensible.

## Referencia rápida

runner / executor / matrix

## Fuentes oficiales

- <https://docs.github.com/en/actions/concepts/runners/github-hosted-runners>
- <https://docs.gitlab.com/runner/executors/>
- <https://docs.gitlab.com/ci/runners/>

---

<!-- navigation-footer -->
[Anterior](../04-gitlab-ci-cd/README.es.md) · [Índice](../README.es.md) · [Siguiente](../06-jobs-steps-stages-and-dependencies/README.es.md)
<!-- /navigation-footer -->
