# 13 Seguridad y mantenimiento

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../12-internals-and-plumbing/README.es.md) · [Índice](../README.es.md) · [Siguiente](../14-platforms-and-automation/README.es.md)
<!-- /navigation -->

Generado a partir del JSON canónico. Edita los registros, no esta página.

Las entradas describen comandos y operaciones, no una secuencia para ejecutar. Practica en repositorios desechables. Las operaciones alojadas son opcionales.

**Total de entradas distintas: 8**

- [`git commit -S`](#git-commit-sign)
- [`git tag -s`](#git-tag-sign)
- [`git verify-commit`](#git-verify-commit)
- [`git verify-tag`](#git-verify-tag)
- [`git credential reject`](#git-credential-reject)
- [`git fsck`](#git-fsck)
- [`git gc`](#git-gc)
- [`git maintenance run`](#git-maintenance-run)

## git-commit-sign

**`git commit -S`**

**Tipo:** Uso de opción

**Nivel:** Intermedio

**Buscar por intención:** Registrar cambios, Verificar firmas

**Riesgo:** Cambio de estado. Protege claves de firma; nunca pongas material privado en archivos rastreados.

**Finalidad:** Crear commit firmado criptográficamente.

**Requisitos previos:** Usa repositorio completo propio desechable, referencias verificadas, trabajo guardado y configuración confiable. Nunca uses credenciales reales ni claves personales en laboratorios.

**Opciones:** -S solicita firma; ID de clave opcional se une a opción corta. -s minúscula añade trailer sign-off.

**Cuándo utilizar:** Cuando commits firmados son exigidos por política.

**Cuándo evitar:** Evita firmar cambios sin revisar o usar claves no autorizadas.

**Sintaxis**

`git commit -S -m "Signed notes"`

**Ejemplo básico**

`git commit -S -m "Signed notes"`

Confirma contenido preparado revisado con clave desechable configurada.

**Ejemplo profesional**

`git commit -S -m "docs: review notes"`

Registra commit privado firmado de documentación.

**Impacto en el estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / historial: Cambia
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** Commit exitoso incluye firma y avanza referencia; fallo de firma puede impedir creación.

**Efectos y efectos secundarios:** Crea objeto firmado y actualiza referencia; herramientas de firma y hooks pueden cambiar estado local. No hay push.

**Errores comunes:** Confundir -S con sign-off o suponer firma prueba calidad.

**Alternativas:** Usa commit ordinario solo si política permite; comprueba commits firmados con git verify-commit.

**Recuperación:** Comprueba configuración de firma y disponibilidad de clave antes de reintentar; verifica commit resultante antes de compartir.

**Versión y dependencias:** Requiere backend de firma o verificación configurado, como GnuPG u OpenSSH con soporte de firma SSH, claves y configuración de confianza apropiadas. Usa claves desechables de laboratorio.

**Capítulos relacionados**

- [security/09-commit-and-tag-signing](../../security/09-commit-and-tag-signing/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-commit>

## git-tag-sign

**`git tag -s`**

**Tipo:** Uso de opción

**Nivel:** Intermedio

**Buscar por intención:** Gestionar etiquetas, Verificar firmas

**Riesgo:** Cambio de estado. Verifica destino y firmante; nunca sobrescribas etiquetas publicadas para ocultar error.

**Finalidad:** Crear etiqueta anotada firmada y referencia local.

**Requisitos previos:** Usa repositorio completo propio desechable, referencias verificadas, trabajo guardado y configuración confiable. Nunca uses credenciales reales ni claves personales en laboratorios.

**Opciones:** -s solicita firma; -m proporciona mensaje; objeto final opcional nombra destino.

**Cuándo utilizar:** Al marcar revisión revisada bajo política de firma de lanzamiento.

**Cuándo evitar:** Evita destinos supuestos o mover etiquetas de versión publicadas.

**Sintaxis**

`git tag -s v1.0.0 -m "Practice release"`

**Ejemplo básico**

`git tag -s v1.0.0 -m "Practice release"`

Firma etiqueta de versión libre en HEAD verificado.

**Ejemplo profesional**

`git tag -s v1.1.0 -m "Reviewed release" main`

Firma etiqueta de versión libre en main local revisada.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Cambia
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** Crea objeto tag firmado y referencia local; no publica lanzamiento ni firma commit objetivo.

**Efectos y efectos secundarios:** Añade objeto tag y referencia; backend puede cambiar metadatos locales; punta de rama no cambia.

**Errores comunes:** Suponer etiqueta firmada verifica cada artefacto o commit.

**Alternativas:** Usa etiqueta anotada sin firma solo cuando política permite; verifica con git verify-tag.

**Recuperación:** Si etiqueta privada incorrecta, registra ID y revisa eliminación antes de reemplazar; sigue política de corrección para etiquetas publicadas.

**Versión y dependencias:** Requiere backend de firma o verificación configurado, como GnuPG u OpenSSH con soporte de firma SSH, claves y configuración de confianza apropiadas. Usa claves desechables de laboratorio.

**Capítulos relacionados**

- [security/09-commit-and-tag-signing](../../security/09-commit-and-tag-signing/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-tag>

## git-verify-commit

**`git verify-commit`**

**Tipo:** Comando nativo

**Nivel:** Intermedio

**Buscar por intención:** Verificar firmas

**Riesgo:** Cambio de estado. Una firma no establece seguridad del código ni aprobación de revisión. Protege claves privadas; verifica objeto exacto y confianza en firmante independientemente.

**Finalidad:** Verificar firma criptográfica de commit seleccionado usando backend configurado.

**Requisitos previos:** Usa repositorio completo propio desechable, referencias verificadas, trabajo guardado y configuración confiable. Nunca uses credenciales reales ni claves personales en laboratorios.

**Opciones:** Indica referencias o IDs de commits; --verbose muestra contenido antes de verificación.

**Cuándo utilizar:** Al comprobar commit firmado según política de identidad confiable.

**Cuándo evitar:** No aceptes firma como prueba de código seguro o aprobación de revisión.

**Sintaxis**

`git verify-commit HEAD`

**Ejemplo básico**

`git verify-commit HEAD`

Verifica commit de práctica firmado existente.

**Ejemplo profesional**

`git verify-commit main`

Verifica main firmada de laboratorio según política de confianza.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** Informa resultado; fallo devuelve no cero y configuración de confianza afecta aceptación.

**Efectos y efectos secundarios:** No cambia referencias ni archivos Git; backend externo puede actualizar metadatos propios.

**Errores comunes:** Comprobar resultado criptográfico ignorando política de firmante confiable.

**Alternativas:** Usa git log --show-signature para contexto; exige ID exacto y resultado de verificación.

**Recuperación:** Si falla, inspecciona estado, objeto seleccionado, backend y configuración de clave o confianza; no eludas firma o verificación obligatoria.

**Versión y dependencias:** Requiere backend de firma o verificación configurado, como GnuPG u OpenSSH con soporte de firma SSH, claves y configuración de confianza apropiadas. Usa claves desechables de laboratorio.

**Capítulos relacionados**

- [security/09-commit-and-tag-signing](../../security/09-commit-and-tag-signing/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-verify-commit>

## git-verify-tag

**`git verify-tag`**

**Tipo:** Comando nativo

**Nivel:** Intermedio

**Buscar por intención:** Verificar firmas, Gestionar etiquetas

**Riesgo:** Cambio de estado. Una firma no establece seguridad del código ni aprobación de revisión. Protege claves privadas; verifica objeto exacto y confianza en firmante independientemente.

**Finalidad:** Verificar firma de objeto tag firmado.

**Requisitos previos:** Usa repositorio completo propio desechable, referencias verificadas, trabajo guardado y configuración confiable. Nunca uses credenciales reales ni claves personales en laboratorios.

**Opciones:** Indica nombres de etiquetas firmadas o IDs de objetos tag; --verbose muestra contenido.

**Cuándo utilizar:** Al comprobar marcadores de lanzamiento firmados bajo política de confianza.

**Cuándo evitar:** No esperes firma en etiquetas ligeras ni confíes automáticamente en artefactos ajenos.

**Sintaxis**

`git verify-tag v1.0.0`

**Ejemplo básico**

`git verify-tag v1.0.0`

Verifica etiqueta anotada firmada existente de laboratorio.

**Ejemplo profesional**

`git verify-tag v1.1.0`

Verifica marcador de versión antes de revisar destino y artefactos.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** Informa resultado; configuración de confianza afecta aceptación.

**Efectos y efectos secundarios:** No mueve referencias ni edita archivos rastreados; backend puede modificar metadatos propios.

**Errores comunes:** Verificar nombre de etiqueta sin comprobar destino exacto o tratarlo como verificación de firma del commit objetivo.

**Alternativas:** Usa git verify-commit por separado cuando sea necesario y revisa procedencia de artefactos independientemente.

**Recuperación:** Si falla, inspecciona estado, objeto seleccionado, backend y configuración de clave o confianza; no eludas firma o verificación obligatoria.

**Versión y dependencias:** Requiere backend de firma o verificación configurado, como GnuPG u OpenSSH con soporte de firma SSH, claves y configuración de confianza apropiadas. Usa claves desechables de laboratorio.

**Capítulos relacionados**

- [security/09-commit-and-tag-signing](../../security/09-commit-and-tag-signing/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-verify-tag>

## git-credential-reject

**`git credential reject`**

**Tipo:** Subcomando

**Nivel:** Avanzado

**Buscar por intención:** Autenticar con seguridad, Diagnosticar configuración

**Riesgo:** Sensible. Puede borrar varias cuentas coincidentes; usa solo helper simulado e identificadores ficticios en laboratorio.

**Finalidad:** Solicitar que helpers configurados borren credenciales almacenadas coincidentes.

**Requisitos previos:** Aísla configuración Git, desactiva helpers heredados y usa solo helper simulado que registra eventos erase sin credenciales reales.

**Opciones:** Lee líneas clave=valor terminadas por línea vacía; coincidencia depende de helper y campos.

**Cuándo utilizar:** Al ensayar eliminación de entrada local de autenticación obsoleta.

**Cuándo evitar:** Evita coincidencia amplia, helpers desconocidos y credenciales reales en práctica.

**Sintaxis**

`git credential reject`

**Ejemplo básico**

`git credential reject`

Con solo helper simulado, introduce protocol=https, host=example.invalid, username=student en líneas separadas, luego línea vacía.

**Ejemplo profesional**

`git credential reject`

Repite con identificadores ficticios en laboratorio simulado e inspecciona evento erase.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** Helpers configurados reciben solicitud erase; eliminación depende de comportamiento. Validez de token del servidor no cambia.

**Efectos y efectos secundarios:** Puede eliminar registros locales; no revoca tokens del proveedor ni cambia historial Git.

**Errores comunes:** Confundir borrado local con revocación de token en servidor.

**Alternativas:** Usa proceso oficial de revocación y rotación del proveedor ante exposición real.

**Recuperación:** Si registro local necesario eliminado, reautentícate por flujo aprobado. Nunca restaures token expuesto.

**Versión y dependencias:** Usa Git 2.40 o superior en laboratorios; comprueba configuración y disponibilidad locales.

**Capítulos relacionados**

- [security/04-credential-managers](../../security/04-credential-managers/README.es.md)
- [security/11-credential-exposure-and-incident-response](../../security/11-credential-exposure-and-incident-response/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-credential>

## git-fsck

**`git fsck`**

**Tipo:** Comando nativo

**Nivel:** Avanzado

**Buscar por intención:** Verificar integridad, Inspeccionar objetos Git

**Riesgo:** Solo lectura. Solo lectura en formas mostradas; éxito de integridad no prueba corrección de aplicación.

**Finalidad:** Comprobar validez y conectividad de objetos.

**Requisitos previos:** Usa repositorio completo propio desechable, referencias verificadas, trabajo guardado y configuración confiable. Nunca uses credenciales reales ni claves personales en laboratorios.

**Opciones:** --full incluye objetos empaquetados y alternates; --strict aplica comprobaciones más estrictas; --lost-found escribe archivos y no se usa aquí.

**Cuándo utilizar:** Al investigar integridad o revisar copia completa antes de mantenimiento.

**Cuándo evitar:** No trates objetos dangling por sí solos como corrupción ni dependas de fsck como copia.

**Sintaxis**

`git fsck --full`

**Ejemplo básico**

`git fsck --full`

Inspecciona conectividad y validez en repositorio local completo de práctica.

**Ejemplo profesional**

`git fsck --full --strict`

Ejecuta inspección de integridad más estricta antes de mantenimiento.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Informa hallazgos de integridad detectados y puede listar objetos dangling.

**Efectos y efectos secundarios:** Formas mostradas inspeccionan repositorio local completo sin cambiar intencionalmente objetos, referencias o archivos.

**Errores comunes:** Ejecutar limpieza tras corrupción y perder datos potencialmente recuperables.

**Alternativas:** Usa git count-objects para estadísticas; repara desde copias verificadas o sanas.

**Recuperación:** Detén escrituras ante errores graves, conserva copia e investiga antes de reparar.

**Versión y dependencias:** Usa Git 2.40 o superior en laboratorios; comprueba configuración y disponibilidad locales.

**Capítulos relacionados**

- [git-internals/07-loose-objects-and-packfiles](../../git-internals/07-loose-objects-and-packfiles/README.es.md)
- [git-internals/08-gc-and-maintenance](../../git-internals/08-gc-and-maintenance/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-fsck>

## git-gc

**`git gc`**

**Tipo:** Comando nativo

**Nivel:** Avanzado

**Buscar por intención:** Mantener un repositorio, Proteger historial

**Riesgo:** Destructivo. Limpieza puede eliminar trabajo inalcanzable permanentemente. Conserva referencias de recuperación y copias antes de ejecutar.

**Finalidad:** Ejecutar mantenimiento como empaquetado y expiración configurada de datos.

**Requisitos previos:** Usa repositorio completo propio desechable, referencias verificadas, trabajo guardado y configuración confiable. Nunca uses credenciales reales ni claves personales en laboratorios.

**Opciones:** --auto comprueba necesidad; --no-prune evita poda ordinaria; no uses --prune=now en laboratorios.

**Cuándo utilizar:** Cuando repositorio local sano requiere mantenimiento bajo retención revisada.

**Cuándo evitar:** Evita escrituras concurrentes, investigaciones de recuperación o trabajo inalcanzable no preservado.

**Sintaxis**

`git gc`

**Ejemplo básico**

`git gc`

En repositorio desechable inactivo con referencias de recuperación guardadas, ejecuta mantenimiento ordinario.

**Ejemplo profesional**

`git gc --no-prune`

Omite etapa ordinaria de poda; revisa también otros ajustes de expiración.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Condicional
- Objetos / refs / historial: Condicional
- Repositorio remoto: Sin cambios
- Otros estados: Cambia

**Resultado esperado:** Puede consolidar objetos y referencias, expirar reflogs y eliminar datos inalcanzables elegibles.

**Efectos y efectos secundarios:** Cambia almacenamiento y metadatos de mantenimiento; no reescribe intencionalmente puntas ni publica cambios.

**Errores comunes:** Suponer --no-prune conserva todos datos de recuperación o gc repara objetos corruptos.

**Alternativas:** Usa tarea limitada de git maintenance run cuando proceda.

**Recuperación:** Comprueba referencias e integridad tras mantenimiento; recupera objetos necesarios ausentes de copias verificadas si posible.

**Versión y dependencias:** Usa Git 2.40 o superior en laboratorios; comprueba configuración y disponibilidad locales.

**Capítulos relacionados**

- [git-internals/08-gc-and-maintenance](../../git-internals/08-gc-and-maintenance/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-gc>

## git-maintenance-run

**`git maintenance run`**

**Tipo:** Subcomando

**Nivel:** Avanzado

**Buscar por intención:** Mantener un repositorio

**Riesgo:** Cambio de estado. Selecciona tareas deliberadamente; no supongas mantenimiento arbitrario sin efectos destructivos o de red.

**Finalidad:** Ejecutar tareas de mantenimiento explícitamente seleccionadas.

**Requisitos previos:** Usa repositorio completo propio desechable, referencias verificadas, trabajo guardado y configuración confiable. Nunca uses credenciales reales ni claves personales en laboratorios.

**Opciones:** --task=commit-graph selecciona mantenimiento de grafo; --auto puede ejecutar tareas configuradas necesarias. Otras tareas tienen efectos distintos.

**Cuándo utilizar:** Al actualizar metadatos locales de aceleración con tarea dirigida.

**Cuándo evitar:** Evita tareas amplias sin revisar o programación global en entorno compartido.

**Sintaxis**

`git maintenance run --task=commit-graph`

**Ejemplo básico**

`git maintenance run --task=commit-graph`

Ejecuta solo mantenimiento commit-graph en repositorio de práctica inactivo.

**Ejemplo profesional**

`git maintenance run --task=commit-graph`

Actualiza metadatos de grafo e inspecciona después.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Cambia

**Resultado esperado:** Tarea seleccionada actualiza metadatos commit-graph según necesidad sin cambiar puntas.

**Efectos y efectos secundarios:** Tarea mostrada escribe metadatos de grafo; otras pueden cambiar almacenamiento o contactar remotos.

**Errores comunes:** Suponer run establece programación persistente o toda tarea es solo lectura.

**Alternativas:** Usa git commit-graph verify para inspeccionar validez de grafo.

**Recuperación:** Inspecciona fallo e integridad; repite solo tarea limitada tras tratar causa.

**Versión y dependencias:** Usa Git 2.40 o superior en laboratorios; comprueba configuración y disponibilidad locales.

**Capítulos relacionados**

- [git-internals/08-gc-and-maintenance](../../git-internals/08-gc-and-maintenance/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-maintenance>


---

<!-- navigation-footer -->
[Anterior](../12-internals-and-plumbing/README.es.md) · [Índice](../README.es.md) · [Siguiente](../14-platforms-and-automation/README.es.md)
<!-- /navigation-footer -->
