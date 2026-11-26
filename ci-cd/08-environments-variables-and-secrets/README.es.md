# Entornos, variables y secretos

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../07-artifacts-and-cache/README.es.md) · [Índice](../README.es.md) · [Siguiente](../09-quality-gates-and-troubleshooting/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 40 min

**Requisitos previos:** [GitHub](../../github/README.es.md) · [GitLab](../../gitlab/README.es.md) · [Artefactos y caché](../07-artifacts-and-cache/README.es.md)

**Objetivo:** Separar destinos de despliegue, configuración no sensible y credenciales; aplicar mínimo privilegio.

## Qué es y por qué

Entorno es destino de despliegue o recurso de plataforma que lo representa, como staging o producción. Variable guarda configuración; secreto guarda material sensible y no debe confirmarse en Git. En GitHub Actions, reglas de protección y secrets de entorno pueden restringir jobs de despliegue según plan, visibilidad y configuración. En GitLab, entornos y variables CI/CD con ámbito, enmascaradas, ocultas o protegidas tienen significados y elegibilidad distintos. Enmascaramiento reduce exposición accidental en algunos logs; no protege contra código malicioso. Variable protegida tiene ámbito de refs protegidas elegibles y condiciones de pipeline, no seguridad universal. Token automático GitHub y job token GitLab también requieren mínimo privilegio. Prefiera credenciales breves y acotadas, jobs confiables aprobados e identidades separadas; no se necesita credencial real.

## Práctica

Sin conexión diseñe dos destinos: `staging` y `production`. Clasifique `APP_MODE=staging` como no sensible y `DEPLOY_CREDENTIAL` solo como nombre de credencial (no asigne valor). Construya tabla de acceso: checks de PR sin credenciales de despliegue; despliegue aprobado recibe acceso acotado al destino. Clasifique aprobación como manual o impuesta solo tras verificar plan/configuración reales.

## Errores comunes y seguridad

Nunca imprima secretos, colóquelos en artefactos ni exponga a código no confiable. Ante sospecha de exposición, detenga ejecuciones afectadas, revoque/rote credenciales, avise a mantenedores autorizados e investigue logs/ámbito. Quitar valor YAML o enmascararlo no revoca credencial. No cree entornos ni secretos reales para práctica.

## Ejercicio y autoevaluación

Apruebe si checks de PR no alcanzan credenciales de despliegue, promoción a producción tiene autorización separada y enmascaramiento no se confunde con aislamiento.

## Referencia rápida

environment / variable / secret

## Fuentes oficiales

- <https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments>
- <https://docs.github.com/en/actions/reference/security/secure-use>
- <https://docs.gitlab.com/ci/variables/>
- <https://docs.gitlab.com/ci/environments/>
