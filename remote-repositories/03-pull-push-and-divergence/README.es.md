# Pull, push e historiales divergentes

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../02-fetch-and-tracking/README.es.md) · [Índice](../README.es.md) · [Siguiente](../04-remote-branch-lifecycle/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 35 min

**Requisitos previos:** [Fetch, referencias y seguimiento upstream](../02-fetch-and-tracking/README.es.md)

**Objetivo:** Reproducir y resolver de forma segura el rechazo non-fast-forward.

## Qué y por qué

Pull hace fetch y luego integra en la rama actual. `git pull --ff-only origin main` rechaza historial divergente, aunque fetch todavía pueda actualizar refs de seguimiento. `git pull --no-rebase origin main` elige merge (puede crear commit de dos padres); `git pull --rebase origin main` reaplica commits locales sobre la base obtenida, normalmente cambiando IDs. Los valores por defecto varían por versión/configuración; elige explícitamente. Push normalmente rechaza una actualización que descartaría ascendencia remota. El rechazo protege trabajo compartido, no debe eludirse.

## Práctica

Continúa con clones sincronizados en main. Repite todas las comprobaciones de seguridad e identidad del capítulo 02 para cada actor antes de operaciones; inspecciona cada diff staged antes del commit. Crea alice/plan.txt con `shared plan` y bob/bob.txt con `bob update`, ambos con salto final. Publica Alice, luego haz commit de Bob e intenta su push.
```text
git -C alice add -- plan.txt
git -C alice diff --cached
git -C alice commit -m "docs: add plan"
git -C alice push origin main
git -C bob add -- bob.txt
git -C bob diff --cached
git -C bob commit -m "docs: add Bob note"
git -C bob push origin main
```
Esperado: el ÚLTIMO push falla (non-fast-forward, a veces descrito como fetch first). Detente ante cualquier fallo anterior. Verifica origin main aún igual a la punta de Alice y commit de Bob conservado. Entonces:
```text
git -C bob fetch origin
git -C bob rev-list --left-right --count main...origin/main
git -C bob log --all --graph --oneline --decorate
git -C bob diff main origin/main
git -C bob pull --ff-only origin main
```
Esperado: conteo 1 1; último pull rechaza. Diagrama: C2 -> A3 (origin/main); C2 -> B3 (main de Bob). Ambos tienen commits exclusivos. Comprueba HEAD de Bob aún B3 y estado limpio. Haz merge explícito de la ref ya inspeccionada; no se espera conflicto porque los archivos difieren.
```text
git -C bob merge --no-edit origin/main
git -C bob show HEAD:plan.txt
git -C bob show HEAD:bob.txt
git -C bob status --short
git -C bob push origin main
git -C alice pull --ff-only origin main
git -C alice rev-parse HEAD origin/main
git -C bob rev-parse HEAD origin/main
git -C origin.git rev-parse refs/heads/main
```
Esperado: commit de merge M tiene padres B3 y A3; ambos archivos sobreviven, puntas main iguales a M, estado limpio. En equipo, elige merge o rebase según política. Solo para commit local no publicado, rebase tras fetch y ref de respaldo es alternativa; consulta módulo 05. No ejecutes ambas estrategias en este laboratorio.

## Errores comunes y seguridad

No hagas force push ni reset para silenciar el rechazo. Ante conflicto inesperado de merge, inspecciona status y usa merge --abort o resuelve como en módulo 05. Si eliges rebase en otro contexto, usa rebase --abort/--continue. Un push completado no se revoca con abort; coordina recuperación con compañeros.

## Ejercicio y autoevaluación

¿Un pull ff-only rechazado implica que nada cambió? Pista: fase fetch. Respuesta: main local no cambia, refs de seguimiento pueden actualizarse. Aprueba si ambos commits exclusivos son ancestros de main final y ambos archivos existen.

## Referencia rápida

- `git pull --ff-only`
- `git pull --no-rebase`
- `git pull --rebase`
- `git push origin main`

## Fuentes oficiales

- [Git: git-pull](https://git-scm.com/docs/git-pull)
- [Git: git-push](https://git-scm.com/docs/git-push)
- [Git: git-merge](https://git-scm.com/docs/git-merge)
- [Git: git-rebase](https://git-scm.com/docs/git-rebase)
