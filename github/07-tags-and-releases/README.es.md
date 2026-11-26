# Tags y GitHub Releases

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../06-protection-and-rulesets/README.es.md) · [Índice](../README.es.md) · [Siguiente](../08-github-cli/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 30 min

**Requisitos previos:** [Remotos](../../remote-repositories/README.es.md) · [Historial y recuperación](../../history-and-recovery/README.es.md) · [Protección de ramas, rulesets y quality gates](../06-protection-and-rulesets/README.es.md) · [Primer repositorio](../../getting-started/03-first-repository/README.es.md) · [Primer commit](../../getting-started/05-first-commit/README.es.md)

**Objetivo:** Distinguir refs Git de versión de metadatos de release y verificar objetivo.

## Qué y por qué

Tag es ref Git que nombra objeto, normalmente commit. Lightweight apunta directamente; annotated guarda objeto tag con metadatos y mensaje. Ramas normalmente avanzan; tags de release deben permanecer estables. GitHub Release añade notas alojadas, assets descargables y estado draft/prerelease asociado a tag. Publicar release no es despliegue automático. SemVer usa MAJOR.MINOR.PATCH para compatibilidad API pública; v0.1.0 es escritura común de tag de desarrollo inicial, no garantía de estabilidad. Assets de release son separados del historial Git fuente; verifica origen, integridad y permisos antes de usar.

## Práctica

Lab local offline: inicia repo aislado nuevo según lecciones de primer repo y commit de módulo 00. Confirma raíz desechable registrada, main limpia con un commit ficticio, sin remotos, sin tags e identidades efectivas ficticias. Ejecuta individualmente y detente ante salida inesperada. Comandos abajo crean tag anotado local, inspeccionan tipo y comparan commit resuelto con HEAD. Sin push. Redacta release notes con alcance, verificación y límites. Opcional solo lectura: inspecciona release pública y tag, sin descargar ni ejecutar assets.

```text
git rev-parse --show-toplevel
git branch --show-current
git status --short
git remote -v
git tag --list
git rev-list --count HEAD
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Continúa solo si se cumplen todas las precondiciones anteriores.

```text
git tag -a v0.1.0 -m "Release 0.1.0"
git cat-file -t v0.1.0
git rev-parse 'v0.1.0^{commit}' HEAD
git show v0.1.0
git status --short
```


## Errores comunes y seguridad

No muevas ni borres tag de release publicado para alterar artefacto silenciosamente. Publica corrección revisada en nueva versión cuando corresponda. Nunca subas secretos ni binarios sin verificar. Cierra sesión dedicada y borra solo padre desechable registrado si no lo necesitas; no se crea release alojada.

## Ejercicio y autoevaluación

Aprueba si tipo de objeto es tag, IDs de commits resueltos coinciden, main no cambia y explicas por qué notas de release no son commits Git. Si solo en papel, predice salida.

## Referencia rápida

- `git tag -a TAG -m MESSAGE`
- `git cat-file -t TAG`
- `git rev-parse 'TAG^{commit}'`

## Fuentes oficiales

- <https://git-scm.com/docs/git-tag>
- <https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases>
- <https://semver.org/>

---

<!-- navigation-footer -->
[Anterior](../06-protection-and-rulesets/README.es.md) · [Índice](../README.es.md) · [Siguiente](../08-github-cli/README.es.md)
<!-- /navigation-footer -->
