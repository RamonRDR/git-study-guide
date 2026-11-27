# ADR 0006: Playground Git opcional en navegador

[English](0006-browser-playground.md) · [Português](0006-browser-playground.pt-BR.md) · [Español](0006-browser-playground.es.md)

Estado: propuesta en Sprint 18, evaluación documental el 27/11/2026; adopción runtime aplazada.

## Decisión

Mantener proyectos prácticos y desafíos nativos local_only. Otros capítulos siguen unverified. Ninguna capacidad browser_compatible, paquete, proxy público, servidor, versión runtime ni despliegue aprobado. Herramienta navegador opcional no sustituye referencia Git nativa ni es requisito de ruta.

## Alternativas

| Alternativa | Evidencia y límites | Decisión |
| --- | --- | --- |
| Git nativo en repos locales desechables | Pruebas Linux/Windows existentes cubren index, refs, conflictos, reflog, orígenes bare y recuperación reales. Sin UI navegador; estudiante instala Git. | Referencia |
| isomorphic-git | Implementación Git JavaScript con adaptadores filesystem/HTTP navegador; APIs documentadas add, commit, branch, checkout, merge, cherry-pick, stash y tag. CLI no sustituye CLI Git nativa; CORS y durabilidad filesystem limitan. Flags, semántica de estado y paridad conflicto/recuperación no verificadas. | Solo candidato |
| wasm-git | libgit2 compilada con Emscripten; builds navegador documentados incluyen worker y variantes filesystem persistente. CORS, requisitos almacenamiento/navegador por build e implementación distinta de CLI Git limitan fidelidad. OPFS pthreads exige cabeceras aislamiento cross-origin. | Solo candidato |
| Simulador educativo | Puede modelar pequeña máquina de estados sin afirmar Git nativo; requiere reglas originales explícitas, rótulo simulación y fixtures comparación nativa. | Exploración futura opcional |
| Shell Git arbitrario alojado | Introduce aislamiento ejecución, riesgo red/seguridad y costo recurrente incierto. | Rechazado |

## Gates de prototipo antes de cambiar capacidad

- Fijar versiones exactas paquete/runtime, licencias dependencias y hashes integridad. Empaquetar assets estáticos sin cuentas obligatorias, proxies CORS públicos, infraestructura pagada ni API por visitante. Verificar límites reales alojamiento/ancho de banda antes de aprobación.
- Empezar fixture pequeña desechable offline y operaciones tipadas permitidas (init, status, add, commit, branch/checkout, diff). Comparar bytes working/index/HEAD y grafo/estado con Git nativo; ampliar solo tras probar conflictos, stash, revert, squash, reflog, etiquetas y simulación bare-remoto local. Nunca inferir soporte por nombres de API. Operaciones no admitidas quedan local_only.
- Separar orígenes sitio/runtime donde sea necesario; CSP y mensajería restringida, sin credenciales, shell arbitrario, red irrestricta ni acceso repos valiosos. Web Worker mejora respuesta pero solo no es frontera de seguridad. Inspeccionar cadena suministro y aislamiento origen.
- Límites propuestos para prueba, no garantías medidas: 5 s por operación, 64 KiB salida, 5 MiB fixture, 100 operaciones por sesión. Cancelar/terminar y recrear workers; sin afirmar aislamiento duro memoria navegador. Probar cuota, crash/reload, limpieza/reset; almacenamiento puede descartarse, orientar exportación/reinicio y persistencia opt-in explícita.
- Verificar teclado, lector pantalla, errores localizados, contraste, foco, diseño móvil, movimiento reducido y Chrome/Edge/Firefox/Safari en dispositivos objetivo. Probar offline, versiones fijadas, bloqueo CORS/red, reset, límites tiempo/salida y recuperación. Documentar resultados reales por ejercicio antes de marcar browser_compatible en versión futura.

## Consecuencias

Ningún costo o dependencia nueva aquí. Sin prueba real runtime/navegador ni afirmación compatibilidad; evaluación documental, no benchmark. Prototipo futuro en sitio requiere autorización aparte, fidelidad medida, revisión seguridad/accesibilidad y confirmación costo adicional cero. Labs locales siguen completos sin él.

## Fuentes consultadas

- <https://github.com/isomorphic-git/isomorphic-git/blob/main/README.md>
- <https://isomorphic-git.org/docs/en/quickstart>
- <https://github.com/petersalomonsen/wasm-git/blob/master/README.md>
- <https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers>
- <https://developer.mozilla.org/en-US/docs/Web/API/Storage_API/Storage_quotas_and_eviction_criteria>
- <https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Same-origin_policy>
- <https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/sandbox>

- [Integration contract](../specs/project-foundation/integration-contract.es.md)
- [ADR index](README.es.md)
