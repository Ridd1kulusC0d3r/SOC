---
id: RB-05
type: runbook
level: "ENG"
status: reference
review_cycle_days: 180
---

# RB-05 · Revisar regra Sigma e tradução

## Quando usar
Mudança de detecção submetida à revisão.

## Pré-condições
- Ambiente e versão identificados; tenant validado.
- Acesso mínimo autorizado, ticket, responsabilidade e janela de mudança.
- Evidência original preservada e processo de reversão acordado.

## Procedimento
1. **Registrar:** executor, case/change ID, fonte, horário UTC e escopo.
2. **Verificar:** Validar versão da linguagem, campos, source, mapping, testes positivos/negativos e semântica da conversão ao backend.
3. **Correlacionar:** confirmar por fonte independente, sem inferir que ausência de logs é ausência de ameaça.
4. **Documentar:** registrar resultados, outputs sanitizados, erros e limitações.
5. **Escalar:** atribuir pendências a responsável habilitado.

## Critério verificável de sucesso
Teste de regressão reprodutível, taxa esperada de ruído documentada, owner e rollback.

## Falhas e reversão
Publicação direta sem revisão e change é proibida.

## Evidências geradas
Case ID, tenant, timestamp UTC, versão da ferramenta, evidência sanitizada, resultados e aprovação, se aplicável.

## Critérios para concluir
Resultado atingido ou impedimento documentado; novo responsável designado quando necessário; sem mudança não autorizada.
