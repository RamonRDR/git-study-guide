# Jobs, steps, stages e dependências

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../05-runners-and-execution-environments/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../07-artifacts-and-cache/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 35 min

**Pré-requisitos:** [GitHub](../../github/README.pt-BR.md) · [GitLab](../../gitlab/README.pt-BR.md) · [Runners e ambientes de execução](../05-runners-and-execution-environments/README.pt-BR.md)

**Objetivo:** Modelar ordem de execução, propagação de falhas e paralelismo.

## O que é e por quê

No GitHub Actions, steps de job são ordenados; jobs independentes podem rodar simultaneamente e `needs` declara dependências. No GitLab, stages impõem ordem padrão e `needs` descreve grafo mais direto, permitindo início antes de toda stage anterior terminar. DAG é grafo direcionado acíclico de dependências. Considere `lint` e `test` independentes; `package` depende dos dois. Nenhuma plataforma garante ordem de jobs apenas pela ordem textual. Dependência obrigatória falha normalmente impede trabalho posterior dependente de sucesso; opções explícitas de falha/condição podem mudar isso. Evite `continue-on-error` ou `allow_failure` em checks obrigatórios. Matriz é expansão, não declaração de dependência.

```text
lint ----> package
           ^
           |
test ------+
```

## Prática

Offline, desenhe grafo abaixo. Calcule próximos jobs permitidos se lint passa mas test falha; depois se ambos passam. Esboce job GitHub com `needs: [lint, test]` e job GitLab com mesma chave de dependência no mapeamento do job. São fragmentos para raciocínio, não configurações completas.

## Erros comuns e segurança

Não remova dependência obrigatória para deixar pipeline verde. Confira se arquivos anteriores precisam ser transferidos explicitamente. Diagnostique jobs ignorados e condições antes de mudar gates; nenhuma execução necessária.

## Exercício e autocorreção

Package fica bloqueado se test falha e elegível se ambos passam, sujeito a runner e condições. Passe se identificar duas arestas, ausência de ciclo e jobs paralelos.

## Referência rápida

`needs` / DAG / stage

## Fontes oficiais

- <https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax>
- <https://docs.gitlab.com/ci/yaml/needs/>

---

<!-- navigation-footer -->
[Anterior](../05-runners-and-execution-environments/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../07-artifacts-and-cache/README.pt-BR.md)
<!-- /navigation-footer -->
