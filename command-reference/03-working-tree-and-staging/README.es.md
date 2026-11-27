# 03 Working tree y staging

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../02-repository-inspection/README.es.md) · [Índice](../README.es.md) · [Siguiente](../04-commits-and-tags/README.es.md)
<!-- /navigation -->

Generado a partir del JSON canónico. Edita los registros, no esta página.

Las entradas describen comandos y operaciones, no una secuencia para ejecutar. Practica en repositorios desechables. Las operaciones alojadas son opcionales.

**Total de entradas distintas: 10**

- [`git add`](#git-add)
- [`git add -A`](#git-add-all)
- [`git add -u`](#git-add-update)
- [`git add -p`](#git-add-patch)
- [`git restore`](#git-restore)
- [`git restore --staged`](#git-restore-staged)
- [`git rm`](#git-rm)
- [`git rm --cached`](#git-rm-cached)
- [`git mv`](#git-mv)
- [`git clean -n`](#git-clean-dry-run)

## git-add

**`git add`**

**Tipo:** Comando nativo

**Nivel:** Principiante

**Buscar por intención:** Preparar cambios

**Riesgo:** Cambio de estado. Revisa rutas exactas y cambios preparados; no operes en el repositorio del guía.

**Finalidad:** Preparar rutas seleccionadas para el próximo commit.

**Requisitos previos:** Usa repositorio propio desechable; inspecciona git status primero y protege trabajo valioso.

**Opciones:** -- termina opciones; especifica una o más rutas.

**Cuándo utilizar:** Tras inspeccionar cambios que quieres confirmar.

**Cuándo evitar:** No prepares credenciales ni cambios ajenos.

**Sintaxis**

`git add -- path`

**Ejemplo básico**

`git add -- notes.txt`

Revisa archivo ficticio de notas antes de prepararlo.

**Ejemplo profesional**

`git add -- src/main.py`

Prepara solo el archivo fuente revisado para un commit enfocado.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Cambia
- Objetos / refs / historial: Condicional
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Entradas del index reflejan contenido o eliminaciones seleccionadas.

**Efectos y efectos secundarios:** Actualiza index y puede almacenar blobs; sin commit ni actualización remota.

**Errores comunes:** Suponer que ediciones posteriores se preparan automáticamente.

**Alternativas:** Usa git add -p para seleccionar fragmentos.

**Recuperación:** Inspecciona git diff --cached después. Retira cambios no deseados del staging con git restore --staged en Git 2.23+ si existe HEAD; conserva archivos de trabajo.

**Versión y dependencias:** Sin herramienta opcional; el ejemplo usa sintaxis estándar Git.

**Capítulos relacionados**

- [basic-commands/02-status-add-commit](../../basic-commands/02-status-add-commit/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-add>

## git-add-all

**`git add -A`**

**Tipo:** Uso de opción

**Nivel:** Principiante

**Buscar por intención:** Preparar cambios

**Riesgo:** Cambio de estado. Revisa rutas exactas y cambios preparados; no operes en el repositorio del guía.

**Finalidad:** Preparar adiciones, modificaciones y eliminaciones en el ámbito seleccionado.

**Requisitos previos:** Usa repositorio propio desechable; inspecciona git status primero y protege trabajo valioso.

**Opciones:** -A actualiza todas las entradas coincidentes; pathspec restringe ámbito.

**Cuándo utilizar:** Cuando todos los cambios de un ámbito deliberado van juntos.

**Cuándo evitar:** Evita staging amplio si hay archivos ajenos o sensibles.

**Sintaxis**

`git add -A [-- pathspec]`

**Ejemplo básico**

`git add -A`

En laboratorio de ámbito claro, inspecciona cambios antes de prepararlos juntos.

**Ejemplo profesional**

`git add -A -- src`

Limita staging amplio al directorio src revisado.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Cambia
- Objetos / refs / historial: Condicional
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Rutas nuevas, modificadas y eliminadas en ámbito se preparan, sujetas a ignore.

**Efectos y efectos secundarios:** Actualiza index y puede escribir objetos; mantiene archivos de trabajo.

**Errores comunes:** Olvidar que eliminaciones y archivos nuevos pueden incluirse.

**Alternativas:** Usa rutas explícitas o git add -p para ámbito fino.

**Recuperación:** Inspecciona git diff --cached después. Retira cambios no deseados del staging con git restore --staged en Git 2.23+ si existe HEAD; conserva archivos de trabajo.

**Versión y dependencias:** Sin herramienta opcional; el ejemplo usa sintaxis estándar Git.

**Capítulos relacionados**

- [basic-commands/02-status-add-commit](../../basic-commands/02-status-add-commit/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-add>

## git-add-update

**`git add -u`**

**Tipo:** Uso de opción

**Nivel:** Intermedio

**Buscar por intención:** Preparar cambios

**Riesgo:** Cambio de estado. Revisa rutas exactas y cambios preparados; no operes en el repositorio del guía.

**Finalidad:** Preparar modificaciones y eliminaciones de rutas ya indexadas sin añadir nuevas no rastreadas.

**Requisitos previos:** Usa repositorio propio desechable; inspecciona git status primero y protege trabajo valioso.

**Opciones:** -u actualiza entradas rastreadas; pathspec limita ámbito opcionalmente.

**Cuándo utilizar:** Al actualizar solo archivos rastreados existentes.

**Cuándo evitar:** No uses si deben incluirse automáticamente archivos nuevos necesarios.

**Sintaxis**

`git add -u [-- pathspec]`

**Ejemplo básico**

`git add -u`

Modifica archivo rastreado y crea otro no rastreado; prepara solo cambios rastreados.

**Ejemplo profesional**

`git add -u -- src`

Prepara cambios rastreados en src sin añadir archivos generados no rastreados.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Cambia
- Objetos / refs / historial: Condicional
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Modificaciones y eliminaciones rastreadas se preparan; nuevas rutas no rastreadas permanecen así.

**Efectos y efectos secundarios:** Cambia index y puede escribir blobs, no commits.

**Errores comunes:** Omitir archivo nuevo de dependencia o preparar eliminaciones rastreadas por error.

**Alternativas:** Usa git add -A si también incluyes rutas nuevas deliberadamente.

**Recuperación:** Inspecciona git diff --cached después. Retira cambios no deseados del staging con git restore --staged en Git 2.23+ si existe HEAD; conserva archivos de trabajo.

**Versión y dependencias:** Sin herramienta opcional; el ejemplo usa sintaxis estándar Git.

**Capítulos relacionados**

- [basic-commands/02-status-add-commit](../../basic-commands/02-status-add-commit/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-add>

## git-add-patch

**`git add -p`**

**Tipo:** Uso de opción

**Nivel:** Intermedio

**Buscar por intención:** Preparar cambios

**Riesgo:** Cambio de estado. Revisa rutas exactas y cambios preparados; no operes en el repositorio del guía.

**Finalidad:** Seleccionar interactivamente fragmentos del diff para staging.

**Requisitos previos:** Usa repositorio propio desechable; inspecciona git status primero y protege trabajo valioso.

**Opciones:** -p abre selección interactiva; las acciones disponibles aparecen en el prompt.

**Cuándo utilizar:** Cuando un archivo contiene cambios de commits distintos.

**Cuándo evitar:** Evita confirmación ciega; fragmentos relacionados pueden depender entre sí.

**Sintaxis**

`git add -p [-- pathspec]`

**Ejemplo básico**

`git add -p -- notes.txt`

Edita dos líneas independientes y elige un fragmento si Git los separa.

**Ejemplo profesional**

`git add -p -- src/main.py`

Separa corrección de fallo de refactorización ajena en archivo revisado.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Cambia
- Objetos / refs / historial: Condicional
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Solo cambios aceptados entran al index; los demás quedan sin preparar.

**Efectos y efectos secundarios:** Actualiza contenido seleccionado del index; archivo de trabajo permanece.

**Errores comunes:** Preparar mitad de cambio dependiente o suponer que fragmento seleccionado es commit probado.

**Alternativas:** Usa rutas explícitas para archivos completos o separa trabajo en archivos.

**Recuperación:** Inspecciona git diff --cached después. Retira cambios no deseados del staging con git restore --staged en Git 2.23+ si existe HEAD; conserva archivos de trabajo.

**Versión y dependencias:** Sin herramienta opcional; el ejemplo usa sintaxis estándar Git.

**Capítulos relacionados**

- [basic-commands/02-status-add-commit](../../basic-commands/02-status-add-commit/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-add>

## git-restore

**`git restore`**

**Tipo:** Comando nativo

**Nivel:** Principiante

**Buscar por intención:** Deshacer cambios

**Riesgo:** Destructivo. Puede eliminar o sobrescribir archivos. Usa solo datos desechables y guarda antes lo valioso.

**Finalidad:** Restaurar ruta del working tree desde el index por defecto, descartando diferencias no preparadas.

**Requisitos previos:** Usa repositorio propio desechable; inspecciona git status primero y protege trabajo valioso.

**Opciones:** --source selecciona árbol explícito; -- termina opciones.

**Cuándo utilizar:** Solo cuando ediciones no preparadas inspeccionadas sean indeseadas.

**Cuándo evitar:** No descartes trabajo sin commit que puedas necesitar; guárdalo antes aparte.

**Sintaxis**

`git restore [--source=tree] -- path`

**Ejemplo básico**

`git restore -- notes.txt`

En laboratorio desechable, descarta edición intencionalmente indeseada de notas rastreadas.

**Ejemplo profesional**

`git restore -- src/main.py`

Tras revisar y guardar cambios, restaura solo edición indeseada del fuente en clon desechable.

**Impacto en el estado**

- Working tree: Cambia
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Ruta seleccionada coincide con origen; por defecto conserva contenido preparado.

**Efectos y efectos secundarios:** Puede sobrescribir o eliminar archivos; no mueve HEAD ni cambia index en este uso.

**Errores comunes:** Confundir origen predeterminado con HEAD cuando staging difiere.

**Alternativas:** Guarda parche o copia antes de descartar; usa git restore --staged para retirar del staging.

**Recuperación:** Ediciones no preparadas quizá nunca entraron en Git; usa copia o historial del editor si existe. Recuperación no garantizada.

**Versión y dependencias:** git restore requiere Git 2.23 o posterior.

**Capítulos relacionados**

- [history-and-recovery/02-restore](../../history-and-recovery/02-restore/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-restore>

## git-restore-staged

**`git restore --staged`**

**Tipo:** Uso de opción

**Nivel:** Principiante

**Buscar por intención:** Retirar cambios del staging

**Riesgo:** Cambio de estado. Revisa rutas exactas y cambios preparados; no operes en el repositorio del guía.

**Finalidad:** Restaurar entrada seleccionada del index desde HEAD por defecto conservando archivos de trabajo.

**Requisitos previos:** Usa repositorio propio desechable; inspecciona git status primero y protege trabajo valioso.

**Opciones:** --staged selecciona index; origen por defecto HEAD; usa -- para rutas.

**Cuándo utilizar:** Cuando existe commit y ruta se preparó prematuramente.

**Cuándo evitar:** No combines con --worktree sin intención de sobrescribir también archivos.

**Sintaxis**

`git restore --staged -- path`

**Ejemplo básico**

`git restore --staged -- notes.txt`

Retira archivo rastreado del staging después del primer commit.

**Ejemplo profesional**

`git restore --staged -- src/main.py`

Retira cambio ajeno del fuente del commit pendiente sin descartar edición.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Cambia
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Entradas seleccionadas coinciden con HEAD; ediciones de trabajo permanecen.

**Efectos y efectos secundarios:** Cambia solo index en este uso; no mueve refs.

**Errores comunes:** Usar origen HEAD antes del primer commit; suponer reconstrucción garantizada de staging parcial.

**Alternativas:** Usa git reset HEAD -- path con HEAD existente en Git antiguo.

**Recuperación:** Revisa diff de trabajo y prepara cambios otra vez; contenido anterior solo en staging puede requerir copia.

**Versión y dependencias:** git restore requiere Git 2.23 o posterior.

**Capítulos relacionados**

- [history-and-recovery/02-restore](../../history-and-recovery/02-restore/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-restore>

## git-rm

**`git rm`**

**Tipo:** Comando nativo

**Nivel:** Principiante

**Buscar por intención:** Gestionar archivos

**Riesgo:** Destructivo. Puede eliminar o sobrescribir archivos. Usa solo datos desechables y guarda antes lo valioso.

**Finalidad:** Eliminar ruta rastreada del working tree y preparar su eliminación.

**Requisitos previos:** Usa repositorio propio desechable; inspecciona git status primero y protege trabajo valioso.

**Opciones:** -r permite eliminación recursiva; --cached elimina solo index; no fuerces omitiendo protecciones.

**Cuándo utilizar:** Cuando archivo rastreado revisado debe eliminarse en el próximo commit.

**Cuándo evitar:** No elimines cambios locales valiosos; evita -f en práctica habitual.

**Sintaxis**

`git rm -- path`

**Ejemplo básico**

`git rm -- old.txt`

Elimina texto obsoleto confirmado en repositorio desechable.

**Ejemplo profesional**

`git rm -- src/obsolete.py`

Prepara eliminación de módulo obsoleto revisado en clon desechable.

**Impacto en el estado**

- Working tree: Cambia
- Index: Cambia
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Archivo rastreado ausente y eliminación preparada si operación tiene éxito.

**Efectos y efectos secundarios:** Cambia working tree e index; commits anteriores permanecen.

**Errores comunes:** Suponer que git rm borra copias confirmadas anteriores del historial.

**Alternativas:** Usa git rm --cached para conservar archivo y eliminar seguimiento.

**Recuperación:** Si eliminación no está confirmada y HEAD contiene archivo deseado, restaura index y copia de trabajo explícitamente desde HEAD tras inspección; otras ediciones perdidas pueden ser irrecuperables.

**Versión y dependencias:** Sin herramienta opcional; el ejemplo usa sintaxis estándar Git.

**Capítulos relacionados**

- [basic-commands/04-move-and-remove](../../basic-commands/04-move-and-remove/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-rm>

## git-rm-cached

**`git rm --cached`**

**Tipo:** Uso de opción

**Nivel:** Intermedio

**Buscar por intención:** Ignorar archivos

**Riesgo:** Cambio de estado. Revisa rutas exactas y cambios preparados; no operes en el repositorio del guía.

**Finalidad:** Eliminar ruta del seguimiento conservando copia de trabajo.

**Requisitos previos:** Usa repositorio propio desechable; inspecciona git status primero y protege trabajo valioso.

**Opciones:** --cached selecciona solo index; -r necesario para eliminar directorio recursivamente.

**Cuándo utilizar:** Cuando archivo generado no sensible ya rastreado debe dejar de seguirse.

**Cuándo evitar:** No uses como procedimiento de eliminación de secretos; commits anteriores aún contienen archivo.

**Sintaxis**

`git rm --cached -- path`

**Ejemplo básico**

`git rm --cached -- notes.tmp`

Deja de seguir archivo temporal inocuo confirmado e inspecciona estado.

**Ejemplo profesional**

`git rm --cached -- local-settings.txt`

Conserva fixture inocuo de configuración local en disco mientras preparas su eliminación del seguimiento.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Cambia
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Archivo permanece; eliminación rastreada se prepara cuando HEAD contiene ruta.

**Efectos y efectos secundarios:** Cambia index; sin cambio inmediato remoto ni de historial confirmado.

**Errores comunes:** Añadir solo regla de ignore esperando que archivo ya rastreado deje de seguirse.

**Alternativas:** Usa regla de ignore adecuada para copias no rastreadas futuras; usa git rm normal si quieres eliminar archivo.

**Recuperación:** Antes de confirmar, inspecciona eliminación preparada y vuelve a añadir archivo si procede; contenido anterior solo en staging puede requerir copia.

**Versión y dependencias:** Sin herramienta opcional; el ejemplo usa sintaxis estándar Git.

**Capítulos relacionados**

- [basic-commands/05-ignore-and-review](../../basic-commands/05-ignore-and-review/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-rm>

## git-mv

**`git mv`**

**Tipo:** Comando nativo

**Nivel:** Principiante

**Buscar por intención:** Gestionar archivos

**Riesgo:** Cambio de estado. Revisa rutas exactas y cambios preparados; no operes en el repositorio del guía.

**Finalidad:** Mover o renombrar ruta y actualizar index en consecuencia.

**Requisitos previos:** Usa repositorio propio desechable; inspecciona git status primero y protege trabajo valioso.

**Opciones:** -- termina opciones; -n previsualiza; evita -f sobrescribiendo destino.

**Cuándo utilizar:** Al renombrar archivo rastreado en cambio enfocado.

**Cuándo evitar:** No sobrescribas destino existente ni ignores referencias dependientes.

**Sintaxis**

`git mv -- source destination`

**Ejemplo básico**

`git mv -- old.txt new.txt`

Renombra notas confirmadas a nombre nuevo no utilizado.

**Ejemplo profesional**

`git mv -- src/old.py src/new.py`

Renombra módulo ilustrativo y revisa por separado imports y pruebas dependientes.

**Impacto en el estado**

- Working tree: Cambia
- Index: Cambia
- Objetos / refs / historial: Condicional
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Ruta antigua eliminada y nueva existente; index actualizado; visualización de rename depende de detección.

**Efectos y efectos secundarios:** Actualiza rutas de trabajo e index; Git confirma snapshots, no registros explícitos de rename.

**Errores comunes:** Suponer actualización automática de imports o enlaces de documentación.

**Alternativas:** Mueve con herramientas del sistema y prepara rutas antigua y nueva explícitamente.

**Recuperación:** Inspecciona estado; revierte rename no confirmado con movimiento inverso explícito si es seguro y destino libre.

**Versión y dependencias:** Sin herramienta opcional; el ejemplo usa sintaxis estándar Git.

**Capítulos relacionados**

- [basic-commands/04-move-and-remove](../../basic-commands/04-move-and-remove/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-mv>

## git-clean-dry-run

**`git clean -n`**

**Tipo:** Uso de opción

**Nivel:** Intermedio

**Buscar por intención:** Inspeccionar archivos

**Riesgo:** Solo lectura. Solo simulación; nunca ejecutes variante destructiva automáticamente.

**Finalidad:** Previsualizar rutas no rastreadas que una operación clean correspondiente eliminaría.

**Requisitos previos:** Usa repositorio propio desechable; inspecciona git status primero y protege trabajo valioso.

**Opciones:** -n simula; -d incluye directorios no rastreados; ignorados normalmente excluidos.

**Cuándo utilizar:** Antes de considerar limpieza de artefactos desechables no rastreados.

**Cuándo evitar:** No sustituyas -n por opción destructiva sin copia y revisión de ámbito separadas.

**Sintaxis**

`git clean -n [-d]`

**Ejemplo básico**

`git clean -n`

Simula limpieza con archivo no rastreado inocuo en laboratorio desechable.

**Ejemplo profesional**

`git clean -nd`

Simula directorios no rastreados en clon desechable antes de decidir sobre limpieza.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Enumera candidatos a eliminación sin borrarlos.

**Efectos y efectos secundarios:** Sin eliminación en modo simulación; sin mutación de index ni refs.

**Errores comunes:** Suponer que simulación sigue válida tras cambios en archivos o ignore.

**Alternativas:** Usa git ls-files --others --exclude-standard para inspeccionar no rastreados.

**Recuperación:** Simulación no requiere recuperación; eliminación real de no rastreados puede ser irrecuperable sin copia.

**Versión y dependencias:** Sin herramienta opcional; el ejemplo usa sintaxis estándar Git.

**Capítulos relacionados**

- [history-and-recovery/01-recovery-safety](../../history-and-recovery/01-recovery-safety/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-clean>


---

<!-- navigation-footer -->
[Anterior](../02-repository-inspection/README.es.md) · [Índice](../README.es.md) · [Siguiente](../04-commits-and-tags/README.es.md)
<!-- /navigation-footer -->
