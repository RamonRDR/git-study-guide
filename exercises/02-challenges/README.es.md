# Desafíos prácticos

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../01-quizzes/README.es.md) · [Índice](../README.es.md) · [Siguiente](../03-interviews/README.es.md)
<!-- /navigation -->

Intenta primero, consulta las soluciones públicas después. Cuestionarios usan opciones exactas; entrevistas y simulacros requieren autoevaluación honesta. Desafíos usan solo repositorios locales desechables nuevos y checks fijos de estado, sin ejecutar automáticamente comandos de estudiantes. Registros son piloto interno, no contrato final de Learning Hub.

## Primera instantánea confirmada

ID: challenge-first-commit

**Dificultad:** fácil

**Prerrequisitos:** [practical-projects/01-my-first-repository](../../practical-projects/01-my-first-repository/README.es.md) · [getting-started/05-first-commit](../../getting-started/05-first-commit/README.es.md)

Confirma notes.txt con status: ready; termina limpio en main con un commit.

**Tiempo (min):** 10

**Ejecución:** local_only · Requiere Git real en repo desechable nuevo; sin afirmación de runtime navegador.

**Preparación:** Inicia repo local nuevo usando solo Preparación desechable del proyecto 01 (prerrequisitos vinculados); comprueba main, identidad ficticia y sin remoto. Git 2.40+ y Bash/Git Bash. Ejecuta comandos individualmente, detente ante fallo inesperado y usa finales LF. Usa repo nuevo vacío.

**Pistas:**

- Archivo debe entrar al index primero.
- Inspecciona contenido preparado antes de confirmar.

**Solución:**

- Escribe exactamente status: ready más LF final en notes.txt.
- git add notes.txt
- git diff --cached
- git commit -m 'docs: add notes'
- Tras comprobar resultados, cierra shell dedicada y elimina solo directorio temporal verificado mediante gestor de archivos. Nunca uses repo del guía.

**Checks de estado:**

- kind=branch, value=main
- kind=commit-count, value=1
- file=notes.txt, kind=head-content, value=status: ready
- file=notes.txt, kind=tracked
- kind=clean

**Explicación:** Estado limpio solo no basta: contenido confirmado y conteo deben coincidir.

## Separar staging y trabajo

ID: challenge-staged-snapshot

**Dificultad:** fácil

**Prerrequisitos:** [practical-projects/01-my-first-repository](../../practical-projects/01-my-first-repository/README.es.md) · [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.es.md)

Deja HEAD en draft, prepara ready y cambia archivo a experiment sin preparar otra vez.

**Tiempo (min):** 10

**Ejecución:** local_only · Requiere Git real en repo desechable nuevo; sin afirmación de runtime navegador.

**Preparación:** Inicia repo local nuevo usando solo Preparación desechable del proyecto 01 (prerrequisitos vinculados); comprueba main, identidad ficticia y sin remoto. Git 2.40+ y Bash/Git Bash. Ejecuta comandos individualmente, detente ante fallo inesperado y usa finales LF. Crea notes.txt con exactamente status: draft y LF final; git add notes.txt; git commit -m 'docs: initialize notes'.

**Pistas:**

- Las tres ubicaciones pueden diferir.
- Inspecciona HEAD:notes.txt y :notes.txt.

**Solución:**

- Escribe exactamente status: ready más LF final en notes.txt.
- git add notes.txt
- Escribe exactamente status: experiment más LF final en notes.txt.
- git show HEAD:notes.txt
- git show :notes.txt
- git status --short
- Tras comprobar resultados, cierra shell dedicada y elimina solo directorio temporal verificado mediante gestor de archivos. Nunca uses repo del guía.

**Checks de estado:**

- kind=branch, value=main
- kind=commit-count, value=1
- file=notes.txt, kind=head-content, value=status: draft
- file=notes.txt, kind=index-content, value=status: ready
- file=notes.txt, kind=work-content, value=status: experiment

**Explicación:** No confirmes ni restaures; tree sucio es resultado requerido aquí.

## Conservar edición de trabajo

ID: challenge-unstage

**Dificultad:** fácil

**Prerrequisitos:** [practical-projects/01-my-first-repository](../../practical-projects/01-my-first-repository/README.es.md) · [history-and-recovery/02-restore](../../history-and-recovery/02-restore/README.es.md)

Quita ready del staging sin perderlo del archivo de trabajo; HEAD e index aún deben contener draft.

**Tiempo (min):** 10

**Ejecución:** local_only · Requiere Git real en repo desechable nuevo; sin afirmación de runtime navegador.

**Preparación:** Inicia repo local nuevo usando solo Preparación desechable del proyecto 01 (prerrequisitos vinculados); comprueba main, identidad ficticia y sin remoto. Git 2.40+ y Bash/Git Bash. Ejecuta comandos individualmente, detente ante fallo inesperado y usa finales LF. Crea notes.txt con exactamente status: draft y LF final; git add notes.txt; git commit -m 'docs: initialize notes'.

**Pistas:**

- Solo index debe cambiar.
- Usa restore --staged tras preparar contenido nuevo.

**Solución:**

- Escribe exactamente status: ready más LF final en notes.txt.
- git add notes.txt
- git restore --staged -- notes.txt
- git diff
- Tras comprobar resultados, cierra shell dedicada y elimina solo directorio temporal verificado mediante gestor de archivos. Nunca uses repo del guía.

**Checks de estado:**

- kind=branch, value=main
- kind=commit-count, value=1
- file=notes.txt, kind=head-content, value=status: draft
- file=notes.txt, kind=index-content, value=status: draft
- file=notes.txt, kind=work-content, value=status: ready

**Explicación:** Restore --staged no descarta edición de trabajo con HEAD existente.

## Aislar feature

ID: challenge-feature-branch

**Dificultad:** fácil

**Prerrequisitos:** [practical-projects/01-my-first-repository](../../practical-projects/01-my-first-repository/README.es.md) · [branches/01-create-and-switch](../../branches/01-create-and-switch/README.es.md)

Crea feat/notes desde draft y confirma ready allí, dejando main en primer commit.

**Tiempo (min):** 15

**Ejecución:** local_only · Requiere Git real en repo desechable nuevo; sin afirmación de runtime navegador.

**Preparación:** Inicia repo local nuevo usando solo Preparación desechable del proyecto 01 (prerrequisitos vinculados); comprueba main, identidad ficticia y sin remoto. Git 2.40+ y Bash/Git Bash. Ejecuta comandos individualmente, detente ante fallo inesperado y usa finales LF. Crea notes.txt con exactamente status: draft y LF final; git add notes.txt; git commit -m 'docs: initialize notes'.

**Pistas:**

- Crear y seleccionar rama son conceptos distintos.
- Usa switch -c antes de editar.

**Solución:**

- git switch -c feat/notes
- Escribe exactamente status: ready más LF final en notes.txt.
- git add notes.txt
- git commit -m 'docs: update notes'
- git log --oneline --all
- Tras comprobar resultados, cierra shell dedicada y elimina solo directorio temporal verificado mediante gestor de archivos. Nunca uses repo del guía.

**Checks de estado:**

- kind=branch, value=feat/notes
- kind=commit-count, value=2
- kind=same-ref, left=main, right=HEAD^1
- file=notes.txt, kind=head-content, value=status: ready
- kind=clean

**Explicación:** Ref main debe permanecer en padre de commit feature.

## Integrar por fast-forward

ID: challenge-fast-forward

**Dificultad:** medio

**Prerrequisitos:** [practical-projects/01-my-first-repository](../../practical-projects/01-my-first-repository/README.es.md) · [merge-and-conflicts/02-fast-forward](../../merge-and-conflicts/02-fast-forward/README.es.md)

Integra feat/notes en main sin commit merge adicional; ambas refs deben coincidir.

**Tiempo (min):** 15

**Ejecución:** local_only · Requiere Git real en repo desechable nuevo; sin afirmación de runtime navegador.

**Preparación:** Inicia repo local nuevo usando solo Preparación desechable del proyecto 01 (prerrequisitos vinculados); comprueba main, identidad ficticia y sin remoto. Git 2.40+ y Bash/Git Bash. Ejecuta comandos individualmente, detente ante fallo inesperado y usa finales LF. Crea notes.txt con exactamente status: draft y LF final; git add notes.txt; git commit -m 'docs: initialize notes'.

**Pistas:**

- Evita divergencia de main.
- Comprueba feature descendiente y usa --ff-only.

**Solución:**

- git switch -c feat/notes
- Escribe exactamente status: ready más LF final en notes.txt.
- git add notes.txt
- git commit -m 'docs: update notes'
- git switch main
- git merge --ff-only feat/notes
- Tras comprobar resultados, cierra shell dedicada y elimina solo directorio temporal verificado mediante gestor de archivos. Nunca uses repo del guía.

**Checks de estado:**

- kind=branch, value=main
- kind=commit-count, value=2
- kind=same-ref, left=main, right=feat/notes
- file=notes.txt, kind=head-content, value=status: ready
- kind=clean

**Explicación:** Fast-forward mueve ref actual en vez de crear merge nuevo.

## Resolver conflicto

ID: challenge-merge-resolution

**Dificultad:** medio

**Prerrequisitos:** [practical-projects/01-my-first-repository](../../practical-projects/01-my-first-repository/README.es.md) · [merge-and-conflicts/04-conflict-resolution](../../merge-and-conflicts/04-conflict-resolution/README.es.md)

Diverge main y feat/notes desde draft, resuelve conflicto de misma línea a reviewed y conserva dos padres.

**Tiempo (min):** 20

**Ejecución:** local_only · Requiere Git real en repo desechable nuevo; sin afirmación de runtime navegador.

**Preparación:** Inicia repo local nuevo usando solo Preparación desechable del proyecto 01 (prerrequisitos vinculados); comprueba main, identidad ficticia y sin remoto. Git 2.40+ y Bash/Git Bash. Ejecuta comandos individualmente, detente ante fallo inesperado y usa finales LF. Crea notes.txt con exactamente status: draft y LF final; git add notes.txt; git commit -m 'docs: initialize notes'.

**Pistas:**

- Haz cambios distintos en misma línea.
- Inspecciona git ls-files -u antes de preparar resolución.

**Solución:**

- git switch -c feat/notes
- Escribe exactamente status: ready más LF final en notes.txt.
- git add notes.txt
- git commit -m 'docs: update notes'
- git switch main
- Escribe exactamente status: experiment más LF final en notes.txt.
- git add notes.txt
- git commit -m 'docs: update notes'
- Ejecuta git merge feat/notes; espera conflicto, comprueba MERGE\_HEAD e inspecciona git ls-files -u. Detente ante otro fallo.
- Escribe exactamente status: reviewed más LF final en notes.txt.
- git add notes.txt
- git diff --cached --check
- git commit -m 'merge: resolve notes'
- Tras comprobar resultados, cierra shell dedicada y elimina solo directorio temporal verificado mediante gestor de archivos. Nunca uses repo del guía.

**Checks de estado:**

- kind=branch, value=main
- kind=commit-count, value=4
- kind=parent-count, value=2
- kind=same-ref, left=HEAD^2, right=feat/notes
- file=notes.txt, kind=head-content, value=status: reviewed
- kind=no-unmerged
- kind=clean

**Explicación:** Si abortas merge ordinario activo, conserva ediciones deseadas antes. Merge exitoso tiene dos padres y sin entradas no fusionadas.

## Deshacer sin reescribir

ID: challenge-revert

**Dificultad:** medio

**Prerrequisitos:** [practical-projects/01-my-first-repository](../../practical-projects/01-my-first-repository/README.es.md) · [history-and-recovery/04-revert](../../history-and-recovery/04-revert/README.es.md)

Confirma ready y deshaz contenido con nuevo commit. Conserva dos commits originales.

**Tiempo (min):** 15

**Ejecución:** local_only · Requiere Git real en repo desechable nuevo; sin afirmación de runtime navegador.

**Preparación:** Inicia repo local nuevo usando solo Preparación desechable del proyecto 01 (prerrequisitos vinculados); comprueba main, identidad ficticia y sin remoto. Git 2.40+ y Bash/Git Bash. Ejecuta comandos individualmente, detente ante fallo inesperado y usa finales LF. Crea notes.txt con exactamente status: draft y LF final; git add notes.txt; git commit -m 'docs: initialize notes'.

**Pistas:**

- Historial debe crecer, no reducir.
- Usa revert en último commit ordinario.

**Solución:**

- Escribe exactamente status: ready más LF final en notes.txt.
- git add notes.txt
- git commit -m 'docs: update notes'
- git revert --no-edit HEAD
- Tras comprobar resultados, cierra shell dedicada y elimina solo directorio temporal verificado mediante gestor de archivos. Nunca uses repo del guía.

**Checks de estado:**

- kind=branch, value=main
- kind=commit-count, value=3
- kind=parent-count, value=1
- file=notes.txt, kind=head-content, value=status: draft
- file=notes.txt, kind=ref-content, ref=HEAD^1, value=status: ready
- file=notes.txt, kind=ref-content, ref=HEAD\~2, value=status: draft
- kind=same-tree, left=HEAD, right=HEAD\~2
- kind=clean

**Explicación:** Revert crea cambio inverso nuevo. No es reset.

## Conservar trabajo incompleto

ID: challenge-stash

**Dificultad:** medio

**Prerrequisitos:** [practical-projects/01-my-first-repository](../../practical-projects/01-my-first-repository/README.es.md) · [history-and-recovery/06-stash](../../history-and-recovery/06-stash/README.es.md)

Guarda edición ready y review.txt no rastreado en stash, comprueba estado limpio y aplica stash. Deja ambos restaurados y HEAD draft.

**Tiempo (min):** 15

**Ejecución:** local_only · Requiere Git real en repo desechable nuevo; sin afirmación de runtime navegador.

**Preparación:** Inicia repo local nuevo usando solo Preparación desechable del proyecto 01 (prerrequisitos vinculados); comprueba main, identidad ficticia y sin remoto. Git 2.40+ y Bash/Git Bash. Ejecuta comandos individualmente, detente ante fallo inesperado y usa finales LF. Crea notes.txt con exactamente status: draft y LF final; git add notes.txt; git commit -m 'docs: initialize notes'.

**Pistas:**

- Incluye no rastreados explícitamente.
- Usa apply en vez de pop para conservar stash para inspección.

**Solución:**

- Escribe exactamente status: ready más LF final en notes.txt.
- Crea review.txt con exactamente review: done más LF.
- git stash push -u -m 'practice notes'
- git status --porcelain
- git stash apply
- git stash list
- Tras comprobar resultados, cierra shell dedicada y elimina solo directorio temporal verificado mediante gestor de archivos. Nunca uses repo del guía.

**Checks de estado:**

- kind=branch, value=main
- kind=commit-count, value=1
- file=notes.txt, kind=head-content, value=status: draft
- file=notes.txt, kind=index-content, value=status: draft
- file=notes.txt, kind=work-content, value=status: ready
- file=review.txt, kind=work-content, value=review: done
- file=review.txt, kind=untracked

**Explicación:** Check final no prueba operación temporal; registra estado limpio intermedio y stash list como evidencia manual.

## Recuperar punta desplazada

ID: challenge-recover-tip

**Dificultad:** difícil

**Prerrequisitos:** [practical-projects/01-my-first-repository](../../practical-projects/01-my-first-repository/README.es.md) · [history-and-recovery/05-reflog](../../history-and-recovery/05-reflog/README.es.md)

Simula pérdida de punta confirmada en repo desechable. Recupera con recovery/notes manteniendo main draft.

**Tiempo (min):** 20

**Ejecución:** local_only · Requiere Git real en repo desechable nuevo; sin afirmación de runtime navegador.

**Preparación:** Inicia repo local nuevo usando solo Preparación desechable del proyecto 01 (prerrequisitos vinculados); comprueba main, identidad ficticia y sin remoto. Git 2.40+ y Bash/Git Bash. Ejecuta comandos individualmente, detente ante fallo inesperado y usa finales LF. Crea notes.txt con exactamente status: draft y LF final; git add notes.txt; git commit -m 'docs: initialize notes'.

**Pistas:**

- Guarda ID de punta antes de demostración.
- Comprueba candidato reflog y crea ref nueva, no otro reset.

**Solución:**

- Escribe exactamente status: recovered más LF final en notes.txt.
- git add notes.txt
- git commit -m 'docs: update notes'
- git rev-parse HEAD; registra ID fuera del repo.
- Comprueba git status --porcelain vacío, después solo en repo desechable ejecuta git reset --hard HEAD\~1.
- git reflog show HEAD
- Inspecciona git show HEAD@{1}; comprueba ID guardado y luego git branch recovery/notes 'HEAD@{1}'.
- Tras comprobar resultados, cierra shell dedicada y elimina solo directorio temporal verificado mediante gestor de archivos. Nunca uses repo del guía.

**Checks de estado:**

- kind=branch, value=main
- kind=commit-count, value=1
- file=notes.txt, kind=head-content, value=status: draft
- kind=ancestor, newer=recovery/notes, older=main
- file=notes.txt, kind=ref-content, ref=recovery/notes, value=status: recovered
- kind=different-ref, left=main, right=recovery/notes
- kind=clean

**Explicación:** Nunca supongas posiciones reflog ni recuperación garantizada; comprueba IDs y evita comandos destructivos en trabajo valioso.

## Integrar tree revisado

ID: challenge-squash

**Dificultad:** difícil

**Prerrequisitos:** [practical-projects/01-my-first-repository](../../practical-projects/01-my-first-repository/README.es.md) · [merge-and-conflicts/05-squash-merge](../../merge-and-conflicts/05-squash-merge/README.es.md)

Crea dos commits feature y haz squash en main intacta. Main debe tener exactamente dos commits y mismo tree de punta feature.

**Tiempo (min):** 20

**Ejecución:** local_only · Requiere Git real en repo desechable nuevo; sin afirmación de runtime navegador.

**Preparación:** Inicia repo local nuevo usando solo Preparación desechable del proyecto 01 (prerrequisitos vinculados); comprueba main, identidad ficticia y sin remoto. Git 2.40+ y Bash/Git Bash. Ejecuta comandos individualmente, detente ante fallo inesperado y usa finales LF. Crea notes.txt con exactamente status: draft y LF final; git add notes.txt; git commit -m 'docs: initialize notes'.

**Pistas:**

- Commit squash tiene un padre.
- Compara IDs de tree, no commits, tras integrar.

**Solución:**

- git switch -c feat/notes
- Escribe exactamente status: ready más LF final en notes.txt.
- git add notes.txt
- git commit -m 'docs: update notes'
- Crea review.txt con exactamente review: done más LF; git add review.txt; git commit -m 'docs: record review'.
- git diff main...HEAD
- git switch main
- git merge --squash feat/notes
- git diff --cached --check
- git commit -m 'feat: deliver reviewed notes'
- Tras comprobar resultados, cierra shell dedicada y elimina solo directorio temporal verificado mediante gestor de archivos. Nunca uses repo del guía.

**Checks de estado:**

- kind=branch, value=main
- kind=commit-count, value=2
- kind=parent-count, value=1
- file=notes.txt, kind=head-content, value=status: ready
- file=review.txt, kind=head-content, value=review: done
- kind=same-tree, left=main, right=feat/notes
- kind=different-ref, left=main, right=feat/notes
- kind=ref-commit-count, ref=feat/notes, value=3
- kind=same-ref, left=HEAD^1, right=feat/notes\~2
- file=notes.txt, kind=ref-content, ref=HEAD^1, value=status: draft
- file=notes.txt, kind=ref-content, ref=feat/notes^1, value=status: ready
- kind=clean

**Explicación:** No supongas merge --abort para squash con conflicto. Detente, conserva ediciones e inspecciona; recrea fixture desechable si hace falta.

## Fijar lanzamiento

ID: challenge-release-tag

**Dificultad:** difícil

**Prerrequisitos:** [practical-projects/01-my-first-repository](../../practical-projects/01-my-first-repository/README.es.md) · [professional-workflows/12-release-management](../../professional-workflows/12-release-management/README.es.md)

Etiqueta revisión ready con v1.0.0 anotada, luego avanza main con future.txt. Etiqueta debe resolver a commit anterior.

**Tiempo (min):** 15

**Ejecución:** local_only · Requiere Git real en repo desechable nuevo; sin afirmación de runtime navegador.

**Preparación:** Inicia repo local nuevo usando solo Preparación desechable del proyecto 01 (prerrequisitos vinculados); comprueba main, identidad ficticia y sin remoto. Git 2.40+ y Bash/Git Bash. Ejecuta comandos individualmente, detente ante fallo inesperado y usa finales LF. Crea notes.txt con exactamente status: draft y LF final; git add notes.txt; git commit -m 'docs: initialize notes'.

**Pistas:**

- Etiqueta debe identificar revisión exacta.
- Usa tag -a y resuelve a commit.

**Solución:**

- Escribe exactamente status: ready más LF final en notes.txt.
- git add notes.txt
- git commit -m 'docs: update notes'
- git tag -a v1.0.0 -m 'Ready notes release'
- Crea future.txt con exactamente future work más LF; git add future.txt; git commit -m 'docs: future work'.
- git rev-parse 'v1.0.0^{commit}'
- Tras comprobar resultados, cierra shell dedicada y elimina solo directorio temporal verificado mediante gestor de archivos. Nunca uses repo del guía.

**Checks de estado:**

- kind=branch, value=main
- kind=commit-count, value=3
- kind=tag-type, tag=v1.0.0, value=tag
- kind=same-ref, left=v1.0.0, right=HEAD^1
- file=notes.txt, kind=ref-content, ref=v1.0.0, value=status: ready
- file=future.txt, kind=head-content, value=future work
- kind=clean

**Explicación:** Etiqueta Git anotada no es lanzamiento alojado; no reemplaces etiquetas publicadas a la ligera.

## Transferir un cambio

ID: challenge-cherry-pick

**Dificultad:** difícil

**Prerrequisitos:** [practical-projects/01-my-first-repository](../../practical-projects/01-my-first-repository/README.es.md) · [history-and-recovery/07-cherry-pick](../../history-and-recovery/07-cherry-pick/README.es.md)

Confirma review.txt en feat/notes, avanza main independientemente a ready y aplica cherry-pick solo del commit review en main. Conserva feature distinta.

**Tiempo (min):** 20

**Ejecución:** local_only · Requiere Git real en repo desechable nuevo; sin afirmación de runtime navegador.

**Preparación:** Inicia repo local nuevo usando solo Preparación desechable del proyecto 01 (prerrequisitos vinculados); comprueba main, identidad ficticia y sin remoto. Git 2.40+ y Bash/Git Bash. Ejecuta comandos individualmente, detente ante fallo inesperado y usa finales LF. Crea notes.txt con exactamente status: draft y LF final; git add notes.txt; git commit -m 'docs: initialize notes'.

**Pistas:**

- Usa archivo separado para evitar conflicto fabricado.
- Comprueba conteo de padres y contenido final; IDs no deben coincidir necesariamente.

**Solución:**

- git switch -c feat/notes
- Crea review.txt con exactamente review: done más LF; git add review.txt; git commit -m 'docs: record review'.
- git switch main
- Escribe exactamente status: ready más LF final en notes.txt.
- git add notes.txt
- git commit -m 'docs: update notes'
- git cherry-pick feat/notes
- Tras comprobar resultados, cierra shell dedicada y elimina solo directorio temporal verificado mediante gestor de archivos. Nunca uses repo del guía.

**Checks de estado:**

- kind=branch, value=main
- kind=commit-count, value=3
- kind=parent-count, value=1
- file=notes.txt, kind=head-content, value=status: ready
- file=review.txt, kind=head-content, value=review: done
- file=notes.txt, kind=ref-content, ref=feat/notes, value=status: draft
- kind=different-ref, left=main, right=feat/notes
- kind=clean

**Explicación:** Ante conflicto inesperado cherry-pick, inspecciona y conserva trabajo antes de abortar. Contenido aplicado no prueba historial idéntico.

---

<!-- navigation-footer -->
[Anterior](../01-quizzes/README.es.md) · [Índice](../README.es.md) · [Siguiente](../03-interviews/README.es.md)
<!-- /navigation-footer -->
