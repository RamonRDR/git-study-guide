# GitHub, repositórios e visibilidade

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Módulo anterior](../../history-and-recovery/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../02-permissions-and-authentication/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 25 min

**Pré-requisitos:** [Remotos](../../remote-repositories/README.pt-BR.md) · [Histórico e recuperação](../../history-and-recovery/README.pt-BR.md)

**Objetivo:** Distinguir dados locais do Git de serviços hospedados e escolher visibilidade segura.

## O que é e por quê

Git funciona sem GitHub. GitHub hospeda repositórios Git e adiciona navegação web, identidades, controle de acesso, issues e pull requests. Clone é repositório Git local; publicar envia objetos e refs selecionados ao servidor. Público permite leitura pública, não push por qualquer pessoa. Privado limita acesso mas não serve para segredos. Visibilidade internal é recurso organizacional/enterprise, não exigido aqui. Repositório público não é automaticamente open source: licença determina direitos de reutilização. README explica projeto; LICENSE concede direitos; CONTRIBUTING descreve contribuições; SECURITY indica canal privado de relato quando disponível.

## Prática

Offline: desenhe clone local -> repositório Git remoto -> recursos web GitHub. Classifique commit, branch, issue, pull request e label por camada. Opcional: visite repositório público no navegador sem postar. Confira branch padrão, arquivos, histórico, licença e visibilidade. Para praticar criação use repo pessoal descartável novo study-sandbox, privado por padrão, só README fictício. Nunca use repos de empregador ou guia. Antes de publicar inspecione todo histórico commitado, identidade e arquivos; não precisa mudar visibilidade. Sandbox hospedado criado com README inicial tem primeiro commit próprio; clone em vez de combinar históricos não relacionados.

## Erros comuns e segurança

Mudar público para privado não recolhe clones existentes ou todas as cópias; tornar privado público expõe histórico. Pare se conteúdo confidencial; não experimente visibilidade em repos reais. Faça backup independente antes de exclusão autorizada; limpeza pode ser apenas deixar sandbox privado vazio sem uso.

## Exercício e autocorreção

Visitante pode fazer push por padrão em repo público? Não. Passe se distinguir leitura, permissão de escrita e licença, e identificar três conceitos Git nativos e dois hospedados.

## Referência rápida

- `Git`
- `GitHub`
- `README`
- `LICENSE`

## Fontes oficiais

- <https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories>
- <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility>

---

<!-- navigation-footer -->
[Módulo anterior](../../history-and-recovery/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../02-permissions-and-authentication/README.pt-BR.md)
<!-- /navigation-footer -->
