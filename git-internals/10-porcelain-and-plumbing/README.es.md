# Porcelain y plumbing: inspección estable

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../09-reflogs-and-reachability/README.es.md) · [Índice](../README.es.md) · [Siguiente](../11-integrated-internals-lab/README.es.md)
<!-- /navigation -->

**Nivel:** avanzado · **Tiempo estimado:** 40 min

**Requisitos:** [14 Funcionamiento interno de Git](../README.es.md) · [Git avanzado](../../advanced-git/README.es.md)

**Objetivo:** Comandos porcelain atienden flujos de usuario; plumbing expone primitivas para scripts y diagnóstico.

## Qué es y por qué

Comandos porcelain atienden flujos de usuario; plumbing expone primitivas para scripts y diagnóstico. `git status --porcelain=v1` da formato estable para máquinas pese al nombre porcelain. Prefiera formatos documentados y listas de rutas delimitadas por NUL; evite mensajes humanos localizados. Plumbing puede cambiar refs/objetos, prefiera lectura hasta comprender invariantes.

## Práctica

Cree laboratorio aislado nuevo desde índice vinculado de Git avanzado antes de cada práctica. Ejecute comandos individualmente y pare ante resultado inesperado. Compruebe raíz y sandbox impreso. Base Git 2.34+, Bash (Git Bash en Windows).

Compare estado humano con porcelain e inspección de objetos. Laboratorio limpio da salida porcelain vacía; rev-parse resuelve HEAD independiente de formato humano. Para nombres arbitrarios use NUL (`-z`) y parser compatible, no dividir líneas. Evite update-ref directo en repos compartidos.

```bash
git status
git status --porcelain=v1
git rev-parse --verify HEAD
git cat-file -t HEAD
git ls-files --stage
git ls-tree -r HEAD
```

## Errores comunes y seguridad

Use solo laboratorio desechable. Nunca modifique archivos de objetos/refs a mano, fuerce prune ni experimente en repo real. Si estado difiere, inspeccione status, log y plumbing de lectura; cierre shell dedicado y elimine solo sandbox anotado mediante gestor de archivos tras revisar contenido.

## Ejercicio y autocorrección

¿Por qué no analizar texto de git status en CI? Puede variar por idioma/config; use formato porcelain documentado y código de salida.

## Referencia rápida

- `git status`
- `git status --porcelain=v1`
- `git rev-parse --verify HEAD`
- `git cat-file -t HEAD`

## Fuentes oficiales

- [https://git-scm.com/docs/git](https://git-scm.com/docs/git)
- [https://git-scm.com/docs/git-status](https://git-scm.com/docs/git-status)
- [https://git-scm.com/docs/git-rev-parse](https://git-scm.com/docs/git-rev-parse)

---

<!-- navigation-footer -->
[Anterior](../09-reflogs-and-reachability/README.es.md) · [Índice](../README.es.md) · [Siguiente](../11-integrated-internals-lab/README.es.md)
<!-- /navigation-footer -->
