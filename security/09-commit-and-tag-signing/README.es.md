# Firma de commits y tags

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../08-codeowners-and-responsibilities/README.es.md) · [Índice](../README.es.md) · [Siguiente](../10-software-supply-chain/README.es.md)
<!-- /navigation -->

**Nivel:** intermedio · **Tiempo estimado:** 40 min

**Requisitos previos:** [Flujos profesionales](../../professional-workflows/README.es.md) · [CODEOWNERS y responsabilidades](../08-codeowners-and-responsibilities/README.es.md)

**Objetivo:** Interpretar firmas y límites.

## Qué es y por qué

Firma criptográfica vincula objeto Git a clave de firma y puede verificarse con configuración de confianza adecuada. Git soporta formatos OpenPGP, SSH y X.509 según versión y herramientas. Commit firmado y tag anotado firmado son objetos distintos; tag anotado sin firma no es firmado. `git verify-commit` y `git verify-tag` verifican firmas con clave/confianza adecuadas. Badge Verified sigue política del host; no prueba código seguro, aprobado o desplegado. Nuevo commit de rebase/squash tiene identidad distinta y no hereda firma original. Autenticación y firma SSH son usos separados.

## Práctica

Sin conexión: compare commit A sin firma, B con firma válida de clave desconocida y C firmado por clave confiable pero tests fallidos. Identifique qué prueba cada evidencia. Esboce verificación de tag anotado firmado y commit destino. No necesita generar ni subir claves.

## Riesgos y recuperación

Nunca exponga claves privadas de firma, ignore claves no confiables ni trate badge verde como review. Si clave comprometida, revoque/rote, evalúe firmas afectadas y coordine política de confianza; no reescriba historial público unilateralmente.

## Ejercicio y autoevaluación

A no tiene evidencia de firma; B requiere verificación de identidad confiable; C aún falla controles. Firma y review independientes.

## Referencia rápida

`git verify-commit` / `git verify-tag` / trust

## Referencias

- <https://git-scm.com/docs/git-verify-commit>
- <https://git-scm.com/docs/git-verify-tag>
- <https://git-scm.com/docs/git-config>
- <https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification>
