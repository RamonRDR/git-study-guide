# Laboratorio de flujo profesional integrado

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../12-release-management/README.es.md) · [Índice](../README.es.md) · [Siguiente módulo](../../security/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 60 min

**Requisitos previos:** [CI/CD](../../ci-cd/README.es.md) · [Gestión de releases](../12-release-management/README.es.md)

**Objetivo:** Verificar flujo local seguro desde especificación hasta tag.

## Qué es y por qué

Lab sin conexión conecta SDD, demostración red/green, rama de funcionalidad, revisión de diff, Conventional Commits, integración y tag anotado local. En ejercicio simplificado, contrato de catálogo permite explícitamente cambiar campo status de draft a ready; suponga capacidad nueva retrocompatible de disponibilidad y release anterior hipotética 1.0.0, por tanto etiqueta ejemplo 1.1.0. No se exige tag anterior. Check verifica una línea exacta, no comportamiento completo. Primer commit representa base, segundo cambio enfocado. Fast-forward elegido en ejercicio local porque main no divergió; PR reales del guía usan squash autorizado. Ningún PR alojado, review, despliegue ni publicación se simula como evento real de plataforma.

## Práctica

Requisitos: Git 2.28+ y Bash con mktemp/grep (Linux, macOS o Git Bash en Windows); use shell normal limpio, nunca repo del guía. Escriba R1/AC1 del capítulo 09 antes de ejecutar. Ejecute bloque en shell desechable; detenga con salida inesperada. Crea directorio temporal, aísla config global/system normal de Git, usa identidad ficticia y deja sandbox para inspección. Esperado: mensaje red, diff staged de una línea, dos commits con main y tag en segundo, PASS final. Registre ruta, checks y límites como PR simulado. Retire sandbox luego con gestor de archivos tras confirmar ruta impresa. Simule revisor y aprobador de release separados; no infiera aprobación real.

```bash
(
  set -eu
  sandbox=$(mktemp -d)
  printf 'Sandbox: %s\n' "$sandbox"
  unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE GIT_COMMON_DIR GIT_CONFIG_PARAMETERS
  export GIT_CONFIG_NOSYSTEM=1 GIT_CONFIG_GLOBAL="$sandbox/global-config" GIT_CONFIG_COUNT=0
  git init -b main "$sandbox/catalog"
  cd "$sandbox/catalog"
  git config user.name 'Catalog Learner'
  git config user.email 'learner@example.invalid'
  git config commit.gpgsign false
  git config tag.gpgsign false
  printf '%s\n' 'status: draft' > catalog.txt
  git add catalog.txt
  git commit -m 'chore: initialize catalog'
  git switch -c feat/ready-catalog
  if grep -Fxq 'status: ready' catalog.txt; then
    exit 1
  else
    test "$?" -eq 1
  fi
  printf '%s\n' 'RED: ready line absent'
  printf '%s\n' 'status: ready' > catalog.txt
  grep -Fxq 'status: ready' catalog.txt
  git diff --check
  git add catalog.txt
  git diff --cached
  git commit -m 'feat: expose catalog readiness'
  git switch main
  test "$(cat catalog.txt)" = 'status: draft'
  git merge --ff-only feat/ready-catalog
  git tag -a v1.1.0 -m 'Release 1.1.0'
  test "$(git rev-parse 'v1.1.0^{commit}')" = "$(git rev-parse HEAD)"
  test -z "$(git status --porcelain)"
  test -z "$(git remote)"
  grep -Fxq 'status: ready' catalog.txt
  git log --oneline --decorate -2
  printf '%s\n' 'PASS: integrated tagged clean revision'
)
```

## Riesgos y recuperación

Sin remote, push, release real ni credenciales. No sustituya ruta real, configure remote ni copie comandos en repo de producción. No es sandbox endurecido contra entorno shell malicioso. Si comando falla, inspeccione repo temporal con status y log; no haga reset ni fuerce merge. Antes de integración, diff solo lectura es práctica de review, no aprobación independiente. Refactor opcional: extraiga check en función en shell desechable aparte y verifique códigos de salida equivalentes; bloque demuestra red/green, no ciclo completo de refactor.

## Ejercicio y autoevaluación

Apruebe si draft inicial no satisface check, ready sí, main no cambia hasta integración, tag resuelve a HEAD, status limpio y sin remote. Explique por qué ejercicio local aprobado no demuestra CI alojada, review formal ni despliegue. Compare versión hipotética con contrato del capítulo 07.

## Referencia rápida

`git status` / `git diff --cached` / `git merge --ff-only` / `git tag -a`

## Fuentes

- <https://git-scm.com/docs/gitworkflows>
- <https://git-scm.com/docs/git-merge>
- <https://git-scm.com/docs/git-tag>
- <https://www.conventionalcommits.org/en/v1.0.0/>
- <https://semver.org/spec/v2.0.0.html>

---

<!-- navigation-footer -->
[Anterior](../12-release-management/README.es.md) · [Índice](../README.es.md) · [Siguiente módulo](../../security/README.es.md)
<!-- /navigation-footer -->
