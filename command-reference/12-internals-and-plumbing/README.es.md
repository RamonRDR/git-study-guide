# 12 Internals y plumbing

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../11-advanced-git-operations/README.es.md) · [Índice](../README.es.md) · [Siguiente](../13-security-and-maintenance/README.es.md)
<!-- /navigation -->

Generado a partir del JSON canónico. Edita los registros, no esta página.

Las entradas describen comandos y operaciones, no una secuencia para ejecutar. Practica en repositorios desechables. Las operaciones alojadas son opcionales.

**Total de entradas distintas: 8**

- [`git cat-file -t`](#git-cat-file-type)
- [`git cat-file -p`](#git-cat-file-pretty)
- [`git hash-object`](#git-hash-object)
- [`git ls-tree`](#git-ls-tree)
- [`git rev-list`](#git-rev-list)
- [`git symbolic-ref HEAD`](#git-symbolic-ref-read)
- [`git for-each-ref`](#git-for-each-ref)
- [`git ls-files --stage`](#git-ls-files-stage)

## git-cat-file-type

**`git cat-file -t`**

**Tipo:** Uso de opción

**Nivel:** Avanzado

**Buscar por intención:** Inspeccionar objetos Git

**Riesgo:** Solo lectura. Solo lectura en formas mostradas en repositorio local completo; no divulgues rutas, contenido de objetos o metadatos sensibles.

**Finalidad:** Identificar tipo de objeto Git existente.

**Requisitos previos:** Usa repositorio propio desechable con objetos indicados existentes y configuración local confiable. Comprueba repositorio antes de los comandos.

**Opciones:** -t muestra tipo de objeto; -s informa tamaño; usa nombre de objeto resoluble.

**Cuándo utilizar:** Al distinguir blobs, trees, commits y objetos de etiquetas anotadas antes de inspeccionar.

**Cuándo evitar:** No uses ID de objeto ambiguo o supuesto, ni esperes que tipo pruebe integridad del contenido.

**Sintaxis**

`git cat-file -t HEAD`

**Ejemplo básico**

`git cat-file -t HEAD`

Identifica tipo del objeto nombrado por HEAD.

**Ejemplo profesional**

`git cat-file -t HEAD:notes.txt`

Identifica blob de archivo ordinario existente en commit.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Muestra tipo de objeto, como commit, tree, blob o tag, o informa fallo de resolución.

**Efectos y efectos secundarios:** En laboratorio local completo, inspección mostrada no escribe objetos, cambia referencias, edita archivos ni actualiza index. Clones parciales pueden obtener objetos ausentes.

**Errores comunes:** Suponer que toda etiqueta apunta a objeto tag; etiquetas ligeras nombran otros objetos directamente.

**Alternativas:** Usa git cat-file -p para inspeccionar contenido del objeto resuelto, o git fsck para comprobar integridad.

**Recuperación:** No es necesario deshacer inspección mostrada. Si salida inesperada, verifica objeto, referencia, rango de revisiones o ruta e inspecciona errores antes de continuar.

**Versión y dependencias:** Sintaxis estándar Git; usa Git 2.40 o superior en laboratorios. IDs de objetos dependen del formato de objetos del repositorio.

**Capítulos relacionados**

- [git-internals/01-object-database](../../git-internals/01-object-database/README.es.md)
- [git-internals/10-porcelain-and-plumbing](../../git-internals/10-porcelain-and-plumbing/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-cat-file>

## git-cat-file-pretty

**`git cat-file -p`**

**Tipo:** Uso de opción

**Nivel:** Avanzado

**Buscar por intención:** Inspeccionar objetos Git, Inspeccionar historial

**Riesgo:** Solo lectura. Solo lectura en formas mostradas en repositorio local completo; no divulgues rutas, contenido de objetos o metadatos sensibles.

**Finalidad:** Mostrar contenido de objeto en forma adecuada a su tipo.

**Requisitos previos:** Usa repositorio propio desechable con objetos indicados existentes y configuración local confiable. Comprueba repositorio antes de los comandos.

**Opciones:** -p muestra según tipo de objeto; usa -t antes si tipo incierto.

**Cuándo utilizar:** Al examinar estructura almacenada de objeto en vez de resumen formateado de cambios.

**Cuándo evitar:** Evita volcar blobs binarios desconocidos a terminal o publicar contenido histórico sensible.

**Sintaxis**

`git cat-file -p HEAD`

**Ejemplo básico**

`git cat-file -p HEAD`

Inspecciona metadatos del commit e IDs de tree y padres.

**Ejemplo profesional**

`git cat-file -p HEAD:notes.txt`

Lee blob de texto confirmado tras comprobar ruta y tipo.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Muestra cabeceras y mensaje de commit, entradas de tree formateadas, bytes de blob o contenido de tag según corresponda.

**Efectos y efectos secundarios:** En laboratorio local completo, inspección mostrada no escribe objetos, cambia referencias, edita archivos ni actualiza index. Clones parciales pueden obtener objetos ausentes.

**Errores comunes:** Confundir IDs de padres de commit almacenado con diff o suponer salida de blob incluye nombres de archivos.

**Alternativas:** Usa git show para revisión humana de commit o git ls-tree para listados estructurados de tree.

**Recuperación:** No es necesario deshacer inspección mostrada. Si salida inesperada, verifica objeto, referencia, rango de revisiones o ruta e inspecciona errores antes de continuar.

**Versión y dependencias:** Sintaxis estándar Git; usa Git 2.40 o superior en laboratorios. IDs de objetos dependen del formato de objetos del repositorio.

**Capítulos relacionados**

- [git-internals/02-blobs-and-trees](../../git-internals/02-blobs-and-trees/README.es.md)
- [git-internals/03-commits-and-tags](../../git-internals/03-commits-and-tags/README.es.md)
- [git-internals/10-porcelain-and-plumbing](../../git-internals/10-porcelain-and-plumbing/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-cat-file>

## git-hash-object

**`git hash-object`**

**Tipo:** Comando nativo

**Nivel:** Avanzado

**Buscar por intención:** Inspeccionar objetos Git

**Riesgo:** Solo lectura. Solo lectura en formas mostradas en repositorio local completo; no divulgues rutas, contenido de objetos o metadatos sensibles.

**Finalidad:** Calcular ID de objeto para contenido suministrado sin almacenarlo por defecto.

**Requisitos previos:** Usa repositorio propio desechable con objetos indicados existentes y configuración local confiable. Comprueba repositorio antes de los comandos.

**Opciones:** --no-filters calcula hash de entrada bruta sin filtros de ruta; -w escribe objeto y no se usa en ejemplos; -t selecciona tipo de objeto.

**Cuándo utilizar:** Al estudiar direccionamiento por contenido o comparar archivo bruto con ID de blob almacenado.

**Cuándo evitar:** No supongas ID como checksum simple del archivo u operación predeterminada preparando archivo.

**Sintaxis**

`git hash-object --no-filters notes.txt`

**Ejemplo básico**

`git hash-object --no-filters notes.txt`

Calcula ID de blob de archivo bruto sin escribirlo.

**Ejemplo profesional**

`git hash-object --no-filters docs/notes.txt`

Compara ID calculado de blob bruto con blob almacenado esperado, teniendo en cuenta filtros.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Muestra ID calculado usando estructura de objeto Git y formato de hash del repositorio; no se escribe objeto en formas mostradas.

**Efectos y efectos secundarios:** Formas mostradas leen entrada y calculan ID sin escribir objeto; -w es elección separada que cambia estado.

**Errores comunes:** Comparar con checksum SHA ordinario sin considerar cabecera de objeto Git, filtros o algoritmo de hash.

**Alternativas:** Usa git rev-parse HEAD:path para localizar blob confirmado existente, o git add para staging intencional.

**Recuperación:** No es necesario deshacer inspección mostrada. Si salida inesperada, verifica objeto, referencia, rango de revisiones o ruta e inspecciona errores antes de continuar.

**Versión y dependencias:** Sintaxis estándar Git; usa Git 2.40 o superior en laboratorios. IDs de objetos dependen del formato de objetos del repositorio.

**Capítulos relacionados**

- [git-internals/04-object-hashes](../../git-internals/04-object-hashes/README.es.md)
- [git-internals/02-blobs-and-trees](../../git-internals/02-blobs-and-trees/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-hash-object>

## git-ls-tree

**`git ls-tree`**

**Tipo:** Comando nativo

**Nivel:** Avanzado

**Buscar por intención:** Inspeccionar objetos Git, Inspeccionar archivos

**Riesgo:** Solo lectura. Solo lectura en formas mostradas en repositorio local completo; no divulgues rutas, contenido de objetos o metadatos sensibles.

**Finalidad:** Listar entradas de tree confirmada seleccionada con modos, tipos, IDs y rutas.

**Requisitos previos:** Usa repositorio propio desechable con objetos indicados existentes y configuración local confiable. Comprueba repositorio antes de los comandos.

**Opciones:** -r recorre subtrees; -z usa salida terminada en NUL para análisis; --name-only selecciona rutas.

**Cuándo utilizar:** Al inspeccionar instantánea histórica independientemente de archivos actuales.

**Cuándo evitar:** No uses como prueba de que working tree coincide con commit o incluye archivos no rastreados.

**Sintaxis**

`git ls-tree HEAD`

**Ejemplo básico**

`git ls-tree HEAD`

Lista entradas de tree raíz del commit actual.

**Ejemplo profesional**

`git ls-tree -r HEAD -- docs/`

Inspecciona entradas confirmadas recursivamente bajo directorio nombrado.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Muestra entradas de tree seleccionada y referencias de objetos; no hay checkout.

**Efectos y efectos secundarios:** En laboratorio local completo, inspección mostrada no escribe objetos, cambia referencias, edita archivos ni actualiza index. Clones parciales pueden obtener objetos ausentes.

**Errores comunes:** Confundir modos ejecutable y gitlink almacenados con permisos completos del sistema operativo.

**Alternativas:** Usa git ls-files --stage para contenido de index o git status para estado de trabajo.

**Recuperación:** No es necesario deshacer inspección mostrada. Si salida inesperada, verifica objeto, referencia, rango de revisiones o ruta e inspecciona errores antes de continuar.

**Versión y dependencias:** Sintaxis estándar Git; usa Git 2.40 o superior en laboratorios. IDs de objetos dependen del formato de objetos del repositorio.

**Capítulos relacionados**

- [git-internals/02-blobs-and-trees](../../git-internals/02-blobs-and-trees/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-ls-tree>

## git-rev-list

**`git rev-list`**

**Tipo:** Comando nativo

**Nivel:** Avanzado

**Buscar por intención:** Inspeccionar historial, Inspeccionar objetos Git

**Riesgo:** Solo lectura. Solo lectura en formas mostradas en repositorio local completo; no divulgues rutas, contenido de objetos o metadatos sensibles.

**Finalidad:** Enumerar alcanzabilidad de commits o recuentos para conjuntos de revisiones especificados.

**Requisitos previos:** Usa repositorio propio desechable con objetos indicados existentes y configuración local confiable. Comprueba repositorio antes de los comandos.

**Opciones:** --count informa recuento; --left-right distingue lados de diferencia simétrica; --objects incluye recorrido de objetos.

**Cuándo utilizar:** Al automatizar recuentos de ascendencia o inspeccionar divergencia de referencias conocidas.

**Cuándo evitar:** No trates recuentos iguales como contenido de archivos equivalente ni supongas historial superficial completo.

**Sintaxis**

`git rev-list --count HEAD`

**Ejemplo básico**

`git rev-list --count HEAD`

Cuenta commits alcanzables desde HEAD actual.

**Ejemplo profesional**

`git rev-list --left-right --count main...feature`

Compara commits alcanzables exclusivos de cada rama local verificada.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Devuelve IDs o recuentos para conjunto de alcanzabilidad solicitado; en ejemplo bilateral los recuentos representan commits exclusivos de cada lado.

**Efectos y efectos secundarios:** En laboratorio local completo, inspección mostrada no escribe objetos, cambia referencias, edita archivos ni actualiza index. Clones parciales pueden obtener objetos ausentes.

**Errores comunes:** Confundir A..B con A...B o comparar recuentos de commits en vez de instantáneas.

**Alternativas:** Usa git log para historial humano o git diff para comparar contenido de instantáneas.

**Recuperación:** No es necesario deshacer inspección mostrada. Si salida inesperada, verifica objeto, referencia, rango de revisiones o ruta e inspecciona errores antes de continuar.

**Versión y dependencias:** Sintaxis estándar Git; usa Git 2.40 o superior en laboratorios. IDs de objetos dependen del formato de objetos del repositorio.

**Capítulos relacionados**

- [git-internals/03-commits-and-tags](../../git-internals/03-commits-and-tags/README.es.md)
- [git-internals/09-reflogs-and-reachability](../../git-internals/09-reflogs-and-reachability/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-rev-list>

## git-symbolic-ref-read

**`git symbolic-ref HEAD`**

**Tipo:** Uso de opción

**Nivel:** Avanzado

**Buscar por intención:** Inspeccionar referencias, Inspeccionar estado del repositorio

**Riesgo:** Solo lectura. Solo lectura en formas mostradas en repositorio local completo; no divulgues rutas, contenido de objetos o metadatos sensibles.

**Finalidad:** Leer destino de referencia simbólica, aquí HEAD.

**Requisitos previos:** Usa repositorio propio desechable con objetos indicados existentes y configuración local confiable. Comprueba repositorio antes de los comandos.

**Opciones:** --short abrevia nombre de referencia; --quiet suprime error para referencia no simbólica manteniendo estado 1; suministrar nuevo destino es forma separada de escritura.

**Cuándo utilizar:** Al determinar si HEAD está asociado a rama nombrada.

**Cuándo evitar:** Evita forma de escritura para cambio ordinario; no realiza checkout normal.

**Sintaxis**

`git symbolic-ref HEAD`

**Ejemplo básico**

`git symbolic-ref HEAD`

Inspecciona referencia seleccionada por HEAD asociado.

**Ejemplo profesional**

`git symbolic-ref --quiet --short HEAD`

Comprueba asociación de rama en script; gestiona código de salida de HEAD separado.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Muestra destino simbólico cuando asociado; HEAD separado causa resultado no cero.

**Efectos y efectos secundarios:** En laboratorio local completo, inspección mostrada no escribe objetos, cambia referencias, edita archivos ni actualiza index. Clones parciales pueden obtener objetos ausentes.

**Errores comunes:** Suponer que symbolic-ref devuelve ID de commit o que cambiar HEAD manualmente actualiza archivos.

**Alternativas:** Usa git branch --show-current para nombre de rama o git rev-parse HEAD para ID de commit.

**Recuperación:** No es necesario deshacer inspección mostrada. Si salida inesperada, verifica objeto, referencia, rango de revisiones o ruta e inspecciona errores antes de continuar.

**Versión y dependencias:** Sintaxis estándar Git; usa Git 2.40 o superior en laboratorios. IDs de objetos dependen del formato de objetos del repositorio.

**Capítulos relacionados**

- [git-internals/05-refs-and-head](../../git-internals/05-refs-and-head/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-symbolic-ref>

## git-for-each-ref

**`git for-each-ref`**

**Tipo:** Comando nativo

**Nivel:** Avanzado

**Buscar por intención:** Inspeccionar referencias, Automatizar flujo

**Riesgo:** Solo lectura. Solo lectura en formas mostradas en repositorio local completo; no divulgues rutas, contenido de objetos o metadatos sensibles.

**Finalidad:** Enumerar referencias con formato y orden configurables.

**Requisitos previos:** Usa repositorio propio desechable con objetos indicados existentes y configuración local confiable. Comprueba repositorio antes de los comandos.

**Opciones:** --format selecciona campos; --sort ordena resultados; patrones de referencia limitan espacio de nombres.

**Cuándo utilizar:** Al producir inventarios estructurados de referencias locales para revisión o automatización.

**Cuándo evitar:** No supongas referencias locales de seguimiento reflejan estado actual del servidor ni uses salida no validada como código shell.

**Sintaxis**

`git for-each-ref --format='%(refname) %(objectname)' refs/heads/`

**Ejemplo básico**

`git for-each-ref --format='%(refname) %(objectname)' refs/heads/`

Lista nombres e IDs de referencias de ramas locales.

**Ejemplo profesional**

`git for-each-ref --sort=-committerdate --format='%(refname:short)' refs/heads/`

Inspecciona nombres de ramas locales ordenados por fecha del committer de punta.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Muestra registros formateados de referencias locales coincidentes; no hay modificación de referencia.

**Efectos y efectos secundarios:** En laboratorio local completo, inspección mostrada no escribe objetos, cambia referencias, edita archivos ni actualiza index. Clones parciales pueden obtener objetos ausentes.

**Errores comunes:** Confundir nombres de referencias con ramas seleccionadas o interpretar fecha de committer como creación de rama.

**Alternativas:** Usa git show-ref para listado simple de nombre e ID o git branch para inspección orientada a ramas.

**Recuperación:** No es necesario deshacer inspección mostrada. Si salida inesperada, verifica objeto, referencia, rango de revisiones o ruta e inspecciona errores antes de continuar.

**Versión y dependencias:** Sintaxis estándar Git; usa Git 2.40 o superior en laboratorios. IDs de objetos dependen del formato de objetos del repositorio.

**Capítulos relacionados**

- [git-internals/05-refs-and-head](../../git-internals/05-refs-and-head/README.es.md)
- [git-internals/10-porcelain-and-plumbing](../../git-internals/10-porcelain-and-plumbing/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-for-each-ref>

## git-ls-files-stage

**`git ls-files --stage`**

**Tipo:** Uso de opción

**Nivel:** Avanzado

**Buscar por intención:** Inspeccionar internals del index, Inspeccionar objetos Git

**Riesgo:** Solo lectura. Solo lectura en formas mostradas en repositorio local completo; no divulgues rutas, contenido de objetos o metadatos sensibles.

**Finalidad:** Inspeccionar entradas de index con modo, ID de objeto, etapa y ruta.

**Requisitos previos:** Usa repositorio propio desechable con objetos indicados existentes y configuración local confiable. Comprueba repositorio antes de los comandos.

**Opciones:** --stage o -s muestra metadatos de entrada; -z es útil para análisis robusto de rutas.

**Cuándo utilizar:** Al estudiar instantánea preparada, gitlinks o etapas de conflicto.

**Cuándo evitar:** No interpretes index como última instantánea confirmada o como todos archivos de directorio de trabajo.

**Sintaxis**

`git ls-files --stage -- notes.txt`

**Ejemplo básico**

`git ls-files --stage -- notes.txt`

Inspecciona entrada de index para archivo de práctica existente.

**Ejemplo profesional**

`git ls-files --stage`

Inspecciona modos preparados, IDs de objetos y etapas de conflicto en repositorio desechable.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Muestra entradas incluyendo etapa 0 para rutas ordinarias fusionadas y etapas mayores para conflictos no resueltos cuando existen.

**Efectos y efectos secundarios:** En laboratorio local completo, inspección mostrada no escribe objetos, cambia referencias, edita archivos ni actualiza index. Clones parciales pueden obtener objetos ausentes.

**Errores comunes:** Suponer etapa 0 significa ausencia de cambios no preparados o gitlink es blob de archivo ordinario.

**Alternativas:** Usa git ls-tree HEAD para comparar entradas confirmadas de tree, o git ls-files --unmerged para aislar conflictos.

**Recuperación:** No es necesario deshacer inspección mostrada. Si salida inesperada, verifica objeto, referencia, rango de revisiones o ruta e inspecciona errores antes de continuar.

**Versión y dependencias:** Sintaxis estándar Git; usa Git 2.40 o superior en laboratorios. IDs de objetos dependen del formato de objetos del repositorio.

**Capítulos relacionados**

- [git-internals/06-index-internals](../../git-internals/06-index-internals/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-ls-files>


---

<!-- navigation-footer -->
[Anterior](../11-advanced-git-operations/README.es.md) · [Índice](../README.es.md) · [Siguiente](../13-security-and-maintenance/README.es.md)
<!-- /navigation-footer -->
