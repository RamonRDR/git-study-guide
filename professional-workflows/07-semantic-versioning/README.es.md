# Versionado semántico

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../06-conventional-commits/README.es.md) · [Índice](../README.es.md) · [Siguiente](../08-code-review/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 35 min

**Requisitos previos:** [CI/CD](../../ci-cd/README.es.md) · [Conventional Commits](../06-conventional-commits/README.es.md)

**Objetivo:** Elegir versión compatible e interpretar precedencia.

## Qué es y por qué

SemVer 2.0.0 describe versiones según API pública declarada (contrato usado por consumidores, no necesariamente API HTTP). Para versiones estables, incremente MAJOR por cambios incompatibles, MINOR por funcionalidad retrocompatible y PATCH por correcciones retrocompatibles; reinicie componentes inferiores al aumentar superior. Major cero es desarrollo inicial con API inestable. Pre-release `2.0.0-rc.1` tiene menor precedencia que versión normal correspondiente; metadatos tras `+` no afectan precedencia. Contenido de versión publicada no debe modificarse. Tag Git `v1.4.2` puede nombrar commit de versión SemVer `1.4.2`; prefijo es convención de tag, no parte de cadena SemVer.

## Práctica

Desde API 1.4.2 de catálogo, elija siguiente versión para cada escenario independiente: corregir error sin cambiar API; añadir campo opcional retrocompatible; retirar campo obligatorio de respuesta. Compare `2.0.0-rc.1` con `2.0.0` y `1.4.2+build.7` con `1.4.2+build.8`. Declare contrato e identifique impacto real a consumidores antes de decidir.

## Riesgos y recuperación

Tipo de mensaje evidencia intención, no prueba compatibilidad. Nunca sustituya silenciosamente contenido publicado ni mueva tag de release. Si release incorrecta, siga política de remediación y publique nueva versión corregida; comunique consumidores afectados.

## Ejercicio y autoevaluación

Resultados independientes: 1.4.3, 1.5.0, 2.0.0. Release candidate precede versión normal; versiones con metadatos de build tienen igual precedencia.

## Referencia rápida

MAJOR.MINOR.PATCH / pre-release / build metadata

## Fuentes

- <https://semver.org/spec/v2.0.0.html>
- <https://www.conventionalcommits.org/en/v1.0.0/>
- <https://git-scm.com/docs/git-tag>
