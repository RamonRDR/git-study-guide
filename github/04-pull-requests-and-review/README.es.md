# Pull requests y revisión de código

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../03-issues-and-planning/README.es.md) · [Índice](../README.es.md) · [Siguiente](../05-forks-and-open-source/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 45 min

**Requisitos previos:** [Remotos](../../remote-repositories/README.es.md) · [Historial y recuperación](../../history-and-recovery/README.es.md) · [Issues, labels, milestones y projects](../03-issues-and-planning/README.es.md)

**Objetivo:** Seguir cambio revisable desde rama hasta merge autorizado.

## Qué y por qué

Pull request (PR) propone integración de head/origen en base/destino; abrirlo no integra historial Git. Draft indica trabajo no listo para revisión final. Files changed muestra diff, Commits muestra commits, Checks muestra ejecuciones automáticas. Revisión puede comentar, aprobar o pedir cambios; comentario solo no aprueba. Nuevos commits cambian head revisado y pueden invalidar aprobación según política. Palabra como Closes #1 en descripción puede cerrar issue al merge en rama predeterminada según reglas GitHub. Merge commit conserva ambos padres, squash crea un commit combinado, rebase-and-merge reaplica commits sin merge commit; métodos dependen de configuración. CI verde no garantiza corrección.

## Práctica

Offline: dibuja issue -> feature branch -> commit -> push -> PR -> revisión/checks -> merge autorizado -> verificar base. Redacta descripción con resumen, alcance, pruebas realmente ejecutadas, limitaciones y vínculo issue. Revisor ficticio encuentra instrucciones faltantes; revisa parche y pide revisión del nuevo head. Opcional: en sandbox privado propio usa edición web de rama/archivo para crear feat/setup-note desde main, añade requisitos ficticios, commit solo en esa rama, abre PR a main, inspecciona diff y vínculo (sustituye número real de issue). Ejercicio individual permite autoinspección pero no cuenta como aprobación independiente; si aprobación/checks requeridos no pueden satisfacerse, deja PR abierto o ciérralo sin merge. Si políticas aplicables y autorización del owner se satisfacen, elige método permitido, comprueba main y limpia solo rama feature integrada. Nunca desactives reglas para completar lab.

## Errores comunes y seguridad

Comprueba origen/destino y head actual, no solo iconos verdes. No marques conversaciones resueltas sin atenderlas. Si cambio integrado falla, propone commit correctivo revisado o revert; no hagas reset de main compartida. Trata feedback de IA como sugerencias, no aprobación humana.

## Ejercicio y autoevaluación

Aparece nuevo commit tras aprobación: ¿qué hacer? Revisa nuevo diff, repite checks aplicables y obtiene revisión requerida. Aprueba si distingues base, head, checks, aprobación y merge.

## Referencia rápida

- `base`
- `head`
- `review`
- `checks`
- `Closes #1`

## Fuentes oficiales

- <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests>
- <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews>
- <https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue>
- <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/about-merge-methods-on-github>
