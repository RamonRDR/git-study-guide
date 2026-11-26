# Protección de ramas y rulesets

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../06-permissions-and-least-privilege/README.es.md) · [Índice](../README.es.md) · [Siguiente](../08-codeowners-and-responsibilities/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 40 min

**Requisitos previos:** [Flujos profesionales](../../professional-workflows/README.es.md) · [Permisos y mínimo privilegio](../06-permissions-and-least-privilege/README.es.md)

**Objetivo:** Distinguir reglas impuestas de rama y política de equipo.

## Qué es y por qué

Ramas Git son refs; alojamiento añade reglas de servidor. Protección y rulesets GitHub pueden restringir push, eliminación, force-push, métodos de merge, checks y reviews; reglas aplicables pueden combinarse. Ramas protegidas y merge checks GitLab gobiernan push/merge y condiciones de pipeline. Recursos varían por plan, visibilidad y configuración. Distinga checks impuestos de política escrita: autorización humana puede existir sin requisito numérico de approvals. Compruebe destino, modo, actores/bypass, nombres de checks y review obsoleto. Historial lineal no garantiza toda modificación revisada.

## Práctica

Sin conexión: diseñe reglas para catálogo público: PR obligatorio, checks Ubuntu/Windows, sin bypass, push directo, force-push ni eliminación main, solo squash, discusiones resueltas y autorización humana separada. Con SHA anterior verde y nuevo no probado, decida merge. Inspeccione ajustes públicos solo lectura si disponibles; nunca cambie ajustes del guía.

## Riesgos y recuperación

Nunca quite protección ni añada bypass solo para liberar CI. Diagnostique checks fallidos/pendientes; corrija cambio enfocado y revalide. Cambios administrativos requieren autorización aparte.

## Ejercicio y autoevaluación

SHA nuevo no tiene evidencia válida. Preserve protecciones y obtenga validación nueva y autorización explícita.

## Referencia rápida

protected branch / ruleset / required checks / bypass

## Referencias

- <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets>
- <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches>
- <https://docs.gitlab.com/user/project/repository/branches/protected/>
