# Renombrar y eliminar archivos rastreados

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../03-diff-log-show/README.es.md) · [Índice](../README.es.md) · [Siguiente](../05-ignore-and-review/README.es.md)
<!-- /navigation -->

**Nivel:** principiante · **Tiempo estimado:** 30 min

**Requisitos previos:** [Comparar e inspeccionar historial](../03-diff-log-show/README.es.md)

**Objetivo:** Distinguir borrado de archivo de trabajo, borrado preparado y eliminación solo de index.

## Qué es y por qué

git mv OLD NEW mueve ruta rastreada y prepara borrado anterior/adición nueva; detección de renombre depende de similitud, no metadato permanente. git rm PATH quita rastreado de working tree e index (prepara borrado). git rm --cached PATH quita solo index manteniendo archivo; si rastreado en HEAD prepara borrado. Git puede rechazar si hay riesgo de pérdida; nunca use -f aquí. Mover/borrar en gestor cambia working tree; Git registra efectos preparados tras add/rm.

## Práctica

Continúe lab desechable capítulo 03: note.txt registrado con third; draft.txt no rastreado. Compruebe raíz/status, asegure que destino notes.txt no existe. Renombre solo note.txt:

```text
git rev-parse --show-toplevel
git status --short
git mv -- note.txt notes.txt
git diff --cached --name-status
git status --short
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Espere renombre preparado (o borrado/adición equivalente). Si correcto e identidades ficticias, registre renombre y quite solo entrada del index:

```text
git commit -m "docs: rename note"
git rm --cached -- notes.txt
git status --short
git diff --cached --name-status
```

Esperado: D preparado de notes.txt y notes.txt no rastreado sigue en disco. No registre eliminación; añada otra vez para cancelar borrado preparado sin cambiar contenido. Luego quite rastreado (solo contenido desechable):

```text
git add -- notes.txt
git diff --cached --name-status
git rm -- notes.txt
git diff --cached --name-status
git status --short
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Esperado: primer diff vacío, segundo D notes.txt y archivo ausente; draft permanece. Si esperado e identidades ficticias, registre:

```text
git commit -m "docs: remove note"
git status --short
```

## Errores comunes y seguridad

Nunca ejecute rm en repo real sin entender borrado/respaldo. Sin -f, borrado recursivo ni comodines. Contenido registrado anterior permanece en historial, pero ediciones no registradas pueden no recuperarse. Si comando rechaza, inspeccione status; deténgase en vez de forzar. Recuperación más adelante.

## Ejercicio y autoevaluación

Compare rm y rm --cached. Respuesta: ambos quitan entrada index; solo rm normal quita archivo. Apruebe si comprueba casos y explica historial anterior. Uso profesional: dejar de rastrear dato generado sin borrar copia local (junto a regla ignore).

## Referencia rápida

- `git mv`
- `git rm`
- `git add`
- `git diff`

## Fuentes oficiales

- [Git: git-mv](https://git-scm.com/docs/git-mv)
- [Git: git-rm](https://git-scm.com/docs/git-rm)
- [Git: git-add](https://git-scm.com/docs/git-add)
- [Git: git-diff](https://git-scm.com/docs/git-diff)

---

<!-- navigation-footer -->
[Anterior](../03-diff-log-show/README.es.md) · [Índice](../README.es.md) · [Siguiente](../05-ignore-and-review/README.es.md)
<!-- /navigation-footer -->
