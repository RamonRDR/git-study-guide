# Por que controle de versão existe

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
— · [Índice](../README.pt-BR.md) · [Próximo](../02-history-of-git/README.pt-BR.md)
<!-- /navigation -->

**Nível:** iniciante · **Tempo estimado:** 20 min

**Pré-requisitos:** [Primeiros passos](../../getting-started/README.pt-BR.md)

**Objetivo:** Explicar histórico intencional versus salvamento comum.

## O que é e por quê

Controle de versão registra revisões para comparar mudanças e identificar decisões. Salvar sobrescreve conteúdo atual; cópias plan-final.txt e plan-final-2.txt confundem. Git registra snapshots escolhidos e relações com commits anteriores. Útil para código e documentação textual, não automaticamente para mídias enormes ou bancos. Não substitui backup: perda do disco pode destruir histórico local.

## Prática

Biblioteca fictícia muda horários de semana e sábado. Em vez de três cópias finais, registre cada mudança separadamente. Snapshot inicial -> revisão semana -> revisão sábado; setas descrevem histórico, não nomes. No lab consulte histórico sem internet.

```text
git log -1 --oneline
```

## Erros comuns e segurança

Não faça commit de segredos ou dados privados. Git não registra cada salvamento nem garante recuperação de edição sem commit. Mantenha backups independentes.

## Exercício e autocorreção

Sugira duas mensagens focadas. Dica: um objetivo por mudança. Resposta: `docs: update weekday hours` e `docs: update Saturday hours`. Passe se explicar por que histórico é claro e backup necessário.

## Referência rápida

- `git log -1 --oneline`

## Fontes oficiais

- [https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control)
- [https://git-scm.com/book/en/v2/Getting-Started-What-is-Git](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git)
