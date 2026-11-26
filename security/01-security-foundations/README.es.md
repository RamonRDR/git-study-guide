# Fundamentos de seguridad en Git

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Módulo anterior](../../professional-workflows/README.es.md) · [Índice](../README.es.md) · [Siguiente](../02-ssh-authentication/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 30 min

**Requisitos previos:** [Flujos profesionales](../../professional-workflows/README.es.md)

**Objetivo:** Distinguir capas de seguridad y fronteras de confianza.

## Qué es y por qué

Seguridad protege confidencialidad (quién lee), integridad (qué es auténtico e inalterado) y disponibilidad (servicio utilizable). Autenticación identifica actor; autorización determina acciones permitidas. Git registra contenido e historial, no es sistema completo de control de acceso. Hash identifica objeto, no identidad ni confianza del autor. Permisos locales, políticas de alojamiento y CI son capas distintas. Repositorio público puede leerse por todos sin permitir escritura. Copias, clones y forks pueden sobrevivir a eliminación.

## Práctica

Para catálogo ficticio de biblioteca, clasifique documentación pública, registros privados de personal y permiso de merge. Dibuje límites entre estación, host y runner. Para cada uno, identifique activo, amenaza y control. Usuario de solo lectura puede leer docs públicas, no alterar main.

## Riesgos y recuperación

No suponga repo privado como bóveda, hash como firma o visibilidad pública como escritura. Si límite incierto, detenga y compruebe permisos reales con administrador autorizado.

## Ejercicio y autoevaluación

Docs públicas son legibles; registros privados quedan fuera del ejercicio; merge es decisión de autorización. Explique tres propiedades de seguridad.

## Referencia rápida

confidentiality / integrity / availability / authentication / authorization

## Referencias

- <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github>
- <https://git-scm.com/docs/git>

---

<!-- navigation-footer -->
[Módulo anterior](../../professional-workflows/README.es.md) · [Índice](../README.es.md) · [Siguiente](../02-ssh-authentication/README.es.md)
<!-- /navigation-footer -->
