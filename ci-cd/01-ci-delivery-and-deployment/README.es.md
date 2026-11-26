# Integración, entrega y despliegue continuos

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
— · [Índice](../README.es.md) · [Siguiente](../02-yaml-fundamentals/README.es.md)
<!-- /navigation -->

**Nivel:** principiante · **Tiempo estimado:** 30 min

**Requisitos previos:** [GitHub](../../github/README.es.md) · [GitLab](../../gitlab/README.es.md)

**Objetivo:** Explicar las tres prácticas y elegir un límite seguro de promoción.

## Qué es y por qué

Integración continua (CI) significa integrar cambios pequeños frecuentemente y obtener feedback automatizado rápido. Entrega continua mantiene revisión probada lista para release; promoción a producción puede exigir decisión deliberada. Despliegue continuo promueve automáticamente a producción cambios que satisfacen los controles configurados. CD puede significar entrega o despliegue; especifique cuál. Build crea entregable, test verifica comportamiento y despliegue cambia entorno en ejecución. CI exitosa no demuestra despliegue ni seguridad para todo usuario.

Flujo accesible:

```text
change -> CI checks -> release candidate -> promotion -> production
              | failure: stop and correct
```

En entrega, promoción puede ser manual; en despliegue, es automática tras controles. Decisión de liberar funcionalidad también puede separarse del despliegue (por ejemplo, feature toggle).

## Práctica

Sin conexión: catálogo ficticio tiene tres revisiones. A falla tests; B pasa pero espera aprobación; C se despliega tras checks. Clasifique cada una y dibuje control entre B y producción. En equipo profesional, registre revisión exacta, evidencias, aprobación y plan de rollback antes de promover.

## Errores comunes y seguridad

No despliegue revisión fallida o desconocida. Rollback puede exigir migraciones de datos compatibles; nunca prometa que Git revert restaura sistema activo. Detenga promoción y siga plan de incidente.

## Ejercicio y autoevaluación

A está bloqueada; B ilustra preparación de entrega; C ilustra despliegue, automático solo si política lo promueve automáticamente. Apruebe si explica tres conceptos sin confundir merge, release y despliegue.

## Referencia rápida

CI / delivery / deployment

## Fuentes oficiales

- <https://docs.gitlab.com/ci/introduction/>
- <https://docs.github.com/en/actions/get-started/understand-github-actions>
