# YAML y lectura de configuración

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../01-ci-delivery-and-deployment/README.es.md) · [Índice](../README.es.md) · [Siguiente](../03-github-actions/README.es.md)
<!-- /navigation -->

**Nivel:** principiante · **Tiempo estimado:** 30 min

**Requisitos previos:** [GitHub](../../github/README.es.md) · [GitLab](../../gitlab/README.es.md) · [Integración, entrega y despliegue continuos](../01-ci-delivery-and-deployment/README.es.md)

**Objetivo:** Leer mapas, secuencias, escalares y comandos multilínea antes de editar automatización.

## Qué es y por qué

YAML es formato de serialización de datos; plataforma asigna significado a claves. Mapa asocia claves y valores; secuencia usa guiones; escalares representan valores individuales. Indente consistentemente con espacios, nunca tabs para indentación. Use comillas cuando puntuación o tipos implícitos sean ambiguos. Escalar de bloque `|` conserva saltos de línea, mientras `>` pliega muchos saltos en espacios. Claves duplicadas y anidamiento incorrecto son defectos aunque parser permisivo acepte. Versiones/parsers YAML pueden interpretar palabras simples de forma diferente; clave `on` de workflow es válida en GitHub, pero parser YAML 1.1 puede interpretarla como booleano. Archivo sintácticamente válido aún puede violar esquema de plataforma.

```yaml
project:
  name: "catalog"
  attempts: 2
  tasks:
    - check
    - report
  message: |
    First line
    Second line
```

## Práctica

Sin conexión, inspeccione ejemplo neutro abajo. Encuentre mapa, lista, cadena y entero; explique por qué `check` pertenece a `tasks`. Dibuje árbol antes y después de quitar indentación de `tasks` por error. Son solo datos, no configuración CI.

## Errores comunes y seguridad

Nunca pegue secretos en YAML. Valide con esquema de plataforma, no solo parser genérico; no se exige editor externo. Inspeccione diff y corrija indentación en copia desechable.

## Ejercicio y autoevaluación

`project` contiene mapa; `tasks` contiene secuencia; `check` es elemento; `attempts` es entero. Apruebe si distingue sintaxis de semántica de plataforma.

## Referencia rápida

mapping / sequence / scalar

## Fuentes oficiales

- <https://yaml.org/spec/1.2.2/>
- <https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax>
- <https://docs.gitlab.com/ci/yaml/>

---

<!-- navigation-footer -->
[Anterior](../01-ci-delivery-and-deployment/README.es.md) · [Índice](../README.es.md) · [Siguiente](../03-github-actions/README.es.md)
<!-- /navigation-footer -->
