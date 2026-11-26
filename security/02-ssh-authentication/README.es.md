# Autenticación SSH e identidad del host

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../01-security-foundations/README.es.md) · [Índice](../README.es.md) · [Siguiente](../03-https-and-access-tokens/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 40 min

**Requisitos previos:** [Flujos profesionales](../../professional-workflows/README.es.md) · [Fundamentos de seguridad en Git](../01-security-foundations/README.es.md)

**Objetivo:** Explicar pares de claves y verificación segura del host.

## Qué es y por qué

SSH usa par criptográfico: clave pública puede registrarse en proveedor; privada queda bajo control del usuario. Servidor tiene clave de host, cuya huella debe verificarse por fuente independiente confiable al conectar por primera vez o ante cambio inesperado. Frase de paso protege clave privada en reposo; agente puede mantener claves desbloqueadas temporalmente. Autenticación SSH no concede escritura ni firma commits automáticamente. `ssh -T git@github.com` es prueba opcional específica del host tras configuración; GitHub no da shell interactivo y autenticación exitosa documentada puede devolver estado distinto de cero. Use instrucciones oficiales para generación, algoritmos, registro y revocación.

## Práctica

Sin conexión: etiquete clave pública, privada, frase de paso y huella del servidor en diagrama ficticio. Compare `git@host.example.invalid:team/catalog.git` con URL HTTPS. Si huella cambia inesperadamente, escriba siguiente acción segura. No requiere generar claves ni red.

## Riesgos y recuperación

Nunca pegue claves privadas ni desactive verificación del host. No elimine entrada known-host a ciegas para silenciar aviso. Verifique independientemente, investigue cambios y revoque clave expuesta en cada proveedor donde autorizada.

## Ejercicio y autoevaluación

Clave pública puede registrarse; privada y frase de paso quedan privadas; detenga ante huella inesperada y verifique independientemente.

## Referencia rápida

public key / private key / host fingerprint / agent

## Referencias

- <https://docs.github.com/en/authentication/connecting-to-github-with-ssh>
- <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection>
- <https://docs.gitlab.com/user/ssh/>

---

<!-- navigation-footer -->
[Anterior](../01-security-foundations/README.es.md) · [Índice](../README.es.md) · [Siguiente](../03-https-and-access-tokens/README.es.md)
<!-- /navigation-footer -->
