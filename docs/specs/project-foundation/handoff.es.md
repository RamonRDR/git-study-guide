# Entrega Learning Hub

[English](handoff.md) · [Português](handoff.pt-BR.md) · [Español](handoff.es.md)

Esta entrega distingue la revisión inmutable de contenido de la revisión de presentación y futura etiqueta de release. La base siguiente se integró con autorización explícita del mantenedor en PR #21 y pasó CI main y manual. Este documento sigue como candidato a release hasta revisión e integración de PR #22; no activa lock del sitio ni publica release.

## Contenido y procedencia

- [Content revision 03c30438a5490d6c8f9b22dbf457a644658e042f](https://github.com/RamonRDR/git-study-guide/commit/03c30438a5490d6c8f9b22dbf457a644658e042f)
- [Main CI](https://github.com/RamonRDR/git-study-guide/actions/runs/46061260750) · [Manual CI](https://github.com/RamonRDR/git-study-guide/actions/runs/46062482507)
- [Manifest](../../../curriculum/manifest.json) · [Contract](integration-contract.es.md) · [Reference consumer](../../../scripts/learning_hub_consumer.py)
- [ADR 0006](../../adr/0006-browser-playground.md)

```json
{
  "guide_id": "git-study-guide",
  "revision": "03c30438a5490d6c8f9b22dbf457a644658e042f",
  "manifest_version": "1.0.0",
  "assessment_version": 1,
  "command_catalog_version": 1
}
```

El consumidor de referencia recibe un lock externo y un repositorio Git SHA-1 confiable con objetos completos. Use versiones exactas soportadas, nunca ejecute código del snapshot y valide antes de adoptar; conserve el pin anterior aprobado en caso de fallo. Adaptador Git distinto del adaptador Python. Lea contrato de integración y ADR de playground. Proyectos y desafíos nativos son local_only, demás capítulos unverified; no se alega runtime navegador ni despliegue del sitio.

## Validación y release

La base contiene 18 módulos, 141 entradas, 423 rutas localizadas de capítulos, 54 de índices, 120 operaciones y 75 registros de evaluación. Comparación independiente cubre 503 rutas canónicas (manifiesto, registro, índices, capítulos, recursos, bancos, catálogo y esquemas); todas coinciden con la base por ID de blob Git antes de revisión final de presentación. Misma suite de 152 pruebas y nueve validadores aprobados por SO en CI main. CI final de presentación y Codex Review deben pasar; renderizado visual, autorización explícita de squash, CI post-merge y autorización separada de release siguen siendo obligatorios. Sin cambios recíprocos en Python o perfil antes de publicación Git.

- [PR #22](https://github.com/RamonRDR/git-study-guide/pull/22)
- [Identidad visual V1](../../assets/learning-hub/README.es.md)
- [Audit](audit.es.md) · [Tasks](tasks.es.md)
