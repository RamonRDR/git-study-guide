# Gobernanza, auditoría y trazabilidad

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../11-credential-exposure-and-incident-response/README.es.md) · [Índice](../README.es.md) · [Siguiente](../13-integrated-security-lab/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 40 min

**Requisitos previos:** [Flujos profesionales](../../professional-workflows/README.es.md) · [Exposición de credenciales y respuesta a incidentes](../11-credential-exposure-and-incident-response/README.es.md)

**Objetivo:** Registrar aprobación y evidencia auditable.

## Qué es y por qué

Gobernanza define quién decide, ejecuta y revisa; evidencia registra lo ocurrido. Historial de commits es útil pero no captura toda acción administrativa/alojamiento. Logs de auditoría, PR/MR, CI, metadatos de artefactos y aprobación complementan, sujetos a acceso y retención. Registre head/base, revisión merge probada, resultados/límites, hallazgos, autorización, commit/tree integrados, limpieza de rama y checks post-merge. Separe diseño de política, imposición efectiva y resultados observados. No invente evidencia ni conserve información privada en notas públicas.

[Registro de tareas](../../docs/specs/project-foundation/tasks.es.md)

## Práctica

Cree registro ficticio: requisito, PR, marcador SHA revisado, estado Linux/Windows, hallazgos pendientes, decisión humana, comparación de tree y riesgo residual. Si Windows pendiente, marque control pendiente, no aprobado. Compare políticas de contribución y tareas del guía.

## Riesgos y recuperación

No confunda solicitud de review con aprobación, ni disponibilidad de log con completitud. Restrinja evidencia sensible a retención/canales autorizados. Nunca cambie reglas ni integre por aprobación supuesta; registre carencias y escale.

## Ejercicio y autoevaluación

Windows pendiente bloquea control; autorización y resultados observados se refieren a revisión exacta. Registre límites honestamente.

## Referencia rápida

revision / evidence / decision / residual risk

## Referencias

- <https://docs.github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/reviewing-the-audit-log-for-your-organization>
- <https://docs.gitlab.com/user/compliance/audit_events/>

---

<!-- navigation-footer -->
[Anterior](../11-credential-exposure-and-incident-response/README.es.md) · [Índice](../README.es.md) · [Siguiente](../13-integrated-security-lab/README.es.md)
<!-- /navigation-footer -->
