# Hashes e identidad de objetos

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../03-commits-and-tags/README.es.md) · [Índice](../README.es.md) · [Siguiente](../05-refs-and-head/README.es.md)
<!-- /navigation -->

**Nivel:** avanzado · **Tiempo estimado:** 40 min

**Requisitos:** [14 Funcionamiento interno de Git](../README.es.md) · [Git avanzado](../../advanced-git/README.es.md)

**Objetivo:** IDs derivan de tipo, longitud en bytes y contenido, con cabecera de objeto Git.

## Qué es y por qué

IDs derivan de tipo, longitud en bytes y contenido, con cabecera de objeto Git. SHA-1 y SHA-256 son formatos de repositorio; no suponga siempre 40 caracteres. Checksum genérico de bytes no es ID blob Git. Hash no es firma ni control de acceso.

## Práctica

Cree laboratorio aislado nuevo desde índice vinculado de Git avanzado antes de cada práctica. Ejecute comandos individualmente y pare ante resultado inesperado. Compruebe raíz y sandbox impreso. Base Git 2.34+, Bash (Git Bash en Windows).

Calcule ID blob crudo sin escribir objetos (`--no-filters` evita conversiones de atributos). Compare mismos bytes dos veces y luego bytes cambiados. Git informa formato con rev-parse; evite hashes fijos o IDs cortos como identificadores globalmente únicos.

```bash
git rev-parse --show-object-format
git hash-object --no-filters src/state.txt
git rev-parse HEAD:src/state.txt
printf '%s\n' bad | git hash-object --stdin
printf '%s\n' ok | git hash-object --stdin
```

## Errores comunes y seguridad

Use solo laboratorio desechable. Nunca modifique archivos de objetos/refs a mano, fuerce prune ni experimente en repo real. Si estado difiere, inspeccione status, log y plumbing de lectura; cierre shell dedicado y elimine solo sandbox anotado mediante gestor de archivos tras revisar contenido.

## Ejercicio y autocorrección

¿Por qué commits con mismo tree pueden diferir? IDs de padres, datos de autor/committer, fechas o mensajes pueden diferir.

## Referencia rápida

- `git rev-parse --show-object-format`
- `git hash-object --no-filters src/state.txt`
- `git rev-parse HEAD:src/state.txt`

## Fuentes oficiales

- [https://git-scm.com/docs/git-hash-object](https://git-scm.com/docs/git-hash-object)
- [https://git-scm.com/docs/git-rev-parse](https://git-scm.com/docs/git-rev-parse)
- [https://git-scm.com/docs/hash-function-transition](https://git-scm.com/docs/hash-function-transition)

---

<!-- navigation-footer -->
[Anterior](../03-commits-and-tags/README.es.md) · [Índice](../README.es.md) · [Siguiente](../05-refs-and-head/README.es.md)
<!-- /navigation-footer -->
