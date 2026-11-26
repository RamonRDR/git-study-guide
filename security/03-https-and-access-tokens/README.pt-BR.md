# HTTPS e tokens de acesso

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../02-ssh-authentication/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../04-credential-managers/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 35 min

**Pré-requisitos:** [Fluxos profissionais](../../professional-workflows/README.pt-BR.md) · [Autenticação SSH e identidade do host](../02-ssh-authentication/README.pt-BR.md)

**Objetivo:** Escolher credenciais HTTPS com escopo adequado.

## O que é e por quê

HTTPS usa TLS para proteger transporte e autenticar servidor por validação de certificado. PAT é credencial com capacidades, escopo e expiração específicos do provedor, não senha da conta. GitHub não aceita senha da conta em operações Git HTTPS. Tokens fine-grained GitHub podem restringir recursos e permissões; classic têm escopos mais amplos e podem ser necessários em casos não suportados. GitLab oferece tokens pessoais, de projeto e grupo conforme configuração e planos. Prefira credenciais curtas e restritas ou identidades de app gerenciadas quando adequadas. Token ainda pode ser usado indevidamente dentro de permissões mesmo com 2FA.

## Prática

Projete acesso para bot fictício que lê um catálogo privado e nunca escreve. Registre repo, permissão leitura, expiração, responsável e caminho de revogação no papel. Use apenas `https://host.example.invalid/team/catalog.git` como URL fictícia; nunca insira credencial nela.

## Riscos e recuperação

Não desative TLS, coloque tokens em URLs, comandos, arquivos ou screenshots, nem amplie escopo para corrigir falha de autenticação. Confira host, conta, expiração e política privadamente. Revogue e substitua token exposto.

## Exercício e autocorreção

Leitura de um repo, menor duração prática e revogação documentada; sem token real.

## Referência rápida

TLS / PAT / scope / expiration

## Referências

- <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens>
- <https://docs.gitlab.com/user/profile/personal_access_tokens/>
- <https://git-scm.com/docs/gitcredentials>

---

<!-- navigation-footer -->
[Anterior](../02-ssh-authentication/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../04-credential-managers/README.pt-BR.md)
<!-- /navigation-footer -->
