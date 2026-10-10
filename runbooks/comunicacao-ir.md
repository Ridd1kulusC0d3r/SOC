---
id: RB-09
type: runbook
level: "N2"
status: reference
review_cycle_days: 180
---

# RB-09 · Atualização de comunicação de incidente

## Quando usar
Incidente em curso ou atualização de status prevista.

## Pré-condições
- Ambiente e versão identificados; tenant validado.
- Acesso mínimo autorizado, ticket, responsabilidade e janela de mudança.
- Evidência original preservada e processo de reversão acordado.

## Procedimento
1. **Registrar:** executor, case/change ID, fonte, horário UTC e escopo.
2. **Verificar:** Confirmar nova evidência, escopo, impacto, limitações e mensagens prévias; seguir canal e cadência contratuais.
3. **Correlacionar:** confirmar por fonte independente, sem inferir que ausência de logs é ausência de ameaça.
4. **Documentar:** registrar resultados, outputs sanitizados, erros e limitações.
5. **Escalar:** atribuir pendências a responsável habilitado.

## Critério verificável de sucesso
Mensagem aprovada, factual, com carimbo UTC e responsável; próximo checkpoint definido.

## Falhas e reversão
Não incluir atribuição especulativa ou dados de outros clientes.

## Evidências geradas
Case ID, tenant, timestamp UTC, versão da ferramenta, evidência sanitizada, resultados e aprovação, se aplicável.

## Critérios para concluir
Resultado atingido ou impedimento documentado; novo responsável designado quando necessário; sem mudança não autorizada.
