# 02 Inspección del repositorio

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../01-setup-and-configuration/README.es.md) · [Índice](../README.es.md) · [Siguiente](../03-working-tree-and-staging/README.es.md)
<!-- /navigation -->

Generado a partir del JSON canónico. Edita los registros, no esta página.

Las entradas describen comandos y operaciones, no una secuencia para ejecutar. Practica en repositorios desechables. Las operaciones alojadas son opcionales.

**Total de entradas distintas: 9**

- [`git status`](#git-status)
- [`git status --porcelain`](#git-status-porcelain)
- [`git rev-parse --show-toplevel`](#git-rev-parse-show-toplevel)
- [`git rev-parse --git-dir`](#git-rev-parse-git-dir)
- [`git rev-parse --is-bare-repository`](#git-rev-parse-is-bare)
- [`git ls-files`](#git-ls-files)
- [`git check-ignore`](#git-check-ignore)
- [`git show-ref`](#git-show-ref)
- [`git count-objects`](#git-count-objects)

## git-status

**`git status`**

**Tipo:** Comando nativo

**Nivel:** Principiante

**Buscar por intención:** Inspeccionar estado del repositorio

**Riesgo:** Cambio de estado. Inspecciona el resultado en privado; nombres de archivos, rutas o historial pueden revelar información del proyecto.

**Finalidad:** Resumir cambios preparados, no preparados y archivos no rastreados.

**Requisitos previos:** Usa un repositorio propio desechable; ejecuta desde su directorio de trabajo.

**Opciones:** --short da estado compacto; --branch añade información de rama.

**Cuándo utilizar:** Antes de preparar, confirmar o cambiar de rama.

**Cuándo evitar:** No tomes un estado limpio como prueba de pruebas aprobadas o sincronización remota.

**Sintaxis**

`git status [--short]`

**Ejemplo básico**

`git status`

Inspecciona el informe completo antes de preparar un archivo modificado.

**Ejemplo profesional**

`git status --short`

Revisa un informe compacto antes de entregar a revisión de código.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Condicional
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Informa rutas por estado; un árbol limpio no tiene cambios visibles pendientes.

**Efectos y efectos secundarios:** Puede refrescar metadatos stat del index sin cambiar contenido preparado; no modifica commits.

**Errores comunes:** Interpretar mal las dos columnas del estado corto; los ignorados suelen ocultarse.

**Alternativas:** Usa git diff y git diff --cached para inspeccionar cambios reales.

**Recuperación:** No hace falta recuperar historial; corrige el contexto y repite la inspección.

**Versión y dependencias:** Sin herramienta opcional; los ejemplos usan sintaxis tradicional de Git.

**Capítulos relacionados**

- [basic-commands/02-status-add-commit](../../basic-commands/02-status-add-commit/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-status>

## git-status-porcelain

**`git status --porcelain`**

**Tipo:** Uso de opción

**Nivel:** Intermedio

**Buscar por intención:** Automatizar flujo

**Riesgo:** Cambio de estado. Inspecciona el resultado en privado; nombres de archivos, rutas o historial pueden revelar información del proyecto.

**Finalidad:** Inspeccionar estado del working tree e index en formato para máquinas.

**Requisitos previos:** Usa un repositorio propio desechable; ejecuta desde su directorio de trabajo.

**Opciones:** --porcelain=v1 selecciona formato v1 estable; -z usa terminadores NUL.

**Cuándo utilizar:** Cuando scripts necesitan salida de estado reproducible.

**Cuándo evitar:** No analices salida humana ni separes registros NUL por espacios.

**Sintaxis**

`git status --porcelain[=v1] [-z]`

**Ejemplo básico**

`git status --porcelain=v1`

Compara el informe v1 con git status normal.

**Ejemplo profesional**

`git status --porcelain=v1 -z`

Captura registros NUL como bytes para comprobación previa; no los imprimas como texto.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Condicional
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Emite estado compacto legible por máquina; informe vacío indica ausencia de cambios informados.

**Efectos y efectos secundarios:** Puede refrescar metadatos stat del index; no prepara contenido ni mueve refs.

**Errores comunes:** Esperar código distinto de cero para árbol sucio; ignorar formato de renombrado.

**Alternativas:** Usa git diff --quiet para comparación específica rastreada; no incluye no rastreados.

**Recuperación:** No hace falta recuperar historial; corrige el contexto y repite la inspección.

**Versión y dependencias:** Sin herramienta opcional; los ejemplos usan sintaxis tradicional de Git.

**Capítulos relacionados**

- [git-architecture/03-file-states](../../git-architecture/03-file-states/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-status>

## git-rev-parse-show-toplevel

**`git rev-parse --show-toplevel`**

**Tipo:** Uso de opción

**Nivel:** Principiante

**Buscar por intención:** Inspeccionar estado del repositorio

**Riesgo:** Solo lectura. Inspecciona el resultado en privado; nombres de archivos, rutas o historial pueden revelar información del proyecto.

**Finalidad:** Encontrar la raíz del working tree actual.

**Requisitos previos:** Usa un repositorio propio desechable; ejecuta desde su directorio de trabajo.

**Opciones:** --show-toplevel informa la ruta raíz; -C cambia el directorio inicial del comando.

**Cuándo utilizar:** Antes de operar en repositorio desde un subdirectorio.

**Cuándo evitar:** No lo uses para localizar working tree en repositorio bare.

**Sintaxis**

`git rev-parse --show-toplevel`

**Ejemplo básico**

`git rev-parse --show-toplevel`

Confirma la raíz antes de inspeccionar archivos.

**Ejemplo profesional**

`git -C src rev-parse --show-toplevel`

Si src existe, confirma qué repositorio usaría una herramienta allí.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Imprime la ruta raíz o falla si no está disponible.

**Efectos y efectos secundarios:** Lee información de descubrimiento sin modificar refs ni archivos.

**Errores comunes:** Suponer que el directorio actual del shell siempre es la raíz.

**Alternativas:** Usa git rev-parse --git-dir para localizar metadatos Git.

**Recuperación:** No hace falta recuperar historial; corrige el contexto y repite la inspección.

**Versión y dependencias:** Sin herramienta opcional; los ejemplos usan sintaxis tradicional de Git.

**Capítulos relacionados**

- [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-rev-parse>

## git-rev-parse-git-dir

**`git rev-parse --git-dir`**

**Tipo:** Uso de opción

**Nivel:** Intermedio

**Buscar por intención:** Inspeccionar estado del repositorio

**Riesgo:** Solo lectura. Inspecciona el resultado en privado; nombres de archivos, rutas o historial pueden revelar información del proyecto.

**Finalidad:** Localizar metadatos sin suponer que .git es un directorio.

**Requisitos previos:** Usa un repositorio propio desechable; ejecuta desde su directorio de trabajo.

**Opciones:** --git-dir puede informar ruta relativa; --absolute-git-dir solicita ruta absoluta.

**Cuándo utilizar:** Diagnosticar worktrees, submódulos o repositorios bare.

**Cuándo evitar:** No edites metadatos directamente a partir de ese resultado.

**Sintaxis**

`git rev-parse --git-dir`

**Ejemplo básico**

`git rev-parse --git-dir`

Inspecciona la ruta de metadatos en un clon normal.

**Ejemplo profesional**

`git rev-parse --absolute-git-dir`

Comprueba ruta absoluta de metadatos al diagnosticar un worktree vinculado.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Informa el directorio Git de este contexto.

**Efectos y efectos secundarios:** Lee ubicación de metadatos; sin cambios de estado.

**Errores comunes:** Confundir directorio Git por worktree con el directorio común compartido.

**Alternativas:** Usa git rev-parse --git-common-dir para inspeccionar ubicación compartida.

**Recuperación:** No hace falta recuperar historial; corrige el contexto y repite la inspección.

**Versión y dependencias:** Sin herramienta opcional; los ejemplos usan sintaxis tradicional de Git.

**Capítulos relacionados**

- [git-internals/01-object-database](../../git-internals/01-object-database/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-rev-parse>

## git-rev-parse-is-bare

**`git rev-parse --is-bare-repository`**

**Tipo:** Uso de opción

**Nivel:** Intermedio

**Buscar por intención:** Inspeccionar estado del repositorio

**Riesgo:** Solo lectura. Inspecciona el resultado en privado; nombres de archivos, rutas o historial pueden revelar información del proyecto.

**Finalidad:** Determinar si Git considera el repositorio bare.

**Requisitos previos:** Usa un repositorio propio desechable; ejecuta desde su directorio de trabajo.

**Opciones:** --is-bare-repository imprime booleano; -C selecciona directorio.

**Cuándo utilizar:** Antes de intentar comandos de working tree en origin local.

**Cuándo evitar:** No deduzcas permiso de escritura ni acceso remoto del resultado bare.

**Sintaxis**

`git rev-parse --is-bare-repository`

**Ejemplo básico**

`git rev-parse --is-bare-repository`

Comprueba repositorio normal; espera false.

**Ejemplo profesional**

`git -C origin.git rev-parse --is-bare-repository`

Desde padre desechable con origin.git, confirma que origin es bare.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Imprime true o false para contexto válido.

**Efectos y efectos secundarios:** No cambia configuración ni contenido del repositorio.

**Errores comunes:** Tomar false como prueba de que el directorio actual es la raíz.

**Alternativas:** Usa git rev-parse --is-inside-work-tree para probar contexto de working tree.

**Recuperación:** No hace falta recuperar historial; corrige el contexto y repite la inspección.

**Versión y dependencias:** Sin herramienta opcional; los ejemplos usan sintaxis tradicional de Git.

**Capítulos relacionados**

- [remote-repositories/01-remote-concepts](../../remote-repositories/01-remote-concepts/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-rev-parse>

## git-ls-files

**`git ls-files`**

**Tipo:** Comando nativo

**Nivel:** Intermedio

**Buscar por intención:** Inspeccionar archivos

**Riesgo:** Solo lectura. Inspecciona el resultado en privado; nombres de archivos, rutas o historial pueden revelar información del proyecto.

**Finalidad:** Listar rutas indexadas u otras rutas seleccionadas del working tree.

**Requisitos previos:** Usa un repositorio propio desechable; ejecuta desde su directorio de trabajo.

**Opciones:** --stage muestra entradas del index; --others enumera no rastreados; --exclude-standard aplica reglas comunes de ignore.

**Cuándo utilizar:** Auditar rutas rastreadas o identificar candidatos no rastreados sin preparar.

**Cuándo evitar:** No interpretes rutas del index como prueba de que existen los archivos de trabajo.

**Sintaxis**

`git ls-files [--stage] [--others --exclude-standard]`

**Ejemplo básico**

`git ls-files`

Enumera rutas indexadas después de preparar un archivo.

**Ejemplo profesional**

`git ls-files --others --exclude-standard`

Inspecciona rutas no rastreadas ni ignoradas antes de empaquetar archivos.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Lista rutas del modo seleccionado; por defecto lista rutas rastreadas del index.

**Efectos y efectos secundarios:** Lee index y posiblemente working tree sin preparar cambios.

**Errores comunes:** Esperar archivos ignorados en una lista con --exclude-standard.

**Alternativas:** Usa git status para vista general y git ls-tree para árbol confirmado.

**Recuperación:** No hace falta recuperar historial; corrige el contexto y repite la inspección.

**Versión y dependencias:** Sin herramienta opcional; los ejemplos usan sintaxis tradicional de Git.

**Capítulos relacionados**

- [git-architecture/03-file-states](../../git-architecture/03-file-states/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-ls-files>

## git-check-ignore

**`git check-ignore`**

**Tipo:** Comando nativo

**Nivel:** Intermedio

**Buscar por intención:** Ignorar archivos

**Riesgo:** Solo lectura. Inspecciona el resultado en privado; nombres de archivos, rutas o historial pueden revelar información del proyecto.

**Finalidad:** Explicar si una ruta coincide con reglas de ignore y cuál se aplica.

**Requisitos previos:** Usa un repositorio propio desechable; ejecuta desde su directorio de trabajo.

**Opciones:** -v informa origen y patrón; --no-index omite la comprobación usual de ruta rastreada.

**Cuándo utilizar:** Diagnosticar ruta inesperadamente ausente del estado de no rastreados.

**Cuándo evitar:** No supongas que ruta ignorada está protegida contra acceso o eliminada del historial.

**Sintaxis**

`git check-ignore [-v] [--no-index] pathname`

**Ejemplo básico**

`git check-ignore notes.tmp`

Crea regla desechable para notes.tmp y comprueba coincidencia.

**Ejemplo profesional**

`git check-ignore -v build/output.log`

Explica qué patrón de ignore excluye un log de build ilustrativo.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Informa rutas ignoradas coincidentes; código de salida distingue coincidencia, ausencia y errores.

**Efectos y efectos secundarios:** Lee reglas de ignore e index sin cambiar contenido rastreado.

**Errores comunes:** Esperar que check-ignore normal informe rutas ya rastreadas.

**Alternativas:** Usa git status --ignored para inspeccionar rutas ignoradas en general.

**Recuperación:** No hace falta recuperar historial; corrige el contexto y repite la inspección.

**Versión y dependencias:** Sin herramienta opcional; los ejemplos usan sintaxis tradicional de Git.

**Capítulos relacionados**

- [basic-commands/05-ignore-and-review](../../basic-commands/05-ignore-and-review/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-check-ignore>

## git-show-ref

**`git show-ref`**

**Tipo:** Comando nativo

**Nivel:** Intermedio

**Buscar por intención:** Inspeccionar referencias

**Riesgo:** Solo lectura. Inspecciona el resultado en privado; nombres de archivos, rutas o historial pueden revelar información del proyecto.

**Finalidad:** Inspeccionar referencias locales e IDs de objetos.

**Requisitos previos:** Usa un repositorio propio desechable; ejecuta desde su directorio de trabajo.

**Opciones:** --heads limita a refs de ramas; --tags limita etiquetas; --verify exige ruta exacta.

**Cuándo utilizar:** Verificar referencia antes de operación que depende de ella.

**Cuándo evitar:** No interpretes refs locales de seguimiento remoto como estado remoto en vivo.

**Sintaxis**

`git show-ref [--heads] [--tags]`

**Ejemplo básico**

`git show-ref --heads`

Enumera refs locales después del primer commit.

**Ejemplo profesional**

`git show-ref --verify refs/heads/main`

Verifica ref exacta main en repositorio de integración desechable.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Imprime IDs y nombres coincidentes; verificación falla si falta ref exacta.

**Efectos y efectos secundarios:** Lee refs sin crearlas ni moverlas.

**Errores comunes:** Usar nombre corto con --verify o comprobar rama sin commit.

**Alternativas:** Usa git for-each-ref para formato personalizado o git ls-remote para refs remotas.

**Recuperación:** No hace falta recuperar historial; corrige el contexto y repite la inspección.

**Versión y dependencias:** Sin herramienta opcional; los ejemplos usan sintaxis tradicional de Git.

**Capítulos relacionados**

- [git-internals/05-refs-and-head](../../git-internals/05-refs-and-head/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-show-ref>

## git-count-objects

**`git count-objects`**

**Tipo:** Comando nativo

**Nivel:** Avanzado

**Buscar por intención:** Inspeccionar objetos Git

**Riesgo:** Solo lectura. Inspecciona el resultado en privado; nombres de archivos, rutas o historial pueden revelar información del proyecto.

**Finalidad:** Medir cantidad de objetos sueltos y estadísticas de almacenamiento.

**Requisitos previos:** Usa un repositorio propio desechable; ejecuta desde su directorio de trabajo.

**Opciones:** -v incluye estadísticas de packs y basura; -H muestra tamaños legibles.

**Cuándo utilizar:** Diagnosticar crecimiento de la base de objetos antes de considerar mantenimiento.

**Cuándo evitar:** No tomes conteos como prueba de corrupción o uso exacto de disco del repositorio entero.

**Sintaxis**

`git count-objects [-v] [-H]`

**Ejemplo básico**

`git count-objects`

Inspecciona conteos tras unos commits locales.

**Ejemplo profesional**

`git count-objects -vH`

Registra estadísticas detalladas antes de proponer mantenimiento en clon desechable.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Informa objetos sueltos y tamaños; salida detallada incluye estadísticas de packs.

**Efectos y efectos secundarios:** Lee almacenamiento de objetos sin podar ni reempaquetar.

**Errores comunes:** Confundir cantidad de objetos sueltos con total de commits.

**Alternativas:** Usa git fsck para diagnóstico de integridad y herramientas del sistema para uso total de disco.

**Recuperación:** No hace falta recuperar historial; corrige el contexto y repite la inspección.

**Versión y dependencias:** Sin herramienta opcional; los ejemplos usan sintaxis tradicional de Git.

**Capítulos relacionados**

- [git-internals/07-loose-objects-and-packfiles](../../git-internals/07-loose-objects-and-packfiles/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-count-objects>


---

<!-- navigation-footer -->
[Anterior](../01-setup-and-configuration/README.es.md) · [Índice](../README.es.md) · [Siguiente](../03-working-tree-and-staging/README.es.md)
<!-- /navigation-footer -->
