# Desenvolvimento assistido por IA

[English](README.en.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

## Princípio e papéis

Usar IA para ampliar capacidade de pensar, aprender, construir e verificar, não para abandonar responsabilidade. ChatGPT pode apoiar conversa, tutoria, planejamento, pesquisa e redação. Codex pode inspecionar repos, implementar, testar e revisar quando disponível. Ambos podem errar de forma convincente. Ramon Rodriguez define estratégia, educação, edição e ativos visuais; IA apoia implementação e revisão; decisões finais são humanas. Estudantes não precisam de conta de IA nem plano pago.

## Estude manualmente primeiro

Tente exercício em repositório descartável primeiro. Preveja qual estado ou referência mudará, inspecione status/diff/histórico, execute um comando seguro e compare resultados. Se travar, peça uma dica, não solução completa. Exemplo: `Estou aprendendo staging. Dê uma dica para explicar por que um novo arquivo não está no próximo commit. Não forneça o comando até eu tentar.` Peça fontes oficiais e explique o resultado com suas palavras. Nunca execute comandos destrutivos sugeridos em projeto real. IA é opcional; fontes oficiais, prática e respostas de referência bastam.

## Da dúvida ao brief de implementação

Um prompt útil fornece contexto, objetivo, estado atual, escopo, restrições, saída esperada e validação. Refinar com perguntas, versão/SO e evidências; não esconder incerteza. Exemplo de brief: explicar criação de branch local a iniciantes; definir refs antes do uso; usar repo fictício descartável; fornecer EN/PT-BR/ES; sem remote real ou comandos destrutivos; verificar exemplos e links; relatar checks não executados; abrir PR focado da main atual. Estabelecer especificação, plano, tarefas e critérios antes da implementação; obter aprovação do escopo pelo mantenedor. Não presumir correção por prompt bem escrito.

## Verificação e revisão

Inspecionar cada arquivo alterado e escopo. Conferir fontes oficiais, pré-requisitos, avisos de segurança, terminologia, exemplos originais e significado entre idiomas. Testar estado Git real em diretórios descartáveis próprios, incluindo falhas representativas; registrar comando, ambiente e resultado. Verificar último SHA, CI e feedback do Codex quando disponíveis; solicitação não é review concluído. Tratar apontamentos, reexecutar checks e obter aprovação humana antes do squash merge. Nunca inventar resultados ou aprovar checks ausentes. Avaliação semântica por IA fora de escopo; preferir asserts de estado objetivos e autoavaliação.

## Privacidade, custos e independência

Nunca compartilhar repos privados não autorizados, processos de empregador/cliente, credenciais, tokens, dados pessoais, URLs privadas, código proprietário ou logs sensíveis com IA ou issues públicas. Anonimização superficial pode não bastar; criar exemplos fictícios originais. Disponibilidade, privacidade e limites mudam; consultar documentação oficial antes de depender de capacidade. Sem API paga, servidor, assinatura IA ou avaliação por IA obrigatória. Guia independente, sem endosso da OpenAI ou plataformas.

- [Constitution](../specs/constitution.pt-BR.md)
- [Autoria](../localized/AUTHORS.pt-BR.md)
- [Guia de contribuição](../localized/CONTRIBUTING.pt-BR.md)
- [Instruções](../localized/AGENTS.pt-BR.md)
