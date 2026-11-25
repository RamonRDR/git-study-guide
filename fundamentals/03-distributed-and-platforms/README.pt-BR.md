# Centralizado, distribuído e plataformas

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../02-history-of-git/README.pt-BR.md) · [Índice](../README.pt-BR.md) · —
<!-- /navigation -->

**Nível:** iniciante · **Tempo estimado:** 25 min

**Pré-requisitos:** [Linux, BitKeeper e nascimento do Git](../02-history-of-git/README.pt-BR.md)

**Objetivo:** Distinguir modelos VCS, Git e plataformas de hospedagem.

## O que é e por quê

VCS centralizado usa histórico central; clientes normalmente o contatam para registrar revisões compartilhadas. VCS distribuído como Git normalmente dá a cada clone (cópia do repo) histórico local; clones rasos/parciais podem omitir histórico ou objetos. Equipes ainda podem escolher repo compartilhado autoritativo. GitHub e GitLab hospedam repos Git e oferecem issues, reviews e automação. Git é sistema de controle de versão. Remote é localização configurada de outro repo.

## Prática

Centralizado: cópia Alice -> histórico central <- cópia Bob. Distribuído: histórico local Alice <-> remote compartilhado <-> histórico local Bob. Setas mostram comunicação. Commits locais funcionam sem servidor. GitHub usa pull requests; GitLab merge requests, objetos de review da plataforma, não comandos nativos. Confira lab:

```text
git log -1 --oneline
git remote -v
```

Esperado: histórico local e nenhum remote (não configurado). Sem conta. Modelos centralizados podem simplificar administração central; distribuídos favorecem trabalho local mas exigem coordenação.

## Erros comuns e segurança

Distribuído não significa backup, permissões ou sincronização automáticos. Commit local não é upload. Não copie credenciais nem adicione remotes reais ainda. Limpe só pasta descartável exata conforme aula primeiro commit ou mantenha para prática.

## Exercício e autocorreção

Classifique `git commit`, pull request, merge request e `git log`. Dica: quais comandos locais? Resposta: commit/log são Git; PR/MR são review de plataforma. Passe se explicar histórico offline e por que equipes precisam remote compartilhado.

## Referência rápida

- `git log -1 --oneline`
- `git remote -v`

## Fontes oficiais

- [https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control)
- [https://git-scm.com/book/en/v2/Getting-Started-What-is-Git](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git)
- [https://docs.github.com/](https://docs.github.com/)
- [https://docs.gitlab.com/](https://docs.gitlab.com/)
