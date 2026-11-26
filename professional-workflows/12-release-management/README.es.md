# Gestión de releases

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../11-ai-assisted-development/README.es.md) · [Índice](../README.es.md) · [Siguiente](../13-integrated-professional-workflow-lab/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 40 min

**Requisitos previos:** [CI/CD](../../ci-cd/README.es.md) · [Trabajo profesional asistido por IA](../11-ai-assisted-development/README.es.md)

**Objetivo:** Preparar release con versión, revisión, evidencia y decisión de publicación separada.

## Qué es y por qué

Release identifica revisión probada y comunica qué pueden usar consumidores. Tag Git es ref, a menudo anotada con mensaje; release alojada puede adjuntar notas y assets a tag. Despliegue es acto separado de promover artefacto a entorno. Parta de revisión integrada aprobada, decida versión según contrato público, registre cambios/migración y límites, compruebe checks y procedencia, cree tag anotado en commit elegido y obtenga autorización de release antes de publicar. Para inspección local use `git show v1.1.0` y `git rev-parse 'v1.1.0^{commit}'` tras capítulo 13. Firma y controles de releases inmutables pueden ayudar si se configuran; tag anotado no está automáticamente firmado ni es inmutable.

```text
tested commit -> annotated tag -> authorized publication -> deployment decision
```

## Práctica

Suponga catálogo 1.0.0 con formato público documentado y disponibilidad como campo nuevo retrocompatible en escenario hipotético. Redacte notas 1.1.0: feature, comportamiento, verificación, migración (ninguna necesaria para consumidores compatibles), límites (solo lab local, sin ejecución alojada) e identificador de artefacto/revisión. Dibuje control entre tag, publicación y despliegue. No publique nada en ejercicio.

## Riesgos y recuperación

No reetiquete versión publicada ni publique head no revisado. Si escapa release defectuosa, comunique, detenga promoción y siga política rollback/forward-fix; migración de datos puede impedir rollback fácil. Permisos de release y despliegue son distintos de merge. No se exige artefacto externo ni despliegue real.

## Ejercicio y autoevaluación

1.1.0 se justifica solo por contrato compatible declarado. Tag apunta a revisión probada; notas informan checks y límites reales; producción queda igual.

## Referencia rápida

tag / release notes / artifact / deployment

## Fuentes

- <https://semver.org/spec/v2.0.0.html>
- <https://git-scm.com/docs/git-tag>
- <https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository>

---

<!-- navigation-footer -->
[Anterior](../11-ai-assisted-development/README.es.md) · [Índice](../README.es.md) · [Siguiente](../13-integrated-professional-workflow-lab/README.es.md)
<!-- /navigation-footer -->
