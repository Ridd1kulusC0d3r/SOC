---
id: RB-07
type: runbook
level: "N2"
status: reference
review_cycle_days: 180
---

# RB-07 · Construir timeline de investigação

## Quando usar
Múltiplas fontes do mesmo caso.

## Pré-condições
- Ambiente e versão identificados; tenant validado.
- Acesso mínimo autorizado, ticket, responsabilidade e janela de mudança.
- Evidência original preservada e processo de reversão acordado.

## Procedimento
1. **Registrar:** executor, case/change ID, fonte, horário UTC e escopo.
2. **Verificar:** Converter timestamps a UTC preservando timezone original, precisão, skew e IDs; correlacionar sem apagar evidência.
3. **Correlacionar:** confirmar por fonte independente, sem inferir que ausência de logs é ausência de ameaça.
4. **Documentar:** registrar resultados, outputs sanitizados, erros e limitações.
5. **Escalar:** atribuir pendências a responsável habilitado.

## Critério verificável de sucesso
Timeline ordenada, fontes referenciadas e lacunas explícitas.

## Falhas e reversão
Proximidade temporal não prova causalidade.

## Evidências geradas
Case ID, tenant, timestamp UTC, versão da ferramenta, evidência sanitizada, resultados e aprovação, se aplicável.

## Critérios para concluir
Resultado atingido ou impedimento documentado; novo responsável designado quando necessário; sem mudança não autorizada.
