# Secretos y prevención de filtraciones

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../04-credential-managers/README.es.md) · [Índice](../README.es.md) · [Siguiente](../06-permissions-and-least-privilege/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 40 min

**Requisitos previos:** [Flujos profesionales](../../professional-workflows/README.es.md) · [Gestores de credenciales y ámbito de configuración](../04-credential-managers/README.es.md)

**Objetivo:** Prevenir exposición accidental e inspeccionar tracking.

## Qué es y por qué

Secreto es material confidencial de autenticación u otro valor sensible. Guarde secretos reales en gestor aprobado fuera de control de versiones. Publique solo plantillas saneadas con ejemplos no secretos. `.gitignore` coincide con rutas no rastreadas; no quita archivos ya en índice ni borra historial. `git check-ignore -- path` comprueba reglas de ruta no rastreada; `git ls-files -- path` inspecciona entradas rastreadas. Check de nombres staged ayuda a evitar adiciones accidentales pero no inspecciona contenido. Secret scanning y push protection son defensas heurísticas dependientes del proveedor, no prueba de ausencia. Elimine u oculte los valores sensibles antes de compartir logs y artefactos; nunca publique secretos reales ni en repos privados.

## Práctica

Use capítulo 13 con valores inocuos `mode=local` y `mode=example`. Prediga rutas ignoradas y staged. Para archivo local hipotético ya rastreado, explique por qué añadirlo a ignore no basta; corrección autorizada debe retirarlo de tracking y evaluar exposición previa.

## Riesgos y recuperación

Nunca cree token falso de apariencia real, pegue secreto real en scanner ni use force-add para eludir ignore. Ante exposición, priorice revocación e incidente; borrar archivo solo no basta.

## Ejercicio y autoevaluación

Ignore y tracking son distintos; plantilla es segura solo por contenido deliberadamente no sensible. Scanning es defensa en profundidad.

## Referencia rápida

`git check-ignore` / `git ls-files` / `.gitignore`

## Referencias

- <https://git-scm.com/docs/gitignore>
- <https://git-scm.com/docs/git-check-ignore>
- <https://git-scm.com/docs/git-ls-files>
- <https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning>
