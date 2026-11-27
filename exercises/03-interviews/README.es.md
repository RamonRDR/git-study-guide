# Preguntas de entrevista

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../02-challenges/README.es.md) · [Índice](../README.es.md) · [Siguiente](../04-mock-assessments/README.es.md)
<!-- /navigation -->

Intenta primero, consulta las soluciones públicas después. Cuestionarios usan opciones exactas; entrevistas y simulacros requieren autoevaluación honesta. Desafíos usan solo repositorios locales desechables nuevos y checks fijos de estado, sin ejecutar automáticamente comandos de estudiantes. Registros son piloto interno, no contrato final de Learning Hub.

## Control de versiones

ID: interview-version-control

**Dificultad:** fácil

**Prerrequisitos:** [fundamentals/01-version-control](../../fundamentals/01-version-control/README.es.md)

Explica por qué Git es útil incluso trabajando solo.

**Pistas:**

- Explica estado o política pertinente antes de nombrar comandos.
- Menciona instantáneas y comparación.

**Respuesta esperada:** Git registra instantáneas intencionales, permite comparar revisiones y experimentar de forma aislada. No guarda toda edición automáticamente ni sustituye copias de seguridad.

**Rúbrica:**

- Menciona instantáneas y comparación.
- Explica límite del trabajo sin commit.

**Seguimiento:**

- ¿Cómo inspeccionarías revisión anterior?

**Explicación:** Compara tu razonamiento con respuesta esperada. Rúbrica mide conceptos explícitos, no palabras exactas; asigna un punto por criterio cumplido, cero en otro caso.

## Tres ubicaciones Git

ID: interview-three-states

**Dificultad:** fácil

**Prerrequisitos:** [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.es.md)

Explica working tree, index y HEAD usando un archivo editado.

**Pistas:**

- Explica estado o política pertinente antes de nombrar comandos.
- Define correctamente tres ubicaciones.

**Respuesta esperada:** Working tree es contenido editable, index prepara próximo commit ordinario, HEAD resuelve revisión actual. Prepara A, edita B, commit: A confirmado, B sin preparar.

**Rúbrica:**

- Define correctamente tres ubicaciones.
- Rastrea A y B sin confundir.

**Seguimiento:**

- ¿Qué diff muestra A respecto a HEAD?

**Explicación:** Compara tu razonamiento con respuesta esperada. Rúbrica mide conceptos explícitos, no palabras exactas; asigna un punto por criterio cumplido, cero en otro caso.

## Rama como ref

ID: interview-branch

**Dificultad:** fácil

**Prerrequisitos:** [branches/01-create-and-switch](../../branches/01-create-and-switch/README.es.md)

¿Qué es rama y qué ocurre al confirmar commit en ella?

**Pistas:**

- Explica estado o política pertinente antes de nombrar comandos.
- Describe ref, no copia de carpeta.

**Respuesta esperada:** Rama local es ref móvil a commit. Con HEAD adjunto, commit ordinario actualiza rama actual mientras otras refs normalmente quedan iguales.

**Rúbrica:**

- Describe ref, no copia de carpeta.
- Distingue creación de selección de rama.

**Seguimiento:**

- ¿Qué difiere con HEAD separado?

**Explicación:** Compara tu razonamiento con respuesta esperada. Rúbrica mide conceptos explícitos, no palabras exactas; asigna un punto por criterio cumplido, cero en otro caso.

## Inspeccionar antes del commit

ID: interview-status-diff

**Dificultad:** fácil

**Prerrequisitos:** [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.es.md)

¿Cómo revisar qué entrará en commit ordinario?

**Pistas:**

- Explica estado o política pertinente antes de nombrar comandos.
- Identifica comparación preparada.

**Respuesta esperada:** Usa git status para estado, git diff para ediciones rastreadas sin preparar y git diff --cached para index contra HEAD. Prepara solo archivos deseados y comprueba.

**Rúbrica:**

- Identifica comparación preparada.
- Menciona no rastreados y staging selectivo.

**Seguimiento:**

- ¿Por qué git diff puede estar vacío con cambios preparados?

**Explicación:** Compara tu razonamiento con respuesta esperada. Rúbrica mide conceptos explícitos, no palabras exactas; asigna un punto por criterio cumplido, cero en otro caso.

## Ignore y rastreo

ID: interview-ignore

**Dificultad:** fácil

**Prerrequisitos:** [basic-commands/05-ignore-and-review](../../basic-commands/05-ignore-and-review/README.es.md)

¿Por qué archivo rastreado aún aparece tras regla ignore?

**Pistas:**

- Explica estado o política pertinente antes de nombrar comandos.
- Distingue ignorado de rastreado.

**Respuesta esperada:** Ignore normalmente filtra rutas no rastreadas. Archivos rastreados siguen en index hasta retirada intencional del rastreo. Revisa efectos antes del commit.

**Rúbrica:**

- Distingue ignorado de rastreado.
- Explica que historial no se borra.

**Seguimiento:**

- ¿Qué cambia git rm --cached?

**Explicación:** Compara tu razonamiento con respuesta esperada. Rúbrica mide conceptos explícitos, no palabras exactas; asigna un punto por criterio cumplido, cero en otro caso.

## Init y clone

ID: interview-clone-init

**Dificultad:** fácil

**Prerrequisitos:** [remote-repositories/01-remote-concepts](../../remote-repositories/01-remote-concepts/README.es.md)

¿Cuándo elegir init en vez de clone?

**Pistas:**

- Explica estado o política pertinente antes de nombrar comandos.
- Explica historial nuevo frente a existente.

**Respuesta esperada:** Init inicia metadatos Git en repo elegido; clone obtiene historial existente y normalmente configura origin y checkout. Evita directorio equivocado.

**Rúbrica:**

- Explica historial nuevo frente a existente.
- Identifica origin como configuración habitual.

**Seguimiento:**

- ¿Cómo verificar raíz del repo?

**Explicación:** Compara tu razonamiento con respuesta esperada. Rúbrica mide conceptos explícitos, no palabras exactas; asigna un punto por criterio cumplido, cero en otro caso.

## Comunicar cambio

ID: interview-commit-message

**Dificultad:** fácil

**Prerrequisitos:** [professional-workflows/06-conventional-commits](../../professional-workflows/06-conventional-commits/README.es.md)

¿Qué hace útil un mensaje de commit?

**Pistas:**

- Explica estado o política pertinente antes de nombrar comandos.
- Da ejemplo acotado como docs: clarify notes.

**Respuesta esperada:** Describe intención acotada y, cuando convenga, motivo. Conventional Commits es convención de equipo, no requisito Git. No incluyas secretos ni cambios ajenos.

**Rúbrica:**

- Da ejemplo acotado como docs: clarify notes.
- Separa convención de requisitos Git.

**Seguimiento:**

- ¿Cuándo dos cambios deben ser commits separados?

**Explicación:** Compara tu razonamiento con respuesta esperada. Rúbrica mide conceptos explícitos, no palabras exactas; asigna un punto por criterio cumplido, cero en otro caso.

## Git y plataforma

ID: interview-platform

**Dificultad:** fácil

**Prerrequisitos:** [fundamentals/03-distributed-and-platforms](../../fundamentals/03-distributed-and-platforms/README.es.md)

¿Git funciona sin GitHub o GitLab? Explica.

**Pistas:**

- Explica estado o política pertinente antes de nombrar comandos.
- Identifica operaciones locales nativas.

**Respuesta esperada:** Sí. Git almacena y manipula repos locales e intercambia objetos con remotos. Alojamiento añade acceso, revisiones PR/MR y CI; cuentas no son necesarias localmente.

**Rúbrica:**

- Identifica operaciones locales nativas.
- Menciona funciones de colaboración de plataforma.

**Seguimiento:**

- ¿Cómo practican dos desarrolladores offline?

**Explicación:** Compara tu razonamiento con respuesta esperada. Rúbrica mide conceptos explícitos, no palabras exactas; asigna un punto por criterio cumplido, cero en otro caso.

## Fetch y pull

ID: interview-fetch-pull

**Dificultad:** medio

**Prerrequisitos:** [remote-repositories/02-fetch-and-tracking](../../remote-repositories/02-fetch-and-tracking/README.es.md)

Ref de seguimiento desactualizada. ¿Cómo actualizar antes de decidir integración?

**Pistas:**

- Explica estado o política pertinente antes de nombrar comandos.
- Distingue fetch de integración.

**Respuesta esperada:** Haz fetch origin, inspecciona divergencia main y origin/main, luego elige política. Pull combina fetch e integración según opciones/config; ff-only rechaza divergencia.

**Rúbrica:**

- Distingue fetch de integración.
- Describe decisión segura ante divergencia.

**Seguimiento:**

- ¿Por qué pull puede fallar aunque fetch funcione?

**Explicación:** Compara tu razonamiento con respuesta esperada. Rúbrica mide conceptos explícitos, no palabras exactas; asigna un punto por criterio cumplido, cero en otro caso.

## Merge o rebase

ID: interview-merge-rebase

**Dificultad:** medio

**Prerrequisitos:** [merge-and-conflicts/06-rebase-and-conflicts](../../merge-and-conflicts/06-rebase-and-conflicts/README.es.md)

Compara merge y rebase para rama feature.

**Pistas:**

- Explica estado o política pertinente antes de nombrar comandos.
- Explica diferencias de topología e identidad.

**Respuesta esperada:** Merge integra historiales, a veces por fast-forward o commit merge. Rebase reaplica commits en nueva base y normalmente cambia IDs reaplicados. Evita reescribir historial compartido sin coordinación.

**Rúbrica:**

- Explica diferencias de topología e identidad.
- Discute política de equipo e historial compartido.

**Seguimiento:**

- ¿Cuándo es posible fast-forward?

**Explicación:** Compara tu razonamiento con respuesta esperada. Rúbrica mide conceptos explícitos, no palabras exactas; asigna un punto por criterio cumplido, cero en otro caso.

## Triaje de conflicto

ID: interview-resolve

**Dificultad:** medio

**Prerrequisitos:** [merge-and-conflicts/04-conflict-resolution](../../merge-and-conflicts/04-conflict-resolution/README.es.md)

Describe proceso seguro para resolver conflicto merge.

**Pistas:**

- Explica estado o política pertinente antes de nombrar comandos.
- Explica inspección y resolución intencional.

**Respuesta esperada:** Inspecciona estado y entradas no fusionadas, entiende base/ours/theirs, elige contenido correcto, prepara resolución, ejecuta pruebas y termina. Conserva ediciones deseadas antes de abortar.

**Rúbrica:**

- Explica inspección y resolución intencional.
- Menciona pruebas y límites de abort seguro.

**Seguimiento:**

- ¿Por qué quitar marcadores no basta?

**Explicación:** Compara tu razonamiento con respuesta esperada. Rúbrica mide conceptos explícitos, no palabras exactas; asigna un punto por criterio cumplido, cero en otro caso.

## Reset y revert

ID: interview-reset-revert

**Dificultad:** medio

**Prerrequisitos:** [history-and-recovery/03-reset](../../history-and-recovery/03-reset/README.es.md)

¿Cómo deshacer commit privado frente a publicado?

**Pistas:**

- Explica estado o política pertinente antes de nombrar comandos.
- Contrasta mover refs y crear nuevo commit.

**Respuesta esperada:** En historial privado, inspecciona estado y elige modo reset solo con destino conocido y trabajo conservado. En publicado, prefiere revert/commit correctivo revisado. Hard reset puede descartar ediciones.

**Rúbrica:**

- Contrasta mover refs y crear nuevo commit.
- Indica riesgos destructivos y política compartida.

**Seguimiento:**

- ¿Qué conserva reset soft?

**Explicación:** Compara tu razonamiento con respuesta esperada. Rúbrica mide conceptos explícitos, no palabras exactas; asigna un punto por criterio cumplido, cero en otro caso.

## Límites de stash

ID: interview-stash

**Dificultad:** medio

**Prerrequisitos:** [history-and-recovery/06-stash](../../history-and-recovery/06-stash/README.es.md)

¿Qué comprobar antes de usar stash para cambiar tareas? Explica el ámbito de archivos no rastreados e ignorados y cómo apply difiere de pop en éxito o conflicto.

**Pistas:**

- Explica estado o política pertinente antes de nombrar comandos.
- Menciona ámbito no rastreado/ignorado.

**Respuesta esperada:** Inspecciona archivos preparados, sin preparar y no rastreados. Por defecto stash push guarda cambios rastreados; -u incluye no rastreados y --all también incluye ignorados. Elige el ámbito deliberadamente, registra la entrada y comprueba el estado de trabajo. Apply intenta restaurar cambios conservando la entrada del stash; pop la elimina tras aplicación exitosa, pero la conserva si conflictos impiden la aplicación. Inspecciona y resuelve conflictos antes de cualquier drop deliberado. Stash es local, no un respaldo duradero.

**Rúbrica:**

- Menciona ámbito no rastreado/ignorado.
- Distingue apply y pop en éxito/conflicto.

**Seguimiento:**

- ¿Por qué apply puede generar conflicto?

**Explicación:** Compara tu razonamiento con respuesta esperada. Rúbrica mide conceptos explícitos, no palabras exactas; asigna un punto por criterio cumplido, cero en otro caso.

## Contribución mediante fork

ID: interview-fork

**Dificultad:** medio

**Prerrequisitos:** [github/05-forks-and-open-source](../../github/05-forks-and-open-source/README.es.md)

Describe flujo de contribución sin permiso push upstream.

**Pistas:**

- Explica estado o política pertinente antes de nombrar comandos.
- Distingue destinos origin y upstream.

**Respuesta esperada:** Crea fork o usa repo contribuyente autorizado, clona, nombra upstream aparte, basa feature en revisión upstream conocida, publica solo en fork y solicita revisión. Respeta política y comprueba diff exacto.

**Rúbrica:**

- Distingue destinos origin y upstream.
- Describe límites de permisos y revisión.

**Seguimiento:**

- ¿Cómo sincronizar fork de forma segura?

**Explicación:** Compara tu razonamiento con respuesta esperada. Rúbrica mide conceptos explícitos, no palabras exactas; asigna un punto por criterio cumplido, cero en otro caso.

## Gate de calidad CI

ID: interview-ci-gate

**Dificultad:** medio

**Prerrequisitos:** [ci-cd/09-quality-gates-and-troubleshooting](../../ci-cd/09-quality-gates-and-troubleshooting/README.es.md)

Job CI falla tras push. ¿Cómo diagnosticar?

**Pistas:**

- Explica estado o política pertinente antes de nombrar comandos.
- Usa logs reales y revisión exacta.

**Respuesta esperada:** Identifica SHA, job y paso fallido, inspecciona logs, reproduce en entorno aislado si posible, corrige causa y ejecuta checks en nuevo SHA. No desactives gates para obtener verde.

**Rúbrica:**

- Usa logs reales y revisión exacta.
- Exige nueva ejecución tras cambios.

**Seguimiento:**

- ¿Prueba verde demuestra despliegue exitoso?

**Explicación:** Compara tu razonamiento con respuesta esperada. Rúbrica mide conceptos explícitos, no palabras exactas; asigna un punto por criterio cumplido, cero en otro caso.

## Versionado de lanzamiento

ID: interview-release

**Dificultad:** medio

**Prerrequisitos:** [professional-workflows/07-semantic-versioning](../../professional-workflows/07-semantic-versioning/README.es.md)

¿Cómo decidir versión SemVer e identificar revisión de lanzamiento?

**Pistas:**

- Explica estado o política pertinente antes de nombrar comandos.
- Basa versión en contrato público.

**Respuesta esperada:** Con API/contrato público definido, elige major para incompatibilidad, minor para funcionalidad retrocompatible, patch para correcciones compatibles. Revisa y prueba revisión exacta, luego etiqueta anotada según política. Lanzamiento alojado es distinto.

**Rúbrica:**

- Basa versión en contrato público.
- Distingue etiqueta de lanzamiento de plataforma.

**Seguimiento:**

- ¿Y si etiqueta publicada es incorrecta?

**Explicación:** Compara tu razonamiento con respuesta esperada. Rúbrica mide conceptos explícitos, no palabras exactas; asigna un punto por criterio cumplido, cero en otro caso.

## Modelo de objetos

ID: interview-objects

**Dificultad:** difícil

**Prerrequisitos:** [git-internals/02-blobs-and-trees](../../git-internals/02-blobs-and-trees/README.es.md)

Rastrea commit hasta contenido almacenado de archivos.

**Pistas:**

- Explica estado o política pertinente antes de nombrar comandos.
- Describe papeles commit, tree y blob.

**Respuesta esperada:** Commit referencia tree raíz y padres. Trees registran nombres, modos e IDs, refiriendo trees/blobs recursivamente. Blobs guardan bytes, no nombres. Refs nombran commits independientemente de almacenamiento físico.

**Rúbrica:**

- Describe papeles commit, tree y blob.
- Explica por qué contenido idéntico puede compartir blob.

**Seguimiento:**

- ¿De qué depende hash de commit además de tree?

**Explicación:** Compara tu razonamiento con respuesta esperada. Rúbrica mide conceptos explícitos, no palabras exactas; asigna un punto por criterio cumplido, cero en otro caso.

## Recuperabilidad

ID: interview-recovery

**Dificultad:** difícil

**Prerrequisitos:** [git-internals/09-reflogs-and-reachability](../../git-internals/09-reflogs-and-reachability/README.es.md)

Punta privada desapareció tras reset. Explica recuperación y límites.

**Pistas:**

- Explica estado o política pertinente antes de nombrar comandos.
- Explica recuperación mediante ref verificada.

**Respuesta esperada:** Detén operaciones destructivas; inspecciona reflog e IDs conocidos, confirma contenido y ascendencia, crea ref de recuperación y verifica. Reflogs caducan y objetos inalcanzables pueden podarse; ediciones sin commit quizá nunca se registraron.

**Rúbrica:**

- Explica recuperación mediante ref verificada.
- Rechaza explícitamente recuperación garantizada.

**Seguimiento:**

- ¿Por qué evitar gc durante recuperación?

**Explicación:** Compara tu razonamiento con respuesta esperada. Rúbrica mide conceptos explícitos, no palabras exactas; asigna un punto por criterio cumplido, cero en otro caso.

## Actualización remota concurrente

ID: interview-lease

**Dificultad:** difícil

**Prerrequisitos:** [remote-repositories/03-pull-push-and-divergence](../../remote-repositories/03-pull-push-and-divergence/README.es.md)

Explica por qué force-with-lease es más seguro que force, pero no política suficiente.

**Pistas:**

- Explica estado o política pertinente antes de nombrar comandos.
- Describe comparación condicional de ref.

**Respuesta esperada:** Lease compara ref remota con valor esperado y rechaza divergencia. Expectativa explícita evita depender de refs tracking actualizadas por fetch de fondo. Incluso lease exitoso puede descartar historial; exige propiedad, coordinación y política.

**Rúbrica:**

- Describe comparación condicional de ref.
- Explica por qué lease exitoso no es consentimiento.

**Seguimiento:**

- ¿Qué hacer si lease falla?

**Explicación:** Compara tu razonamiento con respuesta esperada. Rúbrica mide conceptos explícitos, no palabras exactas; asigna un punto por criterio cumplido, cero en otro caso.

## Checkout paralelo

ID: interview-worktree

**Dificultad:** difícil

**Prerrequisitos:** [advanced-git/02-worktree](../../advanced-git/02-worktree/README.es.md)

¿Cómo inspeccionar lanzamiento mientras desarrollas feature?

**Pistas:**

- Explica estado o política pertinente antes de nombrar comandos.
- Identifica estado compartido e independiente.

**Respuesta esperada:** Worktree vinculada ofrece archivos, HEAD e index separados, compartiendo objetos y muchas refs. Crea rama separada adecuada o worktree detached, comprueba ruta y elimina solo worktree propia limpia.

**Rúbrica:**

- Identifica estado compartido e independiente.
- Explica selección segura de rama/ruta y limpieza.

**Seguimiento:**

- ¿Por qué no seleccionar misma rama dos veces por defecto?

**Explicación:** Compara tu razonamiento con respuesta esperada. Rúbrica mide conceptos explícitos, no palabras exactas; asigna un punto por criterio cumplido, cero en otro caso.

## Dependencia fijada

ID: interview-submodules

**Dificultad:** difícil

**Prerrequisitos:** [advanced-git/03-submodules](../../advanced-git/03-submodules/README.es.md)

Explica qué significa actualizar submódulo para reproducibilidad.

**Pistas:**

- Explica estado o política pertinente antes de nombrar comandos.
- Explica papeles gitlink y configuración.

**Respuesta esperada:** Superproyecto guarda gitlink a commit específico y .gitmodules describe configuración. Checkout reproducible exige commit disponible e inicialización/update adecuados. Actualizar checkout anidado solo no confirma dependencia en superproyecto.

**Rúbrica:**

- Explica papeles gitlink y configuración.
- Menciona disponibilidad y commit de fijación.

**Seguimiento:**

- ¿Qué ocurre si commit referenciado no está disponible?

**Explicación:** Compara tu razonamiento con respuesta esperada. Rúbrica mide conceptos explícitos, no palabras exactas; asigna un punto por criterio cumplido, cero en otro caso.

## Búsqueda de regresión

ID: interview-bisect

**Dificultad:** difícil

**Prerrequisitos:** [advanced-git/01-bisect](../../advanced-git/01-bisect/README.es.md)

¿Cómo diseñar experimento fiable de git bisect?

**Pistas:**

- Explica estado o política pertinente antes de nombrar comandos.
- Define good/bad y prueba fiable.

**Respuesta esperada:** Establece frontera good/bad conocida, usa clasificación determinista estable por revisión, omite commits realmente no comprobables, registra entorno/evidencia, verifica candidato y termina bisect. Comportamiento no monótono puede complicar resultados.

**Rúbrica:**

- Define good/bad y prueba fiable.
- Discute skip, verificación y limpieza.

**Seguimiento:**

- ¿Y si prueba es inestable?

**Explicación:** Compara tu razonamiento con respuesta esperada. Rúbrica mide conceptos explícitos, no palabras exactas; asigna un punto por criterio cumplido, cero en otro caso.

## Integración basada en evidencia

ID: interview-audit

**Dificultad:** difícil

**Prerrequisitos:** [security/12-governance-audit-and-traceability](../../security/12-governance-audit-and-traceability/README.es.md)

¿Cómo probar que commit squash integrado coincide con cambio revisado?

**Pistas:**

- Explica estado o política pertinente antes de nombrar comandos.
- Asocia evidencia a SHA y base exactos.

**Respuesta esperada:** Registra head/tree revisados y base, comprueba checks/revisión y autorización de SHA, exige head esperado en merge. Si base no cambió y feature la incluye, compara tree integrado con revisado y padre único con base; verifica post-merge y metadatos.

**Rúbrica:**

- Asocia evidencia a SHA y base exactos.
- Explica igualdad de tree condicionada a base intacta.

**Seguimiento:**

- ¿Por qué base distinta puede exigir nueva revisión?

**Explicación:** Compara tu razonamiento con respuesta esperada. Rúbrica mide conceptos explícitos, no palabras exactas; asigna un punto por criterio cumplido, cero en otro caso.

## Incidente de credencial

ID: interview-secret-incident

**Dificultad:** difícil

**Prerrequisitos:** [security/11-credential-exposure-and-incident-response](../../security/11-credential-exposure-and-incident-response/README.es.md)

Responde a credencial confirmada y publicada por accidente.

**Pistas:**

- Explica estado o política pertinente antes de nombrar comandos.
- Prioriza revocación antes de limpiar historial.

**Respuesta esperada:** Trata como comprometida: revoca/rota, limita exposición y notifica responsables, investiga uso, quita secreto de archivos actuales y coordina limpieza de historial. Copias pueden persistir; prevención incluye escaneo y mínimo privilegio.

**Rúbrica:**

- Prioriza revocación antes de limpiar historial.
- Reconoce copias persistentes y coordinación del incidente.

**Seguimiento:**

- ¿Por qué eliminar archivo no basta?

**Explicación:** Compara tu razonamiento con respuesta esperada. Rúbrica mide conceptos explícitos, no palabras exactas; asigna un punto por criterio cumplido, cero en otro caso.

---

<!-- navigation-footer -->
[Anterior](../02-challenges/README.es.md) · [Índice](../README.es.md) · [Siguiente](../04-mock-assessments/README.es.md)
<!-- /navigation-footer -->
