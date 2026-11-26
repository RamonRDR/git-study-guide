# 13 Git avanzado

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../security/README.es.md) · [Índice](../docs/learning-path.es.md) · [Siguiente](../git-internals/README.es.md)
<!-- /navigation -->

**Estado: lecciones incluidas en Sprint 14.** 470 min. Requisito: seguridad y módulos previos de flujo. Git 2.34+ recomendado; Bash (Git Bash en Windows), auxiliar subtree opcional. Sin credenciales en línea.

## Laboratorio desechable

Abra shell Bash dedicado nuevo (`bash --noprofile --norc`) antes de cada capítulo; no ejecute en shell normal. Ejecute comandos individualmente, deteniéndose ante fallos. Antes de commit, compruebe ambas identidades con `Study Guide Example <learner@example.invalid>` al inicio; si no, pare. Compruebe sandbox y raíz impresos, sin remoto y estado limpio. Tres commits cambian catálogo ficticio; primeros dos buenos, último malo. No reutilice sandbox antiguo.

```bash
sandbox=$(mktemp -d)
printf 'Sandbox: %s\n' "$sandbox"
while IFS= read -r name; do unset "$name"; done < <(compgen -e GIT_)
mkdir "$sandbox/home" "$sandbox/template"
export HOME="$sandbox/home" USERPROFILE="$sandbox/home"
export GIT_CONFIG_GLOBAL="$sandbox/gitconfig" GIT_CONFIG_NOSYSTEM=1
export GIT_CONFIG_COUNT=0 GIT_TEMPLATE_DIR="$sandbox/template"
export GIT_ALLOW_PROTOCOL=file GIT_TERMINAL_PROMPT=0
git init -b main "$sandbox/repo"
cd "$sandbox/repo"
git config --local user.name "Study Guide Example"
git config --local user.email learner@example.invalid
git config --local commit.gpgsign false
git config --local tag.gpgsign false
git config --local core.autocrlf false
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
mkdir docs src
printf '%s\n' ok > src/state.txt
printf '%s\n' catalog > docs/guide.txt
git add -- docs/guide.txt src/state.txt
git commit -m "docs: initial catalog"
printf '%s\n' reviewed > docs/guide.txt
git add -- docs/guide.txt
git commit -m "docs: review guide"
printf '%s\n' bad > src/state.txt
git add -- src/state.txt
git commit -m "docs: regression fixture"
git rev-parse --show-toplevel
git log --oneline -3
git status --short
git remote
```

Use solo laboratorio desechable y datos ficticios. Si estado difiere, pare; inspeccione estado y operación antes de abortar o recrear laboratorio. Cierre shell dedicado y elimine solo sandbox anotado mediante gestor de archivos tras revisar contenido.

## Capítulos

<!-- chapters -->
- 01 [Bisect: localizar una regresión](01-bisect/README.es.md)
- 02 [Worktrees: directorios de trabajo paralelos](02-worktree/README.es.md)
- 03 [Submodules: dependencias fijadas por commit](03-submodules/README.es.md)
- 04 [Subtree: integrar contenido de otro origen](04-subtree/README.es.md)
- 05 [Hooks: automatización local y confianza](05-hooks/README.es.md)
- 06 [Rerere: reutilizar resoluciones de conflictos](06-rerere/README.es.md)
- 07 [Sparse checkout: seleccionar archivos de trabajo](07-sparse-checkout/README.es.md)
- 08 [Clones parciales y superficiales](08-partial-and-shallow-clone/README.es.md)
- 09 [Blame y grep: investigar cambios](09-blame-and-grep/README.es.md)
- 10 [Archive y bundle: distribuir snapshots o historial](10-archive-and-bundle/README.es.md)
- 11 [Laboratorio integrado de Git avanzado](11-integrated-advanced-lab/README.es.md)
<!-- /chapters -->

---

<!-- navigation-footer -->
[Anterior](../security/README.es.md) · [Índice](../docs/learning-path.es.md) · [Siguiente](../git-internals/README.es.md)
<!-- /navigation-footer -->
