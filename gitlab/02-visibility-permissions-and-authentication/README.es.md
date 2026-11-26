# Visibilidad, permisos y autenticación

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../01-projects-groups-and-offerings/README.es.md) · [Índice](../README.es.md) · [Siguiente](../03-issues-labels-milestones-and-boards/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 35 min

**Requisitos previos:** [GitHub](../../github/README.es.md) · [Remotos](../../remote-repositories/README.es.md)

**Objetivo:** Separar identidad, permisos efectivos y visibilidad de lectura; elegir acceso mínimo.

## Qué es y por qué

Los proyectos públicos exponen contenido público a lectura, no escritura ilimitada. Privado limita acceso a miembros elegibles; la visibilidad interna existe en Self-Managed y Dedicated, no GitLab.com. Interno no es privado: usuarios autenticados elegibles pueden leer. Los roles típicos incluyen Guest, Planner, Reporter, Developer, Maintainer y Owner; sus capacidades exactas dependen del plan, configuración y recurso. Reporter suele servir para leer repositorios, Developer para ramas de funcionalidad, Maintainer para gestión de proyectos y Owner para propiedad de alto nivel. El acceso efectivo puede heredarse de grupos; reducir una membresía directa puede no quitar acceso heredado. Autenticación establece identidad; autorización determina operaciones permitidas. Use inicio web con 2FA, SSH con huella del host verificada y clave pública (mantenga la privada local), o HTTPS con gestor de credenciales adecuado o token de alcance mínimo y caducidad. Nombre/correo de Git atribuyen commits, no autentican. Nunca incluya tokens en URLs de remotos o comandos.

## Práctica

Sin conexión, asigne roles a analista de lectura, colaborador y mantenedor de un proyecto privado ficticio; justifique cada rol y rastree un Developer heredado del grupo padre. Opcional: inspeccione visibilidad y su rol en un sandbox privado desechable propio sin cambiar permisos ni crear tokens. Si se deniega acceso, compruebe host, identidad, membresía, restricciones de rama y alcance de credencial antes de escalar.

## Errores comunes y seguridad

Cambiar visibilidad no recupera copias. Si una credencial se expone, revóquela/rótela de inmediato y siga la política de incidentes; eliminar un commit no basta. Nunca desactive verificación de host ni conceda Owner para corregir un error común de autenticación.

## Ejercicio y autoevaluación

¿Un lector público puede hacer push a main automáticamente? No. Apruebe si identifica autorización separada de lectura, escritura y merge, acceso heredado y no propone secretos en el historial Git.

## Fuentes oficiales

- <https://docs.gitlab.com/user/public_access/>
- <https://docs.gitlab.com/user/permissions/>
- <https://docs.gitlab.com/user/ssh/>
- <https://docs.gitlab.com/user/profile/personal_access_tokens/>
- <https://docs.gitlab.com/user/profile/account/two_factor_authentication/>

---

<!-- navigation-footer -->
[Anterior](../01-projects-groups-and-offerings/README.es.md) · [Índice](../README.es.md) · [Siguiente](../03-issues-labels-milestones-and-boards/README.es.md)
<!-- /navigation-footer -->
