# Laboratorio integrado de seguridad

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../12-governance-audit-and-traceability/README.es.md) · [Índice](../README.es.md) · [Siguiente módulo](../../advanced-git/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 50 min

**Requisitos previos:** [Flujos profesionales](../../professional-workflows/README.es.md) · [Gobernanza, auditoría y trazabilidad](../12-governance-audit-and-traceability/README.es.md)

**Objetivo:** Verificar staging local seguro y ensayar respuesta.

## Qué es y por qué

Ejercicio sin conexión usa solo ajustes inocuos, no secretos. Ilustra ignore y staging explícito en repo temporal nuevo. Simulación complementaria ensaya control de acceso e incidentes; no crea credenciales, cambia política alojada, firma commit, despliega ni prueba incidente real. Use Git 2.28+ y Bash (Linux/macOS o Git Bash en Windows), shell normal limpio. Bloque aísla configuración system/global normal y deja sandbox impreso para inspección posterior; no es frontera endurecida contra ambiente malicioso.

## Práctica

Antes de ejecutar, prediga `local-settings.txt` ignorado y `.gitignore` más `settings.example.txt` staged. Ejecute bloque entero abajo solo en shell desechable. Esperado: check ignore imprime nombre local, nombres staged enumeran exactamente dos archivos públicos y PASS. Luego simule exposición hipotética sin valor de credencial: elija revocación, notificación, evaluación y corrección; redacte matriz de acceso y control del catálogo ficticio. No se necesita remote.

```bash
(
  set -eu
  sandbox=$(mktemp -d)
  printf 'Sandbox: %s\n' "$sandbox"
  unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE GIT_COMMON_DIR GIT_CONFIG_PARAMETERS
  export GIT_CONFIG_NOSYSTEM=1 GIT_CONFIG_GLOBAL="$sandbox/global-config" GIT_CONFIG_COUNT=0
  git init -b main "$sandbox/catalog"
  cd "$sandbox/catalog"
  printf '%s\n' 'local-settings.txt' > .gitignore
  printf '%s\n' 'mode=local' > local-settings.txt
  printf '%s\n' 'mode=example' > settings.example.txt
  git check-ignore -- local-settings.txt
  git add -- .gitignore settings.example.txt
  test -z "$(git ls-files -- local-settings.txt)"
  test "$(git ls-files -- settings.example.txt)" = 'settings.example.txt'
  git diff --cached --check
  git diff --cached --name-only
  test -z "$(git remote)"
  printf '%s\n' 'PASS: local file ignored, template staged, no remote'
)
```

## Riesgos y recuperación

No sustituya por proyecto real o archivo de credenciales. Si comando falla, detenga e inspeccione sandbox impreso con status/diff de solo lectura. Retire mediante gestor de archivos solo tras confirmar ruta exacta. Checks de nombres exitosos no prueban ausencia de secretos en contenido; proyectos reales también requieren review de contenido y scanning adecuado.

## Ejercicio y autoevaluación

Apruebe si archivo local no rastreado, plantilla staged, sin remote y respuesta simulada prioriza revocación antes de limpiar historial. Explique lo no probado: credenciales reales, imposición de plataforma, firma, CI alojada y despliegue.

## Referencia rápida

`git check-ignore` / `git add --` / `git diff --cached`

## Referencias

- <https://git-scm.com/docs/gitignore>
- <https://git-scm.com/docs/git-check-ignore>
- <https://git-scm.com/docs/git-ls-files>
- <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository>

---

<!-- navigation-footer -->
[Anterior](../12-governance-audit-and-traceability/README.es.md) · [Índice](../README.es.md) · [Siguiente módulo](../../advanced-git/README.es.md)
<!-- /navigation-footer -->
