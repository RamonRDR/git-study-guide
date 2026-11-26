# Estados de archivos y límites del remoto

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../02-snapshots-head-and-refs/README.es.md) · [Índice](../README.es.md) · [Siguiente módulo](../../basic-commands/README.es.md)
<!-- /navigation -->

**Nivel:** principiante · **Tiempo estimado:** 25 min

**Requisitos previos:** [Snapshots, HEAD y referencias](../02-snapshots-head-and-refs/README.es.md)

**Objetivo:** Interpretar archivos rastreados, no rastreados, modificados, preparados e ignorados.

## Qué es y por qué

Rastreado significa ruta representada en index; no rastreado no está. Modificado significa contenido diferente de base de comparación; preparado significa index difiere de HEAD. No son excluyentes: MM indica dos diferencias. Archivo no rastreado ignorado coincide con regla y normalmente se omite de status/add; ignorar no deja de rastrear archivo ya rastreado. Status limpio significa ausencia de diferencias informadas o no rastreados no ignorados, no respaldo ni sincronización remota.

## Práctica

Continúe lab con third aún editado. Cree draft.txt nuevo en editor con draft. Inspeccione (solo lectura):

```text
git status --short
git ls-files
git remote -v
```

Esperado: espacio-M note.txt y ?? draft.txt; ls-files lista note.txt; remotos vacío porque ninguno fue configurado. Status corto tiene dos posiciones XY: X compara index con HEAD, Y working tree con index (entradas comunes sin conflicto). ?? no rastreado, !! ignorado cuando solicitado. A añadido, M modificado, D borrado, R renombre detectado. Conflictos más adelante.

## Errores comunes y seguridad

No deduzca estado remoto de status local. No hace falta fetch, push ni credenciales. No añada todo a ciegas; inspeccione antes. Si rutas inesperadas, deténgase y compruebe raíz desechable. Conserve lab para módulo 03 o recréelo desde 00.

## Ejercicio y autoevaluación

Clasifique note.txt y draft.txt. Respuesta: note rastreado y modificado no preparado; draft no rastreado. Apruebe si explica por qué remoto vacío no impide commits. Uso profesional: inspeccionar cambios antes de revisión.

## Referencia rápida

- `git status`
- `git ls-files`
- `git remote`
- `gitignore`

## Fuentes oficiales

- [Git: git-status](https://git-scm.com/docs/git-status)
- [Git: git-ls-files](https://git-scm.com/docs/git-ls-files)
- [Git: git-remote](https://git-scm.com/docs/git-remote)
- [Git: gitignore](https://git-scm.com/docs/gitignore)

---

<!-- navigation-footer -->
[Anterior](../02-snapshots-head-and-refs/README.es.md) · [Índice](../README.es.md) · [Siguiente módulo](../../basic-commands/README.es.md)
<!-- /navigation-footer -->
