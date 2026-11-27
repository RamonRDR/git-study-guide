# 05 Historial y comparación

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../04-commits-and-tags/README.es.md) · [Índice](../README.es.md) · [Siguiente](../06-branch-management/README.es.md)
<!-- /navigation -->

Generado a partir del JSON canónico. Edita los registros, no esta página.

Las entradas describen comandos y operaciones, no una secuencia para ejecutar. Practica en repositorios desechables. Las operaciones alojadas son opcionales.

**Total de entradas distintas: 10**

- [`git log`](#git-log)
- [`git log --graph`](#git-log-graph)
- [`git log -- path`](#git-log-path)
- [`git show`](#git-show)
- [`git diff`](#git-diff)
- [`git diff --cached`](#git-diff-cached)
- [`git diff A B`](#git-diff-two-revisions)
- [`git diff --stat`](#git-diff-stat)
- [`git diff A...B`](#git-diff-three-dot)
- [`git range-diff`](#git-range-diff)

## git-log

**`git log`**

**Tipo:** Comando nativo

**Nivel:** Principiante

**Buscar por intención:** Inspeccionar historial

**Riesgo:** Solo lectura. Solo lectura con la configuración mostrada; la salida puede contener rutas, mensajes o contenido privados. Usa un repositorio local confiable y revisa antes de compartir.

**Finalidad:** Inspeccionar commits alcanzables desde una revisión inicial, normalmente HEAD.

**Requisitos previos:** Usa un repositorio de práctica confiable con los commits referenciados disponibles localmente.

**Opciones:** -5 limita la cantidad de commits mostrados; --oneline muestra IDs abreviados y asuntos.

**Cuándo utilizar:** Al investigar qué se registró y por quién.

**Cuándo evitar:** No uses el log predeterminado para inferir todas las ramas o ediciones sin confirmar.

**Sintaxis**

`git log -5`

**Ejemplo básico**

`git log -3`

Inspecciona tres commits recientes en un historial de práctica.

**Ejemplo profesional**

`git log --oneline main..feature`

Inspecciona commits alcanzables desde la rama local feature pero no desde main; ambas deben existir.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Se muestran metadatos de commits del historial alcanzable seleccionado; puede abrirse un paginador.

**Efectos y efectos secundarios:** Con la visualización interna normal, no se modifican archivos de trabajo, index, referencias de commits ni remoto.

**Errores comunes:** Suponer que el log predeterminado incluye commits inalcanzables o todas las ramas remotas.

**Alternativas:** Usa git show para un commit o git reflog para investigar movimientos de referencias locales.

**Recuperación:** No hace falta recuperar el repositorio tras la inspección; comprueba revisiones o rutas seleccionadas y repite la comparación si es necesario.

**Versión y dependencias:** Usa Git estándar en un repositorio local confiable; no requiere visor opcional. Puede abrirse un paginador configurado.

**Capítulos relacionados**

- [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.es.md)
- [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-log>

## git-log-graph

**`git log --graph`**

**Tipo:** Uso de opción

**Nivel:** Intermedio

**Buscar por intención:** Inspeccionar historial, Gestionar ramas

**Riesgo:** Solo lectura. Solo lectura con la configuración mostrada; la salida puede contener rutas, mensajes o contenido privados. Usa un repositorio local confiable y revisa antes de compartir.

**Finalidad:** Visualizar relaciones de padres y divergencias en el historial de commits.

**Requisitos previos:** Usa un repositorio de práctica confiable con los commits referenciados disponibles localmente.

**Opciones:** --graph dibuja líneas de ascendencia; --oneline condensa cada commit; --all parte de referencias locales y HEAD.

**Cuándo utilizar:** Al revisar topología de ramas e historial de merges.

**Cuándo evitar:** No trates la posición de columnas o separación vertical como cronología exacta.

**Sintaxis**

`git log --oneline --graph --all`

**Ejemplo básico**

`git log --oneline --graph`

Visualiza la ascendencia de la rama actual.

**Ejemplo profesional**

`git log --oneline --graph --all --decorate`

Revisa la topología local de ramas y etiquetas antes de integrar trabajo.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Un grafo textual muestra commits seleccionados y conexiones de padres.

**Efectos y efectos secundarios:** Con la visualización interna normal, no se modifican archivos de trabajo, index, referencias de commits ni remoto.

**Errores comunes:** Suponer que --all obtiene estado remoto o incluye objetos inalcanzables.

**Alternativas:** Usa git merge-base para un ancestro común o git log sin grafo para mensajes detallados.

**Recuperación:** No hace falta recuperar el repositorio tras la inspección; comprueba revisiones o rutas seleccionadas y repite la comparación si es necesario.

**Versión y dependencias:** Usa Git estándar en un repositorio local confiable; no requiere visor opcional. Puede abrirse un paginador configurado.

**Capítulos relacionados**

- [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.es.md)
- [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.es.md)
- [branches/02-start-points-and-comparison](../../branches/02-start-points-and-comparison/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-log>

## git-log-path

**`git log -- path`**

**Tipo:** Uso de opción

**Nivel:** Intermedio

**Buscar por intención:** Inspeccionar historial, Inspeccionar archivos

**Riesgo:** Solo lectura. Solo lectura con la configuración mostrada; la salida puede contener rutas, mensajes o contenido privados. Usa un repositorio local confiable y revisa antes de compartir.

**Finalidad:** Inspeccionar historial seleccionado por cambios en una ruta concreta.

**Requisitos previos:** Usa un repositorio de práctica confiable con los commits referenciados disponibles localmente.

**Opciones:** -- separa revisiones de rutas; --follow sigue el historial más allá de renombrados para un solo archivo con limitaciones.

**Cuándo utilizar:** Al investigar la evolución de un archivo o directorio concreto.

**Cuándo evitar:** No supongas que la simplificación predeterminada lista cada merge relevante o sigue cada renombrado.

**Sintaxis**

`git log -- notes.txt`

**Ejemplo básico**

`git log -- notes.txt`

Inspecciona cambios en un archivo ficticio de notas rastreado.

**Ejemplo profesional**

`git log --follow -- docs/setup.md`

Investiga un solo archivo de documentación a través de renombrados detectados.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Muestra commits seleccionados por reglas de historial de ruta y simplificación, no ediciones actuales sin confirmar.

**Efectos y efectos secundarios:** Con la visualización interna normal, no se modifican archivos de trabajo, index, referencias de commits ni remoto.

**Errores comunes:** Omitir -- cuando un nombre de ruta también puede nombrar una revisión.

**Alternativas:** Usa git blame para atribución por línea o git log --full-history con una ruta al investigar merges.

**Recuperación:** No hace falta recuperar el repositorio tras la inspección; comprueba revisiones o rutas seleccionadas y repite la comparación si es necesario.

**Versión y dependencias:** Usa Git estándar en un repositorio local confiable; no requiere visor opcional. Puede abrirse un paginador configurado.

**Capítulos relacionados**

- [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.es.md)
- [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-log>

## git-show

**`git show`**

**Tipo:** Comando nativo

**Nivel:** Principiante

**Buscar por intención:** Inspeccionar historial, Revisar cambios, Inspeccionar objetos Git

**Riesgo:** Solo lectura. Solo lectura con el diff interno; revisa la salida sensible y evita controladores externos de diff, filtros de conversión de texto o paginadores no confiables.

**Finalidad:** Mostrar un objeto Git; para un commit ordinario incluye metadatos y parche de forma predeterminada.

**Requisitos previos:** Usa un repositorio de práctica confiable con los commits referenciados disponibles localmente.

**Opciones:** --stat resume cambios; revision:path selecciona un blob en una ruta histórica.

**Cuándo utilizar:** Al revisar un commit, etiqueta o instantánea histórica de archivo concreto.

**Cuándo evitar:** No supongas que mostrar un merge presenta diferencias de todos los padres por defecto.

**Sintaxis**

`git show HEAD`

**Ejemplo básico**

`git show HEAD`

Revisa el último cambio confirmado.

**Ejemplo profesional**

`git show HEAD:notes.txt`

Inspecciona el contenido confirmado de un archivo ficticio sin hacer checkout.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Muestra el objeto solicitado en una representación adecuada a su tipo; HEAD es el valor predeterminado.

**Efectos y efectos secundarios:** Con la visualización interna normal, no se modifican archivos de trabajo, index, referencias de commits ni remoto.

**Errores comunes:** Confundir git show HEAD:path con el archivo de trabajo actual.

**Alternativas:** Usa git diff para dos instantáneas o git cat-file para inspección de objetos de bajo nivel.

**Recuperación:** No hace falta recuperar el repositorio tras la inspección; comprueba revisiones o rutas seleccionadas y repite la comparación si es necesario.

**Versión y dependencias:** Usa Git estándar en un repositorio local confiable; no requiere visor opcional. Puede abrirse un paginador configurado.

**Capítulos relacionados**

- [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.es.md)
- [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.es.md)
- [git-internals/02-blobs-and-trees](../../git-internals/02-blobs-and-trees/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-show>

## git-diff

**`git diff`**

**Tipo:** Comando nativo

**Nivel:** Principiante

**Buscar por intención:** Comparar cambios, Revisar cambios

**Riesgo:** Cambio de estado. Operación de inspección con posibles escrituras en metadatos del index, no una operación de preparación; evita controladores externos de diff no confiables y revisa la salida sensible antes de compartir.

**Finalidad:** Comparar contenido rastreado del working tree con el index.

**Requisitos previos:** Usa un repositorio de práctica confiable con working tree e index; revisa git status primero.

**Opciones:** -- separa opciones y revisiones de rutas; --stat resume cambios.

**Cuándo utilizar:** Antes de preparar cambios, para revisar diferencias no preparadas.

**Cuándo evitar:** No dependas solo de esta forma para revisar cambios preparados o archivos no rastreados.

**Sintaxis**

`git diff -- notes.txt`

**Ejemplo básico**

`git diff`

Revisa una edición rastreada no preparada.

**Ejemplo profesional**

`git diff -- notes.txt`

Revisa un archivo rastreado antes de prepararlo.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Condicional
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Muestra diferencias no preparadas de rutas rastreadas; una salida vacía puede indicar ausencia de esas diferencias.

**Efectos y efectos secundarios:** Archivos de trabajo, IDs de blobs preparados, referencias de commits y remoto permanecen sin cambios con el comportamiento interno; diff.autoRefreshIndex puede actualizar metadatos stat de archivos en el index.

**Errores comunes:** Suponer que un diff vacío significa que todo el repositorio está limpio.

**Alternativas:** Usa git diff --cached para cambios preparados y git status para archivos no rastreados.

**Recuperación:** No hace falta recuperar el repositorio tras la inspección; comprueba revisiones o rutas seleccionadas y repite la comparación si es necesario.

**Versión y dependencias:** Usa Git estándar en un repositorio local confiable; no requiere visor opcional. Puede abrirse un paginador configurado.

**Capítulos relacionados**

- [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.es.md)
- [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-diff>
- <https://git-scm.com/docs/git-config/2.36.3.html>

## git-diff-cached

**`git diff --cached`**

**Tipo:** Uso de opción

**Nivel:** Principiante

**Buscar por intención:** Comparar cambios, Revisar cambios, Preparar cambios

**Riesgo:** Solo lectura. Solo lectura con el diff interno; revisa la salida sensible y evita controladores externos de diff, filtros de conversión de texto o paginadores no confiables.

**Finalidad:** Comparar index con HEAD para revisar cambios preparados.

**Requisitos previos:** Usa un repositorio de práctica confiable con working tree e index; revisa git status primero.

**Opciones:** --staged es sinónimo de --cached; -- seguido de una ruta limita la salida.

**Cuándo utilizar:** Inmediatamente antes de confirmar la instantánea preparada.

**Cuándo evitar:** No uses esta forma para inspeccionar cambios posteriores a la preparación sin prepararlos de nuevo.

**Sintaxis**

`git diff --cached`

**Ejemplo básico**

`git diff --cached`

Inspecciona cambios ya seleccionados para commit.

**Ejemplo profesional**

`git diff --cached -- notes.txt`

Confirma que solo la parte deseada de un archivo parcialmente preparado está en el index.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Muestra la diferencia preparada respecto a HEAD; en una rama sin primer commit muestra todos los cambios preparados si no se proporciona un commit.

**Efectos y efectos secundarios:** Con la visualización interna normal, no se modifican archivos de trabajo, index, referencias de commits ni remoto.

**Errores comunes:** Confundir diferencias del caché con diferencias del working tree.

**Alternativas:** Usa git diff para ver lo que aún no está preparado o git status para inspeccionar ambos estados.

**Recuperación:** No hace falta recuperar el repositorio tras la inspección; comprueba revisiones o rutas seleccionadas y repite la comparación si es necesario.

**Versión y dependencias:** Usa Git estándar en un repositorio local confiable; no requiere visor opcional. Puede abrirse un paginador configurado.

**Capítulos relacionados**

- [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.es.md)
- [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-diff>

## git-diff-two-revisions

**`git diff A B`**

**Tipo:** Uso de opción

**Nivel:** Intermedio

**Buscar por intención:** Comparar cambios, Revisar cambios

**Riesgo:** Solo lectura. Solo lectura con el diff interno; revisa la salida sensible y evita controladores externos de diff, filtros de conversión de texto o paginadores no confiables.

**Finalidad:** Comparar directamente dos instantáneas confirmadas, independientemente de su ascendencia.

**Requisitos previos:** Usa un repositorio de práctica confiable con los commits referenciados disponibles localmente.

**Opciones:** Proporciona dos revisiones; A..B es equivalente en git diff, a diferencia de un rango de commits en git log.

**Cuándo utilizar:** Al comprobar diferencias de estado final entre ramas, etiquetas o commits.

**Cuándo evitar:** Evita interpretar esto como lista de commits individuales o solo cambios introducidos por feature.

**Sintaxis**

`git diff main feature`

**Ejemplo básico**

`git diff HEAD~1 HEAD`

Compara un commit no inicial con su primer padre.

**Ejemplo profesional**

`git diff main feature`

Compara las puntas de ramas locales main y feature existentes.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Muestra el parche de la primera instantánea a la segunda; invertir entradas invierte la comparación.

**Efectos y efectos secundarios:** Con la visualización interna normal, no se modifican archivos de trabajo, index, referencias de commits ni remoto.

**Errores comunes:** Tratar la sintaxis de dos puntos en diff como conjunto de revisiones igual a git log A..B.

**Alternativas:** Usa git diff A...B para comparar desde una base de merge hasta B o git log A..B para listar commits.

**Recuperación:** No hace falta recuperar el repositorio tras la inspección; comprueba revisiones o rutas seleccionadas y repite la comparación si es necesario.

**Versión y dependencias:** Usa Git estándar en un repositorio local confiable; no requiere visor opcional. Puede abrirse un paginador configurado.

**Capítulos relacionados**

- [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.es.md)
- [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.es.md)
- [branches/02-start-points-and-comparison](../../branches/02-start-points-and-comparison/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-diff>

## git-diff-stat

**`git diff --stat`**

**Tipo:** Uso de opción

**Nivel:** Principiante

**Buscar por intención:** Comparar cambios, Revisar cambios

**Riesgo:** Cambio de estado. Operación de inspección con posibles escrituras en metadatos del index, no una operación de preparación; evita controladores externos de diff no confiables y revisa la salida sensible antes de compartir.

**Finalidad:** Resumir el alcance de un diff por archivos afectados y cantidades de cambios.

**Requisitos previos:** Usa un repositorio de práctica confiable con working tree e index; revisa git status primero.

**Opciones:** --stat solicita un resumen; combina con --cached o dos revisiones para elegir otra comparación.

**Cuándo utilizar:** Al estimar el alcance de revisión antes de leer un parche completo.

**Cuándo evitar:** No trates cantidades de líneas como medida de corrección, complejidad o productividad.

**Sintaxis**

`git diff --stat`

**Ejemplo básico**

`git diff --stat`

Resume cambios no preparados.

**Ejemplo profesional**

`git diff --cached --stat`

Estima el alcance preparado antes de leer el parche.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Condicional
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Muestra resúmenes por archivo y totales de la comparación seleccionada; binarios tienen resúmenes diferentes.

**Efectos y efectos secundarios:** Archivos de trabajo, IDs de blobs preparados, referencias de commits y remoto permanecen sin cambios con el comportamiento interno; diff.autoRefreshIndex puede actualizar metadatos stat de archivos en el index.

**Errores comunes:** Suponer que --stat altera los extremos de comparación o sustituye leer el parche.

**Alternativas:** Usa git diff --name-status para códigos de estado o git diff completo para revisar contenido.

**Recuperación:** No hace falta recuperar el repositorio tras la inspección; comprueba revisiones o rutas seleccionadas y repite la comparación si es necesario.

**Versión y dependencias:** Usa Git estándar en un repositorio local confiable; no requiere visor opcional. Puede abrirse un paginador configurado.

**Capítulos relacionados**

- [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.es.md)
- [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-diff>
- <https://git-scm.com/docs/git-config/2.36.3.html>

## git-diff-three-dot

**`git diff A...B`**

**Tipo:** Uso de opción

**Nivel:** Intermedio

**Buscar por intención:** Comparar cambios, Revisar cambios, Inspeccionar historial

**Riesgo:** Solo lectura. Solo lectura con el diff interno; revisa la salida sensible y evita controladores externos de diff, filtros de conversión de texto o paginadores no confiables.

**Finalidad:** Comparar la instantánea de una base de merge de A y B con la instantánea de B.

**Requisitos previos:** Usa un repositorio local confiable con ambas referencias y ancestro común adecuado; verifica primero la base de merge.

**Opciones:** Tres puntos seleccionan una base de merge como primer extremo; la revisión derecha es el segundo extremo.

**Cuándo utilizar:** Al revisar cambios de rama respecto a un ancestro común, especialmente tras divergencia.

**Cuándo evitar:** Evita suponer simetría o identidad con diff de PR alojado; inspecciona bases de merge ambiguas.

**Sintaxis**

`git diff main...feature`

**Ejemplo básico**

`git diff main...feature`

Revisa una rama feature local existente respecto a su base común con main.

**Ejemplo profesional**

`git diff main...feature -- notes.txt`

Revisa cambios de rama en un archivo ficticio tras comprobar la base de merge.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Muestra la diferencia neta de la base común seleccionada a la instantánea derecha, no cambios exclusivos de la rama izquierda.

**Efectos y efectos secundarios:** Con la visualización interna normal, no se modifican archivos de trabajo, index, referencias de commits ni remoto.

**Errores comunes:** Confundir git diff A...B con diferencia simétrica de conjuntos de commits en git log A...B.

**Alternativas:** Usa git diff A B para comparar puntas o inspecciona git merge-base --all A B antes de seleccionar base explícita.

**Recuperación:** No hace falta recuperar el repositorio tras la inspección; comprueba revisiones o rutas seleccionadas y repite la comparación si es necesario.

**Versión y dependencias:** Usa Git estándar en un repositorio local confiable; no requiere visor opcional. Puede abrirse un paginador configurado.

**Capítulos relacionados**

- [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.es.md)
- [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.es.md)
- [branches/02-start-points-and-comparison](../../branches/02-start-points-and-comparison/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-diff>

## git-range-diff

**`git range-diff`**

**Tipo:** Comando nativo

**Nivel:** Avanzado

**Buscar por intención:** Comparar cambios, Revisar cambios, Reescribir historial local

**Riesgo:** Solo lectura. Solo lectura con el diff interno; revisa la salida sensible y evita controladores externos de diff, filtros de conversión de texto o paginadores no confiables.

**Finalidad:** Comparar parches y mensajes de dos versiones de una serie de commits.

**Requisitos previos:** Usa un repositorio local confiable con ambos rangos de commits no vacíos; conserva la punta anterior antes de reescribir historial.

**Opciones:** Proporciona dos rangos explícitos de revisiones; --no-color desactiva colores para leer salida simple.

**Cuándo utilizar:** Al revisar cambios en una serie privada de parches tras correcciones o rebase.

**Cuándo evitar:** No lo uses como prueba de equivalencia semántica o API estable para máquinas; los merges se ignoran por defecto.

**Sintaxis**

`git range-diff main..old-series main..feature`

**Ejemplo básico**

`git range-diff main..old-series main..feature`

Compara dos series locales existentes basadas en main.

**Ejemplo profesional**

`git range-diff --no-color main..old-series main..feature`

Revisa una serie guardada antes de rebase contra su versión revisada; confirma cambios reales por separado.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Muestra correspondencia aproximada entre commits y cambios en parches y metadatos; identifica commits sin correspondencia.

**Efectos y efectos secundarios:** Con la visualización interna normal, no se modifican archivos de trabajo, index, referencias de commits ni remoto.

**Errores comunes:** Comparar solo instantáneas finales y perder cambios individuales, o confiar en correspondencia como prueba de corrección.

**Alternativas:** Usa git diff entre ambas puntas para comparar contenido final y ejecuta pruebas pertinentes.

**Recuperación:** No hace falta recuperar el repositorio tras la inspección; comprueba revisiones o rutas seleccionadas y repite la comparación si es necesario.

**Versión y dependencias:** Requiere Git 2.19 o superior; usa configuración local confiable. La salida se destina a humanos, no a un parser estable.

**Capítulos relacionados**

- [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.es.md)
- [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.es.md)
- [merge-and-conflicts/07-interactive-rebase](../../merge-and-conflicts/07-interactive-rebase/README.es.md)
- [professional-workflows/08-code-review](../../professional-workflows/08-code-review/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-range-diff>


---

<!-- navigation-footer -->
[Anterior](../04-commits-and-tags/README.es.md) · [Índice](../README.es.md) · [Siguiente](../06-branch-management/README.es.md)
<!-- /navigation-footer -->
