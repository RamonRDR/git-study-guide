# Puntos de partida y comparación de ramas

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../01-create-and-switch/README.es.md) · [Índice](../README.es.md) · [Siguiente](../03-switch-safety-and-naming/README.es.md)
<!-- /navigation -->

**Nivel:** principiante · **Tiempo estimado:** 30 min

**Requisitos previos:** [Crear y cambiar ramas locales](../01-create-and-switch/README.es.md)

**Objetivo:** Elegir commit inicial y comparar historiales y snapshots.

## Qué es y por qué

Ramas pueden partir de rama local o ID de commit, no solo HEAD actual. HEAD~1 es primer padre de HEAD. Hay divergencia cuando ambos lados tienen commits ausentes en el otro. `git log A..B` lista commits alcanzables desde B pero no A; invertir nombres cambia conjunto. `git diff A B` compara árboles finales, no cantidad de commits. `git diff A..B` también compara extremos; `git diff A...B` compara merge base (mejor ancestro común) con B. Merge y rebase en próximo módulo; estos comandos solo inspeccionan.

## Práctica

Continúe en feat/note limpia (C2). Cree rama del padre C1 y seleccione nueva rama docs desde main. Compruebe raíz y status limpio primero:

```text
git branch archive/base HEAD~1
git rev-parse archive/base main
git switch -c docs/overview main
git branch --show-current
git status --short
```

Esperado: archive/base y main mismo ID, docs/overview actual en C1. Cree overview.txt con overview y salto final. Prepare y compruebe:

```text
git add -- overview.txt
git diff --cached
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Solo con diff esperado e identidades ficticias:

```text
git commit -m "docs: add overview"
git log --all --graph --oneline --decorate
git log --oneline feat/note..docs/overview
git log --oneline docs/overview..feat/note
git diff --name-status feat/note docs/overview
git diff --name-status feat/note...docs/overview
git merge-base feat/note docs/overview
git rev-parse main
```

Esperado: un commit distinto por rango log. Diff de extremos muestra note.txt modificado y overview.txt añadido; diff tres puntos solo overview.txt añadido. IDs finales merge-base/main iguales. Diagrama: feat/note -> C2 -> C1; docs/overview -> C3 -> C1; main y archive/base -> C1. Ningún historial cambia al comparar.

## Errores comunes y seguridad

No suponga que rangos log y diff significan lo mismo. Nombre de rama puede moverse; compruebe rev-parse antes de elegir base. Si IDs difieren de esperado, vea gráfico en vez de mover refs a la fuerza.

## Ejercicio y autoevaluación

¿Qué comparación aísla commits de docs/overview ausentes en feat/note? Respuesta: git log feat/note..docs/overview. ¿Qué diff muestra cambios desde ancestro común? git diff feat/note...docs/overview. Apruebe si salidas coinciden con gráfico. Uso profesional: comprobar alcance de review.

## Referencia rápida

`git branch NAME START`: crear en base; `git log A..B`: commits exclusivos de B respecto a A; `git diff A B`: árboles; `git diff A...B`: base a B.

## Fuentes oficiales

- [Git: git-branch](https://git-scm.com/docs/git-branch)
- [Git: git-log](https://git-scm.com/docs/git-log)
- [Git: git-diff](https://git-scm.com/docs/git-diff)
- [Git: git-merge-base](https://git-scm.com/docs/git-merge-base)
- [Git: gitrevisions](https://git-scm.com/docs/gitrevisions)
