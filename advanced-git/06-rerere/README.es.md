# Rerere: reutilizar resoluciones de conflictos

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../05-hooks/README.es.md) · [Índice](../README.es.md) · [Siguiente](../07-sparse-checkout/README.es.md)
<!-- /navigation -->

**Nivel:** avanzado · **Tiempo estimado:** 45 min

**Requisitos:** [13 Git avanzado](../README.es.md) · [Seguridad y gobernanza](../../security/README.es.md)

**Objetivo:** Rerere registra preimagen conflictiva y postimagen resuelta para que Git reaplique una resolución compatible después.

## Qué es y por qué

Rerere registra preimagen conflictiva y postimagen resuelta para que Git reaplique una resolución compatible después. No prueba que la decisión antigua siga cumpliendo la intención actual. Con rerere.autoupdate=false, inspeccione archivo y prepare explícitamente. Equipos pueden reducir trabajo repetido en integraciones largas.

## Práctica

Cree laboratorio aislado nuevo desde índice del módulo antes de cada práctica. Ejecute un comando por vez; pare ante resultado inesperado. Compruebe sandbox impreso y raíz antes de cambiar. Use Git 2.34+ como base de práctica; consulte ayuda y omita funciones opcionales no disponibles. No ejecute en repositorios de producción.

Use dos ramas desde HEAD actual del laboratorio. Cree cambios conflictivos en la misma línea. Primer merge debe confligir; resuelva con texto elegido, ejecute rerere y commit. Inspeccione estado e historial. Esto registra resolución; no suponga que autorresolución futura sea correcta. Si para en conflicto, use merge --abort en laboratorio.

El segundo merge debe indicar conflicto sin resolver, pero rerere debe restaurar `reviewed` en el archivo de trabajo. Como preparación automática está deshabilitada, `git ls-files -u` aún muestra entradas sin resolver. Inspeccione contenido; aborte este merge repetido tras el check. Si algún merge tiene éxito inesperado o contenido difiere, pare y recree el laboratorio.

```bash
git config --local rerere.enabled true
git config --local rerere.autoupdate false
git switch -c side
printf '%s\n' 'side' > src/state.txt
git add -- src/state.txt
git commit -m "docs: side state"
git switch main
printf '%s\n' 'main' > src/state.txt
git add -- src/state.txt
git commit -m "docs: main state"
before=$(git rev-parse HEAD)
git merge side
git rerere status
printf '%s\n' 'reviewed' > src/state.txt
git rerere
git add -- src/state.txt
git commit -m "merge: reviewed resolution"
git switch -c repeat "$before"
git merge side
git ls-files -u -- src/state.txt
git diff -- src/state.txt
test "$(cat src/state.txt)" = reviewed
git merge --abort
git status --short
```

## Errores comunes y seguridad

Use solo laboratorio desechable y datos ficticios. Si estado difiere, pare; inspeccione estado y operación antes de abortar o recrear laboratorio. Cierre shell dedicado y elimine solo sandbox anotado mediante gestor de archivos tras revisar contenido.

## Ejercicio y autocorrección

¿Rerere reemplaza revisión? No; compruebe contenido y pruebas antes de preparar.

## Referencia rápida

- `git config --local rerere.enabled true`
- `git config --local rerere.autoupdate false`
- `git switch -c side`
- `git add -- src/state.txt`

## Fuentes oficiales

- [https://git-scm.com/docs/git-rerere](https://git-scm.com/docs/git-rerere)
- [https://git-scm.com/docs/git-merge](https://git-scm.com/docs/git-merge)

---

<!-- navigation-footer -->
[Anterior](../05-hooks/README.es.md) · [Índice](../README.es.md) · [Siguiente](../07-sparse-checkout/README.es.md)
<!-- /navigation-footer -->
