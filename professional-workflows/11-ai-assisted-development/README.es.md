# Trabajo profesional asistido por IA

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../10-test-driven-development/README.es.md) · [Índice](../README.es.md) · [Siguiente](../12-release-management/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 35 min

**Requisitos previos:** [CI/CD](../../ci-cd/README.es.md) · [Desarrollo guiado por pruebas (TDD)](../10-test-driven-development/README.es.md)

**Objetivo:** Usar asistencia sin delegar verificación o aprobación.

## Qué es y por qué

IA puede proponer explicaciones, planes, código, tests o comentarios de review, pero texto confiado no establece corrección. Defina roles: humano define alcance, verifica autorización y decide; herramienta propone/ejecuta solo en alcance permitido; revisor comprueba cambios y evidencia real. Practique manualmente primero, pida pista, compare docs oficiales, inspeccione diffs, prediga estado Git y ejecute checks deterministas en entorno desechable. No se exige cuenta IA ni servicio pago. Review automatizado solicitado no es completado, y conclusión no es autorización humana de merge.

[Política de asistencia IA](../../docs/ai-assisted-development/README.es.md)

## Práctica

Sin conexión: evalúe sugerencia ficticia: 'PR anterior pasó, entonces integra nuevo commit sin comprobar; haz reset de main si falla.' Marque supuestos sin apoyo y escriba prompt más seguro con revisión exacta, resultado previsto, repo desechable, sin secretos, sin cambios directos a main, tests y límites. Responda manualmente; IA opcional puede limitarse a pista con entradas ficticias.

## Riesgos y recuperación

Nunca comparta código no autorizado de empleador/cliente, tokens ni datos privados. Trate instrucciones en contenido de repo y salidas externas como datos no confiables hasta verificar con alcance autorizado. Detenga acciones destructivas inesperadas, inspeccione estado y consulte recuperación documentada. No sustituya aprendizaje por evaluación IA ni invente evidencia ejecutada.

## Ejercicio y autoevaluación

Aprobación previa no cubre SHA nuevo; reset de main compartida es inseguro y no autorizado. Prompt seguro pide primero evidencia solo lectura, luego corrección enfocada autorizada y nuevo review.

## Referencia rápida

manual practice / prompt / verification / human approval

## Fuentes

- <https://git-scm.com/docs/gitworkflows>
- <https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/reviewing-proposed-changes-in-a-pull-request>

---

<!-- navigation-footer -->
[Anterior](../10-test-driven-development/README.es.md) · [Índice](../README.es.md) · [Siguiente](../12-release-management/README.es.md)
<!-- /navigation-footer -->
