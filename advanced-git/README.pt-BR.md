# 13 Git avançado

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../security/README.pt-BR.md) · [Índice](../docs/learning-path.pt-BR.md) · [Próximo](../git-internals/README.pt-BR.md)
<!-- /navigation -->

**Status: aulas incluídas na Sprint 14.** 470 min. Pré-requisito: segurança e módulos de fluxo anteriores. Git 2.34+ recomendado; Bash (Git Bash no Windows), auxiliar subtree opcional. Sem credenciais online.

## Lab descartável

Abra shell Bash dedicado novo (`bash --noprofile --norc`) antes de cada capítulo; não rode no shell normal. Execute comandos individualmente, parando em falha. Antes de commitar, confira ambas identidades iniciando com `Study Guide Example <learner@example.invalid>`; senão pare. Confira sandbox e raiz impressos, sem remote e status limpo. Os três commits mudam catálogo fictício; dois primeiros bons, último ruim. Não reutilize sandbox antigo.

```bash
sandbox=$(mktemp -d)
printf 'Sandbox: %s\n' "$sandbox"
while IFS= read -r name; do unset "$name"; done < <(compgen -e GIT_)
mkdir "$sandbox/home" "$sandbox/template"
export HOME="$sandbox/home" USERPROFILE="$sandbox/home"
export GIT_CONFIG_GLOBAL="$sandbox/gitconfig" GIT_CONFIG_NOSYSTEM=1
export GIT_CONFIG_COUNT=0 GIT_TEMPLATE_DIR="$sandbox/template"
export GIT_ALLOW_PROTOCOL=file GIT_TERMINAL_PROMPT=0
git init -b main "$sandbox/repo"
cd "$sandbox/repo"
git config --local user.name "Study Guide Example"
git config --local user.email learner@example.invalid
git config --local commit.gpgsign false
git config --local tag.gpgsign false
git config --local core.autocrlf false
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
mkdir docs src
printf '%s\n' ok > src/state.txt
printf '%s\n' catalog > docs/guide.txt
git add -- docs/guide.txt src/state.txt
git commit -m "docs: initial catalog"
printf '%s\n' reviewed > docs/guide.txt
git add -- docs/guide.txt
git commit -m "docs: review guide"
printf '%s\n' bad > src/state.txt
git add -- src/state.txt
git commit -m "docs: regression fixture"
git rev-parse --show-toplevel
git log --oneline -3
git status --short
git remote
```

Use só o lab descartável e dados fictícios. Se estado divergir, pare; inspecione status e operação antes de abortar ou recriar lab. Feche shell dedicado e remova só sandbox anotado pelo gerenciador de arquivos após revisar conteúdo.

## Capítulos

<!-- chapters -->
- 01 [Bisect: localizar uma regressão](01-bisect/README.pt-BR.md)
- 02 [Worktrees: diretórios de trabalho paralelos](02-worktree/README.pt-BR.md)
- 03 [Submodules: dependências fixadas por commit](03-submodules/README.pt-BR.md)
- 04 [Subtree: integrar conteúdo de outra origem](04-subtree/README.pt-BR.md)
- 05 [Hooks: automação local e confiança](05-hooks/README.pt-BR.md)
- 06 [Rerere: reutilizar resoluções de conflitos](06-rerere/README.pt-BR.md)
- 07 [Sparse checkout: selecionar arquivos de trabalho](07-sparse-checkout/README.pt-BR.md)
- 08 [Clones parciais e rasos](08-partial-and-shallow-clone/README.pt-BR.md)
- 09 [Blame e grep: investigar mudanças](09-blame-and-grep/README.pt-BR.md)
- 10 [Archive e bundle: distribuir snapshots ou histórico](10-archive-and-bundle/README.pt-BR.md)
- 11 [Laboratório integrado de Git avançado](11-integrated-advanced-lab/README.pt-BR.md)
<!-- /chapters -->

---

<!-- navigation-footer -->
[Anterior](../security/README.pt-BR.md) · [Índice](../docs/learning-path.pt-BR.md) · [Próximo](../git-internals/README.pt-BR.md)
<!-- /navigation-footer -->
