# Auditoria inicial da Sprint 00

[English](audit.md) · [Português](audit.pt-BR.md) · [Español](audit.es.md)

Auditoria de leitura pela API GitHub antes de criar branch. Git baseline main b4bd782519ebc8e52e6751362443aa634e86e56d; apenas LICENSE e README.md, uma branch protegida e nenhum PR aberto. Público, MIT, somente squash, auto-merge desabilitado, sugestão de atualizar branch e exclusão após merge habilitadas. Ruleset 28108699 ativo para branch padrão, sem bypass, PR e resolução de conversas obrigatórios, 0 aprovações exigidas, histórico linear, exclusão/force push bloqueados, aprovação extra para mudanças sem atribuição, somente squash. Sem checks obrigatórios no ruleset; sem workflow na árvore inicial. Não alterar administração na Sprint 00.

Python baseline main 9102bbbf8f8dd846f2fb9682dd3f55bcacc10c95, público MIT, main protegida e feat/problem-solving-foundations no mesmo SHA. Consultados árvore, AGENTS, constitution, specification, plano, tarefas, critérios, ADRs 0001–0003, orientação de IA, contrato e registro relacionado (representantes em inglês). Encontrados localização, quality-checks.yml, scripts para links, cobertura linguística, estrutura, exemplos e navegação. Reutilizar layout, SDD, processo de review e contrato fixado por revisão; adaptar runtime específico Python, PEP 8 e testes de código para testes de estado Git independentes de linguagem. Sem reexecução de CI Python, auditoria semântica exaustiva de traduções ou alterações no Python. Auditoria não afirma que todo currículo de referência passa.

- [Git baseline](https://github.com/RamonRDR/git-study-guide/commit/b4bd782519ebc8e52e6751362443aa634e86e56d)
- [Ruleset](https://github.com/RamonRDR/git-study-guide/rules/28108699)
- [Python baseline](https://github.com/RamonRDR/python-study-guide/tree/9102bbbf8f8dd846f2fb9682dd3f55bcacc10c95)

## Documentos relacionados

- [Especificação](specification.pt-BR.md)
- [Tarefas](tasks.pt-BR.md)

## QA final Sprint 19B — evidências da base (em andamento)

Base imutável: [03c3043](https://github.com/RamonRDR/git-study-guide/commit/03c30438a5490d6c8f9b22dbf457a644658e042f). [Encerramento da Sprint 19A](https://github.com/RamonRDR/git-study-guide/pull/21#issuecomment-7227417357): [CI push](https://github.com/RamonRDR/git-study-guide/actions/runs/46061260750) e [CI manual](https://github.com/RamonRDR/git-study-guide/actions/runs/46062482507) passaram nove validadores e 152 testes por SO; tree revisada, pai único, metadados noreply, assinatura verificada e exclusão de branch confirmados. Cancelamento efetivo de execuções obsoletas de PR ainda não exercitado.

Conferência independente do inventário: 637 arquivos regulares rastreados; 18 módulos, 141 IDs únicos de capítulos, 423 caminhos únicos de capítulos localizados e 54 caminhos de índices localizados presentes; nenhuma ausência de idioma ou divergência na sequência global de navegação; 159 associações de avaliações e 312 de comandos. Schema do manifesto 1.0.0.

Amostragem semântica dirigida de trechos de seis capítulos nos três idiomas (18 arquivos): primeiro commit, resolução de conflitos, reset, secrets/prevenção de vazamentos, refs e HEAD e O commit perdido. Comparação de explicações centrais, condições de segurança e estados esperados; nenhuma divergência material nos trechos amostrados. Conteúdo dos blocos cercados coincide nos seis conjuntos. Não equivale a auditoria semântica integral de traduções, execução de todos os labs, teste macOS, auditoria de links externos ou validação de runtime navegador.

AC-19 continua em andamento: READMEs finais localizados, identidade aprovada pelo mantenedor ou exceção explícita, badges verídicos, QA aplicável restante e limitações, handoff revisado e evidência imutável de release aprovada. Não criar tag nem publicar ainda. Sem mudanças em outros repositórios.
