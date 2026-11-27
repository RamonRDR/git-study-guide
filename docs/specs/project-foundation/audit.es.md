# Auditoría inicial del Sprint 00

[English](audit.md) · [Português](audit.pt-BR.md) · [Español](audit.es.md)

Auditoría de lectura por API GitHub antes de crear rama. Git baseline main b4bd782519ebc8e52e6751362443aa634e86e56d; solo LICENSE y README.md, una rama protegida y ningún PR abierto. Público, MIT, solo squash, auto-merge desactivado, sugerencia de actualizar rama y eliminación tras merge habilitadas. Ruleset 28108699 activo para rama predeterminada, sin bypass, PR y resolución de conversaciones obligatorios, 0 aprobaciones exigidas, historial lineal, eliminación/force push bloqueados, aprobación extra para cambios sin atribución, solo squash. Sin checks obligatorios en ruleset; sin workflow en árbol inicial. No cambiar administración en Sprint 00.

Python baseline main 9102bbbf8f8dd846f2fb9682dd3f55bcacc10c95, público MIT, main protegida y feat/problem-solving-foundations en mismo SHA. Consultados árbol, AGENTS, constitution, specification, plan, tareas, criterios, ADR 0001–0003, orientación de IA, contrato y registro relacionado (representantes en inglés). Encontrados localización, quality-checks.yml, scripts de enlaces, cobertura de idiomas, estructura, ejemplos y navegación. Reutilizar diseño, SDD, proceso de review y contrato fijado por revisión; adaptar runtime específico Python, PEP 8 y pruebas de código a pruebas de estado Git independientes del lenguaje. Sin reejecución de CI Python, auditoría semántica exhaustiva de traducciones ni cambios en Python. Auditoría no afirma que todo currículo de referencia pase.

- [Git baseline](https://github.com/RamonRDR/git-study-guide/commit/b4bd782519ebc8e52e6751362443aa634e86e56d)
- [Ruleset](https://github.com/RamonRDR/git-study-guide/rules/28108699)
- [Python baseline](https://github.com/RamonRDR/python-study-guide/tree/9102bbbf8f8dd846f2fb9682dd3f55bcacc10c95)

## Documentos relacionados

- [Especificación](specification.es.md)
- [Tareas](tasks.es.md)

## QA final Sprint 19B — evidencia de base (en curso)

Base inmutable: [03c3043](https://github.com/RamonRDR/git-study-guide/commit/03c30438a5490d6c8f9b22dbf457a644658e042f). [Cierre Sprint 19A](https://github.com/RamonRDR/git-study-guide/pull/21#issuecomment-7227417357): [CI push](https://github.com/RamonRDR/git-study-guide/actions/runs/46061260750) y [CI manual](https://github.com/RamonRDR/git-study-guide/actions/runs/46062482507) aprobaron nueve validadores y 152 pruebas por SO; tree revisado, padre único, metadatos noreply, firma verificada y eliminación de rama confirmados. Cancelación efectiva de ejecuciones obsoletas de PR aún no ejercitada.

Comprobación independiente de inventario: 637 archivos regulares rastreados; 18 módulos, 141 IDs únicos de capítulos, 423 rutas únicas de capítulos localizados y 54 rutas de índices localizados presentes; sin idiomas ausentes ni discrepancia de secuencia global de navegación; 159 asociaciones de evaluaciones y 312 de comandos. Schema del manifiesto 1.0.0.

Muestreo semántico dirigido de fragmentos de seis capítulos en tres idiomas (18 archivos): primer commit, resolución de conflictos, reset, secretos/prevención de filtraciones, refs y HEAD y El commit perdido. Comparación de explicaciones centrales, condiciones de seguridad y estados esperados; ninguna discrepancia material en los fragmentos muestreados. Contenido de bloques delimitados coincide en los seis conjuntos. No equivale a auditoría semántica completa de traducciones, ejecución de todos los labs, prueba macOS, auditoría de enlaces externos ni validación de runtime navegador.

AC-19 sigue en curso: READMEs finales localizados, identidad aprobada por mantenedor o excepción explícita, badges verídicos, QA aplicable restante y limitaciones, entrega revisada y evidencia inmutable de release aprobada. No crear tag ni publicar todavía. Sin cambios en otros repositorios.
