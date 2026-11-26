# Protección de ramas, rulesets y quality gates

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../05-forks-and-open-source/README.es.md) · [Índice](../README.es.md) · [Siguiente](../07-tags-and-releases/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 40 min

**Requisitos previos:** [Remotos](../../remote-repositories/README.es.md) · [Historial y recuperación](../../history-and-recovery/README.es.md) · [Forks y contribuciones open source](../05-forks-and-open-source/README.es.md)

**Objetivo:** Diseñar política que proteja ramas compartidas sin eludir revisión.

## Qué y por qué

Branch protection y rulesets son políticas servidor GitHub, no comandos Git. Rulesets apuntan a refs y pueden coexistir con branch protection. Ejemplo para main: exigir PR, checks obligatorios con nombres observados, actualización estricta cuando exigida, conversaciones resueltas, historial lineal, bloqueo force push y eliminación, bypass restringido y revisiones obligatorias adecuadas cuando hay revisores independientes. Historial lineal solo permite squash o rebase, no merge commit normal; elige métodos y reglas juntos. Cantidad de aprobaciones debe ser realista: autores no aprueban su PR. Repos públicos GitHub Free soportan branch rulesets; disponibilidad privada varía según plan y tipo de regla. Nunca pagues para completar curso. Check verde es evidencia de commit específico, no garantía universal.

## Práctica

Ejercicio offline de política: evalúa cuatro PR ficticios. A: destino correcto, head actual, checks pasan, revisiones satisfechas, conversaciones resueltas. B: igual pero check requerido falla. C: igual pero thread abierto. D: igual pero base avanzó y actualización estricta requerida. Solo A es elegible a autorización humana de merge; B corrige check, C atiende feedback, D actualiza con seguridad y revalida. Opcional solo lectura: comprueba reglas visibles y caja de merge en repo accesible. Ningún cambio admin requerido. Antes de proponer reglas reales, inventaría checks y métodos existentes, revisa permisos, evalúa impacto en sandbox y obtiene aprobación admin explícita; lección no ejecuta cambio de configuración.

## Errores comunes y seguridad

No añadas check requerido nunca ejecutado, confundas skipped/neutral con éxito significativo de pruebas, eludas enforcement ni bloquees mantenedores. Lee logs reales y revisa head actual; si regla bloquea, diagnostica y solicita resolución aprobada en vez de desactivar. Workflows y permisos de runners se amplían en módulo 10.

## Ejercicio y autoevaluación

Aprueba si solo A elegible, explicas por qué squash no elude requisito de PR y nombras limitación de revisor independiente en proyecto solo.

## Referencia rápida

- `ruleset`
- `required checks`
- `linear history`
- `bypass`

## Fuentes oficiales

- <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches>
- <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets>
- <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets>
