# 04 Commits y etiquetas

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../03-working-tree-and-staging/README.es.md) · [Índice](../README.es.md) · [Siguiente](../05-history-and-comparison/README.es.md)
<!-- /navigation -->

Generado a partir del JSON canónico. Edita los registros, no esta página.

Las entradas describen comandos y operaciones, no una secuencia para ejecutar. Practica en repositorios desechables. Las operaciones alojadas son opcionales.

**Total de entradas distintas: 8**

- [`git commit`](#git-commit)
- [`git commit -a`](#git-commit-all)
- [`git commit --amend`](#git-commit-amend)
- [`git commit --fixup`](#git-commit-fixup)
- [`git tag`](#git-tag)
- [`git tag -a`](#git-tag-annotated)
- [`git tag -d`](#git-tag-delete)
- [`git tag -l`](#git-tag-list)

## git-commit

**`git commit`**

**Tipo:** Comando nativo

**Nivel:** Principiante

**Buscar por intención:** Registrar cambios

**Riesgo:** Cambio de estado. Revisa git diff --cached, identidad y hooks; el commit puede conservar contenido sensible localmente.

**Finalidad:** Registrar la instantánea preparada y revisada como un nuevo commit.

**Requisitos previos:** Usa un repositorio propio desechable con identidad ficticia configurada y cambios preparados revisados.

**Opciones:** -m proporciona el mensaje sin abrir el editor; -v muestra un diff en el editor.

**Cuándo utilizar:** Cuando los cambios preparados forman una unidad coherente de trabajo.

**Cuándo evitar:** No confirmes secretos, cambios ajenos ni conflictos sin resolver.

**Sintaxis**

`git commit -m "message"`

**Ejemplo básico**

`git commit -m "Add notes"`

Tras preparar un archivo ficticio de notas.

**Ejemplo profesional**

`git commit -m "docs: explain setup"`

Registra un cambio de documentación revisado.

**Impacto en el estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / historial: Cambia
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** Un commit ordinario exitoso registra el index y avanza la rama actual o HEAD separado.

**Efectos y efectos secundarios:** Normalmente no cambia el contenido de los archivos; los metadatos del index y hooks locales pueden alterar el estado. No hay push.

**Errores comunes:** Suponer que incluye ediciones no preparadas o que un commit publica cambios.

**Alternativas:** Usa git add -p antes del commit para seleccionar fragmentos individuales.

**Recuperación:** Inspecciona git show HEAD; corrige un error no publicado con amend o considera git revert para un commit compartido tras revisarlo.

**Versión y dependencias:** Sintaxis estándar documentada para Git 2.34; sin herramienta opcional para el comando mostrado. Los hooks locales o la configuración de firma pueden afectar la ejecución.

**Capítulos relacionados**

- [basic-commands/02-status-add-commit](../../basic-commands/02-status-add-commit/README.es.md)
- [getting-started/05-first-commit](../../getting-started/05-first-commit/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-commit/2.34.0>

## git-commit-all

**`git commit -a`**

**Tipo:** Uso de opción

**Nivel:** Intermedio

**Buscar por intención:** Registrar cambios, Preparar cambios

**Riesgo:** Cambio de estado. Puede capturar más de lo previsto; inspecciona diferencias preparadas y no preparadas y configura identidad ficticia primero.

**Finalidad:** Preparar archivos rastreados modificados y eliminados y crear un commit en una operación.

**Requisitos previos:** Usa un repositorio propio desechable; inspecciona el estado y preserva el trabajo valioso.

**Opciones:** -a incluye modificaciones y eliminaciones rastreadas; -m define el mensaje.

**Cuándo utilizar:** Cuando cada cambio rastreado y adición ya preparada pertenece a un commit.

**Cuándo evitar:** Evita cuando existan ediciones o eliminaciones rastreadas ajenas.

**Sintaxis**

`git commit -a -m "message"`

**Ejemplo básico**

`git commit -a -m "Update notes"`

Edita primero un archivo de notas ya rastreado.

**Ejemplo profesional**

`git commit -a -m "docs: fix typos"`

Solo tras revisar todos los cambios rastreados y el index.

**Impacto en el estado**

- Working tree: Condicional
- Index: Cambia
- Objetos / refs / historial: Cambia
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** El nuevo commit incluye actualizaciones rastreadas y contenido ya preparado; los archivos nuevos no preparados siguen sin rastrear.

**Efectos y efectos secundarios:** Actualiza index e historial; el contenido de los archivos normalmente no cambia, sujeto a hooks.

**Errores comunes:** Esperar que incluya archivos no rastreados o pasar por alto eliminaciones rastreadas.

**Alternativas:** Usa rutas explícitas con git add y git commit para delimitar el alcance.

**Recuperación:** Inspecciona el commit resultante; corrige con cuidado el historial no publicado o revierte un commit compartido.

**Versión y dependencias:** Sintaxis estándar documentada para Git 2.34; sin herramienta opcional para el comando mostrado. Los hooks locales o la configuración de firma pueden afectar la ejecución.

**Capítulos relacionados**

- [basic-commands/02-status-add-commit](../../basic-commands/02-status-add-commit/README.es.md)
- [getting-started/05-first-commit](../../getting-started/05-first-commit/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-commit/2.34.0>

## git-commit-amend

**`git commit --amend`**

**Tipo:** Uso de opción

**Nivel:** Intermedio

**Buscar por intención:** Reescribir historial local, Registrar cambios

**Riesgo:** Reescritura del historial. Reescribir historial puede perjudicar a colaboradores; mantén el ejemplo local y no publicado.

**Finalidad:** Sustituir el commit actual de la punta por un commit recién creado.

**Requisitos previos:** Usa un repositorio propio desechable con HEAD existente no publicado, index revisado y referencia guardada al commit anterior.

**Opciones:** --no-edit mantiene el mensaje; -m proporciona un reemplazo; ambos usan la instantánea preparada.

**Cuándo utilizar:** Corregir un commit privado de la punta antes de compartirlo.

**Cuándo evitar:** No reescribas historial compartido sin cuidado ni uses amend con cambios preparados ajenos.

**Sintaxis**

`git commit --amend -m "message"`

**Ejemplo básico**

`git commit --amend -m "Clarify notes"`

Usa una punta privada y verifica un diff preparado vacío para corregir solo el mensaje.

**Ejemplo profesional**

`git commit --amend --no-edit`

Tras preparar un cambio de documentación olvidado para una punta no publicada.

**Impacto en el estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / historial: Cambia
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** El reemplazo normalmente tiene un ID distinto y los mismos padres que la punta anterior.

**Efectos y efectos secundarios:** Mueve la rama local o HEAD separado; el commit anterior puede seguir alcanzable por otra referencia o reflog. Los hooks pueden alterar el estado local.

**Errores comunes:** Tratar --no-edit como cambio solo del mensaje o suponer que el ID anterior sigue válido para la nueva punta.

**Alternativas:** Crea un commit adicional cuando sea importante preservar el historial existente.

**Recuperación:** Inspecciona git reflog y la referencia guardada; crea una rama de recuperación en el ID anterior verificado si sigue disponible. No uses reset a ciegas.

**Versión y dependencias:** Sintaxis estándar documentada para Git 2.34; sin herramienta opcional para el comando mostrado. Los hooks locales o la configuración de firma pueden afectar la ejecución.

**Capítulos relacionados**

- [history-and-recovery/08-amend](../../history-and-recovery/08-amend/README.es.md)
- [basic-commands/02-status-add-commit](../../basic-commands/02-status-add-commit/README.es.md)
- [getting-started/05-first-commit](../../getting-started/05-first-commit/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-commit/2.34.0>

## git-commit-fixup

**`git commit --fixup`**

**Tipo:** Uso de opción

**Nivel:** Avanzado

**Buscar por intención:** Registrar cambios, Reescribir historial local

**Riesgo:** Cambio de estado. Crear el fixup no reescribe historial, pero el autosquash posterior puede hacerlo; guarda una referencia antes del rebase.

**Finalidad:** Crear un commit de corrección separado marcado para un rebase posterior con autosquash.

**Requisitos previos:** Usa un repositorio propio desechable con una corrección preparada revisada y un commit de destino existente en historial no publicado.

**Opciones:** --fixup HEAD apunta a la punta actual; también puede recibir el ID verificado de un commit anterior.

**Cuándo utilizar:** Al preparar correcciones de revisión para incorporarlas después en commits privados.

**Cuándo evitar:** Evita apuntar al commit incorrecto o planear autosquash en historial compartido sin coordinación.

**Sintaxis**

`git commit --fixup HEAD`

**Ejemplo básico**

`git commit --fixup HEAD`

Prepara una pequeña corrección para el commit privado actual.

**Ejemplo profesional**

`git commit --fixup HEAD~1`

Tras verificar que el padre anterior es el destino revisado de la corrección.

**Impacto en el estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / historial: Cambia
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** Se crea un nuevo commit ordinario con asunto fixup!; el destino aún no se sustituye.

**Efectos y efectos secundarios:** Se registra la instantánea del index y HEAD avanza; solo un rebase posterior reescribe historial. Los hooks pueden afectar el estado local.

**Errores comunes:** Suponer que --fixup ya incorpora la corrección al destino.

**Alternativas:** Usa un commit adicional normal cuando se desee preservar cada corrección pública.

**Recuperación:** Inspecciona git log; si el destino era incorrecto, revisa y corrige el fixup no publicado antes de intentar autosquash.

**Versión y dependencias:** Sintaxis estándar documentada para Git 2.34; sin herramienta opcional para el comando mostrado. Los hooks locales o la configuración de firma pueden afectar la ejecución.

**Capítulos relacionados**

- [merge-and-conflicts/07-interactive-rebase](../../merge-and-conflicts/07-interactive-rebase/README.es.md)
- [basic-commands/02-status-add-commit](../../basic-commands/02-status-add-commit/README.es.md)
- [getting-started/05-first-commit](../../getting-started/05-first-commit/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-commit/2.34.0>

## git-tag

**`git tag`**

**Tipo:** Comando nativo

**Nivel:** Principiante

**Buscar por intención:** Gestionar etiquetas, Gestionar versiones

**Riesgo:** Cambio de estado. Verifica el destino y los nombres existentes; los ejemplos suponen tag.gpgSign desactivado para crear una etiqueta ligera.

**Finalidad:** Crear una etiqueta local ligera que apunta directamente a un objeto Git, normalmente un commit.

**Requisitos previos:** Usa un repositorio propio desechable con un commit de destino existente; inspecciona primero las etiquetas y el destino.

**Opciones:** Proporciona un nombre y opcionalmente una revisión de destino; sin destino Git usa HEAD.

**Cuándo utilizar:** Marcar un hito local sin un objeto de etiqueta anotada separado.

**Cuándo evitar:** Evita etiquetas ligeras cuando la política de publicación exige anotaciones o firmas.

**Sintaxis**

`git tag v0.1.0`

**Ejemplo básico**

`git tag v0.1.0`

Marca el commit ficticio actual de práctica.

**Ejemplo profesional**

`git tag review-ready HEAD`

Marca un hito revisado localmente, no una publicación.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Cambia
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Una nueva referencia refs/tags apunta al destino; la ascendencia de commits no cambia.

**Efectos y efectos secundarios:** Cambia solo una referencia local; no hay checkout ni push con configuración ordinaria sin firma.

**Errores comunes:** Suponer que la etiqueta se mueve con la rama o crea una publicación alojada automáticamente.

**Alternativas:** Usa git tag -a para un objeto de etiqueta con metadatos y mensaje.

**Recuperación:** Si una etiqueta no publicada es incorrecta, registra su destino actual, elimínala localmente y recréala en el destino verificado.

**Versión y dependencias:** Sintaxis estándar documentada en Git 2.31; el manual oficial registra ausencia de cambios hasta Git 2.34.8. Sin herramienta opcional para la operación sin firma mostrada.

**Capítulos relacionados**

- [git-internals/03-commits-and-tags](../../git-internals/03-commits-and-tags/README.es.md)
- [professional-workflows/12-release-management](../../professional-workflows/12-release-management/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-tag/2.31.0>

## git-tag-annotated

**`git tag -a`**

**Tipo:** Uso de opción

**Nivel:** Intermedio

**Buscar por intención:** Gestionar etiquetas, Gestionar versiones

**Riesgo:** Cambio de estado. Configura identidad ficticia del etiquetador; verifica destino, mensaje y política de firma. La anotación puede exponer identidad al compartirla.

**Finalidad:** Crear un objeto de etiqueta anotada local y una referencia a él.

**Requisitos previos:** Usa un repositorio propio desechable con un commit de destino existente; inspecciona primero las etiquetas y el destino.

**Opciones:** -a solicita anotación; -m proporciona el mensaje; -s solicita una firma por separado.

**Cuándo utilizar:** Al marcar una publicación con metadatos del etiquetador y un mensaje.

**Cuándo evitar:** Evita sustituir una etiqueta de versión ya publicada o tratar la anotación como prueba de firma.

**Sintaxis**

`git tag -a v1.0.0 -m "Release 1.0.0"`

**Ejemplo básico**

`git tag -a v1.0.0 -m "Release 1.0.0"`

Marca el commit de práctica actual revisado.

**Ejemplo profesional**

`git tag -a v1.2.0 -m "Stable release" HEAD`

Tras verificar el destino y la lista local de publicación.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Cambia
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Una referencia refs/tags apunta a un objeto de etiqueta que identifica el destino y contiene metadatos de anotación.

**Efectos y efectos secundarios:** Crea un objeto y referencia local; la ascendencia de commits, archivos, index y remoto no se modifican.

**Errores comunes:** Confundir etiqueta anotada con etiqueta firmada o publicación alojada.

**Alternativas:** Usa una etiqueta ligera git tag para un marcador local temporal cuando la política lo permita.

**Recuperación:** Inspecciona git show en la etiqueta; si no está publicada, conserva el ID anterior del objeto antes de corregirla. Para etiquetas publicadas coordina una nueva versión.

**Versión y dependencias:** Sintaxis estándar documentada en Git 2.31; el manual oficial registra ausencia de cambios hasta Git 2.34.8. Sin herramienta opcional para la operación sin firma mostrada.

**Capítulos relacionados**

- [git-internals/03-commits-and-tags](../../git-internals/03-commits-and-tags/README.es.md)
- [professional-workflows/12-release-management](../../professional-workflows/12-release-management/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-tag/2.31.0>

## git-tag-delete

**`git tag -d`**

**Tipo:** Uso de opción

**Nivel:** Intermedio

**Buscar por intención:** Gestionar etiquetas, Deshacer cambios

**Riesgo:** Destructivo. La eliminación pierde una referencia; registra git rev-parse refs/tags/name antes de eliminar. La recuperación no está garantizada.

**Finalidad:** Eliminar una referencia de etiqueta local por nombre.

**Requisitos previos:** Usa un repositorio propio desechable; verifica una etiqueta existente no publicada y guarda primero el ID exacto del objeto de la referencia.

**Opciones:** -d elimina una o más etiquetas locales por nombre; no es una eliminación remota.

**Cuándo utilizar:** Al eliminar un marcador privado de práctica obsoleto.

**Cuándo evitar:** Evita eliminar etiquetas de versión publicadas o la única referencia a objetos importantes sin plan de recuperación.

**Sintaxis**

`git tag -d v0.1.0`

**Ejemplo básico**

`git tag -d v0.1.0`

Elimina una etiqueta local desechable verificada.

**Ejemplo profesional**

`git tag -d review-ready`

Elimina un marcador privado de revisión tras preservar el ID de destino.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Cambia
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** La referencia local nombrada deja de existir; las etiquetas remotas no cambian.

**Efectos y efectos secundarios:** Puede dejar un objeto de etiqueta o destino inalcanzable si ninguna otra referencia lo conserva; el comando no borra objetos inmediatamente.

**Errores comunes:** Suponer que eliminar localmente borra la etiqueta remota o que el objeto anotado exacto es fácil de reconstruir.

**Alternativas:** Conserva la etiqueta y crea un nuevo marcador de versión cuando se haya compartido.

**Recuperación:** Si el objeto exacto sigue disponible, recrea la referencia verificada con git update-ref; una etiqueta anotada no se restaura fielmente solo etiquetando de nuevo su commit.

**Versión y dependencias:** Sintaxis estándar documentada en Git 2.31; el manual oficial registra ausencia de cambios hasta Git 2.34.8. Sin herramienta opcional para la operación sin firma mostrada.

**Capítulos relacionados**

- [git-internals/03-commits-and-tags](../../git-internals/03-commits-and-tags/README.es.md)
- [professional-workflows/12-release-management](../../professional-workflows/12-release-management/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-tag/2.31.0>

## git-tag-list

**`git tag -l`**

**Tipo:** Uso de opción

**Nivel:** Principiante

**Buscar por intención:** Gestionar etiquetas, Inspeccionar referencias

**Riesgo:** Solo lectura. Listado de solo lectura; no obtiene etiquetas ni verifica contenido de publicaciones.

**Finalidad:** Listar nombres de etiquetas locales, opcionalmente coincidentes con un patrón.

**Requisitos previos:** Usa un repositorio propio; una etiqueta coincidente es opcional.

**Opciones:** -l activa el listado; entrecomilla patrones glob para que el shell los pase a Git; --sort permite seleccionar clave de ordenación.

**Cuándo utilizar:** Al comprobar nombres de publicaciones locales existentes o seleccionar un punto de comparación.

**Cuándo evitar:** No trates la lista local como lista oficial de etiquetas remotas.

**Sintaxis**

`git tag -l "v1.*"`

**Ejemplo básico**

`git tag -l`

Inspecciona todos los nombres de etiquetas locales.

**Ejemplo profesional**

`git tag -l "v1.*" --sort=version:refname`

Lista etiquetas ficticias de versiones coincidentes en orden de versión.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Se muestran nombres de etiquetas coincidentes; un patrón sin coincidencias no produce nombres.

**Efectos y efectos secundarios:** No se modifican referencias, objetos locales ni estado remoto.

**Errores comunes:** Dejar un comodín sin comillas o suponer que el orden léxico equivale al orden de versiones.

**Alternativas:** Usa git show-ref --tags para inspeccionar referencias de etiquetas e IDs de objetos.

**Recuperación:** El listado no requiere recuperación; inspecciona patrón y referencias locales si el resultado es inesperado.

**Versión y dependencias:** Sintaxis estándar documentada en Git 2.31; el manual oficial registra ausencia de cambios hasta Git 2.34.8. Sin herramienta opcional para la operación sin firma mostrada.

**Capítulos relacionados**

- [git-internals/03-commits-and-tags](../../git-internals/03-commits-and-tags/README.es.md)
- [professional-workflows/12-release-management](../../professional-workflows/12-release-management/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-tag/2.31.0>


---

<!-- navigation-footer -->
[Anterior](../03-working-tree-and-staging/README.es.md) · [Índice](../README.es.md) · [Siguiente](../05-history-and-comparison/README.es.md)
<!-- /navigation-footer -->
