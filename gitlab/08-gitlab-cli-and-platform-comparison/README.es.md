# CLI GitLab opcional y comparación de plataformas

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../07-tags-and-releases/README.es.md) · [Índice](../README.es.md) · —
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 30 min

**Requisitos previos:** [GitHub](../../github/README.es.md) · [Remotos](../../remote-repositories/README.es.md)

**Objetivo:** Elegir Git nativo o CLI alojada y mapear conceptos de colaboración sin suponer paridad.

## Qué es y por qué

`git` manipula objetos y refs Git; `glab` es CLI separada de GitLab para recursos de plataforma vía APIs de red; `gh` es CLI análoga de GitHub. CLI GitLab puede trabajar con GitLab.com y hosts Self-Managed configurados; confirme host y cuenta antes de consultas. Con CLI ya instalada, `glab --version` y `glab --help` inspeccionan herramienta local; `glab auth status` comprueba estado de autenticación; `glab mr list`, `glab issue list` y `glab release list` consultan proyecto seleccionado. No crean ni integran recursos. Para acceso autenticado siga documentación oficial de instalación/autenticación, use almacén seguro de credenciales cuando se soporte y evite exponer credenciales o datos de cuenta. Disponibilidad, permisos API y flags pueden variar por versión.

## Práctica

Sin conexión mapee pares: repositorio GitHub ↔ proyecto GitLab (contiene repositorio); organización/equipo ↔ grupo/subgrupo (modelos de permisos distintos); pull request ↔ merge request; workflow GitHub Actions ↔ pipeline GitLab CI/CD; branch protection/ruleset ↔ rama protegida/branch rule; `gh` ↔ `glab`. Ambos usan Git nativo para commits, ramas, tags y clones. Elija Git para inspeccionar historial, GitLab para listar MRs y plataforma adecuada para política de equipo. Opcional: use CLI autorizada existente en sandbox propio, verifique `git remote -v` localmente sin compartir salida e inspeccione `glab --help`; ejecute comandos de listado solo si host/proyecto correctos y autenticación confirmados. No se exige login, instalación u operación alojada.

## Errores comunes y seguridad

No traduzca comandos CLI a ciegas ni prometa paridad. Planes gratuitos permiten colaboración básica, pero aprobación obligatoria, cuotas y gobernanza avanzada difieren por modalidad, plan, versión y configuración. Si consulta falla, compruebe ayuda, host y acceso antes de repetir; no amplíe credenciales ni use comando de escritura como alternativa.

## Ejercicio y autoevaluación

¿Qué herramienta lista MRs alojadas: `git log` o `glab mr list`? `glab mr list`. Apruebe si explica los seis mapeos como analogías, no equivalencias exactas, y ninguna actividad pagada o autenticada es necesaria.

## Fuentes oficiales

- <https://docs.gitlab.com/cli/>
- <https://docs.gitlab.com/cli/authentication/>
- <https://docs.gitlab.com/cli/mr/list/>
- <https://docs.gitlab.com/cli/issue/list/>
- <https://docs.gitlab.com/cli/release/list/>
- <https://docs.github.com/en/github-cli/github-cli/about-github-cli>
