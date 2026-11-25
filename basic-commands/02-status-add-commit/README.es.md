# Inspeccionar, preparar y registrar

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../01-init-config-help/README.es.md) · [Índice](../README.es.md) · [Siguiente](../03-diff-log-show/README.es.md)
<!-- /navigation -->

**Nivel:** principiante · **Tiempo estimado:** 30 min

**Requisitos previos:** [Inicializar, configurar y consultar ayuda](../01-init-config-help/README.es.md)

**Objetivo:** Registrar cambio enfocado y comprobar otro archivo no rastreado.

## Qué es y por qué

git status consulta estado preparado/no preparado/no rastreado; --short muestra códigos compactos. git add PATH prepara contenido actual del archivo. git add -p selecciona interactivamente hunks (grupos de líneas cambiadas) de rastreados; git add . puede preparar muchas rutas y git add -A abarca adiciones, cambios y borrados de todo working tree sin ruta. Prefiera rutas explícitas. git commit -m registra index con mensaje; git commit -a prepara también cambios/borrados de rastreados, no nuevos no rastreados, pudiendo incluir ediciones no deseadas. Evite hasta entender selección.

## Práctica

Use repo aislado nuevo de capítulo 01. En editor cree note.txt con practice y draft.txt con draft, cada uno con salto final. Inspeccione y prepare solo note.txt:

```text
git rev-parse --show-toplevel
git status --short
git add -- note.txt
git status --short
git diff --cached -- note.txt
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Esperado: A seguido de espacio para note.txt, ?? draft.txt. Si raíz, diff preparado o identidad incorrectos, deténgase. Si todo correcto:

```text
git commit -m "docs: add note"
git status --short
git show HEAD:note.txt
git ls-files
```

Esperado: solo draft.txt no rastreado; note.txt rastreado y guardado como practice. -- termina lectura de opciones para no confundir ruta con opción. Ninguna operación remota.

## Errores comunes y seguridad

Si cambios no deseados preparados, no haga commit; en ejercicio recree lab. Nunca fuerce inclusión de secretos ni haga commit de borradores privados. Compruebe ambas identidades antes de cada commit; shell aislado, no controles del editor.

## Ejercicio y autoevaluación

Prediga si draft.txt entra al commit. Respuesta: no, no preparado. Apruebe si ls-files lista solo note.txt. Uso profesional: elegir archivos para cambio revisable.

## Referencia rápida

- `git status`
- `git add`
- `git commit`

## Fuentes oficiales

- [Git: git-status](https://git-scm.com/docs/git-status)
- [Git: git-add](https://git-scm.com/docs/git-add)
- [Git: git-commit](https://git-scm.com/docs/git-commit)
