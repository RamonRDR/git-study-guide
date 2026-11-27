# 01 Inicio y configuración

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Módulo anterior](../../git-internals/README.es.md) · [Índice](../README.es.md) · [Siguiente](../02-repository-inspection/README.es.md)
<!-- /navigation -->

Generado a partir del JSON canónico. Edita los registros, no esta página.

Las entradas describen comandos y operaciones, no una secuencia para ejecutar. Practica en repositorios desechables. Las operaciones alojadas son opcionales.

**Total de entradas distintas: 8**

- [`git --version`](#git-version)
- [`git help`](#git-help)
- [`git init`](#git-init)
- [`git init --bare`](#git-init-bare)
- [`git config --local`](#git-config-local)
- [`git config --global`](#git-config-global)
- [`git config --list --show-origin`](#git-config-show-origin)
- [`git config --get`](#git-config-get)

## git-version

**`git --version`**

**Tipo:** Uso de opción

**Nivel:** Principiante

**Buscar por intención:** Comprobar versión de Git, Configurar Git

**Riesgo:** Solo lectura. No cambia el repositorio; la versión por sí sola no garantiza el comportamiento.

**Finalidad:** Identificar el ejecutable de Git instalado y la versión indicada.

**Requisitos previos:** Git instalado y accesible en el shell actual.

**Opciones:** --version indica la versión; no actualiza Git.

**Cuándo utilizar:** Comprobar compatibilidad antes de seguir instrucciones o informar de un error.

**Cuándo evitar:** No considerar la versión una prueba de que una extensión opcional está instalada.

**Sintaxis**

`git --version`

**Ejemplo básico**

`git --version`

Ejecuta en un terminal nuevo y anota la versión.

**Ejemplo profesional**

`git --version`

Registra la versión de Git del runner en un informe de diagnóstico de CI sin asumir que todos son iguales.

**Impacto en el estado**

- Working tree: No aplica
- Index: No aplica
- Objetos / refs / historial: No aplica
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Muestra una versión; no requiere repositorio.

**Efectos y efectos secundarios:** Lee información del ejecutable sin cambiar el estado de Git.

**Errores comunes:** Un ejecutable ausente o un PATH incorrecto impiden la ejecución; varias instalaciones pueden resolverse de forma diferente.

**Alternativas:** Usa el mecanismo del sistema operativo para identificar el binario de Git seleccionado.

**Recuperación:** No hay recuperación del repositorio; corrige la instalación o PATH si es necesario.

**Versión y dependencias:** Sin dependencia opcional; compara la versión indicada con el mínimo documentado de la función.

**Capítulos relacionados**

- [getting-started/01-install-git](../../getting-started/01-install-git/README.es.md)
- [getting-started/02-terminal-and-help](../../getting-started/02-terminal-and-help/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git>

## git-help

**`git help`**

**Tipo:** Comando nativo

**Nivel:** Principiante

**Buscar por intención:** Encontrar ayuda, Comprobar versión de Git

**Riesgo:** Solo lectura. El visor puede iniciar un proceso o abrir un navegador; los datos de Git no se modifican.

**Finalidad:** Abrir la ayuda de un comando Git o enumerar comandos disponibles.

**Requisitos previos:** Git instalado; la ayuda detallada requiere un visor de documentación disponible.

**Opciones:** -a enumera comandos disponibles; -w solicita ayuda en formato web.

**Cuándo utilizar:** Comprobar sintaxis y comportamiento documentado de una operación desconocida.

**Cuándo evitar:** No confundir la ayuda instalada localmente con la documentación de otra versión de Git.

**Sintaxis**

`git help [command]`

**Ejemplo básico**

`git help status`

Lee el manual de status antes de interpretar su salida.

**Ejemplo profesional**

`git help -a`

Enumera comandos en una nueva estación de desarrollo para descubrir extensiones instaladas.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Muestra documentación o una lista de comandos.

**Efectos y efectos secundarios:** No modifica el repositorio; el visor o navegador seleccionado puede iniciar un proceso.

**Errores comunes:** La falta de visor de manuales o archivos de documentación puede impedir abrir la página completa.

**Alternativas:** Usa git COMMAND -h para sintaxis breve o el manual oficial versionado en línea.

**Recuperación:** Cierra el visor; usa la ayuda breve o el manual oficial si no está disponible.

**Versión y dependencias:** La disponibilidad del visor depende de la instalación y del sistema operativo.

**Capítulos relacionados**

- [getting-started/02-terminal-and-help](../../getting-started/02-terminal-and-help/README.es.md)
- [basic-commands/01-init-config-help](../../basic-commands/01-init-config-help/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-help>

## git-init

**`git init`**

**Tipo:** Comando nativo

**Nivel:** Principiante

**Buscar por intención:** Crear repositorio, Configurar Git

**Riesgo:** Cambio de estado. Crea metadatos del repositorio; comprueba el destino primero.

**Finalidad:** Crear un repositorio Git local o reinicializar uno existente.

**Requisitos previos:** Directorio propio con permiso de escritura o padre escribible para uno nuevo.

**Opciones:** -b selecciona el nombre de la rama inicial; el directorio opcional selecciona el destino.

**Cuándo utilizar:** Empezar a versionar un proyecto local nuevo sin remoto.

**Cuándo evitar:** No inicialices el directorio equivocado ni crees un repositorio anidado involuntariamente.

**Sintaxis**

`git init [-b branch] [directory]`

**Ejemplo básico**

`git init -b main notes-lab`

En un directorio padre propio y desechable, crea un repositorio de notas en main.

**Ejemplo profesional**

`git init -b main prototype-lab`

Crea un repositorio separado para un prototipo en lugar de inicializar por error el directorio de una aplicación existente.

**Impacto en el estado**

- Working tree: Condicional
- Index: Sin cambios
- Objetos / refs / historial: Cambia
- Repositorio remoto: Sin cambios
- Otros estados: Cambia

**Resultado esperado:** En un repositorio nuevo existen metadatos y HEAD nombra una rama aún sin commit; no se crea ningún commit.

**Efectos y efectos secundarios:** Puede crear el directorio y los metadatos; los archivos no se añaden al staging automáticamente.

**Errores comunes:** Inicializar un directorio padre o anidado por error confunde los límites del repositorio.

**Alternativas:** Usa git clone cuando necesites un repositorio existente y su historial.

**Recuperación:** Inspecciona la ruta y haz una copia; no elimines metadatos sin verificar que el repositorio es desechable y su historial innecesario.

**Versión y dependencias:** -b / --initial-branch requiere Git 2.28 o posterior.

**Capítulos relacionados**

- [getting-started/03-first-repository](../../getting-started/03-first-repository/README.es.md)
- [basic-commands/01-init-config-help](../../basic-commands/01-init-config-help/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-init>
- <https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup>

## git-init-bare

**`git init --bare`**

**Tipo:** Uso de opción

**Nivel:** Intermedio

**Buscar por intención:** Crear repositorio, Simular colaboración

**Riesgo:** Cambio de estado. Un origin bare puede contener historial valioso; nunca lo elimines solo porque no hay archivos extraídos.

**Finalidad:** Inicializar un repositorio sin working tree extraído, adecuado como origin compartido local.

**Requisitos previos:** Destino desechable y escribible; elige deliberadamente la rama inicial.

**Opciones:** --bare crea la disposición bare de metadatos; -b elige la rama inicial.

**Cuándo utilizar:** Crear un origin local para un ejercicio de colaboración con dos clones.

**Cuándo evitar:** No lo uses como repositorio normal donde pretendes editar y preparar archivos.

**Sintaxis**

`git init --bare [-b branch] [directory]`

**Ejemplo básico**

`git init --bare -b main origin.git`

Crea un origin bare local en un directorio padre desechable.

**Ejemplo profesional**

`git init --bare -b main collaboration.git`

Usa un origin bare local para ensayar push y fetch con dos clones separados sin cuenta de alojamiento.

**Impacto en el estado**

- Working tree: No aplica
- Index: No aplica
- Objetos / refs / historial: Cambia
- Repositorio remoto: Sin cambios
- Otros estados: Cambia

**Resultado esperado:** Existe el repositorio bare; HEAD es simbólico y al inicio no hay commit.

**Efectos y efectos secundarios:** No crea working tree ni flujo normal de staging; refs y objetos residen en el directorio del repositorio.

**Errores comunes:** Los comandos de working tree en un repositorio bare fallan o no tienen sentido.

**Alternativas:** Usa git init normal para editar; clona el origin bare para trabajar con archivos.

**Recuperación:** Protege refs y objetos existentes; elimina solo un origin desechable verificado cuando todos terminen.

**Versión y dependencias:** -b requiere Git 2.28 o posterior; sin servicio alojado.

**Capítulos relacionados**

- [remote-repositories/01-remote-concepts](../../remote-repositories/01-remote-concepts/README.es.md)
- [git-architecture/01-three-locations](../../git-architecture/01-three-locations/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-init>
- <https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup>

## git-config-local

**`git config --local`**

**Tipo:** Uso de opción

**Nivel:** Principiante

**Buscar por intención:** Configurar Git, Configurar identidad

**Riesgo:** Cambio de estado. La configuración puede afectar commits futuros o comportamiento de ejecución; usa identidad ficticia solo en laboratorios.

**Finalidad:** Definir un valor de configuración local del repositorio, como la identidad de commit.

**Requisitos previos:** Repositorio propio y motivo claro para el ajuste; inspecciona primero los valores existentes.

**Opciones:** --local selecciona la configuración del repositorio; --get lee un valor; --unset elimina una clave de valor único.

**Cuándo utilizar:** Definir identidad o comportamiento específico del proyecto sin cambiar otros repositorios.

**Cuándo evitar:** No almacenes tokens de acceso o claves privadas en valores ordinarios de configuración.

**Sintaxis**

`git config --local name value`

**Ejemplo básico**

`git config --local user.name "Alice Example"`

En un repositorio desechable, define un nombre de autor ficticio.

**Ejemplo profesional**

`git config --local user.email alice@example.invalid`

Define un correo ficticio en un proyecto desechable para separar su identidad de commit de la identidad normal de la estación.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Cambia

**Resultado esperado:** La clave especificada tiene el valor local solicitado; las operaciones futuras pueden usarlo.

**Efectos y efectos secundarios:** Cambia configuración, no commits existentes ni archivos preparados; la identidad se aplica a commits futuros.

**Errores comunes:** Usar --global por error afecta otros repositorios; sin repositorio, --local no funciona.

**Alternativas:** Usa git -c para una sustitución puntual o --global para un valor predeterminado intencional del usuario.

**Recuperación:** Restaura el valor local anterior o elimina la clave solo si antes no existía; comprueba después la configuración efectiva.

**Versión y dependencias:** Sin dependencia opcional; los ejemplos usan la forma tradicional nombre/valor.

**Capítulos relacionados**

- [getting-started/03-first-repository](../../getting-started/03-first-repository/README.es.md)
- [basic-commands/01-init-config-help](../../basic-commands/01-init-config-help/README.es.md)
- [security/09-commit-and-tag-signing](../../security/09-commit-and-tag-signing/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-config>

## git-config-global

**`git config --global`**

**Tipo:** Uso de opción

**Nivel:** Principiante

**Buscar por intención:** Configurar Git, Configurar identidad

**Riesgo:** Cambio de estado. Cambio general del usuario; el ejemplo de escritura solo es para un home desechable aislado.

**Finalidad:** Leer o definir configuración de Git del usuario compartida entre repositorios.

**Requisitos previos:** Cuenta bajo tu control; para practicar escritura aísla primero el home/ruta de configuración.

**Opciones:** --global selecciona el ámbito del usuario; --get lee en lugar de escribir; --unset elimina clave de valor único.

**Cuándo utilizar:** Inspeccionar valores del usuario o establecer intencionalmente una preferencia general.

**Cuándo evitar:** Evita escribir identidad ficticia del laboratorio en la configuración global normal o cambiar una máquina gestionada/compartida.

**Sintaxis**

`git config --global name value`

**Ejemplo básico**

`git config --global --get user.name`

Inspecciona el nombre de autor global sin cambiarlo; la ausencia puede devolver un código distinto de cero.

**Ejemplo profesional**

`git config --global user.name "Alice Example"`

Solo en home/config de laboratorio aislado por separado, define identidad ficticia general para compararla con una sustitución local.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Condicional

**Resultado esperado:** La lectura indica el valor si existe; la escritura actualiza la configuración del usuario, sujeta a sustituciones de mayor precedencia.

**Efectos y efectos secundarios:** Puede afectar operaciones futuras en varios repositorios; los objetos de commits existentes no cambian.

**Errores comunes:** Confundir ámbito global con sustitución específica del repositorio puede provocar identidad o comportamiento inesperados.

**Alternativas:** Usa git config --local para ajustes del proyecto o git -c para una ejecución.

**Recuperación:** Registra el valor anterior antes de cambiarlo; restáuralo o elimina solo una clave recién creada. Comprueba ámbito y valor efectivo.

**Versión y dependencias:** Sin dependencia opcional; la ubicación del archivo global depende de Git y de la configuración del entorno.

**Capítulos relacionados**

- [getting-started/03-first-repository](../../getting-started/03-first-repository/README.es.md)
- [basic-commands/01-init-config-help](../../basic-commands/01-init-config-help/README.es.md)
- [security/05-secrets-and-disclosure-prevention](../../security/05-secrets-and-disclosure-prevention/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-config>

## git-config-show-origin

**`git config --list --show-origin`**

**Tipo:** Uso de opción

**Nivel:** Intermedio

**Buscar por intención:** Inspeccionar configuración, Diagnosticar configuración

**Riesgo:** Sensible. Salida sensible; revisa y oculta datos sensibles antes de compartir.

**Finalidad:** Inspeccionar entradas de configuración junto con su origen.

**Requisitos previos:** Git instalado; ejecuta dentro de un repositorio para incluir ajustes locales relevantes.

**Opciones:** --list enumera entradas; --show-origin indica origen; --show-scope añade el ámbito.

**Cuándo utilizar:** Diagnosticar conflictos entre ajustes del usuario y repositorio antes de cambiar nada.

**Cuándo evitar:** No pegues la lista sin revisar en issues o logs públicos; valores y rutas pueden ser sensibles.

**Sintaxis**

`git config --list --show-origin [--show-scope]`

**Ejemplo básico**

`git config --list --show-origin`

Inspecciona orígenes de configuración en privado en un repositorio desechable.

**Ejemplo profesional**

`git config --list --show-origin --show-scope`

Diagnostica qué ámbito proporciona una identidad inesperada sin exponer la lista completa en un ticket.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Imprime entradas con origen y opcionalmente ámbito; pueden aparecer claves repetidas.

**Efectos y efectos secundarios:** No cambia datos Git, pero la salida puede exponer rutas personales, identidad o configuración sensible.

**Errores comunes:** Suponer que siempre prevalece el primer valor impreso ignora precedencia y ajustes multivalor.

**Alternativas:** Usa git config --get para una clave o restringe con --local o --global.

**Recuperación:** No requiere recuperación Git; si se divulgaron secretos, sigue el procedimiento de incidente de credenciales.

**Versión y dependencias:** --show-origin disponible desde Git 2.8; --show-scope desde Git 2.26.

**Capítulos relacionados**

- [basic-commands/01-init-config-help](../../basic-commands/01-init-config-help/README.es.md)
- [security/05-secrets-and-disclosure-prevention](../../security/05-secrets-and-disclosure-prevention/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-config>
- <https://git-scm.com/docs/git-config/2.8.6>
- <https://git-scm.com/docs/git-config/2.26.0>

## git-config-get

**`git config --get`**

**Tipo:** Uso de opción

**Nivel:** Principiante

**Buscar por intención:** Inspeccionar configuración, Configurar identidad

**Riesgo:** Sensible. Una consulta específica reduce divulgación frente a una lista completa, pero revisa la salida.

**Finalidad:** Consultar una clave específica de configuración Git sin modificarla.

**Requisitos previos:** Git instalado; --local exige repositorio.

**Opciones:** --get lee un valor; --get-all obtiene múltiples valores; las opciones de ámbito restringen la consulta.

**Cuándo utilizar:** Comprobar identidad efectiva o inspeccionar una clave antes de cambiarla.

**Cuándo evitar:** No consultes ni compartas valores de configuración sensibles sin necesidad.

**Sintaxis**

`git config [--local|--global] --get name`

**Ejemplo básico**

`git config --get user.name`

Lee el nombre de autor efectivo en un repositorio desechable.

**Ejemplo profesional**

`git config --local --get user.email`

Comprueba si un proyecto tiene correo de autor local antes del primer commit; no publiques la dirección real.

**Impacto en el estado**

- Working tree: Sin cambios
- Index: Sin cambios
- Objetos / refs / historial: Sin cambios
- Repositorio remoto: Sin cambios
- Otros estados: Sin cambios

**Resultado esperado:** Imprime un valor si se encuentra; una clave ausente produce código de salida distinto de cero.

**Efectos y efectos secundarios:** No modifica el repositorio; los valores consultados pueden contener datos personales o sensibles.

**Errores comunes:** Suponer que una clave ausente es un valor vacío configurado o tratar el código no cero como fallo no relacionado.

**Alternativas:** Usa --get-all para claves multivalor o --list --show-origin para investigar el origen.

**Recuperación:** No hay recuperación del repositorio; comprueba la escritura de la clave y ámbito si no se encuentra.

**Versión y dependencias:** Sin dependencia opcional; usa la sintaxis tradicional --get para amplia compatibilidad Git.

**Capítulos relacionados**

- [basic-commands/01-init-config-help](../../basic-commands/01-init-config-help/README.es.md)
- [remote-repositories/05-secure-authentication](../../remote-repositories/05-secure-authentication/README.es.md)

**Documentación oficial**

- <https://git-scm.com/docs/git-config>


---

<!-- navigation-footer -->
[Módulo anterior](../../git-internals/README.es.md) · [Índice](../README.es.md) · [Siguiente](../02-repository-inspection/README.es.md)
<!-- /navigation-footer -->
