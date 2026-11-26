# Comparar e inspeccionar historial

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../02-status-add-commit/README.es.md) · [Índice](../README.es.md) · [Siguiente](../04-move-and-remove/README.es.md)
<!-- /navigation -->

**Nivel:** principiante · **Tiempo estimado:** 35 min

**Requisitos previos:** [Inspeccionar, preparar y registrar](../02-status-add-commit/README.es.md)

**Objetivo:** Elegir base correcta de diff e inspeccionar historial registrado.

## Qué es y por qué

git diff compara working tree con index para rastreados; --cached (también --staged) compara index con HEAD (o árbol vacío antes del primer commit); git diff HEAD compara contenido rastreado de trabajo con HEAD. No rastreados no salen en diff normal. Diff usa - para líneas quitadas y + añadidas; contexto muestra posición. git log lista commits con --oneline compacto y -n para limitar; git show muestra objeto como commit con parche o ruta en commit.

## Práctica

Continúe capítulo 02. Edite note.txt a second y guarde con salto final, luego prepare:

```text
git add -- note.txt
```

Ahora edite note.txt a third y guarde sin preparar. Compruebe:

```text
git diff -- note.txt
git diff --cached -- note.txt
git diff HEAD -- note.txt
git log -1 --oneline
git show --stat HEAD
git show HEAD:note.txt
git show :note.txt
```

Esperado: diff simple second -> third, cached practice -> second, HEAD practice -> third. Log y show solo lectura; HEAD practice, index second. Si paginador abre, q sale. Ahora prepare third, inspeccione diff cached e identidades efectivas; si correcto haga commit:

```text
git add -- note.txt
git diff --cached -- note.txt
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Deténgase ante salida inesperada o identidades no ficticias. Luego:

```text
git commit -m "docs: update note"
git log -2 --oneline
git diff HEAD~1 HEAD -- note.txt
git show HEAD:note.txt
```

HEAD~1 significa primer padre de HEAD (aquí un commit atrás); comparación muestra practice -> third. Contenido third; draft.txt sigue no rastreado.

## Errores comunes y seguridad

Diff simple vacío no prueba ausencia de staging o no rastreados. Compruebe status y diff cached también. Si historial más corto, no invente IDs; inspeccione log.

## Ejercicio y autoevaluación

¿Qué diff muestra cambios del próximo commit? Respuesta: --cached. ¿Cuál muestra cambios rastreados frente al último commit? git diff HEAD. Apruebe si identifica tres bases. Uso profesional: revisar exactamente qué entrará al commit.

## Referencia rápida

- `git diff`
- `git log`
- `git show`
- `gitrevisions`

## Fuentes oficiales

- [Git: git-diff](https://git-scm.com/docs/git-diff)
- [Git: git-log](https://git-scm.com/docs/git-log)
- [Git: git-show](https://git-scm.com/docs/git-show)
- [Git: gitrevisions](https://git-scm.com/docs/gitrevisions)

---

<!-- navigation-footer -->
[Anterior](../02-status-add-commit/README.es.md) · [Índice](../README.es.md) · [Siguiente](../04-move-and-remove/README.es.md)
<!-- /navigation-footer -->
