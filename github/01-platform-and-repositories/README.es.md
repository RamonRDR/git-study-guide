# GitHub, repositorios y visibilidad

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Módulo anterior](../../history-and-recovery/README.es.md) · [Índice](../README.es.md) · [Siguiente](../02-permissions-and-authentication/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 25 min

**Requisitos previos:** [Remotos](../../remote-repositories/README.es.md) · [Historial y recuperación](../../history-and-recovery/README.es.md)

**Objetivo:** Distinguir datos locales de Git de servicios alojados y elegir visibilidad segura.

## Qué y por qué

Git funciona sin GitHub. GitHub aloja repositorios Git y añade navegación web, identidades, control de acceso, issues y pull requests. Un clon es repositorio Git local; publicar envía objetos y refs seleccionados al servidor. Público permite lectura pública, no push de cualquiera. Privado limita acceso pero no sirve para secretos. Visibilidad internal es función organizacional/enterprise, no requerida aquí. Repositorio público no es automáticamente open source: licencia determina derechos de reutilización. README explica proyecto; LICENSE concede derechos; CONTRIBUTING describe contribuciones; SECURITY indica canal privado de reporte cuando existe.

## Práctica

Offline: dibuja clon local -> repositorio Git remoto -> funciones web GitHub. Clasifica commit, rama, issue, pull request y label por capa. Opcional: visita repositorio público en navegador sin publicar. Comprueba rama predeterminada, archivos, historial, licencia y visibilidad. Para practicar creación usa repo personal desechable nuevo study-sandbox, privado por defecto, solo README ficticio. Nunca uses repos de empleador ni guía. Antes de publicar inspecciona historial confirmado completo, identidad y archivos; no hace falta cambiar visibilidad. Sandbox alojado creado con README inicial tiene primer commit propio; clónalo en vez de combinar historiales no relacionados.

## Errores comunes y seguridad

Cambiar público a privado no recupera clones existentes ni todas las copias; hacer privado público expone historial. Detente ante contenido confidencial; no experimentes visibilidad en repos reales. Haz respaldo independiente antes de eliminación autorizada; limpieza puede ser dejar sandbox privado vacío sin uso.

## Ejercicio y autoevaluación

¿Visitante puede hacer push por defecto en repo público? No. Aprueba si distingues lectura, permiso de escritura y licencia, e identificas tres conceptos Git nativos y dos alojados.

## Referencia rápida

- `Git`
- `GitHub`
- `README`
- `LICENSE`

## Fuentes oficiales

- <https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories>
- <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility>

---

<!-- navigation-footer -->
[Módulo anterior](../../history-and-recovery/README.es.md) · [Índice](../README.es.md) · [Siguiente](../02-permissions-and-authentication/README.es.md)
<!-- /navigation-footer -->
