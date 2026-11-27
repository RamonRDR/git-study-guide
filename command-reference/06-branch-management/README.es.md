# 06 Gestión de ramas

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../05-history-and-comparison/README.es.md) · [Índice](../README.es.md) · [Siguiente](../07-merge-rebase-and-conflicts/README.es.md)
<!-- /navigation -->

Generado a partir del JSON canónico. Edita los registros, no esta página.

Las entradas describen comandos y operaciones, no una secuencia para ejecutar. Practica en repositorios desechables. Las operaciones alojadas son opcionales.

**Total de entradas distintas: 10**

- [`git branch --list`](#git-branch-list)
- [`git branch NAME`](#git-branch-create)
- [`git branch --show-current`](#git-branch-show-current)
- [`git switch`](#git-switch)
- [`git switch -c`](#git-switch-create)
- [`git switch --detach`](#git-switch-detach)
- [`git branch -m`](#git-branch-rename)
- [`git branch -d`](#git-branch-delete)
- [`git branch --merged`](#git-branch-merged)
- [`git branch --set-upstream-to`](#git-branch-upstream)

## git-branch-list

**`git branch --list`**

**Tipo:** Uso de opción

**Nivel:** Principiante

**Buscar por intención:** Gestionar ramas, Inspeccionar referencias

**Riesgo:** Solo lectura. Inspección de solo lectura; comprueba los nombres de ramas antes de compartir la salida.

**Finalidad:** Listar nombres de ramas locales, opcionalmente filtrados por un patrón.

**Requisitos previos:** Usa un repositorio propio desechable con un commit existente. Inspecciona estado y referencias antes de operar.

**Opciones:** --list selecciona el listado explícitamente; -a incluye referencias de seguimiento remoto y -vv muestra información de upstream y otros detalles.

**Cuándo utilizar:** Al inspeccionar ramas disponibles antes de seleccionar o limpiar trabajo.

**Cuándo evitar:** No trates el listado local como inventario remoto en tiempo real.

**Sintaxis**

`git branch --list "feat/*"`

**Ejemplo básico**

`git branch --list`

Inspecciona ramas locales.

**Ejemplo profesional**

`git branch --list "feat/*"`

Inspecciona ramas locales de feature sin crear una.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Muestra ramas coincidentes; la rama local actual se marca con asterisco en la salida normal.

**Efectos y efectos secundarios:** Esta inspección no modifica contenido rastreado, instantánea preparada, referencias locales ni estado remoto.

**Errores comunes:** Omitir --list con nombre o patrón puede interpretarse como creación de rama.

**Alternativas:** Usa git branch --show-current para solo la rama actual o git show-ref para inspeccionar IDs.

**Recuperación:** El listado no requiere recuperación; inspecciona la referencia o filtro seleccionado si la salida es inesperada.

**Versión y dependencias:** Sintaxis estándar documentada en Git 2.34; no requiere herramienta opcional.

**Capítulos relacionados**

- [branches/01-create-and-switch](../../branches/01-create-and-switch/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-branch/2.34.0>

## git-branch-create

**`git branch NAME`**

**Tipo:** Uso de opción

**Nivel:** Principiante

**Buscar por intención:** Gestionar ramas, Trabajar en paralelo

**Riesgo:** Cambio de estado. Verifica nombre y punto inicial; no uses fuerza para resolver colisiones de nombre.

**Finalidad:** Crear una rama local con nombre en un commit existente sin cambiar a ella.

**Requisitos previos:** Usa un repositorio propio desechable con un commit existente. Inspecciona estado y referencias antes de operar.

**Opciones:** Proporciona nombre nuevo y punto inicial opcional; sin punto inicial usa HEAD. --no-track impide configuración automática de upstream.

**Cuándo utilizar:** Al preparar una línea de trabajo independiente o preservar un commit.

**Cuándo evitar:** Evita crear una rama desde una revisión no verificada o sobrescribir una rama existente con -f.

**Sintaxis**

`git branch feat/notes main`

**Ejemplo básico**

`git branch feat/notes`

Crea una rama local en HEAD actual.

**Ejemplo profesional**

`git branch feat/review main`

Crea una rama en la punta existente verificada de main.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Cambia
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** Una nueva referencia local apunta al commit seleccionado; HEAD permanece donde estaba.

**Efectos y efectos secundarios:** Añade referencia de rama y posiblemente reflog o configuración de seguimiento; archivos de trabajo e index no cambian.

**Errores comunes:** Suponer que crear una rama también cambia a ella o copia una carpeta.

**Alternativas:** Usa git switch -c para crear y seleccionar en una operación.

**Recuperación:** Inspecciona ambas referencias; si una rama nueva sin uso es incorrecta, elimínala solo tras confirmar que su punta es alcanzable desde una referencia superviviente prevista.

**Versión y dependencias:** Sintaxis estándar documentada en Git 2.34; no requiere herramienta opcional.

**Capítulos relacionados**

- [branches/01-create-and-switch](../../branches/01-create-and-switch/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-branch/2.34.0>

## git-branch-show-current

**`git branch --show-current`**

**Tipo:** Uso de opción

**Nivel:** Principiante

**Buscar por intención:** Inspeccionar estado del repositorio, Gestionar ramas

**Riesgo:** Solo lectura. Inspección de solo lectura; comprueba los nombres de ramas antes de compartir la salida.

**Finalidad:** Mostrar el nombre de la rama local actual cuando HEAD está asociado.

**Requisitos previos:** Usa un repositorio propio desechable con un commit existente. Inspecciona estado y referencias antes de operar.

**Opciones:** --show-current selecciona salida de nombre único; queda vacía en HEAD separado.

**Cuándo utilizar:** Al confirmar la rama activa antes de commit o cambio.

**Cuándo evitar:** No supongas que una salida vacía es nombre de rama o prueba de fallo del comando.

**Sintaxis**

`git branch --show-current`

**Ejemplo básico**

`git branch --show-current`

Comprueba qué rama está activa.

**Ejemplo profesional**

`git branch --show-current`

Antes del commit, verifica la rama de feature esperada.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Muestra el nombre de la rama o ningún nombre si HEAD está separado.

**Efectos y efectos secundarios:** Esta inspección no modifica contenido rastreado, instantánea preparada, referencias locales ni estado remoto.

**Errores comunes:** Suponer que devuelve ID del commit o upstream remoto.

**Alternativas:** Usa git symbolic-ref --quiet --short HEAD para comprobar HEAD simbólico, o git rev-parse HEAD para el ID del commit.

**Recuperación:** El listado no requiere recuperación; inspecciona la referencia o filtro seleccionado si la salida es inesperada.

**Versión y dependencias:** Git 2.22 o superior admite --show-current; el guía usa Git 2.40 o superior en laboratorios.

**Capítulos relacionados**

- [branches/01-create-and-switch](../../branches/01-create-and-switch/README.es.md)
- [branches/05-detached-head](../../branches/05-detached-head/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-branch/2.34.0>

## git-switch

**`git switch`**

**Tipo:** Comando nativo

**Nivel:** Principiante

**Buscar por intención:** Cambiar contexto de trabajo, Gestionar ramas

**Riesgo:** Cambio de estado. Las ediciones compatibles pueden acompañar el cambio; las conflictivas pueden bloquearlo. No uses opciones de fuerza ni descarte.

**Finalidad:** Seleccionar una rama existente para trabajo posterior.

**Requisitos previos:** Usa un repositorio propio desechable con estado limpio, commit existente y hooks locales confiables. Preserva primero el trabajo valioso.

**Opciones:** --no-guess desactiva creación automática basada en una rama de seguimiento remoto coincidente única; - abrevia checkout anterior.

**Cuándo utilizar:** Al alternar entre líneas locales de trabajo existentes.

**Cuándo evitar:** Evita salir de commits separados no preservados o forzar ante ediciones conflictivas.

**Sintaxis**

`git switch main`

**Ejemplo básico**

`git switch main`

Vuelve a main local existente tras preservar trabajo.

**Ejemplo profesional**

`git switch --no-guess feat/notes`

Selecciona rama local de feature existente verificada sin creación automática de rama de seguimiento.

**Impacto en el estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / historial: Cambia
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** HEAD apunta a la rama seleccionada; archivos rastreados e index reflejan el nuevo contexto con ediciones compatibles preservadas cuando sea posible.

**Efectos y efectos secundarios:** Selecciona HEAD y actualiza index y archivos de trabajo según sea necesario; los hooks post-checkout configurados pueden afectar otro estado local. No hay push ni merge.

**Errores comunes:** Confundir cambio con merge o esperar que todas las ediciones sin confirmar permanezcan en la rama anterior.

**Alternativas:** Git antiguo usa git checkout con un nombre de rama verificado; prefiere switch por claridad en laboratorios actuales.

**Recuperación:** Si el cambio falla, inspecciona el estado y preserva ediciones; no lo fuerces. Vuelve a la rama original con estado limpio y guarda antes los commits separados deseados.

**Versión y dependencias:** Git 2.23 introdujo switch; la base de práctica del guía es Git 2.40 o superior. La sintaxis mostrada está documentada en el manual Git 2.35.

**Capítulos relacionados**

- [branches/01-create-and-switch](../../branches/01-create-and-switch/README.es.md)
- [branches/03-switch-safety-and-naming](../../branches/03-switch-safety-and-naming/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-switch/2.35.0>

## git-switch-create

**`git switch -c`**

**Tipo:** Uso de opción

**Nivel:** Principiante

**Buscar por intención:** Gestionar ramas, Cambiar contexto de trabajo, Trabajar en paralelo

**Riesgo:** Cambio de estado. Las ediciones compatibles pueden acompañar el cambio; las conflictivas pueden bloquearlo. No uses opciones de fuerza ni descarte.

**Finalidad:** Crear una rama local nueva y cambiar a ella en una operación.

**Requisitos previos:** Usa un repositorio propio desechable con estado limpio, commit existente y hooks locales confiables. Preserva primero el trabajo valioso.

**Opciones:** -c exige nombre nuevo y acepta punto inicial opcional; no lo confundas con -C, que puede restablecer una rama existente.

**Cuándo utilizar:** Al iniciar una tarea aislada o nombrar un commit separado antes de salir de él.

**Cuándo evitar:** Evita usar un punto inicial no verificado o sobrescribir un nombre existente.

**Sintaxis**

`git switch -c feat/notes main`

**Ejemplo básico**

`git switch -c feat/notes`

Inicia una tarea en el commit actual.

**Ejemplo profesional**

`git switch -c feat/review main`

Inicia una tarea de revisión desde un commit local verificado de main.

**Impacto en el estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / historial: Cambia
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** Si tiene éxito, la rama nueva apunta al punto inicial elegido y HEAD la selecciona; si el cambio falla no se crea la rama.

**Efectos y efectos secundarios:** Selecciona HEAD y actualiza index y archivos de trabajo según sea necesario; los hooks post-checkout configurados pueden afectar otro estado local. No hay push ni merge.

**Errores comunes:** Usar -C para evitar una colisión o suponer que la rama nueva siempre empieza en main.

**Alternativas:** Usa git branch NAME START y git switch NAME por separado cuando crear sin cambiar sea útil.

**Recuperación:** Verifica HEAD y ambas referencias; preserva commits nuevos antes de volver a la rama original o limpiar.

**Versión y dependencias:** Git 2.23 introdujo switch; la base de práctica del guía es Git 2.40 o superior. La sintaxis mostrada está documentada en el manual Git 2.35.

**Capítulos relacionados**

- [branches/01-create-and-switch](../../branches/01-create-and-switch/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-switch/2.35.0>

## git-switch-detach

**`git switch --detach`**

**Tipo:** Uso de opción

**Nivel:** Intermedio

**Buscar por intención:** Cambiar contexto de trabajo, Inspeccionar historial, Recuperar trabajo

**Riesgo:** Cambio de estado. Los commits separados pueden quedar inalcanzables; recuperación no garantizada. Presérvalos antes de cambiar.

**Finalidad:** Seleccionar un commit directamente sin asociar HEAD a una rama.

**Requisitos previos:** Usa un repositorio propio desechable con estado limpio, commit existente y hooks locales confiables. Preserva primero el trabajo valioso.

**Opciones:** --detach solicita HEAD separado explícitamente; usa un commit verificado o etiqueta que resuelva a commit.

**Cuándo utilizar:** Al inspeccionar instantáneas históricas o realizar un experimento desechable.

**Cuándo evitar:** Evita dejar commits deseados sin nombre o tratar trabajo separado como actualizaciones de main.

**Sintaxis**

`git switch --detach HEAD~1`

**Ejemplo básico**

`git switch --detach HEAD~1`

Inspecciona el primer padre de un commit actual no inicial.

**Ejemplo profesional**

`git switch --detach v1.0.0`

Inspecciona una etiqueta local de versión existente que resuelve a commit.

**Impacto en el estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / historial: Cambia
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** HEAD apunta directamente al commit; puntas de ramas no cambian y --show-current no imprime nombre.

**Efectos y efectos secundarios:** Selecciona HEAD y actualiza index y archivos de trabajo según sea necesario; los hooks post-checkout configurados pueden afectar otro estado local. No hay push ni merge.

**Errores comunes:** Suponer que commits creados en estado separado avanzan la rama seleccionada anteriormente.

**Alternativas:** Crea una rama temporal con nombre si esperas conservar cambios.

**Recuperación:** Antes de salir, usa git switch -c con nombre libre para conservar commits deseados; si ya saliste, inspecciona reflog y nombra el commit verificado si está disponible.

**Versión y dependencias:** Git 2.23 introdujo switch; la base de práctica del guía es Git 2.40 o superior. La sintaxis mostrada está documentada en el manual Git 2.35.

**Capítulos relacionados**

- [branches/05-detached-head](../../branches/05-detached-head/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-switch/2.35.0>

## git-branch-rename

**`git branch -m`**

**Tipo:** Uso de opción

**Nivel:** Intermedio

**Buscar por intención:** Gestionar ramas

**Riesgo:** Cambio de estado. Comprueba ambos nombres y dependencias; evita reemplazo forzado.

**Finalidad:** Renombrar una rama local y mover su configuración asociada y reflog cuando existan.

**Requisitos previos:** Usa un repositorio propio desechable con un commit existente. Inspecciona estado y referencias antes de operar.

**Opciones:** -m acepta nombres anterior y nuevo o solo nombre nuevo para rama actual; -M fuerza reemplazo y no se usa aquí.

**Cuándo utilizar:** Al corregir nombre de rama privada conforme convenciones del equipo.

**Cuándo evitar:** Evita renombrar ramas compartidas sin coordinación o usar -M para reemplazar otra rama.

**Sintaxis**

`git branch -m feat/old feat/new`

**Ejemplo básico**

`git branch -m feat/notes feat/docs`

Renombra una rama privada existente a nombre libre.

**Ejemplo profesional**

`git branch -m feat/review`

Renombra la rama privada actual a nombre libre.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Cambia
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** El nuevo nombre local identifica la misma punta; el nombre anterior desaparece. Si es actual, HEAD sigue la rama renombrada.

**Efectos y efectos secundarios:** Mueve referencias locales, configuración y reflog cuando existen, no contenido de commits ni nombres de ramas remotas.

**Errores comunes:** Esperar que rama remota o nombre de destino upstream se renombre automáticamente.

**Alternativas:** Conserva nombre existente cuando colaboradores o automatización dependan de él.

**Recuperación:** Verifica punta, upstream y nombre original libre antes de renombrar de vuelta con -m; coordina si ya se compartió.

**Versión y dependencias:** Sintaxis estándar documentada en Git 2.34; no requiere herramienta opcional.

**Capítulos relacionados**

- [branches/03-switch-safety-and-naming](../../branches/03-switch-safety-and-naming/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-branch/2.34.0>

## git-branch-delete

**`git branch -d`**

**Tipo:** Uso de opción

**Nivel:** Intermedio

**Buscar por intención:** Gestionar ramas, Proteger historial

**Riesgo:** Destructivo. La eliminación puede quitar el último nombre conveniente del trabajo; nunca uses -D para evitar una negativa sin evaluación separada. Recuperación no garantizada.

**Finalidad:** Eliminar una rama local con protección de estado integrado.

**Requisitos previos:** Usa un repositorio propio desechable; verifica que rama objetivo no esté seleccionada en ningún worktree y punta sea alcanzable desde la rama superviviente prevista. Registra su ID.

**Opciones:** -d comprueba integración completa en upstream configurado, o HEAD si no existe upstream; -D omite esa protección y no es alternativa ante dudas.

**Cuándo utilizar:** Al limpiar ramas privadas cuyos commits se conservan en el destino previsto.

**Cuándo evitar:** Evita eliminar trabajo sin alcance verificado, o forzar eliminación tras squash merge sin revisar contenido e historial.

**Sintaxis**

`git branch -d feat/notes`

**Ejemplo básico**

`git branch -d feat/notes`

Con main seleccionada, elimina solo una rama privada contenida verificada sin upstream.

**Ejemplo profesional**

`git branch -d feat/review`

Tras confirmar ascendencia, upstream y estado de worktrees, elimina la rama local de revisión.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Cambia
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** La referencia local y reflog de la rama, si existe, se eliminan si tiene éxito; de lo contrario Git puede negarse.

**Efectos y efectos secundarios:** Elimina nombre local y metadatos asociados; no borra inmediatamente objetos de commit ni elimina ramas remotas.

**Errores comunes:** Suponer que -d siempre comprueba main o que squash merge conserva ascendencia de commits.

**Alternativas:** Conserva la rama si hay duda; inspecciona git branch --merged main y git log main..NAME primero.

**Recuperación:** Si el commit registrado aún existe, recrea una rama en su ID verificado; configuración y reflog anteriores no se restauran automáticamente.

**Versión y dependencias:** Sintaxis estándar documentada en Git 2.34; no requiere herramienta opcional.

**Capítulos relacionados**

- [branches/04-safe-local-deletion](../../branches/04-safe-local-deletion/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-branch/2.34.0>

## git-branch-merged

**`git branch --merged`**

**Tipo:** Uso de opción

**Nivel:** Intermedio

**Buscar por intención:** Gestionar ramas, Inspeccionar historial, Proteger historial

**Riesgo:** Solo lectura. Inspección de solo lectura; comprueba los nombres de ramas antes de compartir la salida.

**Finalidad:** Listar ramas cuyos commits de punta son alcanzables desde un commit seleccionado.

**Requisitos previos:** Usa un repositorio propio desechable con un commit existente. Inspecciona estado y referencias antes de operar.

**Opciones:** --merged usa HEAD por defecto; --no-merged selecciona el conjunto opuesto. Proporciona destino explícito como main.

**Cuándo utilizar:** Al revisar ascendencia antes de limpiar ramas locales.

**Cuándo evitar:** No equipares ausencia en la lista con ausencia de cambios equivalentes tras squash o cherry-pick.

**Sintaxis**

`git branch --merged main`

**Ejemplo básico**

`git branch --merged main`

Inspecciona puntas locales contenidas en main existente.

**Ejemplo profesional**

`git branch --no-merged main`

Identifica puntas locales no contenidas en main antes de revisar candidatos a limpieza.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Muestra puntas de ramas seleccionadas ancestras del destino o iguales a él.

**Efectos y efectos secundarios:** Esta inspección no modifica contenido rastreado, instantánea preparada, referencias locales ni estado remoto.

**Errores comunes:** Suponer que la lista prueba que una rama se puede eliminar independientemente de worktrees o configuración upstream.

**Alternativas:** Usa git merge-base --is-ancestor NAME main para probar una rama verificada contra main.

**Recuperación:** El listado no requiere recuperación; inspecciona la referencia o filtro seleccionado si la salida es inesperada.

**Versión y dependencias:** Sintaxis estándar documentada en Git 2.34; no requiere herramienta opcional.

**Capítulos relacionados**

- [branches/04-safe-local-deletion](../../branches/04-safe-local-deletion/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-branch/2.34.0>

## git-branch-upstream

**`git branch --set-upstream-to`**

**Tipo:** Uso de opción

**Nivel:** Intermedio

**Buscar por intención:** Gestionar ramas, Sincronizar repositorios, Configurar Git

**Riesgo:** Cambio de estado. Seguimiento incorrecto puede afectar pull y push posteriores según configuración; verifica git branch -vv antes de sincronizar.

**Finalidad:** Configurar qué rama sigue como upstream una rama local existente.

**Requisitos previos:** Usa clon propio desechable o laboratorio con remoto local. Verifica rama local, referencia de seguimiento remoto existente y relación upstream prevista; no contactes un servicio real para práctica.

**Opciones:** -u abrevia --set-upstream-to; omite argumento de rama local para configurar la actual. --unset-upstream elimina configuración de seguimiento.

**Cuándo utilizar:** Cuando una rama necesita relación de seguimiento explícita verificada para estado y sincronización.

**Cuándo evitar:** Evita seleccionar un destino de integración distinto accidentalmente o suponer que realiza fetch o push.

**Sintaxis**

`git branch --set-upstream-to=origin/main main`

**Ejemplo básico**

`git branch --set-upstream-to=origin/main main`

En laboratorio de clon local, conecta main existente a su referencia origin/main verificada.

**Ejemplo profesional**

`git branch -u origin/feat/notes feat/notes`

Tras comprobar ambas referencias existentes, corrige seguimiento de rama privada de feature en el laboratorio local.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Cambia

**Resultado esperado:** Configuración local de seguimiento identifica upstream elegido; git branch -vv puede mostrar la relación.

**Efectos y efectos secundarios:** Modifica configuración local de rama; no requiere movimiento de referencia, checkout ni transferencia de red.

**Errores comunes:** Confundir configuración upstream con publicación remota o esperar que seguimiento solo mantenga referencias actualizadas.

**Alternativas:** Usa argumentos explícitos de remoto y referencia para fetch o push cuando no desees valores de seguimiento predeterminados.

**Recuperación:** Registra upstream anterior; restáuralo explícitamente o usa git branch --unset-upstream para rama local si no existía ninguno.

**Versión y dependencias:** Sintaxis estándar documentada en Git 2.34; no requiere herramienta opcional.

**Capítulos relacionados**

- [remote-repositories/02-fetch-and-tracking](../../remote-repositories/02-fetch-and-tracking/README.es.md)
- [remote-repositories/03-pull-push-and-divergence](../../remote-repositories/03-pull-push-and-divergence/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-branch/2.34.0>


---

<!-- navigation-footer -->
[Anterior](../05-history-and-comparison/README.es.md) · [Índice](../README.es.md) · [Siguiente](../07-merge-rebase-and-conflicts/README.es.md)
<!-- /navigation-footer -->
