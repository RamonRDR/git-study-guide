# 11 Operaciones avanzadas

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../10-search-and-troubleshooting/README.es.md) · [Índice](../README.es.md) · [Siguiente](../12-internals-and-plumbing/README.es.md)
<!-- /navigation -->

Generado a partir del JSON canónico. Edita los registros, no esta página.

Las entradas describen comandos y operaciones, no una secuencia para ejecutar. Practica en repositorios desechables. Las operaciones alojadas son opcionales.

**Total de entradas distintas: 9**

- [`git worktree add`](#git-worktree-add)
- [`git submodule add`](#git-submodule-add)
- [`git submodule update --init --recursive`](#git-submodule-update)
- [`git subtree add`](#git-subtree-add)
- [`git rerere`](#git-rerere)
- [`git sparse-checkout set`](#git-sparse-checkout-set)
- [`git clone --filter`](#git-clone-filter)
- [`git archive`](#git-archive)
- [`git bundle create`](#git-bundle-create)

## git-worktree-add

**`git worktree add`**

**Tipo:** Subcomando

**Nivel:** Avanzado

**Buscar por intención:** Trabajar en paralelo, Gestionar ramas

**Riesgo:** Cambio de estado. Revisa rutas, referencias y configuración local primero. Conserva trabajo valioso; nunca pruebes contra el guía o servicio compartido.

**Finalidad:** Crear checkout vinculado adicional compartiendo objetos y mayoría de referencias.

**Requisitos previos:** Usa repositorio propio desechable limpio con trabajo guardado, rutas locales y referencias verificadas y configuración confiable. Usa solo fuentes locales propias.

**Opciones:** -b crea rama; --detach usa checkout separado; git worktree list muestra worktrees registradas.

**Cuándo utilizar:** Al trabajar en tareas independientes sin alternar repetidamente checkout original.

**Cuándo evitar:** Evita reutilizar ruta ocupada o forzar misma rama en múltiples worktrees.

**Sintaxis**

`git worktree add -b feat/notes ../notes-lab main`

**Ejemplo básico**

`git worktree add -b feat/notes ../notes-lab main`

Crea worktree vinculada en ruta vecina libre y rama nueva.

**Ejemplo profesional**

`git worktree add --detach ../review-lab main`

Inspecciona main verificada en checkout separado.

**Impacto en el estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / historial: Condicional
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** Crea checkout vinculado con HEAD e index propios; rama nueva opcional se comparte entre worktrees.

**Efectos y efectos secundarios:** Crea archivos y metadatos de worktree, posiblemente referencia nueva; contenido de checkout original no cambia en forma mostrada.

**Errores comunes:** Tratar worktrees vinculadas como clones independientes o borrar directorios manualmente.

**Alternativas:** Usa clon separado cuando se requieran referencias y almacenamiento de objetos independientes.

**Recuperación:** Conserva ediciones de worktree vinculada, comprueba estado limpio allí, luego usa git worktree remove con ruta exacta; inspecciona worktree list después.

**Versión y dependencias:** Usa Git 2.40 o superior en laboratorios del guía; verifica disponibilidad en ayuda local Git.

**Capítulos relacionados**

- [advanced-git/02-worktree](../../advanced-git/02-worktree/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-worktree>

## git-submodule-add

**`git submodule add`**

**Tipo:** Subcomando

**Nivel:** Avanzado

**Buscar por intención:** Gestionar dependencias de repositorios

**Riesgo:** Cambio de estado. Revisa rutas, referencias y configuración local primero. Conserva trabajo valioso; nunca pruebes contra el guía o servicio compartido.

**Finalidad:** Registrar repositorio separado como submódulo fijado por gitlink en proyecto padre.

**Requisitos previos:** Usa repositorio propio desechable limpio con trabajo guardado, rutas locales y referencias verificadas y configuración confiable. Usa solo fuentes locales propias. Para la URL relativa mostrada, asegúrate de que la biblioteca sea vecina del remoto predeterminado del padre (o del repositorio padre local si no hay remoto predeterminado).

**Opciones:** Indica repositorio y ruta; -b configura preferencia de rama para actualizaciones remotas, no sustituye gitlink registrado. Las URL relativas se resuelven respecto al remoto predeterminado del repositorio padre, o al repositorio local si no hay remoto predeterminado configurado; organiza orígenes bare vecinos para simular clones.

**Cuándo utilizar:** Cuando dependencia debe conservar historial independiente y versión fijada explícitamente.

**Cuándo evitar:** Evita URLs de submódulos no confiables, archivos valiosos en destino o permisos amplios de protocolo.

**Sintaxis**

`git submodule add ../library.git vendor/library`

**Ejemplo básico**

`git submodule add ../library.git vendor/library`

Añade repositorio local propio poblado de biblioteca en ruta libre; transporte file local puede requerir permiso explícito de laboratorio.

**Ejemplo profesional**

`git -c protocol.file.allow=always submodule add ../library.git vendor/library`

Solo en laboratorio aislado confiable, permite fuente local propia en esta invocación.

**Impacto en el estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / historial: Condicional
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** Normalmente crea checkout de submódulo, prepara .gitmodules y gitlink; commit padre aún requiere revisión y confirmación.

**Efectos y efectos secundarios:** Cambia archivos, index y configuración u objetos locales de submódulo; no publica proyecto padre.

**Errores comunes:** Suponer submódulo como archivos ordinarios copiados o cambios sin confirmar incluidos en commit padre.

**Alternativas:** Usa integración subtree o gestor de paquetes cuando checkout separado no sea deseado.

**Recuperación:** Inspecciona .gitmodules, gitlink preparado y estado del submódulo; conserva commits del submódulo antes de flujo revisado de eliminación. No borres metadatos sin más.

**Versión y dependencias:** Usa Git 2.40 o superior en laboratorios del guía; verifica disponibilidad en ayuda local Git.

**Capítulos relacionados**

- [advanced-git/03-submodules](../../advanced-git/03-submodules/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-submodule>

## git-submodule-update

**`git submodule update --init --recursive`**

**Tipo:** Uso de opción

**Nivel:** Avanzado

**Buscar por intención:** Gestionar dependencias de repositorios, Sincronizar repositorios

**Riesgo:** Cambio de estado. Revisa rutas, referencias y configuración local primero. Conserva trabajo valioso; nunca pruebes contra el guía o servicio compartido.

**Finalidad:** Poblar submódulos registrados y actualizar checkouts, normalmente a commits registrados por padre.

**Requisitos previos:** Usa repositorio propio desechable limpio con trabajo guardado, rutas locales y referencias verificadas y configuración confiable. Usa solo fuentes locales propias. Revisa las URL relativas resueltas antes de inicializar; en laboratorio, clona desde un origen bare padre vecino para que se resuelva correctamente la URL relativa de la biblioteca.

**Opciones:** --init inicializa submódulos no inicializados; --recursive desciende a anidados; procedimiento predeterminado de checkout normalmente separa HEAD del submódulo.

**Cuándo utilizar:** Al preparar checkout consistente de proyecto con dependencias fijadas.

**Cuándo evitar:** Evita URLs anidadas no revisadas, cambios de submódulos no preservados o --force para evitar rechazo.

**Sintaxis**

`git submodule update --init --recursive`

**Ejemplo básico**

`git submodule update --init --recursive`

Inicializa y actualiza submódulos confiables registrados a commits registrados en laboratorio.

**Ejemplo profesional**

`git -c protocol.file.allow=always submodule update --init --recursive`

Solo para URLs de submódulos locales propios revisados, permite transporte file local en esta invocación.

**Impacto en el estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / historial: Condicional
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** Puede clonar submódulos ausentes, obtener objetos y seleccionar commits registrados; estrategias configuradas pueden diferir.

**Efectos y efectos secundarios:** Cambia archivos, index, referencias y configuración de submódulo; normalmente no mueve punta de rama padre.

**Errores comunes:** Esperar últimas versiones de ramas remotas en vez de commits registrados o suponer estado padre prueba checkouts anidados limpios.

**Alternativas:** Usa git submodule status --recursive para inspeccionar sin actualizar.

**Recuperación:** Inspecciona rutas fallidas y puntas guardadas de submódulos; conserva commits separados con rama nombrada antes de reintentar. No fuerces a ciegas.

**Versión y dependencias:** Usa Git 2.40 o superior en laboratorios del guía; verifica disponibilidad en ayuda local Git.

**Capítulos relacionados**

- [advanced-git/03-submodules](../../advanced-git/03-submodules/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-submodule>

## git-subtree-add

**`git subtree add`**

**Tipo:** Herramienta externa

**Nivel:** Avanzado

**Buscar por intención:** Gestionar dependencias de repositorios, Integrar cambios

**Riesgo:** Cambio de estado. Revisa rutas, referencias y configuración local primero. Conserva trabajo valioso; nunca pruebes contra el guía o servicio compartido.

**Finalidad:** Importar contenido de otro repositorio en directorio del proyecto actual con helper subtree opcional.

**Requisitos previos:** Usa repositorio propio desechable limpio con trabajo guardado, rutas locales y referencias verificadas y configuración confiable. Usa solo fuentes locales propias.

**Opciones:** --prefix selecciona destino; --squash combina historial importado en vez de conservar cada commit fuente en ascendencia destino.

**Cuándo utilizar:** Al versionar contenido de dependencia directamente en checkout padre conservando flujo de sincronización.

**Cuándo evitar:** Evita prefijo ocupado, estado sucio o importación sin revisar licencia y contenido.

**Sintaxis**

`git subtree add --prefix=vendor/library ../library.git main --squash`

**Ejemplo básico**

`git subtree add --prefix=vendor/library ../library.git main --squash`

Importa rama fuente local propia en prefijo libre.

**Ejemplo profesional**

`git subtree add --prefix=vendor/tools ../tools.git main --squash`

Integra instantánea local de herramientas revisada bajo directorio nuevo.

**Impacto en el estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / historial: Condicional
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** Con éxito crea historial de integración e importa contenido fuente bajo prefijo seleccionado.

**Efectos y efectos secundarios:** Puede obtener objetos, crear commits, avanzar rama actual y actualizar index y working tree.

**Errores comunes:** Confundir subtree con submódulo o suponer --squash no produce commit de integración.

**Alternativas:** Usa submódulo para checkout fijado separado o gestor de paquetes para dependencias publicadas.

**Recuperación:** Inspecciona punta original guardada y ascendencia resultante; si inadecuada, conserva trabajo y elige recuperación privada revisada o corrección compartida.

**Versión y dependencias:** Git subtree es helper distribuido opcional; verifica disponibilidad de git subtree antes de usar. Usa Git 2.40 o superior en laboratorios.

**Capítulos relacionados**

- [advanced-git/04-subtree](../../advanced-git/04-subtree/README.es.md)

**Documentación oficial**

- <https://github.com/git/git/tree/master/contrib/subtree>

## git-rerere

**`git rerere`**

**Tipo:** Comando nativo

**Nivel:** Avanzado

**Buscar por intención:** Resolver conflictos

**Riesgo:** Cambio de estado. Revisa rutas, referencias y configuración local primero. Conserva trabajo valioso; nunca pruebes contra el guía o servicio compartido.

**Finalidad:** Registrar y reutilizar resoluciones para patrones de conflicto coincidentes.

**Requisitos previos:** Usa repositorio propio desechable limpio con trabajo guardado, rutas locales y referencias verificadas y configuración confiable. Usa solo fuentes locales propias.

**Opciones:** Habilita rerere.enabled localmente en laboratorio; git rerere status y diff inspeccionan registros actuales; autoupdate puede preparar resultados reutilizados.

**Cuándo utilizar:** Al resolver repetidamente conflictos similares en flujos privados de integración.

**Cuándo evitar:** Evita aceptar resoluciones reutilizadas a ciegas o compartir caché con material sensible.

**Sintaxis**

`git rerere`

**Ejemplo básico**

`git rerere`

En laboratorio desechable de conflictos repetidos, inspecciona y registra o reutiliza resolución según corresponda.

**Ejemplo profesional**

`git rerere`

Tras revisar conflicto repetido, permite rerere habilitado reutilizar resolución registrada e inspecciónala.

**Impacto en el estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / historial: Condicional
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** Puede registrar conflictos y resoluciones o aplicar coincidencia registrada; index puede actualizarse según configuración.

**Efectos y efectos secundarios:** Puede cambiar caché de resolución y archivos, y posiblemente index; rerere ordinario no crea commit nuevo en rama.

**Errores comunes:** Suponer texto de conflicto coincidente garantiza corrección semántica.

**Alternativas:** Resuelve manualmente y revisa diff y pruebas cuando reutilización sea insegura.

**Recuperación:** Inspecciona rerere diff y estado; corrige y prepara contenido revisado. Usa rerere forget solo para ruta afectada verificada al reemplazar resolución registrada incorrecta.

**Versión y dependencias:** Usa Git 2.40 o superior en laboratorios del guía; verifica disponibilidad en ayuda local Git.

**Capítulos relacionados**

- [advanced-git/06-rerere](../../advanced-git/06-rerere/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-rerere>

## git-sparse-checkout-set

**`git sparse-checkout set`**

**Tipo:** Subcomando

**Nivel:** Avanzado

**Buscar por intención:** Limitar checkout o clonación, Inspeccionar archivos

**Riesgo:** Cambio de estado. Revisa rutas, referencias y configuración local primero. Conserva trabajo valioso; nunca pruebes contra el guía o servicio compartido.

**Finalidad:** Configurar working tree dispersa con rutas seleccionadas en vez de toda ruta rastreada.

**Requisitos previos:** Usa repositorio propio desechable limpio con trabajo guardado, rutas locales y referencias verificadas y configuración confiable. Usa solo fuentes locales propias.

**Opciones:** --cone selecciona reglas por directorio; list muestra selecciones; disable vuelve a checkout completo.

**Cuándo utilizar:** Cuando solo parte de repositorio grande se necesita para trabajo actual.

**Cuándo evitar:** Evita cambiar patrones dispersos con ediciones valiosas sin guardar o suponer rutas omitidas eliminadas del historial.

**Sintaxis**

`git sparse-checkout set --cone docs`

**Ejemplo básico**

`git sparse-checkout set --cone docs`

Selecciona directorio docs existente en checkout desechable limpio.

**Ejemplo profesional**

`git sparse-checkout set --cone src tests`

Limita contenido materializado a directorios existentes seleccionados de código y pruebas, más reglas cone.

**Impacto en el estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / historial: Condicional
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** Working tree materializa rutas seleccionadas según reglas cone, incluidos algunos archivos de niveles ancestros; otras rutas rastreadas pueden faltar.

**Efectos y efectos secundarios:** Actualiza configuración dispersa, index y working tree; no reescribe historial confirmado en repositorio local completo ordinario.

**Errores comunes:** Confundir checkout disperso con clon superficial o parcial y suponer solo directorios nombrados visibles.

**Alternativas:** Usa checkout completo si herramientas necesitan todos archivos rastreados; clon parcial controla transferencia de objetos por separado.

**Recuperación:** Conserva ediciones, inspecciona sparse-checkout list y usa sparse-checkout disable para restaurar materialización completa cuando sea seguro.

**Versión y dependencias:** Usa Git 2.40 o superior en laboratorios del guía; verifica disponibilidad en ayuda local Git.

**Capítulos relacionados**

- [advanced-git/07-sparse-checkout](../../advanced-git/07-sparse-checkout/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-sparse-checkout>

## git-clone-filter

**`git clone --filter`**

**Tipo:** Uso de opción

**Nivel:** Avanzado

**Buscar por intención:** Limitar checkout o clonación, Crear repositorio

**Riesgo:** Cambio de estado. Revisa rutas, referencias y configuración local primero. Conserva trabajo valioso; nunca pruebes contra el guía o servicio compartido.

**Finalidad:** Solicitar clon parcial que omite inicialmente tipos de objeto seleccionados cuando fuente admite filtrado.

**Requisitos previos:** Usa directorio padre desechable, destino libre y fuente bare propia configurada localmente con uploadpack.allowFilter=true; verifica ruta y capacidad.

**Opciones:** --filter=blob:none solicita omisión de blobs hasta necesitarlos; --no-checkout evita checkout inicial; --no-local usa transporte en vez de optimización de copia local.

**Cuándo utilizar:** Al reducir transferencia inicial de objetos desde fuente grande compatible.

**Cuándo evitar:** Evita depender de objetos ausentes disponibles offline o suponer todo servidor respeta filtros.

**Sintaxis**

`git clone --no-local --filter=blob:none --no-checkout origin.git partial-lab`

**Ejemplo básico**

`git clone --no-local --filter=blob:none --no-checkout origin.git partial-lab`

Desde directorio padre desechable, clona fuente bare local propia configurada para permitir filtrado.

**Ejemplo profesional**

`git clone --no-local --filter=blob:none origin.git review-lab`

Clona fuente propia capaz de filtrar; checkout puede obtener blobs necesarios inmediatamente.

**Impacto en el estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / historial: Condicional
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** Crea clon parcial local con configuración promisor cuando se admite; objetos ausentes necesarios pueden obtenerse después.

**Efectos y efectos secundarios:** Crea repositorio local y puede materializar archivos y obtener blobs; no cambia referencias fuente.

**Errores comunes:** Confundir --filter con --depth o tratar éxito de clon como prueba de aplicación del filtro.

**Alternativas:** Usa clon completo para acceso offline confiable a objetos; usa sparse-checkout para selección de working tree.

**Recuperación:** Inspecciona avisos de clon y configuración promisor; si filtro no se admite, usa destino nuevo limpio con clon completo o fuente compatible verificada.

**Versión y dependencias:** Usa Git 2.40 o superior en laboratorios del guía; verifica disponibilidad en ayuda local Git.

**Capítulos relacionados**

- [advanced-git/08-partial-and-shallow-clone](../../advanced-git/08-partial-and-shallow-clone/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-clone>

## git-archive

**`git archive`**

**Tipo:** Comando nativo

**Nivel:** Avanzado

**Buscar por intención:** Empaquetar historial o archivos

**Riesgo:** Cambio de estado. Revisa rutas, referencias y configuración local primero. Conserva trabajo valioso; nunca pruebes contra el guía o servicio compartido.

**Finalidad:** Exportar contenido de árbol confirmado seleccionado como archivo sin historial Git.

**Requisitos previos:** Usa repositorio propio desechable limpio con trabajo guardado, rutas locales y referencias verificadas y configuración confiable. Usa solo fuentes locales propias.

**Opciones:** --format selecciona formato; --output nombra salida; --prefix antepone rutas; atributos export-ignore pueden omitir rutas.

**Cuándo utilizar:** Al preparar instantánea de código revisada para distribución o inspección.

**Cuándo evitar:** Evita sobrescribir artefactos existentes, exportar secretos o suponer contenido de submódulo incluido recursivamente.

**Sintaxis**

`git archive --format=tar --output=../snapshot.tar HEAD`

**Ejemplo básico**

`git archive --format=tar --output=../snapshot.tar HEAD`

Escribe archivo de árbol confirmado verificado en archivo vecino libre.

**Ejemplo profesional**

`git archive --format=zip --prefix=release/ --output=../release.zip v1.0.0`

Empaqueta etiqueta de versión existente verificada en ZIP local nuevo.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Cambia

**Resultado esperado:** Crea archivo de árbol seleccionado con atributos de exportación aplicables; ediciones sin confirmar y metadatos Git no se incluyen.

**Efectos y efectos secundarios:** Escribe archivo externo nombrado; operación mostrada no cambia referencias, index o archivos rastreados.

**Errores comunes:** Tratar archivo como copia de repositorio o suponer inclusión de ediciones del working tree.

**Alternativas:** Usa git bundle para transferir referencias seleccionadas e historial de commits.

**Recuperación:** Verifica contenido del archivo y destino; recrea con nombre nuevo si necesario. No borres archivos ajenos.

**Versión y dependencias:** Usa Git 2.40 o superior en laboratorios del guía; verifica disponibilidad en ayuda local Git.

**Capítulos relacionados**

- [advanced-git/10-archive-and-bundle](../../advanced-git/10-archive-and-bundle/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-archive>

## git-bundle-create

**`git bundle create`**

**Tipo:** Subcomando

**Nivel:** Avanzado

**Buscar por intención:** Empaquetar historial o archivos, Recuperar trabajo

**Riesgo:** Cambio de estado. Revisa rutas, referencias y configuración local primero. Conserva trabajo valioso; nunca pruebes contra el guía o servicio compartido.

**Finalidad:** Empaquetar referencias Git seleccionadas y objetos alcanzables para transporte offline.

**Requisitos previos:** Usa repositorio propio desechable limpio con trabajo guardado, rutas locales y referencias verificadas y configuración confiable. Usa solo fuentes locales propias.

**Opciones:** --all selecciona referencias ampliamente; rangos pueden crear bundles incrementales que requieren objetos previos; git bundle verify comprueba aplicabilidad.

**Cuándo utilizar:** Al transferir historial confirmado seleccionado sin conexión remota activa.

**Cuándo evitar:** Evita empaquetar historial privado sin revisar o tratarlo como copia completa de configuración y trabajo sin confirmar.

**Sintaxis**

`git bundle create ../main.bundle main`

**Ejemplo básico**

`git bundle create ../main.bundle main`

Crea bundle de referencia main local verificada en ruta libre.

**Ejemplo profesional**

`git bundle create ../transfer.bundle --all`

Tras revisar cada referencia seleccionada e historial por contenido sensible, crea bundle local de transferencia.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Cambia

**Resultado esperado:** Crea bundle con referencias anunciadas seleccionadas y datos de objetos necesarios; formas incrementales pueden requerir objetos base existentes.

**Efectos y efectos secundarios:** Escribe artefacto de salida fuera del checkout; creación mostrada no actualiza referencias actuales ni remoto.

**Errores comunes:** Suponer --all captura archivos no rastreados, reflogs, hooks y metadatos de plataforma.

**Alternativas:** Usa archive para instantánea de código; usa copia separada verificada para todos datos de repositorio y trabajo.

**Recuperación:** Ejecuta git bundle verify e inspecciona referencias anunciadas; prueba clon o fetch en destino desechable antes de depender del artefacto.

**Versión y dependencias:** Usa Git 2.40 o superior en laboratorios del guía; verifica disponibilidad en ayuda local Git.

**Capítulos relacionados**

- [advanced-git/10-archive-and-bundle](../../advanced-git/10-archive-and-bundle/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-bundle>


---

<!-- navigation-footer -->
[Anterior](../10-search-and-troubleshooting/README.es.md) · [Índice](../README.es.md) · [Siguiente](../12-internals-and-plumbing/README.es.md)
<!-- /navigation-footer -->
