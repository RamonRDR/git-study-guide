# Remotos, repositórios bare e clones

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Módulo anterior](../../merge-and-conflicts/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../02-fetch-and-tracking/README.pt-BR.md)
<!-- /navigation -->

**Nível:** iniciante · **Tempo estimado:** 35 min

**Pré-requisitos:** [Laboratório isolado](../../getting-started/03-first-repository/README.pt-BR.md) · [Primeiro commit](../../getting-started/05-first-commit/README.pt-BR.md) · [Merge e conflitos](../../merge-and-conflicts/README.pt-BR.md)

**Objetivo:** Explicar aliases de remotos e criar clones independentes sem conta.

## O que é e por quê

Um remoto é outro repositório Git, não necessariamente um servidor na internet. Um repositório bare armazena histórico e refs sem uma árvore de trabalho normal em checkout. É útil como ponto de troca compartilhado. Clone cria um novo repositório, baixa o histórico e normalmente faz checkout da branch indicada pelo HEAD remoto. Origin é uma convenção criada pelo clone; upstream pode ser outro alias, frequentemente o projeto original em um fluxo com fork. Nenhum é reservado. Uma branch de tracking upstream é, por sua vez, uma relação configurada entre uma branch local e outra ref. GitHub e GitLab acrescentam hospedagem, revisão e permissões sobre o Git.

## Prática

Crie um NOVO laboratório descartável seguindo o módulo 00 capítulo 03 e a aula do primeiro commit. Use Git 2.40+ e a mesma sessão dedicada Bash ou PowerShell com configuração system/global isolada, variáveis Git herdadas limpas e template vazio. Verifique que repo/main tem exatamente um commit com note.txt = practice, status limpo e ambas as identidades fictícias. Registre o caminho do pai temporário em privado. Suba um nível com `cd ..`; confira `pwd` (Bash) ou `Get-Location` (PowerShell). Pare se não for exatamente esse pai ou se houver algo além de repo, template e gitconfig. Restrinja o transporte nesta sessão a arquivos locais: Bash `export GIT_ALLOW_PROTOCOL=file`, PowerShell `$env:GIT_ALLOW_PROTOCOL = 'file'`. Execute individualmente, pare em erros inesperados. Após remote -v confira que ambas as URLs resolvem para o origin.git recém-criado antes de enviar. Esperado: true para bare, refs/heads/main para HEAD. O repo inicial serve apenas para publicar o primeiro commit.
```text
git init --bare --initial-branch=main origin.git
git -C origin.git rev-parse --is-bare-repository
git -C origin.git symbolic-ref HEAD
git -C repo remote add origin ../origin.git
git -C repo remote -v
```

Confira que ambas as URLs resolvem para o origin.git local recém-criado. Só então continue:

```text
git -C repo push -u origin main
git -C origin.git rev-parse refs/heads/main
git clone --no-local origin.git alice
git clone --no-local origin.git bob
```
Configure identidades locais nos clones (clone não copia a identidade local do repo inicial).
```text
git -C alice config --local user.name "Study Guide Example"
git -C alice config --local user.email learner@example.invalid
git -C alice config --local commit.gpgsign false
git -C alice config --local core.autocrlf false
git -C bob config --local user.name "Study Guide Example"
git -C bob config --local user.email learner@example.invalid
git -C bob config --local commit.gpgsign false
git -C bob config --local core.autocrlf false
```

```text
git -C alice rev-parse --show-toplevel
git -C bob rev-parse --show-toplevel
git -C alice remote -v
git -C bob remote -v
git -C alice branch -vv
git -C bob branch -vv
git -C alice status --short
git -C bob status --short
```
As raízes devem ser as pastas alice/bob previstas, as URLs origin devem resolver para o mesmo origin.git local, main acompanha origin/main e o status está limpo. Os três tips main são iguais ao commit inicial. `--no-local` usa o transporte Git normal em vez de otimizações de cópia local. Mantenha a sessão dedicada no pai para os capítulos 02–04. Diagrama: repo (inicial) -> origin.git (bare); alice e bob têm HEAD, árvore de trabalho, index e refs próprios; ambos trocam commits com origin.git. Na prática de configuração, o alias temporário aponta para o MESMO bare, não para um segundo servidor.
```text
git -C alice remote add upstream ../origin.git
git -C alice remote set-url upstream .././origin.git
git -C alice remote rename upstream training
git -C alice remote get-url training
git -C alice remote remove training
git -C alice remote -v
```
Esperado: resta apenas origin; remover alias elimina configuração local e suas refs de tracking, não o repositório remoto. Alterar URL não migra histórico. Em fluxo profissional com fork, origin frequentemente nomeia seu fork e upstream o original; verifique ambos.

## Erros comuns e segurança

Nunca clone ou envie para URL desconhecida. Clone não concede autenticação; identidade local não é autorização. Se caminhos ou identidades diferirem, pare e reinicie o laboratório em vez de alterar configurações reais. Não reutilize a sessão para remotos reais.

## Exercício e autocorreção

Por que o origin bare não tem note.txt em checkout? Dica: separe histórico e árvore de trabalho. Resposta: o arquivo existe nos snapshots dos commits, não em uma árvore normal. Passe se ambos os clones mostrarem o mesmo ID main inicial e raízes independentes.

## Referência rápida

- `git init --bare --initial-branch=main`
- `git clone --no-local`
- `git remote -v`
- `git remote add / set-url / rename / remove`

## Fontes oficiais

- [Git: git-init](https://git-scm.com/docs/git-init)
- [Git: git-clone](https://git-scm.com/docs/git-clone)
- [Git: git-remote](https://git-scm.com/docs/git-remote)

---

<!-- navigation-footer -->
[Módulo anterior](../../merge-and-conflicts/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../02-fetch-and-tracking/README.pt-BR.md)
<!-- /navigation-footer -->
