# Dos desarrolladores, un proyecto

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../01-my-first-repository/README.es.md) · [Índice](../README.es.md) · [Siguiente](../03-merge-conflict-laboratory/README.es.md)
<!-- /navigation -->

**Nivel:** principiante · **Tiempo estimado:** 60 min

**Prerrequisitos:** [remote-repositories/02-fetch-and-tracking](../../remote-repositories/02-fetch-and-tracking/README.es.md) · Git 2.40+ · Bash/Git Bash

**Objetivo:** Crea base compartida, clona como Alice y Bob, publica cambio de Alice, haz fetch en Bob sin cambiar su checkout, luego integra y publica archivo separado de Bob. Comprueba convergencia.

## Escenario

Alice y Bob mantienen notas ficticias mediante origin bare local. Alice publica un cambio mientras Bob trabaja independientemente.

## Preparación desechable

Usa solo la sección Preparación desechable de [Mi primer repositorio](../01-my-first-repository/README.es.md). Abre shell Bash/Git Bash dedicada nueva; comprueba raíz impresa, identidades ficticias y ausencia de remotos antes de seguir. No ejecutes desafío 01. Git 2.40+. Ejecuta un comando a la vez, detente ante fallo inesperado y nunca ejecutes en el guía.

## Desafío

Crea base compartida, clona como Alice y Bob, publica cambio de Alice, haz fetch en Bob sin cambiar su checkout, luego integra y publica archivo separado de Bob. Comprueba convergencia. Intenta antes de leer la solución.

## Pistas progresivas

Usa repositorio bare como origin. Fetch actualiza referencias de seguimiento, no rama seleccionada. Integra en main limpia antes de crear commit de Bob.

## Solución de referencia

Crea revisión inicial y publica localmente. Clona dos veces; configura cada clon antes de confirmar commits.

```bash
printf '%s\n' 'shared: draft' > notes.txt
git add notes.txt
git commit -m 'docs: initialize shared notes'
git init --bare -b main "$sandbox/origin.git"
git remote add origin "$sandbox/origin.git"
git push -u origin main
git clone "$sandbox/origin.git" "$sandbox/alice"
git clone "$sandbox/origin.git" "$sandbox/bob"
for who in alice bob; do
  git -C "$sandbox/$who" config user.name 'Study Guide Example'
  git -C "$sandbox/$who" config user.email learner@example.invalid
  git -C "$sandbox/$who" config commit.gpgsign false
  git -C "$sandbox/$who" config core.autocrlf false
  git -C "$sandbox/$who" config core.hooksPath "$sandbox/no-hooks"
done
```

Publica actualización de Alice; Bob registra HEAD anterior y hace fetch. Inspecciona referencias distintas antes de integrar.

```bash
printf '%s\n' 'shared: ready' > "$sandbox/alice/notes.txt"
git -C "$sandbox/alice" add notes.txt
git -C "$sandbox/alice" commit -m 'docs: prepare shared notes'
git -C "$sandbox/alice" push origin main
cd "$sandbox/bob"
before=$(git rev-parse HEAD)
git fetch origin
test "$(git rev-parse HEAD)" = "$before"
test "$(git rev-parse origin/main)" != "$before"
git merge --ff-only origin/main
printf '%s\n' 'review: done' > review.txt
git add review.txt
git commit -m 'docs: record review'
git push origin main
git -C "$sandbox/alice" pull --ff-only origin main
test "$(git -C "$sandbox/alice" rev-parse HEAD)" = "$(git rev-parse HEAD)"
git status --porcelain
```

## Criterios de éxito

HEAD de Bob queda sin cambios tras fetch; tras integrar ambos clones y main bare tienen misma punta, con notas ready y review.txt. Ambos clones limpios. Explica fetch frente a pull.

Prueba fija de mantenimiento (no código de estudiante): `tests/test_git_practical_projects.py::test_two_developers_sync`.

## Recuperación y limpieza

Ante rechazo, inspecciona referencias obtenidas y divergencia. Nunca fuerces push para superarlo. Comprueba tres repositorios locales antes de eliminar sandbox. Cierra la shell dedicada y elimina solo el sandbox impreso verificado mediante gestor de archivos. Conserva antes trabajo deseado.

## Fuentes oficiales

- <https://git-scm.com/docs/git-clone>
- <https://git-scm.com/docs/git-fetch>
- <https://git-scm.com/docs/git-push>
- <https://git-scm.com/docs/git-merge>

---

<!-- navigation-footer -->
[Anterior](../01-my-first-repository/README.es.md) · [Índice](../README.es.md) · [Siguiente](../03-merge-conflict-laboratory/README.es.md)
<!-- /navigation-footer -->
