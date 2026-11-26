# Detached HEAD y preservación del trabajo

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../04-safe-local-deletion/README.es.md) · [Índice](../README.es.md) · [Siguiente módulo](../../merge-and-conflicts/README.es.md)
<!-- /navigation -->

**Nivel:** principiante · **Tiempo estimado:** 30 min

**Requisitos previos:** [Borrado seguro de ramas locales](../04-safe-local-deletion/README.es.md)

**Objetivo:** Inspeccionar commit anterior y dar nombre de rama persistente a commit detached.

## Qué es y por qué

Normalmente HEAD es ref simbólica a rama. Detached HEAD apunta directo a commit. Permite inspeccionar snapshot histórico o probar versión sin mover rama. Commits nuevos en detached avanzan HEAD, no rama nombrada. Antes de salir de commit detached que desea guardar, cree rama allí. Si no, commit puede quedar inalcanzable y eliminarse; recuperación por reflog no garantizada. Diagrama textual: conectado HEAD -> main -> C1; detached HEAD -> C1, main -> C1; tras commit detached HEAD -> C4 -> C1, main sigue C1.

## Práctica

Continúe lab en main con status limpio. Compruebe raíz, luego entre detached HEAD en main:

```text
git rev-parse --show-toplevel
git status --short
git switch --detach main
git branch --show-current
git status
git rev-parse HEAD main
```

Esperado: branch --show-current vacío; status menciona detached HEAD; IDs iguales. Cree experiment.txt con experiment y salto final, prepare y compruebe:

```text
git add -- experiment.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Solo si identidades ficticias y diff esperado:

```text
git commit -m "docs: record experiment"
git rev-parse HEAD main
git log -1 --oneline
```

HEAD ahora difiere de main. ANTES de salir, conserve commit creando y seleccionando rama nombrada en HEAD actual:

```text
git switch -c experiment/saved
git branch --show-current
git rev-parse HEAD experiment/saved
git status --short
git switch main
git ls-files
git show experiment/saved:experiment.txt
git branch --list
```

Esperado: IDs guardados iguales; main no contiene experiment.txt; git show lee experiment de rama guardada. Sin integración. Para inspeccionar commit histórico sin crear trabajo, elija ID o ref local existente con status limpio y vuelva con git switch main. Si ya salió de commit detached y conoce ID, compruebe git show ID y cree rama allí mientras exista; recuperación detallada después.

## Errores comunes y seguridad

No salga hasta que trabajo detached deseado tenga ref nombrada. No confíe en recuperación automática ni use fuerza. Conserve lab solo si necesita; si no cierre editor y shell dedicado y borre solo carpeta padre temporal exacta anotada con gestor, según módulo 00.

## Ejercicio y autoevaluación

Explique por qué crear rama conservó commit detached sin merge. Respuesta: nueva ref nombra commit existente; main sin cambio. Apruebe si contenido guardado legible desde main y status limpio. Uso profesional: investigar release antigua sin mover historial compartido.

## Referencia rápida

`git switch --detach REF`: inspeccionar sin rama; `git switch -c NAME`: nombrar commit actual y conectar HEAD; `git branch --show-current`: vacío en detached.

## Fuentes oficiales

- [Git: git-switch](https://git-scm.com/docs/git-switch)
- [Git: git-checkout](https://git-scm.com/docs/git-checkout)
- [Git: git-branch](https://git-scm.com/docs/git-branch)
- [Git: git-symbolic-ref](https://git-scm.com/docs/git-symbolic-ref)

---

<!-- navigation-footer -->
[Anterior](../04-safe-local-deletion/README.es.md) · [Índice](../README.es.md) · [Siguiente módulo](../../merge-and-conflicts/README.es.md)
<!-- /navigation-footer -->
