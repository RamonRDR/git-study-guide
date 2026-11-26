# Exposición de credenciales y respuesta a incidentes

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../10-software-supply-chain/README.es.md) · [Índice](../README.es.md) · [Siguiente](../12-governance-audit-and-traceability/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 45 min

**Requisitos previos:** [Flujos profesionales](../../professional-workflows/README.es.md) · [Seguridad de cadena de suministro de software](../10-software-supply-chain/README.es.md)

**Objetivo:** Priorizar contención y remediación coordinada.

## Qué es y por qué

Trate sospecha de credencial expuesta como comprometida hasta evaluación. Primero contenga: revoque/rote en emisor pronto, detenga automatización afectada y avise responsables autorizados en privado. Preserve evidencia segura (revisión, período, sistema, no secreto) y evalúe alcance: historial, clones, forks, cachés, logs, artefactos y registros de acceso. Restaure servicio con reemplazos acotados por canales aprobados. Borrar archivo o revertir commit no revoca credencial ni borra historial alcanzable. Limpieza de historial puede requerir reescritura coordinada, IDs cambiados, pérdida de firmas, limpieza de colaboradores y soporte del host; no garantiza eliminación de copias. Siga procedimiento autorizado antes de limpieza destructiva.

[Política de seguridad](../../docs/localized/SECURITY.es.md)

## Práctica

Simulación de mesa: credencial ficticia de despliegue aparece en commit público. No se proporciona valor. Ordene contención, notificación, investigación, reemplazo, decisión de limpieza y lecciones. Redacte informe privado con componente, marcador de revisión, riesgo y mitigación; nunca detalles sensibles en issue pública. Consulte política de seguridad del guía.

## Riesgos y recuperación

Nunca pruebe si credencial expuesta ajena funciona. No pegue en chat/scanner ni force-push historial como primera respuesta. Si no hay canal privado verificado, establezca uno sin divulgar detalles públicamente.

## Ejercicio y autoevaluación

Revoque/rote y contenga primero; investigue y coordine limpieza después. Recuperación no garantiza desaparición de copias.

## Referencia rápida

revoke / rotate / contain / investigate

## Referencias

- <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository>
- <https://csrc.nist.gov/pubs/sp/800/61/r3/final>

---

<!-- navigation-footer -->
[Anterior](../10-software-supply-chain/README.es.md) · [Índice](../README.es.md) · [Siguiente](../12-governance-audit-and-traceability/README.es.md)
<!-- /navigation-footer -->
