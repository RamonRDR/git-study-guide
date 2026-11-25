# Por qué existe control de versiones

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
— · [Índice](../README.es.md) · [Siguiente](../02-history-of-git/README.es.md)
<!-- /navigation -->

**Nivel:** principiante · **Tiempo estimado:** 20 min

**Requisitos previos:** [Primeros pasos](../../getting-started/README.es.md)

**Objetivo:** Explicar historial intencional frente a guardado normal.

## Qué es y por qué

Control de versiones registra revisiones para comparar cambios e identificar decisiones. Guardar sobrescribe contenido actual; copias plan-final.txt y plan-final-2.txt confunden. Git registra snapshots elegidos y relaciones con commits anteriores. Útil para código y documentación textual, no automáticamente para medios enormes o bases. No sustituye respaldo: perder disco puede destruir historial local.

## Práctica

Biblioteca ficticia cambia horarios entre semana y sábado. En vez de tres copias finales, registre cada cambio por separado. Snapshot inicial -> revisión semana -> revisión sábado; flechas describen historial, no nombres. En lab consulte historial sin internet.

```text
git log -1 --oneline
```

## Errores comunes y seguridad

No haga commit de secretos ni datos privados. Git no registra cada guardado ni garantiza recuperar ediciones sin commit. Mantenga respaldos independientes.

## Ejercicio y autoevaluación

Sugiera dos mensajes enfocados. Pista: un propósito por cambio. Respuesta: `docs: update weekday hours` y `docs: update Saturday hours`. Apruebe si explica por qué historial es claro y respaldo necesario.

## Referencia rápida

- `git log -1 --oneline`

## Fuentes oficiales

- [https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control)
- [https://git-scm.com/book/en/v2/Getting-Started-What-is-Git](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git)
