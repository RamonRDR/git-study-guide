# Remotos, repositorios bare y clones

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
— · [Índice](../README.es.md) · [Siguiente](../02-fetch-and-tracking/README.es.md)
<!-- /navigation -->

**Nivel:** principiante · **Tiempo estimado:** 35 min

**Requisitos previos:** [Laboratorio aislado](../../getting-started/03-first-repository/README.es.md) · [Primer commit](../../getting-started/05-first-commit/README.es.md) · [Merge y conflictos](../../merge-and-conflicts/README.es.md)

**Objetivo:** Explicar alias de remotos y crear clones independientes sin cuenta.

## Qué y por qué

Un remoto es otro repositorio Git, no necesariamente un servidor en internet. Un repositorio bare almacena historial y refs sin un árbol de trabajo normal en checkout. Sirve como punto de intercambio compartido. Clone crea un repositorio nuevo, descarga historial y normalmente hace checkout de la rama indicada por el HEAD remoto. Origin es una convención creada por clone; upstream puede ser otro alias, a menudo el proyecto original en un flujo con fork. Ninguno es reservado. Una rama de seguimiento upstream es una relación configurada entre una rama local y otra ref. GitHub y GitLab añaden alojamiento, revisión y permisos sobre Git.

## Práctica

Crea un NUEVO laboratorio desechable siguiendo el módulo 00 capítulo 03 y la lección del primer commit. Usa Git 2.40+ y la misma sesión dedicada Bash o PowerShell con configuración system/global aislada, variables Git heredadas limpiadas y plantilla vacía. Verifica que repo/main tenga exactamente un commit con note.txt = practice, estado limpio y ambas identidades ficticias. Anota en privado la ruta del padre temporal. Sube un nivel con `cd ..`; comprueba `pwd` (Bash) o `Get-Location` (PowerShell). Detente si no es exactamente ese padre o contiene algo más que repo, template y gitconfig. Restringe el transporte en esta sesión a archivos locales: Bash `export GIT_ALLOW_PROTOCOL=file`, PowerShell `$env:GIT_ALLOW_PROTOCOL = 'file'`. Ejecuta individualmente; detente ante errores inesperados. Tras remote -v comprueba que ambas URL resuelven al origin.git recién creado antes de enviar. Esperado: true para bare, refs/heads/main para HEAD. El repo inicial solo publica el primer commit.
```text
git init --bare --initial-branch=main origin.git
git -C origin.git rev-parse --is-bare-repository
git -C origin.git symbolic-ref HEAD
git -C repo remote add origin ../origin.git
git -C repo remote -v
git -C repo push -u origin main
git -C origin.git rev-parse refs/heads/main
git clone --no-local origin.git alice
git clone --no-local origin.git bob
```
Configura identidades locales en ambos clones (clone no copia la identidad local del repo inicial).
```text
git -C alice config --local user.name "Study Guide Example"
git -C alice config --local user.email learner@example.invalid
git -C alice config --local commit.gpgsign false
git -C alice config --local core.autocrlf false
git -C bob config --local user.name "Study Guide Example"
git -C bob config --local user.email learner@example.invalid
git -C bob config --local commit.gpgsign false
git -C bob config --local core.autocrlf false
```

```text
git -C alice rev-parse --show-toplevel
git -C bob rev-parse --show-toplevel
git -C alice remote -v
git -C bob remote -v
git -C alice branch -vv
git -C bob branch -vv
git -C alice status --short
git -C bob status --short
```
Las raíces deben ser las carpetas alice/bob previstas, las URL origin deben resolver al mismo origin.git local, main sigue origin/main y el estado es limpio. Las tres puntas main coinciden con el commit inicial. `--no-local` utiliza el transporte Git normal en vez de optimizaciones de copia local. Mantén la sesión dedicada en el padre para capítulos 02–04. Diagrama: repo (inicial) -> origin.git (bare); alice y bob tienen HEAD, árbol de trabajo, index y refs propios; ambos intercambian commits con origin.git. Para practicar configuración, el alias temporal apunta al MISMO bare, no a un segundo servidor.
```text
git -C alice remote add upstream ../origin.git
git -C alice remote set-url upstream ../origin.git
git -C alice remote rename upstream training
git -C alice remote get-url training
git -C alice remote remove training
git -C alice remote -v
```
Esperado: queda solo origin; eliminar un alias quita configuración local y refs de seguimiento, no el repositorio remoto. Cambiar URL no migra historial. En un flujo profesional con fork, origin suele nombrar tu fork y upstream el original; verifica ambos.

## Errores comunes y seguridad

Nunca clones ni envíes a una URL desconocida. Clone no concede autenticación; identidad local no es autorización. Si rutas o identidades difieren, detente y reinicia el laboratorio en vez de cambiar configuración real. No reutilices la sesión para remotos reales.

## Ejercicio y autoevaluación

¿Por qué el origin bare no tiene note.txt en checkout? Pista: distingue historial y árbol de trabajo. Respuesta: existe en snapshots de commits, no en un árbol normal. Aprueba si ambos clones muestran el mismo ID main inicial y raíces independientes.

## Referencia rápida

- `git init --bare --initial-branch=main`
- `git clone --no-local`
- `git remote -v`
- `git remote add / set-url / rename / remove`

## Fuentes oficiales

- [Git: git-init](https://git-scm.com/docs/git-init)
- [Git: git-clone](https://git-scm.com/docs/git-clone)
- [Git: git-remote](https://git-scm.com/docs/git-remote)
