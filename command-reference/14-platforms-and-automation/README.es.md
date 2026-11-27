# 14 Plataformas y automatización

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../13-security-and-maintenance/README.es.md) · [Índice](../README.es.md) · [Siguiente módulo](../../practical-projects/README.es.md)
<!-- /navigation -->

Generado a partir del JSON canónico. Edita los registros, no esta página.

Las entradas describen comandos y operaciones, no una secuencia para ejecutar. Practica en repositorios desechables. Las operaciones alojadas son opcionales.

**Total de entradas distintas: 8**

- [`gh pr create`](#gh-pr-create)
- [`gh pr view`](#gh-pr-view)
- [`gh pr checks`](#gh-pr-checks)
- [`gh run view`](#gh-run-view)
- [`gh release create`](#gh-release-create)
- [`glab mr create`](#glab-mr-create)
- [`glab mr view`](#glab-mr-view)
- [`glab ci status`](#glab-ci-status)

## gh-pr-create

**`gh pr create`**

**Tipo:** Herramienta externa

**Nivel:** Intermedio

**Buscar por intención:** Revisar cambios, Automatizar flujo

**Riesgo:** Cambio remoto. Crea estado en plataforma y puede notificar personas o activar automatización. No ejecutes ejemplos ficticios contra repositorios reales; exige autorización y verifica destino.

**Finalidad:** Crear pull request GitHub para integración propuesta de rama.

**Requisitos previos:** Ejemplos son modelos ficticios, no ejercicios en servicio real. Sustituye solo por repositorio sandbox explícitamente autorizado, cuenta, referencias e IDs verificados. Comprueba versión y autenticación CLI primero.

**Opciones:** --base y --head identifican referencias; --draft abre borrador; --head explícito evita fork o push implícito. --dry-run aún puede hacer push.

**Cuándo utilizar:** Cuando rama de feature autorizada publicada está lista para revisión o comentarios preliminares.

**Cuándo evitar:** Evita repositorio incorrecto, contenido sensible sin revisar o eludir controles de revisión.

**Sintaxis**

`gh pr create -R example-org/example-repo --base main --head feat/notes --title "Review notes" --body "Fictional review" --draft`

**Ejemplo básico**

`gh pr create -R example-org/example-repo --base main --head feat/notes --title "Review notes" --body "Fictional review" --draft`

Ilustra apertura de borrador desde rama autorizada ya publicada; sustituye solo repositorio sandbox.

**Ejemplo profesional**

`gh pr create -R example-org/example-repo --base main --head feat/docs --title "Review documentation" --body "Describe changes and test evidence"`

Ilustra solicitud de revisión de cambios confirmados revisados con head y base explícitos.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Condicional
- Otros estados: Condicional

**Resultado esperado:** Devuelve URL del PR creado con éxito; creación sola no integra rama.

**Efectos y efectos secundarios:** Crea metadatos remotos de PR y puede activar CI o notificaciones. Head explícito mostrado exige rama ya publicada; formas implícitas pueden hacer push o fork.

**Errores comunes:** Confundir creación de PR con aprobación de merge o esperar dry run garantice ausencia de escrituras en red.

**Alternativas:** Usa interfaz web de plataforma para inspeccionar y crear solicitud autorizada manualmente.

**Recuperación:** Inspecciona URL creada y referencias exactas; si incorrecto, coordina corrección o cierre autorizado del PR equivocado. Cerrar no borra historial.

**Versión y dependencias:** Requiere GitHub CLI (gh) compatible actual, autenticación autorizada, red y permisos relevantes. Comprueba gh help para opciones instaladas.

**Capítulos relacionados**

- [github/04-pull-requests-and-review](../../github/04-pull-requests-and-review/README.es.md)
- [github/08-github-cli](../../github/08-github-cli/README.es.md)

**Documentación oficial**

- <https://cli.github.com/manual/gh_pr_create>

## gh-pr-view

**`gh pr view`**

**Tipo:** Herramienta externa

**Nivel:** Intermedio

**Buscar por intención:** Revisar cambios, Inspeccionar estado del repositorio

**Riesgo:** Solo lectura. Inspección no autoriza merge. Protege metadatos privados y logs; no expongas credenciales.

**Finalidad:** Inspeccionar pull request GitHub y metadatos de revisión o merge.

**Requisitos previos:** Ejemplos son modelos ficticios, no ejercicios en servicio real. Sustituye solo por repositorio sandbox explícitamente autorizado, cuenta, referencias e IDs verificados. Comprueba versión y autenticación CLI primero.

**Opciones:** --json selecciona campos; --comments muestra comentarios y revisiones; --web abre página.

**Cuándo utilizar:** Al comprobar PR exacto y head en revisión.

**Cuándo evitar:** No deduzcas autorización de merge solo de campo de posibilidad de merge.

**Sintaxis**

`gh pr view 42 -R example-org/example-repo`

**Ejemplo básico**

`gh pr view 42 -R example-org/example-repo`

Inspecciona PR ficticio número 42 en modelo de sandbox autorizado.

**Ejemplo profesional**

`gh pr view 42 -R example-org/example-repo --json headRefOid,reviewDecision,mergeStateStatus`

Inspecciona head exacto y estado de revisión, luego comprueba checks obligatorios independientemente.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Muestra instantánea de metadatos del PR; cálculo y estado de revisión pueden cambiar.

**Efectos y efectos secundarios:** Lee metadatos de plataforma por red; no altera intencionalmente referencias Git, index, checkout ni recursos de plataforma en forma mostrada.

**Errores comunes:** Leer aprobación de head anterior como aprobación de cambios nuevos.

**Alternativas:** Usa interfaz web y gh pr checks para inspeccionar checks y discusión.

**Recuperación:** Inspección no requiere deshacer. Verifica repositorio, ID, permisos y asociación con commit exacto; actualiza estado si incompleto u obsoleto.

**Versión y dependencias:** Requiere GitHub CLI (gh) compatible actual, autenticación autorizada, red y permisos relevantes. Comprueba gh help para opciones instaladas.

**Capítulos relacionados**

- [github/04-pull-requests-and-review](../../github/04-pull-requests-and-review/README.es.md)
- [github/08-github-cli](../../github/08-github-cli/README.es.md)

**Documentación oficial**

- <https://cli.github.com/manual/gh_pr_view>

## gh-pr-checks

**`gh pr checks`**

**Tipo:** Herramienta externa

**Nivel:** Intermedio

**Buscar por intención:** Inspeccionar CI, Revisar cambios

**Riesgo:** Solo lectura. Inspección no autoriza merge. Protege metadatos privados y logs; no expongas credenciales.

**Finalidad:** Inspeccionar resultados de checks CI asociados al pull request GitHub.

**Requisitos previos:** Ejemplos son modelos ficticios, no ejercicios en servicio real. Sustituye solo por repositorio sandbox explícitamente autorizado, cuenta, referencias e IDs verificados. Comprueba versión y autenticación CLI primero.

**Opciones:** --required limita a checks obligatorios; --watch espera actualizaciones; checks pendientes tienen código de salida distinto en CLI actual.

**Cuándo utilizar:** Al determinar si checks obligatorios terminaron para cambio revisado.

**Cuándo evitar:** Evita declarar éxito con resultados incompletos, ausentes u obsoletos.

**Sintaxis**

`gh pr checks 42 -R example-org/example-repo`

**Ejemplo básico**

`gh pr checks 42 -R example-org/example-repo`

Inspecciona checks de PR ficticio de sandbox autorizado.

**Ejemplo profesional**

`gh pr checks 42 -R example-org/example-repo --required`

Inspecciona checks obligatorios y confirma correspondencia al head revisado más reciente.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Muestra estados reportados de checks; código no cero puede indicar pendiente o fallo según código.

**Efectos y efectos secundarios:** Lee metadatos de plataforma por red; no altera intencionalmente referencias Git, index, checkout ni recursos de plataforma en forma mostrada.

**Errores comunes:** Tratar ausencia de checks reportados o checks antiguos aprobados como señal verde actual.

**Alternativas:** Inspecciona head del PR y ejecuciones individuales de workflow, incluidos checks obligatorios y logs.

**Recuperación:** Inspección no requiere deshacer. Verifica repositorio, ID, permisos y asociación con commit exacto; actualiza estado si incompleto u obsoleto.

**Versión y dependencias:** Requiere GitHub CLI (gh) compatible actual, autenticación autorizada, red y permisos relevantes. Comprueba gh help para opciones instaladas.

**Capítulos relacionados**

- [github/04-pull-requests-and-review](../../github/04-pull-requests-and-review/README.es.md)
- [ci-cd/09-quality-gates-and-troubleshooting](../../ci-cd/09-quality-gates-and-troubleshooting/README.es.md)

**Documentación oficial**

- <https://cli.github.com/manual/gh_pr_checks>

## gh-run-view

**`gh run view`**

**Tipo:** Herramienta externa

**Nivel:** Intermedio

**Buscar por intención:** Inspeccionar CI

**Riesgo:** Solo lectura. Inspección no autoriza merge. Protege metadatos privados y logs; no expongas credenciales.

**Finalidad:** Inspeccionar ejecución específica de workflow GitHub Actions e información disponible de jobs.

**Requisitos previos:** Ejemplos son modelos ficticios, no ejercicios en servicio real. Sustituye solo por repositorio sandbox explícitamente autorizado, cuenta, referencias e IDs verificados. Comprueba versión y autenticación CLI primero.

**Opciones:** --log-failed solicita logs de pasos fallidos; --exit-status devuelve no cero para ejecución fallida; ID de ejecución no es número de PR.

**Cuándo utilizar:** Al diagnosticar intento identificado de workflow para commit específico.

**Cuándo evitar:** No supongas ejecución ajena exitosa prueba aprobación de checks obligatorios.

**Sintaxis**

`gh run view 123456 -R example-org/example-repo`

**Ejemplo básico**

`gh run view 123456 -R example-org/example-repo`

Inspecciona ID ficticio de ejecución de workflow en modelo sandbox.

**Ejemplo profesional**

`gh run view 123456 -R example-org/example-repo --log-failed`

Inspecciona logs de pasos fallidos sin publicar salida sensible.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Devuelve detalles o logs disponibles; ejecuciones incompletas y logs expirados pueden no dar evidencia final.

**Efectos y efectos secundarios:** Lee metadatos de plataforma por red; no altera intencionalmente referencias Git, index, checkout ni recursos de plataforma en forma mostrada.

**Errores comunes:** Confundir ID de ejecución, ID de job y número de PR o ignorar intento y SHA del head.

**Alternativas:** Usa gh pr checks para checks del PR e interfaz Actions para contexto completo del intento.

**Recuperación:** Inspección no requiere deshacer. Verifica repositorio, ID, permisos y asociación con commit exacto; actualiza estado si incompleto u obsoleto.

**Versión y dependencias:** Requiere GitHub CLI (gh) compatible actual, autenticación autorizada, red y permisos relevantes. Comprueba gh help para opciones instaladas.

**Capítulos relacionados**

- [ci-cd/03-github-actions](../../ci-cd/03-github-actions/README.es.md)
- [ci-cd/09-quality-gates-and-troubleshooting](../../ci-cd/09-quality-gates-and-troubleshooting/README.es.md)

**Documentación oficial**

- <https://cli.github.com/manual/gh_run_view>

## gh-release-create

**`gh release create`**

**Tipo:** Herramienta externa

**Nivel:** Avanzado

**Buscar por intención:** Gestionar versiones, Gestionar etiquetas

**Riesgo:** Cambio remoto. Crea estado en plataforma y puede notificar personas o activar automatización. No ejecutes ejemplos ficticios contra repositorios reales; exige autorización y verifica destino.

**Finalidad:** Crear metadatos de lanzamiento asociados a etiqueta GitHub, opcionalmente como borrador.

**Requisitos previos:** Ejemplos son modelos ficticios, no ejercicios en servicio real. Sustituye solo por repositorio sandbox explícitamente autorizado, cuenta, referencias e IDs verificados. Comprueba versión y autenticación CLI primero.

**Opciones:** --verify-tag exige etiqueta remota existente; sin él la CLI puede crear etiqueta ausente. --draft aplaza publicación; --notes-file proporciona notas.

**Cuándo utilizar:** Al preparar lanzamiento autorizado revisado tras verificar etiqueta de versión.

**Cuándo evitar:** Evita destinos no verificados, aprobación ausente, activos sensibles o creación implícita de etiqueta.

**Sintaxis**

`gh release create v1.0.0 -R example-org/example-repo --verify-tag --draft --title "Practice release" --notes "Fictional release notes"`

**Ejemplo básico**

`gh release create v1.0.0 -R example-org/example-repo --verify-tag --draft --title "Practice release" --notes "Fictional release notes"`

Ilustra borrador usando etiqueta remota autorizada existente en sandbox.

**Ejemplo profesional**

`gh release create v1.1.0 -R example-org/example-repo --verify-tag --draft --notes-file release-notes.md`

Prepara borrador solo tras revisar etiqueta existente, archivo de notas y política de lanzamiento.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Condicional
- Otros estados: Condicional

**Resultado esperado:** Crea borrador de lanzamiento para etiqueta remota existente en formas mostradas; publicación requiere acción separada.

**Efectos y efectos secundarios:** Escribe metadatos remotos de borrador; forma --verify-tag mostrada exige etiqueta existente y no la crea. Otras formas pueden crear etiquetas o publicar activos.

**Errores comunes:** Confundir verificación de existencia de etiqueta con verificación de firma o publicar antes de aprobaciones.

**Alternativas:** Usa interfaz Releases para preparar borrador y revisar manualmente; verifica firmas y artefactos por separado.

**Recuperación:** Inspecciona borrador creado y etiqueta asociada. Coordina ediciones autorizadas o eliminación del borrador si incorrecto; no reescribas etiqueta publicada.

**Versión y dependencias:** Requiere GitHub CLI (gh) compatible actual, autenticación autorizada, red y permisos relevantes. Comprueba gh help para opciones instaladas.

**Capítulos relacionados**

- [github/07-tags-and-releases](../../github/07-tags-and-releases/README.es.md)
- [professional-workflows/12-release-management](../../professional-workflows/12-release-management/README.es.md)

**Documentación oficial**

- <https://cli.github.com/manual/gh_release_create>

## glab-mr-create

**`glab mr create`**

**Tipo:** Herramienta externa

**Nivel:** Intermedio

**Buscar por intención:** Revisar cambios, Automatizar flujo

**Riesgo:** Cambio remoto. Crea estado en plataforma y puede notificar personas o activar automatización. No ejecutes ejemplos ficticios contra repositorios reales; exige autorización y verifica destino.

**Finalidad:** Abrir merge request GitLab para integración propuesta.

**Requisitos previos:** Ejemplos son modelos ficticios, no ejercicios en servicio real. Sustituye solo por repositorio sandbox explícitamente autorizado, cuenta, referencias e IDs verificados. Comprueba versión y autenticación CLI primero.

**Opciones:** --source-branch y --target-branch seleccionan ramas; --draft crea borrador; --push puede publicar commits locales y se omite aquí.

**Cuándo utilizar:** Cuando rama fuente autorizada publicada está lista para revisión.

**Cuándo evitar:** Evita cambios sin revisar, proyecto objetivo incorrecto o eludir política de ramas protegidas.

**Sintaxis**

`glab mr create -R example-group/example-project --source-branch feat/notes --target-branch main --title "Review notes" --description "Fictional review" --draft`

**Ejemplo básico**

`glab mr create -R example-group/example-project --source-branch feat/notes --target-branch main --title "Review notes" --description "Fictional review" --draft`

Ilustra apertura de borrador desde rama fuente sandbox publicada.

**Ejemplo profesional**

`glab mr create -R example-group/example-project --source-branch feat/docs --target-branch main --title "Review documentation" --description "Describe changes and test evidence"`

Ilustra solicitud autorizada de revisión con ramas fuente y destino explícitas.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Condicional
- Otros estados: Condicional

**Resultado esperado:** Crea MR y devuelve información; no integra rama fuente.

**Efectos y efectos secundarios:** Escribe metadatos de MR; puede activar pipelines o notificaciones. Formas mostradas usan referencias publicadas existentes sin --push.

**Errores comunes:** Tratar creación de MR como aprobación o suponer que ninguna automatización se activa.

**Alternativas:** Usa interfaz web GitLab para creación y revisión autorizadas de MR.

**Recuperación:** Verifica enlace del MR y origen y destino. Si incorrecto, coordina edición o cierre autorizado; cerrar no borra historial del MR.

**Versión y dependencias:** Requiere GitLab CLI (glab) compatible actual, autenticación autorizada, red y permisos relevantes. Comprueba glab help y compatibilidad del servidor.

**Capítulos relacionados**

- [gitlab/04-merge-requests-review-and-forks](../../gitlab/04-merge-requests-review-and-forks/README.es.md)
- [gitlab/08-gitlab-cli-and-platform-comparison](../../gitlab/08-gitlab-cli-and-platform-comparison/README.es.md)

**Documentación oficial**

- <https://docs.gitlab.com/cli/mr/create/>

## glab-mr-view

**`glab mr view`**

**Tipo:** Herramienta externa

**Nivel:** Intermedio

**Buscar por intención:** Revisar cambios, Inspeccionar estado del repositorio

**Riesgo:** Solo lectura. Inspección no autoriza merge. Protege metadatos privados y logs; no expongas credenciales.

**Finalidad:** Inspeccionar detalles y estado reportado de merge request GitLab.

**Requisitos previos:** Ejemplos son modelos ficticios, no ejercicios en servicio real. Sustituye solo por repositorio sandbox explícitamente autorizado, cuenta, referencias e IDs verificados. Comprueba versión y autenticación CLI primero.

**Opciones:** --output json selecciona salida estructurada; --comments incluye discusiones; --web abre página de plataforma.

**Cuándo utilizar:** Al verificar MR revisado y estado actual de integración.

**Cuándo evitar:** No dependas de indicador de conflicto mientras servidor calcula posibilidad de merge.

**Sintaxis**

`glab mr view 42 -R example-group/example-project`

**Ejemplo básico**

`glab mr view 42 -R example-group/example-project`

Inspecciona MR ficticio 42 de sandbox.

**Ejemplo profesional**

`glab mr view 42 -R example-group/example-project --output json`

Inspecciona metadatos estructurados del MR; verifica SHA actual y estado de merge antes de decidir.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Muestra información solicitada; posibilidad de merge y aprobaciones pueden cambiar o ser temporalmente desconocidas.

**Efectos y efectos secundarios:** Lee metadatos de plataforma por red; no altera intencionalmente referencias Git, index, checkout ni recursos de plataforma en forma mostrada.

**Errores comunes:** Tratar MR sin conflictos o aprobación antigua como prueba de todos controles aprobados.

**Alternativas:** Inspecciona detalles web del MR y pipeline asociado a revisión exacta revisada.

**Recuperación:** Inspección no requiere deshacer. Verifica repositorio, ID, permisos y asociación con commit exacto; actualiza estado si incompleto u obsoleto.

**Versión y dependencias:** Requiere GitLab CLI (glab) compatible actual, autenticación autorizada, red y permisos relevantes. Comprueba glab help y compatibilidad del servidor.

**Capítulos relacionados**

- [gitlab/04-merge-requests-review-and-forks](../../gitlab/04-merge-requests-review-and-forks/README.es.md)
- [gitlab/08-gitlab-cli-and-platform-comparison](../../gitlab/08-gitlab-cli-and-platform-comparison/README.es.md)

**Documentación oficial**

- <https://docs.gitlab.com/cli/mr/view/>

## glab-ci-status

**`glab ci status`**

**Tipo:** Herramienta externa

**Nivel:** Intermedio

**Buscar por intención:** Inspeccionar CI

**Riesgo:** Solo lectura. Inspección no autoriza merge. Protege metadatos privados y logs; no expongas credenciales.

**Finalidad:** Inspeccionar estado de pipeline CI/CD GitLab para rama.

**Requisitos previos:** Ejemplos son modelos ficticios, no ejercicios en servicio real. Sustituye solo por repositorio sandbox explícitamente autorizado, cuenta, referencias e IDs verificados. Comprueba versión y autenticación CLI primero.

**Opciones:** --branch selecciona rama; --compact condensa salida; --live o --wait espera actualizaciones o finalización.

**Cuándo utilizar:** Al revisar pipeline reportado de rama e investigar progreso CI.

**Cuándo evitar:** No supongas pipeline más reciente de rama sea pipeline exacto del head del MR, especialmente entre forks.

**Sintaxis**

`glab ci status -R example-group/example-project --branch=main`

**Ejemplo básico**

`glab ci status -R example-group/example-project --branch=main`

Inspecciona estado reportado de pipeline de rama ficticia sandbox.

**Ejemplo profesional**

`glab ci status -R example-group/example-project --branch=feat/docs --compact`

Inspecciona estado condensado de pipeline de rama y verifica commit y asociación al MR.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Muestra estado reportado del pipeline; finalización y asociación a commit deben comprobarse por separado antes de merge.

**Efectos y efectos secundarios:** Lee metadatos de plataforma por red; no altera intencionalmente referencias Git, index, checkout ni recursos de plataforma en forma mostrada.

**Errores comunes:** Confundir pipeline pendiente o ajeno de rama con check obligatorio del MR aprobado.

**Alternativas:** Usa página web del MR y pipeline vinculado para inspeccionar resultados y logs exactos de jobs.

**Recuperación:** Inspección no requiere deshacer. Verifica repositorio, ID, permisos y asociación con commit exacto; actualiza estado si incompleto u obsoleto.

**Versión y dependencias:** Requiere GitLab CLI (glab) compatible actual, autenticación autorizada, red y permisos relevantes. Comprueba glab help y compatibilidad del servidor.

**Capítulos relacionados**

- [gitlab/06-pipelines-and-runners](../../gitlab/06-pipelines-and-runners/README.es.md)
- [ci-cd/04-gitlab-ci-cd](../../ci-cd/04-gitlab-ci-cd/README.es.md)

**Documentación oficial**

- <https://docs.gitlab.com/cli/ci/status/>


---

<!-- navigation-footer -->
[Anterior](../13-security-and-maintenance/README.es.md) · [Índice](../README.es.md) · [Siguiente módulo](../../practical-projects/README.es.md)
<!-- /navigation-footer -->
