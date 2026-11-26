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

Instale VS Code desde página oficial si desea; editor de texto plano también sirve. Use File > Open Folder para abrir SOLO subcarpeta repo del lab. Si configurado, `code .` desde terminal dedicada es alternativa. Source Control puede mostrar cambios, pero proceso del editor quizá no herede entorno Git aislado. Úselo solo para editar texto e inspeccionar cambios; no haga stage, commit ni ejecute Git desde editor o terminal integrada. Vuelva al shell dedicado original para todos comandos Git. Compruebe allí:

```text
git rev-parse --show-toplevel
git status
```

Source Control debe detectar repo; etiquetas pueden variar. GUI basada en documentación, no ejecutada en CI. Si se cerró shell original, repita capítulo 03 en lab nuevo.

## Errores comunes y seguridad

No pulse Publish, Sync, Clone ni Initialize Repository en este lab. Si Git no se detecta, compruebe `git --version` en terminal dedicada del lab y reinicie editor si hace falta. Confíe solo en carpetas creadas/revisadas; evite extensiones y tareas desconocidas.

## Ejercicio y autoevaluación

Encuentre Source Control y terminal, o use editor simple más terminal. Pista: compare raíz del repo. Apruebe si explica por qué interfaces reflejan mismo estado Git. Hábito profesional: inspeccionar visualmente y verificar con comandos.

## Referencia rápida

- `git rev-parse --show-toplevel`
- `git status`

## Fuentes oficiales

- [https://code.visualstudio.com/download](https://code.visualstudio.com/download)
- [https://code.visualstudio.com/docs/sourcecontrol/quickstart](https://code.visualstudio.com/docs/sourcecontrol/quickstart)
- [https://git-scm.com/docs/git-gui](https://git-scm.com/docs/git-gui)

---

<!-- navigation-footer -->
[Anterior](../03-first-repository/README.es.md) · [Índice](../README.es.md) · [Siguiente](../05-first-commit/README.es.md)
<!-- /navigation-footer -->
