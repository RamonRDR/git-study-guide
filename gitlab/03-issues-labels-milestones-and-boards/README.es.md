# Issues, labels, milestones y tableros

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../02-visibility-permissions-and-authentication/README.es.md) · [Índice](../README.es.md) · [Siguiente](../04-merge-requests-review-and-forks/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 25 min

**Requisitos previos:** [GitHub](../../github/README.es.md) · [Remotos](../../remote-repositories/README.es.md)

**Objetivo:** Convertir un problema en trabajo rastreable con criterios de aceptación y visibilidad.

## Qué es y por qué

Una issue registra problema o tarea, no un commit Git. Una label categoriza trabajo, un milestone agrupa trabajo hacia una meta y un tablero muestra trabajo en listas. Un tablero puede usar labels u otros filtros; arrastrar tarjeta puede cambiar metadatos según configuración. Proyectos y grupos pueden compartir contexto de planificación; tipos de work items y tableros avanzados varían por plan y versión. Assignee asume ejecución; reviewer verifica el cambio propuesto. Vincule MR a issue para preservar trazabilidad. Una palabra de cierre como `Closes #12` puede cerrar la issue referenciada cuando la MR pertinente se integra en la rama predeterminada según configuración aplicable. No la use para trabajo no relacionado.

## Práctica

En papel cree issue #12: catálogo ficticio sin instrucciones de instalación. Defina resultado esperado (principiante localiza instrucciones), label `documentation`, milestone `v1`, responsable y reviewer. Mueva tarjeta por Open, In progress y Closed, registrando evidencia que justifica cierre. Opcional: reproduzca solo en proyecto privado desechable propio; inspeccione tablero antes y después, cierre solo su issue si desea.

## Errores comunes y seguridad

No publique datos reales de clientes, logs internos ni secretos. Issue cerrada o tarjeta movida no demuestra funcionamiento del código. Reabra issue cerrada incorrectamente y registre motivo; evite alterar milestones ajenos.

## Ejercicio y autoevaluación

Apruebe si la issue tiene resultado medible, label y milestone tienen propósitos distintos y el cierre depende de evidencia verificada, no de mover tarjeta.

## Fuentes oficiales

- <https://docs.gitlab.com/user/work_items/>
- <https://docs.gitlab.com/user/project/labels/>
- <https://docs.gitlab.com/user/project/milestones/>
- <https://docs.gitlab.com/user/project/issue_board/>

---

<!-- navigation-footer -->
[Anterior](../02-visibility-permissions-and-authentication/README.es.md) · [Índice](../README.es.md) · [Siguiente](../04-merge-requests-review-and-forks/README.es.md)
<!-- /navigation-footer -->
