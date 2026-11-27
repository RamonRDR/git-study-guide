# Mi primer repositorio

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Módulo anterior](../../command-reference/README.es.md) · [Índice](../README.es.md) · [Siguiente módulo](../../exercises/README.es.md)
<!-- /navigation -->

**Nivel:** principiante · **Tiempo estimado:** 30 min

**Prerrequisitos:** [Primer repositorio](../../getting-started/03-first-repository/README.es.md) · [Tres ubicaciones](../../git-architecture/01-three-locations/README.es.md) · [Status, add y commit](../../basic-commands/02-status-add-commit/README.es.md). Git 2.40+ y Bash (Linux/macOS o Git Bash en Windows).

**Objetivo:** Crear repositorio local privado de notas y demostrar que un commit registra el index, no todas las ediciones de archivos de trabajo.

## Escenario

Mantienes un archivo ficticio de notas con estado draft y ready. Una tercera edición experimental no debe entrar en el historial. No se necesita remoto, cuenta ni programación.

## Preparación desechable

Abre una shell Bash ordinaria dedicada, no el directorio de trabajo del guía. Ejecuta los comandos uno a uno. Detente si alguno falla, especialmente creación del directorio temporal o cd. Confirma que la raíz impresa es el nuevo repositorio sandbox, ambas identidades son ficticias y la salida de remote está vacía. La configuración aislada solo vale para esta shell, no es un sandbox de seguridad reforzada.

```bash
sandbox=$(mktemp -d)
printf 'Sandbox: %s\n' "$sandbox"
for key in $(compgen -e); do
  case "$key" in GIT_*) unset "$key";; esac
done
mkdir "$sandbox/home" "$sandbox/template"
export HOME="$sandbox/home" USERPROFILE="$sandbox/home"
export XDG_CONFIG_HOME="$sandbox/home"
export GIT_CONFIG_NOSYSTEM=1 GIT_CONFIG_GLOBAL="$sandbox/gitconfig"
export GIT_CONFIG_COUNT=0 GIT_TERMINAL_PROMPT=0
export GIT_TEMPLATE_DIR="$sandbox/template"
git init -b main "$sandbox/repo"
cd "$sandbox/repo"
git config --local user.name 'Study Guide Example'
git config --local user.email 'learner@example.invalid'
git config --local commit.gpgsign false
git config --local core.autocrlf false
git config --local core.hooksPath "$sandbox/no-hooks"
git rev-parse --show-toplevel
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
git remote
```

## Desafío

Crea notes.txt con status: draft y realiza el primer commit. Cambia a status: ready y prepara en staging; después cambia el archivo de trabajo a status: experiment sin preparar otra vez. Inspecciona las tres ubicaciones. Confirma solo la instantánea ready. Comprueba que experiment sigue sin preparar y descarta intencionalmente solo esa edición ficticia. Termina en main con dos commits y working tree limpia. Intenta sin consultar la solución.

## Pistas progresivas

1. Usa git status y git add para distinguir archivo no rastreado de cambio preparado.
2. Compara git show HEAD:notes.txt, git show :notes.txt y archivo de trabajo. git diff y git diff --cached comparan ubicaciones distintas.
3. Un commit ordinario registra el index. Tras confirmar que la edición restante es desechable, restaura solo esa ruta de trabajo desde el index.

## Solución de referencia

Primero crea y confirma draft. La salida inicial de porcelain es ?? notes.txt.

```bash
printf '%s\n' 'status: draft' > notes.txt
git status --porcelain=v1
git add notes.txt
git diff --cached
git commit -m 'docs: initialize notes'
```

Luego prepara ready y edita otra vez el archivo de trabajo. Espera MM notes.txt antes del commit: index y archivo difieren de sus respectivos puntos de comparación. HEAD contiene draft, index contiene ready y archivo contiene experiment. Tras commit, HEAD contiene ready y porcelain muestra espacio inicial seguido de M.

```bash
printf '%s\n' 'status: ready' > notes.txt
git add notes.txt
printf '%s\n' 'status: experiment' > notes.txt
git status --porcelain=v1
git show HEAD:notes.txt
git show :notes.txt
git diff
git diff --cached
git commit -m 'docs: mark notes ready'
git show HEAD:notes.txt
git status --porcelain=v1
```

Solo tras verificar que la línea experimental es deliberadamente desechable, restaura el archivo de trabajo desde el index. Esto descarta la edición no preparada; no lo uses con trabajo valioso.

```bash
git restore --worktree -- notes.txt
git status --porcelain=v1
git log --oneline
git rev-list --count HEAD
git branch --show-current
git remote
```

## Criterios de éxito

- Exactamente dos commits alcanzables desde main; el segundo contiene status: ready, su padre contiene status: draft.
- Archivo de trabajo e index coinciden con HEAD; salida porcelain vacía.
- Rama actual main; sin remotos.
- Explica por qué se confirmó la instantánea ready preparada mientras experiment quedó sin preparar. Una working tree limpia por sí sola no demuestra instantánea prevista.

Prueba de mantenimiento: tests/test_git_practical_projects.py, test_first_repository_staged_snapshot. Comprueba estados intermedios y finales, incluido candidato final sucio intencionalmente incorrecto. Ejecuta solo comandos fijos, no entregas de estudiantes.

## Recuperación y limpieza

Si el estado difiere, detente e inspecciona status, diff y diff preparado. Conserva contenido valioso antes de restaurar; Git no garantiza recuperación de ediciones no preparadas descartadas. Cierra la shell dedicada y elimina solo el directorio sandbox impreso mediante gestor de archivos tras comprobar su contenido. Nunca elimines repositorio real.

## Fuentes oficiales

- <https://git-scm.com/docs/git-init>
- <https://git-scm.com/docs/git-status>
- <https://git-scm.com/docs/git-add>
- <https://git-scm.com/docs/git-commit>
- <https://git-scm.com/docs/git-restore>

---

<!-- navigation-footer -->
[Módulo anterior](../../command-reference/README.es.md) · [Índice](../README.es.md) · [Siguiente módulo](../../exercises/README.es.md)
<!-- /navigation-footer -->
