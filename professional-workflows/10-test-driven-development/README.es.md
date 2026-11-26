# Desarrollo guiado por pruebas (TDD)

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../09-spec-driven-development/README.es.md) · [Índice](../README.es.md) · [Siguiente](../11-ai-assisted-development/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 40 min

**Requisitos previos:** [CI/CD](../../ci-cd/README.es.md) · [Desarrollo guiado por especificación (SDD)](../09-spec-driven-development/README.es.md)

**Objetivo:** Explicar red, green y refactor sin confundir fallo de test con error de herramienta.

## Qué es y por qué

TDD es práctica iterativa de programación: escriba test pequeño que falla por comportamiento ausente previsto (red), implemente mínimo para pasar (green), luego mejore estructura manteniendo tests aprobados (refactor). Refactor cambia estructura interna sin alterar intencionalmente comportamiento observable. Test posterior a implementación puede ser útil, pero no evidencia ciclo red-first. SDD define lo necesario; TDD ayuda a implementar y verificar comportamientos pequeños. Ninguno exige lenguaje, IA, modelo de rama ni commit automático en cada color. Aserción de contenido shell ilustra feedback red/green; no es framework completo de tests unitarios.

```text
red -> green -> refactor -> next test
```

## Práctica

Antes del capítulo 13, prediga resultado de `grep -Fxq 'status: ready' catalog.txt` cuando archivo existente contiene draft. Luego prediga tras escribir línea exacta ready. Para refactor, imagine extraer check a función nombrada conservando entradas y comportamiento de salida; repita casos positivo, valor incorrecto y archivo ausente. Distinga error de herramienta/archivo ausente de fallo significativo de aserción. No exige experiencia en programación para rastrear resultados.

## Riesgos y recuperación

Nunca fuerce green borrando aserción, aceptando toda entrada o suprimiendo fallo. Inspeccione motivo; si test erróneo, corrija transparentemente. Mantenga integración compartida verde; si registra commits red intermedios localmente, no integre revisión rota. Ejemplo aprobado no es cobertura exhaustiva.

## Ejercicio y autoevaluación

Red esperado: sin coincidencia en draft existente (grep salida 1). Green: línea exacta coincide (salida 0). Error operativo no demuestra red válido. Refactor debe preservar resultados.

## Referencia rápida

red / green / refactor

## Fuentes

- <https://agilealliance.org/glossary/tdd/>
- <https://www.gnu.org/software/grep/manual/grep.html>

---

<!-- navigation-footer -->
[Anterior](../09-spec-driven-development/README.es.md) · [Índice](../README.es.md) · [Siguiente](../11-ai-assisted-development/README.es.md)
<!-- /navigation-footer -->
