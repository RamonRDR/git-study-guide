# Exclusão segura de branches locais

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../03-switch-safety-and-naming/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../05-detached-head/README.pt-BR.md)
<!-- /navigation -->

**Nível:** iniciante · **Tempo estimado:** 25 min

**Pré-requisitos:** [Alternância segura e nomes de branches](../03-switch-safety-and-naming/README.pt-BR.md)

**Objetivo:** Identificar commits alcançáveis e excluir só branch local já contida.

## O que é e por quê

Excluir branch remove nome, não imediatamente todos objetos referenciados. Se commits não alcançáveis por refs sobreviventes, limpeza futura pode torná-los irrecuperáveis. `git branch --merged main` lista branches cujas pontas são ancestrais de main ou a própria main; `--no-merged main` lista outras. `git branch -d NAME` verifica integração no upstream configurado, ou HEAD se ausente; nem sempre verifica main. Neste lab não há upstream. `-D` ignora proteção de integração e pode perder único acesso nomeado ao trabalho; não execute. Branch ativa em worktree não pode ser excluída assim. Confira alcance em relação à branch sobrevivente pretendida antes de remover.

## Prática

Continue lab isolado em main com status limpo. archive/base ainda C1; feat/note-revision e docs/overview têm commits separados. Confira:

```text
git rev-parse --show-toplevel
git branch --show-current
git status --short
git branch --merged main
git branch --no-merged main
git log --oneline main..archive/base
git log --oneline main..feat/note-revision
```

Esperado: archive/base e main contidas; feature e docs não. Primeiro intervalo vazio; segundo tem commit. Exclua APENAS archive/base após confirmar contida e não atual:

```text
git branch -d archive/base
git branch --list
git log -1 --oneline main
```

Nome antigo desaparece, C1 segue em main. Agora demonstre proteção contra excluir trabalho não integrado; NÃO substitua por -D:

```text
git branch -d feat/note-revision
```

Recusa não zero esperada. Confira branch existente, commit distinto preservado e main inalterada:

```text
git branch --list
git log --oneline main..feat/note-revision
git status --short
```

## Erros comuns e segurança

Não force exclusão aqui. Squash merge pode preservar conteúdo sem ancestralidade, então falha -d não prova ausência de trabalho em outro snapshot; confira histórico/conteúdo, peça review e mantenha branch na dúvida. Estratégias merge no módulo 05. Tracking e exclusão remota no 06; sem push neste módulo.

## Exercício e autocorreção

Qual branch pode ser removida neste lab específico? Resposta: archive/base, ponta já alcançável por main. Passe se feature permanecer após recusa. Uso profissional: conferir integração, destino pretendido e política antes de limpar.

## Referência rápida

`git branch --merged main`: pontas contidas; `git branch --no-merged main`: outras pontas; `git branch -d NAME`: exclusão local protegida.

## Fontes oficiais

- [Git: git-branch](https://git-scm.com/docs/git-branch)
- [Git: git-log](https://git-scm.com/docs/git-log)
- [Git: gitrevisions](https://git-scm.com/docs/gitrevisions)

---

<!-- navigation-footer -->
[Anterior](../03-switch-safety-and-naming/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../05-detached-head/README.pt-BR.md)
<!-- /navigation-footer -->
