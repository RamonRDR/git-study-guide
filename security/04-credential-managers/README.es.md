# Gestores de credenciales y ámbito de configuración

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../03-https-and-access-tokens/README.es.md) · [Índice](../README.es.md) · [Siguiente](../05-secrets-and-disclosure-prevention/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 35 min

**Requisitos previos:** [Flujos profesionales](../../professional-workflows/README.es.md) · [HTTPS y tokens de acceso](../03-https-and-access-tokens/README.es.md)

**Objetivo:** Distinguir almacenamiento de helper y revocación.

## Qué es y por qué

Helpers Git obtienen y guardan credenciales para HTTPS; Git Credential Manager puede usar autenticación del proveedor y almacenamiento del SO adecuado según configuración. Helper `cache` guarda temporalmente en memoria; `store` guarda texto plano en disco, inadecuado para credenciales sensibles duraderas. Configuración system, global y local tienen ámbitos distintos; varios helpers pueden estar activos. `git config --show-origin --get-all credential.helper` es diagnóstico de solo lectura, pero puede revelar comando personalizado o rutas sensibles. Inspeccione localmente, nunca comparta salida bruta. Agentes SSH y helpers HTTPS son mecanismos distintos.

## Práctica

Sin conexión: compare caché memoria, texto plano y gestor aprobado del SO. Dada credencial guardada obsoleta ficticia, describa eliminación segura y nueva autenticación mediante interfaz documentada del gestor. Distinga olvidar credencial local de revocar remotamente.

## Riesgos y recuperación

No ejecute comandos de recuperación para imprimir contraseñas/tokens. No cambie helpers globales en ejercicio. Use flujo de eliminación/cierre de sesión soportado para cuenta y host correctos; revoque credenciales comprometidas también en emisor.

## Ejercicio y autoevaluación

Prefiera almacenamiento protegido aprobado; eliminación local no revoca credencial del emisor. Sin credenciales reales.

## Referencia rápida

helper / cache / store / credential manager

## Referencias

- <https://git-scm.com/docs/gitcredentials>
- <https://git-scm.com/docs/git-credential-store>
- <https://git-scm.com/docs/git-credential-cache>
- <https://github.com/git-ecosystem/git-credential-manager>

---

<!-- navigation-footer -->
[Anterior](../03-https-and-access-tokens/README.es.md) · [Índice](../README.es.md) · [Siguiente](../05-secrets-and-disclosure-prevention/README.es.md)
<!-- /navigation-footer -->
