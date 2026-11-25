# Desarrollo asistido por IA

[English](README.en.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

## Principio y roles

Usar IA para ampliar capacidad de pensar, aprender, construir y verificar, no para renunciar a responsabilidad. ChatGPT puede asistir conversación, tutoría, planificación, investigación y redacción. Codex puede inspeccionar repos, implementar, probar y revisar cuando esté disponible. Ambos pueden equivocarse de forma convincente. Ramon Rodriguez define estrategia, educación, edición y activos visuales; IA asiste implementación y revisión; decisiones finales son humanas. Estudiantes no necesitan cuenta de IA ni plan de pago.

## Estudie manualmente primero

Intente primero un ejercicio en repositorio desechable. Prediga qué estado o referencia cambiará, inspeccione status/diff/historial, ejecute un comando seguro y compare resultados. Si se atasca, pida una pista, no solución completa. Ejemplo: `Estoy aprendiendo staging. Dame una pista para explicar por qué un archivo nuevo no está en mi próximo commit. No me des el comando hasta que lo intente.` Pida fuentes oficiales y explique el resultado con sus palabras. Nunca ejecute comandos destructivos sugeridos en proyecto real. IA es opcional; fuentes oficiales, práctica y respuestas de referencia bastan.

## De la pregunta al brief de implementación

Un prompt útil aporta contexto, objetivo, estado actual, alcance, restricciones, salida esperada y validación. Refinar con preguntas, versión/SO y evidencia; no ocultar incertidumbre. Ejemplo de brief: explicar creación de rama local a principiantes; definir refs antes de usarlas; usar repo ficticio desechable; aportar EN/PT-BR/ES; sin remoto real ni comandos destructivos; verificar ejemplos y enlaces; informar checks no ejecutados; abrir PR enfocado desde main actual. Establecer especificación, plan, tareas y criterios antes de implementar; obtener aprobación de alcance del mantenedor. No suponer corrección por un prompt bien escrito.

## Verificación y revisión

Inspeccionar cada archivo cambiado y alcance. Comprobar fuentes oficiales, requisitos, advertencias de seguridad, terminología, ejemplos originales y significado entre idiomas. Probar estado Git real en directorios desechables propios, incluidos fallos representativos; registrar comando, entorno y resultado. Verificar último SHA, CI y feedback de Codex cuando estén disponibles; solicitud no es review terminado. Atender hallazgos, repetir checks y obtener aprobación humana antes de squash merge. Nunca inventar resultados ni aprobar checks ausentes. Evaluación semántica por IA fuera de alcance; preferir comprobaciones de estado objetivas y autoevaluación.

## Privacidad, costos e independencia

Nunca compartir repos privados no autorizados, procesos de empleadores/clientes, credenciales, tokens, datos personales, URL privadas, código propietario ni logs sensibles con IA o issues públicas. Anonimización superficial puede no bastar; crear ejemplos ficticios originales. Disponibilidad, privacidad y límites cambian; consultar documentación oficial antes de depender de capacidad. Sin API de pago, servidor, suscripción IA ni evaluación IA obligatoria. Guía independiente, sin respaldo de OpenAI o plataformas.

- [Constitution](../specs/constitution.es.md)
- [Autoría](../localized/AUTHORS.es.md)
- [Guía de contribución](../localized/CONTRIBUTING.es.md)
- [Instrucciones](../localized/AGENTS.es.md)
