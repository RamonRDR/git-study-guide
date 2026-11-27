# Cuestionarios

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Módulo anterior](../../practical-projects/README.es.md) · [Índice](../README.es.md) · [Siguiente](../02-challenges/README.es.md)
<!-- /navigation -->

Intenta primero, consulta las soluciones públicas después. Cuestionarios usan opciones exactas; entrevistas y simulacros requieren autoevaluación honesta. Desafíos usan solo repositorios locales desechables nuevos y checks fijos de estado, sin ejecutar automáticamente comandos de estudiantes. Registros son piloto interno, no contrato final de Learning Hub.

## Instantánea del commit

ID: quiz-snapshot

**Dificultad:** fácil

**Prerrequisitos:** [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.es.md)

Prepara A, edita a B sin preparar y confirma normalmente. ¿Qué versión se registra?

- a. A
- b. B
- c. Ambas

**Pistas:**

- Consulta el prerrequisito antes de decidir.
- Compara index y archivo de trabajo.

**Respuesta:** a

**Explicación:** El index contiene A; B queda sin preparar.

## Preparar archivo

ID: quiz-add

**Dificultad:** fácil

**Prerrequisitos:** [basic-commands/02-status-add-commit](../../basic-commands/02-status-add-commit/README.es.md)

¿Qué comando prepara notes.txt?

- a. git add notes.txt
- b. git log
- c. git branch

**Pistas:**

- Consulta el prerrequisito antes de decidir.
- El destino es el index.

**Respuesta:** a

**Explicación:** Add copia contenido actual al index.

## Diff preparado

ID: quiz-diff

**Dificultad:** fácil

**Prerrequisitos:** [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.es.md)

¿Cuál compara index con HEAD?

- a. git diff
- b. git diff --cached
- c. git log

**Pistas:**

- Consulta el prerrequisito antes de decidir.
- Busca comparación preparada.

**Respuesta:** b

**Explicación:** Diff cached muestra cambios preparados relativos a HEAD.

## Ámbito de identidad

ID: quiz-config

**Dificultad:** fácil

**Prerrequisitos:** [basic-commands/01-init-config-help](../../basic-commands/01-init-config-help/README.es.md)

¿Qué ámbito afecta solo al repositorio actual?

- a. --global
- b. --system
- c. --local

**Pistas:**

- Consulta el prerrequisito antes de decidir.
- Evita cambiar identidad de otros repos.

**Respuesta:** c

**Explicación:** Configuración local es específica del repo.

## Crear y cambiar

ID: quiz-switch

**Dificultad:** fácil

**Prerrequisitos:** [branches/01-create-and-switch](../../branches/01-create-and-switch/README.es.md)

¿Cuál crea y selecciona feat/notes?

- a. git branch feat/notes
- b. git switch -c feat/notes
- c. git switch main

**Pistas:**

- Consulta el prerrequisito antes de decidir.
- Busca ambas operaciones.

**Respuesta:** b

**Explicación:** Crear rama por sí solo no la selecciona.

## HEAD

ID: quiz-head

**Dificultad:** fácil

**Prerrequisitos:** [git-architecture/02-snapshots-head-and-refs](../../git-architecture/02-snapshots-head-and-refs/README.es.md)

Cuando está adjunto a main, ¿qué referencia HEAD?

- a. Ref de rama actual
- b. Servidor remoto
- c. Todos archivos

**Pistas:**

- Consulta el prerrequisito antes de decidir.
- Considera referencia simbólica.

**Respuesta:** a

**Explicación:** HEAD adjunto es simbólico a rama seleccionada.

## Reglas de ignore

ID: quiz-ignore

**Dificultad:** fácil

**Prerrequisitos:** [basic-commands/05-ignore-and-review](../../basic-commands/05-ignore-and-review/README.es.md)

¿.gitignore deja de rastrear archivo ya rastreado?

- a. Siempre
- b. Tras fetch
- c. No

**Pistas:**

- Consulta el prerrequisito antes de decidir.
- Rastreo depende del index.

**Respuesta:** c

**Explicación:** Ignore no elimina entradas existentes del index.

## Clonar

ID: quiz-clone

**Dificultad:** fácil

**Prerrequisitos:** [remote-repositories/01-remote-concepts](../../remote-repositories/01-remote-concepts/README.es.md)

¿Cuál crea copia local normal de repo remoto?

- a. git init
- b. git clone
- c. git status

**Pistas:**

- Consulta el prerrequisito antes de decidir.
- Busca copia de historial existente.

**Respuesta:** b

**Explicación:** Clone obtiene historial y normalmente configura origin.

## Status

ID: quiz-status

**Dificultad:** fácil

**Prerrequisitos:** [basic-commands/02-status-add-commit](../../basic-commands/02-status-add-commit/README.es.md)

¿Cuál inspecciona cambios de working tree e index?

- a. git status
- b. git push
- c. git reset --hard

**Pistas:**

- Consulta el prerrequisito antes de decidir.
- Inspecciona sin descartar ediciones.

**Respuesta:** a

**Explicación:** Status informa cambios preparados, sin preparar y no rastreados.

## Movimiento de etiqueta

ID: quiz-tag

**Dificultad:** fácil

**Prerrequisitos:** [git-internals/03-commits-and-tags](../../git-internals/03-commits-and-tags/README.es.md)

¿Qué ocurre con etiqueta cuando main avanza?

- a. Avanza
- b. Desaparece
- c. Mantiene destino

**Pistas:**

- Consulta el prerrequisito antes de decidir.
- Etiqueta nombra revisión.

**Respuesta:** c

**Explicación:** Etiquetas no avanzan automáticamente con ramas.

## Función de alojamiento

ID: quiz-hosting

**Dificultad:** fácil

**Prerrequisitos:** [fundamentals/03-distributed-and-platforms](../../fundamentals/03-distributed-and-platforms/README.es.md)

¿Cuál es función de plataforma y no objeto Git?

- a. Commit
- b. Pull request
- c. Blob

**Pistas:**

- Consulta el prerrequisito antes de decidir.
- Distingue alojamiento de almacenamiento nativo.

**Respuesta:** b

**Explicación:** PR es registro de colaboración en plataforma.

## Inspección remota

ID: quiz-remote

**Dificultad:** fácil

**Prerrequisitos:** [remote-repositories/01-remote-concepts](../../remote-repositories/01-remote-concepts/README.es.md)

¿Cuál lista URLs fetch y push configuradas?

- a. git remote -v
- b. git branch -d main
- c. git push

**Pistas:**

- Consulta el prerrequisito antes de decidir.
- Lee configuración sin transmitir commits.

**Respuesta:** a

**Explicación:** Remote -v lista URLs sin publicar.

## Fetch

ID: quiz-fetch

**Dificultad:** medio

**Prerrequisitos:** [remote-repositories/02-fetch-and-tracking](../../remote-repositories/02-fetch-and-tracking/README.es.md)

Con refspec habitual, ¿qué ocurre al obtener nueva main remota?

- a. Main local siempre avanza
- b. Seguimiento actualiza; main seleccionada no cambia
- c. Commits locales desaparecen

**Pistas:**

- Consulta el prerrequisito antes de decidir.
- Distingue ref seguimiento de rama local.

**Respuesta:** b

**Explicación:** Fetch actualiza refs configuradas; integración es separada.

## Solo fast-forward

ID: quiz-ff

**Dificultad:** medio

**Prerrequisitos:** [merge-and-conflicts/02-fast-forward](../../merge-and-conflicts/02-fast-forward/README.es.md)

Puntas divergieron. ¿Qué hace merge --ff-only?

- a. Rechaza
- b. Crea commit merge
- c. Rebasa

**Pistas:**

- Consulta el prerrequisito antes de decidir.
- Comprueba ascendencia.

**Respuesta:** a

**Explicación:** Fast-forward no une historiales divergentes.

## Padres del merge

ID: quiz-parents

**Dificultad:** medio

**Prerrequisitos:** [merge-and-conflicts/03-merge-commit](../../merge-and-conflicts/03-merge-commit/README.es.md)

¿Cuántos padres tiene commit merge ordinario de dos ramas sin fast-forward?

- a. 1
- b. 3
- c. 2

**Pistas:**

- Consulta el prerrequisito antes de decidir.
- Ambos historiales quedan conectados.

**Respuesta:** c

**Explicación:** Padres son punta actual anterior y punta integrada.

## Etapas de conflicto

ID: quiz-conflict

**Dificultad:** medio

**Prerrequisitos:** [merge-and-conflicts/04-conflict-resolution](../../merge-and-conflicts/04-conflict-resolution/README.es.md)

¿Cuál lista entradas no fusionadas del index?

- a. git commit
- b. git ls-files -u
- c. git clean -n

**Pistas:**

- Consulta el prerrequisito antes de decidir.
- Inspecciona index, no log de commits.

**Respuesta:** b

**Explicación:** Index puede contener etapas base, ours y theirs.

## Quitar del staging

ID: quiz-unstage

**Dificultad:** medio

**Prerrequisitos:** [history-and-recovery/02-restore](../../history-and-recovery/02-restore/README.es.md)

Con HEAD existente, ¿cuál retira notes.txt de staging sin descartar ediciones?

- a. git restore --staged -- notes.txt
- b. git restore --worktree -- notes.txt
- c. git reset --hard HEAD

**Pistas:**

- Consulta el prerrequisito antes de decidir.
- Archivo de trabajo debe permanecer.

**Respuesta:** a

**Explicación:** Restore --staged usa HEAD por defecto y cambia solo index.

## Reset soft

ID: quiz-soft

**Dificultad:** medio

**Prerrequisitos:** [history-and-recovery/03-reset](../../history-and-recovery/03-reset/README.es.md)

¿Qué conserva reset --soft al mover rama privada?

- a. Solo estado remoto
- b. Nada
- c. Index y working tree

**Pistas:**

- Consulta el prerrequisito antes de decidir.
- Modos afectan ubicaciones distintas.

**Respuesta:** c

**Explicación:** Reset soft mueve HEAD/rama y conserva index y archivos.

## Deshacer compartido

ID: quiz-revert

**Dificultad:** medio

**Prerrequisitos:** [history-and-recovery/04-revert](../../history-and-recovery/04-revert/README.es.md)

¿Cuál deshace commit ordinario compartido sin reescribir historial publicado?

- a. git reset --hard
- b. git revert
- c. git push --force

**Pistas:**

- Consulta el prerrequisito antes de decidir.
- Conserva ascendencia existente.

**Respuesta:** b

**Explicación:** Revert registra cambio inverso en nuevo commit.

## Ámbito stash

ID: quiz-stash

**Dificultad:** medio

**Prerrequisitos:** [history-and-recovery/06-stash](../../history-and-recovery/06-stash/README.es.md)

¿Qué opción stash push incluye no rastreados pero no ignorados?

- a. -u
- b. --keep-index
- c. --all

**Pistas:**

- Consulta el prerrequisito antes de decidir.
- No rastreado no equivale a ignorado.

**Respuesta:** a

**Explicación:** -u incluye no rastreados; --all incluye también ignorados.

## Cherry-pick

ID: quiz-pick

**Dificultad:** medio

**Prerrequisitos:** [history-and-recovery/07-cherry-pick](../../history-and-recovery/07-cherry-pick/README.es.md)

Cherry-pick ordinario exitoso de commit no vacío sobre otra punta suele crear ¿qué?

- a. Nuevo commit con cambios aplicados
- b. Rama remota
- c. Merge de dos padres

**Pistas:**

- Consulta el prerrequisito antes de decidir.
- Considera aplicar cambio en vez de fusionar historial.

**Respuesta:** a

**Explicación:** Parche aplicado en nuevo contexto de padre.

## Reflog

ID: quiz-reflog

**Dificultad:** medio

**Prerrequisitos:** [history-and-recovery/05-reflog](../../history-and-recovery/05-reflog/README.es.md)

¿Push normal transfiere tu reflog local?

- a. Sí
- b. No
- c. Solo con etiquetas

**Pistas:**

- Consulta el prerrequisito antes de decidir.
- Distingue transferencia de objetos de metadatos locales.

**Respuesta:** b

**Explicación:** Reflogs son metadatos locales y pueden caducar.

## Revisión de revisión

ID: quiz-review

**Dificultad:** medio

**Prerrequisitos:** [github/04-pull-requests-and-review](../../github/04-pull-requests-and-review/README.es.md)

Nuevo commit llega al PR tras checks verdes. ¿Qué revisión necesita verificación?

- a. Primer commit
- b. Cualquier revisión verde
- c. Head previsto más reciente

**Pistas:**

- Consulta el prerrequisito antes de decidir.
- Evidencia debe identificar SHA probado.

**Respuesta:** c

**Explicación:** Checks de revisiones antiguas no cubren cambios nuevos.

## Credencial expuesta

ID: quiz-secret

**Dificultad:** medio

**Prerrequisitos:** [security/05-secrets-and-disclosure-prevention](../../security/05-secrets-and-disclosure-prevention/README.es.md)

Token real entró en historial público. ¿Qué acción esencial viene primero?

- a. Revocar o rotar
- b. Solo eliminar archivo
- c. Renombrar rama

**Pistas:**

- Consulta el prerrequisito antes de decidir.
- Copias fuera del repo pueden persistir.

**Respuesta:** a

**Explicación:** Supón compromiso; limpieza de historial es distinta de invalidación.

## Identidad en rebase

ID: quiz-rebase

**Dificultad:** difícil

**Prerrequisitos:** [merge-and-conflicts/06-rebase-and-conflicts](../../merge-and-conflicts/06-rebase-and-conflicts/README.es.md)

Rebase de commits sobre padre diferente normalmente cambia ¿qué?

- a. Solo permisos
- b. IDs de commits reaplicados
- c. Remoto automáticamente

**Pistas:**

- Consulta el prerrequisito antes de decidir.
- Piensa en padre almacenado.

**Respuesta:** b

**Explicación:** Objetos commit incluyen IDs de padres; reaplicación crea nuevos objetos cuando hace falta.

## Squash

ID: quiz-squash

**Dificultad:** difícil

**Prerrequisitos:** [merge-and-conflicts/05-squash-merge](../../merge-and-conflicts/05-squash-merge/README.es.md)

Tras merge --squash exitoso, antes de commit, ¿qué es cierto?

- a. HEAD se movió
- b. MERGE\_HEAD guarda segundo padre
- c. Cambios preparados; HEAD intacto

**Pistas:**

- Consulta el prerrequisito antes de decidir.
- Commit es paso separado.

**Respuesta:** c

**Explicación:** Squash prepara cambios sin crear MERGE\_HEAD ni mover HEAD.

## Diff de tres puntos

ID: quiz-three-dot

**Dificultad:** difícil

**Prerrequisitos:** [basic-commands/03-diff-log-show](../../basic-commands/03-diff-log-show/README.es.md)

Con una merge base, ¿qué compara git diff main...feature?

- a. Merge base a punta feature
- b. Punta feature a main
- c. Index a HEAD

**Pistas:**

- Consulta el prerrequisito antes de decidir.
- Primer punto deriva de ascendencia.

**Respuesta:** a

**Explicación:** Diff tres puntos compara merge base a segunda punta; log difiere.

## Force-with-lease

ID: quiz-lease

**Dificultad:** difícil

**Prerrequisitos:** [remote-repositories/03-pull-push-and-divergence](../../remote-repositories/03-pull-push-and-divergence/README.es.md)

¿Contra qué protege lease de OID esperado explícito?

- a. Toda pérdida de datos
- b. Ref remota distinta de lo esperado
- c. Todos conflictos merge

**Pistas:**

- Consulta el prerrequisito antes de decidir.
- Compara ref actual con expectativa.

**Respuesta:** b

**Explicación:** Lease es condicional, no garantía contra reescrituras dañinas.

## Bisect

ID: quiz-bisect

**Dificultad:** difícil

**Prerrequisitos:** [advanced-git/01-bisect](../../advanced-git/01-bisect/README.es.md)

¿Qué debe clasificar prueba útil de bisect?

- a. Popularidad del autor
- b. Tamaño de archivo
- c. Propiedad objetivo de revisión seleccionada

**Pistas:**

- Consulta el prerrequisito antes de decidir.
- Prueba la revisión, no metadatos ajenos.

**Respuesta:** c

**Explicación:** Clasificación good/bad consistente reduce frontera conocida; salta incertidumbre.

## Identidad del blob

ID: quiz-blob

**Dificultad:** difícil

**Prerrequisitos:** [git-internals/02-blobs-and-trees](../../git-internals/02-blobs-and-trees/README.es.md)

Dos archivos tienen bytes blob almacenados iguales en mismo formato. ¿Qué puede diferir?

- a. Ruta y modo tree
- b. Bytes almacenados
- c. Tipo objeto blob

**Pistas:**

- Consulta el prerrequisito antes de decidir.
- ¿Qué objeto guarda nombres?

**Respuesta:** a

**Explicación:** Blob guarda contenido; tree guarda nombres y modos.

## Peeling de etiqueta

ID: quiz-peel

**Dificultad:** difícil

**Prerrequisitos:** [git-internals/03-commits-and-tags](../../git-internals/03-commits-and-tags/README.es.md)

¿Qué solicita git rev-parse 'v1.0.0^{commit}' de etiqueta apuntando a commit?

- a. Mensaje de etiqueta
- b. ID del commit subyacente
- c. Ruta de trabajo

**Pistas:**

- Consulta el prerrequisito antes de decidir.
- Distingue objeto etiqueta de su destino.

**Respuesta:** b

**Explicación:** Peeling resuelve a commit o falla.

## Alcanzabilidad

ID: quiz-reachable

**Dificultad:** difícil

**Prerrequisitos:** [git-internals/09-reflogs-and-reachability](../../git-internals/09-reflogs-and-reachability/README.es.md)

¿Por qué nombrar commit desplazado hallado en reflog con rama de recuperación?

- a. Desactivar todo GC
- b. Copiar archivos sin confirmar
- c. Hacer commit alcanzable mediante ref

**Pistas:**

- Consulta el prerrequisito antes de decidir.
- Piensa en referencia persistente.

**Respuesta:** c

**Explicación:** Rama hace commit alcanzable independientemente de entradas temporales reflog.

## Worktree

ID: quiz-worktree

**Dificultad:** difícil

**Prerrequisitos:** [advanced-git/02-worktree](../../advanced-git/02-worktree/README.es.md)

¿Qué suele estar separado en worktrees vinculados?

- a. Archivos de trabajo, HEAD e index
- b. Cada objeto Git
- c. Todas refs de rama

**Pistas:**

- Consulta el prerrequisito antes de decidir.
- Distingue almacenamiento compartido de checkout.

**Respuesta:** a

**Explicación:** Worktrees comparten objetos y mayoría de refs, pero tienen HEAD/index/archivos propios.

## Gitlink

ID: quiz-gitlink

**Dificultad:** difícil

**Prerrequisitos:** [advanced-git/03-submodules](../../advanced-git/03-submodules/README.es.md)

¿Qué registra gitlink del superproyecto?

- a. Todos archivos anidados
- b. ID de commit del submódulo
- c. Solo nombre de rama

**Pistas:**

- Consulta el prerrequisito antes de decidir.
- Dependencia se fija a una revisión.

**Respuesta:** b

**Explicación:** Gitlink guarda commit referenciado, no tree anidado.

## Límites de firma

ID: quiz-signature

**Dificultad:** difícil

**Prerrequisitos:** [security/09-commit-and-tag-signing](../../security/09-commit-and-tag-signing/README.es.md)

¿Firma criptográfica válida sola prueba seguridad y autorización?

- a. Siempre
- b. Si main
- c. No

**Pistas:**

- Consulta el prerrequisito antes de decidir.
- Identifica qué atestigua una firma.

**Respuesta:** c

**Explicación:** Verificación criptográfica difiere de política de confianza y revisión.

## Clon parcial

ID: quiz-partial

**Dificultad:** difícil

**Prerrequisitos:** [advanced-git/08-partial-and-shallow-clone](../../advanced-git/08-partial-and-shallow-clone/README.es.md)

¿Por qué acceso posterior a archivo en clon parcial blob:none puede exigir red?

- a. Blobs prometidos pueden requerir fetch bajo demanda
- b. Todos commits fueron eliminados
- c. Todos comandos son llamadas API remota

**Pistas:**

- Consulta el prerrequisito antes de decidir.
- Transferencia inicial puede ser incompleta por diseño.

**Respuesta:** a

**Explicación:** Objetos prometidos ausentes pueden obtenerse bajo demanda.

---

<!-- navigation-footer -->
[Módulo anterior](../../practical-projects/README.es.md) · [Índice](../README.es.md) · [Siguiente](../02-challenges/README.es.md)
<!-- /navigation-footer -->
