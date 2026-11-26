# Garbage collection y maintenance

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../07-loose-objects-and-packfiles/README.es.md) · [Índice](../README.es.md) · [Siguiente](../09-reflogs-and-reachability/README.es.md)
<!-- /navigation -->

**Nivel:** avanzado · **Tiempo estimado:** 40 min

**Requisitos:** [14 Funcionamiento interno de Git](../README.es.md) · [Git avanzado](../../advanced-git/README.es.md)

**Objetivo:** Garbage collection organiza almacenamiento y puede eliminar objetos inalcanzables según retención; maintenance programa o ejecuta tareas de mantenimiento.

## Qué es y por qué

Garbage collection organiza almacenamiento y puede eliminar objetos inalcanzables según retención; maintenance programa o ejecuta tareas de mantenimiento. Alcanzabilidad y expiración dependen de refs, reflogs, config y versión. Prune inmediato puede destruir recuperación e interferir con escritores concurrentes. Mantenimiento normal no garantiza borrar secretos.

## Práctica

Cree laboratorio aislado nuevo desde índice vinculado de Git avanzado antes de cada práctica. Ejecute comandos individualmente y pare ante resultado inesperado. Compruebe raíz y sandbox impreso. Base Git 2.34+, Bash (Git Bash en Windows).

Use solo diagnósticos aquí. Inspeccione conteos, IDs alcanzables y config relevante. Sin prune forzado, cambio de expiración, programación automática ni eliminación manual. Plan profesional incluye copias, ventana tranquila y verificación posterior. Consulta config puede retornar distinto de cero si ausente.

```bash
git count-objects -v
git rev-list --objects --all
git config --local --get gc.pruneExpire
git config --local --get gc.reflogExpire
git fsck --no-reflogs
```

## Errores comunes y seguridad

Use solo laboratorio desechable. Nunca modifique archivos de objetos/refs a mano, fuerce prune ni experimente en repo real. Si estado difiere, inspeccione status, log y plumbing de lectura; cierre shell dedicado y elimine solo sandbox anotado mediante gestor de archivos tras revisar contenido.

## Ejercicio y autocorrección

¿Por qué no usar prune inmediato para commit perdido? Puede eliminar objetos necesarios para recuperación. Preserve evidencia y consulte recuperación primero.

## Referencia rápida

- `git count-objects -v`
- `git rev-list --objects --all`
- `git config --local --get gc.pruneExpire`
- `git config --local --get gc.reflogExpire`

## Fuentes oficiales

- [https://git-scm.com/docs/git-gc](https://git-scm.com/docs/git-gc)
- [https://git-scm.com/docs/git-maintenance](https://git-scm.com/docs/git-maintenance)
- [https://git-scm.com/docs/git-fsck](https://git-scm.com/docs/git-fsck)

---

<!-- navigation-footer -->
[Anterior](../07-loose-objects-and-packfiles/README.es.md) · [Índice](../README.es.md) · [Siguiente](../09-reflogs-and-reachability/README.es.md)
<!-- /navigation-footer -->
