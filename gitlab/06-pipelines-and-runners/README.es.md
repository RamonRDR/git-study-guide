# Introducción a pipelines y runners

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../05-protected-branches-and-merge-checks/README.es.md) · [Índice](../README.es.md) · [Siguiente](../07-tags-and-releases/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 30 min

**Requisitos previos:** [GitHub](../../github/README.es.md) · [Remotos](../../remote-repositories/README.es.md)

**Objetivo:** Explicar cómo se ejecuta automatización alojada e interpretar estado sin ejecutar pipeline.

## Qué es y por qué

Pipeline coordina jobs automatizados para revisión y evento; job es unidad individual de trabajo. Runner es agente de ejecución que recibe jobs elegibles, prepara entorno, ejecuta comandos y devuelve resultados. GitLab normalmente lee `.gitlab-ci.yml` del proyecto; configuración y evento determinan si existe pipeline. GitHub Actions usa workflows generalmente en `.github/workflows/`; ambos automatizan trabajo, pero sintaxis, eventos, permisos y modelos de runners difieren. Runner puede tener ámbito de proyecto, grupo o instancia, y ser alojado o autogestionado según modalidad. Disponibilidad, permisos y tags del runner pueden afectar planificación. Runners alojados en GitLab.com consumen cuota según uso y tipo; no suponga cómputo gratuito ilimitado. YAML completo, artifacts, cache y deployment quedan para módulo 10.

## Práctica

Dibuje revisión A → pipeline → job `validate` → runner → resultado de job. Escenario: A aprueba; revisión B llega y su job está pendiente. Registre por qué A no establece estado de B. Job fallido exige inspección de logs; pendiente puede significar espera de runner elegible. Opcional: inspeccione pipeline público existente y revisión solo lectura cuando visible; no dispare, repita ni registre runners.

## Errores comunes y seguridad

No ejecute código no confiable con secretos o runners privilegiados. Check omitido, ausente o pendiente no demuestra ejecución exitosa. Inspeccione revisión, evento, estado y logs; no eluda checks ni compre cómputo para práctica.

## Ejercicio y autoevaluación

Apruebe si distingue pipeline, job y runner, identifica B como aún no validada y explica por qué problema de cuota/planificación no es test aprobado.

## Fuentes oficiales

- <https://docs.gitlab.com/runner/>
- <https://docs.gitlab.com/ci/runners/>
- <https://docs.gitlab.com/ci/pipelines/compute_minutes/>
- <https://docs.gitlab.com/ci/pipelines/settings/>

---

<!-- navigation-footer -->
[Anterior](../05-protected-branches-and-merge-checks/README.es.md) · [Índice](../README.es.md) · [Siguiente](../07-tags-and-releases/README.es.md)
<!-- /navigation-footer -->
