# Criterios de aceptación

[English](acceptance-criteria.md) · [Português](acceptance-criteria.pt-BR.md) · [Español](acceptance-criteria.es.md)

Fundación aprobada e integrada mediante PR #1 el 25/11/2026. Cambios posteriores requieren revisión y aprobación explícita del mantenedor.

| ID | Sprint | Condición observable de aceptación |
| --- | --- | --- |
| AC-00 | 00 | Auditar baseline y ruleset; 11 documentos principales en tres idiomas más índices, auditoría, hoja de ruta y README provisional; requisitos/decisiones alineados; enlaces y presencia de idiomas comprobados; evidencia del último PR, sin CI inventada; aprobación antes del merge. |
| AC-01 | 01 | Documentos de gobernanza y plantillas localizados; autoría y roles de IA explícitos; seguridad y soporte utilizables; sin afirmar afiliación. |
| AC-02 | 02 | Validadores rechazan idiomas ausentes, enlaces rotos, rutas/navegación inválidas y ejemplos inseguros o no aprobados; CI Linux/Windows con mínimo privilegio; evidencia de ejecución; configuración de status checks aprobada por separado. |
| AC-03 | 03 | Todos los temas 00–01 enseñados; primer commit reproducible; instrucciones por SO verificadas o limitaciones declaradas; historia referenciada. |
| AC-04 | 04 | Módulos 02–03 explican estados y efectos; pruebas verifican staging/commit/diff; diagrama accesible. |
| AC-05 | 05 | Ejemplos locales del 04 validan refs, cambio y detached HEAD; práctica remota aplazada; avisos de eliminación. |
| AC-06 | 06 | Módulo 05 valida topologías distintas, conflicto/abort/continue y efectos de squash/rebase; sin ejercicio destructivo en historial compartido. |
| AC-07 | 07 | Módulo 06 usa origin bare y dos clones; verifica tracking, divergencia y sincronización; autenticación en línea opcional, segura y documentada. |
| AC-08 | 08 | Módulo 07 distingue deshacer y reescribir historial; pruebas de recuperación y límites; labs destructivos desechables con inspección/limpieza. |
| AC-09 | 09 | Módulo 08 cubre funciones GitHub, flujo PR/review/protección, distinción de Git; tareas con cuenta opcionales y fuentes oficiales actuales. |
| AC-10 | 10 | Módulo 09 cubre MR GitLab, grupos, runners, protección y comparación; práctica alojada opcional y fuentes oficiales actuales. |
| AC-11 | 11 | Módulo 10 distingue CI/entrega/despliegue; ejemplos YAML seguros de ambas plataformas; pruebas/lint cuando proceda; sin pipeline privilegiado no confiable. |
| AC-12 | 12 | Módulo 11 compara compensaciones de flujos, SDD/TDD, práctica manual, reviews y releases con escenarios originales. |
| AC-13 | 13 | Módulo 12 cubre protección de credenciales, mínimo privilegio, firma, cadena de suministro y respuesta a incidentes; nunca exponer secretos reales. |
| AC-14 | 14 | Módulos 13–14 enseñan operaciones avanzadas e internals de objetos/refs; pruebas seguras y acotadas, diagramas correctos; requisitos de versión identificados. |
| AC-15 | 15 | Catálogo con al menos 101 IDs de entradas relevantes distintos; informar conteos por categoría por separado y validar campos, riesgos y fuentes. |
| AC-16 | 16 | Ocho proyectos en tres idiomas con preparación, objetivos, estados esperados, limpieza, soluciones y pruebas; tareas dependientes de cuenta opcionales. |
| AC-17 | 17 | Desafíos y entrevistas mapean requisitos, tienen pistas, soluciones, explicaciones, rúbricas objetivas y checks deterministas que rechazan estados incorrectos representativos; esquema piloto documentado. |
| AC-18 | 18 | Manifiesto y esquemas versionados rechazan rutas inválidas, idiomas ausentes, IDs duplicados, refs colgantes y versiones no soportadas; fixture consume revisión inmutable; ADR de playground opcional registra compatibilidad, aislamiento, límites y costo. |
| AC-19 | 19 | Tres README finales y activos visuales aprobados (o excepción aplazada explícita), insignias reales, QA aplicable completo, limitaciones registradas, entrega revisada, aprobación y evidencia de revisión inmutable. |

## Definición global de terminado

Todos los documentos públicos afectados alineados en tres idiomas; fuentes/enlaces/estructura verificados; checks relevantes ejecutados o ausencia declarada; sin hallazgos relevantes pendientes, secretos ni cambios ajenos; evidencia de tareas actual; última revisión del PR revisada y mantenedor autoriza squash merge. Checks estructurales no prueban paridad conceptual; revisión humana sigue siendo necesaria. CI ausente no es CI aprobada. Sprint 00 no puede marcarse integrada antes del merge.

## Documentos relacionados

- [Especificación](specification.es.md)
- [Tareas](tasks.es.md)
