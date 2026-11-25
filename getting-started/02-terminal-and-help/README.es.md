# Terminal y ayuda

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../01-install-git/README.es.md) · [Índice](../README.es.md) · [Siguiente](../03-first-repository/README.es.md)
<!-- /navigation -->

**Nivel:** principiante · **Tiempo estimado:** 20 min

**Requisitos previos:** [Instalar Git](../01-install-git/README.es.md)

**Objetivo:** Navegar directorios y consultar ayuda.

## Qué es y por qué

Directorio actual es donde comienzan rutas relativas. Repositorio es carpeta con metadatos e historial Git. Git suele encontrarlo desde directorio actual. Comandos tienen programa, operación y argumentos opcionales; sepa dónde está antes de cambiar.

## Práctica

Pruebe estas operaciones de navegación/ayuda. PowerShell y Bash/Zsh tienen sintaxis distintas.

```powershell
Get-Location
Get-ChildItem
Set-Location $HOME
```

```bash
pwd
ls
cd "$HOME"
```

```text
git --version
git status -h
git help status
```

Ayuda corta lista opciones; completa puede abrir manual o navegador. Pulse q para salir del paginador (visor desplazable).

## Errores comunes y seguridad

No copie símbolos del prompt como `$` o `PS>`. Use comillas en rutas con espacios. `git status` fuera de repo normalmente informa ausencia de repo; no es fallo de instalación. No comparta capturas con rutas privadas.

## Ejercicio y autoevaluación

Encuentre carpeta actual y consulte `git add -h`. Pista: distinga shell y Git. Apruebe si encuentra una opción sin cambiar archivos. Hábito profesional: compruebe ubicación del proyecto antes de comandos.

## Referencia rápida

- `git --version`
- `git status -h`
- `git help status`

## Fuentes oficiales

- [https://git-scm.com/docs/git-help](https://git-scm.com/docs/git-help)
- [https://git-scm.com/docs/gittutorial](https://git-scm.com/docs/gittutorial)
