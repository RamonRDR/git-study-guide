# ADR 0003: Entornos de práctica

[English](0003-practice-environments.md) · [Português](0003-practice-environments.pt-BR.md) · [Español](0003-practice-environments.es.md)

Propuesta para revisión del mantenedor; no autoriza iniciar el Sprint 01.

## Contexto

Cambios de estado Git pueden destruir trabajo y servicios remotos requieren cuentas; práctica debe seguir gratuita.

## Decisión

Usar Git instalado en directorios temporales desechables, origin bare y múltiples clones. Aislar identidad/config, hooks y credenciales; evitar remotos reales por defecto. Marcar tareas exclusivas de plataformas como opcionales. Inspeccionar estado antes de comandos destructivos y limpiar solo rutas temporales propias; nunca usar el repositorio de la guía.

## Alternativas

Rechazar labs alojados obligatorios y shell remoto (costo, credenciales, aislamiento); aplazar simulador/runtime de navegador hasta ADR separada en Sprint 18.

## Consecuencias

Verificar estado determinísticamente, probar Linux/Windows, documentar versiones soportadas y diferencias de shell. Sin garantía de recuperación tras operaciones destructivas. Simulador de navegador no debe afirmar fidelidad sin pruebas.

## Documentos relacionados

- [Índice ADR](README.es.md)
- [Contrato de integración](../specs/project-foundation/integration-contract.es.md)
