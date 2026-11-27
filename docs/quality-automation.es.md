# Automatización de calidad

[English](quality-automation.md) · [Português](quality-automation.pt-BR.md) · [Español](quality-automation.es.md)

Mantenedores necesitan Git (2.28 o superior para la opción initial-branch) y Python 3.12; Python y CI no son requisitos del estudiante. Desde la raíz, añadir archivos nuevos al índice antes de validar, pues checks inspeccionan rutas rastreadas. Ejecutar:

```text
python scripts/validate.py
python -m unittest discover -s tests -v
```

Usar --check con structure, locales, links, navigation, examples, secrets, command-catalog, assessment-pilot o learning-hub-contract para aislar un check. Validadores inspeccionan rutas rastreadas portables, presencia de tres idiomas, enlaces relativos e imágenes Markdown inline, orden/navegación de módulos y capítulos, política de ejemplos ejecutables y patrones comunes de secretos. No prueban traducción semántica, enlaces externos, anclas, todas las sintaxis Markdown, ausencia de todos los secretos ni comportamiento de UI de plantillas. Detector informa archivo y línea, no valores; es heurístico, no exhaustivo. Revisar diffs y rotar credenciales expuestas por separado.

La validación de navegación exige bloques canónicos localizados de encabezado y pie para cada índice de módulo y capítulo, etiquetas y rutas exactas, transiciones entre capítulos y módulos, ubicación y detección de duplicados. Pruebas incluyen casos negativos de navegación ausente, divergente, reordenada, en idioma incorrecto, invertida, oculta o mal ubicada. Índices previstos siguen navegables; sus lecciones aún no se publicaron.

El check command-catalog valida las 14 categorías JSON registradas, al menos 101 operaciones distintas (objetivo aprobado de 120), mapas de idiomas, riesgos, política de URL de fuentes oficiales, capítulos relacionados, intenciones e igualdad exacta con el renderizador canónico. No ejecuta comandos del catálogo ni demuestra traducción semántica, disponibilidad de URL externas o corrección de cada ejemplo. Para cambiar el catálogo, edita el JSON canónico, prepara nuevas entradas y regenera el Markdown registrado desde la raíz:

```text
python scripts/render_command_reference.py --write
```

Prepara las páginas generadas, ejecuta `python scripts/validate.py --check command-catalog`, luego todos los validadores y pruebas. La invocación predeterminada del renderizador comprueba contenido generado sin escribir.

Aún no hay ejemplos didácticos ejecutables aprobados. El manifiesto vacío bloquea por defecto: todos los archivos en examples/ (incluidos archivos inertes y variantes de mayúsculas/minúsculas) se rechazan, independientemente de extensión o modo, y manifiestos no vacíos fallan hasta contar con protocolo de ejecución revisado. No ejecutar código arbitrario de estudiantes. Prueba inicial Git usa repo temporal aislado y comprueba staging, rama, contenido del commit y estado limpio. Sprints posteriores amplían escenarios deterministas. Ejecutar pruebas locales solo desde revisiones confiables y revisadas.

Sprint 16 añade ocho pruebas fijas de integración para resultados de proyectos, incluidos estados intermedios, conflicto esperado e instantáneas confirmadas inválidas. Ejecutan en repositorios temporales aislados y orígenes bare locales; las pruebas no extraen ni ejecutan Markdown ni entregas de estudiantes. Flujos alojados permanecen simulaciones no ejecutadas. Ejecuta suite completa e inspecciona logs reales Ubuntu/Windows del SHA más reciente.

CI usa runners estándar hospedados por GitHub Linux y Windows en pull_request y pushes a main, con permisos contents de solo lectura, actions oficiales fijadas por SHA, sin credenciales persistidas de checkout, sin secretos, sin runners propios y sin servicio de pago. Cada job limitado a diez minutos. Código de PR sigue siendo no confiable; runners desechables no son entornos privilegiados de despliegue. Comprobar runs reales en última revisión; checks obligatorios requieren aprobación separada tras observar nombres.

- [Estructura del proyecto](project-structure.es.md)
- [GitHub Actions security](https://docs.github.com/en/actions/reference/security/secure-use)

El check assessment-pilot verifica cuatro bancos versionados, conteos exactos por dificultad, IDs globalmente únicos, prerrequisitos y referencias de simulacros válidos, campos localizados, opciones, respuestas, predicados de estado permitidos e igualdad con Markdown generado. Edita records.json, prepara JSON y currículo, ejecuta python scripts/render_assessments.py --write; prepara páginas generadas y ejecuta python scripts/validate.py --check assessment-pilot y todos checks/pruebas. Los 12 escenarios fijos QA ejercitan estados Git válidos e incorrectos representativos. Ningún evaluador ejecuta entregas de estudiantes ni lee repos arbitrarios; solo fixtures desechables confiables. Validación estructural no demuestra traducción semántica ni precisión educativa.

- [Esquema del piloto de evaluaciones](assessment-pilot.es.md)

El validador learning-hub-contract reconstruye manifesto desde registro curricular, índices localizados, rutas rastreadas y bancos canónicos. Comprueba versiones exactas, JSON estricto, títulos, navegación global y relaciones tipadas. Tras editar fuentes, prepara fuentes y ejecuta python scripts/learning_hub_contract.py --write; prepara resultado y ejecuta checks/pruebas. Doce pruebas contrato/consumidor incluyen manifestos y locks inválidos, idiomas ausentes, rutas inválidas, IDs duplicados, refs pendientes, esquema distinto, instantáneas mezcladas, symlinks, revisión inmutable y rollback. Esquemas estructurales publicados como especificaciones de intercambio; validador semántico biblioteca estándar es gate repo, no motor JSON Schema genérico. Renderizado/runtime sitio y bases Git hostiles están fuera de pruebas.

- [Contrato de integración Learning Hub](specs/project-foundation/integration-contract.es.md)

## Estandarización del workflow (Sprint 19)

Mantener matrix completa Ubuntu/Windows, nombres exactos de checks requeridos, SHA fijos de Actions, permiso contents de solo lectura, timeout de 10 minutos y ambos disparadores automáticos existentes. Añadir workflow_dispatch para revalidación manual en ref seleccionada (disponible cuando workflow exista en rama predeterminada). Grupos de concurrencia usan nombre del workflow más ref de merge del PR para pull requests e IDs únicos de ejecución para otros eventos. Solo ejecución sustituida dentro del mismo grupo de PR puede cancelarse; ejecuciones post-merge de main y manuales son independientes, preservando evidencia. Ejecución cancelada no es aprobación: exigir checks terminados exitosamente en SHA previsto más reciente, luego inspeccionar logs y Codex Review. Sin nuevo runner, job duplicado específico de proyecto, dependencia ni cambio administrativo. Job separado File Organizer Windows del Python Study Guide es específico del proyecto de manipulación de archivos; su workflow queda intacto. Estándares comunes son garantías equivalentes de calidad, no pipelines idénticos.

[Sintaxis y concurrencia de workflows GitHub](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)
