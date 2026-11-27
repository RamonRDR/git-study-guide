# 10 Búsqueda y diagnóstico

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../09-recovery-and-stash/README.es.md) · [Índice](../README.es.md) · [Siguiente](../11-advanced-git-operations/README.es.md)
<!-- /navigation -->

Generado a partir del JSON canónico. Edita los registros, no esta página.

Las entradas describen comandos y operaciones, no una secuencia para ejecutar. Practica en repositorios desechables. Las operaciones alojadas son opcionales.

**Total de entradas distintas: 8**

- [`git grep`](#git-grep)
- [`git blame`](#git-blame)
- [`git log -S`](#git-log-pickaxe-string)
- [`git log -G`](#git-log-pickaxe-regex)
- [`git log --follow`](#git-log-follow)
- [`git diff --check`](#git-diff-check)
- [`git ls-files --unmerged`](#git-ls-files-unmerged)
- [`git bisect`](#git-bisect)

## git-grep

**`git grep`**

**Tipo:** Comando nativo

**Nivel:** Intermedio

**Buscar por intención:** Buscar contenido

**Riesgo:** Solo lectura. Solo lectura en contexto local ordinario mostrado; evita divulgar salida sensible. Usa configuración confiable y objetos locales completos.

**Finalidad:** Buscar líneas coincidentes en archivos rastreados, index o árboles seleccionados.

**Requisitos previos:** Usa repositorio desechable con archivos y revisiones indicados existentes; comprueba el repositorio y usa configuración confiable.

**Opciones:** -n muestra números de línea; -F usa patrones literales; --cached busca contenido del index; argumento de árbol busca árbol confirmada.

**Cuándo utilizar:** Al localizar símbolo o texto en contenido versionado.

**Cuándo evitar:** No supongas búsqueda predeterminada en archivos ignorados o no rastreados.

**Sintaxis**

`git grep -n -F "TODO"`

**Ejemplo básico**

`git grep -n -F "TODO"`

Encuentra TODO literal en archivos rastreados de práctica.

**Ejemplo profesional**

`git grep -n -F "timeout" HEAD -- src/`

Busca directorio de código confirmado en laboratorio.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Muestra coincidencias con contexto solicitado; salida 1 significa ausencia de coincidencias, no necesariamente error de ejecución.

**Efectos y efectos secundarios:** La inspección mostrada no modifica intencionalmente contenido rastreado, index, referencias ni remoto.

**Errores comunes:** Confundir expresiones regulares con literales o buscar instantánea incorrecta.

**Alternativas:** Usa búsqueda confiable del sistema de archivos para archivos fuera del alcance Git seleccionado.

**Recuperación:** La inspección no requiere deshacer; verifica revisión, ruta, expresión de búsqueda y código de salida antes de interpretar resultados.

**Versión y dependencias:** Sintaxis estándar Git; usa Git 2.40 o superior en laboratorios del guía.

**Capítulos relacionados**

- [advanced-git/09-blame-and-grep](../../advanced-git/09-blame-and-grep/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-grep>

## git-blame

**`git blame`**

**Tipo:** Comando nativo

**Nivel:** Intermedio

**Buscar por intención:** Inspeccionar autoría, Inspeccionar historial

**Riesgo:** Solo lectura. Solo lectura en contexto local ordinario mostrado; evita divulgar salida sensible. Usa configuración confiable y objetos locales completos.

**Finalidad:** Rastrear cada línea seleccionada a la revisión a la que Git la atribuye.

**Requisitos previos:** Usa repositorio desechable con archivos y revisiones indicados existentes; comprueba el repositorio y usa configuración confiable.

**Opciones:** -L limita rangos; -w ignora diferencias de espacios; -M y -C pueden detectar líneas movidas o copiadas con trabajo adicional.

**Cuándo utilizar:** Al investigar contexto de línea antes de cambiar.

**Cuándo evitar:** No uses atribución como prueba de culpa o autoría original de una idea.

**Sintaxis**

`git blame HEAD -- notes.txt`

**Ejemplo básico**

`git blame HEAD -- notes.txt`

Inspecciona atribución de líneas confirmadas de práctica.

**Ejemplo profesional**

`git blame -L 1,10 HEAD -- notes.txt`

Revisa primeras diez líneas del archivo confirmado, si existen.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Muestra commits atribuidos y líneas; resultado depende de revisión y opciones de detección.

**Efectos y efectos secundarios:** La inspección mostrada no modifica intencionalmente contenido rastreado, index, referencias ni remoto.

**Errores comunes:** Suponer que autor atribuido más reciente introdujo problema subyacente.

**Alternativas:** Inspecciona git show e historial anterior para contexto; usa git log -G para líneas cambiadas.

**Recuperación:** La inspección no requiere deshacer; verifica revisión, ruta, expresión de búsqueda y código de salida antes de interpretar resultados.

**Versión y dependencias:** Sintaxis estándar Git; usa Git 2.40 o superior en laboratorios del guía.

**Capítulos relacionados**

- [advanced-git/09-blame-and-grep](../../advanced-git/09-blame-and-grep/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-blame>

## git-log-pickaxe-string

**`git log -S`**

**Tipo:** Uso de opción

**Nivel:** Avanzado

**Buscar por intención:** Buscar contenido, Inspeccionar historial

**Riesgo:** Solo lectura. Solo lectura en contexto local ordinario mostrado; evita divulgar salida sensible. Usa configuración confiable y objetos locales completos.

**Finalidad:** Encontrar commits cuyo diff cambia cantidad de ocurrencias de cadena.

**Requisitos previos:** Usa repositorio desechable con archivos y revisiones indicados existentes; comprueba el repositorio y usa configuración confiable.

**Opciones:** -S usa cadena; --pickaxe-regex cambia interpretación; -p muestra parches.

**Cuándo utilizar:** Al rastrear cuándo se introdujo o eliminó un literal.

**Cuándo evitar:** No uses como búsqueda general de toda edición de línea que contiene texto.

**Sintaxis**

`git log -S "timeout" -- notes.txt`

**Ejemplo básico**

`git log -S "timeout" -- notes.txt`

Encuentra cambios en el recuento de ocurrencias de timeout.

**Ejemplo profesional**

`git log -p -S "timeout" -- notes.txt`

Inspecciona parches coincidentes en archivo de práctica.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Lista commits coincidentes en historial seleccionado; ediciones que conservan recuento pueden no coincidir.

**Efectos y efectos secundarios:** La inspección mostrada no modifica intencionalmente contenido rastreado, index, referencias ni remoto.

**Errores comunes:** Esperar que -S y -G seleccionen mismos commits o ignorar configuración de diff de merges.

**Alternativas:** Usa git log -G para localizar líneas añadidas o eliminadas coincidentes.

**Recuperación:** La inspección no requiere deshacer; verifica revisión, ruta, expresión de búsqueda y código de salida antes de interpretar resultados.

**Versión y dependencias:** Sintaxis estándar Git; usa Git 2.40 o superior en laboratorios del guía.

**Capítulos relacionados**

- [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.es.md)
- [advanced-git/09-blame-and-grep](../../advanced-git/09-blame-and-grep/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-log>

## git-log-pickaxe-regex

**`git log -G`**

**Tipo:** Uso de opción

**Nivel:** Avanzado

**Buscar por intención:** Buscar contenido, Inspeccionar historial

**Riesgo:** Solo lectura. Solo lectura en contexto local ordinario mostrado; evita divulgar salida sensible. Usa configuración confiable y objetos locales completos.

**Finalidad:** Encontrar commits con líneas de parche añadidas o eliminadas que coinciden con expresión regular.

**Requisitos previos:** Usa repositorio desechable con archivos y revisiones indicados existentes; comprueba el repositorio y usa configuración confiable.

**Opciones:** -G acepta expresión regular; -p muestra parches de commits coincidentes.

**Cuándo utilizar:** Al rastrear cambios en línea coincidente aunque recuentos sigan iguales.

**Cuándo evitar:** No supongas búsqueda en líneas sin cambios o todas instantáneas históricas.

**Sintaxis**

`git log -G "timeout" -- notes.txt`

**Ejemplo básico**

`git log -G "timeout" -- notes.txt`

Encuentra parches con líneas coincidentes añadidas o eliminadas.

**Ejemplo profesional**

`git log -p -G "timeout[ ]*=" -- notes.txt`

Inspecciona cambios de asignación coincidentes en historial de práctica.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Lista commits con líneas de diff coincidentes según revisión y configuración seleccionadas.

**Efectos y efectos secundarios:** La inspección mostrada no modifica intencionalmente contenido rastreado, index, referencias ni remoto.

**Errores comunes:** Usar metacaracteres regex sin intención o esperar inclusión predeterminada de diffs de merge.

**Alternativas:** Usa -S cuando cambio en recuento de ocurrencias sea señal relevante.

**Recuperación:** La inspección no requiere deshacer; verifica revisión, ruta, expresión de búsqueda y código de salida antes de interpretar resultados.

**Versión y dependencias:** Sintaxis estándar Git; usa Git 2.40 o superior en laboratorios del guía.

**Capítulos relacionados**

- [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.es.md)
- [advanced-git/09-blame-and-grep](../../advanced-git/09-blame-and-grep/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-log>

## git-log-follow

**`git log --follow`**

**Tipo:** Uso de opción

**Nivel:** Intermedio

**Buscar por intención:** Inspeccionar historial, Buscar contenido

**Riesgo:** Solo lectura. Solo lectura en contexto local ordinario mostrado; evita divulgar salida sensible. Usa configuración confiable y objetos locales completos.

**Finalidad:** Continuar historial de un archivo a través de renombrados detectados.

**Requisitos previos:** Usa repositorio desechable con archivos y revisiones indicados existentes; comprueba el repositorio y usa configuración confiable.

**Opciones:** --follow opera en una sola ruta; -p incluye parches.

**Cuándo utilizar:** Al investigar archivo cuya ruta cambió.

**Cuándo evitar:** No esperes historial completo de directorio o seguimiento perfecto en renombrados y merges complejos.

**Sintaxis**

`git log --follow -- notes.txt`

**Ejemplo básico**

`git log --follow -- notes.txt`

Inspecciona historial de archivo actual a través de renombrados detectados.

**Ejemplo profesional**

`git log -p --follow -- docs/notes.txt`

Inspecciona parches de archivo de documentación a través de renombrados detectados.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Muestra historial del archivo seleccionado con nombres anteriores detectados, sujeto a historial y detección.

**Efectos y efectos secundarios:** La inspección mostrada no modifica intencionalmente contenido rastreado, index, referencias ni remoto.

**Errores comunes:** Pasar varias rutas o interpretar ausencia de renombrado detectado como prueba de falta de relación.

**Alternativas:** Inspecciona git log --name-status y diffs de commits para reorganizaciones complejas.

**Recuperación:** La inspección no requiere deshacer; verifica revisión, ruta, expresión de búsqueda y código de salida antes de interpretar resultados.

**Versión y dependencias:** Sintaxis estándar Git; usa Git 2.40 o superior en laboratorios del guía.

**Capítulos relacionados**

- [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.es.md)
- [advanced-git/09-blame-and-grep](../../advanced-git/09-blame-and-grep/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-log>

## git-diff-check

**`git diff --check`**

**Tipo:** Uso de opción

**Nivel:** Intermedio

**Buscar por intención:** Revisar cambios, Inspeccionar estado del repositorio

**Riesgo:** Cambio de estado. Inspección puede actualizar metadatos del index; no corrige errores.

**Finalidad:** Señalar marcadores de conflicto y errores de espacios introducidos según configuración.

**Requisitos previos:** Usa repositorio desechable con archivos y revisiones indicados existentes; comprueba el repositorio y usa configuración confiable.

**Opciones:** --check informa problemas y devuelve código no cero al detectarlos; --cached selecciona cambios preparados.

**Cuándo utilizar:** Al comprobar cambio propuesto antes de commit o revisión.

**Cuándo evitar:** No lo sustituyas por pruebas o inspección completa de conflictos.

**Sintaxis**

`git diff --check`

**Ejemplo básico**

`git diff --check`

Comprueba cambios no preparados por errores de espacios o marcadores de conflicto introducidos.

**Ejemplo profesional**

`git diff --cached --check`

Comprueba cambios preparados antes de commit revisado.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Condicional
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Informa líneas problemáticas al detectarlas; no hay corrección automática.

**Efectos y efectos secundarios:** No edita contenido; diff ordinario de working tree puede actualizar metadatos stat del index.

**Errores comunes:** Comprobar solo ediciones no preparadas cuando commit previsto está preparado.

**Alternativas:** Usa git diff --cached para revisar contenido y linter del proyecto para reglas más amplias.

**Recuperación:** La inspección no requiere deshacer; verifica revisión, ruta, expresión de búsqueda y código de salida antes de interpretar resultados.

**Versión y dependencias:** Sintaxis estándar Git; usa Git 2.40 o superior en laboratorios del guía.

**Capítulos relacionados**

- [basic-commands/05-ignore-and-review](../../basic-commands/05-ignore-and-review/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-diff>

## git-ls-files-unmerged

**`git ls-files --unmerged`**

**Tipo:** Uso de opción

**Nivel:** Intermedio

**Buscar por intención:** Inspeccionar internals del index, Resolver conflictos

**Riesgo:** Solo lectura. Solo lectura en contexto local ordinario mostrado; evita divulgar salida sensible. Usa configuración confiable y objetos locales completos.

**Finalidad:** Inspeccionar entradas del index que aún tienen etapas no fusionadas.

**Requisitos previos:** Usa repositorio desechable con archivos y revisiones indicados existentes; comprueba el repositorio y usa configuración confiable.

**Opciones:** -u o --unmerged muestra rutas no fusionadas con modo, ID de objeto y etapa; pathspec limita salida.

**Cuándo utilizar:** Al diagnosticar conflictos antes de preparar resolución.

**Cuándo evitar:** No trates salida vacía como prueba de resolución final correcta.

**Sintaxis**

`git ls-files --unmerged`

**Ejemplo básico**

`git ls-files --unmerged`

Inspecciona entradas no fusionadas del index durante conflicto de práctica.

**Ejemplo profesional**

`git ls-files -u -- notes.txt`

Inspecciona etapas de conflicto de archivo nombrado en laboratorio.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Lista etapas de conflicto disponibles; etapas 1, 2 y 3 representan base y dos lados cuando existen.

**Efectos y efectos secundarios:** La inspección mostrada no modifica intencionalmente contenido rastreado, index, referencias ni remoto.

**Errores comunes:** Suponer que todo conflicto tiene tres etapas o que ours siempre significa feature original durante rebase.

**Alternativas:** Usa git status para resumen e inspecciona cada etapa disponible con git show.

**Recuperación:** La inspección no requiere deshacer; verifica revisión, ruta, expresión de búsqueda y código de salida antes de interpretar resultados.

**Versión y dependencias:** Sintaxis estándar Git; usa Git 2.40 o superior en laboratorios del guía.

**Capítulos relacionados**

- [merge-and-conflicts/04-conflict-resolution](../../merge-and-conflicts/04-conflict-resolution/README.es.md)
- [git-internals/06-index-internals](../../git-internals/06-index-internals/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-ls-files>

## git-bisect

**`git bisect`**

**Tipo:** Flujo

**Nivel:** Avanzado

**Buscar por intención:** Encontrar regresión, Inspeccionar historial

**Riesgo:** Cambio de estado. Selecciona solo código histórico confiable en laboratorio aislado; no ejecutes scripts desconocidos automáticamente. Conserva trabajo original.

**Finalidad:** Encontrar límite de regresión clasificando repetidamente commits históricos.

**Requisitos previos:** Usa repositorio desechable limpio con historial completo, punta original guardada, commits good y bad conocidos y prueba segura repetible.

**Opciones:** Inicia, marca revisiones bad y good, prueba cada candidato, clasifica con good o bad, omite commits no comprobables con skip y termina con git bisect reset.

**Cuándo utilizar:** Cuando prueba repetible distingue revisión con fallo conocido de revisión anterior aprobada.

**Cuándo evitar:** Evita con ediciones no preservadas o pruebas no confiables; código histórico puede no ser confiable.

**Sintaxis**

`git bisect start`

**Ejemplo básico**

`git bisect start`

Inicia bisect en laboratorio aislado limpio con commits buenos y malos conocidos; márcalos por separado.

**Ejemplo profesional**

`git bisect good`

Tras probar candidato seleccionado con prueba confiable repetible, marca good; usa bad cuando falle.

**Impacto en el estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / historial: Condicional
- Repositorio remoto: Sin cambios
- Otros estados: Cambia

**Resultado esperado:** Git selecciona candidatos, típicamente separados, hasta identificar límite o informar ambigüedad; reset vuelve al checkout original por defecto.

**Efectos y efectos secundarios:** Bisect puede seleccionar commits, actualizar index y archivos y crear referencias y metadatos temporales; scripts de prueba pueden tener efectos independientes.

**Errores comunes:** Marcar candidato sin probar o dejar estado bisect activo tras investigación.

**Alternativas:** Usa git log -G o inspección manual cuando prueba confiable no pueda clasificar revisiones.

**Recuperación:** Guarda resultado y trabajo deseado; ejecuta git bisect reset y comprueba checkout original y estado. Detente e inspecciona si restauración falla.

**Versión y dependencias:** Sintaxis estándar Git; usa Git 2.40 o superior en laboratorios del guía.

**Capítulos relacionados**

- [advanced-git/01-bisect](../../advanced-git/01-bisect/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-bisect>


---

<!-- navigation-footer -->
[Anterior](../09-recovery-and-stash/README.es.md) · [Índice](../README.es.md) · [Siguiente](../11-advanced-git-operations/README.es.md)
<!-- /navigation-footer -->
