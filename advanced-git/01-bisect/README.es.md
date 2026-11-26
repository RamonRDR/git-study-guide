# Bisect: localizar una regresión

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Módulo anterior](../../security/README.es.md) · [Índice](../README.es.md) · [Siguiente](../02-worktree/README.es.md)
<!-- /navigation -->

**Nivel:** avanzado · **Tiempo estimado:** 45 min

**Requisitos:** [13 Git avanzado](../README.es.md) · [Seguridad y gobernanza](../../security/README.es.md)

**Objetivo:** Localice el primer commit malo usando extremos bueno y malo conocidos.

## Qué es y por qué

Localice el primer commit malo usando extremos bueno y malo conocidos. Git reduce candidatos alcanzables eligiendo commits para probar; no diagnostica el fallo por sí solo. Use una prueba determinista en entorno estable; si un commit no se puede probar, use skip, que puede dejar varios candidatos. En un incidente profesional, registre el rango probado y verifique el resultado frente a su padre antes de corregir.

## Práctica

Cree laboratorio aislado nuevo desde índice del módulo antes de cada práctica. Ejecute un comando por vez; pare ante resultado inesperado. Compruebe sandbox impreso y raíz antes de cambiar. Use Git 2.34+ como base de práctica; consulte ayuda y omita funciones opcionales no disponibles. No ejecute en repositorios de producción.

El commit intermedio del laboratorio aún tiene `ok` en `src/state.txt`. Tras `git bisect start`, inspeccione el commit elegido; marque good solo tras confirmar `ok`. El resultado debe ser el commit más reciente. Reset vuelve al checkout original. Si difiere, ejecute reset e inspeccione el laboratorio.

```bash
git bisect start HEAD HEAD~2
git show HEAD:src/state.txt
git bisect good
git bisect log
git bisect reset
git status --short
```

## Errores comunes y seguridad

Use solo laboratorio desechable y datos ficticios. Si estado difiere, pare; inspeccione estado y operación antes de abortar o recrear laboratorio. Cierre shell dedicado y elimine solo sandbox anotado mediante gestor de archivos tras revisar contenido.

## Ejercicio y autocorrección

¿Por qué no marcar automáticamente como bueno un commit omitido? Puede contener la regresión; el intervalo pierde fiabilidad.

## Referencia rápida

- `git bisect start HEAD HEAD~2`
- `git show HEAD:src/state.txt`
- `git bisect good`
- `git bisect log`

## Fuentes oficiales

- [https://git-scm.com/docs/git-bisect](https://git-scm.com/docs/git-bisect)
- [https://git-scm.com/docs/git-rev-list](https://git-scm.com/docs/git-rev-list)

---

<!-- navigation-footer -->
[Módulo anterior](../../security/README.es.md) · [Índice](../README.es.md) · [Siguiente](../02-worktree/README.es.md)
<!-- /navigation-footer -->
