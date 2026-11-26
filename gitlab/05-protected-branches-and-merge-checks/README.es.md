# Ramas protegidas, aprobaciones y controles de merge

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../04-merge-requests-review-and-forks/README.es.md) · [Índice](../README.es.md) · [Siguiente](../06-pipelines-and-runners/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 35 min

**Requisitos previos:** [GitHub](../../github/README.es.md) · [Remotos](../../remote-repositories/README.es.md)

**Objetivo:** Diseñar política de protección de rama predeterminada y distinguir controles obligatorios de convenciones.

## Qué es y por qué

Las ramas protegidas de GitLab usan reglas para restringir operaciones en refs seleccionadas. `Allowed to merge` controla integración vía MR; `Allowed to push and merge` también concede push directo. Para exigir MRs, seleccione explícitamente No one para push and merge y conceda merge solo a roles adecuados; regla sin configurar no equivale a denegación explícita. Inspeccione reglas solapadas con wildcard y heredadas; acceso efectivo puede ser más permisivo que una regla aislada sugiere. Desactive force push salvo justificación explícita. Merge checks pueden exigir pipelines exitosos y discusiones resueltas cuando se configuran. GitLab Free ofrece protección básica y aprobaciones voluntarias, pero reglas de aprobación obligatoria y enforcement de aprobación por Code Owner dependen de Premium/Ultimate y configuración aplicable. No presente checklist informal como regla técnicamente impuesta. Branch rules y rulesets de GitHub tienen intención análoga, no equivalencia recurso por recurso. Check aprobado evidencia una revisión, no corrección universal.

## Práctica

Sin conexión diseñe política: developers envían ramas de funcionalidad, ningún push directo a `main`, mantenedores integran solo tras review, pipeline obligatorio exitoso y discusiones resueltas. Marque cada control como impuesto, manual o no disponible hasta verificar plan real. En escenario mantenedor encuentra pipeline fallido y discusión abierta: rechace merge y pida corrección. Opcional: inspeccione reglas en sandbox privado propio sin modificarlas; identifique plan/versión y configuración real.

## Errores comunes y seguridad

Nunca debilite protección para pasar merge. Si merge bloqueado, lea check exacto, resuelva causa, repita checks en nueva revisión y busque autorización. No suponga que aprobación o pipeline no relacionado exitoso reemplaza controles obligatorios.

## Ejercicio y autoevaluación

¿Maintainer en Allowed to push and merge impide push directo? No. Apruebe si deniega push explícitamente y distingue aprobación obligatoria de revisión voluntaria.

## Fuentes oficiales

- <https://docs.gitlab.com/user/project/repository/branches/protected/>
- <https://docs.gitlab.com/user/project/repository/branches/branch_rules/>
- <https://docs.gitlab.com/user/project/merge_requests/approvals/>
- <https://docs.gitlab.com/user/project/merge_requests/approvals/rules/>
- <https://docs.gitlab.com/user/project/merge_requests/auto_merge/>

---

<!-- navigation-footer -->
[Anterior](../04-merge-requests-review-and-forks/README.es.md) · [Índice](../README.es.md) · [Siguiente](../06-pipelines-and-runners/README.es.md)
<!-- /navigation-footer -->
