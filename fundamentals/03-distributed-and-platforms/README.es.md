# Centralizado, distribuido y plataformas

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../02-history-of-git/README.es.md) · [Índice](../README.es.md) · [Siguiente módulo](../../git-architecture/README.es.md)
<!-- /navigation -->

**Nivel:** principiante · **Tiempo estimado:** 25 min

**Requisitos previos:** [Linux, BitKeeper y nacimiento de Git](../02-history-of-git/README.es.md)

**Objetivo:** Distinguir modelos VCS, Git y plataformas de alojamiento.

## Qué es y por qué

VCS centralizado usa historial central; clientes suelen contactarlo para registrar revisiones compartidas. VCS distribuido como Git normalmente da a cada clone (copia del repo) historial local; clones superficiales/parciales pueden omitir historial u objetos. Equipos aún pueden elegir repo compartido autoritativo. GitHub y GitLab alojan repos Git y ofrecen issues, reviews y automatización. Git es sistema de control de versiones. Remoto es ubicación configurada de otro repo.

## Práctica

Centralizado: copia Alice -> historial central <- copia Bob. Distribuido: historial local Alice <-> remoto compartido <-> historial local Bob. Flechas muestran comunicación. Commits locales funcionan sin servidor. GitHub usa pull requests; GitLab merge requests, objetos de review de plataforma, no comandos nativos. Compruebe lab:

```text
git log -1 --oneline
git remote -v
```

Esperado: historial local y ningún remoto (no configurado). Sin cuenta. Modelos centralizados pueden simplificar administración central; distribuidos favorecen trabajo local pero requieren coordinación.

## Errores comunes y seguridad

Distribuido no significa respaldo, permisos ni sincronización automáticos. Commit local no es subida. No copie credenciales ni añada remotos reales aún. Limpie solo carpeta desechable exacta según lección primer commit o conserve para práctica.

## Ejercicio y autoevaluación

Clasifique `git commit`, pull request, merge request y `git log`. Pista: ¿qué comandos locales? Respuesta: commit/log son Git; PR/MR son review de plataforma. Apruebe si explica historial sin red y por qué equipos necesitan remoto compartido.

## Referencia rápida

- `git log -1 --oneline`
- `git remote -v`

## Fuentes oficiales

- [https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control)
- [https://git-scm.com/book/en/v2/Getting-Started-What-is-Git](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git)
- [https://docs.github.com/](https://docs.github.com/)
- [https://docs.gitlab.com/](https://docs.gitlab.com/)

---

<!-- navigation-footer -->
[Anterior](../02-history-of-git/README.es.md) · [Índice](../README.es.md) · [Siguiente módulo](../../git-architecture/README.es.md)
<!-- /navigation-footer -->
