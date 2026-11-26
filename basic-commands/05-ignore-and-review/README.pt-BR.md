# Regras de ignore e revisão final

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../04-move-and-remove/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo módulo](../../branches/README.pt-BR.md)
<!-- /navigation -->

**Nível:** iniciante · **Tempo estimado:** 30 min

**Pré-requisitos:** [Renomear e remover arquivos rastreados](../04-move-and-remove/README.pt-BR.md)

**Objetivo:** Usar .gitignore e entender por que rastreados ignorados continuam rastreados.

## O que é e por quê

Arquivo .gitignore contém padrões para caminhos intencionalmente não rastreados, como saídas geradas. Barra inicial ancora padrão relativo ao ignore; barra final casa diretórios; * casa dentro de componentes; ! pode negar regra anterior (mas não reincluir arquivo se pai excluído). Git também suporta .git/info/exclude local e core.excludesFile global; lab usa só .gitignore compartilhado. Ignore não é criptografia, controle de acesso nem remoção de histórico. Rastreados não são afetados até remoção do index.

## Prática

Continue lab: draft.txt não rastreado. Crie .gitignore de texto simples na raiz com linhas abaixo e report.tmp fictício contendo sample (nunca segredos reais):

```text
/draft.txt
*.tmp
!keep.tmp
/build/
```

Crie keep.tmp com keep. Confira:

```text
git status --short --ignored
git check-ignore -v -- draft.txt report.tmp
git add -- .gitignore keep.tmp
git diff --cached --name-status
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Esperado: draft.txt/report.tmp ignorados (!!), keep.tmp não rastreado antes do add, depois preparado com .gitignore. Se diff e identidades fictícias corretos, registre. 

```text
git commit -m "docs: add ignore rules"
```

Só agora acrescente /keep.tmp ao .gitignore e edite keep.tmp para updated; salve ambos. Depois:

```text
git status --short
git ls-files -- keep.tmp
git check-ignore --no-index -v -- keep.tmp
```

Rode últimos três comandos DEPOIS das mudanças no editor. Esperado: ambos rastreados modificados, keep.tmp continua rastreado, --no-index mostra regra mesmo para rastreado. Não prepare keep.tmp. Opcionalmente pare de rastreá-lo como exercício local deliberado, confira exclusão preparada e prepare só mudança de ignore:

```text
git rm --cached -- keep.tmp
git add -- .gitignore
git diff --cached --name-status
git status --short --ignored
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Esperado: exclusão preparada keep.tmp, modificação .gitignore, keep.tmp permanece no disco e ignorado. Registre só se esperado e identidades fictícias verificadas:

```text
git commit -m "docs: stop tracking generated file"
git status --short --ignored
git ls-files
```

## Erros comuns e segurança

Se segredo foi commitado, ignore ou rm --cached não basta; revogue/rotacione credencial e siga processo de incidente (módulo 12). Nunca force inclusão de conteúdo sensível. Revise status, diff cached, identidade e histórico. Para terminar feche editor e shell dedicado, depois exclua APENAS pasta pai temporária exata anotada no módulo 00 pelo gerenciador, se não precisar.

## Exercício e autocorreção

Por que keep.tmp ainda aparece modificado após regra ignore? Resposta: já rastreado. Passe se distinguir ignorar, parar de rastrear e apagar, e explicar por que segredo ignorado no histórico ainda é problema. Uso profissional: revisar ignore de gerados antes do primeiro commit.

## Referência rápida

- `gitignore`
- `git check-ignore`
- `git rm`
- `git status`

## Fontes oficiais

- [Git: gitignore](https://git-scm.com/docs/gitignore)
- [Git: git-check-ignore](https://git-scm.com/docs/git-check-ignore)
- [Git: git-rm](https://git-scm.com/docs/git-rm)
- [Git: git-status](https://git-scm.com/docs/git-status)

---

<!-- navigation-footer -->
[Anterior](../04-move-and-remove/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo módulo](../../branches/README.pt-BR.md)
<!-- /navigation-footer -->
