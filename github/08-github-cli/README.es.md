# GitHub CLI opcional e consulta de solo lectura

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../07-tags-and-releases/README.es.md) · [Índice](../README.es.md) · [Siguiente módulo](../../gitlab/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 25 min

**Requisitos previos:** [Remotos](../../remote-repositories/README.es.md) · [Historial y recuperación](../../history-and-recovery/README.es.md) · [Tags y GitHub Releases](../07-tags-and-releases/README.es.md)

**Objetivo:** Distinguir gh de git e inspeccionar metadatos alojados sin escritura.

## Qué y por qué

GitHub CLI (gh) es cliente opcional de APIs GitHub. git gestiona historial Git local y transporte; gh lee o modifica recursos alojados según autenticación y permisos. Comando terminal puede tener efectos remotos; repo create, issue create, pr merge y release create son escrituras. Usa destinos --repo explícitos y comandos de lectura primero. Navegador o ejercicios en papel bastan; instalar CLI o login no es requerido. Instala solo desde instrucciones oficiales si quieres; autenticación puede usar navegador y almacenamiento aprobado. Tokens del entorno pueden prevalecer sobre credenciales guardadas; nunca muestres valores.

## Práctica

Ejercicio autenticado opcional solo lectura: primero ejecuta gh --version, gh help y gh auth status --hostname github.com en privado. Si autenticación falla, detente o sigue instrucciones oficiales; nunca pegues salida con datos de cuenta. Sustituye OWNER/study-sandbox por identificador real de sandbox autorizado, no placeholder literal. Confirma gh repo view identifica repo deseado antes de listar issues o PRs. Usa navegador si no hay sandbox/cuenta. Sin escrituras, sin mostrar token, sin automatización requerida. Esperado: nombre/visibilidad y listas de issues/PR abiertos accesibles; listas pueden estar vacías.

```text
gh --version
gh help
gh auth status --hostname github.com
```

Confirma cuenta correcta en privado; sustituye placeholder e inspecciona primer resultado antes de ejecutar los otros dos comandos.

```text
gh repo view OWNER/study-sandbox --json nameWithOwner,visibility,defaultBranchRef
gh issue list --repo OWNER/study-sandbox --state open
gh pr list --repo OWNER/study-sandbox --state open
```


## Errores comunes y seguridad

Nunca ejecutes gh auth token ni flags que muestran token para diagnóstico en sesión compartida. No ejecutes comandos de issue no confiable. Cuenta o repo incorrecto: detente antes de escribir. No hace falta logout ni borrar credenciales para limpieza; sigue política normal de cuenta.

## Ejercicio y autoevaluación

Aprueba si clasificas git status como consulta local, gh pr list como consulta alojada y gh pr merge como escritura alojada. Explica por qué listar con éxito no implica permiso merge.

## Referencia rápida

- `gh --version`
- `gh repo view`
- `gh issue list`
- `gh pr list`

## Fuentes oficiales

- <https://cli.github.com/manual/>
- <https://cli.github.com/manual/gh_auth_status>
- <https://cli.github.com/manual/gh_repo_view>
- <https://cli.github.com/manual/gh_issue_list>
- <https://cli.github.com/manual/gh_pr_list>

---

<!-- navigation-footer -->
[Anterior](../07-tags-and-releases/README.es.md) · [Índice](../README.es.md) · [Siguiente módulo](../../gitlab/README.es.md)
<!-- /navigation-footer -->
