# VS Code e interfaces gráficas

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../03-first-repository/README.es.md) · [Índice](../README.es.md) · [Siguiente](../05-first-commit/README.es.md)
<!-- /navigation -->

**Nivel:** principiante · **Tiempo estimado:** 20 min

**Requisitos previos:** [Primer repositorio y configuración](../03-first-repository/README.es.md)

**Objetivo:** Abrir lab en editor y comparar GUI y terminal.

## Qué es y por qué

Editor cambia archivos; Git registra contenido seleccionado. VS Code integra Git pero usa instalación Git separada para operaciones locales. Source Control muestra cambios y permite stage (seleccionar contenido para commit) y commit (registrar contenido elegido). Git GUI es otro cliente opcional si instalado. Ninguno requiere cuenta de alojamiento para trabajo local.

## Práctica

Instale VS Code desde página oficial si desea; editor de texto plano sirve. Use File > Open Folder para abrir SOLO su lab. Si configurado, `code .` es alternativa. Abra Terminal > New Terminal y compruebe raíz y status.

```text
git rev-parse --show-toplevel
git status
```

Source Control debe detectar repo. Etiquetas pueden variar. Compare cambios allí en próxima lección. GUI basada en documentación, no ejecutada en CI.

## Errores comunes y seguridad

No pulse Publish, Sync, Clone ni Initialize Repository en este lab. Si Git no se detecta, compruebe `git --version` en terminal integrada y reinicie editor. Confíe solo en carpetas creadas/revisadas; evite extensiones y tareas desconocidas.

## Ejercicio y autoevaluación

Encuentre Source Control y terminal, o use editor simple más terminal. Pista: compare raíz del repo. Apruebe si explica por qué interfaces reflejan mismo estado Git. Hábito profesional: inspeccionar visualmente y verificar con comandos.

## Referencia rápida

- `git rev-parse --show-toplevel`
- `git status`

## Fuentes oficiales

- [https://code.visualstudio.com/download](https://code.visualstudio.com/download)
- [https://code.visualstudio.com/docs/sourcecontrol/quickstart](https://code.visualstudio.com/docs/sourcecontrol/quickstart)
- [https://git-scm.com/docs/git-gui](https://git-scm.com/docs/git-gui)
