# Tags e GitHub Releases

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../06-protection-and-rulesets/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../08-github-cli/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 30 min

**Pré-requisitos:** [Remotos](../../remote-repositories/README.pt-BR.md) · [Histórico e recuperação](../../history-and-recovery/README.pt-BR.md) · [Branch protection, rulesets e quality gates](../06-protection-and-rulesets/README.pt-BR.md) · [Primeiro repositório](../../getting-started/03-first-repository/README.pt-BR.md) · [Primeiro commit](../../getting-started/05-first-commit/README.pt-BR.md)

**Objetivo:** Distinguir refs Git de versão de metadados de release e verificar alvo.

## O que é e por quê

Tag é ref Git que nomeia objeto, normalmente commit. Lightweight aponta diretamente; annotated guarda objeto tag com metadados e mensagem. Branches normalmente avançam; tags de release devem permanecer estáveis. GitHub Release adiciona notas hospedadas, assets baixáveis e estado draft/prerelease associado a tag. Publicar release não é deploy automático. SemVer usa MAJOR.MINOR.PATCH para compatibilidade API pública; v0.1.0 é grafia comum de tag de desenvolvimento inicial, não garantia de estabilidade. Assets de release são separados de histórico Git fonte; verifique origem, integridade e permissões antes de usar.

## Prática

Lab local offline: inicie repo isolado novo pelas aulas de primeiro repo e commit do módulo 00. Confirme raiz descartável registrada, main limpa com um commit fictício, sem remotos, sem tags e identidades efetivas fictícias. Execute individualmente e pare em saída inesperada. Comandos abaixo criam tag anotada local, inspecionam tipo e comparam commit resolvido com HEAD. Sem push. Rascunhe release notes com escopo, verificação e limites. Opcional somente leitura: inspecione release pública e tag, sem baixar ou executar assets.

```text
git rev-parse --show-toplevel
git branch --show-current
git status --short
git remote -v
git tag --list
git rev-list --count HEAD
git var GIT_AUTHOR_IDENT
git var GIT_COMMITTER_IDENT
```

Prossiga somente se todas as pré-condições acima forem satisfeitas.

```text
git tag -a v0.1.0 -m "Release 0.1.0"
git cat-file -t v0.1.0
git rev-parse 'v0.1.0^{commit}' HEAD
git show v0.1.0
git status --short
```


## Erros comuns e segurança

Não mova nem exclua tag de release publicada para alterar artefato silenciosamente. Publique correção revisada em nova versão quando adequado. Nunca envie segredos ou binários não verificados. Feche sessão dedicada e exclua só pai descartável registrado se não precisar; nenhuma release hospedada criada.

## Exercício e autocorreção

Passe se tipo do objeto é tag, IDs de commits resolvidos coincidem, main não muda e explicar por que notas de release não são commits Git. Se só em papel, preveja saída.

## Referência rápida

- `git tag -a TAG -m MESSAGE`
- `git cat-file -t TAG`
- `git rev-parse 'TAG^{commit}'`

## Fontes oficiais

- <https://git-scm.com/docs/git-tag>
- <https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases>
- <https://semver.org/>
