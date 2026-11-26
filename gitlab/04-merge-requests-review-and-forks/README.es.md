# Merge requests, revisión de código y forks

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../03-issues-labels-milestones-and-boards/README.es.md) · [Índice](../README.es.md) · [Siguiente](../05-protected-branches-and-merge-checks/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 45 min

**Requisitos previos:** [GitHub](../../github/README.es.md) · [Remotos](../../remote-repositories/README.es.md)

**Objetivo:** Revisar cambio propuesto y elegir colaboración en proyecto o por fork con seguridad.

## Qué es y por qué

Una MR es propuesta alojada en GitLab para integrar rama de origen en destino; GitHub llama pull request (PR) a la función análoga. Ninguna es objeto Git nativo. Una MR registra descripción, diff, commits, discusiones, reviewers, checks y estado de merge. En proyecto compartido, colaboradores envían ramas de funcionalidad donde se permita; para contribución externa, fork es proyecto alojado separado, con permisos propios y relación con upstream. Clon es copia local, no fork. MR de fork puede apuntar a upstream, pero acceso, ejecución de pipeline y permisos de colaboración difieren. Revise proyecto y rama de origen/destino reales, revisión exacta, diff, evidencia de pruebas y discusiones abiertas. Draft señala trabajo no listo para integración. Tras corregir, verifique la nueva revisión antes de resolver discusión; aprobaciones no prueban tests ni seguridad. Método de merge altera historial como enseña módulo 05.

## Práctica

Simule sin conexión issue #12 y MR !7: `docs/setup` → `main`. Diff propuesto añade instrucciones pero omite requisito. Escriba review pidiendo ese requisito y comprobación verificable; simule revisión corregida y revise de nuevo. Para comparación Git real, use laboratorio desechable de dos clones del [módulo 06](../../remote-repositories/README.es.md); inspeccione `git status`, `git log --oneline main..HEAD` y `git diff main...HEAD` tras verificar ref base local. Estos comandos no crean MR. Opcional: inspeccione MR pública existente solo lectura; o cree draft en sandbox privado propio tras comprobar origen, destino e historial. No se exige merge ni contribución externa.

## Errores comunes y seguridad

Nunca ejecute pipeline de fork no confiable con credenciales privilegiadas; fork puede cambiar configuración del pipeline. Verifique licencia antes de reutilizar. Si destino o diff es incorrecto, pare, corrija propuesta o cierre su draft; no haga force-push de historial compartido. Respete política de contribución.

## Ejercicio y autoevaluación

Apruebe si distingue clon, fork, rama y MR, nombra refs y proyectos, explica por qué la corrección exige nueva revisión e identifica requisito faltante antes de recomendar merge.

## Fuentes oficiales

- <https://docs.gitlab.com/user/project/merge_requests/>
- <https://docs.gitlab.com/user/project/merge_requests/reviews/>
- <https://docs.gitlab.com/user/project/merge_requests/authorization_for_merge_requests/>
- <https://docs.gitlab.com/user/project/repository/forking_workflow/>

---

<!-- navigation-footer -->
[Anterior](../03-issues-labels-milestones-and-boards/README.es.md) · [Índice](../README.es.md) · [Siguiente](../05-protected-branches-and-merge-checks/README.es.md)
<!-- /navigation-footer -->
