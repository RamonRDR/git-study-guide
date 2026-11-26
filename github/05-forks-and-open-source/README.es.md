# Forks y contribuciones open source

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../04-pull-requests-and-review/README.es.md) · [Índice](../README.es.md) · [Siguiente](../06-protection-and-rulesets/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 30 min

**Requisitos previos:** [Remotos](../../remote-repositories/README.es.md) · [Historial y recuperación](../../history-and-recovery/README.es.md) · [Pull requests y revisión de código](../04-pull-requests-and-review/README.es.md)

**Objetivo:** Explicar contribuciones por fork y mantener upstream separado de origin.

## Qué y por qué

Fork GitHub es repositorio alojado asociado a original; clone es copia Git nativa. Fork no concede escritura en original. Clon local de fork normalmente usa origin para fork y upstream para original; convenciones, no nombres reservados. Haz fetch upstream, inspecciona divergencia y actualiza rama predeterminada local limpia solo por fast-forward si posible. Contribuye en ramas separadas; push al fork y propone PR de head del fork a base original. Sigue licencia, CONTRIBUTING, código de conducta y política de issues. Mantenedor puede rechazar contribución.

## Práctica

Offline: dibuja repo original alojado -> fork alojado -> clon local; etiqueta upstream y origin desde perspectiva local. Reutiliza modelo bare local del módulo 06 para razonar refs de seguimiento; simula transporte Git, no metadatos fork GitHub. Opcional solo lectura: inspecciona botón fork e instrucciones de contribución de proyecto público sin crear fork ni enviar PR de práctica. Si quieres contribución real después, coordina antes con mantenedores. Comprueba URL upstream, rama, estado y divergencia antes de sincronizar. No fuerces sincronización si fast-forward rechazado.

## Errores comunes y seguridad

No supongas que forks ocultan contenido público u obligaciones de licencia. Evita envíos de práctica no solicitados, issues duplicadas y parches confidenciales. Si destino incorrecto, detente y corrige o cierra tu PR en vez de integrar.

## Ejercicio y autoevaluación

¿Dónde envía colaborador rama propuesta si no tiene escritura upstream? Su fork autorizado. Aprueba si flechas y dirección PR correctas y distingues refs Git de forks alojados.

## Referencia rápida

- `origin`
- `upstream`
- `fork`
- `clone`

## Fuentes oficiales

- <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks>
- <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork>
- <https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-open-source>
