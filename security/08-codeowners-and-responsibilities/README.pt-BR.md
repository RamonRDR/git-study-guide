# CODEOWNERS e responsabilidades

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Anterior](../07-branch-protection-and-rulesets/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../09-commit-and-tag-signing/README.pt-BR.md)
<!-- /navigation -->

**Nível:** intermediário · **Tempo estimado:** 35 min

**Pré-requisitos:** [Fluxos profissionais](../../professional-workflows/README.pt-BR.md) · [Proteção de branches e rulesets](../07-branch-protection-and-rulesets/README.pt-BR.md)

**Objetivo:** Explicar padrões de ownership e imposição de review.

## O que é e por quê

CODEOWNERS associa padrões de arquivos a revisores responsáveis em plataformas. Git não impõe. GitHub procura `.github/CODEOWNERS`, `CODEOWNERS` raiz, depois `docs/CODEOWNERS`, usando primeiro encontrado na base do PR; padrão correspondente posterior prevalece. Owners GitHub precisam escrita; solicitação de review não é aprovação obrigatória salvo proteção. GitLab tem locais, sintaxe, seções e regras próprias; aprovação depende de proteção e disponibilidade. Proteja regras de propriedade contra mudanças não autorizadas. Trate padrões e equipes abaixo só como documentação.

## Prática

Para padrões fictícios estilo GitHub abaixo, escolha responsáveis por `docs/guide.md`, `.github/workflows/quality.yml` e `.github/CODEOWNERS`. Explique por que pedido de review sozinho não impõe gate; confira política real. Não crie equipes nem CODEOWNERS no guia.

```text
* @fictional-org/maintainers
/docs/ @fictional-org/docs
/.github/workflows/ @fictional-org/security
/.github/CODEOWNERS @fictional-org/security
```

## Riscos e recuperação

Evite copiar exemplo para repo real: handles fictícios não resolvem. Valide ordem, acesso e regras impostas com mantenedores autorizados; não suponha GitLab com comportamento idêntico.

## Exercício e autocorreção

Docs: equipe docs; workflow: segurança; arquivo ownership: segurança. Aprovação obrigatória é política configurada separada.

## Referência rápida

CODEOWNERS / pattern / owner / required review

## Referências

- <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners>
- <https://docs.gitlab.com/user/project/codeowners/>

---

<!-- navigation-footer -->
[Anterior](../07-branch-protection-and-rulesets/README.pt-BR.md) · [Índice](../README.pt-BR.md) · [Próximo](../09-commit-and-tag-signing/README.pt-BR.md)
<!-- /navigation-footer -->
