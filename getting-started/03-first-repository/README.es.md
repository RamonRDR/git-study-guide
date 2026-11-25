# Primer repositorio y configuración

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../02-terminal-and-help/README.es.md) · [Índice](../README.es.md) · [Siguiente](../04-editor-and-gui/README.es.md)
<!-- /navigation -->

**Nivel:** principiante · **Tiempo estimado:** 30 min

**Requisitos previos:** [Terminal y ayuda](../02-terminal-and-help/README.es.md)

**Objetivo:** Crear repo desechable y configurar identidad local ficticia.

## Qué es y por qué

Repo local guarda metadatos e historial en directorio oculto `.git`. Rama es línea de desarrollo nombrada; main es nombre inicial. Init crea metadatos, no commit. Identidad es autoría registrada, no autenticación. Configuración system aplica ampliamente, global al usuario y local al repo; local normalmente prevalece.

## Práctica

Cree carpeta temporal nueva, no guía ni proyecto existente. Elija su shell.

```powershell
$lab = Join-Path ([System.IO.Path]::GetTempPath()) ("git-study-" + [guid]::NewGuid().ToString("N"))
New-Item -ItemType Directory -Path $lab -ErrorAction Stop
Set-Location $lab -ErrorAction Stop
Get-Location
```

```bash
lab=$(mktemp -d) && cd "$lab" && pwd
```

Deténgase si falla creación/navegación. En carpeta nueva vacía, `git rev-parse --show-toplevel` debe fallar (fuera de repo). Si funciona, elija otra. Luego ejecute individualmente:

```text
git init --initial-branch=main
git config --local user.name "Study Guide Example"
git config --local user.email "learner@example.invalid"
git config --local commit.gpgsign false
git config --local --get user.name
git config --local --get user.email
git rev-parse --show-toplevel
git status
```

Esperado: identidad ficticia, carpeta nueva, rama main y ningún commit. Firma desactivada solo en lab desechable; no cambie políticas reales. Conserve lab para próximas lecciones.

## Errores comunes y seguridad

Nunca inicialice en guía, carpeta personal o repo laboral. No borre `.git` para corregir errores. Correo real puede hacerse público al compartir commits. Consulte solo claves locales, no volcado completo. Hooks (scripts automáticos) o ajustes existentes pueden afectar práctica; CI aísla configuración. Si duda, deténgase y cree lab nuevo.

## Ejercicio y autoevaluación

Compruebe raíz, nombre y correo. Apruebe si identidad ficticia, main e historial vacío. Pista: `git config --local --get user.email`. Uso profesional: separar identidades por repo.

## Referencia rápida

- `git rev-parse --show-toplevel`
- `git init --initial-branch=main`
- `git config --local --get user.email`
- `git status`

## Fuentes oficiales

- [https://git-scm.com/docs/git-init](https://git-scm.com/docs/git-init)
- [https://git-scm.com/docs/git-config](https://git-scm.com/docs/git-config)
- [https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)
