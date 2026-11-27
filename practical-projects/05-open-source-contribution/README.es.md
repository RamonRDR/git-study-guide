# Contribución de código abierto

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../04-the-lost-commit/README.es.md) · [Índice](../README.es.md) · [Siguiente](../06-automated-quality-pipeline/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 60 min

**Prerrequisitos:** [github/05-forks-and-open-source](../../github/05-forks-and-open-source/README.es.md) · Git 2.40+ · Bash/Git Bash

**Objetivo:** Prepara fork independiente, realiza cambio acotado de documentación en rama feature, revisa diff de upstream/main, publica solo en fork y luego simula mantenedor que obtiene e integra rama revisada en upstream.

## Escenario

Un proyecto de código abierto ficticio tiene upstream y fork de contribuyente. Repositorios bare locales simulan la relación de alojamiento sin cuentas.

## Preparación desechable

Usa solo la sección Preparación desechable de [Mi primer repositorio](../01-my-first-repository/README.es.md). Abre shell Bash/Git Bash dedicada nueva; comprueba raíz impresa, identidades ficticias y ausencia de remotos antes de seguir. No ejecutes desafío 01. Git 2.40+. Ejecuta un comando a la vez, detente ante fallo inesperado y nunca ejecutes en el guía.

## Desafío

Prepara fork independiente, realiza cambio acotado de documentación en rama feature, revisa diff de upstream/main, publica solo en fork y luego simula mantenedor que obtiene e integra rama revisada en upstream. Intenta antes de leer la solución.

## Pistas progresivas

Clona origin bare a otro repositorio bare, luego clona fork normalmente. Usa nombres distintos origin y upstream. Fetch y merge locales no son PR real ni aprobación humana independiente.

## Solución de referencia

Crea base upstream y fork local. En clon contribuyente, comprueba remotos y configura identidad ficticia.

```bash
printf '%s\n' 'status: draft' > notes.txt
git add notes.txt
git commit -m 'docs: initialize notes'
git init --bare -b main "$sandbox/upstream.git"
git remote add origin "$sandbox/upstream.git"
git push -u origin main
git clone --bare "$sandbox/upstream.git" "$sandbox/fork.git"
git clone "$sandbox/fork.git" "$sandbox/contributor"
cd "$sandbox/contributor"
git config user.name 'Study Guide Example'
git config user.email learner@example.invalid
git config commit.gpgsign false
git config core.autocrlf false
git config core.hooksPath "$sandbox/no-hooks"
git remote add upstream "$sandbox/upstream.git"
git remote -v
git fetch upstream
git switch -c feat/clarify-notes
printf '%s\n' 'status: ready' > notes.txt
git add notes.txt
git commit -m 'docs: clarify notes'
git diff --check upstream/main...HEAD
git diff upstream/main...HEAD
git push -u origin feat/clarify-notes
```

Escribe revisión simulada describiendo cambio, evidencia y límites. Cambia rol al clon original; comprueba upstream intacto e inspecciona contribución. En ejercicio offline, elige fast-forward explícitamente tras revisión; no lo confundas con merge de PR alojado.

```bash
cd "$sandbox/repo"
git fetch origin
test "$(git rev-parse HEAD)" = "$(git rev-parse origin/main)"
git remote add contribution "$sandbox/fork.git"
git fetch contribution
git diff --check main...contribution/feat/clarify-notes
git diff main...contribution/feat/clarify-notes
git merge --ff-only contribution/feat/clarify-notes
git push origin main
git show HEAD:notes.txt
git status --porcelain
```

## Criterios de éxito

Rama feature del fork contiene ready y main del fork queda en base draft. Main upstream avanza solo en fase mantenedor y coincide con contribución revisada. Opcional: inspecciona flujo GitHub/GitLab en módulos anteriores; usa solo proyectos propios autorizados, nunca envíes PR no solicitado.

Prueba fija de mantenimiento (no código de estudiante): `tests/test_git_practical_projects.py::test_contribution_offline`.

## Recuperación y limpieza

Si destino difiere de ruta local esperada, detente antes del push. Si revisión o fast-forward falla, inspecciona cambios sin forzar. Conserva rama de contribución hasta verificar trabajo. Cierra la shell dedicada y elimina solo el sandbox impreso verificado mediante gestor de archivos. Conserva antes trabajo deseado.

## Fuentes oficiales

- <https://git-scm.com/docs/git-clone>
- <https://git-scm.com/docs/git-remote>
- <https://git-scm.com/docs/git-fetch>
- <https://git-scm.com/docs/git-diff>
- <https://git-scm.com/docs/git-merge>

---

<!-- navigation-footer -->
[Anterior](../04-the-lost-commit/README.es.md) · [Índice](../README.es.md) · [Siguiente](../06-automated-quality-pipeline/README.es.md)
<!-- /navigation-footer -->
