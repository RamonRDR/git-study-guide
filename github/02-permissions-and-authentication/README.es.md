# Permisos y autenticación

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../01-platform-and-repositories/README.es.md) · [Índice](../README.es.md) · [Siguiente](../03-issues-and-planning/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 25 min

**Requisitos previos:** [Remotos](../../remote-repositories/README.es.md) · [Historial y recuperación](../../history-and-recovery/README.es.md) · [GitHub, repositorios y visibilidad](../01-platform-and-repositories/README.es.md)

**Objetivo:** Separar identidad, autenticación y autorización y aplicar mínimo privilegio.

## Qué y por qué

Campos de autor identifican autor declarado; no son credenciales de login. Autenticación verifica acceso a cuenta; autorización determina acciones permitidas. Roles organizacionales incluyen read, triage, write, maintain y admin; repositorios personales usan modelo distinto. Colaborador con escritura normalmente propone y envía ramas permitidas pero sigue rulesets. Owners/admins configuran permisos; revisores evalúan cambios; mantenedores deciden integración. Usa autenticación de dos factores, gestores HTTPS aprobados o claves SSH, y tokens limitados con caducidad solo si es necesario. Nunca guardes credenciales en URLs, Markdown, historial de shell ni capturas. Firma verificada es distinta de autorización.

## Práctica

Offline: equipo ficticio tiene lector, coordinador de issues, desarrollador y administrador. Asigna rol organizacional mínimo para lectura, triaje, push de ramas y cambio de accesos respectivamente. Opcional: revisa configuración de seguridad de tu cuenta en privado; no hace falta generar tokens, compartir ni cambiar roles. Consulta guía oficial antes de clonar sandbox privado; comprueba cuenta y repo. Si acceso denegado, inspecciona cuenta, remoto y política en vez de elevar permisos.

## Errores comunes y seguridad

No concedas admin solo para corregir push rechazado. Si credencial se filtra, revoca o rota inmediatamente y avisa al responsable; quitarla del último commit no basta. Nunca pegues diagnósticos de cuenta o tokens en issues.

## Ejercicio y autoevaluación

Respuesta: read, triage, write, admin, sujetos a política organizacional. Aprueba si nombre de autor no se trata como prueba de login y permisos no se amplían innecesariamente.

## Referencia rápida

- `authentication`
- `authorization`
- `least privilege`

## Fuentes oficiales

- <https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/repository-roles-for-an-organization>
- <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github>
