# Autenticação SSH e identidade do host

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../01-security-foundations/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../03-https-and-access-tokens/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 40 min

**Pré-requisitos:** [Fluxos profissionais](../../professional-workflows/README.pt-BR.md) · [Fundamentos de segurança no Git](../01-security-foundations/README.pt-BR.md)

**Objetivo:** Explicar pares de chaves e verificação segura do host.

## O que é e por quê

SSH usa par criptográfico: chave pública pode ser registrada no provedor; privada fica sob controle do usuário. Servidor tem chave de host, cujo fingerprint deve ser verificado por fonte independente confiável na primeira conexão ou mudança inesperada. Passphrase protege chave privada em repouso; agente pode manter chaves desbloqueadas temporariamente. Autenticação SSH não concede escrita nem assina commits automaticamente. `ssh -T git@github.com` é teste opcional específico do host após configuração; GitHub não fornece shell interativo e autenticação bem-sucedida documentada pode retornar status diferente de zero. Use instruções oficiais para geração, algoritmos, registro e revogação.

## Prática

Offline: rotule chave pública, privada, passphrase e fingerprint do servidor em diagrama fictício. Compare `git@host.example.invalid:team/catalog.git` com URL HTTPS. Se fingerprint mudar inesperadamente, escreva próxima ação segura. Não exige gerar chaves nem rede.

## Riscos e recuperação

Nunca cole chaves privadas ou desative verificação do host. Não remova entrada known-host às cegas para silenciar aviso. Verifique independentemente, investigue mudanças e revogue chave exposta em cada provedor onde autorizada.

## Exercício e autocorreção

Chave pública pode ser registrada; privada e passphrase ficam privadas; pare diante de fingerprint inesperado e verifique independentemente.

## Referência rápida

public key / private key / host fingerprint / agent

## Referências

- <https://docs.github.com/en/authentication/connecting-to-github-with-ssh>
- <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection>
- <https://docs.gitlab.com/user/ssh/>
