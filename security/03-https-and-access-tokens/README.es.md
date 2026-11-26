# HTTPS y tokens de acceso

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../02-ssh-authentication/README.es.md) · [Índice](../README.es.md) · [Siguiente](../04-credential-managers/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 35 min

**Requisitos previos:** [Flujos profesionales](../../professional-workflows/README.es.md) · [Autenticación SSH e identidad del host](../02-ssh-authentication/README.es.md)

**Objetivo:** Elegir credenciales HTTPS de ámbito adecuado.

## Qué es y por qué

HTTPS usa TLS para proteger transporte y autenticar servidor mediante certificado. PAT es credencial con capacidades, ámbito y expiración específicos del proveedor, no contraseña de cuenta. GitHub no acepta contraseña de cuenta en operaciones Git HTTPS. Tokens fine-grained GitHub pueden restringir recursos y permisos; classic tienen ámbitos más amplios y pueden ser necesarios en casos no soportados. GitLab ofrece tokens personales, de proyecto y grupo según configuración y planes. Prefiera credenciales breves y acotadas o identidades de app gestionadas cuando convenga. Token aún puede usarse indebidamente dentro de permisos incluso con 2FA.

## Práctica

Diseñe acceso para bot ficticio que lee un catálogo privado y nunca escribe. Registre repo, permiso lectura, expiración, responsable y ruta de revocación en papel. Use solo `https://host.example.invalid/team/catalog.git` como URL ficticia; nunca inserte credencial.

## Riesgos y recuperación

No desactive TLS, inserte tokens en URLs, comandos, archivos o capturas ni amplíe ámbito para corregir fallo de autenticación. Compruebe host, cuenta, expiración y política en privado. Revoque y sustituya token expuesto.

## Ejercicio y autoevaluación

Lectura de un repo, menor duración práctica y revocación documentada; sin token real.

## Referencia rápida

TLS / PAT / scope / expiration

## Referencias

- <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens>
- <https://docs.gitlab.com/user/profile/personal_access_tokens/>
- <https://git-scm.com/docs/gitcredentials>

---

<!-- navigation-footer -->
[Anterior](../02-ssh-authentication/README.es.md) · [Índice](../README.es.md) · [Siguiente](../04-credential-managers/README.es.md)
<!-- /navigation-footer -->
