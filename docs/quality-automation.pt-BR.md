# Automação de qualidade

[English](quality-automation.md) · [Português](quality-automation.pt-BR.md) · [Español](quality-automation.es.md)

Mantenedores precisam de Git (2.28 ou superior para a opção initial-branch) e Python 3.12; Python e CI não são pré-requisitos de estudo. Na raiz, adicionar arquivos novos ao index antes de validar, pois checks inspecionam caminhos rastreados. Executar:

```text
python scripts/validate.py
python -m unittest discover -s tests -v
```

Usar --check com structure, locales, links, navigation, examples ou secrets para isolar um check. Validadores inspecionam caminhos rastreados portáveis, presença dos três idiomas, links relativos e imagens Markdown inline, ordem/navegação de módulos e capítulos, política de exemplos executáveis e padrões comuns de segredos. Não provam tradução semântica, links externos, âncoras, todas as sintaxes Markdown, ausência de todos os segredos ou comportamento da UI de templates. Detector informa arquivo e linha, não valores; é heurístico, não completo. Revisar diffs e rotacionar credenciais expostas separadamente.

A validação de navegação exige blocos canônicos localizados de cabeçalho e rodapé para cada índice de módulo e capítulo, rótulos e caminhos exatos, transições entre capítulos e módulos, posicionamento e detecção de duplicidade. Testes incluem casos negativos de navegação ausente, divergente, reordenada, em idioma errado, invertida, oculta ou mal posicionada. Índices planejados permanecem navegáveis; suas aulas ainda não foram publicadas.

Ainda não há exemplos didáticos executáveis aprovados. O manifesto vazio é um gate que bloqueia por padrão: todos os arquivos em examples/ (incluindo arquivos inertes e variações de maiúsculas/minúsculas) são rejeitados, independentemente de extensão ou modo, e manifestos não vazios falham até existir protocolo de execução revisado. Não executar código arbitrário de estudantes. Teste inicial Git usa repo temporário isolado e verifica staging, branch, conteúdo commitado e status limpo. Sprints futuras ampliam cenários determinísticos. Rodar testes locais somente de revisões confiáveis e revisadas.

CI usa runners padrão hospedados pelo GitHub Linux e Windows em pull_request e pushes na main, com permissão contents somente leitura, actions oficiais fixadas por SHA, sem credenciais persistidas de checkout, sem segredos, sem runners próprios e sem serviço pago. Cada job limitado a dez minutos. Código de PR continua não confiável; runners descartáveis não são ambientes privilegiados de deploy. Conferir runs reais na última revisão; checks obrigatórios exigem aprovação separada após observar nomes.

- [Estrutura do projeto](project-structure.pt-BR.md)
- [GitHub Actions security](https://docs.github.com/en/actions/reference/security/secure-use)
