# Inicializar, configurar y consultar ayuda

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
— · [Índice](../README.es.md) · [Siguiente](../02-status-add-commit/README.es.md)
<!-- /navigation -->

**Nivel:** principiante · **Tiempo estimado:** 25 min

**Requisitos previos:** [Primeros pasos](../../getting-started/README.es.md) · [Arquitectura Git](../../git-architecture/README.es.md)

**Objetivo:** Distinguir inicialización, ámbitos de configuración y comandos de ayuda.

## Qué es y por qué

git init crea metadatos normalmente en .git; --initial-branch fija rama inicial (Git 2.28+). Segundo init suele reinicializar sin descartar historial, pero no use como reparación. git config lee/escribe ajustes: system, global, local y overrides por comando tienen ámbitos distintos. Use --local en lab y -c clave=valor por invocación. git help da ayuda completa; comando -h uso corto (puede retornar no cero).

## Práctica

Inicie NUEVO lab desechable aislado siguiendo módulo 00 capítulo 03, incluidos git init e identidades efectivas ficticias, pero sin commit aún. En subcarpeta repo ejecute:

```text
git config --local --get user.name
git config --local --get user.email
git config --show-origin --get user.email
git config --local core.autocrlf false
git config --local --get core.autocrlf
git -c core.autocrlf=true config --get core.autocrlf
git config --local --get core.autocrlf
git status -h
git help init
```

Esperado: identidad ficticia, ajuste local false; override de invocación true, después local aún false. --show-origin muestra ruta de origen; no comparta rutas privadas. Ayuda no cambia repo; salga de paginador con q. core.autocrlf controla conversión automática de finales de línea; false evita esa conversión en estos ejercicios de texto. No se modifican ajustes globales.

## Errores comunes y seguridad

Use shell dedicado solo en este lab. Compruebe Git 2.40+ según aislamiento de módulo 00. No ejecute init en carpeta personal/trabajo; evite --global/--system y volcar configuración. Si origen/identidad inesperada reinicie lab aislado sin cambiar ajustes reales.

## Ejercicio y autoevaluación

Prediga tres salidas core.autocrlf. Respuesta: false, true, false. Apruebe si explica por qué -c no persiste. Uso profesional: comprobar origen de ajuste antes de diagnosticar.

## Referencia rápida

- `git init`
- `git config`
- `git help`
- `git`

## Fuentes oficiales

- [Git: git-init](https://git-scm.com/docs/git-init)
- [Git: git-config](https://git-scm.com/docs/git-config)
- [Git: git-help](https://git-scm.com/docs/git-help)
- [Git: git](https://git-scm.com/docs/git)
