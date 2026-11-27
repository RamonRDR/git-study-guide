# 09 Recuperación y stash

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../08-remotes-and-synchronization/README.es.md) · [Índice](../README.es.md) · [Siguiente](../10-search-and-troubleshooting/README.es.md)
<!-- /navigation -->

Generado a partir del JSON canónico. Edita los registros, no esta página.

Las entradas describen comandos y operaciones, no una secuencia para ejecutar. Practica en repositorios desechables. Las operaciones alojadas son opcionales.

**Total de entradas distintas: 7**

- [`git reset`](#git-reset)
- [`git revert`](#git-revert)
- [`git reflog`](#git-reflog)
- [`git cherry-pick`](#git-cherry-pick)
- [`git stash push`](#git-stash-push)
- [`git stash apply`](#git-stash-apply)
- [`git stash pop`](#git-stash-pop)

## git-reset

**`git reset`**

**Tipo:** Comando nativo

**Nivel:** Avanzado

**Buscar por intención:** Deshacer cambios, Reescribir historial local, Retirar cambios del staging

**Riesgo:** Destructivo. Elección de modo importa: hard puede destruir trabajo local y todos modos por commit pueden reescribir historial. Mantén ejemplos privados y desechables.

**Finalidad:** Mover rama actual o HEAD separado a commit seleccionado en forma por commit; elegir cómo se afectan index y working tree.

**Requisitos previos:** Usa repositorio propio desechable; inspecciona estado, referencias seleccionadas e identidad ficticia. Guarda punta original y trabajo valioso sin confirmar por separado.

**Opciones:** --soft deja index y working tree intactos; --mixed restablece index y deja archivos; --hard restablece ambos y puede sobrescribir o eliminar rutas no rastreadas obstructivas. Reset por ruta es distinto y no mueve HEAD.

**Cuándo utilizar:** Al reorganizar intencionalmente commits privados con punta guardada y elección explícita de modo.

**Cuándo evitar:** Evita restablecer historial compartido o usar --hard con trabajo no preservado. Nunca practiques en repositorio del guía.

**Sintaxis**

`git reset --soft HEAD~1`

**Ejemplo básico**

`git reset --soft HEAD~1`

Tras guardar punta privada, deshaz último commit conservando index y archivos; la punta debe tener padre.

**Ejemplo profesional**

`git reset --mixed HEAD~1`

En rama privada desechable con punta guardada y sin trabajo valioso sin confirmar, retrocede un commit y revisa diferencias ahora no preparadas.

**Impacto en el estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / historial: Condicional
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** HEAD identifica commit seleccionado; soft conserva contenido preparado, mixed ajusta index al destino, hard ajusta contenido rastreado e index al destino.

**Efectos y efectos secundarios:** Puede mover referencias y actualizar ORIG\_HEAD y reflogs; modo determina cambios de index y archivos. No hay actualización remota.

**Errores comunes:** Confundir reset de ruta con mover rama o esperar que reflog recupere ediciones sin confirmar descartadas.

**Alternativas:** Usa git restore --staged para retirar ruta de staging; usa git revert para deshacer commit compartido sin quitarlo del historial.

**Recuperación:** Inspecciona referencias guardadas y reflog; crea rama de recuperación en punta anterior verificada si aún existe. Trabajo no preparado o no rastreado descartado puede ser irrecuperable.

**Versión y dependencias:** Sintaxis estándar Git; usa Git 2.40 o superior en laboratorios del guía. Configuración local confiable y hooks pueden afectar ejecución.

**Capítulos relacionados**

- [history-and-recovery/01-recovery-safety](../../history-and-recovery/01-recovery-safety/README.es.md)
- [history-and-recovery/03-reset](../../history-and-recovery/03-reset/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-reset>

## git-revert

**`git revert`**

**Tipo:** Comando nativo

**Nivel:** Intermedio

**Buscar por intención:** Deshacer cambios, Proteger historial

**Riesgo:** Cambio de estado. Cambios inversos pueden entrar en conflicto con trabajo posterior; revisa resultado y pruebas. Revertir secreto no lo borra del historial.

**Finalidad:** Crear nuevo commit que invierte cambios introducidos por commit seleccionado.

**Requisitos previos:** Usa repositorio propio desechable; inspecciona estado, referencias seleccionadas e identidad ficticia. Guarda punta original y trabajo valioso sin confirmar por separado.

**Opciones:** --no-edit usa mensaje generado; --no-commit prepara cambios sin confirmar; revertir merge requiere padre principal elegido cuidadosamente con -m.

**Cuándo utilizar:** Al corregir cambio confirmado conservando ascendencia compartida.

**Cuándo evitar:** Evita revertir commit o merge no revisado sin comprender dependencias y efectos en integraciones futuras.

**Sintaxis**

`git revert HEAD`

**Ejemplo básico**

`git revert HEAD`

En rama de práctica limpia, revierte último commit ordinario tras verificarlo.

**Ejemplo profesional**

`git revert --no-edit HEAD`

Registra cambio inverso en rama local aprobada de corrección; inspecciona mensaje generado y resultado.

**Impacto en el estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / historial: Condicional
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** En ejecución ordinaria exitosa, nuevo commit de cambio inverso avanza HEAD; commit original permanece en historial. Conflictos pueden pausar operación.

**Efectos y efectos secundarios:** Puede cambiar archivos, index, objetos, referencias y metadatos de secuencia; no hay push automático.

**Errores comunes:** Esperar que desaparezca commit original o repositorio entero sea idéntico a instantánea anterior.

**Alternativas:** Usa commit correctivo ordinario para correcciones selectivas; reset solo para historial privado cuidadosamente revisado.

**Recuperación:** Si operación pausa, inspecciona estado y usa --continue correspondiente tras resolución revisada, o --abort tras conservar ediciones deseadas. Para operación finalizada, evalúa nuevo commit correctivo en vez de reescribir historial compartido.

**Versión y dependencias:** Sintaxis estándar Git; usa Git 2.40 o superior en laboratorios del guía. Configuración local confiable y hooks pueden afectar ejecución.

**Capítulos relacionados**

- [history-and-recovery/01-recovery-safety](../../history-and-recovery/01-recovery-safety/README.es.md)
- [history-and-recovery/04-revert](../../history-and-recovery/04-revert/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-revert>

## git-reflog

**`git reflog`**

**Tipo:** Comando nativo

**Nivel:** Intermedio

**Buscar por intención:** Recuperar trabajo, Inspeccionar referencias, Inspeccionar historial

**Riesgo:** Solo lectura. Solo inspección de lectura; salida de reflog puede contener mensajes e identidades privadas. Recuperación no garantizada.

**Finalidad:** Inspeccionar movimientos registrados localmente de referencias para localizar IDs anteriores de commits.

**Requisitos previos:** Usa repositorio propio desechable; inspecciona estado, referencias seleccionadas e identidad ficticia. Guarda punta original y trabajo valioso sin confirmar por separado.

**Opciones:** Invocación predeterminada muestra reflog de HEAD; show con referencia nombrada selecciona ese log. Expire y delete son operaciones modificadoras separadas no usadas aquí.

**Cuándo utilizar:** Al investigar punta anterior de rama tras movimiento local accidental de referencia.

**Cuándo evitar:** No supongas que toda referencia tiene reflog o entradas persisten para siempre; no es copia de seguridad de ediciones no preparadas.

**Sintaxis**

`git reflog show HEAD`

**Ejemplo básico**

`git reflog`

Inspecciona movimientos locales recientes de HEAD tras reset de práctica.

**Ejemplo profesional**

`git reflog show main`

Investiga puntas anteriores de main del laboratorio antes de elegir rama de recuperación.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Muestra movimientos registrados e IDs de commits asociados donde existen logs; entradas pueden expirar.

**Efectos y efectos secundarios:** Inspección mostrada no cambia archivos, index, referencias, objetos ni remoto; logs pertenecen al repositorio local.

**Errores comunes:** Suponer que HEAD@{1} siempre identifica commit deseado u otro clon tiene entradas idénticas.

**Alternativas:** Inspecciona nombres de ramas, etiquetas o copias guardadas primero cuando estén disponibles.

**Recuperación:** Verifica candidato con git show y crea rama de recuperación en ID exacto si disponible. No restablezcas directamente a posición supuesta de reflog.

**Versión y dependencias:** Sintaxis estándar Git; usa Git 2.40 o superior en laboratorios del guía. Configuración local confiable y hooks pueden afectar ejecución.

**Capítulos relacionados**

- [history-and-recovery/01-recovery-safety](../../history-and-recovery/01-recovery-safety/README.es.md)
- [history-and-recovery/05-reflog](../../history-and-recovery/05-reflog/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-reflog>

## git-cherry-pick

**`git cherry-pick`**

**Tipo:** Comando nativo

**Nivel:** Intermedio

**Buscar por intención:** Integrar cambios, Recuperar trabajo

**Riesgo:** Cambio de estado. Revisa diff de origen, contexto de destino y dependencias; reaplicación puede causar conflictos o introducir comportamiento duplicado.

**Finalidad:** Aplicar cambios introducidos por commit seleccionado a rama actual, normalmente creando nuevo commit.

**Requisitos previos:** Usa repositorio propio desechable; inspecciona estado, referencias seleccionadas e identidad ficticia. Guarda punta original y trabajo valioso sin confirmar por separado.

**Opciones:** -x registra ID de origen en mensajes adecuados de commits exitosos; --no-commit prepara cambios sin confirmar. Merges requieren elegir padre principal.

**Cuándo utilizar:** Al transferir corrección independiente revisada sin integrar toda rama de origen.

**Cuándo evitar:** Evita seleccionar commits sin comprobar dependencias o duplicar cambios ya integrados.

**Sintaxis**

`git cherry-pick FIX_ID`

**Ejemplo básico**

`git cherry-pick FIX_ID`

Sustituye FIX\_ID por ID revisado de commit ordinario de otra rama local de práctica.

**Ejemplo profesional**

`git cherry-pick -x FIX_ID`

En simulación local de backport, sustituye ID de corrección independiente verificada y prueba resultado.

**Impacto en el estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / historial: Condicional
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** Éxito ordinario crea commit nuevo basado en HEAD actual, típicamente con ID distinto; conflictos o cambios vacíos pueden pausar o requerir decisión.

**Efectos y efectos secundarios:** Puede actualizar working tree, index, objetos, referencias y estado de secuencia; rama de origen no se mueve.

**Errores comunes:** Suponer que cherry-pick conserva ascendencia de origen o incluye commits previos necesarios automáticamente.

**Alternativas:** Usa merge si debe integrarse toda ascendencia de origen; usa corrección revisada manualmente si cambio requiere adaptación.

**Recuperación:** Si operación pausa, inspecciona estado y usa --continue correspondiente tras resolución revisada, o --abort tras conservar ediciones deseadas. Para operación finalizada, evalúa nuevo commit correctivo en vez de reescribir historial compartido.

**Versión y dependencias:** Sintaxis estándar Git; usa Git 2.40 o superior en laboratorios del guía. Configuración local confiable y hooks pueden afectar ejecución.

**Capítulos relacionados**

- [history-and-recovery/01-recovery-safety](../../history-and-recovery/01-recovery-safety/README.es.md)
- [history-and-recovery/07-cherry-pick](../../history-and-recovery/07-cherry-pick/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-cherry-pick>

## git-stash-push

**`git stash push`**

**Tipo:** Subcomando

**Nivel:** Intermedio

**Buscar por intención:** Guardar trabajo temporalmente, Cambiar contexto de trabajo

**Riesgo:** Cambio de estado. Stash es almacenamiento temporal local, no copia de seguridad. Aplicar puede generar conflictos; revisa estado y conserva trabajo valioso antes de cambiar estado.

**Finalidad:** Guardar modificaciones locales seleccionadas en entrada de stash y revertir cambios correspondientes de trabajo e index hacia HEAD.

**Requisitos previos:** Usa repositorio propio desechable con commit existente; revisa estado, lista de stash y entrada prevista. Conserva trabajo valioso por separado.

**Opciones:** -m nombra entrada; -u incluye archivos no rastreados pero no ignorados; -a incluye también ignorados y no se usa aquí. --keep-index conserva cambios preparados en estado de trabajo.

**Cuándo utilizar:** Al guardar temporalmente trabajo inacabado en contexto local controlado.

**Cuándo evitar:** Evita depender de stash como única copia de trabajo importante o guardar archivos sensibles.

**Sintaxis**

`git stash push -m "draft notes"`

**Ejemplo básico**

`git stash push -m "draft notes"`

Guarda ediciones rastreadas de práctica temporalmente.

**Ejemplo profesional**

`git stash push -u -m "review draft"`

Tras comprobar archivos sensibles, incluye también borrador ficticio no rastreado previsto.

**Impacto en el estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / historial: Condicional
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** Si existen cambios correspondientes, se registra entrada de stash; cambios seleccionados se retiran del estado de trabajo según opciones. Archivos no rastreados permanecen salvo inclusión.

**Efectos y efectos secundarios:** Puede crear objetos de commit locales y actualizar refs/stash y reflog, index y archivos; punta actual y remoto permanecen sin cambios.

**Errores comunes:** Suponer que stash predeterminado incluye archivos no rastreados e ignorados o estado limpio prueba que todo archivo deseado se guardó.

**Alternativas:** Usa rama temporal privada con commit revisado para trabajo que requiere referencia nombrada más duradera.

**Recuperación:** Inspecciona git stash list y git stash show; usa apply en entrada verificada antes de quitarla. Objetos ausentes o expirados pueden no ser recuperables.

**Versión y dependencias:** Sintaxis estándar Git; usa Git 2.40 o superior en laboratorios del guía. Configuración local confiable y hooks pueden afectar ejecución.

**Capítulos relacionados**

- [history-and-recovery/01-recovery-safety](../../history-and-recovery/01-recovery-safety/README.es.md)
- [history-and-recovery/06-stash](../../history-and-recovery/06-stash/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-stash>

## git-stash-apply

**`git stash apply`**

**Tipo:** Subcomando

**Nivel:** Intermedio

**Buscar por intención:** Guardar trabajo temporalmente, Recuperar trabajo

**Riesgo:** Cambio de estado. Stash es almacenamiento temporal local, no copia de seguridad. Aplicar puede generar conflictos; revisa estado y conserva trabajo valioso antes de cambiar estado.

**Finalidad:** Reaplicar entrada de stash seleccionada sin quitarla de la lista de stash.

**Requisitos previos:** Usa repositorio propio desechable con commit existente; revisa estado, lista de stash y entrada prevista. Conserva trabajo valioso por separado.

**Opciones:** --index también intenta restaurar estado preparado; indica entrada verificada explícitamente. Sin --index, división original de staging no garantizada.

**Cuándo utilizar:** Al restaurar trabajo guardado conservando copia de entrada de stash para verificación.

**Cuándo evitar:** Evita aplicar sobre cambios valiosos sin confirmar o seleccionar entrada por posición sin verificar.

**Sintaxis**

`git stash apply "stash@{0}"`

**Ejemplo básico**

`git stash apply "stash@{0}"`

Inspecciona list y show primero, luego aplica última entrada de práctica verificada en checkout limpio.

**Ejemplo profesional**

`git stash apply --index "stash@{0}"`

En rama de laboratorio limpia compatible, intenta restaurar trabajo preparado y no preparado e inspecciona diferencias.

**Impacto en el estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / historial: Condicional
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** Aplica cambios guardados al estado de trabajo cuando es posible; puede causar conflictos. Entrada de stash sigue disponible tras apply ordinario.

**Efectos y efectos secundarios:** Puede actualizar working tree, index y metadatos de conflicto; referencia de stash no se elimina y punta de rama actual no avanza.

**Errores comunes:** Suponer que apply elimina entrada o que --index siempre restaura index exacto pese a conflictos.

**Alternativas:** Usa pop solo cuando aplicación exitosa también debe quitar entrada; prefiere apply al verificar trabajo recuperado.

**Recuperación:** Si aplicación entra en conflicto, inspecciona rutas no fusionadas y stash conservado; preserva resolución antes de limpiar. No existe stash abort general; evita reset a ciegas o aplicación repetida.

**Versión y dependencias:** Sintaxis estándar Git; usa Git 2.40 o superior en laboratorios del guía. Configuración local confiable y hooks pueden afectar ejecución.

**Capítulos relacionados**

- [history-and-recovery/01-recovery-safety](../../history-and-recovery/01-recovery-safety/README.es.md)
- [history-and-recovery/06-stash](../../history-and-recovery/06-stash/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-stash>

## git-stash-pop

**`git stash pop`**

**Tipo:** Subcomando

**Nivel:** Intermedio

**Buscar por intención:** Guardar trabajo temporalmente, Recuperar trabajo

**Riesgo:** Destructivo. Pop puede quitar acceso nombrado al trabajo guardado si tiene éxito. Conserva copia independiente o prefiere apply ante dudas.

**Finalidad:** Reaplicar entrada de stash y quitarla de la lista solo cuando aplicación tenga éxito.

**Requisitos previos:** Usa repositorio propio desechable con commit existente; revisa estado, lista de stash y entrada prevista. Conserva trabajo valioso por separado.

**Opciones:** --index intenta restaurar estado preparado también; indica entrada verificada. git stash drop elimina entrada sin aplicar y requiere revisión separada.

**Cuándo utilizar:** Al retomar cambio temporal verificado cuya copia de stash ya no se necesita tras éxito.

**Cuándo evitar:** Evita cuando stash es única copia de trabajo importante o destino ya tiene cambios no preservados.

**Sintaxis**

`git stash pop "stash@{0}"`

**Ejemplo básico**

`git stash pop "stash@{0}"`

Tras verificar stash desechable y destino limpio, reanuda trabajo e inspecciona estado y lista de stash.

**Ejemplo profesional**

`git stash pop --index "stash@{0}"`

Restaura entrada temporal revisada de laboratorio incluyendo estado de staging y confirma resultado antes de continuar.

**Impacto en el estado**

- Working tree: Condicional
- Index: Condicional
- Objetos / refs / historial: Condicional
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** Aplicación exitosa quita entrada seleccionada; conflicto la conserva para revisión, con posibles cambios parciales en checkout.

**Efectos y efectos secundarios:** Puede cambiar working tree, index, refs/stash y reflog; punta de rama y remoto no cambian en operación normal.

**Errores comunes:** Suponer stash eliminado tras conflicto o pop exitoso deja entrada reutilizable en misma posición.

**Alternativas:** Prefiere apply, inspecciona cambios restaurados y conserva entrada hasta estar satisfecho; solo entonces considera drop verificado.

**Recuperación:** Si ocurre conflicto, verifica entrada conservada e inspecciona rutas no fusionadas. Tras éxito, conserva trabajo restaurado pronto; recuperación de entrada eliminada desde objetos restantes no garantizada.

**Versión y dependencias:** Sintaxis estándar Git; usa Git 2.40 o superior en laboratorios del guía. Configuración local confiable y hooks pueden afectar ejecución.

**Capítulos relacionados**

- [history-and-recovery/01-recovery-safety](../../history-and-recovery/01-recovery-safety/README.es.md)
- [history-and-recovery/06-stash](../../history-and-recovery/06-stash/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-stash>


---

<!-- navigation-footer -->
[Anterior](../08-remotes-and-synchronization/README.es.md) · [Índice](../README.es.md) · [Siguiente](../10-search-and-troubleshooting/README.es.md)
<!-- /navigation-footer -->
