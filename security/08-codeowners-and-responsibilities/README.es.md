# CODEOWNERS y responsabilidades

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../07-branch-protection-and-rulesets/README.es.md) · [Índice](../README.es.md) · [Siguiente](../09-commit-and-tag-signing/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 35 min

**Requisitos previos:** [Flujos profesionales](../../professional-workflows/README.es.md) · [Protección de ramas y rulesets](../07-branch-protection-and-rulesets/README.es.md)

**Objetivo:** Explicar patrones de ownership e imposición de review.

## Qué es y por qué

CODEOWNERS asocia patrones de archivos a revisores responsables en plataformas. Git no impone. GitHub busca `.github/CODEOWNERS`, `CODEOWNERS` raíz, luego `docs/CODEOWNERS`, usando primero encontrado en base del PR; patrón coincidente posterior prevalece. Owners GitHub necesitan escritura; solicitud de review no es aprobación obligatoria salvo protección. GitLab tiene ubicaciones, sintaxis, secciones y reglas propias; aprobación depende de protección y disponibilidad. Proteja reglas de propiedad contra cambios no autorizados. Patrones y equipos abajo son solo documentación.

## Práctica

Para patrones ficticios estilo GitHub abajo, elija responsables de `docs/guide.md`, `.github/workflows/quality.yml` y `.github/CODEOWNERS`. Explique por qué solicitud de review sola no impone control; compruebe política real. No cree equipos ni CODEOWNERS en guía.

```text
* @fictional-org/maintainers
/docs/ @fictional-org/docs
/.github/workflows/ @fictional-org/security
/.github/CODEOWNERS @fictional-org/security
```

## Riesgos y recuperación

Evite copiar ejemplo a repo real: handles ficticios no resuelven. Valide orden, acceso y reglas impuestas con mantenedores autorizados; no suponga GitLab con comportamiento idéntico.

## Ejercicio y autoevaluación

Docs: equipo docs; workflow: seguridad; archivo ownership: seguridad. Aprobación obligatoria es política configurada aparte.

## Referencia rápida

CODEOWNERS / pattern / owner / required review

## Referencias

- <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners>
- <https://docs.gitlab.com/user/project/codeowners/>
