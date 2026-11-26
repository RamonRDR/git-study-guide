# Fetch, referencias y seguimiento upstream

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../01-remote-concepts/README.es.md) · [Índice](../README.es.md) · [Siguiente](../03-pull-push-and-divergence/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 30 min

**Requisitos previos:** [Remotos, repositorios bare y clones](../01-remote-concepts/README.es.md)

**Objetivo:** Observar una actualización remota antes y después de fetch sin cambiar el árbol de Bob.

## Qué y por qué

HEAD normalmente apunta a refs/heads/main. El remoto tiene su propia refs/heads/main; refs/remotes/origin/main de Bob es un registro local de la última punta remota conocida. Fetch descarga objetos y actualiza refs configuradas (y FETCH_HEAD), no la rama en checkout, index ni archivos de trabajo en este clon normal. Push solicita actualización remota y puede actualizar la ref de seguimiento del clon que envía. El upstream configurado permite que status y branch -vv comparen historial local con la ref de seguimiento, no con el estado en vivo del servidor. Ahead/behind cuentan commits exclusivos de cada lado.

## Práctica

Continúa capítulo 01 en el padre registrado. Antes de cada cambio, comprueba raíz del clon objetivo, rama, estado limpio, URL de push/fetch e identidades ficticias de autor y committer; el ejemplo es para Alice, sustituye alice por bob al actuar como Bob. Ambas identidades deben empezar con `Study Guide Example <learner@example.invalid>`. Antes de cada commit repite ambas comprobaciones e inspecciona el diff staged. Ejecuta individualmente y detente ante estado inesperado.
```text
git -C alice rev-parse --show-toplevel
git -C alice branch --show-current
git -C alice status --short
git -C alice var GIT_AUTHOR_IDENT
git -C alice var GIT_COMMITTER_IDENT
git -C alice remote get-url origin
git -C alice remote get-url --push origin
```
Crea alice/alice.txt en editor de texto plano con línea `alice update` y salto final. Añade al index e inspecciona; haz commit solo si es correcto, luego envía únicamente al origin local verificado.
```text
git -C alice add -- alice.txt
git -C alice diff --cached
git -C alice commit -m "docs: add Alice note"
git -C alice push origin main
git -C origin.git rev-parse refs/heads/main
git -C bob rev-parse HEAD refs/remotes/origin/main
```

Registra estos dos IDs antes de continuar. Confirma Bob en main limpia del clon verificado; luego haz fetch:

```text
git -C bob fetch origin
git -C bob rev-parse HEAD refs/remotes/origin/main
git -C bob rev-list --left-right --count main...origin/main
git -C bob log --oneline main..origin/main
git -C bob diff main origin/main
git -C bob branch -vv
git -C bob config --get remote.origin.fetch
```
Antes del fetch de Bob, origin main está en C2, main y origin/main de Bob siguen en C1. Tras fetch, origin/main = C2 y HEAD/main = C1; conteo 0 1, alice.txt ausente del árbol de Bob. El refspec estándar `+refs/heads/*:refs/remotes/origin/*` mapea refs de ramas remotas a refs locales de seguimiento; + permite actualizarlas incluso ante cambio remoto no fast-forward. No autoriza force push. `main..origin/main` enumera commits alcanzables desde origin/main pero no main. Compara snapshots con diff antes de integrar. Comprueba Bob limpio y en main, entonces:
```text
git -C bob merge --ff-only origin/main
git -C bob rev-parse HEAD origin/main
git -C bob show HEAD:alice.txt
git -C bob status --short
```
Esperado: puntas iguales, alice update en Bob, estado limpio. Uso profesional: fetch e inspección antes de integrar trabajo de compañeros.

## Errores comunes y seguridad

No trates origin/main como dato en vivo ni lo edites directamente. Fetch no resuelve conflictos. Si fast-forward rechaza, inspecciona divergencia sin forzar.

## Ejercicio y autoevaluación

Tras push de Alice y antes del fetch de Bob, ¿puede Bob estar atrasado aunque status diga actualizado? Pista: seguimiento local. Respuesta: sí; su ref está obsoleta. Aprueba si fetch cambia solo la punta de seguimiento y merge posterior avanza main.

## Referencia rápida

- `git fetch origin`
- `git branch -vv`
- `git rev-list --left-right --count main...origin/main`
- `git merge --ff-only origin/main`

## Fuentes oficiales

- [Git: git-fetch](https://git-scm.com/docs/git-fetch)
- [Git: git-branch](https://git-scm.com/docs/git-branch)
- [Git: git-rev-list](https://git-scm.com/docs/git-rev-list)
- [Git: git-merge](https://git-scm.com/docs/git-merge)

---

<!-- navigation-footer -->
[Anterior](../01-remote-concepts/README.es.md) · [Índice](../README.es.md) · [Siguiente](../03-pull-push-and-divergence/README.es.md)
<!-- /navigation-footer -->
