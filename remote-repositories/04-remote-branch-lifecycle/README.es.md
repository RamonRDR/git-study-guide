# Ciclo de vida de ramas remotas y prune

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../03-pull-push-and-divergence/README.es.md) · [Índice](../README.es.md) · [Siguiente](../05-secure-authentication/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 30 min

**Requisitos previos:** [Pull, push e historiales divergentes](../03-pull-push-and-divergence/README.es.md)

**Objetivo:** Publicar, seguir, integrar y eliminar una rama remota desechable conservando trabajo.

## Qué y por qué

`git push -u origin BRANCH` publica y configura upstream si push tiene éxito o ya está actualizado. `git switch --track origin/BRANCH` crea rama local que sigue la ref remota de seguimiento. `git push --delete origin BRANCH` elimina una ref remota, no necesariamente los objetos; compañeros pueden mantener refs obsoletas hasta fetch --prune. Prune usa el refspec de fetch y no elimina ramas locales comunes con el mapeo estándar de clone. Refspecs no estándar pueden eliminar otras refs, incluso tags; inspecciona configuración.

## Práctica

Continúa capítulo 03 con clones limpios y sincronizados en el padre registrado. Repite comprobaciones del capítulo 02 para cada actor antes de cambios. Tras cambiar Alice a feat/summary, crea alice/summary.txt con `summary ready` y salto final; inspecciona diff staged y ambas identidades antes del commit. Ejecuta en orden, pausando en switch para crear el archivo.
```text
git -C alice switch -c feat/summary
git -C alice add -- summary.txt
git -C alice diff --cached
git -C alice commit -m "docs: add summary"
git -C alice push -u origin feat/summary
git -C alice branch -vv
git -C bob fetch origin
git -C bob switch --track origin/feat/summary
git -C bob branch -vv
git -C bob switch main
git -C alice switch main
git -C alice merge --ff-only feat/summary
git -C alice push origin main
git -C bob pull --ff-only origin main
```
Esperado: rama local de Bob sigue origin/feat/summary; main contiene commit summary en ambos clones. Para eliminar, confirma acuerdo de todos los compañeros (Alice y Bob en este lab), ausencia de trabajo adicional en feature y que feature remota sea ancestro de main remota. Ejecuta por separado los cuatro primeros comandos de inspección; ascendencia debe devolver 0 y ambas refs de ls-remote deben coincidir con refs obtenidas. Solo entonces elimina feat/summary, nunca main. Ningún actor concurrente debe cambiar refs durante el ejercicio; en equipos reales vuelve a comprobar y usa protección de plataforma y flujo acordado.
```text
git -C alice fetch origin
git -C alice merge-base --is-ancestor origin/feat/summary origin/main
git -C alice ls-remote --heads origin refs/heads/main refs/heads/feat/summary
git -C alice rev-parse origin/main origin/feat/summary
```

Detente aquí si la ascendencia y ambos IDs no coinciden con las comprobaciones anteriores. Con origin local verificado y solo la rama desechable acordada, ejecuta:

```text
git -C alice push --delete origin feat/summary
git -C bob ls-remote --heads origin refs/heads/feat/summary
git -C bob branch -r
git -C bob fetch --prune origin
git -C bob branch -r
git -C bob branch -vv
git -C bob branch -d feat/summary
git -C alice branch -d feat/summary
git -C alice rev-parse main
git -C bob rev-parse main
git -C origin.git rev-parse refs/heads/main
git -C bob show HEAD:summary.txt
git -C bob status --short
git -C alice status --short
```
Esperado: rama remota ausente tras eliminación; caché origin/feat/summary de Bob puede existir antes de prune y desaparece después. La rama local permanece hasta -d; puntas main locales iguales a origin main y summary ready conservado. Eliminación local puede rechazar si no integrada; detente en vez de forzar. Uso profesional: limpiar ramas integradas tras revisión, no antes. Confirma que no quede trabajo necesario. Cierra editores y sesión dedicada; elimina solo el padre temporal registrado mediante gestor de archivos, nunca guía, home o repo de trabajo.

## Errores comunes y seguridad

Eliminar remoto puede afectar compañeros o quitar la última ref nombrada de trabajo. Ascendencia vale para este lab fast-forward/merge; squash puede requerir evidencia de contenido y revisión aparte. Prune no elimina en servidor. Recuperación depende de commit disponible y autorización para republicar; no garantizada.

## Ejercicio y autoevaluación

Tras eliminar feature remota, ¿por qué Bob aún la ve? Pista: ref en caché. Respuesta: fetch --prune elimina ref de seguimiento obsoleta, no rama local de Bob. Aprueba si feature remota y caché desaparecen tras prune, main conserva summary y estado limpio.

## Referencia rápida

- `git push -u origin feat/summary`
- `git switch --track origin/feat/summary`
- `git push --delete origin feat/summary`
- `git fetch --prune origin`

## Fuentes oficiales

- [Git: git-push](https://git-scm.com/docs/git-push)
- [Git: git-fetch](https://git-scm.com/docs/git-fetch)
- [Git: git-switch](https://git-scm.com/docs/git-switch)
- [Git: git-branch](https://git-scm.com/docs/git-branch)
- [Git: git-ls-remote](https://git-scm.com/docs/git-ls-remote)
- [Git: git-merge-base](https://git-scm.com/docs/git-merge-base)
