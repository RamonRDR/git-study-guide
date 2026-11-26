# Reglas de ignore y revisión final

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../04-move-and-remove/README.es.md) · [Índice](../README.es.md) · [Siguiente módulo](../../branches/README.es.md)
<!-- /navigation -->

**Nivel:** principiante · **Tiempo estimado:** 30 min

**Requisitos previos:** [Renombrar y eliminar archivos rastreados](../04-move-and-remove/README.es.md)

**Objetivo:** Usar .gitignore y entender por qué rastreados ignorados siguen rastreados.

## Qué es y por qué

Archivo .gitignore contiene patrones para rutas intencionalmente no rastreadas, como salidas generadas. Barra inicial ancla patrón relativo al ignore; barra final coincide con directorios; * coincide dentro de componentes; ! puede negar regla anterior (pero no reincluir archivo si padre excluido). Git también admite .git/info/exclude local y core.excludesFile global; lab usa solo .gitignore compartido. Ignore no es cifrado, control de acceso ni eliminación de historial. Rastreado no se ve afectado hasta quitar del index.

## Práctica

Continúe lab: draft.txt no rastreado. Cree .gitignore de texto plano en raíz con estas líneas y report.tmp ficticio con sample (nunca secretos reales):

```text
/draft.txt
*.tmp
!keep.tmp
/build/
```

Cree keep.tmp con keep. Compruebe:

```text
git status --short --ignored
git check-ignore -v -- draft.txt report.tmp
git add -- .gitignore keep.tmp
git diff --cached --name-status
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Esperado: draft.txt/report.tmp ignorados (!!), keep.tmp no rastreado antes de add, luego preparado con .gitignore. Si diff e identidades ficticias correctos, registre. 

```text
git commit -m "docs: add ignore rules"
```

Solo ahora añada /keep.tmp a .gitignore y edite keep.tmp a updated; guarde ambos. Luego:

```text
git status --short
git ls-files -- keep.tmp
git check-ignore --no-index -v -- keep.tmp
```

Ejecute últimos tres comandos DESPUÉS de cambios en editor. Esperado: ambos rastreados modificados, keep.tmp sigue rastreado, --no-index muestra regla aun para rastreado. No prepare keep.tmp. Opcionalmente deje de rastrearlo como ejercicio local deliberado, inspeccione borrado preparado y prepare solo cambio de ignore:

```text
git rm --cached -- keep.tmp
git add -- .gitignore
git diff --cached --name-status
git status --short --ignored
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Esperado: borrado preparado keep.tmp, modificación .gitignore, keep.tmp sigue en disco e ignorado. Registre solo si esperado e identidades ficticias verificadas:

```text
git commit -m "docs: stop tracking generated file"
git status --short --ignored
git ls-files
```

## Errores comunes y seguridad

Si secreto fue registrado, ignore o rm --cached no basta; revoque/rote credencial y siga proceso de incidente (módulo 12). Nunca fuerce contenido sensible. Revise status, diff cached, identidad e historial. Para finalizar cierre editor y shell dedicado, luego borre SOLO carpeta padre temporal exacta anotada en módulo 00 mediante gestor, si no necesita.

## Ejercicio y autoevaluación

¿Por qué keep.tmp sigue modificado tras regla ignore? Respuesta: ya rastreado. Apruebe si distingue ignorar, dejar de rastrear y borrar, y explica por qué secreto ignorado en historial sigue siendo problema. Uso profesional: revisar ignore de generados antes del primer commit.

## Referencia rápida

- `gitignore`
- `git check-ignore`
- `git rm`
- `git status`

## Fuentes oficiales

- [Git: gitignore](https://git-scm.com/docs/gitignore)
- [Git: git-check-ignore](https://git-scm.com/docs/git-check-ignore)
- [Git: git-rm](https://git-scm.com/docs/git-rm)
- [Git: git-status](https://git-scm.com/docs/git-status)

---

<!-- navigation-footer -->
[Anterior](../04-move-and-remove/README.es.md) · [Índice](../README.es.md) · [Siguiente módulo](../../branches/README.es.md)
<!-- /navigation-footer -->
