---
id: RB-06
type: runbook
level: "N1"
status: reference
review_cycle_days: 180
---

# RB-06 · Abrir e atribuir case

## Quando usar
Novo alerta qualificado requer acompanhamento.

## Pré-condições
- Ambiente e versão identificados; tenant validado.
- Acesso mínimo autorizado, ticket, responsabilidade e janela de mudança.
- Evidência original preservada e processo de reversão acordado.

## Procedimento
1. **Registrar:** executor, case/change ID, fonte, horário UTC e escopo.
2. **Verificar:** Abrir caso em tenant correto, indicar severidade, hipóteses, owner, prazos, eventos correlatos e evidência minimizada.
3. **Correlacionar:** confirmar por fonte independente, sem inferir que ausência de logs é ausência de ameaça.
4. **Documentar:** registrar resultados, outputs sanitizados, erros e limitações.
5. **Escalar:** atribuir pendências a responsável habilitado.

## Critério verificável de sucesso
Outro analista reproduz raciocínio e aceita handover sem canal paralelo.

## Falhas e reversão
Sem PII nem artefatos sensíveis em issues públicas.

## Evidências geradas
Case ID, tenant, timestamp UTC, versão da ferramenta, evidência sanitizada, resultados e aprovação, se aplicável.

## Critérios para concluir
Resultado atingido ou impedimento documentado; novo responsável designado quando necessário; sem mudança não autorizada.
