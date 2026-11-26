# Autenticación segura y plataformas de alojamiento

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../04-remote-branch-lifecycle/README.es.md) · [Índice](../README.es.md) · [Siguiente módulo](../../history-and-recovery/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 20 min

**Requisitos previos:** [Ciclo de vida de ramas remotas y prune](../04-remote-branch-lifecycle/README.es.md)

**Objetivo:** Elegir métodos de acceso seguros sin crear ni exponer credenciales.

## Qué y por qué

Autenticación demuestra quién puede acceder a un servicio; autorización controla acciones permitidas. Identidad de autor de commit es metadato, no autenticación. HTTPS usa TLS para proteger transporte; proveedores pueden exigir tokens o inicio de sesión en navegador en vez de contraseña de cuenta. SSH usa par de claves privada/pública; la privada permanece privada y el servicio recibe la pública. Verifica claves de host contra huellas oficiales confiables de forma independiente antes de aceptar; nunca desactives verificación de host o TLS. Un credential helper o manager almacena/recupera credenciales; prefiere almacenamiento seguro del SO, no texto plano. Los tokens deben tener alcance mínimo de repo/acción, caducar cuando sea viable y revocarse si ya no se necesitan.

## Práctica

No se exige operación en línea. En el lab local terminado no fue necesaria autenticación con servicio externo. Para clone hipotético de solo lectura, compara formatos ficticios de URL (no ejecutes): `https://example.invalid/team/project.git` y `git@example.invalid:team/project.git`. HTTPS y SSH cambian la conexión de Git, no IDs de commits, refs ni semántica de merge. Antes de futura práctica en línea opcional, usa instrucciones oficiales del proveedor y repo desechable propio autorizado. Comprueba destinos de fetch/push en privado, host y permisos, luego elige mínimo privilegio. No pongas tokens en URL, argumentos, archivos fuente, capturas ni logs. No pegues claves privadas ni tokens en esta guía ni herramientas de IA. Git implementa clone/fetch/push; pull requests, merge requests, checks obligatorios y protección de ramas son funciones de GitHub/GitLab, tratadas después. Un remoto puede rechazar actualización válida por permisos o política. Un bare Git nativo también puede aplicar hooks/políticas, pero no proporciona interfaz de PR alojada por sí mismo.

## Errores comunes y seguridad

Si falla autenticación, verifica URL, cuenta, caducidad y permisos con documentación oficial; no amplíes acceso indiscriminadamente. Si se filtra una credencial, revoca/rota inmediatamente y avisa al responsable; borrar archivo o commit no basta. No imprimas configuración completa ni contenido de credenciales para diagnóstico. No se probó autenticación externa en este módulo.

## Ejercicio y autoevaluación

Un compañero necesita leer un repo. ¿Compartes un token amplio o clave SSH privada? Pista: identidad y mínimo privilegio. Respuesta: ninguno; concede acceso individual autorizado con permisos mínimos. Aprueba si explicas autenticación frente a metadatos de autor, HTTPS frente a SSH y por qué PR no es comando Git.

## Referencia rápida

- `git remote get-url origin`
- `git remote get-url --push origin`
- `git help credentials`

## Fuentes oficiales

- [Git: gitcredentials](https://git-scm.com/docs/gitcredentials)
- [Git: git-clone](https://git-scm.com/docs/git-clone)
- [Git: git-config](https://git-scm.com/docs/git-config)
- [GitHub: authentication](https://docs.github.com/en/authentication)
- [GitLab: SSH](https://docs.gitlab.com/user/ssh/)
- [GitLab: access tokens](https://docs.gitlab.com/user/profile/personal_access_tokens/)

---

<!-- navigation-footer -->
[Anterior](../04-remote-branch-lifecycle/README.es.md) · [Índice](../README.es.md) · [Siguiente módulo](../../history-and-recovery/README.es.md)
<!-- /navigation-footer -->
