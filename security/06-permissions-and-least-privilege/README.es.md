# Permisos y mínimo privilegio

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../05-secrets-and-disclosure-prevention/README.es.md) · [Índice](../README.es.md) · [Siguiente](../07-branch-protection-and-rulesets/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 40 min

**Requisitos previos:** [Flujos profesionales](../../professional-workflows/README.es.md) · [Secretos y prevención de filtraciones](../05-secrets-and-disclosure-prevention/README.es.md)

**Objetivo:** Diseñar matriz de mínimo privilegio.

## Qué es y por qué

Mínimo privilegio concede solo recursos y acciones necesarios durante tiempo necesario. Distinga roles de repo, permisos de rama, API e identidades CI. Roles GitHub y GitLab son específicos, no equivalentes por nombre; plan, instancia y herencia afectan acceso efectivo. Job build solo lectura no recibe credenciales de despliegue; identidad release no puede usarse por PR no confiable. Separe funciones cuando posible, revise accesos obsoletos y documente excepciones. Login exitoso o clone público no autoriza mutación.

## Práctica

Construya matriz para lector, contribuidor, revisor, mantenedor, check CI e identidad despliegue ficticios. Marque leer, proponer, aprobar, integrar o desplegar solo si necesario. Registre responsable y fecha de revisión. Explique por qué identidad de automatización con escritura amplia es excesiva para lint.

## Riesgos y recuperación

Nunca resuelva error de permiso haciendo a todos administradores o permitiendo ejecución privilegiada no confiable. Inspeccione política efectiva y solicite ajuste autorizado mínimo; revoque concesiones obsoletas.

## Ejercicio y autoevaluación

Lector lee, contribuidor propone, review/merge/deploy siguen políticas separadas; CI lectura salvo job justificado aparte.

## Referencia rápida

role / resource / action / duration

## Referencias

- <https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/repository-roles-for-an-organization>
- <https://docs.gitlab.com/user/permissions/>
- <https://docs.github.com/en/actions/reference/security/secure-use>

---

<!-- navigation-footer -->
[Anterior](../05-secrets-and-disclosure-prevention/README.es.md) · [Índice](../README.es.md) · [Siguiente](../07-branch-protection-and-rulesets/README.es.md)
<!-- /navigation-footer -->
