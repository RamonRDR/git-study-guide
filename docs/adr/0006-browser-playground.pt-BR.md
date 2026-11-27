# ADR 0006: Playground Git opcional no navegador

[English](0006-browser-playground.md) · [Português](0006-browser-playground.pt-BR.md) · [Español](0006-browser-playground.es.md)

Status: proposta na Sprint 18, avaliação documental em 27/11/2026; adoção de runtime adiada.

## Decisão

Manter todos projetos práticos e desafios nativos local_only. Outros capítulos permanecem unverified. Nenhuma capacidade browser_compatible, pacote, proxy público, servidor, versão runtime ou deploy aprovado. Ferramenta de navegador é opcional e não deve substituir referência Git nativa nem ser requisito de trilha.

## Alternativas

| Alternativa | Evidência e limites | Decisão |
| --- | --- | --- |
| Git nativo em repos locais descartáveis | Testes Linux/Windows existentes cobrem index, refs, conflitos, reflog, origens bare e recuperação reais. Sem UI navegador; aluno instala Git. | Referência |
| isomorphic-git | Implementação Git JavaScript com adaptadores de filesystem/HTTP navegador; APIs documentadas add, commit, branch, checkout, merge, cherry-pick, stash e tag. CLI não substitui CLI Git nativa; CORS e durabilidade filesystem restringem. Flags, semântica de estado e paridade de conflito/recuperação não verificadas. | Só candidato |
| wasm-git | libgit2 compilada com Emscripten; builds navegador documentados incluem worker e variantes de filesystem persistente. CORS, requisitos de armazenamento/navegador por build e implementação distinta da CLI Git limitam fidelidade. OPFS pthreads exige cabeçalhos de isolamento cross-origin. | Só candidato |
| Simulador educacional | Pode modelar pequena máquina de estados sem alegar Git nativo; exige regras originais explícitas, rótulo simulação e fixtures de comparação nativa. | Exploração futura opcional |
| Shell Git arbitrário hospedado | Introduz isolamento de execução, risco rede/segurança e custo recorrente incerto. | Rejeitado |

## Gates de protótipo antes de alterar capacidade

- Fixar versões exatas de pacote/runtime, licenças de dependências e hashes de integridade. Empacotar assets estáticos sem contas obrigatórias, proxies CORS públicos, infraestrutura paga ou API por visitante. Verificar limites reais hospedagem/banda antes de aprovação.
- Começar fixture pequena descartável offline e operações tipadas permitidas (init, status, add, commit, branch/checkout, diff). Comparar bytes working/index/HEAD e grafo/estado ao Git nativo; expandir só após testar conflitos, stash, revert, squash, reflog, tags e simulação bare-remoto local. Nunca inferir suporte de nomes de APIs. Operações não suportadas ficam local_only.
- Separar origens site/runtime quando necessário; CSP e mensagens restritas, sem credenciais, shell arbitrário, rede irrestrita ou acesso a repos valiosos. Web Worker melhora responsividade mas sozinho não é fronteira de segurança. Inspecionar supply chain e isolamento de origem.
- Limites propostos para teste, não garantias medidas: 5 s por operação, 64 KiB saída, 5 MiB fixture, 100 operações por sessão. Cancelar/terminar e recriar workers; sem alegar isolamento rígido de memória navegador. Testar quota, crash/reload, limpeza/reset; armazenamento pode ser descartado, portanto orientar exportação/reinício e persistência opt-in explícita.
- Verificar teclado, leitor de tela, erros localizados, contraste, foco, layout móvel, movimento reduzido e Chrome/Edge/Firefox/Safari nos dispositivos alvo. Testar offline, versões fixas, bloqueio CORS/rede, reset, limites tempo/saída e recuperação. Documentar resultados reais por exercício antes de marcar browser_compatible em versão futura.

## Consequências

Nenhum custo ou dependência nova introduzido aqui. Sem teste real de runtime/navegador ou alegação de compatibilidade; avaliação documental, não benchmark. Protótipo futuro no site exige autorização separada, fidelidade medida, revisão segurança/acessibilidade e confirmação custo adicional zero. Labs locais seguem completos sem ele.

## Fontes consultadas

- <https://github.com/isomorphic-git/isomorphic-git/blob/main/README.md>
- <https://isomorphic-git.org/docs/en/quickstart>
- <https://github.com/petersalomonsen/wasm-git/blob/master/README.md>
- <https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Using_web_workers>
- <https://developer.mozilla.org/en-US/docs/Web/API/Storage_API/Storage_quotas_and_eviction_criteria>
- <https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Same-origin_policy>
- <https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/sandbox>

- [Integration contract](../specs/project-foundation/integration-contract.pt-BR.md)
- [ADR index](README.pt-BR.md)
