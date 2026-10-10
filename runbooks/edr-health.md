---
id: RB-02
type: runbook
level: "N1"
status: reference
review_cycle_days: 180
---

# RB-02 · Saúde do agente EDR

## Quando usar
Heartbeat atrasado ou agente com falha.

## Pré-condições
- Ambiente e versão identificados; tenant validado.
- Acesso mínimo autorizado, ticket, responsabilidade e janela de mudança.
- Evidência original preservada e processo de reversão acordado.

## Procedimento
1. **Registrar:** executor, case/change ID, fonte, horário UTC e escopo.
2. **Verificar:** Comparar inventário, última conexão, versão, política, logs de comunicação e status do coletor.
3. **Correlacionar:** confirmar por fonte independente, sem inferir que ausência de logs é ausência de ameaça.
4. **Documentar:** registrar resultados, outputs sanitizados, erros e limitações.
5. **Escalar:** atribuir pendências a responsável habilitado.

## Critério verificável de sucesso
Heartbeat restaurado e telemetria de teste não maliciosa reconhecida.

## Falhas e reversão
Reinstalação ou alteração de política exige aprovação.

## Evidências geradas
Case ID, tenant, timestamp UTC, versão da ferramenta, evidência sanitizada, resultados e aprovação, se aplicável.

## Critérios para concluir
Resultado atingido ou impedimento documentado; novo responsável designado quando necessário; sem mudança não autorizada.
