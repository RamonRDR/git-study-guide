# Visibilidade, permissões e autenticação

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../01-projects-groups-and-offerings/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../03-issues-labels-milestones-and-boards/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 35 min

**Pré-requisitos:** [GitHub](../../github/README.pt-BR.md) · [Remotos](../../remote-repositories/README.pt-BR.md)

**Objetivo:** Separar identidade, permissões efetivas e visibilidade de leitura; escolher acesso mínimo.

## O que é e por quê

Projetos públicos expõem conteúdo público à leitura, não escrita irrestrita. Privado limita acesso a membros elegíveis; visibilidade interna está disponível em Self-Managed e Dedicated, não GitLab.com. Interno não é privado: usuários autenticados elegíveis podem ler. Papéis típicos incluem Guest, Planner, Reporter, Developer, Maintainer e Owner; capacidades exatas dependem de plano, configurações e recurso. Reporter geralmente serve para leitura de repositório, Developer para branches de funcionalidade, Maintainer para gestão de projeto e Owner para propriedade de alto nível. Acesso efetivo pode ser herdado dos grupos; reduzir um vínculo direto pode não remover acesso herdado. Autenticação estabelece identidade; autorização determina operações permitidas. Use login web com 2FA, SSH com fingerprint do host verificado e chave pública (mantenha a privada local), ou HTTPS com gerenciador de credenciais adequado ou token de escopo mínimo e expiração. Nome/e-mail do Git atribuem commits, não autenticam. Nunca coloque tokens em URLs de remotos ou comandos.

## Prática

Offline, atribua papéis a analista de leitura, colaborador e mantenedor de um projeto privado fictício; justifique cada papel e rastreie um Developer herdado do grupo pai. Opcional: inspecione visibilidade e seu papel em sandbox privado descartável próprio, sem alterar permissões ou criar tokens. Se acesso for negado, verifique host, identidade, associação, restrições da branch e escopo da credencial antes de escalar.

## Erros comuns e segurança

Alterar visibilidade não recolhe cópias. Se uma credencial vazar, revogue/rotacione imediatamente e siga a política de incidentes; apagar commit não basta. Nunca desative verificação de host nem conceda Owner para corrigir erro comum de autenticação.

## Exercício e autocorreção

Um leitor público pode fazer push na main automaticamente? Não. Passe se identificar autorização de leitura, escrita e merge separadas, acesso herdado e não propor segredo no histórico Git.

## Fontes oficiais

- <https://docs.gitlab.com/user/public_access/>
- <https://docs.gitlab.com/user/permissions/>
- <https://docs.gitlab.com/user/ssh/>
- <https://docs.gitlab.com/user/profile/personal_access_tokens/>
- <https://docs.gitlab.com/user/profile/account/two_factor_authentication/>

---

<!-- navigation-footer -->
[Anterior](../01-projects-groups-and-offerings/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../03-issues-labels-milestones-and-boards/README.pt-BR.md)
<!-- /navigation-footer -->
