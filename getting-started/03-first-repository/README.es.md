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

Abra terminal PowerShell o Bash nuevo dedicado al lab (en macOS/Zsh, inicie Bash con `bash` antes). Manténgalo abierto hasta módulo 01. Los comandos limpian variables Git heredadas solo en este shell y crean carpeta padre nueva con carpeta del repo, configuración global vacía y directorio de plantilla vacío. Excluyen configuración system/global y overrides heredados de autor/committer; plantilla vacía evita hooks heredados. No editan su configuración Git real. Use Git mantenido 2.40 o superior para este aislamiento. Elija un shell; deténgase ante cualquier error.

```powershell
Get-ChildItem Env: | Where-Object { $_.Name -like 'GIT_*' } | ForEach-Object {
    Remove-Item -LiteralPath ("Env:" + $_.Name) -ErrorAction Stop
}
$lab = Join-Path ([System.IO.Path]::GetTempPath()) ("git-study-" + [guid]::NewGuid().ToString("N"))
New-Item -ItemType Directory -Path $lab -ErrorAction Stop
New-Item -ItemType Directory -Path (Join-Path $lab "repo"), (Join-Path $lab "template") -ErrorAction Stop
$env:GIT_CONFIG_GLOBAL = Join-Path $lab "gitconfig"
New-Item -ItemType File -Path $env:GIT_CONFIG_GLOBAL -ErrorAction Stop
$env:GIT_CONFIG_NOSYSTEM = "1"
$env:GIT_TEMPLATE_DIR = Join-Path $lab "template"
$env:GIT_TERMINAL_PROMPT = "0"
Set-Location (Join-Path $lab "repo") -ErrorAction Stop
Get-Location
```

```bash
for name in $(compgen -e); do
    case "$name" in GIT_*) unset "$name" ;; esac
done
lab=$(mktemp -d) &&
mkdir "$lab/repo" "$lab/template" &&
touch "$lab/gitconfig" &&
export GIT_CONFIG_GLOBAL="$lab/gitconfig" GIT_CONFIG_NOSYSTEM=1 &&
export GIT_TEMPLATE_DIR="$lab/template" GIT_TERMINAL_PROMPT=0 &&
cd "$lab/repo" && pwd
```

Anote ruta de carpeta padre privadamente para limpieza. En subcarpeta repo nueva vacía, `git rev-parse --show-toplevel` debe fallar antes de inicializar; si funciona, deténgase y elija otro lab. Ejecute individualmente:

```text
git init --initial-branch=main
git config --local user.name "Study Guide Example"
git config --local user.email "learner@example.invalid"
git config --local commit.gpgsign false
git config --local --get user.name
git config --local --get user.email
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
git rev-parse --show-toplevel
git status
```

Ambas identidades efectivas deben comenzar con `Study Guide Example <learner@example.invalid>`; timestamps/zonas varían. Si alguna difiere o falla comando, deténgase; no haga commit. Esperado: raíz es subcarpeta repo, main sin commits. Mantenga mismo shell dedicado y no lo use para otros repos. Firma desactivada solo en lab desechable; no cambie política real.

## Errores comunes y seguridad

Nunca inicialice en guía, carpeta personal o repo laboral. No borre `.git` para corregir errores. Correo real puede hacerse público al compartir commits. Consulte solo claves locales, no volcado completo. Configuración local user sola no basta: ajustes heredados de autor/committer pueden sobrescribirla. Hooks son scripts automáticos. Use shell dedicado aislado; si falla, ciérrelo y reinicie lab en vez de alterar ajustes personales.

## Ejercicio y autoevaluación

Compruebe raíz, nombre y correo. Apruebe si identidad ficticia, main e historial vacío. Pista: `git var GIT_AUTHOR_IDENT` / `git var GIT_COMMITTER_IDENT`. Uso profesional: separar identidades por repo.

## Referencia rápida

- `git rev-parse --show-toplevel`
- `git init --initial-branch=main`
- `git config --local --get user.email`
- `git var GIT_AUTHOR_IDENT`
- `git var GIT_COMMITTER_IDENT`
- `git status`

## Fuentes oficiales

- [https://git-scm.com/docs/git-init](https://git-scm.com/docs/git-init)
- [https://git-scm.com/docs/git-config](https://git-scm.com/docs/git-config)
- [https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)

- [Git: git-var](https://git-scm.com/docs/git-var)
