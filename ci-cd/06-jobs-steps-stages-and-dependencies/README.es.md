# Jobs, steps, stages y dependencias

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../05-runners-and-execution-environments/README.es.md) · [Índice](../README.es.md) · [Siguiente](../07-artifacts-and-cache/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 35 min

**Requisitos previos:** [GitHub](../../github/README.es.md) · [GitLab](../../gitlab/README.es.md) · [Runners y entornos de ejecución](../05-runners-and-execution-environments/README.es.md)

**Objetivo:** Modelar orden de ejecución, propagación de fallos y paralelismo.

## Qué es y por qué

En GitHub Actions, steps del job se ordenan; jobs independientes pueden correr concurrentemente y `needs` declara dependencias. En GitLab, stages imponen orden predeterminado y `needs` describe grafo más directo, permitiendo inicio antes de terminar toda stage anterior. DAG es grafo dirigido acíclico de dependencias. Considere `lint` y `test` independientes; `package` depende de ambos. Ninguna plataforma garantiza orden de jobs solo por orden textual. Dependencia obligatoria fallida normalmente impide trabajo posterior dependiente de éxito; opciones explícitas de fallo/condición pueden cambiarlo. Evite `continue-on-error` o `allow_failure` en checks obligatorios. Matriz es expansión, no declaración de dependencia.

```text
lint ----> package
           ^
           |
test ------+
```

## Práctica

Sin conexión, dibuje grafo abajo. Determine próximos jobs permitidos si lint pasa pero test falla; luego si ambos pasan. Esboce job GitHub con `needs: [lint, test]` y job GitLab con misma clave de dependencia en mapa del job. Son fragmentos para razonar, no configuraciones completas.

## Errores comunes y seguridad

No quite dependencia obligatoria para dejar pipeline verde. Compruebe si archivos previos deben transferirse explícitamente. Diagnostique jobs omitidos y condiciones antes de cambiar controles; no se necesita ejecución.

## Ejercicio y autoevaluación

Package queda bloqueado si test falla y elegible si ambos pasan, sujeto a runner y condiciones. Apruebe si identifica ambas aristas, ausencia de ciclo y jobs paralelos.

## Referencia rápida

`needs` / DAG / stage

## Fuentes oficiales

- <https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax>
- <https://docs.gitlab.com/ci/yaml/needs/>

---

<!-- navigation-footer -->
[Anterior](../05-runners-and-execution-environments/README.es.md) · [Índice](../README.es.md) · [Siguiente](../07-artifacts-and-cache/README.es.md)
<!-- /navigation-footer -->
