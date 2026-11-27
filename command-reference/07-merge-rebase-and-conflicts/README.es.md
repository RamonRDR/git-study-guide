# 07 Merge, rebase y conflictos

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../06-branch-management/README.es.md) · [Índice](../README.es.md) · [Siguiente](../08-remotes-and-synchronization/README.es.md)
<!-- /navigation -->

Generado a partir del JSON canónico. Edita los registros, no esta página.

Las entradas describen comandos y operaciones, no una secuencia para ejecutar. Practica en repositorios desechables. Las operaciones alojadas son opcionales.

**Total de entradas distintas: 10**

- [`git merge`](#git-merge)
- [`git merge --ff-only`](#git-merge-ff-only)
- [`git merge --no-ff`](#git-merge-no-ff)
- [`git merge --squash`](#git-merge-squash)
- [`git merge --abort`](#git-merge-abort)
- [`git merge --continue`](#git-merge-continue)
- [`git rebase`](#git-rebase)
- [`git rebase -i`](#git-rebase-interactive)
- [`git rebase --continue`](#git-rebase-continue)
- [`git rebase --abort`](#git-rebase-abort)

## git-merge

**`git merge`**

**Tipo:** Comando nativo

**Nivel:** Intermedio

**Buscar por intención:** Integrar cambios

**Riesgo:** Cambio de estado. La integración puede generar conflictos o cambiar la punta actual; verifica destino y revisa diff resultante y pruebas antes de compartir.

**Finalidad:** Integrar cambios de otra revisión en la rama actual.

**Requisitos previos:** Usa un repositorio propio desechable, estado limpio, referencias verificadas e identidad ficticia. Guarda la punta original antes de integrar.

**Opciones:** --ff-only rechaza integración no fast-forward; --no-ff solicita commit de merge cuando se necesita integrar.

**Cuándo utilizar:** Al incorporar trabajo revisado de una rama al destino local seleccionado.

**Cuándo evitar:** Evita integrar con ediciones valiosas sin confirmar, referencias desconocidas u operaciones inconclusas.

**Sintaxis**

`git merge feature`

**Ejemplo básico**

`git merge feature`

Desde main limpia, integra una rama local de práctica existente.

**Ejemplo profesional**

`git merge feat/docs`

Tras verificar destino local y rama revisada de documentación, integra y prueba.

**Impacto en el estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / historial: Condicional
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** Puede informar que ya está actualizado, avanzar por fast-forward, crear commit de merge o pausar por conflictos, según ascendencia y configuración.

**Efectos y efectos secundarios:** Puede actualizar archivos, index, referencia actual, objetos y metadatos de merge; no implica actualización remota.

**Errores comunes:** Ejecutar desde rama de origen en vez de destino o suponer que merge siempre crea commit.

**Alternativas:** Usa --ff-only cuando solo se permita avance lineal; usa rebase solo bajo política de historial adecuada.

**Recuperación:** Inspecciona estado y punta guardada. Si la operación está pausada, usa el comando abort correspondiente cuando proceda. Tras finalizar, elige recuperación según si se compartió el historial; no uses reset a ciegas.

**Versión y dependencias:** Sintaxis estándar de Git; usa la base de laboratorio del guía, Git 2.40 o superior. Un editor confiable y hooks locales pueden afectar la ejecución.

**Capítulos relacionados**

- [merge-and-conflicts/01-integration-safety](../../merge-and-conflicts/01-integration-safety/README.es.md)
- [merge-and-conflicts/03-merge-commit](../../merge-and-conflicts/03-merge-commit/README.es.md)
- [merge-and-conflicts/04-conflict-resolution](../../merge-and-conflicts/04-conflict-resolution/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-merge>

## git-merge-ff-only

**`git merge --ff-only`**

**Tipo:** Uso de opción

**Nivel:** Principiante

**Buscar por intención:** Integrar cambios, Proteger historial

**Riesgo:** Cambio de estado. La integración puede generar conflictos o cambiar la punta actual; verifica destino y revisa diff resultante y pruebas antes de compartir.

**Finalidad:** Integrar solo si la punta actual puede avanzar sin commit de merge o ya está actualizada.

**Requisitos previos:** Usa un repositorio propio desechable, estado limpio, referencias verificadas e identidad ficticia. Guarda la punta original antes de integrar.

**Opciones:** --ff-only rechaza integración que requiere commit de merge.

**Cuándo utilizar:** Al exigir una vía de integración lineal sin reescribir commits.

**Cuándo evitar:** No lo uses esperando conciliación automática de historiales divergentes.

**Sintaxis**

`git merge --ff-only feature`

**Ejemplo básico**

`git merge --ff-only feature`

Integra una rama local descendiente de main desde main.

**Ejemplo profesional**

`git merge --ff-only feat/docs`

Exige integración local lineal tras comprobar ascendencia.

**Impacto en el estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / historial: Condicional
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** Avanza referencia actual a punta de origen cuando es posible, la mantiene si ya está contenida o rechaza divergencia.

**Efectos y efectos secundarios:** Puede actualizar archivos, index y referencia actual; no crea un nuevo commit de merge.

**Errores comunes:** Tratar un rechazo como motivo para forzar o restablecer la rama.

**Alternativas:** Inspecciona divergencia y elige merge revisado o rebase privado según política.

**Recuperación:** Si se rechaza, inspecciona ascendencia y estado; si avanzó incorrectamente, usa punta original guardada para evaluar recuperación sin sobrescribir historial compartido.

**Versión y dependencias:** Sintaxis estándar de Git; usa la base de laboratorio del guía, Git 2.40 o superior. Un editor confiable y hooks locales pueden afectar la ejecución.

**Capítulos relacionados**

- [merge-and-conflicts/02-fast-forward](../../merge-and-conflicts/02-fast-forward/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-merge>

## git-merge-no-ff

**`git merge --no-ff`**

**Tipo:** Uso de opción

**Nivel:** Intermedio

**Buscar por intención:** Integrar cambios

**Riesgo:** Cambio de estado. La integración puede generar conflictos o cambiar la punta actual; verifica destino y revisa diff resultante y pruebas antes de compartir.

**Finalidad:** Conservar un límite explícito de merge incluso cuando fast-forward sería posible.

**Requisitos previos:** Usa un repositorio propio desechable, estado limpio, referencias verificadas e identidad ficticia. Guarda la punta original antes de integrar.

**Opciones:** --no-ff solicita commit de merge cuando hay cambios que integrar; -m proporciona mensaje.

**Cuándo utilizar:** Cuando la política del equipo exige un commit explícito de integración.

**Cuándo evitar:** Evita en ramas que exigen historial estrictamente lineal.

**Sintaxis**

`git merge --no-ff feature`

**Ejemplo básico**

`git merge --no-ff feature`

Integra una rama de práctica no contenida con límite explícito de merge.

**Ejemplo profesional**

`git merge --no-ff -m "Merge documentation" feat/docs`

Registra integración revisada donde se permiten commits de merge.

**Impacto en el estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / historial: Condicional
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** Al integrar con éxito una única rama no contenida, crea commit con dos padres; historial ya contenido puede quedar igual.

**Efectos y efectos secundarios:** Puede actualizar working tree, index, objetos y referencia; conflictos pueden pausar antes de crear commit.

**Errores comunes:** Esperar commit de merge incluso cuando no hay nada que integrar.

**Alternativas:** Usa --ff-only para avance lineal o flujo squash revisado cuando política exige un commit nuevo sin ascendencia de merge.

**Recuperación:** Inspecciona estado y punta guardada. Si la operación está pausada, usa el comando abort correspondiente cuando proceda. Tras finalizar, elige recuperación según si se compartió el historial; no uses reset a ciegas.

**Versión y dependencias:** Sintaxis estándar de Git; usa la base de laboratorio del guía, Git 2.40 o superior. Un editor confiable y hooks locales pueden afectar la ejecución.

**Capítulos relacionados**

- [merge-and-conflicts/03-merge-commit](../../merge-and-conflicts/03-merge-commit/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-merge>

## git-merge-squash

**`git merge --squash`**

**Tipo:** Uso de opción

**Nivel:** Intermedio

**Buscar por intención:** Integrar cambios, Preparar cambios

**Riesgo:** Cambio de estado. Revisa resultado preparado completo antes del commit; commits de origen pueden quedar fuera de ascendencia de destino.

**Finalidad:** Preparar cambios combinados de otra rama sin mover HEAD ni registrar ascendencia de merge.

**Requisitos previos:** Usa un repositorio propio desechable, estado limpio, referencias verificadas e identidad ficticia. Guarda la punta original antes de integrar.

**Opciones:** --squash prepara resultado de integración; git commit separado registra instantánea preparada.

**Cuándo utilizar:** Cuando una integración local revisada debe convertirse en un commit ordinario.

**Cuándo evitar:** Evita cuando se requiere conservar ascendencia de origen o index contiene ediciones ajenas.

**Sintaxis**

`git merge --squash feature`

**Ejemplo básico**

`git merge --squash feature`

Prepara cambios combinados de rama de práctica existente, luego inspecciona antes de confirmar.

**Ejemplo profesional**

`git merge --squash feat/docs`

Prepara documentación revisada para un único commit posterior; verifica diff y pruebas.

**Impacto en el estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / historial: Condicional
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** Con éxito limpio, working tree e index reflejan resultado combinado mientras HEAD no cambia; conflictos pueden exigir resolución.

**Efectos y efectos secundarios:** No define MERGE\_HEAD; el commit ordinario posterior tiene un padre. Pueden crearse objetos locales o metadatos de squash.

**Errores comunes:** Suponer que --squash confirma automáticamente o que git merge --abort siempre funciona para squash.

**Alternativas:** Usa merge ordinario cuando conservar ascendencia sea importante.

**Recuperación:** Inspecciona estado y cambios preparados; sin MERGE\_HEAD, no dependas de merge --abort. En laboratorio desechable verificado inicialmente limpio, reset --merge HEAD puede descartar integración rastreada intentada tras preservar ediciones necesarias; evalúa aparte si había trabajo.

**Versión y dependencias:** Sintaxis estándar de Git; usa la base de laboratorio del guía, Git 2.40 o superior. Un editor confiable y hooks locales pueden afectar la ejecución.

**Capítulos relacionados**

- [merge-and-conflicts/05-squash-merge](../../merge-and-conflicts/05-squash-merge/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-merge>

## git-merge-abort

**`git merge --abort`**

**Tipo:** Uso de opción

**Nivel:** Intermedio

**Buscar por intención:** Resolver conflictos, Recuperar trabajo

**Riesgo:** Destructivo. Cancelar descarta trabajo de resolución de conflictos; conserva antes las ediciones deseadas por separado. No se garantiza recuperar trabajo previo sin confirmar.

**Finalidad:** Intentar cancelar merge ordinario en curso y reconstruir estado previo.

**Requisitos previos:** Usa un repositorio propio desechable con la operación indicada ya pausada; inspecciona git status y conserva las ediciones de resolución necesarias.

**Opciones:** --abort opera en merge activo; no es un comando genérico de deshacer.

**Cuándo utilizar:** Al abandonar merge ordinario no resuelto en laboratorio desechable inicialmente limpio.

**Cuándo evitar:** Evita si trabajo de resolución debe conservarse o merge ya finalizó; squash carece de MERGE\_HEAD.

**Sintaxis**

`git merge --abort`

**Ejemplo básico**

`git merge --abort`

Cancela merge ordinario de práctica con conflicto deliberado.

**Ejemplo profesional**

`git merge --abort`

Tras guardar ediciones deseadas de resolución, abandona integración local inadecuada.

**Impacto en el estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / historial: Condicional
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** Intenta restaurar estado previo y cierra merge activo con éxito; trabajo previo sin confirmar puede no reconstruirse.

**Efectos y efectos secundarios:** Puede cambiar working tree, index y metadatos de merge; auto-stash puede reaplicarse y generar conflictos.

**Errores comunes:** Usar abort tras merge finalizado o suponer recuperación garantizada de trabajo sin confirmar.

**Alternativas:** Resuelve y prepara conflictos y usa git merge --continue si integración debe finalizar.

**Recuperación:** Verifica estado y punta original tras abort. Si falla, detente e inspecciona estado restante antes de nuevos cambios.

**Versión y dependencias:** Sintaxis estándar de Git; usa la base de laboratorio del guía, Git 2.40 o superior. Un editor confiable y hooks locales pueden afectar la ejecución.

**Capítulos relacionados**

- [merge-and-conflicts/04-conflict-resolution](../../merge-and-conflicts/04-conflict-resolution/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-merge>

## git-merge-continue

**`git merge --continue`**

**Tipo:** Uso de opción

**Nivel:** Intermedio

**Buscar por intención:** Resolver conflictos, Integrar cambios

**Riesgo:** Cambio de estado. La integración puede generar conflictos o cambiar la punta actual; verifica destino y revisa diff resultante y pruebas antes de compartir.

**Finalidad:** Finalizar merge ordinario activo tras resolver y preparar conflictos.

**Requisitos previos:** En repositorio desechable con la operación indicada pausada, resuelve conflictos, prepara resoluciones deseadas, revisa diff preparado y confirma identidad ficticia.

**Opciones:** --continue comprueba merge activo e invoca commit; editor o hooks pueden requerir interacción.

**Cuándo utilizar:** Cuando todas las resoluciones deseadas están preparadas y revisadas.

**Cuándo evitar:** No continúes mientras haya rutas no fusionadas o contenido de resolución sin revisar.

**Sintaxis**

`git merge --continue`

**Ejemplo básico**

`git merge --continue`

Finaliza merge de práctica tras preparar archivo resuelto.

**Ejemplo profesional**

`git merge --continue`

Tras revisar diff de resolución y ejecutar pruebas, completa merge local.

**Impacto en el estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / historial: Condicional
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** Con éxito crea commit de merge y limpia estado de merge; de lo contrario puede seguir pausado.

**Efectos y efectos secundarios:** Puede actualizar referencia, objetos, metadatos de index y estado de merge; hooks pueden cambiar estado local.

**Errores comunes:** Suponer que quitar marcadores de conflicto prepara resolución automáticamente.

**Alternativas:** Usa git commit para concluir merge ordinario tras inspeccionar su estado o abort si lo abandonas.

**Recuperación:** Inspecciona estado y punta guardada. Si la operación está pausada, usa el comando abort correspondiente cuando proceda. Tras finalizar, elige recuperación según si se compartió el historial; no uses reset a ciegas.

**Versión y dependencias:** Sintaxis estándar de Git; usa la base de laboratorio del guía, Git 2.40 o superior. Un editor confiable y hooks locales pueden afectar la ejecución.

**Capítulos relacionados**

- [merge-and-conflicts/04-conflict-resolution](../../merge-and-conflicts/04-conflict-resolution/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-merge>

## git-rebase

**`git rebase`**

**Tipo:** Comando nativo

**Nivel:** Avanzado

**Buscar por intención:** Integrar cambios, Reescribir historial local

**Riesgo:** Reescritura del historial. La reaplicación puede cambiar IDs y perjudicar colaboradores. Usa historial privado, conserva la punta original y verifica el resultado antes de compartir.

**Finalidad:** Reaplicar commits seleccionados sobre otra base para reorganizar historial local.

**Requisitos previos:** Usa un repositorio propio desechable, estado limpio, referencias verificadas e identidad ficticia. Guarda la punta original antes de integrar.

**Opciones:** Indica revisión upstream; --onto permite nueva base separada y exige selección cuidadosa del rango.

**Cuándo utilizar:** Al actualizar rama privada de feature sobre base de integración más nueva.

**Cuándo evitar:** Evita reescribir commits compartidos sin acuerdo o rebase con operaciones inconclusas.

**Sintaxis**

`git rebase main`

**Ejemplo básico**

`git rebase main`

Desde rama privada limpia de feature, reaplica sobre main existente.

**Ejemplo profesional**

`git rebase main`

Tras guardar punta privada, actualiza base y compara serie revisada.

**Impacto en el estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / historial: Condicional
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** Puede reaplicar commits con nuevos IDs, omitir cambios equivalentes, avanzar fast-forward, no cambiar o pausar por conflictos.

**Efectos y efectos secundarios:** Puede cambiar archivos, index, objetos, referencia actual y estado de secuencia; HEAD puede quedar separado durante reaplicación.

**Errores comunes:** Suponer que rebase conserva IDs o ejecutarlo en destino de integración en vez de rama reaplicada.

**Alternativas:** Usa merge para integrar sin reemplazar commits de origen existentes.

**Recuperación:** Inspecciona estado y punta guardada. Si la operación está pausada, usa el comando abort correspondiente cuando proceda. Tras finalizar, elige recuperación según si se compartió el historial; no uses reset a ciegas.

**Versión y dependencias:** Sintaxis estándar de Git; usa la base de laboratorio del guía, Git 2.40 o superior. Un editor confiable y hooks locales pueden afectar la ejecución.

**Capítulos relacionados**

- [merge-and-conflicts/06-rebase-and-conflicts](../../merge-and-conflicts/06-rebase-and-conflicts/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-rebase>

## git-rebase-interactive

**`git rebase -i`**

**Tipo:** Uso de opción

**Nivel:** Avanzado

**Buscar por intención:** Reescribir historial local, Revisar cambios

**Riesgo:** Reescritura del historial. La reaplicación puede cambiar IDs y perjudicar colaboradores. Usa historial privado, conserva la punta original y verifica el resultado antes de compartir.

**Finalidad:** Editar secuencia de commits privados seleccionados antes de reaplicarlos.

**Requisitos previos:** Usa un repositorio propio desechable, estado limpio, referencias verificadas e identidad ficticia. Guarda la punta original antes de integrar.

**Opciones:** -i abre lista de tareas con acciones como pick, reword, edit, squash, fixup y drop; revisa orden y efectos antes de guardar.

**Cuándo utilizar:** Al refinar serie de parches no publicada antes de revisión.

**Cuándo evitar:** Evita cambiar historial compartido, descartar commits necesarios o reordenar cambios dependientes a ciegas.

**Sintaxis**

`git rebase -i HEAD~2`

**Ejemplo básico**

`git rebase -i HEAD~2`

Con al menos dos commits privados después de una base, inspecciona lista antes de cambiar.

**Ejemplo profesional**

`git rebase -i main`

En serie lineal privada de feature, revisa ediciones o acciones fixup planeadas y valida después.

**Impacto en el estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / historial: Condicional
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** Aplica acciones elegidas; puede reemplazar, combinar, omitir o pausar en commits. Lista sin cambios puede dejar historial igual.

**Efectos y efectos secundarios:** Puede modificar historial, archivos, index y metadatos de rebase; comportamiento predeterminado no conserva topología de merges.

**Errores comunes:** Confundir orden de lista con orden del log más reciente primero, o descartar commit previo necesario.

**Alternativas:** Usa commit adicional ordinario si historial debe permanecer intacto; usa range-diff para revisar serie revisada.

**Recuperación:** Inspecciona estado y punta guardada. Si la operación está pausada, usa el comando abort correspondiente cuando proceda. Tras finalizar, elige recuperación según si se compartió el historial; no uses reset a ciegas.

**Versión y dependencias:** Sintaxis estándar de Git; usa la base de laboratorio del guía, Git 2.40 o superior. Un editor confiable y hooks locales pueden afectar la ejecución.

**Capítulos relacionados**

- [merge-and-conflicts/07-interactive-rebase](../../merge-and-conflicts/07-interactive-rebase/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-rebase>

## git-rebase-continue

**`git rebase --continue`**

**Tipo:** Uso de opción

**Nivel:** Avanzado

**Buscar por intención:** Resolver conflictos, Reescribir historial local

**Riesgo:** Reescritura del historial. La reaplicación puede cambiar IDs y perjudicar colaboradores. Usa historial privado, conserva la punta original y verifica el resultado antes de compartir.

**Finalidad:** Reanudar rebase interrumpido tras gestionar su pausa actual.

**Requisitos previos:** En repositorio desechable con la operación indicada pausada, resuelve conflictos, prepara resoluciones deseadas, revisa diff preparado y confirma identidad ficticia.

**Opciones:** --continue reanuda secuencia activa; pueden seguir otros conflictos o pausas de edición.

**Cuándo utilizar:** Cuando resoluciones deseadas o ediciones planeadas están listas y revisadas.

**Cuándo evitar:** Evita continuar con rutas no resueltas o usar --skip solo para silenciar conflicto.

**Sintaxis**

`git rebase --continue`

**Ejemplo básico**

`git rebase --continue`

Tras preparar archivo de práctica resuelto, reanuda reaplicación.

**Ejemplo profesional**

`git rebase --continue`

Revisa resolución preparada y prueba serie privada antes de reanudar; repite si vuelve a pausar.

**Impacto en el estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / historial: Condicional
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** Reanuda reaplicación; puede finalizar y actualizar rama o pausar de nuevo.

**Efectos y efectos secundarios:** Puede crear commits sustitutos, actualizar index y working tree, mover HEAD y cambiar metadatos de secuencia.

**Errores comunes:** Suponer que una continuación siempre completa toda la serie.

**Alternativas:** Usa git rebase --abort para abandonar rebase activo tras conservar resolución necesaria.

**Recuperación:** Inspecciona estado y punta guardada. Si la operación está pausada, usa el comando abort correspondiente cuando proceda. Tras finalizar, elige recuperación según si se compartió el historial; no uses reset a ciegas.

**Versión y dependencias:** Sintaxis estándar de Git; usa la base de laboratorio del guía, Git 2.40 o superior. Un editor confiable y hooks locales pueden afectar la ejecución.

**Capítulos relacionados**

- [merge-and-conflicts/06-rebase-and-conflicts](../../merge-and-conflicts/06-rebase-and-conflicts/README.es.md)
- [merge-and-conflicts/07-interactive-rebase](../../merge-and-conflicts/07-interactive-rebase/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-rebase>

## git-rebase-abort

**`git rebase --abort`**

**Tipo:** Uso de opción

**Nivel:** Avanzado

**Buscar por intención:** Resolver conflictos, Recuperar trabajo

**Riesgo:** Destructivo. Cancelar descarta trabajo de resolución de conflictos; conserva antes las ediciones deseadas por separado. No se garantiza recuperar trabajo previo sin confirmar.

**Finalidad:** Cancelar rebase activo y restaurar HEAD a rama original o posición inicial.

**Requisitos previos:** Usa un repositorio propio desechable con la operación indicada ya pausada; inspecciona git status y conserva las ediciones de resolución necesarias.

**Opciones:** --abort cancela reaplicación; --quit termina seguimiento de operación sin la misma restauración de HEAD, index y working tree.

**Cuándo utilizar:** Al abandonar rebase privado inconcluso por conflictos o plan inadecuados.

**Cuándo evitar:** Evita abortar si cambios necesarios de resolución no están guardados por separado; no deshace rebase concluido.

**Sintaxis**

`git rebase --abort`

**Ejemplo básico**

`git rebase --abort`

Cancela rebase de práctica con conflicto iniciado en estado limpio.

**Ejemplo profesional**

`git rebase --abort`

Tras conservar ediciones necesarias de resolución, abandona reaplicación privada y verifica punta original.

**Impacto en el estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / historial: Condicional
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** Restaura posición original de checkout y limpia rebase activo con éxito; auto-stash puede complicar restauración.

**Efectos y efectos secundarios:** Puede descartar estado intermedio de reaplicación y resolución, actualizar archivos, index y HEAD; objetos creados pueden permanecer hasta limpieza.

**Errores comunes:** Esperar que ediciones realizadas durante resolución sobrevivan a la cancelación.

**Alternativas:** Resuelve y continúa cuando plan original de integración siga siendo adecuado.

**Recuperación:** Verifica punta original guardada, estado y posible stash tras cancelar; si restauración falla, conserva datos restantes e inspecciona antes de actuar.

**Versión y dependencias:** Sintaxis estándar de Git; usa la base de laboratorio del guía, Git 2.40 o superior. Un editor confiable y hooks locales pueden afectar la ejecución.

**Capítulos relacionados**

- [merge-and-conflicts/06-rebase-and-conflicts](../../merge-and-conflicts/06-rebase-and-conflicts/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-rebase>


---

<!-- navigation-footer -->
[Anterior](../06-branch-management/README.es.md) · [Índice](../README.es.md) · [Siguiente](../08-remotes-and-synchronization/README.es.md)
<!-- /navigation-footer -->
