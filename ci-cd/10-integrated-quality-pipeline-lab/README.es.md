# Laboratorio de pipeline de calidad integrado

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../09-quality-gates-and-troubleshooting/README.es.md) · [Índice](../README.es.md) · [Siguiente módulo](../../professional-workflows/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 45 min

**Requisitos previos:** [GitHub](../../github/README.es.md) · [GitLab](../../gitlab/README.es.md) · [Controles de calidad y diagnóstico](../09-quality-gates-and-troubleshooting/README.es.md)

**Objetivo:** Reproducir checks exitosos y fallidos sin conexión y conectarlos a pipeline profesional.

## Qué es y por qué

Pipeline puede combinar lint y tests sin dependencia de lenguaje de programación. Catálogo ficticio debe ser no vacío y contener línea exacta `status: ready`. Primer comando es comprobación estructural, segundo aserción simple de contenido; ninguno es lint completo ni test de aplicación. Mismos checks shell aparecen en ejemplos GitHub/GitLab de capítulos 03 y 04. Ejecute solo ejemplo local acotado abajo en Bash en Linux/macOS o Git Bash en Windows, no PowerShell ni cmd. Crea directorio temporal aislado, no requiere configuración Git, red, Python, credenciales ni alojamiento, y elimina solo dos archivos creados y directorio temporal vacío. Informa tres resultados esperados; casos fallidos se prueban deliberadamente, no se suprimen como checks de contenido exitosos.

```bash
(
  set -eu
  sandbox=$(mktemp -d)
  printf 'Sandbox: %s\n' "$sandbox"
  trap 'rm -f -- "$sandbox/catalog.txt" "$sandbox/empty.txt"; rmdir -- "$sandbox"' EXIT
  check_catalog() {
    test -s "$1" && grep -Fxq 'status: ready' "$1"
  }
  printf '%s\n' 'status: ready' > "$sandbox/catalog.txt"
  check_catalog "$sandbox/catalog.txt"
  printf '%s\n' 'PASS ready'
  printf '%s\n' 'status: draft' > "$sandbox/catalog.txt"
  if check_catalog "$sandbox/catalog.txt"; then
    exit 1
  fi
  printf '%s\n' 'PASS wrong rejected'
  : > "$sandbox/empty.txt"
  if check_catalog "$sandbox/empty.txt"; then
    exit 1
  fi
  printf '%s\n' 'PASS empty rejected'
)
```

## Práctica

Lea script y ejecute bloque completo tal como está en shell desechable. Salida esperada: `PASS ready`, `PASS wrong rejected`, `PASS empty rejected`, estado de salida cero. Primer test usa archivo ready; segundo archivo no vacío incorrecto; tercero vacío. Equipo profesional versionaría solo checks revisados, usaría herramientas reales adecuadas de lint/test, exigiría ambos entornos si necesario, inspeccionaría revisiones exactas y separaría despliegue de producción. Práctica alojada opcional no exigida; use solo repositorio desechable propio si uso gratuito y aislamiento verificados, nunca habilite despliegue.

## Errores comunes y seguridad

Si setup falla, pare. Nunca sustituya directorio temporal por ruta de proyecto real. Trap de limpieza elimina solo archivos conocidos; si falla, inspeccione ruta temporal impresa, no use eliminación recursiva en rutas desconocidas. Si check pasa o falla inesperadamente, inspeccione contenido y código de salida; no debilite aserción. Lección manual, no archivo ejecutado automáticamente por guía.

## Ejercicio y autoevaluación

Apruebe si aparecen tres mensajes esperados, explica por qué entradas incorrecta/vacía fallan e identifica mismos comandos en ambos YAML. Sandbox exitoso no demuestra ejecución alojada.

## Referencia rápida

`test -s` / `grep -Fxq` / exit status

## Fuentes oficiales

- <https://www.gnu.org/software/bash/manual/html_node/Exit-Status.html>
- <https://www.gnu.org/software/grep/manual/grep.html>
- <https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax>
- <https://docs.gitlab.com/ci/yaml/>

---

<!-- navigation-footer -->
[Anterior](../09-quality-gates-and-troubleshooting/README.es.md) · [Índice](../README.es.md) · [Siguiente módulo](../../professional-workflows/README.es.md)
<!-- /navigation-footer -->
