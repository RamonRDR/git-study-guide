# Entrega Learning Hub

[English](handoff.md) · [Português](handoff.pt-BR.md) · [Español](handoff.es.md)

Esta entrega distingue la revisión inmutable de contenido de la revisión de presentación y etiqueta publicada. La base siguiente se integró con autorización explícita del mantenedor en PR #21 y pasó CI main y manual. La entrega fue revisada e integrada en PR #22; v1.0.0 está publicada. Este documento no activa lock del sitio.

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

La base contiene 18 módulos, 141 entradas, 423 rutas localizadas de capítulos, 54 de índices, 120 operaciones y 75 registros de evaluación. Comparación independiente cubre 503 rutas canónicas (manifiesto, registro, índices, capítulos, recursos, bancos, catálogo y esquemas); todas coinciden con la base por ID de blob Git antes de revisión final de presentación. En la revisión de la base, la misma suite de 152 pruebas y nueve validadores fueron aprobados por SO en CI main. La evidencia final de presentación y release consta abajo. No hubo cambios recíprocos en Python o perfil antes de publicación Git.

- [PR #22](https://github.com/RamonRDR/git-study-guide/pull/22)
- [Identidad visual V1](../../assets/learning-hub/README.es.md)
- [Audit](audit.es.md) · [Tasks](tasks.es.md)

## Cierre de Sprint 19B: release oficial v1.0.0

El mantenedor aprobó la Identidad Visual V1, los tres READMEs renderizados en desktop y móvil, enlaces externos y social preview; la confirmación visual fue comunicada por el mantenedor. PR #22 y #23 aprobaron CI en el HEAD exacto, Codex Review y Final Pre-Merge Audit, fueron autorizados explícitamente e integrados por squash. Ambos CI post-merge en main aprobaron 156 pruebas y nueve validadores por SO; no se observaron marcadores de error/aviso. Las 503 rutas canónicas permanecieron intactas. La v1.0.0 estable y latest fue publicada por el mantenedor el 28/11/2026 a las 17:41:35 UTC; la etiqueta apunta directamente a `706105ee5ef51befd2282a143e7deafd256c61a8`. Pin de contenido `03c30438a5490d6c8f9b22dbf457a644658e042f`; revisión de presentación `c26c41fee624a74f7ba7a70ac531063061a6559e`. AC-19 y T19-01 cumplidos; esta documentación post-release reconcilia los registros históricos en curso y no modifica la etiqueta publicada. Limitaciones: revisión semántica por muestreo, sin ejecución exhaustiva de labs de estudiantes ni CI macOS, sin runtime navegador o despliegue del sitio verificados, sin cancelación observada de ejecuciones sustituidas. Enlaces recíprocos con Python y perfil son PR posteriores separados.

- [Release v1.0.0](https://github.com/RamonRDR/git-study-guide/releases/tag/v1.0.0)
- [Final main CI](https://github.com/RamonRDR/git-study-guide/actions/runs/46170822488)
- [PR #22](https://github.com/RamonRDR/git-study-guide/pull/22) · [PR #23](https://github.com/RamonRDR/git-study-guide/pull/23)
