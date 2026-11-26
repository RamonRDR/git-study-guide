# Autenticação segura e plataformas de hospedagem

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../04-remote-branch-lifecycle/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo módulo](../../history-and-recovery/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 20 min

**Pré-requisitos:** [Ciclo de vida de branches remotas e prune](../04-remote-branch-lifecycle/README.pt-BR.md)

**Objetivo:** Escolher métodos seguros de acesso sem criar ou expor credenciais.

## O que é e por quê

Autenticação comprova quem pode acessar um serviço; autorização controla ações permitidas. Identidade de autor de commit é metadado, não autenticação. HTTPS usa TLS para proteger transporte; provedores podem exigir tokens ou login pelo navegador em vez de senha da conta. SSH usa par de chaves privada/pública; a privada permanece privada, e o serviço recebe a pública. Verifique chaves do host contra fingerprints oficiais confiáveis de forma independente antes de aceitar; nunca desative verificação de host ou TLS. Credential helper ou manager armazena/recupera credenciais; prefira armazenamento seguro do SO, não texto simples. Tokens devem ter escopo mínimo de repo/ação, expirar quando viável e ser revogados quando desnecessários.

## Prática

Nenhuma operação online é obrigatória. No lab local concluído não foi necessária autenticação em serviço externo. Para clone hipotético somente leitura, compare formatos fictícios de URL (não execute): `https://example.invalid/team/project.git` e `git@example.invalid:team/project.git`. HTTPS e SSH alteram conexão do Git, não IDs de commits, refs ou semântica de merge. Antes de prática online futura opcional, use instruções oficiais do provedor e repo descartável próprio autorizado. Confira destinos de fetch/push privadamente, host e permissões, depois escolha menor privilégio. Não coloque tokens em URLs, argumentos, arquivos fonte, capturas ou logs. Não cole chaves privadas ou tokens neste guia nem em ferramentas de IA. Git implementa clone/fetch/push; pull requests, merge requests, checks obrigatórios e proteção de branches são recursos de GitHub/GitLab, abordados depois. Um remoto pode recusar atualização válida por permissões ou política. Um bare Git nativo também pode aplicar hooks/políticas, mas não fornece interface de PR hospedada por si.

## Erros comuns e segurança

Se autenticação falhar, verifique URL, conta, validade da credencial e permissões pela documentação oficial; não amplie acesso indiscriminadamente. Se credencial vazar, revogue/rotacione imediatamente e avise o responsável; excluir arquivo ou commit não basta. Não imprima configuração completa ou conteúdo de credenciais para diagnóstico. Nenhuma autenticação externa foi testada neste módulo.

## Exercício e autocorreção

Um colega precisa ler um repo. Você deve compartilhar token amplo ou chave SSH privada? Dica: identidade e menor privilégio. Resposta: nenhum; conceda acesso individual autorizado com permissões mínimas. Passe se explicar autenticação versus metadados de autor, HTTPS versus SSH e por que PR não é comando Git.

## Referência rápida

- `git remote get-url origin`
- `git remote get-url --push origin`
- `git help credentials`

## Fontes oficiais

- [Git: gitcredentials](https://git-scm.com/docs/gitcredentials)
- [Git: git-clone](https://git-scm.com/docs/git-clone)
- [Git: git-config](https://git-scm.com/docs/git-config)
- [GitHub: authentication](https://docs.github.com/en/authentication)
- [GitLab: SSH](https://docs.gitlab.com/user/ssh/)
- [GitLab: access tokens](https://docs.gitlab.com/user/profile/personal_access_tokens/)

---

<!-- navigation-footer -->
[Anterior](../04-remote-branch-lifecycle/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo módulo](../../history-and-recovery/README.pt-BR.md)
<!-- /navigation-footer -->
