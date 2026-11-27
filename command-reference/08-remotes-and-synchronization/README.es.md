# 08 Remotos y sincronización

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../07-merge-rebase-and-conflicts/README.es.md) · [Índice](../README.es.md) · [Siguiente](../09-recovery-and-stash/README.es.md)
<!-- /navigation -->

Generado a partir del JSON canónico. Edita los registros, no esta página.

Las entradas describen comandos y operaciones, no una secuencia para ejecutar. Practica en repositorios desechables. Las operaciones alojadas son opcionales.

**Total de entradas distintas: 7**

- [`git clone`](#git-clone)
- [`git remote add`](#git-remote-add)
- [`git fetch`](#git-fetch)
- [`git pull --ff-only`](#git-pull-ff-only)
- [`git push`](#git-push)
- [`git push --delete`](#git-push-delete)
- [`git push --force-with-lease`](#git-push-force-with-lease)

## git-clone

**`git clone`**

**Tipo:** Comando nativo

**Nivel:** Principiante

**Buscar por intención:** Crear repositorio, Sincronizar repositorios

**Riesgo:** Cambio de estado. Verifica origen y destino; trata código seleccionado y configuración local como no confiables hasta revisión.

**Finalidad:** Crear repositorio local desde repositorio existente y normalmente seleccionar su rama inicial.

**Requisitos previos:** Usa directorio padre propio desechable, origen local confiable existente y nombre de destino libre.

**Opciones:** Indica origen y destino opcional; --no-checkout omite checkout inicial; --branch selecciona rama o etiqueta inicial.

**Cuándo utilizar:** Al obtener copia de trabajo independiente de proyecto existente.

**Cuándo evitar:** Evita clonar repositorios no confiables en directorios importantes o tratar clon como copia íntegra de todos datos del servidor.

**Sintaxis**

`git clone origin.git learner`

**Ejemplo básico**

`git clone origin.git learner`

Desde directorio padre desechable, clona repositorio bare local existente y poblado.

**Ejemplo profesional**

`git clone --branch main origin.git reviewer`

Crea segundo clon local para simulación de revisión; main debe existir.

**Impacto en el estado**

- Working tree: Cambia
- Index: Cambia
- Objetos / refs / historial: Cambia
- Repositorio remoto: Sin cambios
- Otros estados: Cambia

**Resultado esperado:** Normalmente crea destino con objetos Git, configuración origin, referencias de seguimiento remoto y rama seleccionada; repositorios vacíos y opciones pueden diferir.

**Efectos y efectos secundarios:** Crea nuevo repositorio y archivos locales; no publica cambios al origen.

**Errores comunes:** Suponer que clon copia issues, permisos, configuración CI o todas referencias remotas.

**Alternativas:** Usa git init con remoto explícito al iniciar proyecto nuevo en vez de copiar existente.

**Recuperación:** Si clon falla, inspecciona error y destino; reintenta en nuevo directorio vacío sin eliminar archivos ajenos.

**Versión y dependencias:** Sintaxis estándar Git; usa Git 2.40 o superior en laboratorios del guía. Servicios alojados pueden requerir autenticación y permisos; ejemplos usan solo rutas locales.

**Capítulos relacionados**

- [remote-repositories/01-remote-concepts](../../remote-repositories/01-remote-concepts/README.es.md)
- [remote-repositories/02-fetch-and-tracking](../../remote-repositories/02-fetch-and-tracking/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-clone>

## git-remote-add

**`git remote add`**

**Tipo:** Subcomando

**Nivel:** Principiante

**Buscar por intención:** Gestionar remotos, Configurar Git

**Riesgo:** Cambio de estado. Confirma remoto y referencia de destino exacta. Nunca practiques contra el guía o servicio compartido real; no publiques secretos.

**Finalidad:** Registrar remoto con nombre y mapeo predeterminado de fetch en configuración local.

**Requisitos previos:** Usa solo laboratorio propio desechable con remoto local. Verifica repositorio, ruta remota, referencias, estado e identidad ficticia antes de operar.

**Opciones:** Indica nombre remoto libre y URL o ruta; git remote -v muestra URLs configuradas; -f también haría fetch.

**Cuándo utilizar:** Al conectar repositorio local existente a remoto propio.

**Cuándo evitar:** Evita insertar credenciales en URLs o añadir destino no verificado.

**Sintaxis**

`git remote add origin ../origin.git`

**Ejemplo básico**

`git remote add origin ../origin.git`

Conecta repositorio de práctica actual a bare vecino.

**Ejemplo profesional**

`git remote add review ../review.git`

Registra segundo remoto propio de laboratorio sin obtener ni publicar.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Cambia

**Resultado esperado:** Configuración local contiene nombre, URL y mapeo de fetch; add ordinario no lo contacta.

**Efectos y efectos secundarios:** Cambia solo configuración local en la forma mostrada; no transfiere objetos ni cambia referencias remotas.

**Errores comunes:** Intentar añadir origin existente o suponer que añadir sube commits automáticamente.

**Alternativas:** Usa git remote set-url para corregir remoto existente verificado; inspecciona git remote get-url primero.

**Recuperación:** Si se añadió mal y sin uso, verifica nombre y elimina con git remote remove; eliminación también puede borrar referencias de seguimiento y configuración asociadas.

**Versión y dependencias:** Sintaxis estándar Git; usa Git 2.40 o superior en laboratorios del guía. Servicios alojados pueden requerir autenticación y permisos; ejemplos usan solo rutas locales.

**Capítulos relacionados**

- [remote-repositories/01-remote-concepts](../../remote-repositories/01-remote-concepts/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-remote>

## git-fetch

**`git fetch`**

**Tipo:** Comando nativo

**Nivel:** Principiante

**Buscar por intención:** Sincronizar repositorios, Inspeccionar referencias

**Riesgo:** Cambio de estado. Confirma remoto y referencia de destino exacta. Nunca practiques contra el guía o servicio compartido real; no publiques secretos.

**Finalidad:** Obtener objetos remotos y actualizar referencias locales según mapeo de fetch.

**Requisitos previos:** Usa solo laboratorio propio desechable con remoto local. Verifica repositorio, ruta remota, referencias, estado e identidad ficticia antes de operar.

**Opciones:** Indica remoto; --prune elimina referencias de destino obsoletas según refspecs, normalmente ramas de seguimiento remoto; inspecciona mapeos personalizados primero.

**Cuándo utilizar:** Al inspeccionar progreso remoto antes de decidir cómo integrarlo.

**Cuándo evitar:** Evita refspecs personalizados sin revisar o suponer que código obtenido es confiable.

**Sintaxis**

`git fetch origin`

**Ejemplo básico**

`git fetch origin`

Actualiza referencias de seguimiento desde bare local propio.

**Ejemplo profesional**

`git fetch --prune origin`

Con mapeo estándar de ramas verificado, elimina referencias obsoletas tras limpieza remota aprobada.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Condicional
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** Fetch ordinario actualiza referencias de seguimiento y FETCH\_HEAD según corresponda; rama local actual y archivos normalmente permanecen sin cambios.

**Efectos y efectos secundarios:** Puede añadir objetos, actualizar referencias y ejecutar mantenimiento; fetch ordinario mostrado no integra rama seleccionada ni actualiza referencias de origen.

**Errores comunes:** Confundir origin/main con estado remoto en tiempo real o suponer que fetch actualiza main directamente.

**Alternativas:** Usa git pull --ff-only cuando también se pretenda integración fast-forward verificada.

**Recuperación:** Si fetch actualiza referencia inesperada, inspecciona mapeo e IDs guardados; no restablezcas a ciegas. Referencias podadas solo pueden obtenerse de nuevo si disponibles en origen o recuperadas de objetos conservados.

**Versión y dependencias:** Sintaxis estándar Git; usa Git 2.40 o superior en laboratorios del guía. Servicios alojados pueden requerir autenticación y permisos; ejemplos usan solo rutas locales.

**Capítulos relacionados**

- [remote-repositories/02-fetch-and-tracking](../../remote-repositories/02-fetch-and-tracking/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-fetch>

## git-pull-ff-only

**`git pull --ff-only`**

**Tipo:** Uso de opción

**Nivel:** Intermedio

**Buscar por intención:** Sincronizar repositorios, Integrar cambios, Proteger historial

**Riesgo:** Cambio de estado. Confirma remoto y referencia de destino exacta. Nunca practiques contra el guía o servicio compartido real; no publiques secretos.

**Finalidad:** Obtener cambios remotos e integrar solo cuando resultado fast-forward o ya contenido sea posible.

**Requisitos previos:** Usa solo laboratorio propio desechable con remoto local. Verifica repositorio, ruta remota, referencias, estado e identidad ficticia antes de operar.

**Opciones:** --ff-only rechaza integración divergente; remoto y rama explícitos evitan depender de valores upstream.

**Cuándo utilizar:** Cuando rama local limpia debe avanzar linealmente a su upstream revisado.

**Cuándo evitar:** Evita pull en rama incorrecta, con ediciones no preservadas o cuando divergencia requiere decisión separada.

**Sintaxis**

`git pull --ff-only origin main`

**Ejemplo básico**

`git pull --ff-only origin main`

Desde main local limpia en laboratorio, integra actualización remota lineal conocida.

**Ejemplo profesional**

`git pull --ff-only origin main`

Tras inspeccionar progreso remoto, exige sincronización lineal de main local del laboratorio.

**Impacto en el estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / historial: Condicional
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** Fetch puede actualizar referencias de seguimiento aunque integración rechace; rama actual solo avanza cuando se permite.

**Efectos y efectos secundarios:** Puede actualizar objetos, referencias de seguimiento, working tree e index; no implica actualizar rama remota.

**Errores comunes:** Suponer que fallo significa ningún cambio local o tratar pull como solo fetch.

**Alternativas:** Separa git fetch y git merge --ff-only para inspeccionar commits entrantes antes de integrar.

**Recuperación:** Si integración rechaza, inspecciona estado, referencias de seguimiento y divergencia; no fuerces ni descartes commits locales. Si hubo avance no deseado, consulta punta guardada y política de historial compartido.

**Versión y dependencias:** Sintaxis estándar Git; usa Git 2.40 o superior en laboratorios del guía. Servicios alojados pueden requerir autenticación y permisos; ejemplos usan solo rutas locales.

**Capítulos relacionados**

- [remote-repositories/03-pull-push-and-divergence](../../remote-repositories/03-pull-push-and-divergence/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-pull>

## git-push

**`git push`**

**Tipo:** Comando nativo

**Nivel:** Intermedio

**Buscar por intención:** Sincronizar repositorios, Gestionar remotos

**Riesgo:** Cambio remoto. Confirma remoto y referencia de destino exacta. Nunca practiques contra el guía o servicio compartido real; no publiques secretos.

**Finalidad:** Enviar objetos necesarios y solicitar actualización de referencias remotas especificadas.

**Requisitos previos:** Usa solo laboratorio propio desechable con remoto local. Verifica repositorio, ruta remota, referencias, estado e identidad ficticia antes de operar.

**Opciones:** Indica remoto y rama; -u configura upstream para ramas enviadas con éxito o actualizadas; --dry-run simula sin actualizar referencias remotas.

**Cuándo utilizar:** Al publicar commits revisados en rama destino autorizada.

**Cuándo evitar:** Evita publicar commits sin revisar, secretos o cambios directos en ramas protegidas.

**Sintaxis**

`git push origin feat/notes`

**Ejemplo básico**

`git push -u origin feat/notes`

Publica rama privada existente de feature en remoto local desechable y configura seguimiento.

**Ejemplo profesional**

`git push origin feat/review`

Tras revisar contenido confirmado, publica solo rama de feature nombrada en laboratorio.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Condicional
- Repositorio remoto: Condicional
- Otros estados: Condicional

**Resultado esperado:** Si se acepta, referencias remotas reflejan actualizaciones solicitadas; pushes ordinarios de ramas rechazan actualizaciones no fast-forward salvo configuración o sustitución explícita.

**Efectos y efectos secundarios:** Puede actualizar objetos y referencias remotas, referencias de seguimiento locales y configuración upstream con -u; hooks confiables pueden ejecutarse.

**Errores comunes:** Esperar que push suba archivos no preparados o suponer éxito como prueba de calidad o aprobación de revisión.

**Alternativas:** Usa git push --dry-run con destino explícito para simulación; usa pull request para integración protegida.

**Recuperación:** Si se rechaza, inspecciona cambios remotos y política. Para push erróneo aceptado, coordina corrección; borrar referencia no garantiza retirar datos expuestos.

**Versión y dependencias:** Sintaxis estándar Git; usa Git 2.40 o superior en laboratorios del guía. Servicios alojados pueden requerir autenticación y permisos; ejemplos usan solo rutas locales.

**Capítulos relacionados**

- [remote-repositories/03-pull-push-and-divergence](../../remote-repositories/03-pull-push-and-divergence/README.es.md)
- [remote-repositories/04-remote-branch-lifecycle](../../remote-repositories/04-remote-branch-lifecycle/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-push>

## git-push-delete

**`git push --delete`**

**Tipo:** Uso de opción

**Nivel:** Intermedio

**Buscar por intención:** Gestionar remotos, Gestionar ramas, Proteger historial

**Riesgo:** Cambio remoto. Confirma remoto y referencia de destino exacta. Nunca practiques contra el guía o servicio compartido real; no publiques secretos.

**Finalidad:** Solicitar eliminación de referencia remota nombrada, aquí una rama remota.

**Requisitos previos:** Usa solo laboratorio propio desechable con remoto local. Verifica repositorio, ruta remota, referencias, estado e identidad ficticia antes de operar.

**Opciones:** --delete marca referencia destino nombrada para eliminación; eliminar rama local es operación separada.

**Cuándo utilizar:** Cuando rama remota de feature obsoleta autorizada tiene trabajo conservado verificado y sin dependientes restantes.

**Cuándo evitar:** Evita eliminar referencias protegidas, activas o no verificadas, o ramas con revisiones abiertas que aún dependen de ellas.

**Sintaxis**

`git push origin --delete feat/notes`

**Ejemplo básico**

`git push origin --delete feat/notes`

Elimina solo referencia de feature obsoleta verificada del bare local de laboratorio.

**Ejemplo profesional**

`git push origin --delete feat/review`

Tras confirmar integración, punta guardada y ausencia de consumidores, limpia rama remota desechable.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Condicional
- Repositorio remoto: Condicional
- Otros estados: Condicional

**Resultado esperado:** Si se acepta, referencia remota nombrada desaparece; rama local permanece y referencias de seguimiento pueden requerir poda en otros clones.

**Efectos y efectos secundarios:** Cambia referencias remotas y posiblemente metadatos locales de seguimiento; no se garantiza borrado inmediato de objetos.

**Errores comunes:** Suponer que eliminar rama local y remota son equivalentes o eliminar antes de revisar ascendencia y dependencias.

**Alternativas:** Conserva rama remota ante duda; poda referencias locales obsoletas tras limpieza autorizada del servidor.

**Recuperación:** Registra punta remota exacta antes. Si objeto se conserva y política permite, coordina recreación en ID verificado; recuperación no garantizada.

**Versión y dependencias:** Sintaxis estándar Git; usa Git 2.40 o superior en laboratorios del guía. Servicios alojados pueden requerir autenticación y permisos; ejemplos usan solo rutas locales.

**Capítulos relacionados**

- [remote-repositories/04-remote-branch-lifecycle](../../remote-repositories/04-remote-branch-lifecycle/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-push>

## git-push-force-with-lease

**`git push --force-with-lease`**

**Tipo:** Uso de opción

**Nivel:** Avanzado

**Buscar por intención:** Reescribir historial local, Proteger historial, Sincronizar repositorios

**Riesgo:** Cambio remoto. Esto es reemplazo de historial remoto, no valor seguro por defecto. Lease coincidente no impide perder cambios ya presentes en punta esperada; nunca eludas protecciones del proyecto.

**Finalidad:** Solicitar actualización remota no fast-forward solo si referencia remota todavía coincide con valor explícitamente esperado.

**Requisitos previos:** Usa solo laboratorio propio desechable con remoto local. Verifica repositorio, ruta remota, referencias, estado e identidad ficticia antes de operar.

**Opciones:** Usa --force-with-lease=ref:expected con ID de objeto exacto revisado; forma abreviada sin expectativa explícita puede verse afectada por fetch en segundo plano.

**Cuándo utilizar:** Solo en simulación desechable autorizada de reemplazo de rama privada tras reescribir y revisar historial.

**Cuándo evitar:** Nunca uses en el guía, ramas protegidas o trabajo compartido sin acuerdo explícito; no reintentes con nueva lease solo para vencer rechazo.

**Sintaxis**

`git push --force-with-lease=refs/heads/feat/notes:EXPECTED origin feat/notes`

**Ejemplo básico**

`git push --force-with-lease=refs/heads/feat/notes:EXPECTED origin feat/notes`

Solo en laboratorio local desechable, sustituye EXPECTED por ID completo de punta remota previamente revisada tras guardarla y comprobar todos commits solo remotos.

**Ejemplo profesional**

`git push --force-with-lease=refs/heads/feat/review:EXPECTED origin feat/review`

Simula reescritura privada coordinada; sustituye por ID verificado guardado y detente si lease rechaza actualización.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Condicional
- Repositorio remoto: Condicional
- Otros estados: Condicional

**Resultado esperado:** Acepta actualización solicitada solo si valor anterior esperado coincide y política del servidor permite; expectativa obsoleta causa rechazo.

**Efectos y efectos secundarios:** Puede reemplazar punta de rama remota, transferir objetos y actualizar referencias de seguimiento locales; commits solo remotos pueden quedar inalcanzables.

**Errores comunes:** Tratar lease coincidente como prueba de seguridad de contenido o suponer protección de todas otras referencias y colaboradores.

**Alternativas:** Prefiere push ordinario o commit adicional preservando historial; si lease falla, obtén y revisa trabajo solo remoto antes de decidir.

**Recuperación:** Mantén referencia duradera a punta remota anterior antes de simular. Si reemplazo incorrecto se acepta, coordina recuperación de objetos conservados y protege trabajo nuevo; restauración no garantizada.

**Versión y dependencias:** Sintaxis estándar Git; usa Git 2.40 o superior en laboratorios del guía. Servicios alojados pueden requerir autenticación y permisos; ejemplos usan solo rutas locales.

**Capítulos relacionados**

- [remote-repositories/03-pull-push-and-divergence](../../remote-repositories/03-pull-push-and-divergence/README.es.md)
- [remote-repositories/04-remote-branch-lifecycle](../../remote-repositories/04-remote-branch-lifecycle/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-push>


---

<!-- navigation-footer -->
[Anterior](../07-merge-rebase-and-conflicts/README.es.md) · [Índice](../README.es.md) · [Siguiente](../09-recovery-and-stash/README.es.md)
<!-- /navigation-footer -->
