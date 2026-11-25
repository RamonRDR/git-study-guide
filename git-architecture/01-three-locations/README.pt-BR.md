# Working tree, index e repositório

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
— · [Índice](../README.pt-BR.md) · [Próximo](../02-snapshots-head-and-refs/README.pt-BR.md)
<!-- /navigation -->

**Nível:** iniciante · **Tempo estimado:** 30 min

**Pré-requisitos:** [Primeiros passos](../../getting-started/README.pt-BR.md) · [Fundamentos](../../fundamentals/README.pt-BR.md)

**Objetivo:** Distinguir os três locais e prever qual conteúdo um commit registra.

## O que é e por quê

Working tree são os arquivos disponíveis para edição. O index (staging area) guarda o conteúdo selecionado para próximo snapshot, incluindo entradas rastreadas inalteradas. Repositório local contém metadados, objetos e referências do Git, normalmente em .git. `git add` atualiza index a partir dos arquivos; `git commit` registra index como snapshot e normalmente avança branch atual. Nenhum envia dados ao remote (localização de outro repositório). Index não é só lista de nomes: representa versões escolhidas.

## Prática

Diagrama de estado acessível (setas mostram direção do conteúdo escolhido, não movimentação de arquivo):

```text
Working tree -- git add --> Index -- git commit --> Local repository
       |                       |                       |
   arquivo editável           versão preparada         histórico gravado
```

Use terminal isolado do módulo 00. Em lab novo com primeiro commit de note.txt concluído, edite note.txt para linha única second, salve com quebra final, depois rode:

```text
git add note.txt
```

Agora edite note.txt para third e salve com quebra final sem preparar. Confira:

```text
git status --short
git diff --cached
git diff
git show HEAD:note.txt
git show :note.txt
```

Esperado: MM note.txt; HEAD tem practice, index second, arquivo third. Primeiro M é index versus HEAD; segundo M é working tree versus index. Diff cached mostra practice -> second; diff simples second -> third. Caminho com dois-pontos consulta versão preparada.

## Erros comuns e segurança

Confira raiz e identidades efetivas antes de commit. Nunca edite arquivos .git manualmente. Salvar não prepara arquivos. Se resultado divergir, inspecione os dois diffs; não faça reset nem force nada.

## Exercício e autocorreção

Qual versão um commit registraria agora? Dica: siga segunda seta. Resposta: second; third continua editado. Passe se explicar as duas colunas M. Uso profissional: separar mudança revisada de edições não relacionadas.

## Referência rápida

- `git add`
- `git commit`
- `git status`
- `git diff`
- `git show`

## Fontes oficiais

- [Git: git-add](https://git-scm.com/docs/git-add)
- [Git: git-commit](https://git-scm.com/docs/git-commit)
- [Git: git-status](https://git-scm.com/docs/git-status)
- [Git: git-diff](https://git-scm.com/docs/git-diff)
- [Git: git-show](https://git-scm.com/docs/git-show)
