# Instalar Git

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
— · [Índice](../README.es.md) · [Siguiente](../02-terminal-and-help/README.es.md)
<!-- /navigation -->

**Nivel:** principiante · **Tiempo estimado:** 25 min

**Requisitos previos:** Ninguno; programación no requerida.

**Objetivo:** Instalar Git y comprobar la versión.

## Qué es y por qué

Git registra versiones seleccionadas de archivos localmente. No es editor ni lenguaje de programación. La terminal recibe comandos y el shell (PowerShell, Bash o Zsh) los interpreta. Instale Git una vez por entorno, no por proyecto.

## Práctica

Abra PowerShell en Windows o Terminal en Linux/macOS. Pruebe `git --version`. Si ya existe, use versión mantenida al menos 2.28. Si no, elija SOLO su SO:

Windows: use instalador oficial de su arquitectura o WinGet si disponible. Reabra terminal.

```powershell
winget install --id Git.Git -e --source winget
```

Debian/Ubuntu (con permiso):

```bash
sudo apt update
sudo apt install git
```

Fedora:

```bash
sudo dnf install git
```

macOS: solicite herramientas de línea de comandos Apple si falta Git, o Homebrew si ya instalado y confiable; elija uno.

```bash
xcode-select --install
```

```bash
brew install git
```

Repita `git --version`. Esperado: versión, no comando inexistente. Instalaciones verificadas en documentación, no probadas en máquinas limpias.

## Errores comunes y seguridad

No ejecute todos instaladores ni use privilegios elevados para Git normal. Si falla búsqueda, reabra terminal y compruebe PATH (directorios buscados para programas). Consulte TI en dispositivos gestionados.

## Ejercicio y autoevaluación

Identifique SO y shell. Pista: instale solo si falta. Apruebe si `git --version` funciona y explica Git frente a terminal. En informes profesionales registre versión Git.

## Referencia rápida

- `git --version`

## Fuentes oficiales

- [https://git-scm.com/install/](https://git-scm.com/install/)
- [https://git-scm.com/install/win](https://git-scm.com/install/win)
- [https://git-scm.com/install/linux.html](https://git-scm.com/install/linux.html)
- [https://git-scm.com/install/mac](https://git-scm.com/install/mac)
