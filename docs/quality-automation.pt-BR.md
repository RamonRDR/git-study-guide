# Automação de qualidade

[English](quality-automation.md) · [Português](quality-automation.pt-BR.md) · [Español](quality-automation.es.md)

Mantenedores precisam de Git (2.28 ou superior para a opção initial-branch) e Python 3.12; Python e CI não são pré-requisitos de estudo. Na raiz, adicionar arquivos novos ao index antes de validar, pois checks inspecionam caminhos rastreados. Executar:

```text
python scripts/validate.py
python -m unittest discover -s tests -v
```

Usar --check com structure, locales, links, navigation, examples, secrets command-catalog ou assessment-pilot para isolar um check. Validadores inspecionam caminhos rastreados portáveis, presença dos três idiomas, links relativos e imagens Markdown inline, ordem/navegação de módulos e capítulos, política de exemplos executáveis e padrões comuns de segredos. Não provam tradução semântica, links externos, âncoras, todas as sintaxes Markdown, ausência de todos os segredos ou comportamento da UI de templates. Detector informa arquivo e linha, não valores; é heurístico, não completo. Revisar diffs e rotacionar credenciais expostas separadamente.

A validação de navegação exige blocos canônicos localizados de cabeçalho e rodapé para cada índice de módulo e capítulo, rótulos e caminhos exatos, transições entre capítulos e módulos, posicionamento e detecção de duplicidade. Testes incluem casos negativos de navegação ausente, divergente, reordenada, em idioma errado, invertida, oculta ou mal posicionada. Índices planejados permanecem navegáveis; suas aulas ainda não foram publicadas.

O check command-catalog valida as 14 categorias JSON registradas, no mínimo 101 operações distintas (meta aprovada de 120), mapas de idiomas, riscos, política de URLs de fontes oficiais, capítulos relacionados, intenções e igualdade exata com o renderizador canônico. Não executa comandos do catálogo nem comprova tradução semântica, disponibilidade de URLs externas ou correção de todo exemplo. Para alterar o catálogo, edite o JSON canônico, prepare novas entradas e regenere o Markdown registrado a partir da raiz:

```text
python scripts/render_command_reference.py --write
```

Prepare as páginas geradas, execute `python scripts/validate.py --check command-catalog`, depois todos os validadores e testes. A invocação padrão do renderizador confere conteúdo gerado sem gravar.

Ainda não há exemplos didáticos executáveis aprovados. O manifesto vazio é um gate que bloqueia por padrão: todos os arquivos em examples/ (incluindo arquivos inertes e variações de maiúsculas/minúsculas) são rejeitados, independentemente de extensão ou modo, e manifestos não vazios falham até existir protocolo de execução revisado. Não executar código arbitrário de estudantes. Teste inicial Git usa repo temporário isolado e verifica staging, branch, conteúdo commitado e status limpo. Sprints futuras ampliam cenários determinísticos. Rodar testes locais somente de revisões confiáveis e revisadas.

A Sprint 16 adiciona oito testes fixos de integração para resultados dos projetos, incluindo estados intermediários, conflito esperado e snapshots registrados inválidos. Executam em repositórios temporários isolados e origens bare locais; os testes não extraem nem executam Markdown ou submissões de alunos. Fluxos hospedados permanecem simulações não executadas. Rode suíte completa e inspecione logs reais Ubuntu/Windows do SHA mais recente.

CI usa runners padrão hospedados pelo GitHub Linux e Windows em pull_request e pushes na main, com permissão contents somente leitura, actions oficiais fixadas por SHA, sem credenciais persistidas de checkout, sem segredos, sem runners próprios e sem serviço pago. Cada job limitado a dez minutos. Código de PR continua não confiável; runners descartáveis não são ambientes privilegiados de deploy. Conferir runs reais na última revisão; checks obrigatórios exigem aprovação separada após observar nomes.

- [Estrutura do projeto](project-structure.pt-BR.md)
- [GitHub Actions security](https://docs.github.com/en/actions/reference/security/secure-use)

O check assessment-pilot verifica quatro bancos versionados, contagens exatas por dificuldade, IDs globalmente únicos, pré-requisitos e referências de simulados válidos, campos localizados, escolhas, respostas, predicados de estado permitidos e igualdade com Markdown gerado. Edite records.json, prepare JSON e currículo, rode python scripts/render_assessments.py --write; prepare páginas geradas e rode python scripts/validate.py --check assessment-pilot e todos checks/testes. Os 12 cenários fixos de QA exercitam estados Git válidos e incorretos representativos. Nenhum avaliador executa submissões de alunos ou lê repos arbitrários; só fixtures descartáveis confiáveis são suportadas. Validação estrutural não prova tradução semântica ou exatidão educacional.

- [Schema do piloto de avaliações](assessment-pilot.pt-BR.md)
