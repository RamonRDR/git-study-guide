# Garbage collection e maintenance

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../07-loose-objects-and-packfiles/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../09-reflogs-and-reachability/README.pt-BR.md)
<!-- /navigation -->

**Nível:** avançado · **Tempo estimado:** 40 min

**Pré-requisitos:** [14 Internals do Git](../README.pt-BR.md) · [Git avançado](../../advanced-git/README.pt-BR.md)

**Objetivo:** Garbage collection organiza armazenamento e pode remover objetos inalcançáveis conforme retenção; maintenance agenda ou executa tarefas de manutenção.

## O que é e por quê

Garbage collection organiza armazenamento e pode remover objetos inalcançáveis conforme retenção; maintenance agenda ou executa tarefas de manutenção. Alcançabilidade e expiração dependem de refs, reflogs, config e versão. Prune imediato pode destruir recuperação e interferir em escritores concorrentes. Manutenção normal não garante apagar segredos.

## Prática

Crie lab isolado novo pelo índice vinculado de Git avançado antes de cada prática. Rode comandos individualmente e pare em resultado inesperado. Confira raiz e sandbox impresso. Base Git 2.34+, Bash (Git Bash no Windows).

Use apenas diagnósticos aqui. Inspecione contagens, IDs alcançáveis e config relevante. Sem prune forçado, mudança de expiração, agendamento automático ou exclusão manual. Plano profissional inclui backups, janela tranquila e verificação posterior. Consulta config pode retornar não zero quando ausente.

```bash
git count-objects -v
git rev-list --objects --all
git config --local --get gc.pruneExpire
git config --local --get gc.reflogExpire
git fsck --no-reflogs
```

## Erros comuns e segurança

Use só lab descartável. Nunca altere arquivos de objetos/refs à mão, force prune ou experimente em repo real. Se estado divergir, inspecione status, log e plumbing de leitura; feche shell dedicado e remova só sandbox anotado pelo gerenciador de arquivos após revisar conteúdo.

## Exercício e autocorreção

Por que não usar prune imediato para commit perdido? Pode remover objetos necessários à recuperação. Preserve evidências e consulte recuperação primeiro.

## Referência rápida

- `git count-objects -v`
- `git rev-list --objects --all`
- `git config --local --get gc.pruneExpire`
- `git config --local --get gc.reflogExpire`

## Fontes oficiais

- [https://git-scm.com/docs/git-gc](https://git-scm.com/docs/git-gc)
- [https://git-scm.com/docs/git-maintenance](https://git-scm.com/docs/git-maintenance)
- [https://git-scm.com/docs/git-fsck](https://git-scm.com/docs/git-fsck)

---

<!-- navigation-footer -->
[Anterior](../07-loose-objects-and-packfiles/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../09-reflogs-and-reachability/README.pt-BR.md)
<!-- /navigation-footer -->
