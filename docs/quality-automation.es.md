# Automatización de calidad

[English](quality-automation.md) · [Português](quality-automation.pt-BR.md) · [Español](quality-automation.es.md)

Mantenedores necesitan Git (2.28 o superior para la opción initial-branch) y Python 3.12; Python y CI no son requisitos del estudiante. Desde la raíz, añadir archivos nuevos al índice antes de validar, pues checks inspeccionan rutas rastreadas. Ejecutar:

```text
python scripts/validate.py
python -m unittest discover -s tests -v
```

Usar --check con structure, locales, links, navigation, examples, secrets o command-catalog para aislar un check. Validadores inspeccionan rutas rastreadas portables, presencia de tres idiomas, enlaces relativos e imágenes Markdown inline, orden/navegación de módulos y capítulos, política de ejemplos ejecutables y patrones comunes de secretos. No prueban traducción semántica, enlaces externos, anclas, todas las sintaxis Markdown, ausencia de todos los secretos ni comportamiento de UI de plantillas. Detector informa archivo y línea, no valores; es heurístico, no exhaustivo. Revisar diffs y rotar credenciales expuestas por separado.

La validación de navegación exige bloques canónicos localizados de encabezado y pie para cada índice de módulo y capítulo, etiquetas y rutas exactas, transiciones entre capítulos y módulos, ubicación y detección de duplicados. Pruebas incluyen casos negativos de navegación ausente, divergente, reordenada, en idioma incorrecto, invertida, oculta o mal ubicada. Índices previstos siguen navegables; sus lecciones aún no se publicaron.

El check command-catalog valida las 14 categorías JSON registradas, al menos 101 operaciones distintas (objetivo aprobado de 120), mapas de idiomas, riesgos, política de URL de fuentes oficiales, capítulos relacionados, intenciones e igualdad exacta con el renderizador canónico. No ejecuta comandos del catálogo ni demuestra traducción semántica, disponibilidad de URL externas o corrección de cada ejemplo. Para cambiar el catálogo, edita el JSON canónico, prepara nuevas entradas y regenera el Markdown registrado desde la raíz:

```text
python scripts/render_command_reference.py --write
```

Prepara las páginas generadas, ejecuta `python scripts/validate.py --check command-catalog`, luego todos los validadores y pruebas. La invocación predeterminada del renderizador comprueba contenido generado sin escribir.

Aún no hay ejemplos didácticos ejecutables aprobados. El manifiesto vacío bloquea por defecto: todos los archivos en examples/ (incluidos archivos inertes y variantes de mayúsculas/minúsculas) se rechazan, independientemente de extensión o modo, y manifiestos no vacíos fallan hasta contar con protocolo de ejecución revisado. No ejecutar código arbitrario de estudiantes. Prueba inicial Git usa repo temporal aislado y comprueba staging, rama, contenido del commit y estado limpio. Sprints posteriores amplían escenarios deterministas. Ejecutar pruebas locales solo desde revisiones confiables y revisadas.

CI usa runners estándar hospedados por GitHub Linux y Windows en pull_request y pushes a main, con permisos contents de solo lectura, actions oficiales fijadas por SHA, sin credenciales persistidas de checkout, sin secretos, sin runners propios y sin servicio de pago. Cada job limitado a diez minutos. Código de PR sigue siendo no confiable; runners desechables no son entornos privilegiados de despliegue. Comprobar runs reales en última revisión; checks obligatorios requieren aprobación separada tras observar nombres.

- [Estructura del proyecto](project-structure.es.md)
- [GitHub Actions security](https://docs.github.com/en/actions/reference/security/secure-use)
