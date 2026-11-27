# Meu primeiro repositório

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Módulo anterior](../../command-reference/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo módulo](../../exercises/README.pt-BR.md)
<!-- /navigation -->

**Nível:** iniciante · **Tempo estimado:** 30 min

**Pré-requisitos:** [Primeiro repositório](../../getting-started/03-first-repository/README.pt-BR.md) · [Três locais](../../git-architecture/01-three-locations/README.pt-BR.md) · [Status, add e commit](../../basic-commands/02-status-add-commit/README.pt-BR.md). Git 2.40+ e Bash (Linux/macOS ou Git Bash no Windows).

**Objetivo:** Criar repositório local privado de notas e demonstrar que um commit registra o index, não toda edição dos arquivos de trabalho.

## Cenário

Você mantém arquivo fictício de notas com estado draft e ready. Uma terceira edição experimental não deve entrar no histórico. Não é necessário remoto, conta ou programação.

## Preparação descartável

Abra um shell Bash comum dedicado, não o diretório de trabalho do guia. Execute os comandos um por vez. Pare se qualquer um falhar, especialmente criação do diretório temporário ou cd. Confirme que a raiz impressa é o novo repositório sandbox, ambas identidades são fictícias e a saída de remote está vazia. A configuração isolada vale só para este shell, não é sandbox de segurança reforçada.

```bash
sandbox=$(mktemp -d)
printf 'Sandbox: %s\n' "$sandbox"
for key in $(compgen -e); do
  case "$key" in GIT_*) unset "$key";; esac
done
mkdir "$sandbox/home" "$sandbox/template"
export HOME="$sandbox/home" USERPROFILE="$sandbox/home"
export XDG_CONFIG_HOME="$sandbox/home"
export GIT_CONFIG_NOSYSTEM=1 GIT_CONFIG_GLOBAL="$sandbox/gitconfig"
export GIT_CONFIG_COUNT=0 GIT_TERMINAL_PROMPT=0
export GIT_TEMPLATE_DIR="$sandbox/template"
git init -b main "$sandbox/repo"
cd "$sandbox/repo"
git config --local user.name 'Study Guide Example'
git config --local user.email 'learner@example.invalid'
git config --local commit.gpgsign false
git config --local core.autocrlf false
git config --local core.hooksPath "$sandbox/no-hooks"
git rev-parse --show-toplevel
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
git remote
```

## Desafio

Crie notes.txt contendo status: draft e faça o primeiro commit. Altere para status: ready e prepare no staging; depois altere o arquivo de trabalho para status: experiment sem preparar novamente. Inspecione os três locais. Registre apenas o snapshot ready. Confirme que experiment continua não preparado e então descarte intencionalmente apenas essa edição fictícia. Termine na main com dois commits e working tree limpa. Tente sem consultar a solução.

## Dicas progressivas

1. Use git status e git add para distinguir arquivo não rastreado de mudança preparada.
2. Compare git show HEAD:notes.txt, git show :notes.txt e arquivo de trabalho. git diff e git diff --cached comparam locais diferentes.
3. Commit comum registra o index. Após confirmar que edição restante é descartável, restaure apenas esse caminho de trabalho a partir do index.

## Solução de referência

Primeiro, crie e registre draft. A saída inicial de porcelain é ?? notes.txt.

```bash
printf '%s\n' 'status: draft' > notes.txt
git status --porcelain=v1
git add notes.txt
git diff --cached
git commit -m 'docs: initialize notes'
```

Depois, prepare ready e edite novamente o arquivo de trabalho. Espere MM notes.txt antes do commit: index e arquivo diferem de seus respectivos pontos de comparação. HEAD contém draft, index contém ready e arquivo contém experiment. Após commit, HEAD contém ready e porcelain mostra espaço inicial seguido de M.

```bash
printf '%s\n' 'status: ready' > notes.txt
git add notes.txt
printf '%s\n' 'status: experiment' > notes.txt
git status --porcelain=v1
git show HEAD:notes.txt
git show :notes.txt
git diff
git diff --cached
git commit -m 'docs: mark notes ready'
git show HEAD:notes.txt
git status --porcelain=v1
```

Só depois de verificar que a linha experimental é deliberadamente descartável, restaure o arquivo de trabalho a partir do index. Isso descarta a edição não preparada; não use em trabalho valioso.

```bash
git restore --worktree -- notes.txt
git status --porcelain=v1
git log --oneline
git rev-list --count HEAD
git branch --show-current
git remote
```

## Critérios de sucesso

- Exatamente dois commits alcançáveis da main; segundo contém status: ready, seu pai contém status: draft.
- Arquivo de trabalho e index correspondem a HEAD; saída porcelain vazia.
- Branch atual main; nenhum remoto.
- Explique por que snapshot ready preparado foi registrado enquanto experiment permaneceu não preparado. Working tree limpa sozinha não prova snapshot pretendido.

Teste de manutenção: tests/test_git_practical_projects.py, test_first_repository_staged_snapshot. Confere estados intermediários e finais, incluindo candidato final sujo intencionalmente incorreto. Executa apenas comandos fixos, não submissões de alunos.

## Recuperação e limpeza

Se estado divergir, pare e inspecione status, diff e diff preparado. Preserve conteúdo valioso antes de restaurar; Git não garante recuperação de edições não preparadas descartadas. Feche o shell dedicado e remova só o diretório sandbox impresso pelo gerenciador de arquivos após conferir seu conteúdo. Nunca remova repositório real.

## Fontes oficiais

- <https://git-scm.com/docs/git-init>
- <https://git-scm.com/docs/git-status>
- <https://git-scm.com/docs/git-add>
- <https://git-scm.com/docs/git-commit>
- <https://git-scm.com/docs/git-restore>

---

<!-- navigation-footer -->
[Módulo anterior](../../command-reference/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo módulo](../../exercises/README.pt-BR.md)
<!-- /navigation-footer -->
