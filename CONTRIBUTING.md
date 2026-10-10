# Contribuindo para SOC Academy & Operations

1. Abra uma issue com problema, impacto, nível, referências e proposta de validação.
2. Mantenha mudanças pequenas e explique por que o material existente não basta.
3. Artefatos nas pastas `tracks/`, `sop/`, `playbooks/`, `runbooks/` e `mssp/` devem conter: id, type, level, status e review_cycle_days.
4. Registre sempre entradas, decisões, evidências, erros, autorização, risco e condição de encerramento.
5. Não copie documentação ou datasets de terceiros sem licença compatível e atribuição; links e síntese autoral são preferíveis.
6. É proibida a publicação de PII, credenciais, tokens, casos reais não sanitizados e dados operacionais de clientes.
7. Rode `python3 scripts/validate_content.py` antes de abrir PR.

## Status editorial
- `reference`: guia documental ainda não validado em produção.
- `lab-tested`: testado em laboratório identificado com evidências sanitizadas.
- `production-reviewed`: revisão por responsável em ambiente e contrato específico, não certificado universal.

## Critérios de rejeição
Contenção sem autoridade, detecção sem fonte comprovada, conclusão sem evidência, conteúdo fora do escopo defensivo, uso de referência obsoleta sem ressalva e violações de privacidade.

Não atribuímos licença geral automaticamente. Contribuições devem respeitar direitos autorais e licenças aplicáveis.
