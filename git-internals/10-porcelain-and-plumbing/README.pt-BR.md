# Porcelain e plumbing: inspeção estável

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../09-reflogs-and-reachability/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../11-integrated-internals-lab/README.pt-BR.md)
<!-- /navigation -->

**Nível:** avançado · **Tempo estimado:** 40 min

**Pré-requisitos:** [14 Internals do Git](../README.pt-BR.md) · [Git avançado](../../advanced-git/README.pt-BR.md)

**Objetivo:** Comandos porcelain atendem fluxos de usuário; plumbing expõe primitivas para scripts e diagnósticos.

## O que é e por quê

Comandos porcelain atendem fluxos de usuário; plumbing expõe primitivas para scripts e diagnósticos. `git status --porcelain=v1` fornece formato estável para máquinas apesar do nome porcelain. Prefira formatos documentados e listas de caminhos delimitadas por NUL; evite mensagens humanas localizadas. Plumbing pode mudar refs/objetos, então prefira leitura até entender invariantes.

## Prática

Crie lab isolado novo pelo índice vinculado de Git avançado antes de cada prática. Rode comandos individualmente e pare em resultado inesperado. Confira raiz e sandbox impresso. Base Git 2.34+, Bash (Git Bash no Windows).

Compare status humano com porcelain e inspeção de objetos. Lab limpo dá saída porcelain vazia; rev-parse resolve HEAD independente da formatação humana. Para nomes arbitrários use NUL (`-z`) e parser compatível, não divisão por linhas. Evite update-ref direto em repos compartilhados.

```bash
git status
git status --porcelain=v1
git rev-parse --verify HEAD
git cat-file -t HEAD
git ls-files --stage
git ls-tree -r HEAD
```

## Erros comuns e segurança

Use só lab descartável. Nunca altere arquivos de objetos/refs à mão, force prune ou experimente em repo real. Se estado divergir, inspecione status, log e plumbing de leitura; feche shell dedicado e remova só sandbox anotado pelo gerenciador de arquivos após revisar conteúdo.

## Exercício e autocorreção

Por que não analisar texto de git status no CI? Pode variar por idioma/config; use formato porcelain documentado e código de saída.

## Referência rápida

- `git status`
- `git status --porcelain=v1`
- `git rev-parse --verify HEAD`
- `git cat-file -t HEAD`

## Fontes oficiais

- [https://git-scm.com/docs/git](https://git-scm.com/docs/git)
- [https://git-scm.com/docs/git-status](https://git-scm.com/docs/git-status)
- [https://git-scm.com/docs/git-rev-parse](https://git-scm.com/docs/git-rev-parse)

---

<!-- navigation-footer -->
[Anterior](../09-reflogs-and-reachability/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../11-integrated-internals-lab/README.pt-BR.md)
<!-- /navigation-footer -->
