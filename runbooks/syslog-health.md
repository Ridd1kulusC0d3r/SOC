---
id: RB-01
type: runbook
level: "N1"
status: reference
review_cycle_days: 180
---

# RB-01 · Diagnóstico de ingestão Syslog

## Quando usar
Alerta de ausência ou atraso de telemetria.

## Pré-condições
- Ambiente e versão identificados; tenant validado.
- Acesso mínimo autorizado, ticket, responsabilidade e janela de mudança.
- Evidência original preservada e processo de reversão acordado.

## Procedimento
1. **Registrar:** executor, case/change ID, fonte, horário UTC e escopo.
2. **Verificar:** Verificar última recepção, relógio UTC, status do coletor e fila; confrontar volume com baseline; pesquisar erros de parsing.
3. **Correlacionar:** confirmar por fonte independente, sem inferir que ausência de logs é ausência de ameaça.
4. **Documentar:** registrar resultados, outputs sanitizados, erros e limitações.
5. **Escalar:** atribuir pendências a responsável habilitado.

## Critério verificável de sucesso
Novo evento sintético autorizado aparece no SIEM com latência dentro do SLO.

## Falhas e reversão
Alterar rota, firewall ou parser requer change, owner e rollback.

## Evidências geradas
Case ID, tenant, timestamp UTC, versão da ferramenta, evidência sanitizada, resultados e aprovação, se aplicável.

## Critérios para concluir
Resultado atingido ou impedimento documentado; novo responsável designado quando necessário; sem mudança não autorizada.
