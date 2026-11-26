# Proyectos, grupos y modalidades de GitLab

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
— · [Índice](../README.es.md) · [Siguiente](../02-visibility-permissions-and-authentication/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 30 min

**Requisitos previos:** [GitHub](../../github/README.es.md) · [Remotos](../../remote-repositories/README.es.md)

**Objetivo:** Distinguir datos Git de servicios GitLab y elegir un espacio de nombres y una modalidad adecuados.

## Qué es y por qué

Git almacena commits, árboles, ramas y etiquetas. GitLab añade un proyecto alrededor del repositorio: issues, merge requests (MRs), control de acceso, pipelines y releases. Un clon contiene datos Git, no toda la base de datos del proyecto. Un namespace identifica dónde reside el proyecto. Un grupo puede contener proyectos y subgrupos; miembros y configuraciones pueden heredarse en la jerarquía. Por ejemplo, `studio/tools/catalog` puede representar el grupo `studio`, subgrupo `tools` y proyecto `catalog`. Un namespace personal no es un grupo compartido. GitLab.com es un servicio alojado multi-tenant; Self-Managed se instala y administra por la organización, que asume costes de infraestructura y mantenimiento; Dedicated es alojamiento gestionado single-tenant. Modalidad y plan (Free, Premium, Ultimate) son decisiones distintas. Los recursos también dependen de versión, configuración y permisos.

## Práctica

En papel diseñe un grupo para un estudio ficticio, con subgrupo `tools` y dos proyectos. Dibuje clon local → repositorio Git → proyecto GitLab → grupo; clasifique commit, issue, tag y MR. Opcionalmente inspeccione un proyecto público en el navegador sin iniciar sesión ni publicar. Para un equipo que necesita centralizar miembros, prefiera un grupo a distribuir la propiedad en namespaces personales.

## Errores comunes y seguridad

No transfiera ni renombre proyectos reales como ejercicio: rutas, integraciones y acceso heredado pueden cambiar. Self-Managed no es automáticamente gratuito. Consulte versión y plan antes de prometer recursos; no se necesita instalar nada.

## Ejercicio y autoevaluación

¿Un clon recupera todas las issues y miembros del grupo? No. Apruebe si distingue objetos Git de metadatos alojados, acierta la jerarquía e identifica quién administra la modalidad elegida.

## Fuentes oficiales

- <https://docs.gitlab.com/user/namespace/>
- <https://docs.gitlab.com/user/group/>
- <https://docs.gitlab.com/subscriptions/choosing_subscription/>
