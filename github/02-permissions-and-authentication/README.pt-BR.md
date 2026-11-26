# Permissões e autenticação

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../01-platform-and-repositories/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../03-issues-and-planning/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 25 min

**Pré-requisitos:** [Remotos](../../remote-repositories/README.pt-BR.md) · [Histórico e recuperação](../../history-and-recovery/README.pt-BR.md) · [GitHub, repositórios e visibilidade](../01-platform-and-repositories/README.pt-BR.md)

**Objetivo:** Separar identidade, autenticação e autorização e aplicar privilégio mínimo.

## O que é e por quê

Campos de autor identificam autor declarado; não são credenciais de login. Autenticação verifica acesso à conta; autorização determina ações permitidas. Roles organizacionais incluem read, triage, write, maintain e admin; repositórios pessoais usam modelo diferente. Colaborador com escrita normalmente propõe e envia branches permitidas mas segue rulesets. Owners/admins configuram permissões; revisores avaliam mudanças; mantenedores decidem integração. Use autenticação de dois fatores, gerenciadores HTTPS aprovados ou chaves SSH, e tokens limitados com expiração só se necessário. Nunca guarde credenciais em URLs, Markdown, histórico de shell ou capturas. Assinatura verificada é separada de autorização.

## Prática

Offline: equipe fictícia tem leitor, coordenador de issues, desenvolvedor e administrador. Atribua role organizacional mínima para leitura, triagem, push de branches e alteração de acessos respectivamente. Opcional: confira configurações de segurança da própria conta em privado; não precisa gerar tokens, compartilhar ou alterar roles. Consulte guia oficial antes de clonar sandbox privado; confira conta e repo. Se acesso negado, inspecione conta, remoto e política em vez de elevar permissões.

## Erros comuns e segurança

Não conceda admin apenas para corrigir push rejeitado. Se credencial vazar, revogue ou rotacione imediatamente e notifique responsável; removê-la do último commit não basta. Nunca cole diagnósticos de conta ou tokens em issues.

## Exercício e autocorreção

Resposta: read, triage, write, admin, sujeitos à política organizacional. Passe se nome do autor não for tratado como prova de login e permissões não forem ampliadas desnecessariamente.

## Referência rápida

- `authentication`
- `authorization`
- `least privilege`

## Fontes oficiais

- <https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/repository-roles-for-an-organization>
- <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github>
