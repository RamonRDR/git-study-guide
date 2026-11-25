# Working tree, index y repositorio

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
— · [Índice](../README.es.md) · [Siguiente](../02-snapshots-head-and-refs/README.es.md)
<!-- /navigation -->

**Nivel:** principiante · **Tiempo estimado:** 30 min

**Requisitos previos:** [Primeros pasos](../../getting-started/README.es.md) · [Fundamentos](../../fundamentals/README.es.md)

**Objetivo:** Distinguir las tres ubicaciones y predecir qué contenido registra un commit.

## Qué es y por qué

Working tree son archivos disponibles para editar. El index (staging area) guarda contenido seleccionado para próximo snapshot, incluidas entradas rastreadas sin cambios. Repositorio local contiene metadatos, objetos y referencias de Git, normalmente en .git. `git add` actualiza index desde archivos; `git commit` registra index como snapshot y normalmente avanza rama actual. Ninguno envía datos al remoto (ubicación de otro repositorio). Index no es solo lista de nombres: representa versiones seleccionadas.

## Práctica

Diagrama de estado accesible (flechas muestran dirección de contenido elegido, no traslado de archivo):

```text
Working tree -- git add --> Index -- git commit --> Local repository
       |                       |                       |
   archivo editable           versión preparada         historial registrado
```

Use terminal aislada de módulo 00. En lab nuevo con primer commit de note.txt completado, edite note.txt a línea única second, guarde con salto final, luego ejecute:

```text
git add note.txt
```

Ahora edite note.txt a third y guarde con salto final sin preparar. Compruebe:

```text
git status --short
git diff --cached
git diff
git show HEAD:note.txt
git show :note.txt
```

Esperado: MM note.txt; HEAD tiene practice, index second, archivo third. Primer M es index frente a HEAD; segundo M es working tree frente a index. Diff cached muestra practice -> second; diff simple second -> third. Ruta con dos puntos consulta versión preparada.

## Errores comunes y seguridad

Compruebe raíz e identidades efectivas antes de commit. Nunca edite archivos .git a mano. Guardar no prepara archivos. Si resultado difiere, inspeccione ambos diffs; no haga reset ni fuerce nada.

## Ejercicio y autoevaluación

¿Qué versión registraría un commit ahora? Pista: siga segunda flecha. Respuesta: second; third queda editado. Apruebe si explica ambas columnas M. Uso profesional: aislar cambio revisado de ediciones ajenas.

## Referencia rápida

- `git add`
- `git commit`
- `git status`
- `git diff`
- `git show`

## Fuentes oficiales

- [Git: git-add](https://git-scm.com/docs/git-add)
- [Git: git-commit](https://git-scm.com/docs/git-commit)
- [Git: git-status](https://git-scm.com/docs/git-status)
- [Git: git-diff](https://git-scm.com/docs/git-diff)
- [Git: git-show](https://git-scm.com/docs/git-show)
