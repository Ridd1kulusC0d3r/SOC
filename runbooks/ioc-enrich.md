---
id: RB-04
type: runbook
level: "N1"
status: reference
review_cycle_days: 180
---

# RB-04 · Enriquecer IOC com contexto

## Quando usar
Alertas possuem hash, domínio ou IP.

## Pré-condições
- Ambiente e versão identificados; tenant validado.
- Acesso mínimo autorizado, ticket, responsabilidade e janela de mudança.
- Evidência original preservada e processo de reversão acordado.

## Procedimento
1. **Registrar:** executor, case/change ID, fonte, horário UTC e escopo.
2. **Verificar:** Validar tipo, formato, data do indicador, provedor CTI, first/last seen e associação comportamental.
3. **Correlacionar:** confirmar por fonte independente, sem inferir que ausência de logs é ausência de ameaça.
4. **Documentar:** registrar resultados, outputs sanitizados, erros e limitações.
5. **Escalar:** atribuir pendências a responsável habilitado.

## Critério verificável de sucesso
Evidência de reputação separada de atribuição; fontes e confiança registradas.

## Falhas e reversão
Reputação isolada não autoriza bloqueio automático.

## Evidências geradas
Case ID, tenant, timestamp UTC, versão da ferramenta, evidência sanitizada, resultados e aprovação, se aplicável.

## Critérios para concluir
Resultado atingido ou impedimento documentado; novo responsável designado quando necessário; sem mudança não autorizada.
