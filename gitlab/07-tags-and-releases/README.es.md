# Tags Git y releases de GitLab

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../06-pipelines-and-runners/README.es.md) · [Índice](../README.es.md) · [Siguiente](../08-gitlab-cli-and-platform-comparison/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 25 min

**Requisitos previos:** [GitHub](../../github/README.es.md) · [Remotos](../../remote-repositories/README.es.md)

**Objetivo:** Distinguir refs de versión de metadatos de publicación y validar revisión prevista.

## Qué es y por qué

Tag Git nombra objeto, normalmente commit; tag ligera referencia objeto directamente, tag anotada añade objeto tag con metadatos y mensaje. Release GitLab asocia tag a notas y assets o enlaces de assets. Tags quedan en Git; notas y adjuntos son metadatos alojados, no incluidos automáticamente en clon. Release profesional identifica commit revisado, resume cambios y describe limitaciones. Tag protegida puede restringir operaciones según configuración; no suponga que protección de rama protege tags. Evite mover tag publicada: consumidores pueden haberla obtenido. Prefiera nueva versión corregida según política de release.

## Práctica

Repita ejercicio local seguro de tags de [tags y releases GitHub](../../github/07-tags-and-releases/README.es.md) en repositorio desechable, sin publicar. Compare `git show v1.0.0` (si existe esa tag) con nota ficticia sobre instalación del catálogo y limitación conocida. Use `git tag --list` para inspeccionar tags antes de elegir una. Opcional: inspeccione release pública existente de GitLab sin descargar ni ejecutar assets. Compare tag y notas; no cree release alojada.

## Errores comunes y seguridad

Nunca publique tag que apunta a commit no revisado ni incluya secretos en notas/assets. Si release referencia commit incorrecto, detenga distribución, avise a mantenedores y siga política de corrección; no reescriba tags públicas silenciosamente.

## Ejercicio y autoevaluación

Apruebe si tag identifica revisión, notas comunican cambios y asset no es confiable solo porque existe release. Ejercicio sin conexión no exige cuenta.

## Fuentes oficiales

- <https://docs.gitlab.com/user/project/releases/>
- <https://git-scm.com/docs/git-tag>

---

<!-- navigation-footer -->
[Anterior](../06-pipelines-and-runners/README.es.md) · [Índice](../README.es.md) · [Siguiente](../08-gitlab-cli-and-platform-comparison/README.es.md)
<!-- /navigation-footer -->
